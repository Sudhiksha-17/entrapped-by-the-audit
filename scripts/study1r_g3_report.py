"""Study 1R gate G3 report (prereg_study1r/STUDY1R_SPEC.md section 9; human message 62). No API calls.

Against the adjudicated gold labels (results/study1r/labeling/validation/adjudication.csv), per judge v2 candidate:
response kappa with bootstrap 95% CI (D-071), inclusive false-accept rate (gold non-accepts labeled accept or
conditional_accept), agreement on inclusive acceptance vs not (2 x 2, raw agreement, kappa), confusion matrix, and
every disagreement. Cross-check: the rule-based detector (rules 1, 2, 4) against gold engagement on Offer items.
Comparison: the frozen Study 1 judge (v1) on the same items. G3 rule: response kappa >= 0.6 and inclusive false
accept <= 10%; the cheapest passing candidate is selected, else the human-coding backup.

Usage: python scripts/study1r_g3_report.py <out_dir> <candidate>=<judge_v2_run_dir> [...] --v1 <judge_v1_run_dir>
"""
from __future__ import annotations

import json
import sys
from collections import Counter
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from study1r_validation import detector_crosscheck, gold_labels, held_out_items, read_key, read_labels  # noqa: E402

from sting.paths import REPO_ROOT  # noqa: E402
from sting.stage2_analysis import kappa_with_ci  # noqa: E402
from sting.study1r_gates import g3  # noqa: E402

KEY = REPO_ROOT / "results" / "study1r" / "labeling_keys" / "validation"
ADJ = REPO_ROOT / "results" / "study1r" / "labeling" / "validation" / "adjudication.csv"
RUNS = REPO_ROOT / "runs" / "study1r_pilot"
RESPONSES = ["accept", "conditional_accept", "reject", "counter", "noncommittal", "ignored", "not_applicable"]
INCLUSIVE = ("accept", "conditional_accept")


def labels_of(run_dir: Path) -> dict[tuple, dict]:
    out = {}
    for line in (run_dir / "labels.jsonl").read_text(encoding="utf-8").splitlines():
        r = json.loads(line)
        out[(r["replicate_id"], r["seller"], r["round"])] = r
    return out


def cost_of(run_dir: Path) -> float:
    return sum((json.loads(l).get("cost_usd_reported") or 0.0)
               for l in (run_dir / "calls.jsonl").read_text(encoding="utf-8").splitlines())


def evaluate_one(gold: dict, item_id: dict, items: dict, lab: dict, inclusive_judge: tuple = INCLUSIVE) -> dict:
    ok = [k for k in gold if lab.get(k, {}).get("status") == "ok"]
    h = [gold[k]["response"] for k in ok]
    j = [lab[k]["response"] for k in ok]
    ha = ["accept" if x in INCLUSIVE else "not" for x in h]
    ja = ["accept" if x in inclusive_judge else "not" for x in j]
    non = [k for k in ok if gold[k]["response"] not in INCLUSIVE]
    fa = sum(lab[k]["response"] in inclusive_judge for k in non)
    conf = Counter(zip(h, j))
    acc2 = Counter(zip(ha, ja))
    dis = [{"item": item_id[k], "gold": gold[k]["response"], "judge": lab[k]["response"],
            "engaged": lab[k].get("engaged_with_message"), "evidence": lab[k].get("evidence"),
            "notes": lab[k].get("notes", ""), "message": items[k]["fields"].get("message_to_sellers", "")}
           for k in sorted(ok, key=lambda k: item_id[k]) if gold[k]["response"] != lab[k]["response"]]
    return {"valid": len(ok), "invalid": len(gold) - len(ok), "kappa_response": kappa_with_ci(h, j),
            "false_accept_inclusive": {"k": fa, "n": len(non), "rate": fa / len(non) if non else None},
            "inclusive_acceptance_agreement": {
                "table": {f"gold {a} / judge {b}": acc2.get((a, b), 0) for a in ("accept", "not") for b in ("accept", "not")},
                "raw_agreement": sum(x == y for x, y in zip(ha, ja)) / len(ok), "kappa": kappa_with_ci(ha, ja)},
            "confusion": {a: {b: conf.get((a, b), 0) for b in RESPONSES} for a in RESPONSES}, "disagreements": dis}


def main() -> None:
    out_dir = Path(sys.argv[1])
    args = sys.argv[2:]
    v1_dir = Path(args[args.index("--v1") + 1]) if "--v1" in args else None
    cands = {a.split("=", 1)[0]: Path(a.split("=", 1)[1]) for a in args if "=" in a}
    gold = gold_labels(KEY, ADJ)
    key = read_key(KEY)
    item_id = {(k["replicate_id"], k["seller"], k["round"]): i for i, k in key.items()}
    items = {(i["replicate_id"], i["seller"], i["round"]): i for i in held_out_items(KEY, RUNS)}
    res = {"gold_counts": dict(Counter(g["response"] for g in gold.values())), "candidates": {}}
    for name, d in cands.items():
        res["candidates"][name] = {**evaluate_one(gold, item_id, items, labels_of(d)), "cost_usd": cost_of(d), "run_dir": str(d)}
    gate = g3({str(k): v["response"] for k, v in gold.items()},
              {n: {str(k): (l["response"] if l["status"] == "ok" else None) for k, l in labels_of(d).items()}
               for n, d in cands.items()}, {n: cost_of(d) for n, d in cands.items()})
    res["g3"] = gate
    res["detector_crosscheck"] = detector_crosscheck(gold, list(items.values()))
    if v1_dir:
        res["judge_v1"] = {**evaluate_one(gold, item_id, items, labels_of(v1_dir), inclusive_judge=("accept",)),
                           "cost_usd": cost_of(v1_dir), "run_dir": str(v1_dir),
                           "note": "v1 has no conditional_accept label; its 'accept' is compared with gold inclusive acceptance"}
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "g3_report.json").write_text(json.dumps(res, indent=2, default=str), encoding="utf-8")
    L = ["# Gate G3: judge v2 against the adjudicated gold (40 validation items)", "",
         f"Gold response counts: {res['gold_counts']}. Judge v2 prompt r1 (D-100). Facts only.", ""]
    for name, r in list(res["candidates"].items()) + ([("judge v1 (comparison)", res["judge_v1"])] if v1_dir else []):
        k, fa, ia = r["kappa_response"], r["false_accept_inclusive"], r["inclusive_acceptance_agreement"]
        L += [f"## {name}", "", f"- Valid {r['valid']} of 40; cost ${r['cost_usd']:.4f}.",
              f"- Response kappa {k['kappa']:.3f} (95% CI {k['ci_low']:.3f} to {k['ci_high']:.3f}).",
              f"- Inclusive false accept: {fa['k']}/{fa['n']}" + (f" = {fa['rate']:.3f}." if fa["rate"] is not None else "."),
              f"- Inclusive acceptance vs not: raw agreement {ia['raw_agreement']:.3f}, kappa {ia['kappa']['kappa']:.3f}; "
              f"{ia['table']}.", "", "| gold \\ judge | " + " | ".join(RESPONSES) + " |", "|---" * (len(RESPONSES) + 1) + "|"]
        for a in RESPONSES:
            if any(r["confusion"][a].values()):
                L.append(f"| {a} | " + " | ".join(str(r["confusion"][a][b]) for b in RESPONSES) + " |")
        L += ["", f"Disagreements ({len(r['disagreements'])}):", ""]
        for d in r["disagreements"]:
            L.append(f"- {d['item']}: gold {d['gold']}; judge {d['judge']} (engaged {d['engaged']}; evidence "
                     f"{json.dumps(d['evidence'], ensure_ascii=False)}). Message: \"{d['message'][:240]}\"")
        L.append("")
    dc = res["detector_crosscheck"]
    L += ["## Rule-based detector (cross-check; never sets gold)", "",
          f"Offer items {dc['n_offer_items']}: gold engaged {dc['gold_engaged']}, detector engaged {dc['detector_engaged']}, "
          f"both {dc['both']}, gold only {dc['gold_only']}, detector only {dc['detector_only']}, kappa "
          f"{dc['kappa'] if dc['kappa'] is None else round(dc['kappa'], 3)}.", "",
          "## G3 decision", ""]
    for n, c in gate["candidates"].items():
        L.append(f"- {n}: kappa {c['kappa']:.3f} (>= 0.6: {c['kappa'] >= 0.6}); false accept "
                 f"{c['false_accept_rate']:.3f} (<= 0.10: {c['false_accept_rate'] <= 0.10}); cost ${c['cost_usd']:.4f}; "
                 f"passes: {c['passed']}.")
    L += ["", f"**Selected (frozen judge): {gate['selected'] or 'none'}; verbal measure: {gate['verbal_measure']}.**"]
    (out_dir / "G3_REPORT.md").write_text("\n".join(L) + "\n", encoding="utf-8")
    print("\n".join(L))


if __name__ == "__main__":
    main()
