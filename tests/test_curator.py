import pytest
pytest.importorskip("langchain_core")
from unittest.mock import AsyncMock, patch
from src.state import RawArticle
from src.agents.curator import curate_articles, BatchScoreResult, ArticleScore

@pytest.mark.asyncio
async def test_curator_smart_fallback(monkeypatch):
    from config.settings import settings
    monkeypatch.setattr(settings, "min_relevance_score", 7)
    monkeypatch.setattr(settings, "max_curated_articles", 5)

    raw_articles = [
        RawArticle(id=f"id-{i}", title=f"News {i}", source="Feed", url=f"https://example.com/{i}", published_at="2026-10-19T10:00:00Z", summary=f"Summary {i}")
        for i in range(5)
    ]

    # Mock LLM scores all below 7 (e.g. 5 and 6)
    mock_evals = [
        ArticleScore(id="id-0", relevance_score=6, reasoning="Decent", category="Industry"),
        ArticleScore(id="id-1", relevance_score=5, reasoning="Fair", category="Tooling"),
        ArticleScore(id="id-2", relevance_score=6, reasoning="Decent update", category="Research"),
        ArticleScore(id="id-3", relevance_score=4, reasoning="Low", category="Industry"),
        ArticleScore(id="id-4", relevance_score=3, reasoning="Hype", category="Industry"),
    ]

    mock_chain = AsyncMock()
    mock_chain.ainvoke.return_value = BatchScoreResult(evaluations=mock_evals)

    with patch("src.agents.curator.get_chat_model") as mock_get_model:
        mock_llm = AsyncMock()
        mock_get_model.return_value = mock_llm
        with patch("src.agents.curator.ChatPromptTemplate") as mock_prompt:
            mock_prompt.from_messages.return_value.__or__.return_value = mock_chain
            curated = await curate_articles(raw_articles)

    # Should activate fallback and take top available items (scores 6, 6, 5)
    assert len(curated) >= 3
    assert all(item.relevance_score >= 5 for item in curated)
    assert curated[0].relevance_score == 6


@pytest.mark.asyncio
async def test_curator_raises_on_all_batches_failed():
    raw_articles = [
        RawArticle(id=f"id-{i}", title=f"News {i}", source="Feed", url=f"https://example.com/{i}", published_at="2026-10-19T10:00:00Z", summary=f"Summary {i}")
        for i in range(3)
    ]

    mock_chain = AsyncMock()
    mock_chain.ainvoke.side_effect = Exception("404 NOT_FOUND. Model is no longer available.")

    with patch("src.agents.curator.get_chat_model") as mock_get_model:
        mock_llm = AsyncMock()
        mock_get_model.return_value = mock_llm
        with patch("src.agents.curator.ChatPromptTemplate") as mock_prompt:
            mock_prompt.from_messages.return_value.__or__.return_value = mock_chain
            with pytest.raises(RuntimeError) as exc_info:
                await curate_articles(raw_articles)
            assert "Curator Agent failed: All" in str(exc_info.value)
            assert "404 NOT_FOUND" in str(exc_info.value)


def test_llm_factory_gemini_model_mapping(monkeypatch):
    import sys
    from unittest.mock import MagicMock
    from src.agents.llm_factory import get_chat_model
    from config.settings import settings

    monkeypatch.setattr(settings, "llm_provider", "gemini")
    monkeypatch.setattr(settings, "gemini_api_key", "test-fake-key")

    mock_chat = MagicMock()
    mock_module = MagicMock()
    mock_module.ChatGoogleGenerativeAI = mock_chat

    with patch.dict(sys.modules, {"langchain_google_genai": mock_module}):
        # Test deprecated model is automatically remapped
        monkeypatch.setattr(settings, "curator_model", "gemini-2.0-flash")
        get_chat_model(role="curator")
        mock_chat.assert_called_with(
            model="gemini-3.8-flash",
            google_api_key="test-fake-key",
            temperature=0.2
        )

        # Test another deprecated alias
        monkeypatch.setattr(settings, "analyst_model", "gemini-pro")
        get_chat_model(role="analyst")
        mock_chat.assert_called_with(
            model="gemini-3.8-flash",
            google_api_key="test-fake-key",
            temperature=0.2
        )

        # Test active model remains untouched
        monkeypatch.setattr(settings, "curator_model", "gemini-3.8-flash")
        get_chat_model(role="curator")
        mock_chat.assert_called_with(
            model="gemini-3.8-flash",
            google_api_key="test-fake-key",
            temperature=0.2
        )

