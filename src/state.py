from typing import List, TypedDict, Optional
from pydantic import BaseModel, Field

class RawArticle(BaseModel):
    id: str
    title: str
    source: str
    url: str
    published_at: str
    summary: str
    full_text: Optional[str] = None

class CuratedArticle(BaseModel):
    raw: RawArticle
    relevance_score: int = Field(..., ge=1, le=10, description="Relevance score from 1 to 10")
    reasoning: str = Field(..., description="Reasoning for the assigned score")
    category: str = Field(..., description="Category: Research, LLM Release, Tooling, or Industry")

class AnalyzedArticle(BaseModel):
    title: str
    source_url: str
    key_takeaways: List[str] = Field(..., description="Key technical highlights and facts")
    technical_depth: str = Field(..., description="Detailed architectural, algorithmic, or benchmark analysis")
    why_it_matters: str = Field(..., description="Significance for developers, researchers, and open-source ecosystem")

class PipelineState(TypedDict, total=False):
    raw_articles: List[RawArticle]
    curated_articles: List[CuratedArticle]
    analyzed_articles: List[AnalyzedArticle]
    final_report_md: str
    report_date: str      # YYYY-MM-DD
    report_file_path: str # reports/YYYY/MM/YYYY-MM-DD-daily-brief.md
    audit_passed: bool
    audit_issues: List[str]
    audit_fixes: List[str]
