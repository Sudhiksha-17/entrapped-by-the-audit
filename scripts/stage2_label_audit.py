"""Audit of the 30 labeled items against the key and raw logs (human message 27). Run after the labels were committed.

Per item: arm type, cell and round (from the key); whether Seller C's full message text appears in that seller's
prompt for that round, by section (messages received, Your Memory, Current Strategy Scratchpad, elsewhere), plus
the share of the message's 6-word sequences found in memory and scratchpad (to catch partial quotes) and
whether memory or scratchpad names Seller C at all; and whether
each seller text field shown in the sheet (as parsed by sting.label_tool) equals the raw upstream response field.
Prints flags and counts only: no asks, prices, seller text, labels or judge output.

Usage: python scripts/stage2_label_audit.py <out.json> <out.md>
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from sting.judge import SELLER_FIELDS, seller_responses  # noqa: E402
from sting.label_tool import parse_sheet  # noqa: E402
from sting.paths import REPO_ROOT  # noqa: E402

SHEET_PATH = REPO_ROOT / "results" / "stage2" / "labeling" / "LABELING_SHEET.md"
KEY_PATH = REPO_ROOT / "results" / "stage2" / "labeling_key" / "labeling_key.json"
RUNS = REPO_ROOT / "runs" / "stage2"
HEADERS = {"memory": "# Your Memory", "messages": "# Messages Received from Other Sellers (Previous Hour)",
           "scratchpad": "# Current Strategy Scratchpad"}
ALL_HEADERS = ["# Introduction", "# Market Rules", "# Your Memory", "# Market Status", "# Your Successful Trades So Far",
               HEADERS["messages"], HEADERS["scratchpad"], "# Output Format"]


def prompts(md: Path) -> dict[int, str]:
    text = md.read_text(encoding="utf-8")
    return {int(m.group(1)): m.group(2) for m in
            re.finditer(r"## Prompt: Round (\d+) - [^\n]*\n`{6}\n(.*?)\n`{6}", text, flags=re.S)}


def section(prompt: str, header: str) -> str:
    """Text from a top-level template header to the next known top-level header."""
    i = prompt.find("\n" + header + "\n")
    if i < 0:
        return ""
    start = i + len(header) + 2
    ends = [prompt.find("\n" + h + "\n", start) for h in ALL_HEADERS if h != header]
    ends = [e for e in ends if e >= 0]
    return prompt[start:min(ends) if ends else len(prompt)]


def shingle_share(message: str, text: str, n: int = 6) -> float:
    words = message.split()
    grams = [" ".join(words[i:i + n]) for i in range(max(1, len(words) - n + 1))]
    flat = " ".join(text.split())
    return sum(g in flat for g in grams) / len(grams)


def find_rep(replicate_id: str) -> Path:
    hits = [p for p in RUNS.glob(f"*/{replicate_id}") if p.is_dir()]
    if len(hits) != 1:
        raise SystemExit(f"{replicate_id}: {len(hits)} directories found")
    return hits[0]


def main() -> None:
    key = json.loads(KEY_PATH.read_text(encoding="utf-8"))
    shown = {it["item_id"]: it for it in parse_sheet(SHEET_PATH.read_text(encoding="utf-8"))}
    rows = []
    for item_id in sorted(key):
        k = key[item_id]
        rep = find_rep(k["replicate_id"])
        sting_log = json.loads((rep / "sting_log.json").read_text(encoding="utf-8"))
        setup = json.loads((rep / "market_setup.json").read_text(encoding="utf-8"))
        msg = sting_log["message_text"]
        md = rep / "upstream_logs" / f"{k['seller']}.md"
        prompt = prompts(md).get(k["round"], "")
        secs = {name: section(prompt, h) for name, h in HEADERS.items()}
        needle = f"- From {setup['sting_id']}: {msg}"
        rest = prompt
        for s in secs.values():
            rest = rest.replace(s, "")
        raw = seller_responses(md)[k["round"]]
        field_match = {f: (str(raw.get(f) or "").strip("\n") == shown[item_id]["fields"][f]) for f in SELLER_FIELDS}
        rows.append({
            "item_id": item_id, "arm_type": k["condition"], "cell": k["cell"], "round": k["round"],
            "prompt_found": bool(prompt), "sheet_message_matches_sting_log": shown[item_id]["message"] == msg,
            "in_messages_section": needle in secs["messages"],
            "in_memory": msg in secs["memory"], "in_scratchpad": msg in secs["scratchpad"],
            "in_prompt_elsewhere": msg in rest,
            "memory_6gram_share": round(shingle_share(msg, secs["memory"]), 2),
            "scratchpad_6gram_share": round(shingle_share(msg, secs["scratchpad"]), 2),
            "memory_mentions_seller_c": setup["sting_id"] in secs["memory"],
            "scratchpad_mentions_seller_c": setup["sting_id"] in secs["scratchpad"],
            "fields_all_match": all(field_match.values()),
            "fields_mismatched": [f for f, ok in field_match.items() if not ok],
            "raw_text_fields_not_in_sheet": sorted(f for f, v in raw.items() if f not in SELLER_FIELDS and isinstance(v, str)),
            "raw_nontext_field_names": sorted(f for f, v in raw.items() if f not in SELLER_FIELDS and not isinstance(v, str)),
        })
    offer_r11_total = 0
    for rep in RUNS.glob("*_offer_*/*"):
        if not rep.is_dir() or "_campaigns" in str(rep):
            continue
        cfg = json.loads((rep.parent / "run_config.json").read_text(encoding="utf-8"))["config"]
        st = json.loads((rep / "status.json").read_text(encoding="utf-8"))
        if cfg.get("run_type") != "confirmatory" or st["status"] != "completed":
            continue
        setup = json.loads((rep / "market_setup.json").read_text(encoding="utf-8"))
        offer_r11_total += sum(11 in seller_responses(rep / "upstream_logs" / f"{s}.md") for s in setup["llm_seller_ids"])
    summary = {"items": len(rows), "offer_round11_seller_rounds_total": offer_r11_total,
               "offer_round11_items": sum(r["arm_type"] == "offer" and r["round"] == 11 for r in rows)}
    Path(sys.argv[1]).write_text(json.dumps({"summary": summary, "items": rows}, indent=2), encoding="utf-8")
    yn = lambda b: "yes" if b else "no"  # noqa: E731
    lines = ["| Item | Arm type | Cell | Round | Messages section | Memory (full / 6-gram share) | "
             "Scratchpad (full / 6-gram share) | Elsewhere | Fields match raw log |", "|---|---|---|---|---|---|---|---|---|"]
    for r in rows:
        lines.append(f"| {r['item_id']} | {r['arm_type']} | {r['cell']} | {r['round']} | {yn(r['in_messages_section'])} | "
                     f"{yn(r['in_memory'])} / {r['memory_6gram_share']} | {yn(r['in_scratchpad'])} / "
                     f"{r['scratchpad_6gram_share']} | {yn(r['in_prompt_elsewhere'])} | "
                     f"{'all 6' if r['fields_all_match'] else 'MISMATCH ' + ','.join(r['fields_mismatched'])} |")
    lines += ["", json.dumps(summary)]
    Path(sys.argv[2]).write_text("\n".join(lines) + "\n", encoding="utf-8")
    print("\n".join(lines))
    print("prompt_found all:", all(r["prompt_found"] for r in rows),
          "| sheet message == sting log:", sum(r["sheet_message_matches_sting_log"] for r in rows),
          "| raw text fields not in sheet:", sorted({f for r in rows for f in r["raw_text_fields_not_in_sheet"]}),
          "| raw non-text field names:", sorted({f for r in rows for f in r["raw_nontext_field_names"]}))
    print("memory mentions Seller C:", sum(r["memory_mentions_seller_c"] for r in rows),
          "| scratchpad mentions Seller C:", sum(r["scratchpad_mentions_seller_c"] for r in rows))


if __name__ == "__main__":
    main()
