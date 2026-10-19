from src.tools.web_scraper import extract_article_content

def test_scraper_invalid_url():
    result = extract_article_content("invalid-url-string")
    assert result is None

def test_scraper_empty_url():
    result = extract_article_content("")
    assert result is None
