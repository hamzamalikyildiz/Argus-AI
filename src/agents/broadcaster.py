"""Broadcaster Agent: Formats and dispatches daily intelligence briefs to Telegram channels/chats."""
import os
import re
import html
import logging
import argparse
from typing import Dict, Any, Optional
import httpx

from config.settings import settings

logger = logging.getLogger(__name__)

def markdown_bullets_to_html(text: str) -> str:
    """Converts common Markdown bold, italic, and bullet syntax to clean Telegram HTML."""
    # 1. Convert bullet points: * or - at start of line -> • (Do this first so * bullets don't collide with italics)
    formatted = re.sub(r"^\s*[\*\-]\s+", "• ", text, flags=re.MULTILINE)
    # 2. Convert bold: **text** -> <b>text</b>
    formatted = re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", formatted)
    # 3. Convert italic: *text* or _text_ -> <i>text</i>
    formatted = re.sub(r"(?<![*\w])\*([^*\n]+)\*(?![*\w])", r"<i>\1</i>", formatted)
    formatted = re.sub(r"(?<![_\w])_([^_\n]+)_(?![_\w])", r"<i>\1</i>", formatted)
    return formatted.strip()

def prepare_telegram_message(report_md: str, report_date: str) -> str:
    """Extracts executive summary and key highlights, preparing an elegant HTML Telegram post."""
    is_tr = settings.report_language == "tr"

    # 1. Extract Executive Summary
    tldr_match = re.search(
        r"##\s*⚡\s*.*?(TL;DR|Yönetici Özeti|Executive Summary)[^\n]*\n(.*?)(?:\n---|\n##)",
        report_md,
        flags=re.DOTALL | re.IGNORECASE
    )
    if tldr_match:
        tldr_raw = tldr_match.group(2).strip()
        tldr_html = markdown_bullets_to_html(tldr_raw)
    else:
        tldr_html = (
            "• Günün kritik gelişmeleri başarıyla arşivlendi."
            if is_tr else
            "• Today's key developments were successfully archived."
        )

    # 2. Extract Top 5 Headlines
    headlines = re.findall(r"###\s*\[([^\]]+)\]\(([^)]+)\)", report_md)
    headlines_text = ""
    if headlines:
        headline_items = []
        for idx, (title, link) in enumerate(headlines[:5], 1):
            clean_title = html.escape(title.strip())
            headline_items.append(f"{idx}. <a href=\"{link}\">{clean_title}</a>")
        headlines_text = "\n".join(headline_items)

    # 3. Construct GitHub permalink
    # Format: reports/YYYY/MM/YYYY-MM-DD-daily-brief.md
    dt_parts = report_date.split("-")
    if len(dt_parts) == 3:
        year, month = dt_parts[0], dt_parts[1]
    else:
        year, month = "2026", "10"
    repo_name = settings.github_repository or os.getenv("GITHUB_REPOSITORY", "hamzamalikyildiz/Argus-AI")
    report_url = f"https://github.com/{repo_name}/blob/main/reports/{year}/{month}/{report_date}-daily-brief.md"

    # Assemble HTML message
    title_header = (
        f"🤖 <b>Argus-AI — Günlük Yapay Zeka Bülteni</b>\n📅 <b>Tarih:</b> <code>{report_date}</code> | 🌐 <b>Dil:</b> {'Türkçe' if is_tr else 'English'}"
    )
    tldr_title = "⚡ <b>Yönetici Özeti (TL;DR):</b>" if is_tr else "⚡ <b>Executive Summary (TL;DR):</b>"
    highlights_title = "📚 <b>Öne Çıkan Başlıklar:</b>" if is_tr else "📚 <b>Featured Highlights:</b>"
    read_more_label = "Raporun Tamamını ve Teknik Analizleri Oku ➔" if is_tr else "Read Full Brief & Architecture Deep-Dive ➔"

    sections = [
        title_header,
        f"\n{tldr_title}\n{tldr_html}",
    ]
    if headlines_text:
        sections.append(f"\n{highlights_title}\n{headlines_text}")

    sections.append(f"\n🔗 <a href=\"{report_url}\"><b>{read_more_label}</b></a>")

    full_message = "\n".join(sections)

    # Telegram hard limit is 4096 characters; ensure safety buffer
    if len(full_message) > 4000:
        truncate_point = 3900 - len(report_url)
        full_message = full_message[:truncate_point] + f"...\n\n🔗 <a href=\"{report_url}\"><b>{read_more_label}</b></a>"

    return full_message

async def send_telegram_broadcast(
    message_html: str,
    bot_token: Optional[str] = None,
    chat_id: Optional[str] = None
) -> bool:
    """Dispatches HTML message to configured Telegram channel or chat via Telegram Bot API."""
    token = bot_token or settings.telegram_bot_token or os.getenv("TELEGRAM_BOT_TOKEN")
    target_chat = chat_id or settings.telegram_chat_id or os.getenv("TELEGRAM_CHAT_ID")

    if not token or not target_chat:
        logger.info("Telegram credentials not configured (TELEGRAM_BOT_TOKEN or TELEGRAM_CHAT_ID missing). Broadcast skipped.")
        return False

    api_url = f"https://api.telegram.org/bot{token}/sendMessage"
    payload = {
        "chat_id": target_chat,
        "text": message_html,
        "parse_mode": "HTML",
        "disable_web_page_preview": True
    }

    try:
        async with httpx.AsyncClient(timeout=15.0) as client:
            response = await client.post(api_url, json=payload)
            if response.status_code == 200:
                logger.info(f"Telegram broadcast sent successfully to chat: {target_chat}")
                return True
            else:
                logger.error(f"Telegram broadcast failed with status {response.status_code}: {response.text}")
                return False
    except Exception as e:
        logger.error(f"Failed to send Telegram broadcast: {e}")
        return False

async def broadcast_node(state: Dict[str, Any]) -> Dict[str, Any]:
    """StateGraph Node: Dispatches summary broadcast to Telegram after archiving."""
    logger.info(">>> [Phase 7] Starting Telegram Broadcaster Agent...")
    report_md = state.get("final_report_md", "")
    report_date = state.get("report_date", "")

    if report_md and report_date:
        message = prepare_telegram_message(report_md, report_date)
        sent = await send_telegram_broadcast(message)
        return {"telegram_broadcast_sent": sent}

    return {"telegram_broadcast_sent": False}

def main():
    """CLI entrypoint to test Telegram broadcast directly from terminal or CI."""
    logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")
    parser = argparse.ArgumentParser(description="Test Telegram Broadcaster")
    parser.add_argument("--test", action="store_true", help="Send a test message")
    parser.add_argument("--date", type=str, default="2026-10-21", help="Date of report to broadcast")
    args = parser.parse_args()

    import asyncio
    import sys
    if args.test:
        test_msg = f"🤖 <b>Argus-AI Bot Test</b>\n📅 <code>{args.date}</code>\n\nTelegram yayın kanalı başarıyla bağlandı! ✅"
        result = asyncio.run(send_telegram_broadcast(test_msg))
        print("Test Broadcast Result:", "SUCCESS ✅" if result else "FAILED (Check credentials) ❌")
        sys.exit(0 if result else 1)

if __name__ == "__main__":
    main()
