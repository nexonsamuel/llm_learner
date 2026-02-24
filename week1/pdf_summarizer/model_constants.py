"""
Model configuration constants for PDF summarizer.
Centralized configuration for different LLM providers and models.

API keys are loaded from environment variables for security.
"""

import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

MODEL_CONFIGS = {
    "tinyllama": {
        "name": "tinyllama",
        "base_url": "http://localhost:11434/v1",
        "api_key": "ollama",  # Local Ollama doesn't need a real key
        "context_window": 2048,
        "provider": "ollama",
    },
    "gpt-4": {
        "name": "gpt-4",
        "base_url": "https://api.openai.com/v1",
        "api_key": os.getenv("OPENAI_API_KEY"),
        "context_window": 8192,
        "provider": "openai",
    },
    "gpt-4-turbo": {
        "name": "gpt-4-turbo-preview",
        "base_url": "https://api.openai.com/v1",
        "api_key": os.getenv("OPENAI_API_KEY"),
        "context_window": 128000,
        "provider": "openai",
    },
    "gpt-3.5-turbo": {
        "name": "gpt-3.5-turbo",
        "base_url": "https://api.openai.com/v1",
        "api_key": os.getenv("OPENAI_API_KEY"),
        "context_window": 4096,
        "provider": "openai",
    },
    "claude-3-sonnet": {
        "name": "claude-3-sonnet-20240229",
        "base_url": "https://api.anthropic.com/v1",
        "api_key": os.getenv("ANTHROPIC_API_KEY"),
        "context_window": 200000,
        "provider": "anthropic",
    },
    "claude-3-opus": {
        "name": "claude-3-opus-20240229",
        "base_url": "https://api.anthropic.com/v1",
        "api_key": os.getenv("ANTHROPIC_API_KEY"),
        "context_window": 200000,
        "provider": "anthropic",
    },
    "llama-2": {
        "name": "llama2",
        "base_url": "http://localhost:11434/v1",
        "api_key": "ollama",  # Local Ollama doesn't need a real key
        "context_window": 4096,
        "provider": "ollama",
    },
    "mistral": {
        "name": "mistral",
        "base_url": "http://localhost:11434/v1",
        "api_key": "ollama",  # Local Ollama doesn't need a real key
        "context_window": 8192,
        "provider": "ollama",
    },
}

# Default configuration
DEFAULT_MODEL = "tinyllama"
DEFAULT_SAFETY_FACTOR = 0.30  # Use 30% of context window for input chunks

# Supported tokenizers
TOKENIZERS = {
    "openai": "cl100k_base",
    "ollama": "cl100k_base",  # TinyLlama compatible
    "anthropic": "anthropic",  # Requires Anthropic's tokenizer
}

# Progress bar styling
PROGRESS_BAR_STYLE = "cyan"
SPINNER_STYLE = "blue"