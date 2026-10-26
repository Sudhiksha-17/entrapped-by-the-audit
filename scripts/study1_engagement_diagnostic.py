"""Study 1 engagement diagnostic (human messages 34 and 36; issue I-044). Exploratory; no API calls.

Inputs: the 40 Study 1 judge runs (runs/judge/*/labels.jsonl, judge v1), the two validation samples' keys, the
confirmatory campaign logs and the sellers' upstream logs.

1. No-proposal items (sham, anchor, rapport) in both validation samples: judge engaged_with_message "yes" count.
2. Judge engaged rate by round: round 11 (Seller C's message visible in the seller's prompt) versus rounds 12-30
   (not visible, I-043), overall, by arm, and per round.
3. Invalid judge outputs by arm.
4. Judge-independent check: share of seller-rounds whose own text names "Seller C" (regex \\bSeller C\\b), in
   message_to_sellers and in any of the six text fields, round 11 versus rounds 12-30. Naming Seller C is necessary,
   not sufficient, for engagement under the N-2 rule.

Usage: python scripts/study1_engagement_diagnostic.py
"""
from __future__ import annotations

import glob
import json
import re
import sys
from collections import Counter, defaultdict
from pathlib import Path

import yaml

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from sting.judge import SELLER_FIELDS, seller_responses  # noqa: E402
from sting.paths import REPO_ROOT  # noqa: E402
from sting.stage2_analysis import wilson  # noqa: E402

OUT = REPO_ROOT / "results" / "study1_diagnostics"
ARMS = ["sham", "anchor", "rapport", "directive", "offer"]
SELLER_C = re.compile(r"\bSeller C\b")


def rate(k: int, n: int) -> str:
    lo, hi = wilson(k, n)
    return f"{k}/{n} = {k / n:.3f} [{lo:.3f}, {hi:.3f}]" if n else "0/0"


def main() -> None:
    arms = {a["name"]: a for a in yaml.safe_load((REPO_ROOT / "configs" / "stage2" / "campaign.yaml")
                                                 .read_text(encoding="utf-8"))["arms"]}
    rep_arm, rep_dirs = {}, {}
    for c in sorted(glob.glob(str(REPO_ROOT / "runs" / "stage2" / "_campaigns" / "*" / "campaign.json"))):
        for name, info in json.loads(Path(c).read_text(encoding="utf-8"))["arms"].items():
            for rep in Path(info["run_dir"]).iterdir():
                if rep.is_dir():
                    rep_arm[rep.name] = (arms[name]["arm"], arms[name]["cell"], name)
                    rep_dirs[rep.name] = rep
    labels = [json.loads(l) for p in sorted(glob.glob(str(REPO_ROOT / "runs" / "judge" / "*" / "labels.jsonl")))
              for l in open(p, encoding="utf-8")]
    labels = [l for l in labels if l["replicate_id"] in rep_arm]           # Study 1 confirmatory, judge v1
    ok = [l for l in labels if l["status"] == "ok"]
    R: dict = {"items": len(labels), "valid": len(ok)}

    # 1
    by_key = {(l["replicate_id"], l["seller"], l["round"]): l for l in labels}
    nop = []
    for sample in ("labeling_key", "labeling_supp_key"):
        for item, k in json.loads((REPO_ROOT / "results" / "stage2" / sample / "labeling_key.json")
                                  .read_text(encoding="utf-8")).items():
            if k["condition"] in ("sham", "anchor", "rapport"):
                j = by_key[(k["replicate_id"], k["seller"], k["round"])]
                nop.append({"sample": sample, "item": item, "arm": k["condition"], "round": k["round"],
                            "status": j["status"], "engaged": j.get("engaged_with_message"), "response": j.get("response")})
    vn = [x for x in nop if x["status"] == "ok"]
    R["no_proposal"] = {"engaged": sum(x["engaged"] == "yes" for x in vn), "valid": len(vn), "total": len(nop),
                        "responses": dict(Counter(x["response"] for x in vn)), "items": nop}

    # 2
    def eng(rows):
        return sum(r["engaged_with_message"] == "yes" for r in rows), len(rows)
    R["engaged_r11"] = eng([l for l in ok if l["round"] == 11])
    R["engaged_r12_30"] = eng([l for l in ok if l["round"] >= 12])
    R["engaged_by_arm"] = {a: {"r11": eng([l for l in ok if rep_arm[l["replicate_id"]][0] == a and l["round"] == 11]),
                               "r12_30": eng([l for l in ok if rep_arm[l["replicate_id"]][0] == a and l["round"] >= 12])}
                           for a in ARMS}
    R["engaged_by_round"] = {r: eng([l for l in ok if l["round"] == r]) for r in range(11, 31)}

    # 3
    inv = Counter(rep_arm[l["replicate_id"]][2] for l in labels if l["status"] != "ok")
    tot = Counter(rep_arm[l["replicate_id"]][2] for l in labels)
    R["invalid_by_arm"] = {a: (inv.get(a, 0), n) for a, n in sorted(tot.items())}

    # 4 (judge-independent)
    names = defaultdict(lambda: [0, 0, 0])          # (round group, arm) -> [n, msg names C, any field names C]
    for rid, rep in rep_dirs.items():
        arm = rep_arm[rid][0]
        if arm == "silent":
            continue
        llm = json.loads((rep / "market_setup.json").read_text(encoding="utf-8"))["llm_seller_ids"]
        for s in llm:
            for rnd, resp in seller_responses(rep / "upstream_logs" / f"{s}.md").items():
                if rnd < 11:
                    continue
                g = "r11" if rnd == 11 else "r12_30"
                msg = str(resp.get("message_to_sellers") or "")
                anyf = " ".join(str(resp.get(k) or "") for k in SELLER_FIELDS)
                for key in ((g, arm), (g, "all")):
                    names[key][0] += 1
                    names[key][1] += bool(SELLER_C.search(msg))
                    names[key][2] += bool(SELLER_C.search(anyf))
    R["names_seller_c"] = {f"{g}|{a}": v for (g, a), v in sorted(names.items())}

    OUT.mkdir(parents=True, exist_ok=True)
    (OUT / "engagement.json").write_text(json.dumps(R, indent=2), encoding="utf-8")
    L = ["# Study 1 engagement diagnostic (EXPLORATORY)", "",
         "Generated by `scripts/study1_engagement_diagnostic.py` (no API calls). Judge v1 labels from the 40 Study 1 "
         "judge runs; Wilson 95% CIs. Seller C's message was in the seller's prompt in round 11 only (I-043). Facts "
         "only.", "",
         f"Judge items: {R['items']}; valid: {R['valid']}.", "",
         "## 1. No-proposal validation items (sham, anchor, rapport; both samples)", "",
         f"Judge engaged on {R['no_proposal']['engaged']} of {R['no_proposal']['valid']} valid items "
         f"({R['no_proposal']['total']} items). Judge response on these: {R['no_proposal']['responses']}.", "",
         "| Sample | Item | Arm | Round | Judge engaged | Judge response |", "|---|---|---|---|---|---|"]
    for x in R["no_proposal"]["items"]:
        L.append(f"| {x['sample'].replace('_key', '')} | {x['item']} | {x['arm']} | {x['round']} | {x['engaged']} | "
                 f"{x['response']} |")
    L += ["", "## 2. Judge engaged rate by round", "",
          f"- Round 11: {rate(*R['engaged_r11'])}", f"- Rounds 12-30: {rate(*R['engaged_r12_30'])}", "",
          "| Arm | Round 11 | Rounds 12-30 |", "|---|---|---|"]
    for a, v in R["engaged_by_arm"].items():
        L.append(f"| {a} | {rate(*v['r11'])} | {rate(*v['r12_30'])} |")
    L += ["", "| Round | Engaged / valid |", "|---|---|"]
    for r, v in R["engaged_by_round"].items():
        L.append(f"| {r} | {rate(*v)} |")
    L += ["", "## 3. Invalid judge outputs by arm", "", "| Arm | Invalid | Items |", "|---|---|---|"]
    for a, (k, n) in R["invalid_by_arm"].items():
        L.append(f"| {a} | {k} | {n} |")
    L += ["", "## 4. Judge-independent: seller text names \"Seller C\"", "",
          "Share of seller-rounds whose own text contains \"Seller C\" (necessary, not sufficient, for engagement "
          "under the N-2 rule).", "",
          "| Arm | Round 11: message_to_sellers | Round 11: any text field | Rounds 12-30: message_to_sellers | "
          "Rounds 12-30: any text field |", "|---|---|---|---|---|"]
    for a in ["all"] + ARMS:
        r11, rl = R["names_seller_c"].get(f"r11|{a}", [0, 0, 0]), R["names_seller_c"].get(f"r12_30|{a}", [0, 0, 0])
        L.append(f"| {a} | {rate(r11[1], r11[0])} | {rate(r11[2], r11[0])} | {rate(rl[1], rl[0])} | {rate(rl[2], rl[0])} |")
    (OUT / "ENGAGEMENT.md").write_text("\n".join(L) + "\n", encoding="utf-8")
    print("\n".join(L))


if __name__ == "__main__":
    main()
