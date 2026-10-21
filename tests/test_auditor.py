import pytest
from pathlib import Path
from src.agents.auditor import (
    audit_report_content,
    audit_report_file,
    check_leaks_and_auto_heal,
    check_markdown_structure,
    check_links_and_tables,
    audit_node,
)
from src.state import PipelineState

SAMPLE_VALID_REPORT = """# 🤖 Yapay Zeka Günlük İstihbarat Bülteni — 2026-10-21

> 📅 **Tarih:** 2026-10-21 | 🌐 **Dil:** Türkçe | ⚡ **Durum:** Otomatik Raporlandı

## ⚡ Yönetici Özeti (TL;DR)
* **Mistral Voxtral 3:** Konuşma ve ses agent SDK'sı yayınlandı.
* **Google TorchTPU:** Cloud TPU için PyTorch backend'i açık kaynak yapıldı.
* **Large Flow LLMs:** Difüzyon akış modelleri ile yeni çıkarım rekoru.

---

## 🔬 Araştırma ve Çığır Açan Gelişmeler (Research & Breakthroughs)
### [[ArXiv] Large Flow Language Models](http://arxiv.org/abs/2610.28559v1)
**Öne Çıkanlar:**
  - Continuous flow language models offer a path to parallel generation.

**Teknik Derinlik & Mimari:**
Detaylı mimari analizi.

**Sektörel Etki & Anlamı:**
Research kategorisinde önemli bir gelişme.

📎 *Kaynak Bağlantısı:* [http://arxiv.org/abs/2610.28559v1](http://arxiv.org/abs/2610.28559v1)

---

## 🛠️ Araçlar, Modeller ve Açık Kaynak (Tooling, Frameworks & Releases)
### [Voxtral 3](https://mistral.ai)
**Öne Çıkanlar:**
  - Ses agent SDK'sı.

**Teknik Derinlik & Mimari:**
Mimari detaylar.

**Sektörel Etki & Anlamı:**
Tooling kategorisinde önemli bir gelişme.

📎 *Kaynak Bağlantısı:* [https://mistral.ai](https://mistral.ai)

---

## 📚 Kaynak Rehberi ve Orijinal Bağlantılar
| # | Başlık | Kaynak | Doğrudan Link |
|---|---|---|---|
| 1 | Large Flow Language Models | `arxiv.org` | [İncele](http://arxiv.org/abs/2610.28559v1) |

---
*Bu rapor LangGraph ve AI Multi-Agent StateGraph mimarisi ile her sabah otomatik olarak üretilmektedir.*
"""

def test_audit_valid_report():
    result = audit_report_content(SAMPLE_VALID_REPORT, auto_heal=True)
    assert result.is_valid is True
    assert len(result.fixes_applied) == 0

def test_audit_auto_heals_leaked_dictionary_and_signature():
    corrupted_report = SAMPLE_VALID_REPORT.replace(
        "## ⚡ Yönetici Özeti (TL;DR)\n* **Mistral Voxtral 3:**",
        """## ⚡ Yönetici Özeti (TL;DR)
[{'type': 'text', 'text': "* **Mistral Voxtral 3:** Konuşma modeli.", 'extras': {'signature': 'EtcjCtQjAWkUfRMehvIGygSWmkNz9Cd5F02QNuX6MfuPXzMLzRPu5CU7b4QuIvZ79ZJsRq1DwzZURWwvmWcp74HhOFUvS1kPamg'}}]
* **Google TorchTPU:**"""
    )

    result = audit_report_content(corrupted_report, auto_heal=True)
    assert result.is_valid is True
    assert len(result.issues_found) >= 1
    assert any("Leaked" in issue for issue in result.issues_found)
    assert len(result.fixes_applied) >= 1
    assert "signature" not in result.cleaned_report_md
    assert "extras" not in result.cleaned_report_md
    assert "{'type':" not in result.cleaned_report_md
    assert "* **Mistral Voxtral 3:** Konuşma modeli." in result.cleaned_report_md

def test_audit_auto_heals_duplicate_header():
    corrupted = SAMPLE_VALID_REPORT.replace(
        "## ⚡ Yönetici Özeti (TL;DR)\n",
        "## ⚡ Yönetici Özeti (TL;DR)\n\n### Yönetici Özeti (TL;DR)\n\n"
    )
    result = audit_report_content(corrupted, auto_heal=True)
    assert result.is_valid is True
    assert "Removed duplicate executive summary subheader" in result.fixes_applied
    assert "### Yönetici Özeti (TL;DR)" not in result.cleaned_report_md

def test_audit_flags_missing_sections():
    truncated = "# 🤖 AI Brief\n\nSome text but no sections."
    result = audit_report_content(truncated, auto_heal=False)
    assert result.is_valid is False
    assert any("Missing required section" in issue for issue in result.issues_found)

def test_audit_report_file_in_place(tmp_path: Path):
    corrupted_file = tmp_path / "test-brief.md"
    corrupted_file.write_text(
        SAMPLE_VALID_REPORT.replace(
            "## ⚡ Yönetici Özeti (TL;DR)\n",
            "## ⚡ Yönetici Özeti (TL;DR)\n\n### Yönetici Özeti (TL;DR)\n\n"
        ),
        encoding="utf-8"
    )

    result = audit_report_file(corrupted_file, auto_heal=True)
    assert result.is_valid is True
    assert len(result.fixes_applied) >= 1

    # Verify file was modified in-place
    saved_text = corrupted_file.read_text(encoding="utf-8")
    assert "### Yönetici Özeti (TL;DR)" not in saved_text

@pytest.mark.asyncio
async def test_audit_node_integration():
    state: PipelineState = {
        "raw_articles": [],
        "curated_articles": [],
        "analyzed_articles": [],
        "final_report_md": SAMPLE_VALID_REPORT,
        "report_date": "2026-10-21",
        "report_file_path": ""
    }

    result_state = await audit_node(state)
    assert result_state["audit_passed"] is True
    assert result_state["final_report_md"] == SAMPLE_VALID_REPORT
