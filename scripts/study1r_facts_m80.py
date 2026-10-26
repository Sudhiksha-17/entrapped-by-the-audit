"""Study 1R facts for the paper (human message 80; exploratory, descriptive; no frozen file changed). No API calls.

1. pre, headroom (100 - pre) and X - pre on the Offer arms only, per cell (same basis for all three), mean with
   bootstrap 95% CI (10,000 resamples, seed 20261025).
3. For the random-round reference of NUMBERS_FOR_PAPER.md section 6.5 (scripts/study1r_posthoc_m78.py): the spread of
   single-episode after-minus-before values (one value per episode and pseudo round, rounds 17-29) in 4.1-high Offer
   without confirmed acceptance and 4.1-high Silent, and the same for the accepters, to show what the reference
   interval (a distribution of group means) is built from.

Usage: python scripts/study1r_facts_m80.py <out.json> <campaign.yaml> <campaign.json>[,...] <verify_sheet> <verify_key>
       <judge_v2_dir>[,...]
"""
from __future__ import annotations

import importlib.util
import json
import sys
from pathlib import Path

import numpy as np

SCRIPTS = Path(__file__).resolve().parent
sys.path.insert(0, str(SCRIPTS.parent))
from sting import study1r_analysis as A  # noqa: E402

SEED, R = 20261025, 10_000


def load(name: str, mod: str):
    spec = importlib.util.spec_from_file_location(mod, SCRIPTS / name)
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


def main() -> None:
    a = sys.argv[1:]
    m78 = load("study1r_posthoc_m78.py", "m78_m80")
    pba = load("study1r_price_by_acceptance.py", "pba_m80")
    episodes, extra, human, strata, excluded = m78.collect(Path(a[1]), [Path(p) for p in a[2].split(",") if p],
                                                           Path(a[3]), Path(a[4]), [p for p in a[5].split(",") if p])
    rng = np.random.default_rng(SEED)
    out = {"label": "exploratory, descriptive (human message 80)", "excluded_episodes": excluded,
           "1_offer_arms_only": {}}
    for c in ("mini-low", "4.1-low", "4.1-high"):
        o = A.eps(episodes, "offer", c)
        out["1_offer_arms_only"][c] = {k: m78.boot_mean(v, rng) for k, v in (
            ("pre", [e["pre"] for e in o]), ("headroom", [100 - e["pre"] for e in o]), ("x_minus_pre", [e["jump"] for e in o]),
            ("x_minus_pre_over_headroom", [e["jump"] / (100 - e["pre"]) for e in o]))}
    o = A.eps(episodes, "offer", "4.1-high")
    groups = {"offer_not_accepting": [e for e in o if not e["acc_inclusive"]], "silent": A.eps(episodes, "silent", "4.1-high")}
    spread = {}
    for g, es in groups.items():
        table = np.array([[m78.before_after(extra[e["replicate_id"]]["asks"], r) for r in range(17, 30)] for e in es], dtype=float)
        ep_means = table.mean(axis=1)
        spread[g] = {"episodes": len(es), "cells": int(table.size), "sd_single_values": float(table.std(ddof=1)),
                     "sd_episode_means_over_rounds": float(ep_means.std(ddof=1)),
                     "range_single_values": [float(table.min()), float(table.max())]}
    acc = []
    for e in o:
        if e["acc_inclusive"]:
            r0 = pba.first_acceptance(e["replicate_id"], human, strata)["first_confirmed_round"]
            v = m78.before_after(extra[e["replicate_id"]]["asks"], r0)
            if v is not None:
                acc.append(v)
    spread["accepters"] = {"episodes": len(acc), "sd_single_values": float(np.std(acc, ddof=1)),
                           "range_single_values": [float(min(acc)), float(max(acc))], "values": acc}
    out["3_single_episode_spread"] = spread
    Path(a[0]).parent.mkdir(parents=True, exist_ok=True)
    Path(a[0]).write_text(json.dumps(out, indent=2), encoding="utf-8")
    print(json.dumps(out, indent=1))


if __name__ == "__main__":
    main()
