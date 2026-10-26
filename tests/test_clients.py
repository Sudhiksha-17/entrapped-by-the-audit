"""Tests for sting.clients. SDK calls are replaced by stubs; no network."""
from types import SimpleNamespace

import openai
import pytest

from sting.clients import (OPENROUTER_BASE_URL, CallBudgetExceeded, FakeClient, MissingAPIKey, ModelCallFailed,
                           ParseCapExceeded, ProviderMismatch, RetryPolicy, TrackedClient, UsageTracker)


def openai_style_response(text="hi", model="returned-model", prompt_tokens=11, completion_tokens=3, cost=None,
                          provider="OpenAI"):
    usage = openai.types.CompletionUsage(prompt_tokens=prompt_tokens, completion_tokens=completion_tokens,
                                         total_tokens=prompt_tokens + completion_tokens,
                                         **({"cost": cost} if cost is not None else {}))
    return SimpleNamespace(model=model, usage=usage, model_extra={"provider": provider} if provider else {},
                           choices=[SimpleNamespace(message=SimpleNamespace(content=text))])


class StubCompletions:
    def __init__(self, outcomes):
        self.outcomes = list(outcomes)
        self.calls = []

    def create(self, **kwargs):
        self.calls.append(kwargs)
        outcome = self.outcomes.pop(0)
        if isinstance(outcome, BaseException):
            raise outcome
        return outcome


def tracked(provider, outcomes, tracker=None, retry=None, monkeypatch=None, validate_json=False):
    env = {"openai": "OPENAI_API_KEY", "openrouter": "OPENROUTER_API_KEY"}[provider]
    monkeypatch.setenv(env, "test-key-not-real")
    client = TrackedClient(provider, "some/model", tracker or UsageTracker(), "Seller A", "seller",
                           retry=retry or RetryPolicy(max_attempts=3), sleep=lambda s: None,
                           openrouter_provider="openai" if provider == "openrouter" else None,
                           validate_json=validate_json)
    stub = StubCompletions(outcomes)
    client._sdk_client = SimpleNamespace(chat=SimpleNamespace(completions=stub))
    return client, stub


def rate_limit_error():
    request = SimpleNamespace(method="POST", url="https://example.invalid")
    response = SimpleNamespace(status_code=429, headers={}, request=request)
    return openai.RateLimitError("rate limited", response=response, body=None)


def test_openrouter_client_uses_openrouter_endpoint_and_env_key(monkeypatch, tmp_path):
    import sting.env as env   # keys come only from a .env file (D-101)
    (tmp_path / ".env").write_text("OPENROUTER_API_KEY=test-key-not-real\n", encoding="utf-8")
    monkeypatch.setattr(env, "ENV_SEARCH_PATHS", [tmp_path / ".env"])
    monkeypatch.setenv("OPENROUTER_API_KEY", "test-key-not-real")
    client = TrackedClient("openrouter", "openai/gpt-4o-mini", UsageTracker(), "Seller A", "seller",
                           openrouter_provider="openai")
    sdk = client.sdk_client()
    assert str(sdk.base_url).rstrip("/") == OPENROUTER_BASE_URL
    assert sdk.max_retries == 0


def test_missing_key_raises_without_value(monkeypatch):
    client = TrackedClient("openrouter", "x/y", UsageTracker(), "Seller A", "seller", openrouter_provider="openai")
    with pytest.raises(MissingAPIKey, match="OPENROUTER_API_KEY is not set"):
        client.sdk_client()


def test_openrouter_records_tokens_cost_and_returned_model(monkeypatch):
    tracker = UsageTracker()
    client, stub = tracked("openrouter", [openai_style_response(cost=0.00042)], tracker, monkeypatch=monkeypatch)
    assert client.generate([{"role": "user", "content": "x"}]) == "hi"
    rec = tracker.records[0]
    assert (rec.tokens_in, rec.tokens_out, rec.cost_usd_reported) == (11, 3, 0.00042)
    assert rec.returned_model == "returned-model" and rec.provider == "openrouter" and rec.role == "seller"
    sent = stub.calls[0]
    assert sent["max_tokens"] == 4000 and "max_completion_tokens" not in sent
    assert sent["extra_body"]["usage"] == {"include": True}
    assert "response_format" not in sent  # JSON mode is OpenAI-only by default, as upstream


def test_openai_matches_upstream_request_parameters(monkeypatch):
    client, stub = tracked("openai", [openai_style_response()], monkeypatch=monkeypatch)
    client.generate([{"role": "user", "content": "x"}])
    sent = stub.calls[0]
    assert sent["max_completion_tokens"] == 4000
    assert sent["response_format"] == {"type": "json_object"}
    assert sent["temperature"] == 0.7 and sent["top_p"] == 1.0


def test_transient_error_is_retried_then_succeeds(monkeypatch):
    tracker = UsageTracker()
    client, _ = tracked("openai", [rate_limit_error(), openai_style_response()], tracker, monkeypatch=monkeypatch)
    assert client.generate([{"role": "user", "content": "x"}]) == "hi"
    assert tracker.attempts_started == 2
    assert [r.error is None for r in tracker.records] == [False, True]


def test_gives_up_with_model_call_failed_not_none(monkeypatch):
    client, _ = tracked("openai", [rate_limit_error()] * 3, monkeypatch=monkeypatch)
    with pytest.raises(ModelCallFailed, match="failed after 3 attempts"):
        client.generate([{"role": "user", "content": "x"}])


def test_non_transient_error_is_not_retried(monkeypatch):
    tracker = UsageTracker()
    client, _ = tracked("openai", [ValueError("bad request")], tracker, monkeypatch=monkeypatch)
    with pytest.raises(ModelCallFailed, match="non-transient"):
        client.generate([{"role": "user", "content": "x"}])
    assert tracker.attempts_started == 1


def test_attempt_cap_stops_calls(monkeypatch):
    tracker = UsageTracker(max_attempts_total=1)
    client, _ = tracked("openai", [openai_style_response(), openai_style_response()], tracker,
                        monkeypatch=monkeypatch)
    client.generate([{"role": "user", "content": "x"}])
    with pytest.raises(CallBudgetExceeded):
        client.generate([{"role": "user", "content": "x"}])


def test_fake_client_is_deterministic_and_records_usage():
    tracker = UsageTracker()
    fake = FakeClient("fake-model", tracker, "Seller A", "seller")
    prompt = [{"role": "user", "content": 'as a seller ... "message_to_sellers" ... This is Hour #3 out of 15 hours.'}]
    assert fake.generate(prompt) == fake.generate(prompt)
    assert len(tracker.records) == 2 and tracker.records[0].tokens_in > 0


def test_totals_by_role():
    tracker = UsageTracker()
    FakeClient("m", tracker, "Seller A", "seller").generate([{"role": "user", "content": "as a seller Hour #1"}])
    FakeClient("m", tracker, "Buyer A", "buyer").generate([{"role": "user", "content": "as a buyer Hour #1"}])
    totals = tracker.totals_by("role")
    assert set(totals) == {"seller", "buyer"} and totals["seller"]["calls"] == 1


def test_openrouter_requires_a_pinned_provider():
    with pytest.raises(ValueError, match="must pin a backend"):
        TrackedClient("openrouter", "x/y", UsageTracker(), "Seller A", "seller")


def test_openrouter_request_pins_single_provider_without_fallbacks(monkeypatch):
    tracker = UsageTracker()
    client, stub = tracked("openrouter", [openai_style_response(provider="OpenAI")], tracker,
                           monkeypatch=monkeypatch)
    client.generate([{"role": "user", "content": "x"}])
    assert stub.calls[0]["extra_body"]["provider"] == {"order": ["openai"], "only": ["openai"],
                                                       "allow_fallbacks": False, "require_parameters": True}
    rec = tracker.records[0]
    assert (rec.routed_provider, rec.pinned_provider) == ("OpenAI", "openai")


def test_openrouter_provider_mismatch_fails_and_is_logged(monkeypatch):
    tracker = UsageTracker()
    client, _ = tracked("openrouter", [openai_style_response(provider="Azure")], tracker, monkeypatch=monkeypatch)
    with pytest.raises(ProviderMismatch):
        client.generate([{"role": "user", "content": "x"}])
    assert tracker.records[0].routed_provider == "Azure" and "ProviderMismatch" in tracker.records[0].error


def test_missing_routed_provider_is_flagged_not_failed(monkeypatch):
    tracker = UsageTracker()
    client, stub = tracked("openrouter", [openai_style_response(provider=None)], tracker, monkeypatch=monkeypatch)
    assert client.generate([{"role": "user", "content": "x"}]) == "hi"
    rec = tracker.records[0]
    assert rec.provider_unknown and rec.error is None and rec.routed_provider is None
    assert stub.calls[0]["extra_body"]["provider"]["allow_fallbacks"] is False
    assert tracker.totals_by("role")["seller"]["provider_unknown"] == 1


def test_unparseable_responses_are_counted_and_cap_raises(monkeypatch):
    tracker = UsageTracker(max_parse_failures=2)
    client, _ = tracked("openai", [openai_style_response(text="no json here"), openai_style_response(text="{bad")],
                        tracker, monkeypatch=monkeypatch, validate_json=True)
    assert client.generate([{"role": "user", "content": "x"}]) == "no json here"  # returned unchanged to upstream
    with pytest.raises(ParseCapExceeded):
        client.generate([{"role": "user", "content": "x"}])
    assert tracker.parse_failures == 2 and all(r.parse_failed for r in tracker.records)
    assert tracker.totals_by("role")["seller"]["parse_failures"] == 2


def test_pinned_variant_slug_matches_base_provider_name(monkeypatch):
    monkeypatch.setenv("OPENROUTER_API_KEY", "test-key-not-real")
    tracker = UsageTracker()
    client = TrackedClient("openrouter", "meta-llama/llama-3.3-70b-instruct", tracker, "Seller A", "seller",
                           openrouter_provider="novita/bf16", retry=RetryPolicy(max_attempts=1), sleep=lambda s: None)
    stub = StubCompletions([openai_style_response(provider="Novita"), openai_style_response(provider="DeepInfra")])
    client._sdk_client = SimpleNamespace(chat=SimpleNamespace(completions=stub))
    assert client.generate([{"role": "user", "content": "x"}]) == "hi"
    assert stub.calls[0]["extra_body"]["provider"]["order"] == ["novita/bf16"]
    with pytest.raises(ProviderMismatch):
        client.generate([{"role": "user", "content": "x"}])


def test_raw_text_is_kept_only_for_unparseable_replies(monkeypatch):
    tracker = UsageTracker(max_parse_failures=5)
    bad = "```json\n{bad"
    client, _ = tracked("openai", [openai_style_response(text=bad), openai_style_response(text='{"ask": 90}')],
                        tracker, monkeypatch=monkeypatch, validate_json=True)
    client.generate([{"role": "user", "content": "x"}])
    client.generate([{"role": "user", "content": "x"}])
    assert tracker.records[0].raw_text_if_parse_failed == bad
    assert tracker.records[1].raw_text_if_parse_failed is None
