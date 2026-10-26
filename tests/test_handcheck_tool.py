"""Part 2(c) hand-check terminal tool: saves answers, hides the keyword classification, resumes, back key. No model calls."""
import csv
import importlib.util

from sting.paths import REPO_ROOT

spec = importlib.util.spec_from_file_location("hct", REPO_ROOT / "scripts" / "handcheck_tool.py")
H = importlib.util.module_from_spec(spec)
spec.loader.exec_module(H)


def sheet(tmp_path):
    p = tmp_path / "h.csv"
    p.write_text("id,sentence,price_related,message_related,your_price_related,your_message_related\n"
                 "S01,Seller C asks $98.,True,False,,\nS02,Seller C proposed a deal.,False,True,,\n", encoding="utf-8")
    return p


def test_marks_hide_classification_and_resume(tmp_path):
    p = sheet(tmp_path)
    shown = []
    answers = iter(["y", "n", "q"])
    assert H.run(p, inp=lambda _: next(answers), out=shown.append) == "quit"
    assert not any("True" in s or "False" in s for s in shown)          # classification never printed
    rows = list(csv.DictReader(p.open(encoding="utf-8")))
    assert (rows[0]["your_price_related"], rows[0]["your_message_related"]) == ("True", "False")
    assert rows[1]["your_price_related"] == "" and rows[0]["price_related"] == "True"
    answers = iter(["n", "y"])
    assert H.run(p, inp=lambda _: next(answers), out=lambda *_: None) == "done"   # resumes at S02
    rows = list(csv.DictReader(p.open(encoding="utf-8")))
    assert (rows[1]["your_price_related"], rows[1]["your_message_related"]) == ("False", "True")


def test_back_clears_previous_row(tmp_path):
    p = sheet(tmp_path)
    answers = iter(["y", "y", "b", "n", "n", "q"])
    H.run(p, inp=lambda _: next(answers), out=lambda *_: None)
    rows = list(csv.DictReader(p.open(encoding="utf-8")))
    assert (rows[0]["your_price_related"], rows[0]["your_message_related"]) == ("False", "False")
