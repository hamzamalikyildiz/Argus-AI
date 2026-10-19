"""Async ArXiv API collector with date filtering and deduplication."""
import asyncio
import hashlib
import logging
import re
from datetime import datetime, timezone, timedelta
from typing import List, Dict, Any, Optional
import feedparser
import httpx
import dateparser

from src.state import RawArticle
from config.settings import settings

logger = logging.getLogger(__name__)

ARXIV_API_URL = "https://export.arxiv.org/api/query"

def generate_paper_id(url: str, title: str) -> str:
    norm = f"{url.strip().lower()}|{title.strip().lower()}"
    return hashlib.sha256(norm.encode("utf-8")).hexdigest()[:16]

def parse_arxiv_date(entry: Dict[str, Any]) -> Optional[datetime]:
    for field in ["published", "updated"]:
        val = entry.get(field)
        if val:
            try:
                dt = dateparser.parse(
                    str(val),
                    settings={"RETURN_AS_TIMEZONE_AWARE": True, "TIMEZONE": "UTC"}
                )
                if dt:
                    return dt.astimezone(timezone.utc)
            except Exception:
                pass
    return None

async def fetch_arxiv_category(
    client: httpx.AsyncClient,
    category: str,
    cutoff_time: datetime,
    max_results: int
) -> List[RawArticle]:
    """Queries ArXiv API for a specific category."""
    params = {
        "search_query": f"cat:{category}",
        "sortBy": "submittedDate",
        "sortOrder": "descending",
        "max_results": max_results
    }

    articles: List[RawArticle] = []
    try:
        resp = await client.get(ARXIV_API_URL, params=params, timeout=15.0)
        if resp.status_code != 200:
            logger.warning(f"ArXiv query for {category} returned HTTP {resp.status_code}")
            return []

        feed = feedparser.parse(resp.content)
        for entry in feed.entries:
            title = entry.get("title", "").replace("\n", " ").strip()
            title = re.sub(r"\s+", " ", title)
            link = entry.get("id", "").strip()
            summary = entry.get("summary", "").replace("\n", " ").strip()
            summary = re.sub(r"\s+", " ", summary)

            if not title or not link:
                continue

            pub_date = parse_arxiv_date(entry)
            # ArXiv announcement delays: allow up to 48 hours for weekend/review schedules
            effective_cutoff = cutoff_time - timedelta(hours=24)
            if pub_date and pub_date < effective_cutoff:
                continue

            pub_str = pub_date.isoformat() if pub_date else datetime.now(timezone.utc).isoformat()
            paper_id = generate_paper_id(link, title)

            articles.append(
                RawArticle(
                    id=paper_id,
                    title=f"[ArXiv] {title}",
                    source=f"ArXiv ({category})",
                    url=link,
                    published_at=pub_str,
                    summary=summary[:1500]
                )
            )

    except Exception as e:
        logger.error(f"Error querying ArXiv for category '{category}': {e}")

    return articles

async def collect_all_arxiv() -> List[RawArticle]:
    """Queries ArXiv API across all configured categories with rate-politeness."""
    config = settings.load_sources_config()
    arxiv_config = config.get("arxiv", {})
    categories = arxiv_config.get("categories", ["cs.AI", "cs.LG", "cs.CL"])
    max_per_cat = arxiv_config.get("max_results_per_category", 6)

    cutoff_time = datetime.now(timezone.utc) - timedelta(hours=settings.max_hours_old)
    all_papers: List[RawArticle] = []
    seen_ids = set()

    headers = {
        "User-Agent": "AI-Intelligence-Bot/1.0 (academic research daily brief; contact: action@github.com)"
    }

    async with httpx.AsyncClient(timeout=20.0, headers=headers) as client:
        for idx, cat in enumerate(categories):
            if idx > 0:
                # ArXiv polite rate-limit delay
                await asyncio.sleep(2.0)
            papers = await fetch_arxiv_category(client, cat, cutoff_time, max_per_cat)
            for paper in papers:
                if paper.id not in seen_ids:
                    seen_ids.add(paper.id)
                    all_papers.append(paper)

    logger.info(f"Ingested {len(all_papers)} unique papers from ArXiv.")
    return all_papers
