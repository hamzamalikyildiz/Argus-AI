from .curator import curate_articles
from .analyst import analyze_articles
from .reporter import synthesize_report
from .llm_factory import get_chat_model

def __getattr__(name):
    if name in ("audit_report_content", "audit_report_file", "audit_latest_report", "audit_node"):
        from . import auditor
        return getattr(auditor, name)
    if name in ("broadcast_node", "send_telegram_broadcast", "prepare_telegram_message"):
        from . import broadcaster
        return getattr(broadcaster, name)
    raise AttributeError(f"module {__name__!r} has no attribute {name!r}")

__all__ = [
    "curate_articles",
    "analyze_articles",
    "synthesize_report",
    "get_chat_model",
    "audit_report_content",
    "audit_report_file",
    "audit_latest_report",
    "audit_node",
    "broadcast_node",
    "send_telegram_broadcast",
    "prepare_telegram_message",
]

