"""Auditor Agent: Quality assurance, syntax/leak inspection, and auto-healing for daily briefs.

Runs as a StateGraph gatekeeper before disk archiving and as a post-push verifier in GitHub Actions.
"""
import os
import re
import sys
import logging
import argparse
from pathlib import Path
from typing import List, Dict, Any, Tuple
from pydantic import BaseModel, Field

from config.settings import settings
from src.agents.reporter import extract_text_content, clean_executive_summary

logger = logging.getLogger(__name__)

class AuditResult(BaseModel):
    is_valid: bool = Field(..., description="True if no critical flaws remain after audit/auto-heal")
    issues_found: List[str] = Field(default_factory=list, description="List of detected anomalies")
    fixes_applied: List[str] = Field(default_factory=list, description="List of auto-healing repairs applied")
    cleaned_report_md: str = Field(..., description="Sanitized and validated markdown content")

# Patterns indicating raw object/code/signature leaks
SUSPICIOUS_LEAK_PATTERNS = [
    (r"\[\s*\{\s*['\"]type['\"]\s*:\s*['\"]text['\"].*?\}", "Leaked raw LLM content block list `[{'type': 'text' ...}]`"),
    (r"['\"]extras['\"]\s*:\s*\{\s*['\"]signature['\"]\s*:", "Leaked Gemini/LLM cryptographic extras/signature block"),
    (r"['\"]signature['\"]\s*:\s*['\"][A-Za-z0-9+/=]{40,}['\"]", "Leaked base64 cryptographic signature"),
    (r"\{\s*['\"]type['\"]\s*:\s*['\"]thinking['\"]", "Leaked LLM internal thinking block"),
    (r"AIMessage\s*\(", "Leaked LangChain AIMessage repr"),
    (r"ChatResult\s*\(", "Leaked LangChain ChatResult repr"),
]

REQUIRED_SECTIONS = [
    (r"#\s*🤖\s*.*?(Bülteni|Brief)", "Report Title Header (`# 🤖 ...`)"),
    (r"##\s*⚡\s*.*?(TL;DR|Özeti|Summary)", "Executive Summary Section (`## ⚡ ...`)"),
    (r"##\s*🔬\s*.*?", "Research & Breakthroughs Section (`## 🔬 ...`)"),
    (r"##\s*🛠️\s*.*?", "Tooling & Frameworks Section (`## 🛠️ ...`)"),
    (r"##\s*📚\s*.*?", "Source Directory Section (`## 📚 ...`)"),
]

def check_leaks_and_auto_heal(markdown_content: str) -> Tuple[str, List[str], List[str]]:
    """Inspects markdown for leaked Python dicts, signatures, or brackets and auto-heals them."""
    issues = []
    fixes = []
    cleaned = markdown_content

    for pattern, description in SUSPICIOUS_LEAK_PATTERNS:
        if re.search(pattern, cleaned, flags=re.DOTALL):
            issues.append(description)

    # Auto-heal: Extract clean text if raw list/dict pattern found in content
    # Handle `[{'type': 'text', 'text': "...", 'extras': ...}]`
    dict_leak_match = re.search(
        r"(\[\s*\{\s*['\"]type['\"]\s*:\s*['\"]text['\"].*?\}\s*\])",
        cleaned,
        flags=re.DOTALL
    )
    if dict_leak_match:
        raw_block = dict_leak_match.group(1)
        extracted = clean_executive_summary(raw_block)
        if extracted and "signature" not in extracted:
            cleaned = cleaned.replace(raw_block, extracted)
            fixes.append("Auto-healed leaked LLM text/signature block into clean markdown")

    # Extra pass: strip any dangling extras or signature tokens
    if "signature" in cleaned or "extras" in cleaned:
        cleaned_sub = re.sub(r",\s*['\"]extras['\"]\s*:\s*\{.*?\}", '', cleaned, flags=re.DOTALL)
        cleaned_sub = re.sub(r"['\"]signature['\"]\s*:\s*['\"][A-Za-z0-9+/=]+['\"]", '', cleaned_sub)
        if cleaned_sub != cleaned:
            cleaned = cleaned_sub
            fixes.append("Stripped residual `extras` and `signature` keys")

    # Auto-heal redundant executive summary subheaders
    # E.g. `## ⚡ Yönetici Özeti (TL;DR)\n\n### Yönetici Özeti (TL;DR)\n`
    redundant_header_pattern = r"(##\s*⚡[^\n]+\n+)\s*#{1,4}\s*.*?(TL;DR|Yönetici Özeti|Executive Summary)[^\n]*\n+"
    if re.search(redundant_header_pattern, cleaned, flags=re.IGNORECASE):
        cleaned = re.sub(redundant_header_pattern, r"\1", cleaned, flags=re.IGNORECASE)
        fixes.append("Removed duplicate executive summary subheader")

    return cleaned, issues, fixes

def check_markdown_structure(markdown_content: str) -> List[str]:
    """Verifies that all mandatory report sections exist and are populated."""
    structural_issues = []
    for pattern, name in REQUIRED_SECTIONS:
        if not re.search(pattern, markdown_content):
            structural_issues.append(f"Missing required section: {name}")

    # Check minimum length to prevent blank or truncated reports
    if len(markdown_content.strip()) < 300:
        structural_issues.append(f"Report is suspiciously short ({len(markdown_content.strip())} chars)")

    return structural_issues

def check_links_and_tables(markdown_content: str) -> List[str]:
    """Inspects markdown links and table integrity."""
    link_issues = []

    # Check for empty links like `[](url)` or `[text]()`
    empty_links = re.findall(r"\[\s*\]\([^\)]*\)|\[[^\]]+\]\(\s*\)", markdown_content)
    if empty_links:
        link_issues.append(f"Found {len(empty_links)} malformed or empty Markdown link(s)")

    # Check table structure: ensure rows have pipes and reasonable alignment
    tables = re.findall(r"(\|[^\n]+\|\n\|[-:| ]+\|\n(?:\|[^\n]+\|\n?)*)", markdown_content)
    if not tables:
        link_issues.append("Source Directory table missing or malformed")

    return link_issues

def audit_report_content(report_md: str, auto_heal: bool = True) -> AuditResult:
    """
    Core auditing routine. Inspects markdown content, applies auto-heals if requested,
    and returns an AuditResult.
    """
    cleaned_md, leak_issues, fixes = check_leaks_and_auto_heal(report_md)
    structure_issues = check_markdown_structure(cleaned_md)
    link_issues = check_links_and_tables(cleaned_md)

    all_issues = leak_issues + structure_issues + link_issues

    # If auto-heal was turned off, revert cleaned_md
    final_md = cleaned_md if auto_heal else report_md

    # Check remaining critical flaws in final output
    remaining_critical = [
        issue for issue in leak_issues
        if any(re.search(pat[0], final_md) for pat in SUSPICIOUS_LEAK_PATTERNS)
    ]

    is_valid = len(remaining_critical) == 0 and len(structure_issues) == 0

    return AuditResult(
        is_valid=is_valid,
        issues_found=all_issues,
        fixes_applied=fixes,
        cleaned_report_md=final_md
    )

def audit_report_file(file_path: Path, auto_heal: bool = True) -> AuditResult:
    """Audits an existing markdown file on disk and auto-heals in-place if needed."""
    if not file_path.exists():
        raise FileNotFoundError(f"Report file not found: {file_path}")

    content = file_path.read_text(encoding="utf-8")
    result = audit_report_content(content, auto_heal=auto_heal)

    if auto_heal and result.fixes_applied and result.cleaned_report_md != content:
        file_path.write_text(result.cleaned_report_md, encoding="utf-8")
        logger.info(f"Auto-healed and updated report file in-place: {file_path}")

    return result

def audit_latest_report(auto_heal: bool = True) -> Tuple[Path, AuditResult]:
    """Finds the most recent daily brief file in reports/ and audits it."""
    reports_dir = settings.reports_dir
    md_files = sorted(list(reports_dir.glob("20*/*/*-daily-brief.md")), reverse=True)
    if not md_files:
        raise FileNotFoundError(f"No daily brief files found under {reports_dir}")

    latest_file = md_files[0]
    result = audit_report_file(latest_file, auto_heal=auto_heal)
    return latest_file, result

async def audit_node(state: Dict[str, Any]) -> Dict[str, Any]:
    """StateGraph Node: Quality assurance gate, syntax/leak verification, and auto-healing."""
    logger.info(">>> [Phase 5] Starting Auditor Agent (Quality Assurance Gate)...")
    report_md = state.get("final_report_md", "")
    audit_result = audit_report_content(report_md, auto_heal=True)

    if audit_result.issues_found:
        logger.warning(f"Auditor detected {len(audit_result.issues_found)} issues: {audit_result.issues_found}")
    if audit_result.fixes_applied:
        logger.info(f"Auditor applied {len(audit_result.fixes_applied)} auto-heals: {audit_result.fixes_applied}")

    return {
        "final_report_md": audit_result.cleaned_report_md,
        "audit_passed": audit_result.is_valid,
        "audit_issues": audit_result.issues_found,
        "audit_fixes": audit_result.fixes_applied
    }

def main():
    """CLI Entrypoint for GitHub Actions post-push verification or local checks."""
    try:
        if sys.stdout.encoding and sys.stdout.encoding.lower() != "utf-8":
            sys.stdout.reconfigure(encoding="utf-8")
            sys.stderr.reconfigure(encoding="utf-8")
    except Exception:
        pass

    parser = argparse.ArgumentParser(description="Auditor Agent: Verify and auto-heal daily intelligence briefs.")
    parser.add_argument("--file", type=str, default=None, help="Path to specific report Markdown file to audit")
    parser.add_argument("--latest", action="store_true", help="Audit the most recent report in reports/")
    parser.add_argument("--no-auto-heal", action="store_true", help="Disable auto-healing repairs")
    parser.add_argument("--strict", action="store_true", help="Exit with code 1 if any issues were detected")

    args = parser.parse_args()
    auto_heal = not args.no_auto_heal

    target_file = None
    if args.file:
        target_file = Path(args.file)
        result = audit_report_file(target_file, auto_heal=auto_heal)
    elif args.latest:
        target_file, result = audit_latest_report(auto_heal=auto_heal)
    else:
        # Default to latest if no argument provided
        target_file, result = audit_latest_report(auto_heal=auto_heal)

    print("\n" + "=" * 65)
    print(" 🛡️ AUDITOR AGENT — QUALITY ASSURANCE & VERIFICATION")
    print(f" 📄 Target File: {target_file}")
    print(f" 🚦 Status: {'PASSED ✅' if result.is_valid else 'FAILED ❌'}")
    
    if result.issues_found:
        print("\n ⚠️ Detected Issues:")
        for issue in result.issues_found:
            print(f"   - {issue}")

    if result.fixes_applied:
        print("\n 🛠️ Auto-Healed Fixes:")
        for fix in result.fixes_applied:
            print(f"   - {fix}")

    print("=" * 65 + "\n")

    if args.strict and (not result.is_valid or result.issues_found):
        sys.exit(1)
    elif not result.is_valid:
        sys.exit(1)
    else:
        sys.exit(0)

if __name__ == "__main__":
    main()
