"""Main CLI entrypoint for AI Intelligence Agent."""
import sys
import os
import asyncio
import logging
import argparse
from datetime import datetime, timezone
from dotenv import load_dotenv

# Ensure root directory is on Python path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from config.settings import settings
from src.graph import build_graph

# Setup clean terminal logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)-7s | %(name)s - %(message)s",
    datefmt="%H:%M:%S"
)
logger = logging.getLogger("intelligence-agent")

async def run_pipeline(date_str: str = None, lang: str = None):
    """Executes the daily brief intelligence pipeline."""
    load_dotenv()
    
    if lang:
        settings.report_language = lang

    today = date_str or datetime.now(timezone.utc).strftime("%Y-%m-%d")

    print("\n" + "=" * 65)
    print(" 👁️ ARGUS-AI — MULTI-AGENT INTELLIGENCE PIPELINE")
    print(f" 📅 Date: {today}")
    print(f" 🧠 LLM Provider: {settings.llm_provider.upper()} (Curator: {settings.curator_model} | Analyst: {settings.analyst_model})")
    print(f" 🌐 Report Language: {settings.report_language.upper()}")
    print("=" * 65 + "\n")

    initial_state = {
        "raw_articles": [],
        "curated_articles": [],
        "analyzed_articles": [],
        "final_report_md": "",
        "report_date": today,
        "report_file_path": "",
        "audit_passed": True,
        "audit_issues": [],
        "audit_fixes": []
    }

    graph = build_graph()
    
    try:
        final_state = await graph.ainvoke(initial_state)
        report_path = final_state.get("report_file_path")
        audit_passed = final_state.get("audit_passed", True)
        issues = final_state.get("audit_issues", [])
        fixes = final_state.get("audit_fixes", [])
        
        telegram_sent = final_state.get("telegram_broadcast_sent", False)
        
        print("\n" + "=" * 65)
        print(" ✅ PIPELINE COMPLETED SUCCESSFULLY")
        print(f" 📄 Generated Report: {report_path}")
        print(f" 📊 Raw: {len(final_state.get('raw_articles', []))} | Curated: {len(final_state.get('curated_articles', []))} | Analyzed: {len(final_state.get('analyzed_articles', []))}")
        print(f" 🛡️ Auditor Gate: {'PASSED ✅' if audit_passed else 'WARNING ⚠️'} (Issues: {len(issues)} | Fixes: {len(fixes)})")
        print(f" 📲 Telegram Broadcast: {'SENT ✅' if telegram_sent else 'SKIPPED (No token configured) ℹ️'}")
        print("=" * 65 + "\n")
        return final_state
    except Exception as e:
        logger.error(f"Pipeline failed with error: {e}", exc_info=True)
        sys.exit(1)

def main():
    try:
        if sys.stdout.encoding and sys.stdout.encoding.lower() != "utf-8":
            sys.stdout.reconfigure(encoding="utf-8")
            sys.stderr.reconfigure(encoding="utf-8")
    except Exception:
        pass

    parser = argparse.ArgumentParser(description="AI Intelligence Daily Brief Agent")
    parser.add_argument("--date", type=str, default=None, help="Target report date (YYYY-MM-DD)")
    parser.add_argument("--lang", type=str, choices=["tr", "en"], default=None, help="Report language override ('tr' or 'en')")
    
    args = parser.parse_args()
    asyncio.run(run_pipeline(date_str=args.date, lang=args.lang))

if __name__ == "__main__":
    main()
