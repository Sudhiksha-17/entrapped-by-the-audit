"""Pre-push check of a release folder (human message 103). No API calls; read-only on the folder.

1. Lists every column of every CSV and every key (at any depth) of every JSON and JSONL file, and flags any whose name
   is a coder free-text field: note, notes, note_A, note_B, reason, comment, comments, unresolved (case-insensitive).
2. Searches every file for each labeler note of 25 or more characters verbatim (whitespace-normalised; notes read
   from the note columns of the repository's human label files).
3. Searches every file for API keys and tokens, `.env` files, local absolute paths and the local user name or e-mail.
Writes <out_json> with the full column/key listing and the findings (counts and file names only; matched secrets and
note text are never written). Exit status 1 if anything is found.

Usage: python scripts/release_check.py <release_dir> <out_json>
"""
from __future__ import annotations

import csv
import io
import json
import re
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO / "scripts"))
import build_release as br  # noqa: E402

FORBIDDEN = {"note", "notes", "note_a", "note_b", "reason", "comment", "comments", "unresolved"}


def keys(o, prefix: str = "") -> set[str]:
    out = set()
    if isinstance(o, dict):
        for k, v in o.items():
            out.add(f"{prefix}{k}")
            out |= keys(v, f"{prefix}{k}.")
    elif isinstance(o, list):
        for v in o:
            out |= keys(v, prefix)
    return out


def leaf(name: str) -> str:
    return name.rsplit(".", 1)[-1].lower()


def main() -> None:
    rel, out_json = Path(sys.argv[1]), Path(sys.argv[2])
    files = sorted(p for p in rel.rglob("*") if p.is_file() and ".git" not in p.relative_to(rel).parts)
    columns, bad_cols, notes_hit, secrets, envs, paths, ident, unreadable = {}, {}, {}, {}, [], [], [], []
    note_text = br.notes()
    ids = br.local_identity()
    home = br.path_forms(Path.home()) + br.path_forms(REPO.parent)
    generic = re.compile(r"(?i)(?<![A-Za-z])[A-Z]:(?:\\\\|\\|/)(?:Users|Projects)\b|/c/U[s]ers/|\\U[s]ers\\")  # [s]: no self-match
    for p in files:
        r = p.relative_to(rel).as_posix()
        if p.name == ".env" or p.name.startswith(".env.") and p.name != ".env.example":
            envs.append(r)
        try:
            text = p.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            if br.is_text(p):
                unreadable.append(r)
            continue
        try:
            if p.suffix == ".csv":
                columns[r] = next(csv.reader(io.StringIO(text)), [])
            elif p.suffix == ".json":
                columns[r] = sorted(keys(json.loads(text)))
            elif p.suffix == ".jsonl":
                ks = set()
                for line in text.splitlines():
                    if line.strip():
                        ks |= keys(json.loads(line))
                columns[r] = sorted(ks)
        except (json.JSONDecodeError, StopIteration):
            unreadable.append(r)
        if r in columns:
            b = [c for c in columns[r] if leaf(c) in FORBIDDEN]
            if b:
                bad_cols[r] = b
        norm = " ".join(text.split())
        n = sum(t in norm for t in note_text)
        if n:
            notes_hit[r] = n
        for k, rx in br.KEY_PATTERNS.items():
            if rx.search(text):
                secrets.setdefault(k, []).append(r)
        if any(h in text for h in home) or generic.search(text):
            paths.append(r)
        low = text.lower()
        if any(i.lower() in low for i in ids):
            ident.append(r)
    res = {"release_dir_files": len(files), "labeler_notes_searched": len(note_text),
           "forbidden_column_names": sorted(FORBIDDEN), "coder_text_columns_found": bad_cols,
           "files_with_verbatim_notes": notes_hit, "secrets": secrets, "env_files": envs,
           "files_with_local_paths": paths, "files_with_local_identity": ident, "unreadable_text_files": unreadable,
           "columns": columns}
    out_json.write_text(json.dumps(res, indent=1), encoding="utf-8")
    fail = any([bad_cols, notes_hit, secrets, envs, paths, ident, unreadable])
    print(json.dumps({k: v for k, v in res.items() if k != "columns"}, indent=1))
    print(f"files with columns or keys listed: {len(columns)}; RESULT: {'FAIL' if fail else 'PASS'}")
    sys.exit(1 if fail else 0)


if __name__ == "__main__":
    main()
