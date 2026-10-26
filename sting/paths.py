"""Repository paths and upstream import setup.

Upstream imports its own modules as ``src.<...>`` (PHASE_1.md, Imports), so the
upstream root must be on ``sys.path``. Our package is ``sting`` at the repo root,
so the two never collide.
"""
from __future__ import annotations

import subprocess
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
UPSTREAM_ROOT = REPO_ROOT / "third_party" / "llm-agent-collusion"
RUNS_DIR = REPO_ROOT / "runs"


def ensure_upstream_on_path() -> None:
    """Make ``import src.continuous_double_auction...`` resolve to the pinned upstream clone.

    Bytecode caches are redirected to ``.pycache/`` in our repo so importing upstream
    never writes ``__pycache__`` folders into third_party/ (ISSUES I-014).
    """
    if sys.pycache_prefix is None:
        sys.pycache_prefix = str(REPO_ROOT / ".pycache")
    upstream = str(UPSTREAM_ROOT)
    if upstream not in sys.path:
        sys.path.append(upstream)


def upstream_commit() -> str:
    """Return the commit hash of the upstream clone, or 'unknown' if git is unavailable."""
    try:
        out = subprocess.run(
            ["git", "-C", str(UPSTREAM_ROOT), "rev-parse", "HEAD"],
            capture_output=True, text=True, check=True,
        )
        return out.stdout.strip()
    except (OSError, subprocess.CalledProcessError):
        return "unknown"
