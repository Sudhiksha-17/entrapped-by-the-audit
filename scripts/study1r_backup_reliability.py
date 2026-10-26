"""Study 1R human-coding reliability under option A (human message 64; prereg_study1r/PREREG.md section 8). No API
calls.

  agreement <A_sheet_dir> <A_key_dir> <B_sheet_dir> <B_key_dir>
      Labeler B codes a random 20% of the verification set (screener accept or conditional_accept) in the `verify_B`
      sheet; Labeler A's labels for the same messages come from the `verify` sheet (matched through the keys by
      replicate, seller and round). Reported: response agreement (raw, Cohen's kappa with bootstrap 95% CI, D-071) and
      inclusive acceptance (accept or conditional_accept vs not: 2 x 2 table, raw agreement, kappa with CI).
The miss audit is computed in sting.study1r_analysis.miss_rates from the verify sheet's audit strata.
"""
from __future__ import annotations

import csv
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from sting.stage2_analysis import kappa_with_ci  # noqa: E402
from sting.study1r_measures import ACCEPT_INCLUSIVE  # noqa: E402


def coded(sheet_dir: Path, key_dir: Path) -> dict[tuple, str]:
    """(replicate, seller, round) -> response, coded rows only."""
    key = json.loads((key_dir / "labeling_key.json").read_text(encoding="utf-8"))
    with (sheet_dir / "labels_template.csv").open(newline="", encoding="utf-8") as f:
        rows = {r["item_id"]: r for r in csv.DictReader(f)}
    return {(k["replicate_id"], k["seller"], k["round"]): rows[i]["response"]
            for i, k in key.items() if rows.get(i, {}).get("response")}


def agreement(a_sheet: Path, a_key: Path, b_sheet: Path, b_key: Path) -> dict:
    a, b = coded(a_sheet, a_key), coded(b_sheet, b_key)
    items = sorted(b)
    missing = [i for i in items if i not in a]
    if missing:
        raise SystemExit(f"{len(missing)} Labeler B items not coded by Labeler A, e.g. {missing[0]}")
    ra, rb = [a[i] for i in items], [b[i] for i in items]
    xa = ["accept" if r in ACCEPT_INCLUSIVE else "not" for r in ra]
    xb = ["accept" if r in ACCEPT_INCLUSIVE else "not" for r in rb]
    table = {f"A {p} / B {q}": sum(1 for x, y in zip(xa, xb) if (x, y) == (p, q))
             for p in ("accept", "not") for q in ("accept", "not")}
    return {"items": len(items),
            "response": {"raw_agreement": sum(x == y for x, y in zip(ra, rb)) / len(items), "kappa": kappa_with_ci(ra, rb)},
            "inclusive_acceptance": {"table": table, "raw_agreement": sum(x == y for x, y in zip(xa, xb)) / len(items),
                                     "kappa": kappa_with_ci(xa, xb)}}


def main() -> None:
    if sys.argv[1] != "agreement":
        raise SystemExit("command must be agreement")
    print(json.dumps(agreement(*(Path(p) for p in sys.argv[2:6])), indent=2))


if __name__ == "__main__":
    main()
