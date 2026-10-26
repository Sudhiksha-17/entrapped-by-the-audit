"""Tests for the automatic documentation system (fake client, temporary directories only)."""
import csv
import json
from pathlib import Path

import pytest
import yaml

from sting.docs import record_run
from sting.minimal_runner import run_batch
from sting.model_check import check_models
from sting.paths import REPO_ROOT


def fake_cfg(**overrides):
    cfg = yaml.safe_load((REPO_ROOT / "configs" / "test_fake.yaml").read_text(encoding="utf-8"))
    cfg.update(overrides)
    return cfg


def test_batch_is_documented_automatically(tmp_path):
    summary = run_batch(fake_cfg(), runs_dir=tmp_path, purpose="unit test", command="pytest")
    docs = tmp_path / "_docs"
    run_dir = Path(summary["run_dir"])
    manifest = json.loads((run_dir / "manifest.json").read_text())
    assert manifest["purpose"] == "unit test" and manifest["upstream_commit"]
    assert set(manifest["prompt_templates_sha256"]) >= {"seller_prompt_base.jinja2", "buyer_prompt_base.jinja2"}
    assert any(k.endswith("status.json") for k in manifest["output_files_sha256"])
    assert [r["status"] for r in manifest["replicates"]] == ["completed", "completed"]
    rows = list(csv.DictReader(open(docs / "ledger" / "runs.csv", encoding="utf-8")))
    assert len(rows) == 1 and rows[0]["run_id"] == summary["run_id"] and rows[0]["episodes"] == "2"
    report = (docs / "results" / "runs" / summary["run_id"] / "report.md").read_text()
    assert "competitive equilibrium price" in report and "90.00" in report and "## Per round" in report
    assert summary["run_id"] in (docs / "notes" / "LAB_NOTEBOOK.md").read_text()
    assert summary["run_id"] in (docs / "results" / "INDEX.md").read_text()
    assert "| 1 |" in (docs / "ledger" / "budget.md").read_text()


def test_failed_episodes_are_documented_with_reason(tmp_path):
    cfg = fake_cfg(replicates=1, concurrency=1)
    cfg["sellers"] = [{"provider": "fake", "model": "fake-model", "bad_json_on_round": 1}] + cfg["sellers"][1:]
    run_batch(cfg, runs_dir=tmp_path, purpose="unit test")
    row = list(csv.DictReader(open(tmp_path / "_docs" / "ledger" / "runs.csv", encoding="utf-8")))[0]
    assert row["failed"] == "1" and json.loads(row["failures_by_reason"]) == {"parse_cap": 1}
    assert row["parse_failures"] == "3"


def test_ledger_running_total_and_index_accumulate(tmp_path):
    run_batch(fake_cfg(), runs_dir=tmp_path, purpose="first")
    run_batch(fake_cfg(), runs_dir=tmp_path, purpose="second")
    docs = tmp_path / "_docs"
    assert len(list(csv.DictReader(open(docs / "ledger" / "runs.csv", encoding="utf-8")))) == 2
    assert "Runs: 2." in (docs / "results" / "INDEX.md").read_text()
    assert (docs / "notes" / "LAB_NOTEBOOK.md").read_text().count("\n## ") == 2


def test_model_check_is_documented(tmp_path):
    out = check_models({"max_tokens": 5, "models": [{"provider": "fake", "model": "fake-model"}]},
                       runs_dir=tmp_path, purpose="unit test")
    assert (tmp_path / "_docs" / "results" / "runs" / out["run_id"] / "report.md").is_file()


def test_manifest_is_never_overwritten(tmp_path):
    summary = run_batch(fake_cfg(), runs_dir=tmp_path, purpose="unit test")
    with pytest.raises(FileExistsError):
        record_run(Path(summary["run_dir"]), "again", "pytest", docs_root=tmp_path / "_docs")


def test_purpose_is_required(tmp_path):
    summary = run_batch(fake_cfg(replicates=1), runs_dir=tmp_path, purpose="unit test")
    with pytest.raises(ValueError, match="purpose"):
        record_run(Path(summary["run_dir"]), " ", "pytest", docs_root=tmp_path / "_other")


def test_manifest_copy_is_published_with_report(tmp_path):
    summary = run_batch(fake_cfg(replicates=1), runs_dir=tmp_path, purpose="unit test")
    published = tmp_path / "_docs" / "results" / "runs" / summary["run_id"] / "manifest.json"
    original = Path(summary["run_dir"]) / "manifest.json"
    assert published.read_bytes() == original.read_bytes()
    assert json.loads(published.read_text())["run_type"] == "exploratory"


def test_ledger_refuses_mismatched_header_and_rebuild_fixes_it(tmp_path):
    from sting.docs import LedgerSchemaMismatch, rebuild_ledger
    first = run_batch(fake_cfg(replicates=1), runs_dir=tmp_path, purpose="first")
    ledger = tmp_path / "_docs" / "ledger" / "runs.csv"
    lines = ledger.read_text(encoding="utf-8").splitlines()
    ledger.write_text("run_id,kind,old_header_only\n" + "\n".join(lines[1:]) + "\n", encoding="utf-8")
    with pytest.raises(LedgerSchemaMismatch):
        run_batch(fake_cfg(replicates=1), runs_dir=tmp_path, purpose="second")
    kept = rebuild_ledger(runs_dir=tmp_path, docs_root=tmp_path / "_docs")
    assert kept.is_file() and kept.read_text(encoding="utf-8").startswith("run_id,kind,old_header_only")
    rows = list(csv.DictReader(open(ledger, encoding="utf-8")))
    assert first["run_id"] in [r["run_id"] for r in rows]
    assert all(r["run_type"] == "exploratory" for r in rows)
