"""Tests for sting.env (no real keys; temporary files only)."""
import os

from sting.env import load_env


def test_dotenv_key_overrides_environment_and_reports_source(tmp_path, monkeypatch):
    monkeypatch.setenv("OPENROUTER_API_KEY", "old-value")
    env_file = tmp_path / ".env"
    env_file.write_text("OPENROUTER_API_KEY=new-value\n", encoding="utf-8")
    info = load_env([env_file])
    assert os.environ["OPENROUTER_API_KEY"] == "new-value"
    assert info["key_sources"]["OPENROUTER_API_KEY"] == ".env"
    assert info["overridden_environment_keys"] == ["OPENROUTER_API_KEY"]
    assert "new-value" not in repr(info) and "old-value" not in repr(info)


def test_environment_key_used_when_dotenv_lacks_it(tmp_path, monkeypatch):
    monkeypatch.setenv("OPENAI_API_KEY", "env-only")
    env_file = tmp_path / ".env"
    env_file.write_text("OPENROUTER_API_KEY=x\n", encoding="utf-8")
    info = load_env([env_file])
    assert os.environ["OPENAI_API_KEY"] == "env-only"
    assert info["key_sources"]["OPENAI_API_KEY"] == "environment"


def test_empty_dotenv_value_does_not_clear_environment(tmp_path, monkeypatch):
    monkeypatch.setenv("OPENROUTER_API_KEY", "keep")
    env_file = tmp_path / ".env"
    env_file.write_text("OPENROUTER_API_KEY=\n", encoding="utf-8")
    load_env([env_file])
    assert os.environ["OPENROUTER_API_KEY"] == "keep"
