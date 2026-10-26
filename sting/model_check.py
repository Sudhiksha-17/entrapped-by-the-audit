"""Model availability check: one minimal call per model (CLAUDE.md credit rule 4).

Each model gets exactly one API attempt with a very small max_tokens. Models whose
provider key is not present are reported as skipped, with no call made.

Usage:
    python -m sting.model_check configs/model_check.yaml --purpose "..."
"""
from __future__ import annotations

import argparse
import json
import os
import sys
import uuid
from pathlib import Path
from typing import Any, Optional

import yaml

from sting.clients import PROVIDER_KEY_ENV, RetryPolicy, UsageTracker, make_client
from sting.docs import docs_root_for, record_run
from sting.env import load_env
from sting.minimal_runner import utc_stamp, write_json
from sting.paths import RUNS_DIR

PROMPT = [{"role": "user", "content": "Reply with the single word OK."}]


def check_models(cfg: dict[str, Any], runs_dir: Path = RUNS_DIR, purpose: str = "test run",
                 command: str = "check_models()") -> dict[str, Any]:
    env_info = load_env()
    run_id = f"{utc_stamp()}_model_check_{uuid.uuid4().hex[:6]}"
    run_dir = runs_dir / "model_check" / run_id
    run_dir.mkdir(parents=True, exist_ok=False)
    results = []
    for spec in cfg["models"]:
        provider = spec["provider"]
        row: dict[str, Any] = {"provider": provider, "requested_model": spec["model"]}
        if provider != "fake" and not os.environ.get(PROVIDER_KEY_ENV[provider], "").strip():
            row.update(status="skipped", reason=f"{PROVIDER_KEY_ENV[provider]} not present")
            results.append(row)
            continue
        tracker = UsageTracker(max_attempts_total=1)
        client = make_client({**spec, "json_mode": False}, tracker, agent_id="model_check", role="check",
                             temperature=0.0, max_tokens=int(cfg.get("max_tokens", 5)),
                             retry=RetryPolicy(max_attempts=1))
        try:
            text = client.generate(PROMPT)
            row.update(status="available", reply=text)
        except Exception as exc:  # noqa: BLE001 - report every failure as data
            row.update(status="error", error=f"{type(exc).__name__}: {exc}")
        rec = tracker.as_dicts()[0] if tracker.records else {}
        row.update({k: rec.get(k) for k in ("returned_model", "routed_provider", "pinned_provider", "tokens_in",
                                            "tokens_out", "cost_usd_reported", "latency_s")})
        row["response_meta"] = getattr(client, "last_response_meta", None)
        results.append(row)
    out = {"run_id": run_id, "finished_utc": utc_stamp(), "max_tokens": int(cfg.get("max_tokens", 5)),
           "env_file_used": env_info["env_file"], "keys_present": env_info["present"],
        "key_sources": env_info["key_sources"], "overridden_environment_keys": env_info["overridden_environment_keys"], "results": results}
    write_json(run_dir / "model_check.json", out)
    record_run(run_dir, purpose, command, docs_root=docs_root_for(runs_dir))
    return out


def main(argv: Optional[list[str]] = None) -> None:
    parser = argparse.ArgumentParser(description="One minimal call per model.")
    parser.add_argument("config", type=Path)
    parser.add_argument("--purpose", required=True, help="Why this check is being made (recorded in the lab notebook).")
    args = parser.parse_args(argv)
    cfg = yaml.safe_load(args.config.read_text(encoding="utf-8"))
    print(json.dumps(check_models(cfg, purpose=args.purpose,
                                  command="python -m sting.model_check " + " ".join(sys.argv[1:])), indent=2))


if __name__ == "__main__":
    main()
