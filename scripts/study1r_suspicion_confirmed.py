"""Study 1R exploratory, post hoc (human messages 74/75; not preregistered; no frozen file changed). No API calls.

Confirmed probe Q1 category (c): a seller's Q1 answer with a keyword (c) hit (scripts/study1r_exploratory_suspicion.py)
that the human coded real_suspicion on the blind Q1 check sheet. Same episodes and denominators as the keyword rates
(main-study completed episodes; unit: LLM seller). Per arm: count and rate with Wilson 95% CI, plus the coded
breakdown of the keyword hits. Offer minus Silent per cell: seller-level rate difference, episode-cluster bootstrap
95% CI (the suspicion script's `cluster_diff`: 10,000 resamples, seed 20261025).

Usage: python scripts/study1r_suspicion_confirmed.py <out_dir> <labels.csv> <key.json> <campaign.yaml> <campaign.json> [...]
"""
from __future__ import annotations

import csv
import importlib.util
import json
import sys
from collections import defaultdict
from pathlib import Path

SCRIPTS = Path(__file__).resolve().parent


def load(name: str, mod: str):
    spec = importlib.util.spec_from_file_location(mod, SCRIPTS / name)
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


S = load("study1r_exploratory_suspicion.py", "susp_confirmed")


def coded(labels: Path, key: Path) -> dict:
    """(replicate_id, seller) -> response; stops unless the coding is complete and matches the key."""
    k = json.loads(key.read_text(encoding="utf-8"))
    rows = list(csv.DictReader(labels.open(encoding="utf-8")))
    ids = [r["item_id"] for r in rows]
    if len(ids) != len(set(ids)) or set(ids) != set(k):
        raise SystemExit("labels do not match the key")
    bad = [r["item_id"] for r in rows if r["response"] not in ("real_suspicion", "false_positive")]
    if bad:
        raise SystemExit(f"uncoded or invalid responses: {bad}")
    return {(k[r["item_id"]]["replicate_id"], k[r["item_id"]]["seller"]): r["response"] for r in rows}


def analyse(eps: list[dict], codes: dict) -> dict:
    by_arm = defaultdict(list)
    for e in eps:
        by_arm[f"{e['cell']}/{e['arm']}"].append(e)
    order = sorted(by_arm, key=lambda k: (k.split("/")[1] != "offer", k))
    hit = {(e["replicate_id"], s): S.q1_categories(e["q1"][s])["c"] for e in eps for s in e["llm"]}
    if {k for k, v in hit.items() if v} != set(codes):
        raise SystemExit("keyword (c) hits differ from the coded items")
    conf = {k: codes.get(k) == "real_suspicion" for k in hit}
    per_arm = {}
    for arm in order:
        keys = [(e["replicate_id"], s) for e in by_arm[arm] for s in e["llm"]]
        n_hit = sum(hit[k] for k in keys)
        n_real = sum(conf[k] for k in keys)
        per_arm[arm] = {"episodes": len(by_arm[arm]), "keyword_c": S.rate(n_hit, len(keys)),
                        "confirmed_c": S.rate(n_real, len(keys)),
                        "coded": {"real_suspicion": n_real, "false_positive": n_hit - n_real}}
    diffs = {}
    for cell in S.CELLS:
        off, sil = by_arm.get(f"{cell}/offer"), by_arm.get(f"{cell}/silent")
        if off and sil:
            diffs[cell] = S.cluster_diff([[conf[(e["replicate_id"], s)] for s in e["llm"]] for e in off],
                                         [[conf[(e["replicate_id"], s)] for s in e["llm"]] for e in sil])
    return {"label": "exploratory, post hoc", "per_arm": per_arm, "offer_minus_silent": diffs,
            "items_coded": len(codes), "real_suspicion": sum(v == "real_suspicion" for v in codes.values()),
            "false_positive": sum(v == "false_positive" for v in codes.values())}


def report(res: dict) -> str:
    f = lambda r: f"{r['k']}/{r['n']} = {r['rate']:.3f} ({r['ci'][0]:.3f}, {r['ci'][1]:.3f})"  # noqa: E731
    L = ["# Study 1R confirmed probe Q1 category (c) (exploratory, post hoc)", "",
         "Human messages 74/75. Not preregistered. Confirmed (c): a keyword (c) hit in a seller's probe Q1 answer that "
         "the human coded real_suspicion on the blind Q1 check sheet "
         "(`results/study1r/labeling/suspicion_check_q1/labels_template.csv`). Same episodes and denominators as the "
         "keyword rates in SUSPICION.md (unit: LLM seller). Script: `scripts/study1r_suspicion_confirmed.py`. Facts only.",
         "", f"Coded items: {res['items_coded']} ({res['real_suspicion']} real_suspicion, "
         f"{res['false_positive']} false_positive).", "",
         "## Per arm (Wilson 95% CI)", "",
         "| Arm | Episodes | Keyword (c) | Coded real / false positive | Confirmed (c) |", "|---|---|---|---|---|"]
    for arm, r in res["per_arm"].items():
        L.append(f"| {arm} | {r['episodes']} | {f(r['keyword_c'])} | {r['coded']['real_suspicion']} / "
                 f"{r['coded']['false_positive']} | {f(r['confirmed_c'])} |")
    L += ["", "## Offer minus Silent per cell (confirmed (c); seller-level rate difference; episode-cluster bootstrap "
          "95% CI, 10,000 resamples, seed 20261025)", "", "| Cell | Offer episodes | Silent episodes | Difference (95% CI) |",
          "|---|---|---|---|"]
    for cell, d in res["offer_minus_silent"].items():
        L.append(f"| {cell} | {d['episodes_a']} | {d['episodes_b']} | {d['estimate']:+.3f} "
                 f"({d['ci_low']:+.3f}, {d['ci_high']:+.3f}) |")
    return "\n".join(L) + "\n"


def main() -> None:
    out_dir, labels, key, cy = (Path(p) for p in sys.argv[1:5])
    eps = S.episodes(cy, [Path(p) for p in sys.argv[5:]])
    res = analyse(eps, coded(labels, key))
    res["episodes"] = len(eps)
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "confirmed.json").write_text(json.dumps(res, indent=2), encoding="utf-8")
    (out_dir / "CONFIRMED.md").write_text(report(res), encoding="utf-8")
    print(report(res))


if __name__ == "__main__":
    main()
