"""Freeze the preregistration (prereg/stage2_spec.md section 12, step 4) and verify it before confirmatory runs.

`freeze` writes prereg/FROZEN.json with the SHA-256 of every file that defines Stage 2 (prereg, spec, messages
and judge file, stimuli, judge config, prompts, the campaign config and every arm config it lists) plus the git
commit. It refuses if the working tree has uncommitted changes, if the prereg still contains "[[BLANK", or if
FROZEN.json already exists. The human then commits FROZEN.json locally; the freeze is that local commit plus the
recorded hashes (no git remote; human message 20).

`verify` (called by the confirmatory campaign runner) recomputes the hashes and refuses on any mismatch.

Parameterized per study (I-045): the campaign config's `prereg_dir` selects the study ("prereg" for Study 1, the
default when absent; "prereg_study1r" for Study 1R). The study's PREREG.md and FROZEN.json live in that directory, and
its base file list is BASE_FILES_BY_DIR[prereg_dir]. A Study 1R campaign is therefore never checked against Study 1's
freeze, and Study 1's freeze is unchanged.

Usage:
    python -m sting.freeze_prereg freeze --campaign configs/stage2_campaign.yaml
    python -m sting.freeze_prereg verify --campaign configs/stage2_campaign.yaml
"""
from __future__ import annotations

import argparse
import hashlib
import json
import subprocess
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Optional

import yaml

from sting.paths import REPO_ROOT

BASE_FILES = ["prereg/PREREG.md", "prereg/stage2_spec.md", "prereg/stage2_message_and_judge.md",
              "configs/stage2_stimuli.yaml", "configs/judge.yaml", "sting/prompts/volume_message.txt",
              "sting/prompts/judge_prompt.jinja2"]
STUDY1R_FILES = ["prereg_study1r/PREREG.md", "prereg_study1r/STUDY1R_SPEC.md", "prereg_study1r/STUDY1R_STIMULI.md",
                 "configs/study1r_stimuli.yaml", "configs/judge_v2.yaml", "sting/prompts/volume_message.txt",
                 "sting/prompts/judge_v2.jinja2"]
# Human message 65: Study 1R also freezes its code. Entry points (the human's list, plus the campaign runner, the
# judge v1 comparison script and this module), and the full import closure over sting/ and scripts/ computed by
# sting.code_closure; tests/test_study1r_batch.py checks that this list equals the computed closure.
STUDY1R_CODE_ENTRIES = ['sting/study1r_analysis.py', 'scripts/study1r_results.py', 'sting/probe.py', 'scripts/study1r_label_sets.py', 'scripts/study1r_backup_reliability.py', 'scripts/study1r_judge_v2_offer.py', 'sting/study1r_gates.py', 'sting/minimal_runner.py', 'sting/sting_seller.py', 'sting/stage2_runner.py', 'scripts/study1r_judge_v1_compare.py', 'sting/freeze_prereg.py']
STUDY1R_CODE = [
    "scripts/stage2_labeling_sheet.py",
    "scripts/study1r_backup_reliability.py",
    "scripts/study1r_judge_v1_compare.py",
    "scripts/study1r_judge_v2_offer.py",
    "scripts/study1r_label_sets.py",
    "scripts/study1r_results.py",
    "scripts/study1r_validation.py",
    "sting/clients.py",
    "sting/docs.py",
    "sting/env.py",
    "sting/freeze_prereg.py",
    "sting/judge.py",
    "sting/judge_v2.py",
    "sting/label_tool.py",
    "sting/minimal_runner.py",
    "sting/paths.py",
    "sting/probe.py",
    "sting/prompt_mirror.py",
    "sting/stage2_analysis.py",
    "sting/stage2_measures.py",
    "sting/stage2_runner.py",
    "sting/sting_seller.py",
    "sting/study1r_analysis.py",
    "sting/study1r_checks.py",
    "sting/study1r_gates.py",
    "sting/study1r_measures.py",
    "sting/study1r_stimuli.py",
]
STUDY1R_FILES = STUDY1R_FILES + STUDY1R_CODE
BASE_FILES_BY_DIR = {"prereg": BASE_FILES, "prereg_study1r": STUDY1R_FILES}


def prereg_dir_of(campaign_path: Path, root: Path = REPO_ROOT) -> str:
    campaign = yaml.safe_load((root / campaign_path).read_text(encoding="utf-8"))
    d = campaign.get("prereg_dir", "prereg")
    if d not in BASE_FILES_BY_DIR:
        raise PreregNotFrozen(f"unknown prereg_dir {d!r}")
    return d


class PreregNotFrozen(RuntimeError):
    pass


def campaign_files(campaign_path: Path, root: Path = REPO_ROOT) -> list[str]:
    campaign = yaml.safe_load((root / campaign_path).read_text(encoding="utf-8"))
    rel = str(Path(campaign_path).as_posix())
    base = BASE_FILES_BY_DIR[campaign.get("prereg_dir", "prereg")]
    return base + [rel] + [str(Path(a["config"]).as_posix()) for a in campaign["arms"]]


def frozen_campaigns(campaign_path: Path, root: Path = REPO_ROOT) -> list[str]:
    """The campaign plus any campaigns it lists under `also_freeze` (Study 1R: the add-on Study 1R-A campaign is
    preregistered in the same freeze; human message 52)."""
    campaign = yaml.safe_load((root / campaign_path).read_text(encoding="utf-8"))
    return [str(Path(campaign_path).as_posix())] + [str(Path(c).as_posix()) for c in campaign.get("also_freeze", [])]


def all_files(campaign_path: Path, root: Path = REPO_ROOT) -> list[str]:
    files: list[str] = []
    for c in frozen_campaigns(campaign_path, root):
        files += [f for f in campaign_files(Path(c), root) if f not in files]
    return files


def hashes(files: list[str], root: Path = REPO_ROOT) -> dict[str, str]:
    return {f: hashlib.sha256((root / f).read_bytes()).hexdigest() for f in files}


def freeze(campaign_path: Path, root: Path = REPO_ROOT, uncommitted: Optional[list[str]] = None) -> dict[str, Any]:
    if uncommitted is None:
        out = subprocess.run(["git", "-C", str(root), "status", "--porcelain"], capture_output=True, text=True).stdout
        uncommitted = [l for l in out.splitlines() if l.strip()]
    if uncommitted:
        raise PreregNotFrozen("refusing to freeze with uncommitted changes:\n  " + "\n  ".join(uncommitted))
    d = prereg_dir_of(campaign_path, root)
    prereg = (root / d / "PREREG.md").read_text(encoding="utf-8")
    if "[[BLANK" in prereg:
        raise PreregNotFrozen(f"refusing to freeze: {d}/PREREG.md has {prereg.count('[[BLANK')} [[BLANK]] markers")
    commit = subprocess.run(["git", "-C", str(root), "rev-parse", "HEAD"], capture_output=True, text=True).stdout.strip()
    lock = {"frozen_utc": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"), "git_commit": commit,
            "campaign": str(Path(campaign_path).as_posix()), "campaigns": frozen_campaigns(campaign_path, root),
            "files_sha256": hashes(all_files(campaign_path, root), root)}
    with open(root / d / "FROZEN.json", "x", encoding="utf-8") as f:
        json.dump(lock, f, indent=2)
    return lock


def verify(campaign_path: Path, root: Path = REPO_ROOT) -> dict[str, Any]:
    d = prereg_dir_of(campaign_path, root)
    path = root / d / "FROZEN.json"
    if not path.is_file():
        raise PreregNotFrozen(f"{d}/FROZEN.json not found: the prereg is not frozen")
    lock = json.loads(path.read_text(encoding="utf-8"))
    if str(Path(campaign_path).as_posix()) not in lock.get("campaigns", [lock["campaign"]]):
        raise PreregNotFrozen(f"frozen for campaigns {lock.get('campaigns', [lock['campaign']])}, not {campaign_path}")
    current = hashes(list(lock["files_sha256"]), root)
    changed = [f for f, h in lock["files_sha256"].items() if current[f] != h]
    missing = [f for f in all_files(campaign_path, root) if f not in lock["files_sha256"]]
    if changed or missing:
        raise PreregNotFrozen(f"frozen files changed {changed} or not covered {missing}")
    lock["sha256_of_lock"] = hashlib.sha256(path.read_bytes()).hexdigest()
    return lock


def main(argv: Optional[list[str]] = None) -> None:
    parser = argparse.ArgumentParser(description="Freeze or verify the Stage 2 preregistration.")
    parser.add_argument("action", choices=["freeze", "verify"])
    parser.add_argument("--campaign", type=Path, required=True)
    args = parser.parse_args(argv)
    result = freeze(args.campaign) if args.action == "freeze" else verify(args.campaign)
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
