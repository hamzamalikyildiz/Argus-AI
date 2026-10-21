import pytest
from unittest.mock import AsyncMock, patch, MagicMock

from src.state import AnalyzedArticle
from src.agents.reporter import (
    extract_text_content,
    clean_executive_summary,
    generate_executive_summary,
    synthesize_report,
)

SAMPLE_SIGNATURE = (
    "EtcjCtQjAWkUfRMehvIGygSWmkNz9Cd5F02QNuX6MfuPXzMLzRPu5CU7b4QuIvZ79ZJsRq1DwzZURWwvmWcp74HhOFUvS1kPamg"
)

def test_extract_text_content_plain_string():
    raw = "Bu bir test özetidir."
    assert extract_text_content(raw) == "Bu bir test özetidir."

def test_extract_text_content_gemini_list_with_signature():
    # Exact structure that caused the 2026-10-20 bug
    gemini_response_content = [
        {
            "type": "text",
            "text": "* **Model A:** 428B MoE duyuruldu.\n* **Model B:** Çıkarım hızında rekor.",
            "extras": {
                "signature": SAMPLE_SIGNATURE
            }
        }
    ]
    extracted = extract_text_content(gemini_response_content)
    assert "* **Model A:** 428B MoE duyuruldu." in extracted
    assert "signature" not in extracted
    assert SAMPLE_SIGNATURE not in extracted
    assert "{'type':" not in extracted

def test_extract_text_content_multiple_blocks():
    blocks = [
        {"type": "text", "text": "Birinci paragraf. "},
        {"type": "text", "text": "İkinci paragraf."}
    ]
    assert extract_text_content(blocks) == "Birinci paragraf. İkinci paragraf."

def test_extract_text_content_stringified_repr():
    # If python list was already stringified
    stringified = (
        "[{'type': 'text', 'text': 'Önemli gelişme.', 'extras': {'signature': '"
        + SAMPLE_SIGNATURE
        + "'}}]"
    )
    extracted = extract_text_content(stringified)
    assert extracted == "Önemli gelişme."
    assert "signature" not in extracted

def test_clean_executive_summary_removes_redundant_headers():
    raw_with_header = (
        "### Yönetici Özeti (TL;DR)\n\n"
        "* **Gelişme 1:** Açıklama.\n"
        "* **Gelişme 2:** Açıklama."
    )
    cleaned = clean_executive_summary(raw_with_header)
    assert not cleaned.startswith("### Yönetici Özeti")
    assert cleaned.startswith("* **Gelişme 1:**")

def test_clean_executive_summary_handles_embedded_signature_leak():
    leaked = (
        "* **Gelişme 1:** Açıklama.",
        "{'extras': {'signature': '" + SAMPLE_SIGNATURE + "'}}"
    )
    cleaned = clean_executive_summary(str(leaked))
    assert "signature" not in cleaned
    assert SAMPLE_SIGNATURE not in cleaned

@pytest.mark.asyncio
async def test_generate_executive_summary_with_mocked_gemini_response():
    articles = [
        AnalyzedArticle(
            title="Model Launch 1",
            source_url="https://example.com/1",
            key_takeaways=["Point 1", "Point 2"],
            technical_depth="Architecture details",
            why_it_matters="Developer impact"
        )
    ]

    mock_llm = MagicMock()
    # Mock chain returns AIMessage with content as list containing extras and signature
    mock_response = MagicMock()
    mock_response.content = [
        {
            "type": "text",
            "text": "### Yönetici Özeti (TL;DR)\n\n* **Model Launch 1:** Önemli takeaway.",
            "extras": {"signature": SAMPLE_SIGNATURE}
        }
    ]

    mock_chain = AsyncMock()
    mock_chain.ainvoke.return_value = mock_response

    with patch("src.agents.reporter.get_chat_model", return_value=mock_llm):
        with patch("src.agents.reporter.ChatPromptTemplate") as mock_prompt:
            mock_prompt.from_messages.return_value.__or__.return_value = mock_chain
            summary = await generate_executive_summary(articles)

    assert "Model Launch 1" in summary
    assert "### Yönetici Özeti" not in summary
    assert "signature" not in summary
    assert SAMPLE_SIGNATURE not in summary
    assert "{'type':" not in summary

@pytest.mark.asyncio
async def test_synthesize_report_contains_no_leaks():
    articles = [
        AnalyzedArticle(
            title="Diffusion LLM Mercury",
            source_url="https://arxiv.org/abs/2610.12345",
            key_takeaways=["1068 tokens/sec"],
            technical_depth="Diffusion architecture replacing autoregressive models",
            why_it_matters="Huge compute efficiency"
        )
    ]

    with patch(
        "src.agents.reporter.generate_executive_summary",
        new=AsyncMock(return_value="* **Mercury 3:** 1068 token/s difüzyon modeli.")
    ):
        report_md = await synthesize_report(articles, "2026-10-22")

    assert "# 🤖 Yapay Zeka Günlük İstihbarat Bülteni — 2026-10-22" in report_md
    assert "## ⚡ Yönetici Özeti (TL;DR)" in report_md
    assert "* **Mercury 3:** 1068 token/s difüzyon modeli." in report_md
    assert "signature" not in report_md
    assert "extras" not in report_md
    assert "{'type':" not in report_md
