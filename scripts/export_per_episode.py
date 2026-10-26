"""Per-episode results tables for the public release (human message 82 step 6). No API calls; read-only on runs.

One CSV per study, one row per episode attempted in the confirmatory campaign logs (status column; failed episodes
are listed and marked, as in the analyses that exclude them):
- Study 1: `sting.stage2_measures.price_measures` (the frozen Study 1 measures) per replicate directory.
- Study 1R, 1R-A, 1R-C: the frozen `build` of scripts/study1r_results.py on the completed episodes (D-116 wrapper
  staging; failed episodes get a row with status, failure reason and replacement only), with Labeler
  A's verify coding for the Study 1R main study (as in the analysis), no judge inputs (judge outputs are released
  separately). Nested fields are flattened; per-round and per-seller acceptance maps are left out.
- Study 1R-D: Cell A only (the two mini-low arms of the finished campaign logs; Cell B is not analysed, I-066, I-070),
  same build. The raw runs live in the Study 1R-D worktree; pass its runs/ directory as the second argument.

Usage: python scripts/export_per_episode.py <out_dir> [<study1r_D_runs_dir>]
"""
from __future__ import annotations

import csv
import importlib.util
import json
import sys
import tempfile
from pathlib import Path

import yaml

SCRIPTS = Path(__file__).resolve().parent
REPO = SCRIPTS.parent
sys.path.insert(0, str(REPO))
from sting.stage2_measures import price_measures  # noqa: E402

STUDY1R_FIELDS = ["replicate_id", "replicate_index", "status", "failure_reason", "cell", "arm", "condition",
                  "paraphrase", "pre", "pre_source", "post", "change", "x", "x_source", "jump", "behavioral_acceptance",
                  "missing_llm_asks_post_window", "ack_rate", "probe_q2_seller_a", "probe_q2_seller_b",
                  "engaged_any_detector", "first_engagement_round_detector", "coding", "verification_messages",
                  "verification_dropped", "verification_uncoded", "acc_inclusive", "acc_strict",
                  "acc_inclusive_11_12", "audit_accept", "test_suspicion_share", "replaced_by"]
STUDY1_EXTRA = ["cell", "arm"]


def load(name: str, mod: str):
    spec = importlib.util.spec_from_file_location(mod, SCRIPTS / name)
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


def logs(sub: str) -> list[Path]:
    return sorted((REPO / "runs" / sub / "_campaigns").glob("*/campaign.json"))


def rel_run_dirs(log: Path) -> dict[str, Path]:
    return {name: Path(info["run_dir"]) for name, info in json.loads(log.read_text(encoding="utf-8"))["arms"].items()}


def write(rows: list[dict], fields: list[str], out: Path) -> int:
    with out.open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=fields, extrasaction="ignore")
        w.writeheader()
        for r in rows:
            w.writerow({k: r.get(k) for k in fields})
    return len(rows)


def study1(out: Path) -> int:
    arms = {a["name"]: (a["cell"], a["arm"]) for a in
            yaml.safe_load((REPO / "configs/stage2/campaign.yaml").read_text(encoding="utf-8"))["arms"]}
    rows = []
    for log in logs("stage2"):
        for name, d in rel_run_dirs(log).items():
            for rep in sorted(p for p in d.iterdir() if p.is_dir()):
                rows.append({**price_measures(rep), "cell": arms[name][0], "arm": arms[name][1]})
    fields = ["replicate_id", "replicate_index", *STUDY1_EXTRA] + [k for k in rows[0] if k not in
                                                                    ("replicate_id", "replicate_index", *STUDY1_EXTRA)]
    return write(rows, fields, out)


def study1r_family(yaml_path: str, sub: str, out: Path, human: dict, strata: dict, protected: frozenset,
                   camp_logs: list[Path] | None = None) -> int:
    res = load("study1r_results.py", f"res_exp_{sub}")
    wrap = load("study1r_results_completed.py", f"wrap_exp_{sub}")
    arms = {a["name"]: (a["cell"], a["arm"]) for a in
            yaml.safe_load((REPO / yaml_path).read_text(encoding="utf-8"))["arms"]}
    with tempfile.TemporaryDirectory(prefix="exp_") as tmp:
        staged, excluded = wrap.stage(logs(sub) if camp_logs is None else camp_logs, Path(tmp))
        eps = res.build([REPO / yaml_path], staged, human, strata, {}, {}, False, protected)
    eps += [{"replicate_id": x["replicate_id"], "status": x["status"], "failure_reason": x["failure_reason"],
             "cell": arms[x["arm"]][0], "arm": arms[x["arm"]][1], "replaced_by": x["replaced_by_completed"]}
            for x in excluded]
    for e in eps:
        probe = e.get("probe") or {}
        e["probe_q2_seller_a"], e["probe_q2_seller_b"] = probe.get("Seller A"), probe.get("Seller B")
    return write(eps, STUDY1R_FIELDS, out)


def main() -> None:
    out = Path(sys.argv[1])
    out.mkdir(parents=True, exist_ok=True)
    res = load("study1r_results.py", "res_exp")
    human, strata, protected = res.verify_labels(REPO / "results/study1r/labeling/main/verify",
                                                 REPO / "results/study1r/labeling_keys/main/verify")
    n = {"study1_episodes.csv": study1(out / "study1_episodes.csv"),
         "study1r_main_episodes.csv": study1r_family("configs/study1r/campaign.yaml", "study1r",
                                                     out / "study1r_main_episodes.csv", human, strata, protected),
         "study1r_addon_A_episodes.csv": study1r_family("configs/study1r_addon_A/campaign.yaml", "study1r_addon_A",
                                                        out / "study1r_addon_A_episodes.csv", {}, {}, frozenset()),
         "study1r_addon_C_episodes.csv": study1r_family("configs/study1r_addon_C/campaign.yaml", "study1r_addon_C",
                                                        out / "study1r_addon_C_episodes.csv", {}, {}, frozenset())}
    if len(sys.argv) > 2:
        with tempfile.TemporaryDirectory(prefix="exp_d_") as tmp:
            a_logs = []
            camps = sorted((Path(sys.argv[2]) / "study1r_addon_D" / "_campaigns").glob("*/campaign.json"))
            for i, log in enumerate(p for p in camps if "finished_utc" in p.read_text(encoding="utf-8")):
                d = json.loads(log.read_text(encoding="utf-8"))
                d["arms"] = {k: v for k, v in d["arms"].items() if k in ("mini-low_offer_floor", "mini-low_silent_floor")}
                if d["arms"]:
                    q = Path(tmp) / f"c{i:02d}.json"
                    q.write_text(json.dumps(d), encoding="utf-8")
                    a_logs.append(q)
            n["study1r_addon_D_cellA_episodes.csv"] = study1r_family(
                "configs/study1r_addon_D/campaign.yaml", "study1r_addon_D", out / "study1r_addon_D_cellA_episodes.csv",
                {}, {}, frozenset(), a_logs)
    print(json.dumps(n, indent=1))


if __name__ == "__main__":
    main()
