"""Study 1R option A: estimated human coding load from the pilot (human messages 64 and 65). No API calls.

Pilot inputs: the pilot screener runs (judge v2 r1, gpt-4.1, public view) and the pilot campaign logs. Per pilot
episode in the 4.1-low and 4.1-high Offer arms: verification messages (screener accept or conditional_accept, or no
valid label) and screener-negative detector-flagged messages (`study1r_label_sets.verify_sets`; counts only, no text).

Main study (66 episodes) by simulation, 10,000 runs, seed 20261025, two-level resampling (the pilot episodes are
resampled first, for the uncertainty of a 6-episode pilot, then 66 episodes from that resample);
Labeler B's sample = a random 20% (rounded) of verification messages, always coded by Labeler A; all of Labeler A's
items in random order; hidden within-episode stopping rule: a removable verification message is dropped once a
verification message of its episode has been confirmed. Each coded verification message is confirmed with
probability q, independently: q = 5/7 (gpt-4.1's precision for inclusive acceptance on the 40 validation items:
gold accept among judge accept, `results/study1r/g3/g3_report.json`), and q = 1.0 and 0.5 as bounds. Audit items:
ceil(10% of flagged negatives) + 50. q = 0 gives the load without the stopping rule (nothing is ever dropped).

Usage: python scripts/study1r_coding_load.py <screener_dir[,...]> <pilot campaign.yaml> <campaign.json> [...]
"""
from __future__ import annotations

import importlib.util
import json
import math
import sys
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parent))
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from study1r_results import load_labels  # noqa: E402

from sting.paths import REPO_ROOT  # noqa: E402

OUT = REPO_ROOT / "results" / "study1r" / "coding_load"
EPISODES, SIMS, SEED = 66, 10_000, 20261025
QS = {"q = 5/7 (validation precision)": 5 / 7, "q = 1.0": 1.0, "q = 0.5": 0.5, "no stopping rule": 0.0}


def pilot_counts(screener_dirs: list[str], campaign_yaml: Path, logs: list[Path]) -> list[dict]:
    spec = importlib.util.spec_from_file_location("sets", Path(__file__).resolve().parent / "study1r_label_sets.py")
    sets = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(sets)
    items = sets.pool(campaign_yaml, logs)
    vs = sets.verify_sets(items, load_labels(screener_dirs))
    eps = sorted({i["replicate_id"] for i in items if i["condition"] == "offer" and i["cell"] in sets.BACKUP_CELLS})
    ver = [i["replicate_id"] for i in vs["strata"]["verification"]]
    offer = [i for i in items if i["condition"] == "offer" and i["cell"] in sets.BACKUP_CELLS and 11 <= i["round"] <= 30]
    flag_neg = [i["replicate_id"] for i in offer if not sets.screener_positive(i, load_labels(screener_dirs)) and sets.flagged(i)]
    return [{"episode": e, "verification": ver.count(e), "flagged_negative": flag_neg.count(e)} for e in eps]


def simulate(pilot: list[dict], q: float, rng: np.random.Generator) -> np.ndarray:
    v = np.array([p["verification"] for p in pilot])
    f = np.array([p["flagged_negative"] for p in pilot])
    out = np.empty(SIMS)
    for s in range(SIMS):
        pick = rng.integers(0, len(pilot), len(pilot))[rng.integers(0, len(pilot), EPISODES)]
        groups = np.repeat(np.arange(EPISODES), v[pick])
        n = groups.size
        protected = np.zeros(n, dtype=bool)
        protected[rng.choice(n, round(0.20 * n), replace=False)] = True
        stopped = np.zeros(EPISODES, dtype=bool)
        coded = 0
        for i in rng.permutation(n):
            if stopped[groups[i]] and not protected[i]:
                continue
            coded += 1
            if rng.random() < q:
                stopped[groups[i]] = True
        out[s] = coded + math.ceil(0.10 * f[pick].sum()) + 50
    return out


def main() -> None:
    pilot = pilot_counts(sys.argv[1].split(","), Path(sys.argv[2]), [Path(p) for p in sys.argv[3:]])
    rng = np.random.default_rng(SEED)
    res = {}
    for name, q in QS.items():
        x = simulate(pilot, q, rng)
        res[name] = {"mean": float(x.mean()), "p2.5": float(np.quantile(x, 0.025)), "p97.5": float(np.quantile(x, 0.975))}
    v = np.array([p["verification"] for p in pilot])
    b = v[rng.integers(0, len(v), (SIMS, len(v)))]
    b = np.array([r[rng.integers(0, len(v), EPISODES)].sum() for r in b])
    labeler_b = {"mean": round(0.2 * v.mean() * EPISODES), "p2.5": round(0.2 * np.quantile(b, 0.025)),
                 "p97.5": round(0.2 * np.quantile(b, 0.975))}
    OUT.mkdir(parents=True, exist_ok=True)
    payload = {"pilot_episodes": pilot, "labeler_a": res,
               "labeler_b": labeler_b, "settings": {"episodes": EPISODES, "sims": SIMS, "seed": SEED}}
    (OUT / "coding_load.json").write_text(json.dumps(payload, indent=2), encoding="utf-8")
    print(json.dumps(payload, indent=2))


if __name__ == "__main__":
    main()
