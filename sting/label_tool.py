"""Terminal tool for the 30 blind hand labels (judge validation; human message 26). No API calls.

Reads items only from <dir>/LABELING_SHEET.md (the sting message and the seller's text fields; any other field in
the sheet is dropped and never shown) and writes labels to <dir>/labels_template.csv, rewriting the file atomically after every confirmed item. A label is
saved only after the confirm step, so quitting mid-item saves nothing partial. On start, items already labeled are
skipped. Single-key input via msvcrt on Windows, with an input() fallback.

Default <dir> is the Study 1R development set, results/study1r/labeling/dev (human message 41), with codebook v2
(which adds the response label conditional_accept, key "o"). Study 1 sheets (labels complete): results/stage2/labeling
and results/stage2/labeling_supp, codebook v1.

Study 1R option A (human message 65): with --stop-map (a file in the keys directory, never in the sheet directory),
the tool applies a hidden within-episode stopping rule. The map gives each verification item an opaque group (its
episode) and whether it is removable (items in Labeler B's sample are not). Once an item of a group is coded accept or
conditional_accept, the group's remaining removable items are silently dropped: the coder sees no episode grouping,
no item total and no skip count. Audit items are not in the map and are always coded.

Usage: python -m sting.label_tool [--dir results/study1r/labeling/dev] [--labels labels_template.csv] [--codebook auto]
                                  [--stop-map <keys>/verify/stop_groups.json]
"""
from __future__ import annotations

import csv
import os
import re
import sys
from collections import Counter
from pathlib import Path
from typing import Any, Callable, Optional

from sting.judge import PROMPT_PATH, SELLER_FIELDS
from sting.paths import REPO_ROOT

# Default: the Study 1R development set (human message 41). Study 1 sheets: --dir results/stage2/labeling[_supp].
LABEL_DIR = REPO_ROOT / "results" / "study1r" / "labeling" / "dev"
SHEET_PATH = LABEL_DIR / "LABELING_SHEET.md"
LABELS_PATH = LABEL_DIR / "labels_template.csv"

RESPONSE_KEYS = {"a": "accept", "r": "reject", "c": "counter", "n": "noncommittal", "i": "ignored",
                 "x": "not_applicable"}
AWARENESS_KEYS = {"t": "test_suspicion", "s": "strategic_distrust", "n": "none"}
# Study 1R codebook v2 adds "conditional accept" (human message 41).
V2_RESPONSE_KEYS = {**RESPONSE_KEYS, "o": "conditional_accept"}
COLUMNS = ["item_id", "response", "awareness", "note"]
MESSAGE_MARKER = "Sting message"

REMINDER = "If the text is ambiguous, choose the more conservative label."


def judge_definitions(prompt_text: str) -> str:
    """Labels 1-3 of the frozen judge prompt, word for word: engaged_with_message, response and awareness, with
    their framing headings (human message 30; closes I-042)."""
    lines = prompt_text.split("\n")
    start = next(i for i, l in enumerate(lines) if l.startswith("1. engaged_with_message:"))
    end = next(i for i, l in enumerate(lines) if l.startswith("4. legal_or_ethical_concern:"))
    return "\n".join(lines[start:end]).strip("\n")


DEFINITIONS = judge_definitions(PROMPT_PATH.read_text(encoding="utf-8")) + "\n\n" + REMINDER


class Quit(Exception):
    pass


def parse_sheet(text: str) -> list[dict[str, Any]]:
    """Items in sheet order: item id, the sting message and the allowed seller fields only."""
    parts = re.split(r"(?m)^---[ \t]*\n\s*\n## (\S+)[ \t]*$", text)
    items = []
    for item_id, body in zip(parts[1::2], parts[2::2]):
        sections: dict[str, str] = {}
        marks = list(re.finditer(r"(?m)^\*\*([^*\n]+):\*\*[ \t]*$", body))
        for m, nxt in zip(marks, marks[1:] + [None]):
            value = body[m.end():nxt.start() if nxt else len(body)].strip("\n")
            sections[m.group(1).strip()] = value
        message = "\n".join(l[2:] if l.startswith("> ") else l for l in sections.get(MESSAGE_MARKER, "").split("\n"))
        item = {"item_id": item_id, "message": message,
                "fields": {k: sections[k] for k in SELLER_FIELDS if k in sections}}
        if "Episode" in sections:  # Study 1R human-coding backup (episode mode, human message 63)
            item["episode"] = sections["Episode"].strip()
        items.append(item)
    return items


INCLUSIVE_ACCEPT = ("accept", "conditional_accept")


def stopped_episodes(items: list[dict[str, Any]], rows: dict[str, dict[str, str]]) -> set[str]:
    """Episode mode: episodes with an inclusive acceptance already coded; their remaining items are not coded."""
    return {it["episode"] for it in items if it.get("episode")
            and (rows.get(it["item_id"]) or {}).get("response") in INCLUSIVE_ACCEPT}


def hidden_stopped(stop_map: dict[str, dict[str, Any]], rows: dict[str, dict[str, str]]) -> set[str]:
    """Option A: items removed by the hidden stopping rule (removable, unlabeled, in a group with a coded inclusive
    acceptance on one of its verification items)."""
    groups = {v["group"] for i, v in stop_map.items() if (rows.get(i) or {}).get("response") in INCLUSIVE_ACCEPT}
    return {i for i, v in stop_map.items() if v["group"] in groups and v["removable"]
            and not (rows.get(i) or {}).get("response")}


def load_labels(path: Path) -> dict[str, dict[str, str]]:
    if not path.is_file():
        return {}
    with path.open(newline="", encoding="utf-8") as f:
        return {r["item_id"]: {c: (r.get(c) or "") for c in COLUMNS} for r in csv.DictReader(f) if r.get("item_id")}


def save_labels(path: Path, order: list[str], rows: dict[str, dict[str, str]]) -> None:
    """Atomic rewrite: earlier answers are never lost if the tool stops mid-write."""
    ids = order + [i for i in rows if i not in order]
    tmp = path.with_name(path.name + ".tmp")
    with tmp.open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=COLUMNS)
        w.writeheader()
        for i in ids:
            w.writerow({**{c: "" for c in COLUMNS}, **rows.get(i, {}), "item_id": i})
        f.flush()
        os.fsync(f.fileno())
    os.replace(tmp, path)


def is_labeled(row: Optional[dict[str, str]], response_keys: Optional[dict[str, str]] = None) -> bool:
    keys = response_keys or RESPONSE_KEYS
    return bool(row) and row["response"] in keys.values() and row["awareness"] in AWARENESS_KEYS.values()


class ConsoleInput:
    """Single keys via msvcrt on a Windows console; otherwise input() (one character per line, empty = Enter)."""

    def __init__(self) -> None:
        try:
            import msvcrt
            self.msvcrt = msvcrt if sys.stdin.isatty() else None
        except ImportError:
            self.msvcrt = None

    def key(self, prompt: str) -> str:
        if self.msvcrt is None:
            s = input(prompt).strip()
            return "\r" if s == "" else (s.lower() if len(s) == 1 else "")
        print(prompt, end="", flush=True)
        ch = self.msvcrt.getwch()
        if ch in ("\x00", "\xe0"):  # arrow and function keys send two codes
            self.msvcrt.getwch()
            ch = ""
        if ch == "\x03":
            raise KeyboardInterrupt
        print("" if ch in ("\r", "\n", "") else ch)
        return "\r" if ch == "\n" else ch.lower()

    def line(self, prompt: str) -> str:
        return input(prompt)


def render(item: dict[str, Any], n: int, total: Optional[int], definitions: Optional[str] = None,
           episode_pos: Optional[tuple[int, int]] = None) -> str:
    head = f"Item {n} of {total}" if total is not None else f"Item {n}"
    if item.get("episode"):
        head += (f"   |   Episode {item['episode']}, message {episode_pos[0]} of {episode_pos[1]} "
                 "(coding stops at the first accept or conditional_accept)")
    lines = ["=" * 78, head, "=" * 78, "", "Seller C's message:", item["message"], "",
             "Seller's text:"]
    for k in SELLER_FIELDS:
        if k in item["fields"]:
            lines += [f"[{k}]", item["fields"][k], ""]
    lines += ["-" * 78, definitions or DEFINITIONS, "-" * 78]
    return "\n".join(lines)


def codebook_v2_definitions(prompt_file: Optional[Path] = None) -> str:
    """Study 1R: the judge v2 prompt's codebook v2 and labels 1-3, word for word, plus the reminder. `prompt_file`
    pins an archived prompt version, so both validation passes show the same text."""
    from sting.judge_v2 import PROMPT_V2_PATH
    lines = (prompt_file or PROMPT_V2_PATH).read_text(encoding="utf-8").split("\n")
    start = next(i for i, l in enumerate(lines) if l.startswith("# Codebook v2"))
    end = next(i for i, l in enumerate(lines) if l.startswith("4. evidence:"))
    return "\n".join(lines[start:end]).strip("\n") + "\n\n" + REMINDER


def ask_key(inp, prompt: str, allowed: dict[str, str], out: Callable[[str], None]) -> str:
    while True:
        k = inp.key(prompt)
        if k == "q":
            raise Quit
        if k in allowed:
            return k
        out("  (invalid key, try again)")


def label_item(inp, out: Callable[[str], None], response_keys: Optional[dict[str, str]] = None) -> dict[str, str]:
    """One item's labels after the confirm step; raises Quit (nothing saved) on q at any prompt."""
    keys = response_keys or RESPONSE_KEYS
    menu = " ".join(f"{k}={v}" for k, v in keys.items())
    while True:
        r = ask_key(inp, f"Response [{menu}, q=quit]: ", keys, out)
        a = ask_key(inp, "Awareness [t=test_suspicion s=strategic_distrust n=none, q=quit]: ", AWARENESS_KEYS, out)
        note = inp.line("Note (Enter to skip, q=quit): ").strip()
        if note.lower() == "q":
            raise Quit
        choice = {"response": keys[r], "awareness": AWARENESS_KEYS[a], "note": note}
        out(f"  -> response={choice['response']}  awareness={choice['awareness']}  note={note or '(none)'}")
        c = ask_key(inp, "Enter = save and next, b = redo this item, q = quit: ", {"\r": "save", "b": "redo"}, out)
        if c == "\r":
            return choice
        out("  Redo this item.")


def validate(rows: dict[str, dict[str, str]], order: list[str], out: Callable[[str], None],
             response_keys: Optional[dict[str, str]] = None, skipped: frozenset = frozenset(),
             quiet: bool = False) -> bool:
    """quiet: option A hidden stopping rule; the row count (which would reveal removed items) is not shown."""
    keys = response_keys or RESPONSE_KEYS
    problems = []
    if len(rows) != len(order) or set(rows) != set(order):
        problems.append(f"expected {len(order)} rows for the sheet's items, found {len(rows)}")
    for i in order:
        row = rows.get(i)
        if i not in skipped and not is_labeled(row, keys):
            problems.append(f"{i}: missing or invalid label")
    out(f"Validation: {'OK' if not problems else 'FAILED'}" + ("" if quiet else f" ({len(rows)} rows)"))
    for p in problems:
        out(f"  {p}")
    for col in ("response", "awareness"):
        counts = Counter(r[col] for r in rows.values())
        out(f"{col}: " + ", ".join(f"{v} {counts.get(v, 0)}" for v in
                                   (keys if col == "response" else AWARENESS_KEYS).values()))
    return not problems


def run(sheet_path: Path = SHEET_PATH, labels_path: Path = LABELS_PATH, inp=None,
        out: Callable[[str], None] = print, definitions: Optional[str] = None,
        response_keys: Optional[dict[str, str]] = None, stop_map: Optional[dict[str, dict[str, Any]]] = None) -> str:
    """Returns "done", "quit" or "invalid". `stop_map`: option A hidden stopping rule (see module docstring)."""
    keys = response_keys or RESPONSE_KEYS
    inp = inp or ConsoleInput()
    items = parse_sheet(sheet_path.read_text(encoding="utf-8"))
    order = [it["item_id"] for it in items]
    rows = load_labels(labels_path)
    episode_mode = any(it.get("episode") for it in items)
    ep_items: dict[str, list[str]] = {}
    for it in items:
        if it.get("episode"):
            ep_items.setdefault(it["episode"], []).append(it["item_id"])

    def next_pending() -> Optional[int]:
        stopped = stopped_episodes(items, rows) if episode_mode else set()
        removed = hidden_stopped(stop_map, rows) if stop_map else set()
        for n, it in enumerate(items, 1):
            if (not is_labeled(rows.get(it["item_id"]), keys) and it.get("episode") not in stopped
                    and it["item_id"] not in removed):
                return n
        return None

    def done_count() -> int:
        return sum(is_labeled(rows.get(i), keys) for i in order)

    first = next_pending()
    if first and any(is_labeled(rows.get(i), keys) for i in order):
        out(f"Resuming at item {done_count() + 1 if stop_map else first}")
    try:
        while (n := next_pending()) is not None:
            item = items[n - 1]
            pos = (ep_items[item["episode"]].index(item["item_id"]) + 1, len(ep_items[item["episode"]])) \
                if item.get("episode") else None
            shown = done_count() + 1 if stop_map else n
            out(render(item, shown, None if stop_map else len(items), definitions, pos))
            rows[item["item_id"]] = {"item_id": item["item_id"], **label_item(inp, out, keys)}
            save_labels(labels_path, order, rows)
            out(f"Saved item {shown}.")
            if episode_mode and rows[item["item_id"]]["response"] in INCLUSIVE_ACCEPT:
                out(f"  Episode {item['episode']}: acceptance coded; its remaining messages are skipped.")
    except (Quit, KeyboardInterrupt, EOFError):
        out(f"Progress saved: {done_count()} labeled. Quit." if stop_map else
            f"Progress saved: {done_count()} of {len(items)} labeled. Quit.")
        return "quit"
    skipped = {i for e in stopped_episodes(items, rows) for i in ep_items.get(e, [])
               if not is_labeled(rows.get(i), keys)} if episode_mode else set()
    if stop_map:
        skipped = hidden_stopped(stop_map, rows)
        out(f"All items done: {done_count()} labeled")
    elif episode_mode:
        out(f"All episodes done: {len(order) - len(skipped)} labeled, {len(skipped)} skipped after an acceptance")
    else:
        out(f"All {len(items)} labeled")
    return "done" if validate(load_labels(labels_path), order, out, keys, skipped, quiet=bool(stop_map)) else "invalid"


def main() -> None:
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    import argparse
    parser = argparse.ArgumentParser(description="Blind hand-labeling tool")
    parser.add_argument("--dir", type=Path, default=LABEL_DIR, help="Directory with LABELING_SHEET.md")
    parser.add_argument("--prompt-file", type=Path, default=None,
                        help="Study 1R: show the codebook from this archived judge v2 prompt (default: current prompt)")
    parser.add_argument("--labels", default="labels_template.csv",
                        help="Label file name in --dir (Study 1R: one file per labeler, e.g. labels_A.csv)")
    parser.add_argument("--codebook", choices=["auto", "v1", "v2"], default="auto",
                        help="v1: Study 1 judge definitions; v2: Study 1R codebook v2 (judge v2 prompt, adds "
                             "conditional_accept); auto: v2 for directories under results/study1r, else v1")
    parser.add_argument("--stop-map", type=Path, default=None,
                        help="Study 1R option A: hidden stopping-rule map from the keys directory (stop_groups.json)")
    args = parser.parse_args()
    d = args.dir
    stop_map = None
    if args.stop_map:
        import json
        stop_map = json.loads(args.stop_map.read_text(encoding="utf-8"))
    v2 = args.codebook == "v2" or (args.codebook == "auto" and "study1r" in d.resolve().as_posix())
    status = run(d / "LABELING_SHEET.md", d / args.labels,
                 definitions=codebook_v2_definitions(args.prompt_file) if v2 else None,
                 response_keys=V2_RESPONSE_KEYS if v2 else RESPONSE_KEYS, stop_map=stop_map)
    sys.exit(0 if status in ("done", "quit") else 1)


if __name__ == "__main__":
    main()
