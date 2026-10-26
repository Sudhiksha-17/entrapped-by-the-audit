"""Study 1R analysis on completed episodes only (post-freeze deviation, bug fix I-056; human approval, option 2).

The frozen `scripts/study1r_results.py` iterates every replicate directory of each arm run and so does not apply the
preregistered rule that failed episodes are excluded and replaced (PREREG.md section 11); it crashes on a failed
episode with no X. This wrapper leaves every frozen file unmodified and filters the input instead:

1. stage: copy each campaign log's arm runs into a temporary staging tree, keeping only replicate directories whose
   status.json says "completed", and write campaign logs pointing at the staged runs (only `run_dir` changes);
2. check: the excluded episodes (status not "completed") must equal --expect-excluded exactly, else STOP before any
   analysis; every excluded episode is listed with its status, failure reason and the replacement that completed;
3. call the frozen `study1r_results.main()` unchanged with the staged logs (all other arguments passed through);
4. add to RESULTS.md: the deviation and exclusion list at the top, the Labeler A vs B agreement and screener precision
   (frozen `scripts/study1r_backup_reliability.py`) when --agreement is given, and the full untruncated JSON of any
   section the frozen report truncated (it cuts each section at 4000 characters; results.json is complete).

Copies, not links, so removing the staging tree can never touch the source runs.

Usage:
  python scripts/study1r_results_completed.py --expect-excluded ID[,ID...] [--agreement A_S A_K B_S B_K]
         <the frozen script's arguments: OUT_DIR --campaign-yaml Y --logs L[,L...] --verify S K ...>
"""
from __future__ import annotations

import argparse
import csv
import importlib.util
import json
import shutil
import sys
import tempfile
from pathlib import Path

SCRIPTS = Path(__file__).resolve().parent
DEVIATION = ("Post-freeze deviation (bug fix, I-056): the frozen results script did not apply the preregistered rule "
             "that failed episodes are excluded and replaced. This run used `scripts/study1r_results_completed.py`, "
             "which passes only completed episodes to the frozen analysis; no frozen file was modified.")


def load(name: str, mod: str):
    spec = importlib.util.spec_from_file_location(mod, SCRIPTS / name)
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


def stage(logs: list[Path], staging: Path) -> tuple[list[Path], list[dict]]:
    """Copy completed episodes into `staging`; return the staged campaign logs and the excluded episodes."""
    new_logs, excluded, completed = [], [], {}
    for i, log in enumerate(logs):
        camp = json.loads(log.read_text(encoding="utf-8"))
        for j, (name, info) in enumerate(camp["arms"].items()):
            src = Path(info["run_dir"])
            # short staging names (Windows path limit); the frozen analysis keys on replicate directory names only
            dst = staging / f"c{i:02d}" / f"a{j:02d}"
            dst.mkdir(parents=True)
            for p in sorted(src.iterdir()):
                if not p.is_dir():
                    shutil.copy2(p, dst / p.name)
                    continue
                st = json.loads((p / "status.json").read_text(encoding="utf-8"))
                if st["status"] == "completed":
                    shutil.copytree(p, dst / p.name)
                    if st.get("replaces"):
                        completed[st["replaces"]] = p.name
                else:
                    excluded.append({"replicate_id": p.name, "arm": name, "status": st["status"],
                                     "failure_reason": st.get("failure_reason"), "campaign": log.parent.name})
            info["run_dir"] = str(dst)
        out = staging / f"c{i:02d}" / "campaign.json"
        out.write_text(json.dumps(camp, indent=2), encoding="utf-8")
        new_logs.append(out)
    for e in excluded:
        e["replaced_by_completed"] = completed.get(e["replicate_id"])
    return new_logs, excluded


def check(excluded: list[dict], expected: set[str]) -> None:
    got = {e["replicate_id"] for e in excluded}
    if got != expected:
        raise SystemExit(f"STOP: excluded episodes {sorted(got)} differ from --expect-excluded {sorted(expected)}; "
                         "no analysis run")


def screener_precision(sheet_a: Path, key_a: Path, sheet_b: Path) -> dict:
    """Post hoc (exploratory; the frozen miss_rates docstring names verification precision but does not output it):
    share of screener-positive (verification) messages human-coded accept or conditional_accept. Estimated on Labeler
    B's random 20% sample of the verification set, which the stopping rule never drops, by each labeler; also the
    counts of verification messages coded by Labeler A and dropped by the stopping rule."""
    sys.path.insert(0, str(SCRIPTS.parent))
    from sting.stage2_analysis import wilson
    from sting.study1r_measures import ACCEPT_INCLUSIVE
    rows_of = lambda d: {r["item_id"]: r for r in csv.DictReader((d / "labels_template.csv").open(newline="", encoding="utf-8"))}  # noqa: E731
    key = json.loads((key_a / "labeling_key.json").read_text(encoding="utf-8"))
    ra, rb = rows_of(sheet_a), rows_of(sheet_b)
    ver = [i for i, k in key.items() if k["stratum"] == "verification"]
    coded = [i for i in ver if ra[i]["response"]]
    sample = [i for i in ver if key[i].get("labeler_b")]
    ka = sum(ra[i]["response"] in ACCEPT_INCLUSIVE for i in sample)
    b = [r["response"] for r in rb.values() if r["response"]]
    kb = sum(r in ACCEPT_INCLUSIVE for r in b)
    return {"verification_messages": len(ver), "coded_by_labeler_a": len(coded),
            "dropped_by_stopping_rule": len(ver) - len(coded),
            "note": "the frozen miss audit's verification 'coded' count is messages minus uncoded, so it includes "
                    "messages dropped by the stopping rule",
            "labeler_b_sample": len(sample),
            "precision_labeler_a_on_b_sample": {"k": ka, "n": len(sample), "rate": ka / len(sample),
                                                "ci": list(wilson(ka, len(sample)))},
            "precision_labeler_b": {"k": kb, "n": len(b), "rate": kb / len(b), "ci": list(wilson(kb, len(b)))}}


def main() -> None:
    ap = argparse.ArgumentParser(add_help=False)
    ap.add_argument("--expect-excluded", required=True)
    ap.add_argument("--agreement", nargs=4, default=None)
    ap.add_argument("--logs", required=True)
    own, rest = ap.parse_known_args()
    expected = {x for x in own.expect_excluded.split(",") if x}
    out_dir = Path(rest[0])
    with tempfile.TemporaryDirectory(prefix="study1r_completed_") as tmp:
        logs, excluded = stage([Path(p) for p in own.logs.split(",") if p], Path(tmp))
        print("excluded (status not completed):")
        for e in excluded:
            print("  ", json.dumps(e))
        check(excluded, expected)
        res = load("study1r_results.py", "study1r_results_frozen")
        argv = sys.argv
        sys.argv = ["study1r_results.py", *rest, "--logs", ",".join(str(p) for p in logs)]
        try:
            res.main()
        finally:
            sys.argv = argv
    if "--dry-run" in rest:
        return
    report = out_dir / "RESULTS.md"
    text = report.read_text(encoding="utf-8")
    head, body = text.split("\n", 1)
    excl = ["## Excluded episodes (post-freeze deviation, I-056)", "", DEVIATION, ""] + [
        f"- `{e['replicate_id']}` ({e['arm']}): status {e['status']}, failure reason {e['failure_reason']}; "
        f"replaced by `{e['replaced_by_completed']}` (completed)" for e in excluded] + [""]
    tail = []
    if own.agreement:
        rel = load("study1r_backup_reliability.py", "study1r_reliability_frozen")
        agr = rel.agreement(*(Path(p) for p in own.agreement))
        (out_dir / "reliability").mkdir(exist_ok=True)
        (out_dir / "reliability" / "agreement_A_vs_B.json").write_text(json.dumps(agr, indent=2), encoding="utf-8")
        tail += ["## Labeler A vs Labeler B agreement (secondary; option A reliability, PREREG section 8)", "",
                 "From `scripts/study1r_backup_reliability.py agreement` (frozen).", "", "```json",
                 json.dumps(agr, indent=1), "```", ""]
    payload = json.loads((out_dir / "results.json").read_text(encoding="utf-8"))
    if own.agreement:
        prec = screener_precision(Path(own.agreement[0]), Path(own.agreement[1]), Path(own.agreement[2]))
        payload["screener_precision_post_hoc"] = prec
        tail += ["## Screener precision (exploratory, post hoc; not output by the frozen analysis)", "",
                 "Share of screener-positive messages human-coded accept or conditional_accept, on Labeler B's random "
                 "20% sample of the verification set (never dropped by the stopping rule).", "", "```json",
                 json.dumps(prec, indent=1), "```", ""]
    payload["excluded_episodes"], payload["deviation"] = excluded, DEVIATION
    (out_dir / "results.json").write_text(json.dumps(payload, indent=2, default=str), encoding="utf-8")
    long = {k: v for k, v in payload["results"].items() if len(json.dumps(v, indent=1, default=str)) > 4000}
    if long:
        tail += ["## Full output of sections truncated above (the frozen report cuts each at 4000 characters)", ""]
        for k, v in long.items():
            tail += [f"### {k}", "", "```json", json.dumps(v, indent=1, default=str), "```", ""]
    report.write_text("\n".join([head, "", *excl]) + body.rstrip("\n") + "\n\n" + "\n".join(tail), encoding="utf-8")


if __name__ == "__main__":
    main()
