import os
from pathlib import Path
from typing import Any, Dict, List, Literal
try:
    import yaml
except ImportError:
    yaml = None
from pydantic_settings import BaseSettings, SettingsConfigDict

BASE_DIR = Path(__file__).resolve().parent.parent

class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=str(BASE_DIR / ".env"),
        env_file_encoding="utf-8",
        extra="ignore"
    )

    # LLM Settings
    llm_provider: Literal["gemini", "openai"] = "gemini"
    gemini_api_key: str = ""
    openai_api_key: str = ""
    
    curator_model: str = "gemini-3.8-flash"
    analyst_model: str = "gemini-3.8-flash"

    # Localization
    report_language: Literal["tr", "en"] = "tr"

    # Ingestion & Filtering
    max_hours_old: int = 24
    max_articles_per_source: int = 8
    min_relevance_score: int = 7
    max_curated_articles: int = 8

    # Paths
    base_dir: Path = BASE_DIR
    sources_yaml_path: Path = BASE_DIR / "config" / "sources.yaml"
    reports_dir: Path = BASE_DIR / "reports"
    readme_path: Path = BASE_DIR / "README.md"

    def load_sources_config(self) -> Dict[str, Any]:
        """Loads RSS feeds and ArXiv categories from sources.yaml."""
        if not self.sources_yaml_path.exists() or yaml is None:
            return {"rss_feeds": [], "arxiv": {"categories": []}}
        with open(self.sources_yaml_path, "r", encoding="utf-8") as f:
            return yaml.safe_load(f) or {}

settings = Settings()
