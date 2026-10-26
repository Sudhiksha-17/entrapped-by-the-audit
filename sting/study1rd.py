"""Study 1R-D, the sting's words with its pricing held fixed (human message 86; prereg_study1r/AMENDMENT_1RD.md).
No frozen file is changed.

Arms: Offer-floor (the Study 1R Offer arm: talking sting, ASK/ACK rule, pricing max(X, follow) from round 10),
Silent-floor (the Study 1R-C Silent-floor arm) and, in Cell B, Silent. This module adds, without editing any frozen file:
- `g2_checks_1rd`: per arm, the frozen Study 1R checks for message arms (Offer-floor: messages in every prompt rounds
  11-30, ASK/ACK recomputation, X placement, pricing) and the Study 1R-C checks for silent arms (`g2_checks_1rc`: frozen
  checks plus no posts, silent condition, floor as specified);
- the consecutive-API-failure stop: three episodes in a row (completion order) failing with an API-related reason
  (api_failure, provider_mismatch, attempt_cap) stop the campaign (`ConsecutiveApiFailures` is raised; no further
  episode starts; the stop is written to `runs/<stage>/_campaigns/STOPPED_*.json`);
- `install()`: the frozen runner builds StingSeller1RC (Study 1R-C; it only adds the Silent-floor floor) and runs
  g2_checks_1rd, and `sting.stage2_runner.run_episode` is wrapped with the failure counter, for this process only;
- `freeze` / `verify`: prereg_study1r/FROZEN_1RD.json (amendment, campaign, arm configs, new or changed code) plus the
  SHA-256 of FROZEN.json (Study 1R) and FROZEN_1RC.json (Study 1R-C); `verify` re-verifies both locks.

Usage:
    python -m sting.study1rd freeze --campaign configs/study1r_addon_D/campaign.yaml
    python -m sting.study1rd verify --campaign configs/study1r_addon_D/campaign.yaml
    python -m sting.study1rd run configs/study1r_addon_D/campaign.yaml --purpose "..." [--indices 0] [--approve-cost]
                                 [--estimate-only] [--skip-replacement] [--arms A,B]
"""
from __future__ import annotations

import argparse
import hashlib
import json
import subprocess
import sys
import threading
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Optional

import yaml

from sting import freeze_prereg, study1rc
from sting.paths import REPO_ROOT, RUNS_DIR

LOCK_NAME = "FROZEN_1RD.json"
STUDY1R_CAMPAIGN = Path("configs/study1r/campaign.yaml")
STUDY1RC_CAMPAIGN = Path("configs/study1r_addon_C/campaign.yaml")
CODE_1RD = ["sting/study1rd.py", "scripts/make_study1rd_configs.py", "scripts/study1r_results_1rd.py",
            "scripts/study1r_results_completed.py", "scripts/study1r_checkpoint.py", "scripts/study1r_health.py"]
AMENDMENT = "prereg_study1r/AMENDMENT_1RD.md"
API_REASONS = {"api_failure", "provider_mismatch", "attempt_cap"}
MAX_CONSECUTIVE_API_FAILURES = 3


class ConsecutiveApiFailures(RuntimeError):
    """Three episodes in a row failed for API reasons; the campaign stops (amendment section 7)."""


def g2_checks_1rd(rep_dir: Path, record: dict[str, Any], llm_ids: list[str], max_len: int) -> dict[str, Any]:
    if record.get("condition") == "silent":
        return study1rc.g2_checks_1rc(rep_dir, record, llm_ids, max_len)
    out = study1rc._FROZEN_G2(rep_dir, record, llm_ids, max_len)
    problems = list(out["problems"])
    if record.get("condition") != "offer" or record.get("competitive") is not None:
        problems.append("message arm is not the offer condition with the follow rule")
    if (record.get("x_rule") or {}).get("silent_floor"):
        problems.append("silent_floor flag in a message arm")
    out["problems"], out["passed"] = problems, not problems
    return out


class FailureGuard:
    """Counts consecutive API-failed episodes in completion order; thread-safe."""

    def __init__(self, limit: int = MAX_CONSECUTIVE_API_FAILURES) -> None:
        self.limit, self.run, self.tripped, self.lock = limit, 0, False, threading.Lock()

    def before(self) -> None:
        if self.tripped:
            raise ConsecutiveApiFailures("campaign stopped after consecutive API failures")

    def after(self, status: dict[str, Any]) -> None:
        with self.lock:
            if status.get("status") != "completed" and status.get("failure_reason") in API_REASONS:
                self.run += 1
            elif status.get("status") == "completed" or status.get("failure_reason") not in API_REASONS:
                self.run = 0
            if self.run >= self.limit:
                self.tripped = True


_GUARD: Optional[FailureGuard] = None


def install(guard: Optional[FailureGuard] = None, stop_dir: Optional[Path] = None) -> FailureGuard:
    """Study 1R-D process only."""
    global _GUARD
    import sting.minimal_runner as mr
    import sting.stage2_runner as sr
    from sting import study1r_checks
    study1rc.install()                                   # StingSeller1RC; keeps the frozen G2 reference
    study1r_checks.g2_checks = g2_checks_1rd
    _GUARD = guard or FailureGuard()
    original = getattr(sr.run_episode, "__wrapped_1rd__", sr.run_episode)

    def run_episode(*args, **kwargs):
        _GUARD.before()
        status = original(*args, **kwargs)
        _GUARD.after(status)
        if _GUARD.tripped:
            d = stop_dir or (RUNS_DIR / "study1r_addon_D" / "_campaigns")
            d.mkdir(parents=True, exist_ok=True)
            (d / f"STOPPED_{datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%SZ')}.json").write_text(json.dumps(
                {"reason": "consecutive API failures", "limit": _GUARD.limit, "last": status.get("replicate_id")},
                indent=2), encoding="utf-8")
            raise ConsecutiveApiFailures(f"{_GUARD.limit} consecutive API-failed episodes; last {status.get('replicate_id')}")
        return status

    run_episode.__wrapped_1rd__ = original
    sr.run_episode = run_episode
    mr.StingSeller = study1rc.StingSeller1RC
    return _GUARD


def campaign_files(campaign_path: Path, root: Path = REPO_ROOT) -> list[str]:
    camp = yaml.safe_load((root / campaign_path).read_text(encoding="utf-8"))
    return [AMENDMENT, str(Path(campaign_path).as_posix())] + [str(Path(a["config"]).as_posix()) for a in camp["arms"]] \
        + CODE_1RD


def _base_locks(root: Path) -> dict[str, str]:
    s1r = freeze_prereg.verify(STUDY1R_CAMPAIGN, root)
    s1rc = study1rc.verify(STUDY1RC_CAMPAIGN, root)
    return {"study1r_lock_sha256": s1r["sha256_of_lock"], "study1rc_lock_sha256": s1rc["sha256_of_lock"]}


def freeze(campaign_path: Path, root: Path = REPO_ROOT, uncommitted: Optional[list[str]] = None) -> dict[str, Any]:
    if uncommitted is None:
        out = subprocess.run(["git", "-C", str(root), "status", "--porcelain"], capture_output=True, text=True).stdout
        uncommitted = [l for l in out.splitlines() if l.strip()]
    if uncommitted:
        raise freeze_prereg.PreregNotFrozen("refusing to freeze with uncommitted changes:\n  " + "\n  ".join(uncommitted))
    if "[[BLANK" in (root / AMENDMENT).read_text(encoding="utf-8"):
        raise freeze_prereg.PreregNotFrozen(f"refusing to freeze: {AMENDMENT} has [[BLANK]] markers")
    base = _base_locks(root)
    commit = subprocess.run(["git", "-C", str(root), "rev-parse", "HEAD"], capture_output=True, text=True).stdout.strip()
    lock = {"frozen_utc": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"), "git_commit": commit,
            "campaign": str(Path(campaign_path).as_posix()), "campaigns": [str(Path(campaign_path).as_posix())], **base,
            "files_sha256": freeze_prereg.hashes(campaign_files(campaign_path, root), root)}
    with open(root / "prereg_study1r" / LOCK_NAME, "x", encoding="utf-8") as f:
        json.dump(lock, f, indent=2)
    return lock


def verify(campaign_path: Path, root: Path = REPO_ROOT) -> dict[str, Any]:
    path = root / "prereg_study1r" / LOCK_NAME
    if not path.is_file():
        raise freeze_prereg.PreregNotFrozen(f"prereg_study1r/{LOCK_NAME} not found: Study 1R-D is not frozen")
    lock = json.loads(path.read_text(encoding="utf-8"))
    if str(Path(campaign_path).as_posix()) not in lock["campaigns"]:
        raise freeze_prereg.PreregNotFrozen(f"{LOCK_NAME} is for {lock['campaigns']}, not {campaign_path}")
    base = _base_locks(root)
    for k, v in base.items():
        if lock.get(k) != v:
            raise freeze_prereg.PreregNotFrozen(f"{k} differs from the one recorded at the 1R-D freeze")
    current = freeze_prereg.hashes(list(lock["files_sha256"]), root)
    changed = [f for f, h in lock["files_sha256"].items() if current[f] != h]
    missing = [f for f in campaign_files(campaign_path, root) if f not in lock["files_sha256"]]
    if changed or missing:
        raise freeze_prereg.PreregNotFrozen(f"Study 1R-D frozen files changed {changed} or not covered {missing}")
    lock["sha256_of_lock"] = hashlib.sha256(path.read_bytes()).hexdigest()
    return lock


def main(argv: Optional[list[str]] = None) -> None:
    p = argparse.ArgumentParser(description="Study 1R-D: freeze, verify or run.")
    sub = p.add_subparsers(dest="action", required=True)
    for name in ("freeze", "verify"):
        s = sub.add_parser(name)
        s.add_argument("--campaign", type=Path, required=True)
    r = sub.add_parser("run")
    r.add_argument("campaign", type=Path)
    r.add_argument("--purpose", required=True)
    r.add_argument("--estimate-only", action="store_true")
    r.add_argument("--approve-cost", action="store_true")
    r.add_argument("--indices", type=lambda s: [int(x) for x in s.split(",")], default=None)
    r.add_argument("--skip-replacement", action="store_true")
    r.add_argument("--arms", type=lambda s: s.split(","), default=None,
                   help="restrict to these arm names (parallel invocations, amendment section 7)")
    a = p.parse_args(argv)
    if a.action == "freeze":
        print(json.dumps(freeze(a.campaign), indent=2))
    elif a.action == "verify":
        print(json.dumps(verify(a.campaign), indent=2))
    else:
        from sting.stage2_runner import run_campaign
        install()
        out = run_campaign(a.campaign, a.purpose, approve_cost=a.approve_cost, estimate_only=a.estimate_only,
                           only_indices=a.indices, skip_replacement=a.skip_replacement, frozen_check=verify, only_arms=a.arms,
                           command="python -m sting.study1rd " + " ".join(sys.argv[1:]))
        print(json.dumps({k: v for k, v in out.items() if k != "arm_summaries"}, indent=2))


if __name__ == "__main__":
    main()
