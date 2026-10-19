import os
from pathlib import Path
from src.utils.archive_manager import save_daily_report, update_catalog_index
from src.state import AnalyzedArticle

def test_archive_creation(tmp_path, monkeypatch):
    from config.settings import settings
    monkeypatch.setattr(settings, "reports_dir", tmp_path / "reports")
    monkeypatch.setattr(settings, "readme_path", tmp_path / "README.md")
    monkeypatch.setattr(settings, "base_dir", tmp_path)

    # Prepare dummy README
    readme_path = tmp_path / "README.md"
    readme_path.write_text("# Test Repo\n<!-- RECENT_REPORTS_START -->\n<!-- RECENT_REPORTS_END -->\n", encoding="utf-8")

    report_md = "# Test Daily Brief\nContent here."
    date_str = "2026-10-19"
    saved_file = save_daily_report(report_md, date_str)

    assert saved_file.exists()
    assert "2026/10/2026-10-19-daily-brief.md" in saved_file.as_posix()

    analyzed = [
        AnalyzedArticle(
            title="Mamba-3 Benchmark",
            source_url="https://example.com/mamba3",
            key_takeaways=["Linear attention scaling"],
            technical_depth="State space models benchmarked against transformers.",
            why_it_matters="Reduces quadratic complexity."
        )
    ]
    update_catalog_index(saved_file, date_str, analyzed)

    # Check INDEX.md created
    index_file = tmp_path / "reports" / "INDEX.md"
    assert index_file.exists()
    index_content = index_file.read_text(encoding="utf-8")
    assert "2026-10-19" in index_content
    assert "Mamba-3 Benchmark" in index_content

    # Check README.md updated
    readme_content = readme_path.read_text(encoding="utf-8")
    assert "2026-10-19" in readme_content
