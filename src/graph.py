"""LangGraph StateGraph orchestration pipeline for AI Intelligence Agent."""
import asyncio
import logging
from datetime import datetime, timezone
from typing import Dict, Any

from langgraph.graph import StateGraph, START, END

from src.state import PipelineState
from src.ingest.rss_collector import collect_all_rss
from src.ingest.arxiv_collector import collect_all_arxiv
from src.agents.curator import curate_articles
from src.agents.analyst import analyze_articles
from src.agents.reporter import synthesize_report
from src.agents.auditor import audit_node
from src.agents.broadcaster import broadcast_node
from src.utils.archive_manager import save_daily_report, update_catalog_index

logger = logging.getLogger(__name__)

async def ingest_node(state: PipelineState) -> Dict[str, Any]:
    """Ingestion Worker: Parallel async fetching of RSS feeds and ArXiv papers."""
    logger.info(">>> [Phase 1] Starting Ingestion Worker (RSS + ArXiv)...")
    rss_task = collect_all_rss()
    arxiv_task = collect_all_arxiv()
    
    rss_items, arxiv_items = await asyncio.gather(rss_task, arxiv_task, return_exceptions=False)
    
    # Deduplicate combined articles
    combined = []
    seen = set()
    for item in (rss_items + arxiv_items):
        if item.id not in seen:
            seen.add(item.id)
            combined.append(item)

    today_str = state.get("report_date") or datetime.now(timezone.utc).strftime("%Y-%m-%d")
    logger.info(f"Ingestion complete. Total unique raw items collected: {len(combined)}")
    return {
        "raw_articles": combined,
        "report_date": today_str
    }

async def curate_node(state: PipelineState) -> Dict[str, Any]:
    """Curator Agent: Relevance scoring (1-10) and filtering."""
    logger.info(">>> [Phase 2] Starting Curator Agent...")
    raw = state.get("raw_articles", [])
    curated = await curate_articles(raw)
    return {
        "curated_articles": curated
    }

async def analyze_node(state: PipelineState) -> Dict[str, Any]:
    """Analyst Agent: Deep technical extraction, architecture & benchmarks."""
    logger.info(">>> [Phase 3] Starting Deep Analyst Agent...")
    curated = state.get("curated_articles", [])
    analyzed = await analyze_articles(curated)
    return {
        "analyzed_articles": analyzed
    }

async def report_node(state: PipelineState) -> Dict[str, Any]:
    """Reporter Agent: Synthesizes executive summary and Markdown sections."""
    logger.info(">>> [Phase 4] Starting Reporter Agent...")
    analyzed = state.get("analyzed_articles", [])
    report_date = state.get("report_date", datetime.now(timezone.utc).strftime("%Y-%m-%d"))
    report_md = await synthesize_report(analyzed, report_date)
    return {
        "final_report_md": report_md
    }

async def archive_node(state: PipelineState) -> Dict[str, Any]:
    """Archive Manager: Hierarchical disk storage and catalog indexing."""
    logger.info(">>> [Phase 6] Saving Report & Updating Catalog Index...")
    report_md = state.get("final_report_md", "")
    report_date = state.get("report_date", datetime.now(timezone.utc).strftime("%Y-%m-%d"))
    analyzed = state.get("analyzed_articles", [])

    saved_path = save_daily_report(report_md, report_date)
    update_catalog_index(saved_path, report_date, analyzed)
    
    return {
        "report_file_path": str(saved_path)
    }

def build_graph():
    """Builds and compiles the deterministic Multi-Agent StateGraph."""
    workflow = StateGraph(PipelineState)

    # Add Nodes
    workflow.add_node("ingest", ingest_node)
    workflow.add_node("curate", curate_node)
    workflow.add_node("analyze", analyze_node)
    workflow.add_node("report", report_node)
    workflow.add_node("audit", audit_node)
    workflow.add_node("archive", archive_node)
    workflow.add_node("broadcast", broadcast_node)

    # Add Linear Transitions
    workflow.add_edge(START, "ingest")
    workflow.add_edge("ingest", "curate")
    workflow.add_edge("curate", "analyze")
    workflow.add_edge("analyze", "report")
    workflow.add_edge("report", "audit")
    workflow.add_edge("audit", "archive")
    workflow.add_edge("archive", "broadcast")
    workflow.add_edge("broadcast", END)

    return workflow.compile()
