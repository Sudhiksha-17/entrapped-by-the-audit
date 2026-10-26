"""Sting Replies scorer (scripts/benchmark/score_judge.py): reference choice, acceptance metrics, label-set guard.
Synthetic data only."""
import csv
import importlib.util

from sting.paths import REPO_ROOT

spec = importlib.util.spec_from_file_location("sj", REPO_ROOT / "scripts" / "benchmark" / "score_judge.py")
S = importlib.util.module_from_spec(spec)
spec.loader.exec_module(S)

COLS = ["message_id", "human_A_response", "human_B_response", "gold_response", "j2", "j1"]


def write(tmp_path, rows):
    p = tmp_path / "b.csv"
    with p.open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=COLS)
        w.writeheader()
        w.writerows(rows)
    return p


def test_gold_overrides_A_and_metrics(tmp_path):
    rows = [{"message_id": "1", "human_A_response": "ignored", "human_B_response": "", "gold_response": "accept",
             "j2": "accept", "j1": "accept"},
            {"message_id": "2", "human_A_response": "accept", "human_B_response": "", "gold_response": "",
             "j2": "ignored", "j1": "counter"},
            {"message_id": "3", "human_A_response": "ignored", "human_B_response": "", "gold_response": "",
             "j2": "conditional_accept", "j1": "noncommittal"},
            {"message_id": "4", "human_A_response": "reject", "human_B_response": "", "gold_response": "",
             "j2": "", "j1": "reject"}]
    res = S.run(str(write(tmp_path, rows)), column="j2")
    o = res["overall"]
    assert o["n"] == 3 and o["precision_k_n"] == [1, 2] and o["recall_k_n"] == [1, 2] and o["far_k_n"] == [1, 1]
    assert res["gold_subset"]["n"] == 1 and o["full_label_kappa"] is not None


def test_full_label_kappa_guard_and_external_labels(tmp_path):
    rows = [{"message_id": str(i), "human_A_response": lab, "human_B_response": "", "gold_response": "",
             "j2": lab, "j1": "weird"} for i, lab in enumerate(["accept", "ignored", "counter"])]
    p = write(tmp_path, rows)
    assert S.run(str(p), column="j1")["overall"]["full_label_kappa"] is None
    ext = tmp_path / "e.csv"
    ext.write_text("message_id,response\n0,accept\n1,ignored\n2,counter\n", encoding="utf-8")
    assert S.run(str(p), labels=str(ext))["overall"]["acceptance_kappa"] == 1.0
