"""Async RSS collector with 24-hour time-window filtering and deduplication."""
import asyncio
import hashlib
import logging
from datetime import datetime, timezone, timedelta
from typing import List, Dict, Any, Optional
import feedparser
import httpx
import dateparser

from src.state import RawArticle
from config.settings import settings

logger = logging.getLogger(__name__)

HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/124.0.0.0 Safari/537.36 AI-Intelligence-Bot/1.0"
    )
}

def generate_article_id(url: str, title: str) -> str:
    """Generates a stable unique hash id from title and normalized url."""
    norm = f"{url.strip().lower()}|{title.strip().lower()}"
    return hashlib.sha256(norm.encode("utf-8")).hexdigest()[:16]

def parse_published_date(entry: Dict[str, Any]) -> Optional[datetime]:
    """Extracts and normalizes publication datetime from feed entry to UTC."""
    for field in ["published", "updated", "pubDate", "created"]:
        raw_val = entry.get(field)
        if raw_val:
            try:
                dt = dateparser.parse(
                    str(raw_val),
                    settings={"RETURN_AS_TIMEZONE_AWARE": True, "TIMEZONE": "UTC"}
                )
                if dt:
                    return dt.astimezone(timezone.utc)
            except Exception:
                pass
    
    # Try parsed structs if available
    for struct_field in ["published_parsed", "updated_parsed"]:
        parsed_tuple = entry.get(struct_field)
        if parsed_tuple:
            try:
                return datetime(*parsed_tuple[:6], tzinfo=timezone.utc)
            except Exception:
                pass

    return None

async def fetch_single_feed(
    client: httpx.AsyncClient,
    feed_config: Dict[str, str],
    cutoff_time: datetime,
    max_items: int
) -> List[RawArticle]:
    """Fetches and parses a single RSS feed asynchronously."""
    source_name = feed_config.get("name", "Unknown RSS")
    url = feed_config.get("url", "")
    if not url:
        return []

    articles: List[RawArticle] = []
    try:
        response = await client.get(url, headers=HEADERS, timeout=12.0)
        if response.status_code != 200:
            logger.warning(f"RSS source {source_name} returned HTTP {response.status_code}")
            return []

        parsed = feedparser.parse(response.content)
        count = 0

        for entry in parsed.entries:
            if count >= max_items:
                break

            title = entry.get("title", "").strip()
            link = entry.get("link", "").strip()
            if not title or not link:
                continue

            summary = entry.get("summary") or entry.get("description") or ""
            # Strip simple html tags from summary if needed
            if summary:
                import re
                summary = re.sub(r"<[^>]+>", " ", summary).strip()
                summary = " ".join(summary.split())[:1200]

            pub_date = parse_published_date(entry)
            
            # If publication date exists, check cutoff. If missing, allow recent items at feed head
            if pub_date and pub_date < cutoff_time:
                continue

            pub_str = pub_date.isoformat() if pub_date else datetime.now(timezone.utc).isoformat()
            article_id = generate_article_id(link, title)

            articles.append(
                RawArticle(
                    id=article_id,
                    title=title,
                    source=source_name,
                    url=link,
                    published_at=pub_str,
                    summary=summary or title
                )
            )
            count += 1

    except Exception as e:
        logger.error(f"Error fetching RSS source '{source_name}' ({url}): {e}")

    return articles

async def collect_all_rss() -> List[RawArticle]:
    """Asynchronously fetches all configured RSS feeds in parallel."""
    config = settings.load_sources_config()
    rss_list = config.get("rss_feeds", [])
    if not rss_list:
        logger.info("No RSS feeds configured in sources.yaml.")
        return []

    cutoff_time = datetime.now(timezone.utc) - timedelta(hours=settings.max_hours_old)
    max_items = settings.max_articles_per_source

    async with httpx.AsyncClient(timeout=15.0, follow_redirects=True) as client:
        tasks = [
            fetch_single_feed(client, feed, cutoff_time, max_items)
            for feed in rss_list
        ]
        results = await asyncio.gather(*tasks, return_exceptions=True)

    all_articles: List[RawArticle] = []
    seen_ids = set()

    for res in results:
        if isinstance(res, list):
            for article in res:
                if article.id not in seen_ids:
                    seen_ids.add(article.id)
                    all_articles.append(article)
        elif isinstance(res, Exception):
            logger.error(f"Feed task raised exception: {res}")

    logger.info(f"Ingested {len(all_articles)} unique articles from RSS feeds.")
    return all_articles
