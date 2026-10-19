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
    )
}

def extract_article_content(url: str, timeout: float = 12.0) -> Optional[str]:
    """
    Downloads and extracts clean article text and structure from a URL using Trafilatura.
    Fails safely without raising exceptions.
    """
    if not url or not url.startswith("http") or not httpx or not trafilatura:
        return None

    try:
        # First attempt with httpx to respect custom headers and timeouts
        with httpx.Client(timeout=timeout, follow_redirects=True, headers=HEADERS) as client:
            resp = client.get(url)
            if resp.status_code == 200:
                html = resp.text
                extracted = trafilatura.extract(
                    html,
                    include_links=True,
                    include_formatting=True,
                    include_comments=False,
                    no_fallback=False
                )
                if extracted and len(extracted.strip()) > 100:
                    return extracted.strip()

        # Fallback directly to trafilatura's native fetcher if needed
        downloaded = trafilatura.fetch_url(url)
        if downloaded:
            extracted = trafilatura.extract(downloaded, include_links=True, include_formatting=True)
            if extracted and len(extracted.strip()) > 100:
                return extracted.strip()

    except Exception as e:
        logger.warning(f"Failed to scrape content from {url}: {e}")

    return None
