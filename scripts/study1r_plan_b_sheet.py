"""Exploratory plan B (notes/EXPLORATORY_PLAN_B_C.md, committed 1e32de1): select accepting sellers and matched controls,
and write the blind coding sheets. EXPLORATORY, post hoc. No API calls; no frozen file changed.

Selection follows the plan exactly: accepting sellers = LLM sellers with a human-confirmed acceptance (Labeler A,
verification set, accept or conditional_accept) in 4.1-low or 4.1-high Offer episodes; r = that seller's earliest such
round; window = rounds r to min(r+2, 30). Controls: sellers of same-cell Offer episodes without confirmed acceptance,
whose public message names "Seller C" in some round 11-30; for each accepting seller (in order of r, then replicate id)
the unused eligible seller whose mention round nearest to r is closest to r, ties by a seeded shuffle; fallback to
the same pool without the mention requirement (counted). Same window rounds as the matched accepting seller.

Sheet (one item per seller window, shuffled): for each window round, in order, a field "window_round_k" with the five
private fields (text only) and, under "Sting message", the Seller C message visible to the seller in that round (the
message Seller C posted the round before). Round numbers, cell, episode, seller, group and acceptance are only in the
key (separate directory). Labeler B sheet: random 50% (rounded up) of the items, own order, own ids, own key.

Usage: python scripts/study1r_plan_b_sheet.py <campaign.yaml> <campaign.json>[,...] <verify_sheet> <verify_key>
"""
from __future__ import annotations

import hashlib
import importlib.util
import json
import math
import random
import re
import sys
import tempfile
from pathlib import Path

SCRIPTS = Path(__file__).resolve().parent
REPO = SCRIPTS.parent
sys.path.insert(0, str(REPO))
from sting.judge import seller_responses  # noqa: E402
from sting.judge_v2 import PRIVATE_FIELDS  # noqa: E402
from sting.study1r_measures import ACCEPT_INCLUSIVE  # noqa: E402

CELLS = ("4.1-low", "4.1-high")
SELLER_C = re.compile(r"\bseller\s*c\b", re.I)
SHEET_DIR = REPO / "results" / "study1r" / "labeling"
KEY_DIR = REPO / "results" / "study1r" / "labeling_keys"
MAX_FIELDS = 3


def load(name: str, mod: str):
    spec = importlib.util.spec_from_file_location(mod, SCRIPTS / name)
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


def first_rounds(rep: str, human: dict, strata: dict) -> dict[str, int]:
    out: dict[str, int] = {}
    for (rid, s, r), lab in human.items():
        if rid == rep and strata.get((rid, s, r)) == "verification" and lab["response"] in ACCEPT_INCLUSIVE:
            out[s] = min(out.get(s, 99), r)
    return out


def select(episodes: list[dict], human: dict, strata: dict, mention: dict) -> tuple[list[dict], dict]:
    """episodes: completed Offer episodes of the two cells (replicate_id, cell, acc_inclusive, llm)."""
    accepters = []
    for e in episodes:
        for s, r in first_rounds(e["replicate_id"], human, strata).items():
            accepters.append({"group": "accepting", "cell": e["cell"], "replicate_id": e["replicate_id"], "seller": s,
                              "first_confirmed_round": r, "rounds": list(range(r, min(r + 2, 30) + 1))})
    accepters.sort(key=lambda a: (a["first_confirmed_round"], a["replicate_id"], a["seller"]))
    pool = {c: [(e["replicate_id"], s) for e in episodes if e["cell"] == c and not e["acc_inclusive"] for s in e["llm"]]
            for c in CELLS}
    rng = random.Random("study1r-plan-B-controls")
    for c in CELLS:
        rng.shuffle(pool[c])                                     # seeded tie order
    used, controls, fallback = set(), [], 0
    for a in accepters:
        r = a["first_confirmed_round"]
        cand = [u for u in pool[a["cell"]] if u not in used and mention.get(u)]
        fb = not cand
        if fb:
            cand = [u for u in pool[a["cell"]] if u not in used]
            fallback += 1
        if not cand:
            raise SystemExit(f"no control left in {a['cell']}")
        dist = (lambda u: 0) if fb else (lambda u: min(abs(m - r) for m in mention[u]))
        best = min(cand, key=lambda u: (dist(u), pool[a["cell"]].index(u)))
        used.add(best)
        controls.append({"group": "control", "cell": a["cell"], "replicate_id": best[0], "seller": best[1],
                         "matched_to": f"{a['replicate_id']}|{a['seller']}", "rounds": a["rounds"],
                         "mention_rounds": sorted(mention.get(best, [])), "fallback": fb,
                         "round_distance": None if fb else dist(best)})
    summary = {"accepting_sellers": len(accepters), "controls": len(controls), "fallback_controls": fallback,
               "per_cell": {c: {"accepting": sum(a["cell"] == c for a in accepters),
                                "control_pool_sellers": len(pool[c]),
                                "control_pool_with_mention": sum(bool(mention.get(u)) for u in pool[c])} for c in CELLS}}
    return accepters + controls, summary


def item_text(unit: dict, resp: dict, sting_sent: dict) -> tuple[dict[str, str], str]:
    fields, msgs = {}, []
    for k, r in enumerate(unit["rounds"], 1):
        rec = resp.get(r) or {}
        fields[f"window_round_{k}"] = "\n".join(f"- {f}: {' '.join(str(rec.get(f) or '').split())}" for f in PRIVATE_FIELDS)
        msgs.append(f"Window round {k}: {sting_sent.get(r - 1, '(no message)')}")
    return fields, "\n".join(msgs)


def write_sheet(items: list[dict], name: str, seed: str) -> list[str]:
    sheet_dir, key_dir = SHEET_DIR / name, KEY_DIR / name
    sheet_dir.mkdir(parents=True, exist_ok=False)
    key_dir.mkdir(parents=True, exist_ok=False)
    order = items[:]
    random.Random(seed).shuffle(order)
    lines = [f"# Plan B coding sheet ({name}; exploratory, post hoc; notes/EXPLORATORY_PLAN_B_C.md)", "",
             "Blind: cell, episode, seller, round numbers, group and acceptance are hidden. Each item is one seller's "
             "private notes over 1 to 3 consecutive rounds; under 'Sting message', Seller C's message visible to the "
             "seller in each of those rounds.", ""]
    key, ids = {}, []
    for n, it in enumerate(order, 1):
        iid = "P" + hashlib.sha256(f"{seed}:{n}:{it['replicate_id']}:{it['seller']}".encode()).hexdigest()[:8]
        ids.append(iid)
        lines += ["---", "", f"## {iid}", "", "**Sting message:**", ""]
        lines += [f"> {l}" for l in it["sting_text"].split("\n")] + [""]
        for f in sorted(it["fields"]):
            lines += [f"**{f}:**", "", it["fields"][f], ""]
        key[iid] = {k: it[k] for k in ("group", "cell", "replicate_id", "seller", "rounds")
                    if k in it} | {k: it[k] for k in ("first_confirmed_round", "matched_to", "fallback",
                                                      "round_distance", "mention_rounds") if k in it}
    (sheet_dir / "LABELING_SHEET.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
    (sheet_dir / "labels_template.csv").write_text("item_id,response,awareness,note\n" + "".join(f"{i},,,\n" for i in ids),
                                                   encoding="utf-8")
    (key_dir / "labeling_key.json").write_text(json.dumps(key, indent=2), encoding="utf-8")
    return ids


def main() -> None:
    cy, logs = Path(sys.argv[1]), [Path(p) for p in sys.argv[2].split(",") if p]
    wrap = load("study1r_results_completed.py", "wrap_pb")
    res = load("study1r_results.py", "res_pb")
    human, strata, protected = res.verify_labels(Path(sys.argv[3]), Path(sys.argv[4]))
    with tempfile.TemporaryDirectory(prefix="s1r_pb_") as tmp:
        staged, excluded = wrap.stage(logs, Path(tmp))
        built = res.build([cy], staged, human, strata, {}, {}, False, protected)
        dirs = {p.name: p for log in staged for info in json.loads(log.read_text(encoding="utf-8"))["arms"].values()
                for p in Path(info["run_dir"]).iterdir() if p.is_dir()}
        eps, resp, sent, mention = [], {}, {}, {}
        for e in built:
            if e["arm"] != "offer" or e["cell"] not in CELLS:
                continue
            rep = dirs[e["replicate_id"]]
            sl = json.loads((rep / "sting_log.json").read_text(encoding="utf-8"))
            llm = sl["llm_seller_ids"]
            eps.append({"replicate_id": e["replicate_id"], "cell": e["cell"], "acc_inclusive": bool(e["acc_inclusive"]),
                        "llm": llm})
            sent[e["replicate_id"]] = {m["round"]: m["text"] for m in sl["messages_sent"]}
            for s in llm:
                r_ = seller_responses(rep / "upstream_logs" / f"{s}.md")
                resp[(e["replicate_id"], s)] = r_
                mention[(e["replicate_id"], s)] = [r for r in range(11, 31)
                                                   if SELLER_C.search(str((r_.get(r) or {}).get("message_to_sellers") or ""))]
    units, summary = select(eps, human, strata, mention)
    for u in units:
        u["fields"], u["sting_text"] = item_text(u, resp[(u["replicate_id"], u["seller"])], sent[u["replicate_id"]])
    ids = write_sheet(units, "plan_b", "study1r-plan-B-sheet")
    sub = random.Random("study1r-plan-B-labeler-b").sample(units, math.ceil(0.5 * len(units)))
    write_sheet(sub, "plan_b_labeler_b", "study1r-plan-B-labeler-b-order")
    summary.update(items=len(ids), labeler_b_items=len(sub), excluded_episodes=[x["replicate_id"] for x in excluded],
                   window_lengths={n: sum(len(u["rounds"]) == n for u in units) for n in (1, 2, 3)})
    (KEY_DIR / "plan_b" / "selection_summary.json").write_text(json.dumps(summary, indent=2), encoding="utf-8")
    print(json.dumps(summary, indent=2))


if __name__ == "__main__":
    main()
