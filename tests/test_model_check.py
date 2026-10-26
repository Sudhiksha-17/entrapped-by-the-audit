"""Tests for sting.model_check (no network)."""
from sting.model_check import check_models


def test_models_without_keys_are_skipped_without_calls(tmp_path):
    out = check_models({"max_tokens": 5, "models": [{"provider": "openrouter", "model": "x/y"},
                                                    {"provider": "openai", "model": "gpt-4o-mini"}]},
                       runs_dir=tmp_path)
    assert [r["status"] for r in out["results"]] == ["skipped", "skipped"]


def test_fake_model_is_called_once(tmp_path):
    out = check_models({"max_tokens": 5, "models": [{"provider": "fake", "model": "fake-model"}]}, runs_dir=tmp_path)
    row = out["results"][0]
    assert row["status"] == "available" and row["returned_model"] == "fake-model"
