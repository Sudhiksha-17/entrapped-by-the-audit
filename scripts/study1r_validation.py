"""Study 1R judge validation workflow (prereg_study1r/STUDY1R_SPEC.md section 9 as amended by human message 59: two
labelers, Labeler A (the entrant) and Labeler B (anonymous at their request), adjudicated gold; gate G3).

  agree     <A_sheet_dir> <A_key_dir> <A_labels.csv> <B_key_dir> <B_labels.csv>
            Inter-rater Cohen's kappa (response, awareness) with bootstrap 95% CIs (over items; D-071) and raw agreement,
            items matched through the two keys. Writes <A_sheet_dir>/adjudication.csv (Labeler A item ids): both
            labelers' labels and notes, the final label filled where they agree (reason "Labelers agreed."), blank final
            label and reason where they disagree; and <A_sheet_dir>/DISAGREEMENTS.md (item text, sting message, both
            labels and notes). Adjudication rule: the labelers resolve each item by discussion; if they cannot agree,
            Labeler A decides with the guide's conservative rule and the reason notes the unresolved disagreement
            (column `unresolved` = yes). Before any judge or detector output on these items is seen.
  judge     <key_dir> <pilot_stage_runs_dir> <candidate> [--approve-cost] [--estimate-only]
            Runs one judge v2 candidate (configs/judge_v2.yaml) on the held-out items, public view.
  evaluate  <key_dir> <adjudication.csv> <pilot_stage_runs_dir> <candidate>=<judge_run_dir> [...]
            G3 (sting.study1r_gates.g3) against the adjudicated gold labels; selects the cheapest passing candidate,
            else the human-coding backup. Also reports the rule-based detector against gold engagement on Offer items, as
            a cross-check only. Refuses unless every item has a final label and a one-line reason. Writes
            g3_report.json next to the adjudication file.
"""
from __future__ import annotations

import csv
import json
import sys
from pathlib import Path

import yaml

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from sting.judge_v2 import ENGAGED_RESPONSES, items_v2, run_judge_v2  # noqa: E402
from sting.paths import REPO_ROOT  # noqa: E402
from sting.stage2_measures import cohens_kappa  # noqa: E402
from sting.study1r_gates import detector, g3  # noqa: E402

LABELS = ("response", "awareness")


def read_labels(path: Path) -> dict[str, dict[str, str]]:
    with path.open(newline="", encoding="utf-8") as f:
        return {r["item_id"]: r for r in csv.DictReader(f)}


def read_key(key_dir: Path) -> dict[str, dict]:
    return json.loads((key_dir / "labeling_key.json").read_text(encoding="utf-8"))


def ident(k: dict) -> tuple:
    return k["replicate_id"], k["seller"], k["round"]


def agree(sheet_a: Path, key_a: Path, labels_a: Path, key_b: Path, labels_b: Path) -> dict:
    from sting.stage2_analysis import kappa_with_ci
    ka, kb = read_key(key_a), read_key(key_b)
    a, b = read_labels(labels_a), read_labels(labels_b)
    to_b = {ident(v): i for i, v in kb.items()}
    pairs = {i: to_b.get(ident(v)) for i, v in ka.items()}
    if None in pairs.values() or len(ka) != len(kb):
        raise SystemExit("the two labelers' sheets do not cover the same items")
    if any(not a.get(i, {}).get(l) or not b.get(j, {}).get(l) for i, j in pairs.items() for l in LABELS):
        raise SystemExit("both labelers must have labeled every item")
    ids = sorted(pairs)
    out: dict = {"n": len(ids)}
    for lab in LABELS:
        x, y = [a[i][lab] for i in ids], [b[pairs[i]][lab] for i in ids]
        out[lab] = {**kappa_with_ci(x, y), "raw_agreement": sum(p == q for p, q in zip(x, y)) / len(ids)}
    rows, disagree = [], []
    for i in ids:
        j = pairs[i]
        row = {"item_id": i, "response_A": a[i]["response"], "response_B": b[j]["response"],
               "awareness_A": a[i]["awareness"], "awareness_B": b[j]["awareness"],
               "note_A": a[i].get("note", ""), "note_B": b[j].get("note", "")}
        same = all(a[i][l] == b[j][l] for l in LABELS)
        row.update(response=a[i]["response"] if same else "", awareness=a[i]["awareness"] if same else "",
                   reason="Labelers agreed." if same else "", unresolved="" if not same else "no")
        if not same:
            disagree.append(i)
        rows.append(row)
    path = sheet_a / "adjudication.csv"
    if path.exists():
        raise SystemExit(f"{path} exists; refusing to overwrite adjudication work")
    with path.open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0]))
        w.writeheader()
        w.writerows(rows)
    out["disagreements"] = disagree
    return out


def disagreement_report(sheet_a: Path, adjudication: Path) -> str:
    """Markdown listing of every disagreement: item text, sting message, both labels and notes."""
    from sting.label_tool import parse_sheet
    items = {it["item_id"]: it for it in parse_sheet((sheet_a / "LABELING_SHEET.md").read_text(encoding="utf-8"))}
    L = ["# Validation set: disagreements between Labeler A and Labeler B", "",
         "Before any judge or detector output on these items. Labeler A item ids.", ""]
    for i, r in read_labels(adjudication).items():
        if r["response_A"] == r["response_B"] and r["awareness_A"] == r["awareness_B"]:
            continue
        it = items[i]
        L += [f"## {i}", "", f"**Sting message:** {it['message']}", "",
              f"**Seller's public message:** {it['fields'].get('message_to_sellers', '')}", "",
              f"- Labeler A: response {r['response_A']}, awareness {r['awareness_A']}; note: {r['note_A'] or 'none'}",
              f"- Labeler B: response {r['response_B']}, awareness {r['awareness_B']}; note: {r['note_B'] or 'none'}", ""]
    return "\n".join(L) + "\n"


def held_out_items(key_dir: Path, runs_root: Path) -> list[dict]:
    key = read_key(key_dir)
    by_run: dict[Path, set] = {}
    for k in key.values():
        hits = list(runs_root.glob(f"*/{k['replicate_id']}"))
        if len(hits) != 1:
            raise SystemExit(f"{k['replicate_id']}: {len(hits)} directories under {runs_root}")
        by_run.setdefault(hits[0].parent, set()).add(ident(k))
    items = []
    for run_dir, wanted in by_run.items():
        items += [i for i in items_v2(run_dir, "public") if (i["replicate_id"], i["seller"], i["round"]) in wanted]
    if len(items) != len(key):
        raise SystemExit(f"rebuilt {len(items)} of {len(key)} items")
    return items


def candidate_cfg(name: str) -> dict:
    jc = yaml.safe_load((REPO_ROOT / "configs" / "judge_v2.yaml").read_text(encoding="utf-8"))
    cand = next(c for c in jc["candidates"] if c["name"] == name)
    return {**{k: v for k, v in jc.items() if k not in ("candidates", "selected")}, "model": cand["model"],
            "price_in_per_m": cand["price_in_per_m"], "price_out_per_m": cand["price_out_per_m"]}


def gold_labels(key_dir: Path, adjudication: Path) -> dict[tuple, dict]:
    key = read_key(key_dir)
    rows = read_labels(adjudication)
    for i, r in rows.items():
        if not r["response"] or not r["awareness"]:
            raise SystemExit(f"adjudication incomplete: {i} has no final label")
        if not r.get("reason", "").strip():
            raise SystemExit(f"adjudication incomplete: {i} has no one-line reason")
        if r.get("unresolved", "").strip() not in ("yes", "no"):
            raise SystemExit(f"adjudication incomplete: {i} must say unresolved yes or no")
    return {ident(key[i]): {"response": r["response"], "awareness": r["awareness"], "condition": key[i]["condition"]}
            for i, r in rows.items()}


def detector_crosscheck(gold: dict[tuple, dict], items: list[dict]) -> dict:
    """Rule-based engagement vs gold engagement (gold response accept/reject/counter/noncommittal) on Offer items.
    Sham items are excluded: their gold response is always not_applicable, which does not encode engagement."""
    rows = []
    for it in items:
        g = gold[(it["replicate_id"], it["seller"], it["round"])]
        if g["condition"] != "offer":
            continue
        d = detector(it["fields"].get("message_to_sellers", ""), it["x"])
        rows.append((g["response"] in ENGAGED_RESPONSES, d["engaged"]))
    both = sum(a and b for a, b in rows)
    return {"n_offer_items": len(rows), "gold_engaged": sum(a for a, _ in rows), "detector_engaged": sum(b for _, b in rows),
            "both": both, "gold_only": sum(a and not b for a, b in rows), "detector_only": sum(b and not a for a, b in rows),
            "kappa": cohens_kappa([str(a) for a, _ in rows], [str(b) for _, b in rows]) if rows else None}


def evaluate(key_dir: Path, adjudication: Path, runs_root: Path, runs: dict[str, Path]) -> dict:
    gold = gold_labels(key_dir, adjudication)
    cands, cost = {}, {}
    for name, run_dir in runs.items():
        labels = [json.loads(l) for l in (run_dir / "labels.jsonl").read_text(encoding="utf-8").splitlines()]
        cands[name] = {str((l["replicate_id"], l["seller"], l["round"])): (l.get("response") if l["status"] == "ok" else None)
                       for l in labels}
        cost[name] = sum((json.loads(l).get("cost_usd_reported") or 0.0)
                         for l in (run_dir / "calls.jsonl").read_text(encoding="utf-8").splitlines())
    res = g3({str(k): v["response"] for k, v in gold.items()}, cands, cost)
    res["detector_crosscheck"] = detector_crosscheck(gold, held_out_items(key_dir, runs_root))
    (adjudication.parent / "g3_report.json").write_text(json.dumps(res, indent=2), encoding="utf-8")
    return res


def main() -> None:
    cmd = sys.argv[1]
    if cmd == "agree":
        args = [Path(p) for p in sys.argv[2:7]]
        out = agree(*args)
        (args[0] / "DISAGREEMENTS.md").write_text(disagreement_report(args[0], args[0] / "adjudication.csv"),
                                                  encoding="utf-8")
        (args[0] / "agreement.json").write_text(json.dumps(out, indent=2), encoding="utf-8")
        print(json.dumps(out, indent=2))
    elif cmd == "judge":
        key_dir, runs_root, name = Path(sys.argv[2]), Path(sys.argv[3]), sys.argv[4]
        items = held_out_items(key_dir, runs_root)
        print(json.dumps(run_judge_v2(None, "public", candidate_cfg(name), f"Study 1R G3 validation, judge {name}",
                                      approve_cost="--approve-cost" in sys.argv, estimate_only="--estimate-only" in sys.argv,
                                      items=items, items_label=f"study1r_validation_{name}",
                                      items_stage="study1r_pilot"), indent=2, default=str))
    elif cmd == "evaluate":
        runs = dict(a.split("=", 1) for a in sys.argv[5:])
        print(json.dumps(evaluate(Path(sys.argv[2]), Path(sys.argv[3]), Path(sys.argv[4]),
                                  {k: Path(v) for k, v in runs.items()}), indent=2))
    else:
        raise SystemExit("command must be agree, judge or evaluate")


if __name__ == "__main__":
    main()
