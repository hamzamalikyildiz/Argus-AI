"""Web scraper tool using Trafilatura for extracting full clean markdown/text content."""
import logging
from typing import Optional

try:
    import httpx
except ImportError:
    httpx = None

try:
    import trafilatura
except ImportError:
    trafilatura = None

logger = logging.getLogger(__name__)

HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/124.0.0.0 Safari/537.36 AI-Intelligence-Bot/1.0"
    ),
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
}

def extract_article_content(url: str, timeout: float = 8.0) -> Optional[str]:
    """
    Downloads and extracts clean article text and structure from a URL using Trafilatura.
    Fails safely and quickly without blocking or hanging.
    """
    if not url or not url.startswith("http") or not httpx or not trafilatura:
        return None

    try:
        with httpx.Client(timeout=timeout, follow_redirects=True, headers=HEADERS) as client:
            resp = client.get(url)
            if resp.status_code == 200 and resp.text:
                extracted = trafilatura.extract(
                    resp.text,
                    include_links=True,
                    include_formatting=True,
                    include_comments=False,
                    no_fallback=False
                )
                if extracted and len(extracted.strip()) > 100:
                    return extracted.strip()
    except Exception as e:
        logger.debug(f"Web scraper notice for {url}: {e}")

    return None
