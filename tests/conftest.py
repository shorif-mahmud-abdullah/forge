"""Shared pytest fixtures.

Configuration tests must not be influenced by the developer's own `.env` file or
shell variables, so every test runs in a clean temporary directory with all
FORGE_* variables removed.
"""

from __future__ import annotations

import os
from pathlib import Path

import pytest


@pytest.fixture(autouse=True)
def isolated_env(monkeypatch: pytest.MonkeyPatch, tmp_path: Path) -> None:
    for key in [k for k in os.environ if k.startswith("FORGE_")]:
        monkeypatch.delenv(key, raising=False)
    monkeypatch.chdir(tmp_path)
