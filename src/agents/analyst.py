"""Deep Analyst Agent: Performs full-text web scraping and deep technical analysis."""
import asyncio
import logging
from typing import List, Optional, Dict, Any
from pydantic import BaseModel, Field
from langchain_core.prompts import ChatPromptTemplate

from src.state import CuratedArticle, AnalyzedArticle
from src.tools.web_scraper import extract_article_content
from src.agents.llm_factory import get_chat_model
from config.settings import settings

logger = logging.getLogger(__name__)

class ArticleAnalysisOutput(BaseModel):
    title: str = Field(..., description="Headline of the technical development, written strictly in the target language")
    key_takeaways: List[str] = Field(..., description="3-5 concrete technical facts or benchmarks, written strictly in the target language")
    technical_depth: str = Field(..., description="Deep dive into algorithmic changes and neural architecture, written strictly in the target language")
    why_it_matters: str = Field(..., description="Strategic significance for engineers and ecosystem, written strictly in the target language")

ANALYST_SYSTEM_PROMPT = """You are a Principal AI Architect and Deep Learning Researcher.
Your job is to provide rigorous, highly technical analysis of newly released AI developments, papers, and models.

CRITICAL MANDATORY RULES:
1. Target Language: {language_instruction}
   - You MUST write the ENTIRE structured output (title, key_takeaways, technical_depth, why_it_matters) strictly in the target language.
   - If the input text or article title is in English, you MUST translate and synthesize it into the target language. Do not output raw English when the target language is Turkish!
2. Grounded Analysis: Rely strictly on the provided article text, abstract, or scraped webpage. Do NOT invent fake metrics, benchmarks, or architectures.
3. Technical Depth:
   - What is the algorithmic or architectural innovation (e.g. Attention mechanism, MoE routing, KV-cache compression, RLHF / DPO method)?
   - Are there specific benchmarks reported (e.g. MMLU, GSM8k, SWE-bench, tokens/sec)?
   - Is open-source code or model weights available?
"""

LANGUAGE_INSTRUCTIONS = {
    "tr": (
        "ZORUNLU DİL KURALI: Tüm analizi (başlık, öne çıkan maddeler, teknik derinlik ve sektörel etki) "
        "TAMAMEN TÜRKÇE yazmalısınız. Kaynak metin İngilizce olsa dahi, içeriği akıcı, teknik terimleri yerinde "
        "(çıkarım maliyeti, dikkat mekanizması, açık ağırlıklar, seyreltilmiş hesaplama gibi) bir Türkçe ile sentezleyin. "
        "Başlık dahil tek bir İngilizce cümle dahi bırakmayın."
    ),
    "en": "Write the entire analysis strictly in professional, fluent, and rigorous technical English."
}

async def analyze_single_article(curated: CuratedArticle, analyst_chain) -> AnalyzedArticle:
    """Extracts full web content and performs deep technical analysis for a single article."""
    raw = curated.raw
    url = raw.url
    logger.info(f"Analyzing article: '{raw.title}' from {url}")

    # Proactively scrape web content to prevent hallucinations (bounded timeout)
    full_content = None
    try:
        full_content = await asyncio.wait_for(
            asyncio.to_thread(extract_article_content, url),
            timeout=10.0
        )
    except Exception as e:
        logger.warning(f"Web scraper bypassed or timed out for {url}: {e}")

    content_to_analyze = full_content if full_content else raw.summary
    # Truncate content to avoid exceeding context window limits while preserving richness
    content_to_analyze = content_to_analyze[:12000]

    lang = settings.report_language
    lang_inst = LANGUAGE_INSTRUCTIONS.get(lang, LANGUAGE_INSTRUCTIONS["tr"])

    output: Optional[ArticleAnalysisOutput] = None
    # Retry once on network or rate limit failure
    for attempt in range(2):
        try:
            output = await asyncio.wait_for(
                analyst_chain.ainvoke({
                    "language_instruction": lang_inst,
                    "article_title": raw.title,
                    "source_name": raw.source,
                    "article_category": curated.category,
                    "article_content": content_to_analyze
                }),
                timeout=40.0
            )
            break
        except Exception as e:
            if attempt == 0:
                logger.warning(f"Retry 1 for '{raw.title}' after error: {e}")
                await asyncio.sleep(2.0)
            else:
                logger.error(f"Failed deep analysis for '{raw.title}' after retry: {e}")

    if output:
        return AnalyzedArticle(
            title=output.title or raw.title,
            source_url=raw.url,  # ZERO HALLUCINATION: guaranteed raw URL
            key_takeaways=output.key_takeaways,
            technical_depth=output.technical_depth,
            why_it_matters=output.why_it_matters
        )
    else:
        # Safe language-aligned fallback if LLM is completely unavailable
        is_tr = lang == "tr"
        fallback_takeaways = (
            [f"{raw.title}: Gelişme detayları inceleniyor.", "Detaylı teknik metin için kaynak bağlantısına başvurunuz."]
            if is_tr else
            [raw.summary[:200]] if raw.summary else ["Detailed summary unavailable."]
        )
        return AnalyzedArticle(
            title=raw.title,
            source_url=raw.url,
            key_takeaways=fallback_takeaways,
            technical_depth=raw.summary or ("Teknik detay bulunamadı." if is_tr else "No technical details found."),
            why_it_matters=(
                f"{curated.category} alanında yapay zeka ekosistemi için dikkate değer bir gelişme."
                if is_tr else
                f"Notable development in the {curated.category} category."
            )
        )

async def analyze_articles(curated_articles: List[CuratedArticle]) -> List[AnalyzedArticle]:
    """Runs deep technical analysis across all curated articles with concurrency throttling."""
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
            "Generate the structured technical analysis in the target language:"
        ))
    ])

    analyst_chain = prompt | structured_llm

    # Throttle concurrency to max 2 simultaneous LLM calls to prevent Gemini rate limit 429
    semaphore = asyncio.Semaphore(2)

    async def analyze_with_semaphore(curated: CuratedArticle) -> AnalyzedArticle:
        async with semaphore:
            await asyncio.sleep(0.5)
            return await analyze_single_article(curated, analyst_chain)

    tasks = [analyze_with_semaphore(curated) for curated in curated_articles]
    results = await asyncio.gather(*tasks, return_exceptions=False)

    return results
