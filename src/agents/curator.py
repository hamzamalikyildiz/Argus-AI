"""Curator Agent: Evaluates raw articles and scores technical relevance (1-10) using structured LLM outputs."""
import logging
from typing import List, Dict
from pydantic import BaseModel, Field
from langchain_core.prompts import ChatPromptTemplate

from src.state import RawArticle, CuratedArticle
from src.agents.llm_factory import get_chat_model
from config.settings import settings

logger = logging.getLogger(__name__)

class ArticleScore(BaseModel):
    id: str = Field(..., description="Unique article ID corresponding to the input")
    relevance_score: int = Field(..., ge=1, le=10, description="Relevance score from 1 (irrelevant/hype) to 10 (historic breakthrough/major release)")
    reasoning: str = Field(..., description="Short explanation of why this item received the score")
    category: str = Field(..., description="One of: Research, LLM Release, Tooling, Industry")

class BatchScoreResult(BaseModel):
    evaluations: List[ArticleScore] = Field(..., description="List of scored articles")

CURATOR_SYSTEM_PROMPT = """You are an elite AI/ML Staff Engineer and Tech Scout.
Your mission is to evaluate incoming AI news and research papers with zero tolerance for marketing fluff.

Scoring Criteria (1-10):
- 9-10: Paradigm shifts, major model releases (e.g. Llama, Mistral, DeepSeek), foundational research breakthroughs, novel architectures.
- 7-8: Solid technical benchmarks, notable open-source frameworks/tools, significant architectural improvements (e.g. MoE, attention optimizations, quantization).
- 4-6: Incremental tool updates, venture capital / business news, corporate opinion pieces.
- 1-3: Generic PR, clickbait, repetitive AI hype, low-information articles.

Categories:
- "Research": ArXiv papers, academic discoveries, mathematical/algorithmic papers.
- "LLM Release": New weights, foundation models, checkpoints, official provider updates.
- "Tooling": Developer libraries, inference engines, quantization frameworks, SDKs.
- "Industry": Policy, infrastructure, key enterprise developments.

Evaluate each article objectively based solely on its title and summary."""

async def curate_articles(raw_articles: List[RawArticle]) -> List[CuratedArticle]:
    """Scores raw articles in batches and filters top relevant entries."""
    if not raw_articles:
        logger.info("No raw articles to curate.")
        return []

    logger.info(f"Curating {len(raw_articles)} raw articles with Curator Model...")
    llm = get_chat_model(role="curator", temperature=0.1)
    structured_llm = llm.with_structured_output(BatchScoreResult)

    prompt = ChatPromptTemplate.from_messages([
        ("system", CURATOR_SYSTEM_PROMPT),
        ("human", "Evaluate the following batch of articles:\n\n{articles_text}")
    ])

    curator_chain = prompt | structured_llm

    # Create mapping by ID for fast lookup
    article_map: Dict[str, RawArticle] = {a.id: a for a in raw_articles}
    batch_size = 15
    all_scores: List[ArticleScore] = []

    for i in range(0, len(raw_articles), batch_size):
        batch = raw_articles[i:i + batch_size]
        articles_text = "\n---\n".join([
            f"ID: {a.id}\nTitle: {a.title}\nSource: {a.source}\nSummary: {a.summary}"
            for a in batch
        ])

        try:
            result: BatchScoreResult = await curator_chain.ainvoke({"articles_text": articles_text})
            if result and result.evaluations:
                all_scores.extend(result.evaluations)
        except Exception as e:
            logger.error(f"Error curating batch {i // batch_size + 1}: {e}")

    # Build CuratedArticle objects
    curated_list: List[CuratedArticle] = []
    for score in all_scores:
        raw = article_map.get(score.id)
        if not raw:
            continue
        
        curated_list.append(
            CuratedArticle(
                raw=raw,
                relevance_score=score.relevance_score,
                reasoning=score.reasoning,
                category=score.category
            )
        )

    # Sort descending by relevance score
    curated_list.sort(key=lambda x: x.relevance_score, reverse=True)

    # Filter by primary threshold (score >= min_relevance_score)
    filtered = [
        item for item in curated_list
        if item.relevance_score >= settings.min_relevance_score
    ]

    # Smart Fallback: If no or fewer than 3 items meet the high threshold (e.g. on quiet news days or weekends),
    # select the highest-scoring available articles (score >= 5 or top 3) so the brief is never empty.
    if len(filtered) < 3 and curated_list:
        fallback_candidates = [item for item in curated_list if item.relevance_score >= 5]
        if not fallback_candidates:
            fallback_candidates = curated_list[:3]

        seen_ids = {item.raw.id for item in filtered}
        for candidate in fallback_candidates:
            if candidate.raw.id not in seen_ids and len(filtered) < 5:
                filtered.append(candidate)
                seen_ids.add(candidate.raw.id)

        filtered.sort(key=lambda x: x.relevance_score, reverse=True)
        logger.info(f"Curator smart fallback activated: Selected {len(filtered)} best available articles.")

    # Take top N
    top_curated = filtered[:settings.max_curated_articles]
    logger.info(
        f"Curation complete: {len(top_curated)} high-impact articles selected "
        f"(threshold >= {settings.min_relevance_score} with smart fallback)."
    )
    return top_curated
