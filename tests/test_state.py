import pytest
from src.state import RawArticle, CuratedArticle, AnalyzedArticle

def test_raw_article_creation():
    article = RawArticle(
        id="test-id-123",
        title="DeepSeek-V3 Architecture Released",
        source="Hacker News",
        url="https://example.com/deepseek-v3",
        published_at="2026-10-19T10:00:00Z",
        summary="A breakthrough MoE model."
    )
    assert article.id == "test-id-123"
    assert article.title == "DeepSeek-V3 Architecture Released"
    assert article.url == "https://example.com/deepseek-v3"

def test_curated_article_validation():
    raw = RawArticle(
        id="test-id-123",
        title="Test Title",
        source="ArXiv",
        url="https://arxiv.org/abs/2610.12345",
        published_at="2026-10-19T10:00:00Z",
        summary="Summary"
    )
    curated = CuratedArticle(
        raw=raw,
        relevance_score=9,
        reasoning="Groundbreaking architectural novelties.",
        category="Research"
    )
    assert curated.relevance_score == 9
    assert curated.category == "Research"

def test_analyzed_article_creation():
    analyzed = AnalyzedArticle(
        title="Llama-4 Scaled MoE",
        source_url="https://ai.meta.com/llama4",
        key_takeaways=["Multi-head latent attention", "128 experts"],
        technical_depth="Detailed architectural analysis of sparse computation.",
        why_it_matters="Massive jump for open weights."
    )
    assert len(analyzed.key_takeaways) == 2
    assert analyzed.source_url == "https://ai.meta.com/llama4"
