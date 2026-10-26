"""Minimal .env loader.

Never prints, logs or returns key values. Callers only learn which variables are
present and non-empty.
"""
from __future__ import annotations

import os
from pathlib import Path
from typing import Optional

from sting.paths import REPO_ROOT

# Searched in order; the first file found is used. The parent directory is
# included because the human's .env currently lives there (outside any repo).
ENV_SEARCH_PATHS = [REPO_ROOT / ".env", REPO_ROOT.parent / ".env"]

KNOWN_KEYS = ["OPENAI_API_KEY", "ANTHROPIC_API_KEY", "OPENROUTER_API_KEY", "GOOGLE_PROJECT_ID"]


def _parse_env_file(path: Path) -> dict[str, str]:
    values: dict[str, str] = {}
    for raw in path.read_text(encoding="utf-8").splitlines():
        line = raw.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        if line.startswith("export "):
            line = line[len("export "):]
        key, _, value = line.partition("=")
        value = value.strip().strip('"').strip("'")
        values[key.strip()] = value
    return values


def load_env(search_paths: Optional[list[Path]] = None) -> dict:
    """Load the first .env found into os.environ.

    API keys (KNOWN_KEYS) in the .env override any value already in the environment,
    so the .env is the single place keys live (ISSUES I-020). Other variables do not
    override existing ones. Also defaults WANDB_MODE to 'disabled' (D-005, D-011).

    Returns {"env_file", "present": {key: bool}, "key_sources": {key: ".env" | "environment" | None},
    "overridden_environment_keys": [key, ...]}. Never returns values.
    """
    used = None
    sources: dict[str, Optional[str]] = {k: ("environment" if os.environ.get(k, "").strip() else None)
                                         for k in KNOWN_KEYS}
    overridden: list[str] = []
    for path in ENV_SEARCH_PATHS if search_paths is None else search_paths:
        if path.is_file():
            for key, value in _parse_env_file(path).items():
                if key in KNOWN_KEYS and value:
                    if os.environ.get(key) not in (None, "", value):
                        overridden.append(key)
                    os.environ[key] = value
                    sources[key] = ".env"
                elif key not in os.environ:
                    os.environ[key] = value
            used = str(path)
            break
    os.environ.setdefault("WANDB_MODE", "disabled")
    return {"env_file": used, "present": key_presence(), "key_sources": sources,
            "overridden_environment_keys": overridden}


def key_presence() -> dict[str, bool]:
    return {key: bool(os.environ.get(key, "").strip()) for key in KNOWN_KEYS}
