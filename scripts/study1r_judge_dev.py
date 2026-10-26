"""Study 1R judge v2 development on the development set ONLY (prereg_study1r/STUDY1R_SPEC.md section 9; human message
45). Never reads the validation sheets, labels or keys.

  estimate                       cost estimate for both candidates on the 30 development items (no API calls)
  run <candidate> [--approve-cost]   run one candidate (configs/judge_v2.yaml) on the development items, public view
  report <out.md> <candidate>=<judge_run_dir> [...]
                                 per candidate: response kappa (full label), inclusive false-accept rate (gold non-
                                 accepts labeled accept or conditional_accept), confusion matrix (rows human, columns
                                 judge), and every disagreement with the human label and note and the judge's label and
                                 evidence. Writes <out.md> and <out.md>.json.
"""
from __future__ import annotations

import csv
import json
import sys
from collections import Counter
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from study1r_validation import candidate_cfg, held_out_items  # noqa: E402

from sting.judge_v2 import V2_ENUMS, estimate_v2, run_judge_v2  # noqa: E402
from sting.paths import REPO_ROOT  # noqa: E402
from sting.stage2_measures import cohens_kappa  # noqa: E402

DEV_SHEET = REPO_ROOT / "results" / "study1r" / "labeling" / "dev"
DEV_KEY = REPO_ROOT / "results" / "study1r" / "labeling_keys" / "dev"
PILOT_RUNS = REPO_ROOT / "runs" / "study1r_pilot"
CANDIDATES = ("gpt-4.1-mini", "gpt-4.1")
RESPONSES = ["accept", "conditional_accept", "reject", "counter", "noncommittal", "ignored", "not_applicable"]
INCLUSIVE = ("accept", "conditional_accept")


def dev_items() -> list[dict]:
    assert DEV_KEY.name == "dev" and DEV_SHEET.name == "dev"
    return held_out_items(DEV_KEY, PILOT_RUNS)


def gold() -> dict[tuple, dict]:
    key = json.loads((DEV_KEY / "labeling_key.json").read_text(encoding="utf-8"))
    with (DEV_SHEET / "labels_template.csv").open(newline="", encoding="utf-8") as f:
        rows = {r["item_id"]: r for r in csv.DictReader(f)}
    return {(key[i]["replicate_id"], key[i]["seller"], key[i]["round"]): {"item": i, **rows[i]} for i in key}


def evaluate(run_dir: Path, g: dict[tuple, dict], items: dict[tuple, dict]) -> dict:
    labels = {(l["replicate_id"], l["seller"], l["round"]): l
              for l in map(json.loads, (run_dir / "labels.jsonl").read_text(encoding="utf-8").splitlines())}
    ok = [k for k in g if labels.get(k, {}).get("status") == "ok"]
    h = [g[k]["response"] for k in ok]
    j = [labels[k]["response"] for k in ok]
    non_acc = [k for k in ok if g[k]["response"] not in INCLUSIVE]
    fa = sum(labels[k]["response"] in INCLUSIVE for k in non_acc)
    conf = Counter(zip(h, j))
    dis = []
    for k in sorted(ok, key=lambda k: g[k]["item"]):
        if g[k]["response"] != labels[k]["response"]:
            dis.append({"item": g[k]["item"], "human": g[k]["response"], "human_note": g[k].get("note", ""),
                        "judge": labels[k]["response"], "judge_engaged": labels[k]["engaged_with_message"],
                        "judge_evidence": labels[k]["evidence"], "judge_notes": labels[k].get("notes", ""),
                        "message": items[k]["fields"]["message_to_sellers"]})
    cost = sum((json.loads(l).get("cost_usd_reported") or 0.0)
               for l in (run_dir / "calls.jsonl").read_text(encoding="utf-8").splitlines())
    return {"run_dir": str(run_dir), "n": len(g), "valid": len(ok),
            "invalid": [g[k]["item"] for k in g if k not in ok],
            "kappa_response": cohens_kappa(h, j) if ok else None,
            "false_accept_inclusive": {"k": fa, "n": len(non_acc), "rate": fa / len(non_acc) if non_acc else None},
            "confusion": {a: {b: conf.get((a, b), 0) for b in RESPONSES} for a in RESPONSES},
            "human_counts": dict(Counter(h)), "judge_counts": dict(Counter(j)), "disagreements": dis, "cost_usd": cost}


def main() -> None:
    cmd = sys.argv[1]
    if cmd == "estimate":
        items = dev_items()
        for c in CANDIDATES:
            print(c, f"${estimate_v2(items, candidate_cfg(c)):.4f}", f"({len(items)} items)")
    elif cmd == "run":
        c = sys.argv[2]
        assert c in CANDIDATES
        print(json.dumps(run_judge_v2(None, "public", candidate_cfg(c), f"Study 1R judge v2 development, {c} (message 45)",
                                      approve_cost="--approve-cost" in sys.argv, items=dev_items(),
                                      items_label=f"study1r_dev_{c}", items_stage="study1r_pilot"), indent=2, default=str))
    elif cmd == "report":
        out = Path(sys.argv[2])
        g = gold()
        items = {(i["replicate_id"], i["seller"], i["round"]): i for i in dev_items()}
        res = {name: evaluate(Path(d), g, items) for name, d in (a.split("=", 1) for a in sys.argv[3:])}
        Path(str(out) + ".json").write_text(json.dumps(res, indent=2), encoding="utf-8")
        L = [f"# Judge v2 development report ({', '.join(res)})", "", "Development set only (30 items). Facts only.", ""]
        for name, r in res.items():
            fa = r["false_accept_inclusive"]
            L += [f"## {name}", "", f"Valid {r['valid']} of {r['n']} (invalid: {r['invalid'] or 'none'}); response kappa "
                  f"{r['kappa_response']:.3f}; inclusive false-accept {fa['k']}/{fa['n']}"
                  + (f" = {fa['rate']:.3f}" if fa['rate'] is not None else "") + f"; cost ${r['cost_usd']:.4f}.", "",
                  "| human \\ judge | " + " | ".join(RESPONSES) + " |", "|---" * (len(RESPONSES) + 1) + "|"]
            for a in RESPONSES:
                if any(r["confusion"][a].values()):
                    L.append(f"| {a} | " + " | ".join(str(r["confusion"][a][b]) for b in RESPONSES) + " |")
            L += ["", f"Disagreements ({len(r['disagreements'])}):", ""]
            for d in r["disagreements"]:
                L.append(f"- {d['item']}: human {d['human']} (note: {d['human_note'] or 'none'}); judge {d['judge']} "
                         f"(engaged {d['judge_engaged']}; evidence {json.dumps(d['judge_evidence'], ensure_ascii=False)}; "
                         f"notes: {d['judge_notes'] or 'none'})")
            L.append("")
        out.write_text("\n".join(L) + "\n", encoding="utf-8")
        print("\n".join(L))
    else:
        raise SystemExit("command must be estimate, run or report")


if __name__ == "__main__":
    main()
