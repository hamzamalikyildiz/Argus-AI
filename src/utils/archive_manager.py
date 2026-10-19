"""Archive Manager: Handles hierarchical report storage and automatic README/INDEX catalogue updates."""
import os
import re
import logging
from pathlib import Path
from typing import List, Optional
from datetime import datetime

from src.state import AnalyzedArticle
from config.settings import settings

logger = logging.getLogger(__name__)

def save_daily_report(report_md: str, report_date_str: str) -> Path:
    """
    Saves report into hierarchical path: reports/YYYY/MM/YYYY-MM-DD-daily-brief.md
    Dynamically creates missing directories.
    """
    try:
        dt = datetime.strptime(report_date_str, "%Y-%m-%d")
    except ValueError:
        dt = datetime.utcnow()
        report_date_str = dt.strftime("%Y-%m-%d")

    year_str = dt.strftime("%Y")
    month_str = dt.strftime("%m")

    target_dir = settings.reports_dir / year_str / month_str
    target_dir.mkdir(parents=True, exist_ok=True)

    filename = f"{report_date_str}-daily-brief.md"
    target_file = target_dir / filename

    with open(target_file, "w", encoding="utf-8") as f:
        f.write(report_md)

    logger.info(f"Daily report saved to: {target_file}")
    return target_file

def generate_focus_summary(analyzed: List[AnalyzedArticle]) -> str:
    """Generates a concise focus highlight (e.g. 'DeepSeek-V3, MoE Attention') for the catalog table."""
    if not analyzed:
        return "Günlük AI Bülteni"
    
    titles = [a.title.split(":")[0].strip() for a in analyzed[:2]]
    focus = ", ".join(titles)
    # clean table characters
    focus = focus.replace("|", "-")
    return focus[:60]

def update_catalog_index(report_file: Path, report_date_str: str, analyzed: List[AnalyzedArticle]) -> None:
    """
    Updates the master index table in reports/INDEX.md and README.md.
    Maintains chronological ordering without duplicate dates.
    """
    rel_path = report_file.relative_to(settings.base_dir).as_posix()
    focus_topic = generate_focus_summary(analyzed)
    new_entry_row = f"| {report_date_str} | {focus_topic} | [Raporu Oku]({rel_path}) |"

    # 1. Update or create reports/INDEX.md
    index_file = settings.reports_dir / "INDEX.md"
    settings.reports_dir.mkdir(parents=True, exist_ok=True)
    
    table_header = "| Tarih | Başlık / Odak Noktası | Rapor Linki |\n|:---:|:---|:---:|\n"
    
    if index_file.exists():
        content = index_file.read_text(encoding="utf-8")
        # Check if already present for this date
        if f"| {report_date_str} |" in content:
            # Replace existing line for this date
            content = re.sub(
                rf"\| {re.escape(report_date_str)} \|.*?\|\n",
                f"{new_entry_row}\n",
                content
            )
        else:
            # Insert right below header
            if table_header.strip() in content:
                content = content.replace(table_header, f"{table_header}{new_entry_row}\n")
            else:
                content = f"# 📚 Rapor Arşivi (All Reports)\n\n{table_header}{new_entry_row}\n"
    else:
        content = f"# 📚 Rapor Arşivi (All Reports)\n\n{table_header}{new_entry_row}\n"

    index_file.write_text(content, encoding="utf-8")
    logger.info(f"Updated archive index at: {index_file}")

    # 2. Update README.md archive section if README exists
    readme_file = settings.readme_path
    if readme_file.exists():
        readme_text = readme_file.read_text(encoding="utf-8")
        archive_marker = "<!-- RECENT_REPORTS_START -->"
        archive_end_marker = "<!-- RECENT_REPORTS_END -->"

        if archive_marker in readme_text and archive_end_marker in readme_text:
            before = readme_text.split(archive_marker)[0]
            after = readme_text.split(archive_end_marker)[1]
            
            # Extract existing lines inside marker
            middle = readme_text.split(archive_marker)[1].split(archive_end_marker)[0].strip()
            lines = [line.strip() for line in middle.splitlines() if line.strip().startswith("|")]
            
            # Remove header if in lines
            data_rows = [l for l in lines if not l.startswith("| Tarih") and not l.startswith("|:---:")]
            # Filter out current date if already exists
            data_rows = [l for l in data_rows if not l.startswith(f"| {report_date_str} |")]
            # Prepend new row
            data_rows.insert(0, new_entry_row)
            
            # Keep top 10 in README
            recent_rows = data_rows[:10]
            new_table = f"{table_header}" + "\n".join(recent_rows)
            updated_readme = f"{before}{archive_marker}\n{new_table}\n\n[Tüm Arşivi Gör (reports/INDEX.md)](reports/INDEX.md)\n{archive_end_marker}{after}"
            readme_file.write_text(updated_readme, encoding="utf-8")
            logger.info("Updated Recent Reports section in README.md")
