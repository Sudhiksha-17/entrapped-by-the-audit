"""Build release/ as a clean public snapshot (human message 82 step 6). No API calls; nothing is pushed; no remote.

Contents (from committed files at HEAD, plus read-only copies from runs/):
- code (sting/, scripts/, tests/, patches/), configs/, preregistrations with freeze files (prereg/, prereg_study1r/),
  deviation files (notes/PREREG_DEVIATIONS.md; results/paper/APPENDIX_B_DEVIATIONS.md), notes/requirements_lock.txt,
  .env.example, .gitmodules, results/ (analysis outputs, figures, run manifests and reports), ledger/ (cost ledger;
  added on human message 84);
- per-episode results: results_per_episode/ (scripts/export_per_episode.py);
- judge outputs: judge_outputs/<run>/ (labels.jsonl, judge_summary.json, judge_run.json, manifest.json from runs/judge);
- human label files with the note columns removed (note, note_A, note_B, reason): item ids and keystroke labels only;
- sample transcripts: sample_transcripts/<study>/<replicate>/ (replicate index 0 of every arm; calls.jsonl left out).

Excluded: .env, .venv, runs/ (except the copies above), CLAUDE.md and internal notes, labeling keys and any other file
that contains labeler note text (checked by verbatim match against every note of 25 characters or more).

Scan: every release file is checked for API keys and tokens, local absolute paths, the local user name and e-mail;
absolute paths are redacted (repository root -> <repo>, other user paths -> <local>). Report: release/RELEASE_SCAN.md
(counts and file names only; matched secrets are never printed). Manifest: release/RELEASE_MANIFEST.md.

Usage: python scripts/build_release.py
"""
from __future__ import annotations

import csv
import hashlib
import io
import json
import os
import re
import shutil
import subprocess
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
OUT = REPO / "release"
KEEP = {"README.md", "benchmark", "LICENSE", "LICENSE-DATA"}   # tracked: hand-written README and licenses; benchmark
                                                                # built by scripts/build_benchmark.py
# coder free-text columns (human message 103: notes, note_A, note_B, reason, comments, unresolved)
NOTE_COLS = ("note", "note_A", "note_B", "reason", "comment", "comments", "unresolved")
D_RUNS = REPO.parent / "s1rd" / "runs"                  # Study 1R-D raw runs (worktree; read-only)
NOTE_MIN = 25
# Files that quote a short fragment of a labeler note (below NOTE_MIN, so not caught automatically); withheld by hand.
MANUAL_EXCLUDE = {
    "results/study1r/judge_dev/REVISIONS.md": "quotes a fragment of development-set labeler notes",
    "results/paper/APPENDIX_C_MATERIALS.md": "embeds results/study1r/judge_dev/REVISIONS.md",
}
TRACKED_PREFIXES = ("sting/", "scripts/", "tests/", "patches/", "configs/", "prereg/", "prereg_study1r/", "results/",
                    "ledger/")
TRACKED_FILES = ("notes/PREREG_DEVIATIONS.md", "notes/requirements_lock.txt", ".env.example", ".gitmodules")
JUDGE_FILES = ("labels.jsonl", "judge_summary.json", "judge_run.json", "manifest.json")
TRANSCRIPT_STUDIES = ("study1r", "study1r_addon_A", "study1r_addon_C", "stage2")
TEXT_EXT = {".py", ".md", ".json", ".jsonl", ".csv", ".yaml", ".yml", ".txt", ".jinja2", ".patch", ".log", ".toml",
            ".cfg", ".ini", ".example", ".gitmodules", ""}

KEY_PATTERNS = {
    "OpenRouter key": re.compile(r"sk-or-v1-[0-9a-f]{32,}"),
    "OpenAI-style key": re.compile(r"\bsk-(?:proj-)?[A-Za-z0-9_-]{32,}"),
    "Anthropic key": re.compile(r"sk-ant-[A-Za-z0-9_-]{20,}"),
    "Bearer token": re.compile(r"Bearer\s+[A-Za-z0-9._-]{20,}"),
    "GitHub token": re.compile(r"\bgh[pousr]_[A-Za-z0-9]{20,}"),
    "AWS key id": re.compile(r"\bAKIA[0-9A-Z]{16}\b"),
    "Google API key": re.compile(r"\bAIza[0-9A-Za-z_-]{35}\b"),
    "Slack token": re.compile(r"\bxox[abpr]-[A-Za-z0-9-]{10,}"),
    "private key block": re.compile(r"-----BEGIN [A-Z ]*PRIVATE KEY-----"),
    "W&B key assignment": re.compile(r"WANDB_API_KEY\s*=\s*\S{20,}"),
}


def git(*a: str) -> str:
    return subprocess.run(["git", *a], cwd=REPO, capture_output=True, text=True, encoding="utf-8", check=True).stdout


def local_identity() -> list[str]:
    """User name (from the home directory) and e-mail (git config) to scan for; never written to the report."""
    ids = [Path.home().name]
    for k in ("user.email", "user.name"):
        try:
            v = git("config", k).strip()
        except subprocess.CalledProcessError:
            v = ""
        if v:
            ids += [v, v.split("@")[0]]
    return sorted({i for i in ids if len(i) >= 4}, key=len, reverse=True)


def path_forms(p: Path) -> list[str]:
    s = str(p)
    fwd = s.replace("\\", "/")
    forms = {s, fwd, s.replace("\\", "\\\\"), "/" + fwd[0].lower() + fwd[2:] if fwd[1:2] == ":" else fwd}
    return sorted(forms, key=len, reverse=True)


def notes() -> list[str]:
    out = set()
    for f in git("ls-files").split("\n"):
        if f.endswith(".csv") and "label" in f:
            for r in csv.DictReader(io.StringIO((REPO / f).read_text(encoding="utf-8"))):
                for c in NOTE_COLS:
                    t = " ".join(str(r.get(c) or "").split())
                    if len(t) >= NOTE_MIN:
                        out.add(t)
    return sorted(out)


def strip_notes_csv(src: Path, dst: Path) -> list[str]:
    rows = list(csv.DictReader(io.StringIO(src.read_text(encoding="utf-8"))))
    fields = list(rows[0].keys()) if rows else next(csv.reader(io.StringIO(src.read_text(encoding="utf-8"))))
    removed = [c for c in fields if c in NOTE_COLS]
    keep = [c for c in fields if c not in NOTE_COLS]
    dst.parent.mkdir(parents=True, exist_ok=True)
    with dst.open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=keep, extrasaction="ignore")
        w.writeheader()
        w.writerows(rows)
    return removed


def copy(src: Path, rel: str) -> None:
    dst = OUT / rel
    dst.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(src, dst)


def clean() -> None:
    OUT.mkdir(exist_ok=True)
    for p in OUT.iterdir():
        if p.name in KEEP:
            continue
        shutil.rmtree(p) if p.is_dir() else p.unlink()


def is_text(p: Path) -> bool:
    return p.suffix.lower() in TEXT_EXT or p.name.startswith(".")


def main() -> None:
    if git("status", "--porcelain", "--untracked-files=no").strip():
        raise SystemExit("refusing: uncommitted changes to tracked files (the snapshot is built from HEAD)")
    head = git("rev-parse", "--short", "HEAD").strip()
    clean()
    log = {"head": head, "label_files_stripped": {}, "excluded_note_files": [], "excluded_other": []}
    tracked = [f for f in git("ls-files").split("\n") if f and (f.startswith(TRACKED_PREFIXES) or f in TRACKED_FILES)]
    for f in tracked:
        src = REPO / f
        if "/labeling_keys/" in f or f.startswith("results/stage2/labeling_key") or f.startswith(
                "results/stage2/labeling_supp_key"):
            continue                                   # keys are checked for notes below, copied if clean
        if f.endswith(".csv") and "label" in f:
            removed = strip_notes_csv(src, OUT / f)
            log["label_files_stripped"][f] = removed
            continue
        copy(src, f)
    keys = [f for f in tracked if "/labeling_keys/" in f or f.startswith(("results/stage2/labeling_key",
                                                                           "results/stage2/labeling_supp_key"))]
    for f in keys:
        copy(REPO / f, f)                              # removed again below if it contains note text
    # per-episode results
    subprocess.run([sys.executable, str(REPO / "scripts/export_per_episode.py"), str(OUT / "results_per_episode")]
                   + ([str(D_RUNS)] if (D_RUNS / "study1r_addon_D").is_dir() else []),
                   cwd=REPO, check=True, capture_output=True)
    # judge outputs
    for d in sorted((REPO / "runs/judge").iterdir()):
        if d.is_dir():
            for n in JUDGE_FILES:
                if (d / n).is_file():
                    copy(d / n, f"judge_outputs/{d.name}/{n}")
    # sample transcripts: replicate index 0 of every arm-run of the first campaign log of each study
    samples = []
    for study in TRANSCRIPT_STUDIES:
        camp = sorted((REPO / "runs" / study / "_campaigns").glob("*/campaign.json"))[0]
        for name, info in json.loads(camp.read_text(encoding="utf-8"))["arms"].items():
            reps = sorted(p for p in Path(info["run_dir"]).glob("*_r000") if p.is_dir())
            if not reps or json.loads((reps[0] / "status.json").read_text(encoding="utf-8"))["status"] != "completed":
                continue
            rep = reps[0]
            if study == "stage2" and name != "mini-low_offer":
                continue                               # Study 1: one example episode
            samples.append(f"{study}/{rep.name}")
            for p in rep.rglob("*"):
                if p.is_file() and p.name != "calls.jsonl":
                    copy(p, f"sample_transcripts/{study}/{rep.name}/{p.relative_to(rep).as_posix()}")
    log["sample_transcripts"] = samples
    for rel, why in MANUAL_EXCLUDE.items():
        if (OUT / rel).is_file():
            (OUT / rel).unlink()
            log["excluded_note_files"].append({"file": rel, "note_matches": f"manual: {why}"})
    # labeler-note check: any release file containing the text of a labeler note is removed
    note_text = notes()
    for p in sorted(OUT.rglob("*")):
        if not p.is_file() or not is_text(p):
            continue
        t = " ".join(p.read_text(encoding="utf-8", errors="replace").split())
        hits = sum(n in t for n in note_text)
        if hits:
            log["excluded_note_files"].append({"file": p.relative_to(OUT).as_posix(), "note_matches": hits})
            p.unlink()
    # secrets, paths, identity: scan and redact
    ids, roots = local_identity(), path_forms(REPO)
    home_forms = path_forms(Path.home())
    generic_path = re.compile(r"(?i)(?<![A-Za-z])[A-Z]:(?:\\\\|\\|/)(?:Users|Projects)[^\s\"'`<>|,;)]*")
    scan = {"keys": {}, "paths_redacted": {}, "identity_remaining": [], "paths_remaining": []}
    for p in sorted(OUT.rglob("*")):
        if not p.is_file() or not is_text(p):
            continue
        rel = p.relative_to(OUT).as_posix()
        text = p.read_bytes().decode("utf-8", errors="surrogateescape")   # bytes kept as they are (line endings)
        for k, rx in KEY_PATTERNS.items():
            if rx.search(text):
                scan["keys"].setdefault(k, []).append(rel)
        new = text
        for r in roots:
            new = new.replace(r, "<repo>")
        for h in home_forms:
            new = new.replace(h, "<local>")
        new = generic_path.sub("<local>", new)
        if new != text:
            scan["paths_redacted"][rel] = sum(text.count(r) for r in roots + home_forms) or 1
            p.write_bytes(new.encode("utf-8", errors="surrogateescape"))
        low = new.lower()
        if any(i.lower() in low for i in ids):
            scan["identity_remaining"].append(rel)
        if generic_path.search(new) or re.search(r"(?i)/c/U[s]ers/|\\\\U[s]ers\\\\|\\U[s]ers\\", new):  # [s]: no self-match
            scan["paths_remaining"].append(rel)
    files = sorted(p for p in OUT.rglob("*") if p.is_file() and p.name not in {"RELEASE_SCAN.md", "RELEASE_MANIFEST.md"})
    frozen_changed = []
    for lock in ("prereg/FROZEN.json", "prereg_study1r/FROZEN.json", "prereg_study1r/FROZEN_1RC.json",
                 "prereg_study1r/FROZEN_1RD.json", "prereg_study1r/FROZEN_1RD_B2.json"):
        d = json.loads((REPO / lock).read_text(encoding="utf-8"))
        hashes = d.get("files_sha256") or {}
        for rel, h in (hashes.items() if isinstance(hashes, dict) else []):
            q = OUT / rel
            if q.is_file() and isinstance(h, str) and hashlib.sha256(q.read_bytes()).hexdigest() != h \
                    and hashlib.sha256((REPO / rel).read_bytes()).hexdigest() == h:
                frozen_changed.append(f"{lock}: {rel}")
    write_reports(log, scan, files, frozen_changed)
    print(json.dumps({"head": head, "files": len(files), "stripped": len(log["label_files_stripped"]),
                      "excluded_note_files": log["excluded_note_files"], "keys": scan["keys"],
                      "paths_redacted_files": len(scan["paths_redacted"]), "identity_remaining": scan["identity_remaining"],
                      "paths_remaining": scan["paths_remaining"], "frozen_changed": frozen_changed,
                      "samples": len(samples)}, indent=1))


def write_reports(log: dict, scan: dict, files: list[Path], frozen_changed: list[str]) -> None:
    size = sum(p.stat().st_size for p in files)
    L = ["# Release scan report", "", f"Built by `scripts/build_release.py` from commit `{log['head']}`. Facts only. "
         "Matched secrets, paths and names are never printed here; only file names and counts.", "",
         f"Files: {len(files)} ({size / 1e6:.1f} MB).", "",
         "## Human label files (note columns removed; keystroke labels only)", ""]
    L += [f"- `{f}`: removed {', '.join(c) or 'none (no note column)'}" for f, c in log["label_files_stripped"].items()]
    L += ["", "## Files withheld because they contain labeler note text "
          f"(verbatim match of any note of {NOTE_MIN}+ characters, or listed by hand)", ""]
    L += [f"- `{x['file']}` ({x['note_matches']}{' note matches' if isinstance(x['note_matches'], int) else ''})"
          for x in log["excluded_note_files"]] or ["- none"]
    L += ["", "## API keys and tokens", ""]
    L += [f"- {k}: {', '.join(f'`{f}`' for f in v)}" for k, v in scan["keys"].items()] or ["- none found"]
    L += ["", "## Local absolute paths (redacted)", "",
          f"Redacted in {len(scan['paths_redacted'])} files (repository root -> `<repo>`, other local paths -> "
          "`<local>`).", ""]
    L += [f"- `{f}`" for f in scan["paths_redacted"]]
    L += ["", "## Residual checks after redaction", "",
          f"- Local user name or e-mail still present: {len(scan['identity_remaining'])} files"
          + "".join(f"\n  - `{f}`" for f in scan["identity_remaining"]),
          f"- Absolute local paths still present: {len(scan['paths_remaining'])} files"
          + "".join(f"\n  - `{f}`" for f in scan["paths_remaining"]),
          f"- Frozen files whose release copy no longer matches its lock hash: {len(frozen_changed)}"
          + "".join(f"\n  - {f}" for f in frozen_changed), "",
          "## Sample transcripts", ""]
    L += [f"- `sample_transcripts/{s}`" for s in log["sample_transcripts"]]
    (OUT / "RELEASE_SCAN.md").write_text("\n".join(L) + "\n", encoding="utf-8")
    M = ["# Release manifest", "", f"Commit `{log['head']}`. SHA-256 of every file in this snapshot (README, this "
         "manifest and the scan report excluded).", "", "| File | Bytes | SHA-256 |", "|---|---|---|"]
    M += [f"| `{p.relative_to(OUT).as_posix()}` | {p.stat().st_size} | {hashlib.sha256(p.read_bytes()).hexdigest()} |"
          for p in files if p.name != "README.md"]
    (OUT / "RELEASE_MANIFEST.md").write_text("\n".join(M) + "\n", encoding="utf-8")


if __name__ == "__main__":
    os.chdir(REPO)
    main()
