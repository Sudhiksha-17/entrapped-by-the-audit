"""Study 1R hand-labeling sets (prereg_study1r/STUDY1R_SPEC.md version 2, section 9, as revised by human messages 40
and 41). No API calls; prints counts only.

Pre-screen = the rule-based detector (sting.study1r_gates.detector: codebook rules 1, 2 and 4 with the restricted reply
rule). All items are public messages (message_to_sellers) from rounds 11-30, where Seller C's message is visible in
every round, shown with the sting message the seller saw that round.

`pilot` mode (from the pilot campaign logs; draw order as approved: validation first, then development):
- validation (held out): 30 Offer items, 10 per cell, each cell half (5) detector-flagged and half random from the
  cell's remaining items (if fewer than 5 flagged items exist, all of them plus random fill; reported); plus 10 Sham
  items at random. Seed "study1r-validation".
- validation_pass2: the same 40 items in a new random order with new item ids and its own key, for the single
  labeler's blind second pass (at least 3 hours after the first; human messages 40 and 42).
- development: 30 Offer items, 10 per cell, from items not in the validation set, drawn the same way (half flagged,
  half random). Seed "study1r-dev".
`verify` mode (confirmatory campaign logs; option A, human message 64, superseding the D-105 stopping-rule procedure;
the T2a verbal measure since no judge passed G3):
- scope: Offer arms of 4.1-low and 4.1-high, public messages, rounds 11-30; mini-low gets no verbal coding;
- screener: judge v2 prompt r1 with gpt-4.1 (`scripts/study1r_judge_v2_offer.py`), screener only;
- strata: verification = screener accept or conditional_accept (and any message without a valid screener label);
  audit_flagged = a random 10% (rounded up) of screener-negative, detector-flagged messages; audit_unflagged = a random
  50 screener-negative, detector-unflagged messages;
- `verify`: verification plus both audit strata in one shuffled sheet, so the coder is blind to arm, cell, stratum and
  the screener's label; every item is coded (no stopping rule);
- `verify_B`: a random 20% (rounded to the nearest item) of the verification set, own order and ids, for Labeler B.
Keys hold arm, cell, stratum, the screener's label and whether the item is in Labeler B's sample. Seeds
"study1r-verify-*".
- hidden within-episode stopping rule (human message 65): `<keys>/verify/stop_groups.json` maps each verification item
  of the `verify` sheet to an opaque group (a hash of its episode) and `removable` (false for items in Labeler B's
  sample, which Labeler A always codes); the label tool reads it with --stop-map and silently drops a group's
  remaining removable items once one of its verification items is coded accept or conditional_accept. Audit items are
  not in the map.
Sheets are shuffled with arm and cell hidden (blind_labeling_sheet); keys go to a separate directory.

Usage:
  python scripts/study1r_label_sets.py pilot <sheets_dir> <keys_dir> <pilot campaign.yaml> <campaign.json> [...]
  python scripts/study1r_label_sets.py verify <sheets_dir> <keys_dir> <screener_dir[,...]> <campaign.yaml> <campaign.json> [...]
"""
from __future__ import annotations

import hashlib
import json
import math
import random
import sys
from collections import Counter
from pathlib import Path

import yaml

sys.path.insert(0, str(Path(__file__).resolve().parent))
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from stage2_labeling_sheet import write_sheet  # noqa: E402

from sting.judge_v2 import items_v2  # noqa: E402
from sting.study1r_measures import ACCEPT_INCLUSIVE  # noqa: E402
from sting.study1r_gates import detector  # noqa: E402
from sting.stage2_measures import blind_labeling_sheet  # noqa: E402

KEEP = ("replicate_id", "seller", "round", "condition", "cell", "arm", "sting_message", "fields")


def pool(campaign_yaml: Path, logs: list[Path]) -> list[dict]:
    arms = {a["name"]: a for a in yaml.safe_load(campaign_yaml.read_text(encoding="utf-8"))["arms"]}
    items = []
    for log_path in logs:
        for name, info in json.loads(log_path.read_text(encoding="utf-8"))["arms"].items():
            if arms[name]["arm"] == "silent":
                continue
            for it in items_v2(Path(info["run_dir"]), "public"):
                items.append({**it, "cell": arms[name]["cell"], "arm": name})
    return sorted(items, key=lambda i: (i["arm"], i["replicate_id"], i["seller"], i["round"]))


def ident(i: dict) -> tuple:
    return i["replicate_id"], i["seller"], i["round"]


def strip(items: list[dict]) -> list[dict]:
    return [{k: i[k] for k in KEEP} for i in items]


def flagged(item: dict) -> bool:
    return detector(item["fields"].get("message_to_sellers", ""), item["x"])["engaged"]


def draw_half(pool: list[dict], n: int, rng: random.Random) -> tuple[list[dict], dict]:
    """n items: half detector-flagged (as many as exist, up to n/2), the rest random from the remaining pool."""
    pre = [i for i in pool if flagged(i)]
    pick = rng.sample(pre, min(n // 2, len(pre)))
    taken = {ident(p) for p in pick}
    rest = [i for i in pool if ident(i) not in taken]
    pick += rng.sample(rest, min(n - len(pick), len(rest)))
    return pick, {"pool": len(pool), "flagged_pool": len(pre), "flagged_drawn": min(n // 2, len(pre)), "drawn": len(pick)}


def pilot_sets(items: list[dict]) -> tuple[list[dict], list[dict], dict]:
    items = [i for i in items if 11 <= i["round"] <= 30]
    offer = [i for i in items if i["condition"] == "offer"]
    cells = sorted({i["cell"] for i in offer})
    rng = random.Random("study1r-validation")
    val, notes = [], {"validation": {}, "dev": {}}
    for c in cells:
        pick, note = draw_half([i for i in offer if i["cell"] == c], 10, rng)
        val += pick
        notes["validation"][c] = note
    sham = [i for i in items if i["condition"] == "sham"]
    val += rng.sample(sham, min(10, len(sham)))
    notes["validation"]["sham"] = {"pool": len(sham), "drawn": min(10, len(sham))}
    used = {ident(i) for i in val}
    rng = random.Random("study1r-dev")
    dev = []
    for c in cells:
        pick, note = draw_half([i for i in offer if i["cell"] == c and ident(i) not in used], 10, rng)
        dev += pick
        notes["dev"][c] = note
    return val, dev, notes


BACKUP_CELLS = ("4.1-low", "4.1-high")


def screener_positive(item: dict, screener: dict[tuple, dict]) -> bool:
    lab = screener.get(ident(item))
    return lab is None or lab.get("response") in ACCEPT_INCLUSIVE


def verify_sets(items: list[dict], screener: dict[tuple, dict]) -> dict:
    offer = [i for i in items if i["condition"] == "offer" and i["cell"] in BACKUP_CELLS and 11 <= i["round"] <= 30]
    verification = [i for i in offer if screener_positive(i, screener)]
    neg = [i for i in offer if not screener_positive(i, screener)]
    neg_flag = [i for i in neg if flagged(i)]
    neg_unflag = [i for i in neg if not flagged(i)]
    audit_flag = random.Random("study1r-verify-audit-flagged").sample(neg_flag, math.ceil(0.10 * len(neg_flag)))
    audit_unflag = random.Random("study1r-verify-audit-unflagged").sample(neg_unflag, min(50, len(neg_unflag)))
    b_set = random.Random("study1r-verify-B").sample(verification, round(0.20 * len(verification)))
    strata = {"verification": verification, "audit_flagged": audit_flag, "audit_unflagged": audit_unflag}
    return {"strata": strata, "labeler_b": b_set,
            "summary": {"cells": list(BACKUP_CELLS), "offer_episodes": len({i["replicate_id"] for i in offer}),
                        "offer_messages": len(offer), "screener_missing": sum(ident(i) not in screener for i in offer),
                        "verification": len(verification), "screener_negative_flagged": len(neg_flag),
                        "screener_negative_unflagged": len(neg_unflag), "audit_flagged": len(audit_flag),
                        "audit_unflagged": len(audit_unflag),
                        "labeler_a_items": len(verification) + len(audit_flag) + len(audit_unflag),
                        "labeler_b_items": len(b_set)}}


def write_keyed(name: str, groups: dict[str, list[dict]], screener: dict[tuple, dict], sheets: Path, keys: Path,
                seed: str, labeler_b: frozenset = frozenset()) -> dict:
    """One shuffled blind sheet from several strata; stratum, screener label and Labeler B membership go to the key
    only. Returns the key."""
    stratum = {ident(i): g for g, its in groups.items() for i in its}
    items = [i for its in groups.values() for i in its]
    sheet, key = blind_labeling_sheet(strip(items), seed=seed)
    for k in key.values():
        sr = (k["replicate_id"], k["seller"], k["round"])
        k["stratum"] = stratum[sr]
        k["screener_response"] = (screener.get(sr) or {}).get("response")
        k["labeler_b"] = sr in labeler_b
    write_sheet(sheet, key, sheets / name, keys / name)
    return key


def stop_groups(key: dict) -> dict:
    """Option A hidden stopping map: verification items only; opaque group per episode; removable unless in Labeler
    B's sample."""
    return {i: {"group": hashlib.sha256(k["replicate_id"].encode("utf-8")).hexdigest()[:12],
                "removable": not k["labeler_b"]}
            for i, k in key.items() if k["stratum"] == "verification"}


def write(name: str, items: list[dict], sheets: Path, keys: Path, seed: str) -> None:
    sheet, key = blind_labeling_sheet(strip(items), seed=seed)
    write_sheet(sheet, key, sheets / name, keys / name)


def main() -> None:
    mode, sheets, keys = sys.argv[1], Path(sys.argv[2]), Path(sys.argv[3])
    args = sys.argv[4:]
    screener = {}
    if mode == "verify":
        from study1r_results import load_labels
        screener, args = load_labels(args[0].split(",")), args[1:]
    campaign_yaml, logs = Path(args[0]), [Path(p) for p in args[1:]]
    items = pool(campaign_yaml, logs)
    if mode == "pilot":
        val, dev, notes = pilot_sets(items)
        write("validation", val, sheets, keys, "study1r-validation-order")
        write("validation_pass2", val, sheets, keys, "study1r-validation-pass2-order")
        write("dev", dev, sheets, keys, "study1r-dev-order")
        summary = {"validation": dict(Counter(f"{i['condition']}|{i['cell']}" for i in val)),
                   "dev": dict(Counter(f"{i['condition']}|{i['cell']}" for i in dev)), "draw_notes": notes,
                   "overlap": len({ident(i) for i in val} & {ident(i) for i in dev})}
    elif mode == "verify":
        bs = verify_sets(items, screener)
        key = write_keyed("verify", bs["strata"], screener, sheets, keys, "study1r-verify-order",
                          frozenset(ident(i) for i in bs["labeler_b"]))
        (keys / "verify" / "stop_groups.json").write_text(json.dumps(stop_groups(key), indent=1), encoding="utf-8")
        write_keyed("verify_B", {"verification": bs["labeler_b"]}, screener, sheets, keys, "study1r-verify-B-order")
        summary = bs["summary"]
    else:
        raise SystemExit("mode must be pilot or verify")
    (sheets / f"{mode}_sampling.json").write_text(json.dumps(summary, indent=2), encoding="utf-8")
    print(json.dumps(summary, indent=2))


if __name__ == "__main__":
    main()
