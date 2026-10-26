"""Key safety check (human message 51, item 2). No model calls; prints masked keys only (first 8, last 4 characters).

Every model-calling component builds its client with sting.clients.make_client, whose `_api_key` runs load_env() and
refuses any key that does not come from the .env file. This script reports, per component, the call path, whether it
also records key sources in its run record, and the masked key it would use; it flags a Windows environment value
that differs from the .env key (that value is never used).

Usage: python scripts/key_safety_check.py
"""
from __future__ import annotations

import os
import sys
from pathlib import Path

ENV_BEFORE = os.environ.get("OPENROUTER_API_KEY", "").strip()      # read before .env is loaded

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from sting.env import load_env  # noqa: E402

COMPONENTS = [
    ("main runner (episodes, pilot campaigns)", "sting.minimal_runner.open_run -> load_env; clients via make_client",
     "run_config.json: env_file_used, key_sources"),
    ("awareness probe", "sting.probe (inside the episode run) -> make_client", "run_config.json of the episode run"),
    ("judge v2 (development, G3, confirmatory)", "sting.judge_v2.run_judge_v2 -> load_env; make_client",
     "judge_run.json: key_sources"),
    ("judge v1 comparison (frozen Study 1 judge)", "sting.judge.run_judge -> load_env; make_client",
     "judge_run.json: key_sources"),
    ("model check", "sting.model_check -> load_env; make_client", "model_check.json"),
    ("pilot tools (gate report, label sets)", "no model calls", "n/a"),
]


def mask(k: str) -> str:
    return f"{k[:8]}...{k[-4:]}" if len(k) >= 12 else ("<unset>" if not k else "<short>")


def main() -> None:
    info = load_env()
    key = os.environ.get("OPENROUTER_API_KEY", "").strip()
    print(f".env file: {info['env_file']}; OPENROUTER_API_KEY source: {info['key_sources'].get('OPENROUTER_API_KEY')}")
    print(f".env key (masked): {mask(key)}")
    if ENV_BEFORE:
        same = ENV_BEFORE == key
        print(f"Windows environment also sets OPENROUTER_API_KEY: {mask(ENV_BEFORE)} "
              f"({'same as .env' if same else 'DIFFERENT from .env; never used: make_client refuses non-.env keys'})")
    for name, path, record in COMPONENTS:
        uses = "none" if path == "no model calls" else mask(key)
        print(f"- {name}: key {uses}; path: {path}; recorded in: {record}")


if __name__ == "__main__":
    main()
