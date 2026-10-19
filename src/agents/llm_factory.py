"""LLM Factory supporting both Google Gemini and OpenAI with tiered model capabilities."""
import os
import logging
from typing import Any
from langchain_core.language_models.chat_models import BaseChatModel

from config.settings import settings

logger = logging.getLogger(__name__)

def get_chat_model(role: str = "curator", temperature: float = 0.2) -> BaseChatModel:
    """
    Returns an instantiated LangChain Chat model based on provider and role.
    
    Roles:
      - 'curator': Fast, low-latency, cost-effective model (e.g. Gemini 2.0 Flash / GPT-4o-mini)
      - 'analyst': Deep reasoning model for architecture, math, code & benchmarks (e.g. Gemini 2.0 Pro / GPT-4o)
    """
    provider = settings.llm_provider.lower().strip()
    
    if provider == "gemini":
        from langchain_google_genai import ChatGoogleGenerativeAI
        
        api_key = settings.gemini_api_key or os.getenv("GEMINI_API_KEY") or os.getenv("GOOGLE_API_KEY")
        if not api_key:
            raise ValueError(
                "GEMINI_API_KEY is not set in environment or .env file. "
                "Please configure GEMINI_API_KEY or switch LLM_PROVIDER to 'openai'."
            )
        
        model_name = settings.curator_model if role == "curator" else settings.analyst_model
        if not model_name:
            model_name = "gemini-3.8-flash" if role == "curator" else "gemini-3.8-flash"

        # Auto-map deprecated versions to active Google Gemini 3.8 models
        model_mapping = {
            "gemini-2.0-flash": "gemini-3.8-flash",
            "gemini-1.5-flash": "gemini-3.8-flash",
            "gemini-2.0-pro": "gemini-3.8-flash",
            "gemini-1.5-pro": "gemini-3.8-flash",
            "gemini-pro": "gemini-3.8-flash",
        }
        model_name = model_mapping.get(model_name.lower().strip(), model_name)

        logger.info(f"Initializing Gemini model '{model_name}' for role '{role}'")
        return ChatGoogleGenerativeAI(
            model=model_name,
            google_api_key=api_key,
            temperature=temperature
        )

    elif provider == "openai":
        from langchain_openai import ChatOpenAI
        
        api_key = settings.openai_api_key or os.getenv("OPENAI_API_KEY")
        if not api_key:
            raise ValueError(
                "OPENAI_API_KEY is not set in environment or .env file. "
                "Please configure OPENAI_API_KEY or switch LLM_PROVIDER to 'gemini'."
            )
        
        model_name = settings.curator_model if role == "curator" else settings.analyst_model
        if not model_name:
            model_name = "gpt-4o-mini" if role == "curator" else "gpt-4o"

        logger.info(f"Initializing OpenAI model '{model_name}' for role '{role}'")
        return ChatOpenAI(
            model=model_name,
            api_key=api_key,
            temperature=temperature
        )

    else:
        raise ValueError(f"Unsupported LLM_PROVIDER '{provider}'. Must be 'gemini' or 'openai'.")
