"""Reporter Agent: Synthesizes analyzed articles into a structured, executive-grade Markdown daily brief."""
import logging
from typing import List
from datetime import datetime, timezone
from langchain_core.prompts import ChatPromptTemplate

from src.state import AnalyzedArticle
from src.agents.llm_factory import get_chat_model
from config.settings import settings

logger = logging.getLogger(__name__)

REPORTER_SYSTEM_PROMPT = """You are an Executive Editor for a top-tier Artificial Intelligence intelligence brief.
Your task is to take analyzed technical articles and synthesize the "Executive Summary (TL;DR)" section.

Requirements:
1. Provide the TOP 3 most impactful takeaways of the entire day in concise, punchy bullet points.
2. Emphasize why engineers and leaders should care (implications for infrastructure, open-weights, and compute).
3. Do NOT invent new facts or external URLs.
4. Language: Write strictly in {language_name} ({language_code}).
"""

async def generate_executive_summary(analyzed: List[AnalyzedArticle]) -> str:
    """Generates the executive TL;DR for the daily report using LLM."""
    if not analyzed:
        return "- Bugün için filtrelenen kriterlere uygun kritik bir gelişme kaydedilmedi." if settings.report_language == "tr" else "- No critical developments met the threshold today."

    llm = get_chat_model(role="curator", temperature=0.2)
    prompt = ChatPromptTemplate.from_messages([
        ("system", REPORTER_SYSTEM_PROMPT),
        ("human", "Analyzed articles of today:\n\n{articles_summary}\n\nGenerate the Top 3 Executive Takeaways:")
    ])

    articles_summary = "\n\n".join([
        f"Title: {a.title}\nKey Takeaways: {', '.join(a.key_takeaways)}\nWhy it matters: {a.why_it_matters}"
        for a in analyzed
    ])

    lang_name = "Turkish" if settings.report_language == "tr" else "English"
    chain = prompt | llm

    try:
        response = await chain.ainvoke({
            "language_name": lang_name,
            "language_code": settings.report_language,
            "articles_summary": articles_summary
        })
        return str(response.content).strip()
    except Exception as e:
        logger.error(f"Failed to generate executive summary: {e}")
        # Deterministic fallback
        bullets = [f"- **{a.title}**: {a.key_takeaways[0] if a.key_takeaways else a.why_it_matters}" for a in analyzed[:3]]
        return "\n".join(bullets)

async def synthesize_report(analyzed_articles: List[AnalyzedArticle], report_date: str) -> str:
    """Compiles the full Markdown report according to design specifications."""
    is_tr = settings.report_language == "tr"

    # Generate executive summary
    exec_summary = await generate_executive_summary(analyzed_articles)

    # Separate into research vs tooling/releases
    research_items = [a for a in analyzed_articles if "arxiv" in a.source_url.lower() or "research" in a.title.lower()]
    tooling_items = [a for a in analyzed_articles if a not in research_items]

    # If all ended up in one, balance them
    if not research_items and tooling_items:
        research_items = tooling_items[:len(tooling_items)//2]
        tooling_items = tooling_items[len(tooling_items)//2:]

    def format_article_section(art: AnalyzedArticle) -> str:
        takeaways_md = "\n".join([f"  - {t}" for t in art.key_takeaways])
        tech_label = "Teknik Derinlik & Mimari" if is_tr else "Technical Depth & Architecture"
        impact_label = "Sektörel Etki & Anlamı" if is_tr else "Why It Matters"
        source_label = "Kaynak Bağlantısı" if is_tr else "Source Link"

        return f"""### [{art.title}]({art.source_url})
**Öne Çıkanlar:**
{takeaways_md}

**{tech_label}:**
{art.technical_depth}

**{impact_label}:**
{art.why_it_matters}

📎 *{source_label}:* [{art.source_url}]({art.source_url})
"""

    research_md = "\n---\n\n".join([format_article_section(a) for a in research_items]) if research_items else (
        "_Bugün öne çıkan akademik araştırma makalesi bulunmamaktadır._" if is_tr else "_No standout academic research papers recorded today._"
    )

    tooling_md = "\n---\n\n".join([format_article_section(a) for a in tooling_items]) if tooling_items else (
        "_Bugün öne çıkan araç/model sürümü bulunmamaktadır._" if is_tr else "_No standout tooling or model releases recorded today._"
    )

    # Source directory table
    source_table_header = (
        "| # | Başlık | Kaynak | Doğrudan Link |\n|---|---|---|---|\n"
        if is_tr else
        "| # | Title | Source | Direct Link |\n|---|---|---|---|\n"
    )
    source_rows = []
    for idx, a in enumerate(analyzed_articles, 1):
        source_domain = a.source_url.split("/")[2] if "://" in a.source_url else "Web"
        clean_title = a.title.replace("|", "-")
        source_rows.append(f"| {idx} | {clean_title} | `{source_domain}` | [İncele]({a.source_url}) |")

    sources_table = source_table_header + "\n".join(source_rows) if source_rows else "_Kayıt yok._"

    # Assemble report
    title_header = (
        f"# 🤖 Yapay Zeka Günlük İstihbarat Bülteni — {report_date}"
        if is_tr else
        f"# 🤖 AI Intelligence Daily Brief — {report_date}"
    )

    badge = f"> 📅 **Tarih:** {report_date} | 🌐 **Dil:** {'Türkçe' if is_tr else 'English'} | ⚡ **Durum:** Otomatik Raporlandı\n\n"

    report_content = f"""{title_header}

{badge}## ⚡ {'Yönetici Özeti (TL;DR)' if is_tr else 'Executive Summary (TL;DR)'}
{exec_summary}

---

## 🔬 {'Araştırma ve Çığır Açan Gelişmeler (Research & Breakthroughs)' if is_tr else 'Research & Breakthroughs'}
{research_md}

---

## 🛠️ {'Araçlar, Modeller ve Açık Kaynak (Tooling, Frameworks & Releases)' if is_tr else 'Tooling, Frameworks & Releases'}
{tooling_md}

---

## 📚 {'Kaynak Rehberi ve Orijinal Bağlantılar' if is_tr else 'Source Directory'}
{sources_table}

---
*Bu rapor LangGraph ve AI Multi-Agent StateGraph mimarisi ile her sabah otomatik olarak üretilmektedir.*
"""
    return report_content
