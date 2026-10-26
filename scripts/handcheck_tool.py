"""Terminal tool for the Part 2(c) hand-check (human message 86): mark the 30 sampled private-note sentences that
mention Seller C as price-related and/or message-related. No API calls.

The keyword classification is hidden while marking. Answers are saved after every sentence into the
`your_price_related` and `your_message_related` columns of
results/study1r/exploratory/final_part2/handcheck/HANDCHECK_SENTENCES.csv (True/False); already-marked rows are
skipped, so the tool can be stopped (q) and resumed. Keys: y = yes, n = no, b = back to the previous sentence, q = quit.

Definitions shown:
- price-related: the sentence is about prices, asks, bids, undercutting or price levels;
- message-related: the sentence is about Seller C's message, proposal, offer, question or an agreement.
A sentence can be both or neither.

Usage: python scripts/handcheck_tool.py [--file PATH]
"""
from __future__ import annotations

import argparse
import csv
import sys
import textwrap
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
DEFAULT = REPO / "results" / "study1r" / "exploratory" / "final_part2" / "handcheck" / "HANDCHECK_SENTENCES.csv"
FIELDS = ["your_price_related", "your_message_related"]
QUESTIONS = {"your_price_related": "Price-related? (about prices, asks, bids, undercutting or price levels)",
             "your_message_related": "Message-related? (about Seller C's message, proposal, offer, question or an agreement)"}


def load(path: Path) -> tuple[list[str], list[dict]]:
    with path.open(encoding="utf-8", newline="") as f:
        r = csv.DictReader(f)
        return list(r.fieldnames or []), list(r)


def save(path: Path, header: list[str], rows: list[dict]) -> None:
    tmp = path.with_suffix(".tmp")
    with tmp.open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=header)
        w.writeheader()
        w.writerows(rows)
    tmp.replace(path)


def ask(prompt: str, inp=input) -> str:
    while True:
        a = inp(f"  {prompt} [y/n, b=back, q=quit]: ").strip().lower()
        if a in ("y", "n", "b", "q"):
            return a


def run(path: Path, inp=input, out=print) -> str:
    header, rows = load(path)
    for f in FIELDS:
        if f not in header:
            raise SystemExit(f"column {f} missing in {path}")
    out("Hand-check (Part 2(c)). A sentence can be both or neither. Answers save after each sentence.\n")
    i = next((k for k, r in enumerate(rows) if not all(r[f] for f in FIELDS)), len(rows))
    while i < len(rows):
        r = rows[i]
        done = sum(all(x[f] for f in FIELDS) for x in rows)
        out(f"\n[{i + 1}/{len(rows)}] {r['id']}  ({done} marked)")
        out(textwrap.fill(r["sentence"], 100, initial_indent="  ", subsequent_indent="  "))
        answers = {}
        for f in FIELDS:
            a = ask(QUESTIONS[f], inp)
            if a == "q":
                save(path, header, rows)
                out("Saved. Run again to resume.")
                return "quit"
            if a == "b":
                break
            answers[f] = "True" if a == "y" else "False"
        if len(answers) < len(FIELDS):           # back
            i = max(0, i - 1)
            for f in FIELDS:
                rows[i][f] = ""
            continue
        r.update(answers)
        save(path, header, rows)
        i += 1
    out(f"\nAll {len(rows)} sentences marked. File: {path}")
    return "done"


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--file", type=Path, default=DEFAULT)
    sys.exit(0 if run(ap.parse_args().file) in ("done", "quit") else 1)


if __name__ == "__main__":
    main()
