"""Import closure of repository code (human message 65): every module under `sting/` and `scripts/` that a set of
entry files imports, directly or indirectly. Imports are read statically (ast), including imports inside functions
and modules loaded by file path with importlib (`spec_from_file_location(..., <dir> / "<name>.py")` patterns are
matched by their literal file name). Third-party and standard-library modules are ignored; upstream code in
`third_party/` is pinned by its commit, not hashed here.
"""
from __future__ import annotations

import ast
import re
from pathlib import Path

from sting.paths import REPO_ROOT

_FILE_LOAD = re.compile(r'"([A-Za-z0-9_]+\.py)"')


def _local_imports(path: Path, root: Path) -> set[str]:
    tree = ast.parse(path.read_text(encoding="utf-8"))
    names: set[str] = set()
    for node in ast.walk(tree):
        if isinstance(node, ast.ImportFrom) and node.module and node.level == 0:
            names.add(node.module)
            names.update(f"{node.module}.{a.name}" for a in node.names)
        elif isinstance(node, ast.Import):
            names.update(a.name for a in node.names)
    out: set[str] = set()
    for n in names:
        parts = n.split(".")
        if parts[0] == "sting" and len(parts) >= 2:
            f = root / "sting" / f"{parts[1]}.py"
            if f.is_file():
                out.add(f"sting/{parts[1]}.py")
        elif len(parts) == 1 and (root / "scripts" / f"{n}.py").is_file() and path.parent.name == "scripts":
            out.add(f"scripts/{n}.py")
    if path.parent.name == "scripts":
        for m in _FILE_LOAD.findall(path.read_text(encoding="utf-8")):
            if (root / "scripts" / m).is_file():
                out.add(f"scripts/{m}")
    return out


def closure(entries: list[str], root: Path = REPO_ROOT) -> list[str]:
    seen: set[str] = set()
    todo = list(entries)
    while todo:
        f = todo.pop()
        if f in seen:
            continue
        seen.add(f)
        todo += sorted(_local_imports(root / f, root) - seen)
    return sorted(seen)
