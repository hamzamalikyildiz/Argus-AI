"""Tests for Broadcaster Agent: Telegram message formatting and broadcast handling."""
import pytest
from unittest.mock import patch, AsyncMock
from src.agents.broadcaster import (
    markdown_bullets_to_html,
    prepare_telegram_message,
    send_telegram_broadcast,
    broadcast_node,
)
from config.settings import settings

SAMPLE_REPORT = """# 🛰️ Argus-AI: Günlük Yapay Zeka İstihbarat Raporu
**Tarih:** 2026-10-21 | **Dil:** Türkçe | **Kaynak:** 12 analiz

## ⚡ Yönetici Özeti (TL;DR)
* OpenAI yeni o3 mimarisini tanıttı; reasoning maliyeti **%40** düştü.
* Google Gemini 2.0 Flash agentic modüllerde liderliği devraldı.
* Meta Llama 4 önizlemesini geliştirici ekosistemine açtı.

---

## 🔬 Teknik İncelemeler ve Mimari Analizler

### [OpenAI o3 Modelini Duyurdu](https://openai.com/index/o3)
- **Kategori:** Büyük Dil Modelleri
- **Mimari:** Düşünce zinciri optimizasyonu yapıldı.

### [Gemini 2.0 Flash Güncellemesi](https://deepmind.google/technologies/gemini)
- **Kategori:** Agent Altyapısı
- **Mimari:** Subagent orkestrasyonu güçlendirildi.

### [Llama 4 Önizlemesi](https://ai.meta.com/blog/llama-4)
- **Kategori:** Açık Kaynak AI
- **Mimari:** MoE mimarisiyle eğitildi.
"""

def test_markdown_bullets_to_html():
    md = "* **Madde 1:** Açıklama\n* **Madde 2:** *Önemli* detay"
    formatted = markdown_bullets_to_html(md)
    assert "• <b>Madde 1:</b> Açıklama" in formatted
    assert "• <b>Madde 2:</b> <i>Önemli</i> detay" in formatted
    assert "*" not in formatted

def test_prepare_telegram_message_structure():
    msg = prepare_telegram_message(SAMPLE_REPORT, "2026-10-21")
    
    # Check Header
    assert "Argus-AI — Günlük Yapay Zeka Bülteni" in msg
    assert "2026-10-21" in msg
    
    # Check Executive Summary
    assert "⚡ <b>Yönetici Özeti (TL;DR):</b>" in msg
    assert "OpenAI yeni o3 mimarisini tanıttı" in msg
    
    # Check Headlines
    assert "📚 <b>Öne Çıkan Başlıklar:</b>" in msg
    assert '<a href="https://openai.com/index/o3">OpenAI o3 Modelini Duyurdu</a>' in msg
    assert '<a href="https://deepmind.google/technologies/gemini">Gemini 2.0 Flash Güncellemesi</a>' in msg
    assert '<a href="https://ai.meta.com/blog/llama-4">Llama 4 Önizlemesi</a>' in msg
    
    # Check Archive link
    assert "https://github.com/hamzamalikyildiz/Argus-AI/blob/main/reports/2026/10/2026-10-21-daily-brief.md" in msg

def test_prepare_telegram_message_length_safety():
    # Construct huge report with 200 items
    huge_report = "## ⚡ Yönetici Özeti (TL;DR)\n" + ("* Önemli gelişme detayı satırı.\n" * 200)
    msg = prepare_telegram_message(huge_report, "2026-10-21")
    assert len(msg) <= 4000
    assert "Raporun Tamamını ve Teknik Analizleri Oku" in msg

@pytest.mark.asyncio
async def test_send_telegram_broadcast_missing_credentials():
    with patch.object(settings, "telegram_bot_token", None), \
         patch.object(settings, "telegram_chat_id", None):
        result = await send_telegram_broadcast("test message", bot_token=None, chat_id=None)
        assert result is False

@pytest.mark.asyncio
async def test_send_telegram_broadcast_success():
    with patch("httpx.AsyncClient.post") as mock_post:
        mock_post.return_value = AsyncMock(status_code=200)
        result = await send_telegram_broadcast(
            "test message",
            bot_token="fake_bot_token",
            chat_id="@test_channel"
        )
        assert result is True

@pytest.mark.asyncio
async def test_broadcast_node_execution():
    state = {
        "final_report_md": SAMPLE_REPORT,
        "report_date": "2026-10-21"
    }
    with patch("src.agents.broadcaster.send_telegram_broadcast", new_callable=AsyncMock) as mock_send:
        mock_send.return_value = True
        res = await broadcast_node(state)
        assert res["telegram_broadcast_sent"] is True
        mock_send.assert_called_once()

@pytest.mark.asyncio
async def test_send_apology_and_reports():
    from src.agents.broadcaster import send_apology_and_reports
    with patch("src.agents.broadcaster.send_telegram_broadcast", new_callable=AsyncMock) as mock_send:
        mock_send.return_value = True
        ok = await send_apology_and_reports(dates=["2026-10-21"])
        assert ok is True
        # Called at least twice: 1 apology + 1 report
        assert mock_send.call_count >= 2
        apology_call = mock_send.call_args_list[0][0][0]
        assert "Özür Mesajı" in apology_call
        assert "Gemini 3.8 Flash" in apology_call
