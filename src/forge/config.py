"""Application configuration.

Every environment-dependent value is read from the environment and validated on
startup. Nothing is hardcoded, so the same code runs against the office GPU
(Ollama) or a cloud provider by changing one variable.
"""

from __future__ import annotations

from enum import StrEnum
from functools import lru_cache

from pydantic import Field, SecretStr
from pydantic_settings import BaseSettings, SettingsConfigDict


class LLMProvider(StrEnum):
    """Which backend the LLM gateway talks to."""

    OLLAMA = "ollama"
    GROQ = "groq"
    GEMINI = "gemini"


class Settings(BaseSettings):
    """Validated application settings, loaded from the environment or `.env`."""

    model_config = SettingsConfigDict(
        env_file=".env",
        env_prefix="FORGE_",
        env_file_encoding="utf-8",
        extra="ignore",
    )

    environment: str = "local"
    log_level: str = "INFO"

    llm_provider: LLMProvider = LLMProvider.OLLAMA

    ollama_base_url: str = "http://localhost:11434/v1"
    ollama_model: str = "qwen3.5:9b"

    groq_api_key: SecretStr | None = None
    groq_model: str = "llama-3.3-70b-versatile"

    gemini_api_key: SecretStr | None = None
    gemini_model: str = "gemini-2.0-flash"

    request_timeout_s: float = Field(default=300.0, gt=0)


@lru_cache(maxsize=1)
def get_settings() -> Settings:
    """Return the process-wide settings, built once and cached."""
    return Settings()
