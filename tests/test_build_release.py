"""Release builder helpers (scripts/build_release.py): note columns removed, path forms. Synthetic files only."""
import csv
import importlib.util
from pathlib import Path

from sting.paths import REPO_ROOT

spec = importlib.util.spec_from_file_location("brel", REPO_ROOT / "scripts" / "build_release.py")
B = importlib.util.module_from_spec(spec)
spec.loader.exec_module(B)


def test_strip_notes_keeps_only_ids_and_labels(tmp_path):
    src = tmp_path / "labels.csv"
    src.write_text("item_id,response_A,note_A,note_B,response,reason,unresolved\n"
                   "i1,accept,\"private, text\",x,accept,agreed,False\n", encoding="utf-8")
    removed = B.strip_notes_csv(src, tmp_path / "out" / "labels.csv")
    assert removed == ["note_A", "note_B", "reason", "unresolved"]     # human message 103
    rows = list(csv.DictReader((tmp_path / "out" / "labels.csv").open(encoding="utf-8")))
    assert rows == [{"item_id": "i1", "response_A": "accept", "response": "accept"}]


def test_path_forms_cover_windows_posix_and_json_escapes():
    forms = B.path_forms(Path(r"E:\work\X Y\repo"))   # not a Users or Projects path, so the release keeps it
    assert r"E:\work\X Y\repo" in forms and "E:/work/X Y/repo" in forms
    assert r"E:\\work\\X Y\\repo" in forms and "/e/work/X Y/repo" in forms
