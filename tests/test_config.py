"""Phase 0 smoke tests: configuration loads, validates and rejects bad input."""

from __future__ import annotations

import pytest
from pydantic import ValidationError

from forge.config import LLMProvider, Settings, get_settings


def test_defaults_point_at_local_ollama() -> None:
    settings = Settings()
    assert settings.llm_provider is LLMProvider.OLLAMA
    assert settings.ollama_base_url.endswith("/v1")


def test_provider_is_read_from_the_environment(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setenv("FORGE_LLM_PROVIDER", "groq")
    assert Settings().llm_provider is LLMProvider.GROQ


def test_unknown_provider_is_rejected(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setenv("FORGE_LLM_PROVIDER", "chatgpt-deluxe")
    with pytest.raises(ValidationError):
        Settings()


def test_timeout_must_be_positive(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setenv("FORGE_REQUEST_TIMEOUT_S", "0")
    with pytest.raises(ValidationError):
        Settings()


def test_secrets_are_not_exposed_in_repr(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setenv("FORGE_GROQ_API_KEY", "super-secret-value")
    assert "super-secret-value" not in repr(Settings())


def test_get_settings_is_cached() -> None:
    get_settings.cache_clear()
    assert get_settings() is get_settings()
