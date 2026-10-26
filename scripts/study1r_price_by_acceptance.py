"""Study 1R exploratory, descriptive (human message 76; no tests; no frozen file changed). No API calls.

4.1-high, three groups: Offer episodes with human-confirmed inclusive acceptance, Offer episodes without it, Silent.
Episode records come from the frozen `build` of scripts/study1r_results.py on completed episodes only (the D-116
wrapper's staging), so pre, X and acceptance are the analysis' own values. Per-round ask = mean of the posted
LLM-seller asks in that round; a window mean is the mean of per-round asks over rounds that have one
(sting.stage2_measures.window_mean, as for pre and post).

1. pre (rounds 6-9) per group.
2. change from pre over rounds 11-20 and over rounds 21-30 (window mean minus pre) per group.
3. accepting episodes: first round with a human-confirmed acceptance (accept or conditional_accept on a verification
   message); mean ask over the 3 rounds before it and the 3 rounds after it (the round itself excluded; windows
   clipped to rounds 1-30). The verify sheet was coded in shuffled order under the hidden stopping rule, so a
   screener-positive message in an earlier round may have been dropped uncoded; for each episode the earliest
   verification-message round and whether an earlier one was dropped are reported with it.
4. X - pre per group (X is computed and logged in every arm, Silent included).

CIs: 95% percentile bootstrap over episodes (10,000 resamples, seed 20261025).

Usage: python scripts/study1r_price_by_acceptance.py <out_dir> <campaign.yaml> <campaign.json>[,...] <verify_sheet> <verify_key>
"""
from __future__ import annotations

import importlib.util
import json
import sys
import tempfile
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from sting.stage2_measures import rounds_of, window_mean  # noqa: E402
from sting.study1r_measures import ACCEPT_INCLUSIVE  # noqa: E402

SCRIPTS = Path(__file__).resolve().parent
CELL = "4.1-high"
SEED = 20261025
GROUPS = [("accept", "Offer, human-confirmed acceptance"), ("no_accept", "Offer, no confirmed acceptance"),
          ("silent", "Silent")]


def load(name: str, mod: str):
    spec = importlib.util.spec_from_file_location(mod, SCRIPTS / name)
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


def summary(values: list[float], rng: np.random.Generator) -> dict:
    v = np.array(values, dtype=float)
    boot = v[rng.integers(0, v.size, size=(10_000, v.size))].mean(axis=1)
    return {"n": int(v.size), "mean": float(v.mean()), "ci": [float(np.quantile(boot, 0.025)),
                                                              float(np.quantile(boot, 0.975))]}


def first_acceptance(rep: str, human: dict, strata: dict) -> dict:
    ver = sorted(r for (rid, _, r), g in strata.items() if rid == rep and g == "verification")
    acc = sorted(r for (rid, _, r), lab in human.items()
                 if rid == rep and strata.get((rid, _, r)) == "verification" and lab["response"] in ACCEPT_INCLUSIVE)
    first = acc[0] if acc else None
    dropped_earlier = sorted({r for (rid, s, r), g in strata.items() if rid == rep and g == "verification"
                              and r < first and (rid, s, r) not in human}) if first else []
    return {"first_confirmed_round": first, "earliest_verification_round": ver[0] if ver else None,
            "dropped_verification_rounds_before_first": dropped_earlier}


def collect(campaign_yaml: Path, logs: list[Path], sheet: Path, key: Path) -> tuple[dict, list]:
    wrap = load("study1r_results_completed.py", "wrap_pba")
    res = load("study1r_results.py", "res_pba")
    human, strata, protected = res.verify_labels(sheet, key)
    groups = {g: [] for g, _ in GROUPS}
    with tempfile.TemporaryDirectory(prefix="s1r_pba_") as tmp:
        staged, excluded = wrap.stage(logs, Path(tmp))
        episodes = res.build([campaign_yaml], staged, human, strata, {}, {}, False, protected)
        dirs = {}
        for log in staged:
            for info in json.loads(log.read_text(encoding="utf-8"))["arms"].values():
                for rep in Path(info["run_dir"]).iterdir():
                    if rep.is_dir():
                        dirs[rep.name] = rep
        for e in episodes:
            if e["cell"] != CELL or e["arm"] not in ("offer", "silent"):
                continue
            rep = dirs[e["replicate_id"]]
            rounds = rounds_of(rep)
            llm = json.loads((rep / "sting_log.json").read_text(encoding="utf-8"))["llm_seller_ids"]
            rec = {"replicate_id": e["replicate_id"], "pre": e["pre"], "pre_source": e["pre_source"], "x": e["x"],
                   "x_minus_pre": e["jump"],
                   "change_11_20": window_mean(rounds, llm, range(11, 21)) - e["pre"],
                   "change_21_30": window_mean(rounds, llm, range(21, 31)) - e["pre"]}
            if e["arm"] == "silent":
                groups["silent"].append(rec)
                continue
            if not e.get("acc_inclusive"):
                groups["no_accept"].append(rec)
                continue
            fa = first_acceptance(e["replicate_id"], human, strata)
            r = fa["first_confirmed_round"]
            before, after = range(max(1, r - 3), r), range(r + 1, min(30, r + 3) + 1)
            rec.update(fa, before_rounds=[before.start, before.stop - 1],
                       after_rounds=[after.start, after.stop - 1] if len(after) else [],
                       ask_before=window_mean(rounds, llm, before),
                       ask_after=window_mean(rounds, llm, after) if len(after) else None)
            groups["accept"].append(rec)
    return groups, [x["replicate_id"] for x in excluded]


def analyse(groups: dict) -> dict:
    rng = np.random.default_rng(SEED)
    out = {"label": "exploratory, descriptive (no tests)", "cell": CELL, "groups": {}}
    for g, label in GROUPS:
        eps = groups[g]
        out["groups"][g] = {"label": label, "n": len(eps),
                            "pre_source_fallback": sum(e["pre_source"] != "pre_rounds" for e in eps),
                            **{k: summary([e[k] for e in eps], rng)
                               for k in ("pre", "change_11_20", "change_21_30", "x_minus_pre")}}
    acc = groups["accept"]
    both = [e for e in acc if e["ask_after"] is not None]
    out["first_acceptance"] = {
        "rounds": sorted(e["first_confirmed_round"] for e in acc),
        "ask_before": summary([e["ask_before"] for e in both], rng),
        "ask_after": summary([e["ask_after"] for e in both], rng),
        "after_minus_before": summary([e["ask_after"] - e["ask_before"] for e in both], rng),
        "episodes_without_after_window": len(acc) - len(both),
        "episodes_with_short_after_window": sum(e["ask_after"] is not None and e["after_rounds"][1] - e["after_rounds"][0] < 2
                                                for e in acc),
        "episodes_with_dropped_earlier_verification": sum(bool(e["dropped_verification_rounds_before_first"]) for e in acc),
        "per_episode": acc}
    return out


def fmt(s: dict, money: bool = False) -> str:
    p = "$" if money else ""
    sign = "" if money else "+"
    return f"{p}{s['mean']:{sign}.2f} ({p}{s['ci'][0]:{sign}.2f}, {p}{s['ci'][1]:{sign}.2f})"


def report(res: dict, excluded: list) -> str:
    G = res["groups"]
    fa = res["first_acceptance"]
    L = ["# Study 1R, 4.1-high: price levels by confirmed acceptance (exploratory, descriptive)", "",
         "Human message 76. No tests. Completed episodes, frozen `build` episode records (D-116 staging; excluded: "
         f"{', '.join(excluded) or 'none'}). Ask = round mean of posted LLM-seller asks. CIs: 95% percentile bootstrap over "
         "episodes (10,000 resamples, seed 20261025). Script: `scripts/study1r_price_by_acceptance.py`. Facts only.", "",
         "## Per group", "",
         "| Group | N | Pre, rounds 6-9 | Change from pre, rounds 11-20 | Change from pre, rounds 21-30 | X - pre |",
         "|---|---|---|---|---|---|"]
    for g, d in G.items():
        L.append(f"| {d['label']} | {d['n']} | {fmt(d['pre'], True)} | {fmt(d['change_11_20'])} | "
                 f"{fmt(d['change_21_30'])} | {fmt(d['x_minus_pre'])} |")
    L += ["", "Pre from the fallback (most recent asks before round 10): "
          + "; ".join(f"{d['label']} {d['pre_source_fallback']}" for d in G.values()) + ".", "",
          "## Accepting episodes: first confirmed acceptance", "",
          f"First round with a human-confirmed acceptance (N = {len(fa['rounds'])}): "
          + ", ".join(str(r) for r in fa["rounds"]) + ".", "",
          f"Mean ask, 3 rounds before vs 3 rounds after (round itself excluded; N = {fa['ask_before']['n']}): before "
          f"{fmt(fa['ask_before'], True)}; after {fmt(fa['ask_after'], True)}; after minus before "
          f"{fmt(fa['after_minus_before'])}. Episodes without an after window (first confirmed round 30, excluded from these means): "
          f"{fa['episodes_without_after_window']}; with an after window shorter than 3 rounds (clipped at round 30): "
          f"{fa['episodes_with_short_after_window']}.", "",
          "Coding order caveat: the verify sheet was coded in shuffled order under the hidden stopping rule. Episodes in "
          f"which a verification (screener-positive) message in a round before the first confirmed acceptance was dropped "
          f"uncoded: {fa['episodes_with_dropped_earlier_verification']} of {len(fa['rounds'])}.", "",
          "| Episode | First confirmed round | Earliest verification round | Dropped verification rounds before it | "
          "Ask before | Ask after |", "|---|---|---|---|---|---|"]
    for e in sorted(fa["per_episode"], key=lambda e: e["replicate_id"]):
        aa = f"${e['ask_after']:.2f}" if e["ask_after"] is not None else "n/a"
        L.append(f"| {e['replicate_id'][-4:]} | {e['first_confirmed_round']} | {e['earliest_verification_round']} | "
                 f"{', '.join(map(str, e['dropped_verification_rounds_before_first'])) or 'none'} | "
                 f"${e['ask_before']:.2f} | {aa} |")
    return "\n".join(L) + "\n"


def main() -> None:
    out_dir, cy = Path(sys.argv[1]), Path(sys.argv[2])
    logs = [Path(p) for p in sys.argv[3].split(",") if p]
    groups, excluded = collect(cy, logs, Path(sys.argv[4]), Path(sys.argv[5]))
    res = analyse(groups)
    res["excluded_episodes"] = excluded
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "price_by_acceptance.json").write_text(json.dumps(res, indent=2), encoding="utf-8")
    text = report(res, excluded)
    (out_dir / "PRICE_BY_ACCEPTANCE.md").write_text(text, encoding="utf-8")
    print(text)


if __name__ == "__main__":
    main()
