"""Deep Analyst Agent: Performs full-text web scraping and deep technical analysis."""
import asyncio
import logging
from typing import List
from pydantic import BaseModel, Field
from langchain_core.prompts import ChatPromptTemplate

from src.state import CuratedArticle, AnalyzedArticle
from src.tools.web_scraper import extract_article_content
from src.agents.llm_factory import get_chat_model
from config.settings import settings

logger = logging.getLogger(__name__)

class ArticleAnalysisOutput(BaseModel):
    title: str = Field(..., description="Clear, concise headline of the technical development")
    key_takeaways: List[str] = Field(..., description="3-5 concrete technical facts, benchmarks, or architectural features")
    technical_depth: str = Field(..., description="Deep dive into algorithmic changes, neural architecture, hardware requirements, or benchmarks")
    why_it_matters: str = Field(..., description="Strategic significance for engineers, researchers, and the open-source community")

ANALYST_SYSTEM_PROMPT = """You are a Principal AI Architect and Deep Learning Researcher.
Your job is to provide rigorous, highly technical analysis of newly released AI developments, papers, and models.

Strict Guardrails:
1. Grounded Analysis: Rely strictly on the provided article text, abstract, or scraped webpage. Do NOT invent fake metrics, benchmarks, or architectures.
2. Technical Depth:
   - What is the algorithmic or architectural innovation (e.g., Attention mechanism, MoE routing, KV-cache compression, RLHF / DPO method)?
   - Are there specific benchmarks reported (e.g. MMLU, GSM8k, SWE-bench, tokens/sec)?
   - Is open-source code or model weights available?
3. Target Language: {language_instruction}
"""

LANGUAGE_INSTRUCTIONS = {
    "tr": "Analizinizi profesyonel, akıcı ve teknik terimleri yerinde kullanan bir Türkçe ile yazın (Mimari, benchmark, çıkarım maliyeti gibi kavramları koruyarak).",
    "en": "Write the analysis in professional, fluent, and rigorous technical English."
}

async def analyze_single_article(curated: CuratedArticle, analyst_chain) -> AnalyzedArticle:
    """Extracts full web content and performs deep technical analysis for a single article."""
    raw = curated.raw
    url = raw.url
    logger.info(f"Analyzing article: '{raw.title}' from {url}")

    # Proactively scrape web content to prevent hallucinations
    full_content = None
    try:
        # Run synchronous web scraper in thread pool to keep event loop responsive
        full_content = await asyncio.to_thread(extract_article_content, url)
    except Exception as e:
        logger.warning(f"Could not scrape {url}: {e}")

    content_to_analyze = full_content if full_content else raw.summary
    # Truncate content to avoid exceeding context window limits while preserving richness
    content_to_analyze = content_to_analyze[:12000]

    lang = settings.report_language
    lang_inst = LANGUAGE_INSTRUCTIONS.get(lang, LANGUAGE_INSTRUCTIONS["tr"])

    try:
        output: ArticleAnalysisOutput = await analyst_chain.ainvoke({
            "language_instruction": lang_inst,
            "article_title": raw.title,
            "source_name": raw.source,
            "article_category": curated.category,
            "article_content": content_to_analyze
        })

        return AnalyzedArticle(
            title=output.title or raw.title,
            source_url=raw.url,  # ZERO HALLUCINATION: guaranteed raw URL
            key_takeaways=output.key_takeaways,
            technical_depth=output.technical_depth,
            why_it_matters=output.why_it_matters
        )
    except Exception as e:
        logger.error(f"Failed deep analysis for '{raw.title}': {e}")
        # Fallback to safe summary structure if LLM error occurs
        fallback_takeaways = [raw.summary[:200]] if raw.summary else ["Ayrıntılı özet mevcut değil."]
        return AnalyzedArticle(
            title=raw.title,
            source_url=raw.url,
            key_takeaways=fallback_takeaways,
            technical_depth=raw.summary or "Teknik detay bulunamadı.",
            why_it_matters=f"{curated.category} kategorisinde önemli bir gelişme."
        )

async def analyze_articles(curated_articles: List[CuratedArticle]) -> List[AnalyzedArticle]:
    """Runs deep technical analysis across all curated articles."""
    if not curated_articles:
        logger.info("No curated articles to analyze.")
        return []

    logger.info(f"Starting deep analysis for {len(curated_articles)} curated articles with Analyst Model...")
    llm = get_chat_model(role="analyst", temperature=0.2)
    structured_llm = llm.with_structured_output(ArticleAnalysisOutput)

    prompt = ChatPromptTemplate.from_messages([
        ("system", ANALYST_SYSTEM_PROMPT),
        ("human", (
            "Source: {source_name}\n"
            "Category: {article_category}\n"
            "Title: {article_title}\n\n"
            "Full / Extracted Content:\n{article_content}\n\n"
            "Generate the structured technical analysis:"
        ))
    ])

    analyst_chain = prompt | structured_llm

    # Execute analyses concurrently with error protection
    tasks = [analyze_single_article(curated, analyst_chain) for curated in curated_articles]
    results = await asyncio.gather(*tasks, return_exceptions=False)

    return results
