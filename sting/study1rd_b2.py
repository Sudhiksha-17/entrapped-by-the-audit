"""Study 1R-D fresh Cell B on a new provider (human message 88; prereg_study1r/AMENDMENT_1RD_ADDENDUM_1.md).
No frozen file is changed.

The first Cell B (DeepInfra) was stopped (I-066). The fresh Cell B runs the same three arms (Silent, Silent-floor,
Offer-floor; N = 33; indices 0-32) on the provider chosen by the addendum's speed-test rule, under its own campaign
(`configs/study1r_addon_D_b2/campaign.yaml`) and its own lock (`prereg_study1r/FROZEN_1RD_B2.json`). Everything it runs
is the frozen Study 1R-D code: `sting.study1rd.install` (StingSeller1RC, per-arm G2 checks, consecutive-API-failure
stop). The lock hashes the amendment, addendum 1, the new campaign and configs and the new code, plus the SHA-256 of
FROZEN.json (Study 1R), FROZEN_1RC.json (Study 1R-C) and FROZEN_1RD.json (Study 1R-D), and `verify` re-verifies all three.

Usage:
    python -m sting.study1rd_b2 freeze --campaign configs/study1r_addon_D_b2/campaign.yaml
    python -m sting.study1rd_b2 verify --campaign configs/study1r_addon_D_b2/campaign.yaml
    python -m sting.study1rd_b2 run configs/study1r_addon_D_b2/campaign.yaml --purpose "..." [--indices 0] [--arms A,B]
                                    [--approve-cost] [--estimate-only] [--skip-replacement]
"""
from __future__ import annotations

import argparse
import hashlib
import json
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Optional

import yaml

from sting import freeze_prereg, study1rd
from sting.paths import REPO_ROOT, RUNS_DIR

LOCK_NAME = "FROZEN_1RD_B2.json"
STUDY1RD_CAMPAIGN = Path("configs/study1r_addon_D/campaign.yaml")
FILES = ["prereg_study1r/AMENDMENT_1RD.md", "prereg_study1r/AMENDMENT_1RD_ADDENDUM_1.md", "sting/study1rd_b2.py",
         "scripts/make_study1rd_b2_configs.py"]


def campaign_files(campaign_path: Path, root: Path = REPO_ROOT) -> list[str]:
    camp = yaml.safe_load((root / campaign_path).read_text(encoding="utf-8"))
    return [str(Path(campaign_path).as_posix())] + [str(Path(a["config"]).as_posix()) for a in camp["arms"]] + FILES


def _base(root: Path) -> dict[str, str]:
    d = study1rd.verify(STUDY1RD_CAMPAIGN, root)          # also re-verifies FROZEN.json and FROZEN_1RC.json
    return {"study1r_lock_sha256": d["study1r_lock_sha256"], "study1rc_lock_sha256": d["study1rc_lock_sha256"],
            "study1rd_lock_sha256": d["sha256_of_lock"]}


def freeze(campaign_path: Path, root: Path = REPO_ROOT) -> dict[str, Any]:
    out = subprocess.run(["git", "-C", str(root), "status", "--porcelain"], capture_output=True, text=True).stdout
    if any(l.strip() for l in out.splitlines()):
        raise freeze_prereg.PreregNotFrozen("refusing to freeze with uncommitted changes")
    commit = subprocess.run(["git", "-C", str(root), "rev-parse", "HEAD"], capture_output=True, text=True).stdout.strip()
    lock = {"frozen_utc": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"), "git_commit": commit,
            "campaign": str(Path(campaign_path).as_posix()), "campaigns": [str(Path(campaign_path).as_posix())],
            **_base(root), "files_sha256": freeze_prereg.hashes(campaign_files(campaign_path, root), root)}
    with open(root / "prereg_study1r" / LOCK_NAME, "x", encoding="utf-8") as f:
        json.dump(lock, f, indent=2)
    return lock


def verify(campaign_path: Path, root: Path = REPO_ROOT) -> dict[str, Any]:
    path = root / "prereg_study1r" / LOCK_NAME
    if not path.is_file():
        raise freeze_prereg.PreregNotFrozen(f"prereg_study1r/{LOCK_NAME} not found: the fresh Cell B is not frozen")
    lock = json.loads(path.read_text(encoding="utf-8"))
    if str(Path(campaign_path).as_posix()) not in lock["campaigns"]:
        raise freeze_prereg.PreregNotFrozen(f"{LOCK_NAME} is for {lock['campaigns']}, not {campaign_path}")
    for k, v in _base(root).items():
        if lock.get(k) != v:
            raise freeze_prereg.PreregNotFrozen(f"{k} differs from the one recorded at the fresh Cell B freeze")
    current = freeze_prereg.hashes(list(lock["files_sha256"]), root)
    changed = [f for f, h in lock["files_sha256"].items() if current[f] != h]
    missing = [f for f in campaign_files(campaign_path, root) if f not in lock["files_sha256"]]
    if changed or missing:
        raise freeze_prereg.PreregNotFrozen(f"fresh Cell B frozen files changed {changed} or not covered {missing}")
    lock["sha256_of_lock"] = hashlib.sha256(path.read_bytes()).hexdigest()
    return lock


def main(argv: Optional[list[str]] = None) -> None:
    p = argparse.ArgumentParser(description="Study 1R-D fresh Cell B: freeze, verify or run.")
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
    r.add_argument("--arms", type=lambda s: s.split(","), default=None)
    a = p.parse_args(argv)
    if a.action == "freeze":
        print(json.dumps(freeze(a.campaign), indent=2))
    elif a.action == "verify":
        print(json.dumps(verify(a.campaign), indent=2))
    else:
        from sting.stage2_runner import run_campaign
        study1rd.install(stop_dir=RUNS_DIR / "study1r_addon_D_b2" / "_campaigns")
        out = run_campaign(a.campaign, a.purpose, approve_cost=a.approve_cost, estimate_only=a.estimate_only,
                           only_indices=a.indices, skip_replacement=a.skip_replacement, frozen_check=verify,
                           only_arms=a.arms, command="python -m sting.study1rd_b2 " + " ".join(sys.argv[1:]))
        print(json.dumps({k: v for k, v in out.items() if k != "arm_summaries"}, indent=2))


if __name__ == "__main__":
    main()
