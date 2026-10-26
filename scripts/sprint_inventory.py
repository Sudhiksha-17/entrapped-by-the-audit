"""Pre-sprint / sprint inventory (human message 72). Read-only: git history, committed DEVLOG, DECISIONS and run ledger.

Cutoff: the sprint started Friday 2026-10-23 at 00:00 local. Every commit carries the local offset -0400, so the cutoff
is 2026-10-23 00:00 -0400 = 2026-10-23T04:00:00Z. Recorded dates are used as they are: commit author dates (local),
DEVLOG heading timestamps (UTC as written), run ledger started_utc (or the run id's UTC stamp when started_utc is
blank), DECISIONS by the author date of the commit that added the heading (git blame). Nothing is changed.

Prints Markdown tables to stdout (sections A-E); the narrative summary and flags are written by hand around them.

Usage: python scripts/sprint_inventory.py [REF ...]   (default: master and exploratory-q1)
"""
from __future__ import annotations

import csv
import io
import re
import subprocess
import sys
from collections import Counter, defaultdict
from datetime import datetime, timezone

CUTOFF = datetime(2026, 10, 23, 4, 0, tzinfo=timezone.utc)
CODE_EXT = (".py", ".ps1", ".sh", ".patch", ".bat")


def git(*args: str) -> str:
    return subprocess.run(["git", *args], capture_output=True, text=True, encoding="utf-8", check=True).stdout


def cls(dt: datetime) -> str:
    return "SPRINT" if dt >= CUTOFF else "PRE-SPRINT"


def iso(s: str) -> datetime:
    return datetime.fromisoformat(s)


def stamp(s: str) -> datetime:
    return datetime.strptime(s[:16], "%Y%m%dT%H%M%SZ").replace(tzinfo=timezone.utc)


def commits(ref: str) -> list[dict]:
    out = []
    for line in git("log", ref, "--reverse", "--format=%h%x09%aI%x09%cI%x09%s").splitlines():
        h, ad, cd, s = line.split("\t", 3)
        files = [f for f in git("show", "--name-only", "--format=", h).splitlines() if f]
        out.append({"hash": h, "ad": iso(ad), "cd": iso(cd), "subject": s, "files": files})
    return out


def key_artifacts(files: list[str]) -> str:
    skip = ("notes/", "ledger/", "results/INDEX.md", "results/runs/")
    keep = [f for f in files if not f.startswith(skip)]
    runs = sum(f.startswith("results/runs/") for f in files)
    shown = ", ".join(f"`{f}`" for f in keep[:5]) + (f" (+{len(keep) - 5} more)" if len(keep) > 5 else "")
    if runs:
        shown += f"{'; ' if shown else ''}{len({f.split('/')[2] for f in files if f.startswith('results/runs/')})} run report dir(s)"
    return shown or "docs only"


def blame_headings(ref: str, path: str) -> list[tuple[str, str, datetime]]:
    """(heading, commit, author date) for each '## ' heading line."""
    out, info = [], {}
    porcelain = git("blame", "--line-porcelain", ref, "--", path).splitlines()
    i = 0
    while i < len(porcelain):
        h = porcelain[i].split()[0]
        meta = {}
        i += 1
        while not porcelain[i].startswith("\t"):
            k, _, v = porcelain[i].partition(" ")
            meta[k] = v
            i += 1
        line = porcelain[i][1:]
        i += 1
        if "author-time" in meta:
            tz = meta["author-tz"]
            off = (1 if tz[0] == "+" else -1) * (int(tz[1:3]) * 3600 + int(tz[3:]) * 60)
            info[h] = datetime.fromtimestamp(int(meta["author-time"]), timezone.utc).astimezone(
                timezone(__import__("datetime").timedelta(seconds=off)))
        if line.startswith("## "):
            out.append((line[3:].strip(), h[:7], info[h]))
    return out


def main() -> None:
    refs = sys.argv[1:] or ["master", "exploratory-q1"]
    master = refs[0]
    cs = commits(master)
    print("## A. Commits on `master` (author date, local -0400)\n")
    print("| # | Date (local) | Class | Phase | What was done (commit subject) | Key artifacts | Commit |")
    print("|---|---|---|---|---|---|---|")
    for n, c in enumerate(cs, 1):
        phase = c["subject"].split(":")[0] if ":" in c["subject"] else ""
        what = c["subject"].split(":", 1)[-1].strip().replace("|", "/")
        print(f"| {n} | {c['ad']:%Y-%m-%d %H:%M} | {cls(c['ad'])} | {phase} | {what} | {key_artifacts(c['files'])} | `{c['hash']}` |")
    for ref in refs[1:]:
        extra = [c for c in commits(ref) if c["hash"] not in {x["hash"] for x in cs}]
        if extra:
            print(f"\nCommits only on branch `{ref}`:\n")
            for c in extra:
                print(f"- {c['ad']:%Y-%m-%d %H:%M} {cls(c['ad'])} `{c['hash']}` {c['subject']}")
    diff = [c for c in cs if c["ad"] != c["cd"]]
    print(f"\nCommits whose committer date differs from the author date: {len(diff)}"
          + "".join(f"\n- `{c['hash']}` author {c['ad']:%Y-%m-%d %H:%M:%S} committer {c['cd']:%Y-%m-%d %H:%M:%S}" for c in diff))
    print(f"\nTotals: {Counter(cls(c['ad']) for c in cs)}")

    print("\n## B. Runs in `ledger/runs.csv` on `master`\n")
    rows = list(csv.DictReader(io.StringIO(git("show", f"{master}:ledger/runs.csv"))))
    agg = defaultdict(lambda: [0, 0.0, []])
    window = []
    for r in rows:
        t = stamp(r["started_utc"]) if r["started_utc"] else stamp(r["run_id"])
        r["_t"], r["_c"] = t, cls(t)
        a = agg[(t.date().isoformat(), r["_c"], r["stage"], r["kind"], r["run_type"])]
        a[0] += 1
        a[1] += float(r["actual_cost_usd"] or 0)
        a[2].append(r["run_id"])
        if datetime(2026, 10, 23, tzinfo=timezone.utc) <= t < CUTOFF:
            window.append(r)
    print("| Date (UTC) | Class | Stage | Kind | Run type | Runs | Actual cost $ | First and last run id |")
    print("|---|---|---|---|---|---|---|---|")
    for (d, c, st, k, rt), (n, cost, ids) in sorted(agg.items()):
        print(f"| {d} | {c} | {st} | {k} | {rt} | {n} | {cost:.4f} | `{ids[0]}`" + (f" ... `{ids[-1]}`" if n > 1 else "") + " |")
    print(f"\nTotals: {Counter(r['_c'] for r in rows)}; cost by class: "
          + ", ".join(f"{c} ${sum(float(r['actual_cost_usd'] or 0) for r in rows if r['_c'] == c):.2f}"
                      for c in ("PRE-SPRINT", "SPRINT")))
    print(f"\nRuns dated 2026-10-23 UTC but before the local cutoff (00:00-04:00Z): {len(window)}"
          + "".join(f"\n- `{r['run_id']}`" for r in window))

    print("\n## C. DEVLOG entries (`notes/DEVLOG.md` on `master`)\n")
    print("| Heading timestamp | Class by heading | Added in commit | Commit date (local) | Class by commit | Title |")
    print("|---|---|---|---|---|---|")
    mism = []
    for head, h, dt in blame_headings(master, "notes/DEVLOG.md"):
        m = re.match(r"(\d{4}-\d{2}-\d{2})(?:T(\d{2}:\d{2}(?::\d{2})?)Z)?", head)
        if m:
            t = datetime.fromisoformat(m.group(1) + "T" + (m.group(2) or "00:00") + "+00:00")
            hc = cls(t) if m.group(2) else ("SPRINT" if m.group(1) >= "2026-10-23" else "PRE-SPRINT") + " (date only)"
        else:
            hc = "no timestamp"
        title = head.split("|", 1)[-1].strip().replace("|", "/") if "|" in head else head
        if not hc.startswith(cls(dt)):
            mism.append((head, h))
        print(f"| {m.group(0) if m else '-'} | {hc} | `{h}` | {dt:%Y-%m-%d %H:%M} | {cls(dt)} | {title} |")
    print(f"\nEntries whose heading class differs from the class of the commit that added them: {len(mism)}"
          + "".join(f"\n- `{h}` {head}" for head, h in mism))

    print("\n## D. Decisions (`notes/DECISIONS.md` on `master`; date = commit that added the heading)\n")
    print("| Decision heading | Added in commit | Date (local) | Class |")
    print("|---|---|---|---|")
    for head, h, dt in blame_headings(master, "notes/DECISIONS.md"):
        print(f"| {head.replace('|', '/')} | `{h}` | {dt:%Y-%m-%d %H:%M} | {cls(dt)} |")
    for ref in refs[1:]:
        base = {x for x, _, _ in blame_headings(master, "notes/DECISIONS.md")}
        extra = [(x, h, dt) for x, h, dt in blame_headings(ref, "notes/DECISIONS.md") if x not in base]
        for x, h, dt in extra:
            print(f"| {x.replace('|', '/')} (branch `{ref}`) | `{h}` | {dt:%Y-%m-%d %H:%M} | {cls(dt)} |")

    print("\n## E. Code files (first and last commit at this path)\n")
    print("| File | First commit | First date (local) | Status | Last commit | Last date | Commits | Sprint commits |")
    print("|---|---|---|---|---|---|---|---|")
    files = {}
    for ref in refs:
        for f in git("ls-tree", "-r", "--name-only", ref).splitlines():
            if f.endswith(CODE_EXT) and (f.startswith(("sting/", "scripts/", "tests/", "patches/")) or "/" not in f):
                files.setdefault(f, ref)
    for f in sorted(files):
        log = [l.split("\t") for l in git("log", files[f], "--format=%h%x09%aI", "--", f).splitlines()]
        first, last = log[-1], log[0]
        fd, ld = iso(first[1]), iso(last[1])
        n_sprint = sum(iso(d) >= CUTOFF for _, d in log)
        status = "PREEXISTING" if fd < CUTOFF else "SPRINT"
        where = "" if files[f] == master else f" (branch `{files[f]}` only)"
        print(f"| `{f}`{where} | `{first[0]}` | {fd:%Y-%m-%d %H:%M} | {status} | `{last[0]}` | {ld:%Y-%m-%d %H:%M} | "
              f"{len(log)} | {n_sprint} |")


if __name__ == "__main__":
    main()
