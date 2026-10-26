"""Study 1R-C, pricing-control add-on (human message 79; prereg_study1r/AMENDMENT_1RC.md). No frozen file is changed.

Arms (cells mini-low and 4.1-high): Silent-floor (Seller C posts no message; rounds 1-9 follow rule; from round 10 its
ask is max(X, follow), X computed exactly as in Study 1R) and a concurrent Silent (follow rule, no message).

The Study 1R code is frozen (prereg_study1r/FROZEN.json, 47 files) and stays byte-identical. This module adds, without
editing it:
- `StingSeller1RC`: a subclass of the frozen StingSeller. With `x_rule["silent_floor"]` true (Silent-floor configs only)
  it sets the price floor to X from the X round in the silent condition, exactly as the frozen class does for Anchor and
  Offer (set_x); everything else is inherited. The flag is part of x_rule, so the runner passes it through unchanged
  and sting_log.json records it.
- `g2_checks_1rc`: the frozen G2 checks (which already verify the sting's ask against max(price_floor, follow) from
  floor_from_round whenever a price floor is logged) plus three Study 1R-C checks: no sting posts; the condition is
  silent with no competitive rule; the price floor equals X from round 10 in Silent-floor and is absent in Silent.
- `install()`: points the frozen runner's StingSeller name and G2 check at these two (the runner looks both up at call
  time), for the Study 1R-C process only.
- `freeze` / `verify`: prereg_study1r/FROZEN_1RC.json with the SHA-256 of the amendment, the Study 1R-C configs and the
  new or changed code; `verify` also re-verifies the Study 1R lock (prereg_study1r/FROZEN.json), so the frozen code the
  add-on runs on is unchanged. The frozen campaign runner (`python -m sting.stage2_runner`) refuses a Study 1R-C
  campaign, because it is not a campaign of FROZEN.json; Study 1R-C runs only through `python -m sting.study1rc run`.

Usage:
    python -m sting.study1rc freeze --campaign configs/study1r_addon_C/campaign.yaml
    python -m sting.study1rc verify --campaign configs/study1r_addon_C/campaign.yaml
    python -m sting.study1rc run configs/study1r_addon_C/campaign.yaml --purpose "..." [--indices 0] [--approve-cost]
                                 [--estimate-only] [--skip-replacement]
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

from sting import freeze_prereg
from sting.paths import REPO_ROOT
from sting.sting_seller import StingSeller

LOCK_NAME = "FROZEN_1RC.json"
STUDY1R_CAMPAIGN = Path("configs/study1r/campaign.yaml")
# New or changed code for Study 1R-C (everything else it runs is in the Study 1R lock).
CODE_1RC = ["sting/study1rc.py", "scripts/make_study1rc_configs.py", "scripts/study1r_results_1rc.py",
            "scripts/study1r_results_completed.py", "scripts/study1r_checkpoint.py", "scripts/study1r_health.py"]
AMENDMENT = "prereg_study1r/AMENDMENT_1RC.md"


class StingSeller1RC(StingSeller):
    def model_post_init(self, __context: Any) -> None:
        super().model_post_init(__context)
        if (self.x_rule or {}).get("silent_floor") and (self.condition != "silent" or self.competitive is not None):
            raise ValueError("x_rule.silent_floor (Study 1R-C) requires the silent condition and no competitive rule")

    def set_x(self, history: list[dict[str, Any]]) -> None:
        super().set_x(history)
        if (self.x_rule or {}).get("silent_floor"):
            self.price_floor, self.floor_from_round = self.x_log["x"], int(self.x_rule["round"])


def g2_checks_1rc(rep_dir: Path, record: dict[str, Any], llm_ids: list[str], max_len: int) -> dict[str, Any]:
    from sting import study1r_checks
    out = (_FROZEN_G2 or study1r_checks.g2_checks)(rep_dir, record, llm_ids, max_len)
    floor_arm = bool((record.get("x_rule") or {}).get("silent_floor"))
    problems = list(out["problems"])
    out["sting_posts"] = len(record.get("messages_sent") or [])
    if out["sting_posts"]:
        problems.append("sting posted a message")
    if record.get("condition") != "silent" or record.get("competitive") is not None:
        problems.append("not the silent condition with the follow rule")
    x = (record.get("x") or {}).get("x")
    if floor_arm:
        ok = record.get("price_floor") == x and record.get("floor_from_round") == int(record["x_rule"]["round"])
        out["floor_check"] = {"arm": "silent_floor", "price_floor": record.get("price_floor"), "x": x,
                              "floor_from_round": record.get("floor_from_round"), "passed": ok}
    else:
        ok = record.get("price_floor") is None
        out["floor_check"] = {"arm": "silent", "price_floor": record.get("price_floor"), "passed": ok}
    if not ok:
        problems.append("price floor not as specified for the arm")
    out["problems"] = problems
    out["passed"] = not problems
    return out


_FROZEN_G2 = None


def install() -> None:
    """Study 1R-C process only: the frozen runner builds StingSeller1RC and runs g2_checks_1rc."""
    global _FROZEN_G2
    import sting.minimal_runner as mr
    from sting import study1r_checks
    if _FROZEN_G2 is None:
        _FROZEN_G2 = study1r_checks.g2_checks
    mr.StingSeller = StingSeller1RC
    study1r_checks.g2_checks = g2_checks_1rc


def campaign_files(campaign_path: Path, root: Path = REPO_ROOT) -> list[str]:
    camp = yaml.safe_load((root / campaign_path).read_text(encoding="utf-8"))
    return [AMENDMENT, str(Path(campaign_path).as_posix())] + [str(Path(a["config"]).as_posix()) for a in camp["arms"]] \
        + CODE_1RC


def freeze(campaign_path: Path, root: Path = REPO_ROOT, uncommitted: Optional[list[str]] = None,
           study1r_campaign: Path = STUDY1R_CAMPAIGN) -> dict[str, Any]:
    if uncommitted is None:
        out = subprocess.run(["git", "-C", str(root), "status", "--porcelain"], capture_output=True, text=True).stdout
        uncommitted = [l for l in out.splitlines() if l.strip()]
    if uncommitted:
        raise freeze_prereg.PreregNotFrozen("refusing to freeze with uncommitted changes:\n  " + "\n  ".join(uncommitted))
    if "[[BLANK" in (root / AMENDMENT).read_text(encoding="utf-8"):
        raise freeze_prereg.PreregNotFrozen(f"refusing to freeze: {AMENDMENT} has [[BLANK]] markers")
    base = freeze_prereg.verify(study1r_campaign, root)  # the frozen Study 1R code must be unchanged
    commit = subprocess.run(["git", "-C", str(root), "rev-parse", "HEAD"], capture_output=True, text=True).stdout.strip()
    lock = {"frozen_utc": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"), "git_commit": commit,
            "campaign": str(Path(campaign_path).as_posix()), "campaigns": [str(Path(campaign_path).as_posix())],
            "study1r_lock_sha256": base["sha256_of_lock"],
            "files_sha256": freeze_prereg.hashes(campaign_files(campaign_path, root), root)}
    with open(root / "prereg_study1r" / LOCK_NAME, "x", encoding="utf-8") as f:
        json.dump(lock, f, indent=2)
    return lock


def verify(campaign_path: Path, root: Path = REPO_ROOT, study1r_campaign: Path = STUDY1R_CAMPAIGN) -> dict[str, Any]:
    path = root / "prereg_study1r" / LOCK_NAME
    if not path.is_file():
        raise freeze_prereg.PreregNotFrozen(f"prereg_study1r/{LOCK_NAME} not found: Study 1R-C is not frozen")
    lock = json.loads(path.read_text(encoding="utf-8"))
    if str(Path(campaign_path).as_posix()) not in lock["campaigns"]:
        raise freeze_prereg.PreregNotFrozen(f"{LOCK_NAME} is for {lock['campaigns']}, not {campaign_path}")
    base = freeze_prereg.verify(study1r_campaign, root)
    if base["sha256_of_lock"] != lock["study1r_lock_sha256"]:
        raise freeze_prereg.PreregNotFrozen("prereg_study1r/FROZEN.json differs from the one recorded at the 1R-C freeze")
    current = freeze_prereg.hashes(list(lock["files_sha256"]), root)
    changed = [f for f, h in lock["files_sha256"].items() if current[f] != h]
    missing = [f for f in campaign_files(campaign_path, root) if f not in lock["files_sha256"]]
    if changed or missing:
        raise freeze_prereg.PreregNotFrozen(f"Study 1R-C frozen files changed {changed} or not covered {missing}")
    lock["sha256_of_lock"] = hashlib.sha256(path.read_bytes()).hexdigest()
    return lock


def main(argv: Optional[list[str]] = None) -> None:
    p = argparse.ArgumentParser(description="Study 1R-C: freeze, verify or run (pricing-control add-on).")
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
    a = p.parse_args(argv)
    if a.action == "freeze":
        print(json.dumps(freeze(a.campaign), indent=2))
    elif a.action == "verify":
        print(json.dumps(verify(a.campaign), indent=2))
    else:
        from sting.stage2_runner import run_campaign
        install()
        out = run_campaign(a.campaign, a.purpose, approve_cost=a.approve_cost, estimate_only=a.estimate_only,
                           only_indices=a.indices, skip_replacement=a.skip_replacement, frozen_check=verify,
                           command="python -m sting.study1rc " + " ".join(sys.argv[1:]))
        print(json.dumps({k: v for k, v in out.items() if k != "arm_summaries"}, indent=2))


if __name__ == "__main__":
    main()
