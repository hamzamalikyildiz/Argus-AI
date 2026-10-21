# Task & Implementation Plan: AI Intelligence Multi-Agent System

## 1. System Architecture
Deterministic LangGraph StateGraph pipeline running daily via GitHub Actions:
- **Ingestion Worker**: Parallel async ingestion from RSS & ArXiv API with 24h cutoff & deduplication.
- **Curator Agent**: Relevance scoring (1-10) with Pydantic structured output, filtering score >= 7.
- **Analyst Agent**: Trafilatura web scraping for full-text extraction, deep technical dive (architecture & benchmarks), zero-hallucination URL linking.
- **Publisher / Reporter Agent**: Synthesizes executive TL;DR and daily brief Markdown sections in configured language (`tr` or `en`).
- **Archive Manager**: Hierarchical file storage (`reports/YYYY/MM/YYYY-MM-DD-daily-brief.md`) and updates `INDEX.md` + `README.md`.

## 2. Completed Milestones
- [x] **Milestone 1.1**: Requirements, configuration (`config/sources.yaml`, `config/settings.py`, `.env.example`).
- [x] **Milestone 1.2**: Ingestion modules (`src/ingest/rss_collector.py`, `src/ingest/arxiv_collector.py`).
- [x] **Milestone 2.1**: LLM Factory (`src/agents/llm_factory.py`) with support for Gemini and OpenAI.
- [x] **Milestone 2.2**: Curator Agent (`src/agents/curator.py`) with batching and structured score output.
- [x] **Milestone 2.3**: Web Scraper Tool (`src/tools/web_scraper.py`) with Trafilatura.
- [x] **Milestone 2.4**: Deep Analyst Agent (`src/agents/analyst.py`) with full-text scraping and architectural analysis.
- [x] **Milestone 2.5**: Reporter Agent (`src/agents/reporter.py`) with executive synthesis and language selection.
- [x] **Milestone 3.1 & 3.2**: Hierarchical Archive & Index Manager (`src/utils/archive_manager.py`).
- [x] **Milestone 4.1 & 4.2**: LangGraph StateGraph (`src/graph.py`) and CLI entrypoint (`main.py`).
- [x] **Milestone 5.1**: GitHub Actions Workflow (`.github/workflows/daily_brief.yml`).
- [x] **Milestone 5.2**: Test suite and Docker configuration (`Dockerfile`, `tests/`).
- [x] **Milestone 6.1**: Bugfix for LLM content leak & cryptographic signature stripping (`src/agents/reporter.py`, `reports/2026/10/2026-10-20-daily-brief.md`).
- [x] **Milestone 6.2**: Auditor Agent with auto-heal capability, StateGraph gatekeeper node, and GitHub Actions post-push verification (`src/agents/auditor.py`, `src/graph.py`, `.github/workflows/daily_brief.yml`).
- [x] **Milestone 6.3**: Unit and integration test suite for leak prevention and quality auditing (`tests/test_reporter.py`, `tests/test_auditor.py`).

## 3. How to Run Locally
```bash
# 1. Install dependencies
pip install -r requirements.txt

# 2. Configure .env with your GEMINI_API_KEY or OPENAI_API_KEY
cp .env.example .env

# 3. Run the daily brief
python main.py
```
