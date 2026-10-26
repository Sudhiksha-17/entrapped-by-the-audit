"""Shared test setup. Tests never make real API calls (CLAUDE.md credit rule 1)."""
import socket
import sys
from pathlib import Path

import pytest

REPO_ROOT = Path(__file__).resolve().parent.parent
# Keep bytecode out of third_party/ (ISSUES I-014); must be set before any upstream import.
if sys.pycache_prefix is None:
    sys.pycache_prefix = str(REPO_ROOT / ".pycache")
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))


@pytest.fixture(autouse=True)
def no_network(monkeypatch):
    """Fail any test that tries to open a network connection."""
    def guard(*args, **kwargs):
        raise RuntimeError("network access is blocked in tests")
    monkeypatch.setattr(socket.socket, "connect", guard)
    monkeypatch.setattr(socket.socket, "connect_ex", guard)
    monkeypatch.setattr(socket, "create_connection", guard)


@pytest.fixture(autouse=True)
def no_real_keys(monkeypatch):
    """Remove real API keys from the test environment and stop .env loading."""
    for key in ["OPENAI_API_KEY", "ANTHROPIC_API_KEY", "OPENROUTER_API_KEY", "GOOGLE_PROJECT_ID"]:
        monkeypatch.delenv(key, raising=False)
    import sting.env
    monkeypatch.setattr(sting.env, "ENV_SEARCH_PATHS", [])
