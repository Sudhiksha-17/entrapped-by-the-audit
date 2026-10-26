"""Supplementary blind labeling sheet, round 11 only (deviation DEV-1 / D-088, human message 28).

30 seller-rounds, all from round 11 of completed confirmatory message-arm episodes: 6 from each Offer cell
(mini-low, 4.1-low, 4.1-medium, 4.1-high), 2 directive, 2 anchor, 1 sham, 1 rapport (mini-low). Random selection
with seed 20261025 over a pool sorted by (arm, replicate, seller), strata in the order of QUOTA; seller-rounds already
in the original sample are excluded. Shuffled with arm and cell hidden by blind_labeling_sheet (order seed
"20261025-order"); key written to a separate directory. Prints only counts per stratum, never item text. No API calls;
does not run the judge.

Usage: python scripts/stage2_labeling_supp.py <sheet_dir> <key_dir> <original_key.json> <campaign.yaml> <campaign.json> [...]
"""
from __future__ import annotations

import json
import random
import sys
from collections import Counter
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from stage2_labeling_sheet import pool, write_sheet  # noqa: E402

from sting.stage2_measures import blind_labeling_sheet  # noqa: E402

ROUND = 11
SEED = 20261025
ORDER_SEED = "20261025-order"
QUOTA = {("offer", "mini-low"): 6, ("offer", "4.1-low"): 6, ("offer", "4.1-medium"): 6, ("offer", "4.1-high"): 6,
         ("directive", "mini-low"): 2, ("anchor", "mini-low"): 2, ("sham", "mini-low"): 1, ("rapport", "mini-low"): 1}


def draw(items: list[dict], exclude: set[tuple], quota: dict = QUOTA, seed: int = SEED) -> list[dict]:
    rng = random.Random(seed)
    out = []
    for stratum, n in quota.items():
        cands = sorted((i for i in items if (i["condition"], i["cell"]) == stratum and i["round"] == ROUND
                        and (i["replicate_id"], i["seller"], i["round"]) not in exclude),
                       key=lambda i: (i["arm"], i["replicate_id"], i["seller"]))
        if len(cands) < n:
            raise SystemExit(f"{stratum}: {len(cands)} candidates < {n}")
        out += rng.sample(cands, n)
    return out


def main() -> None:
    sheet_dir, key_dir, original_key, campaign_yaml = (Path(p) for p in sys.argv[1:5])
    logs = [Path(p) for p in sys.argv[5:]]
    orig = json.loads(original_key.read_text(encoding="utf-8"))
    exclude = {(k["replicate_id"], k["seller"], k["round"]) for k in orig.values()}
    items = pool(campaign_yaml, logs)
    sample = draw(items, exclude)
    sheet, key = blind_labeling_sheet(sample, seed=ORDER_SEED)
    write_sheet(sheet, key, sheet_dir, key_dir)
    round11 = Counter((i["condition"], i["cell"]) for i in items if i["round"] == ROUND)
    meta = {"n_items": len(sheet), "round": ROUND, "seed": SEED, "order_seed": ORDER_SEED,
            "excluded_from_original_sample": sorted(f"{c}|{cell}" for (r, s, rnd) in exclude for (c, cell) in [
                next(((i["condition"], i["cell"]) for i in items if (i["replicate_id"], i["seller"], i["round"]) == (r, s, rnd)))
            ] if rnd == ROUND),
            "round11_pool_per_stratum": {f"{c}|{cell}": n for (c, cell), n in sorted(round11.items())},
            "sample_per_stratum": {f"{c}|{cell}": n for (c, cell), n in sorted(
                Counter((i["condition"], i["cell"]) for i in sample).items())},
            "sample_rounds": sorted({i["round"] for i in sample}),
            "campaign_logs": [str(p) for p in logs], "deviation": "DEV-1 / D-088 (notes/PREREG_DEVIATIONS.md)"}
    (sheet_dir / "sampling.json").write_text(json.dumps(meta, indent=2), encoding="utf-8")
    print(json.dumps({k: v for k, v in meta.items() if k != "campaign_logs"}, indent=2))


if __name__ == "__main__":
    main()
