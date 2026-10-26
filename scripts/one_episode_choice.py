"""One-episode figure choice (human message 86, Part 1). No API calls; no Plan B file is read.

Accepting sellers = LLM sellers of 4.1-high Offer episodes (completed episodes, D-116 staging) with a human-confirmed
acceptance (Labeler A, verification message, accept or conditional_accept); r = that seller's first confirmed round
(first_rounds of scripts/study1r_plan_b_sheet.py, which reads only the verify coding). The median of r over these
sellers is computed (statistics.median; with an even count it is the mean of the two middle values). Candidates =
sellers whose r is closest to that median; one is chosen with random.Random(20261025).choice over the candidates
sorted by (replicate id, seller).

Usage: python scripts/one_episode_choice.py <campaign.yaml> <campaign.json>[,...] <verify_sheet> <verify_key>
"""
from __future__ import annotations

import importlib.util
import json
import random
import statistics
import sys
import tempfile
from pathlib import Path

SCRIPTS = Path(__file__).resolve().parent


def load(name: str, mod: str):
    spec = importlib.util.spec_from_file_location(mod, SCRIPTS / name)
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


def choose(sellers: list[tuple[str, str, int]], seed: int = 20261025) -> dict:
    rounds = [r for _, _, r in sellers]
    med = statistics.median(rounds)
    best = min(abs(r - med) for r in rounds)
    cand = sorted((rep, s, r) for rep, s, r in sellers if abs(r - med) == best)
    pick = random.Random(seed).choice(cand)
    return {"n_sellers": len(sellers), "rounds_sorted": sorted(rounds), "median": med,
            "candidates": [list(c) for c in cand], "chosen": {"replicate_id": pick[0], "seller": pick[1],
                                                              "first_confirmed_round": pick[2]}}


def main() -> None:
    cy, logs = Path(sys.argv[1]), [Path(p) for p in sys.argv[2].split(",") if p]
    wrap, res = load("study1r_results_completed.py", "w1e"), load("study1r_results.py", "r1e")
    pb = load("study1r_plan_b_sheet.py", "pb1e")
    human, strata, protected = res.verify_labels(Path(sys.argv[3]), Path(sys.argv[4]))
    with tempfile.TemporaryDirectory(prefix="s1r_1e_") as tmp:
        staged, _ = wrap.stage(logs, Path(tmp))
        eps = res.build([cy], staged, human, strata, {}, {}, False, protected)
    sellers = [(e["replicate_id"], s, r) for e in eps if e["cell"] == "4.1-high" and e["arm"] == "offer"
               for s, r in pb.first_rounds(e["replicate_id"], human, strata).items()]
    print(json.dumps(choose(sellers), indent=1))


if __name__ == "__main__":
    main()
