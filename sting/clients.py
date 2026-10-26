"""Model clients used by our runner.

Every LLM call in our runs goes through ``TrackedClient``. It subclasses the
upstream ``ModelWrapper`` so upstream ``LMSeller`` and ``LMBuyer`` accept it, and:

- routes to OpenAI, Anthropic or OpenRouter (OpenAI-compatible endpoint), so we
  are not bound by upstream's 9-string model whitelist (DECISIONS D-014);
- records tokens in and out (and OpenRouter's reported cost) for every call
  (DECISIONS D-013, ISSUES I-009);
- retries transient API errors with exponential backoff and raises
  ``ModelCallFailed`` instead of returning ``None`` when it gives up, so a failed
  episode fails loudly (DECISIONS D-016, ISSUES I-003);
- enforces a per-episode cap on API attempts, which stops upstream's unlimited
  retry on JSON decode errors (``agents.py:155-162,237-245``) from running away.

``FakeClient`` is a deterministic stand-in with the same interface. All tests use
it; it never touches the network.

Request parameters match upstream ``get_client`` + ``ModelWrapper`` (``misc.py:10-26``,
``model_wrappers.py``) except: SDK-internal retries are disabled (``max_retries=0``)
so every attempt is counted here, and OpenRouter calls send ``max_tokens`` and ask
for usage accounting.
"""
from __future__ import annotations

import json
import os
import random
import re
import threading
import time
from dataclasses import asdict, dataclass
from typing import Any, Callable, Optional

from sting.paths import ensure_upstream_on_path

ensure_upstream_on_path()
from src.resources.model_wrappers import ModelWrapper  # noqa: E402

OPENROUTER_BASE_URL = "https://openrouter.ai/api/v1"
PROVIDER_KEY_ENV = {
    "openai": "OPENAI_API_KEY",
    "anthropic": "ANTHROPIC_API_KEY",
    "openrouter": "OPENROUTER_API_KEY",
}


class ModelCallFailed(RuntimeError):
    """A model call failed after all retry attempts, or with a non-transient error."""


class CallBudgetExceeded(RuntimeError):
    """The episode reached its cap on API attempts."""


class MissingAPIKey(RuntimeError):
    """The provider's API key is not set. The message never contains key values."""


class ParseCapExceeded(RuntimeError):
    """The episode reached its cap on responses that upstream cannot parse as JSON."""


class ProviderMismatch(ModelCallFailed):
    """OpenRouter served the call from a provider other than the pinned one."""


@dataclass
class CallRecord:
    timestamp: float
    agent_id: str
    role: str
    provider: str
    requested_model: str
    returned_model: Optional[str]
    tokens_in: int
    tokens_out: int
    cost_usd_reported: Optional[float]
    latency_s: float
    attempts: int
    error: Optional[str] = None
    routed_provider: Optional[str] = None   # OpenRouter: backend that served the call
    pinned_provider: Optional[str] = None   # OpenRouter: slug we required
    parse_failed: bool = False              # response not parseable by upstream extract_json
    provider_unknown: bool = False          # OpenRouter response had no provider field (H-5)
    raw_text_if_parse_failed: Optional[str] = None  # full reply text, kept only when unparseable (D-054)
    system_fingerprint: Optional[str] = None        # as returned by the API, if any
    temperature: Optional[float] = None             # request settings, recorded per call (stage2_spec section 2)
    top_p: Optional[float] = None
    max_tokens: Optional[int] = None


class UsageTracker:
    """Thread-safe store of call records for one episode, with attempt and parse-failure caps."""

    def __init__(self, max_attempts_total: Optional[int] = None, max_parse_failures: Optional[int] = None):
        self._lock = threading.Lock()
        self.records: list[CallRecord] = []
        self.max_attempts_total = max_attempts_total
        self.max_parse_failures = max_parse_failures
        self.attempts_started = 0
        self.parse_failures = 0

    def reserve_attempt(self) -> None:
        with self._lock:
            if self.max_attempts_total is not None and self.attempts_started >= self.max_attempts_total:
                raise CallBudgetExceeded(
                    f"episode reached its cap of {self.max_attempts_total} API attempts"
                )
            self.attempts_started += 1

    def add(self, record: CallRecord) -> None:
        with self._lock:
            self.records.append(record)

    def check_parse(self, text: str, record: CallRecord) -> None:
        """Mark the record if upstream's ``extract_json`` would fail on ``text``; enforce the parse cap.

        The text is still returned to upstream unchanged, so upstream's own handling
        (retry on JSONDecodeError, crash on a reply with no '{') is preserved until
        the cap is reached. Reaching the cap raises ``ParseCapExceeded``, which
        upstream's backoff does not catch, so the episode ends as failed.
        """
        if _upstream_parses(text):
            return
        record.parse_failed = True
        record.raw_text_if_parse_failed = text
        with self._lock:
            self.parse_failures += 1
            reached = self.max_parse_failures is not None and self.parse_failures >= self.max_parse_failures
        if reached:
            raise ParseCapExceeded(f"episode reached its cap of {self.max_parse_failures} unparseable "
                                   f"responses (latest from {record.agent_id})")

    def totals_by(self, field: str = "role") -> dict[str, dict[str, Any]]:
        with self._lock:
            records = list(self.records)
        out: dict[str, dict[str, Any]] = {}
        for rec in records:
            group = out.setdefault(getattr(rec, field), {
                "calls": 0, "failed_calls": 0, "parse_failures": 0, "provider_unknown": 0, "tokens_in": 0,
                "tokens_out": 0,
                "cost_usd_reported": 0.0, "cost_reported_for_all_calls": True,
            })
            group["calls"] += 1
            if rec.error:
                group["failed_calls"] += 1
            if rec.parse_failed:
                group["parse_failures"] += 1
            if rec.provider_unknown:
                group["provider_unknown"] += 1
            group["tokens_in"] += rec.tokens_in
            group["tokens_out"] += rec.tokens_out
            if rec.cost_usd_reported is None:
                group["cost_reported_for_all_calls"] = False
            else:
                group["cost_usd_reported"] += rec.cost_usd_reported
        return out

    def as_dicts(self) -> list[dict[str, Any]]:
        with self._lock:
            return [asdict(r) for r in self.records]


@dataclass
class RetryPolicy:
    max_attempts: int = 5
    base_delay_s: float = 1.0
    max_delay_s: float = 30.0

    def delay(self, attempt: int) -> float:
        """Exponential backoff with full jitter, for the wait after failed attempt number ``attempt`` (1-based)."""
        return random.uniform(0, min(self.max_delay_s, self.base_delay_s * (2 ** (attempt - 1))))


def _upstream_parses(text: str) -> bool:
    """True if upstream ``extract_json`` (util/json_util.py:3-10) would parse ``text``."""
    from src.continuous_double_auction.util.json_util import extract_json
    import contextlib
    import io
    try:
        with contextlib.redirect_stdout(io.StringIO()):  # extract_json prints the response on failure
            extract_json(text)
        return True
    except (ValueError, json.JSONDecodeError):
        return False


def _normalize_provider(name: Optional[str]) -> str:
    return re.sub(r"[^a-z0-9]", "", (name or "").lower())


def _transient_errors() -> tuple[type[BaseException], ...]:
    import anthropic
    import openai
    return (
        openai.RateLimitError, openai.APIConnectionError, openai.APITimeoutError, openai.InternalServerError,
        anthropic.RateLimitError, anthropic.APIConnectionError, anthropic.APITimeoutError,
        anthropic.InternalServerError, EmptyResponse,
    )


class EmptyResponse(RuntimeError):
    """The provider returned no text. Treated as transient."""


class TrackedClient(ModelWrapper):
    def __init__(
        self,
        provider: str,
        model_name: str,
        tracker: UsageTracker,
        agent_id: str,
        role: str,
        temperature: float = 0.7,
        max_tokens: int = 4000,
        top_p: Optional[float] = 1.0,
        json_mode: Optional[bool] = None,
        retry: Optional[RetryPolicy] = None,
        sleep: Callable[[float], None] = time.sleep,
        openrouter_provider: Optional[str] = None,
        require_parameters: bool = True,
        validate_json: bool = False,
    ):
        if provider not in PROVIDER_KEY_ENV:
            raise ValueError(f"unknown provider {provider!r}; expected one of {sorted(PROVIDER_KEY_ENV)}")
        if provider == "openrouter" and not openrouter_provider:
            raise ValueError("OpenRouter models must pin a backend with 'openrouter_provider' (no fallbacks)")
        super().__init__(model_name, temperature=temperature, max_tokens=max_tokens, top_p=top_p)
        self.provider = provider
        self.tracker = tracker
        self.agent_id = agent_id
        self.role = role
        # Upstream uses JSON mode for OpenAI models only (misc.py:13).
        self.json_mode = (provider == "openai") if json_mode is None else json_mode
        self.retry = retry or RetryPolicy()
        self._sleep = sleep
        self._sdk_client = None
        self.openrouter_provider = openrouter_provider
        self.require_parameters = require_parameters
        self.validate_json = validate_json
        self.last_response_meta: Optional[dict[str, Any]] = None

    # Upstream's abstract interface -------------------------------------------------
    def generate(self, messages):
        last_error: Optional[BaseException] = None
        transient = _transient_errors()
        for attempt in range(1, self.retry.max_attempts + 1):
            self.tracker.reserve_attempt()
            start = time.time()
            try:
                text, returned_model, tokens_in, tokens_out, cost, routed = self._call(messages)
            except transient as exc:
                last_error = exc
                self._record(start, None, 0, 0, None, attempt, f"{type(exc).__name__}: {exc}")
                if attempt < self.retry.max_attempts:
                    self._sleep(self.retry.delay(attempt))
                continue
            except Exception as exc:
                self._record(start, None, 0, 0, None, attempt, f"{type(exc).__name__}: {exc}")
                raise ModelCallFailed(f"{self.agent_id}: non-transient error from {self.provider}/{self.model_name}: "
                                      f"{type(exc).__name__}: {exc}") from exc
            record = self._record(start, returned_model, tokens_in, tokens_out, cost, attempt, None, routed)
            if self.provider == "openrouter":
                if routed is None:
                    # H-5 (human message 11): no provider field -> flag, do not fail; fallbacks are disabled
                    # in every request, so the pinned backend is the only one OpenRouter may use.
                    record.provider_unknown = True
                elif _normalize_provider(routed) != _normalize_provider(self.openrouter_provider.split("/")[0]):
                    # Compare the base provider only: a pin such as "novita/bf16" or "deepinfra/turbo" is served by
                    # a provider whose response name has no variant suffix.
                    record.error = f"ProviderMismatch: routed to {routed!r}, pinned {self.openrouter_provider!r}"
                    raise ProviderMismatch(f"{self.agent_id}: {self.model_name} was served by {routed!r}, "
                                           f"not the pinned provider {self.openrouter_provider!r}")
            if self.validate_json:
                self.tracker.check_parse(text, record)
            return text
        raise ModelCallFailed(f"{self.agent_id}: {self.provider}/{self.model_name} failed after "
                              f"{self.retry.max_attempts} attempts; last error "
                              f"{type(last_error).__name__}: {last_error}") from last_error

    def batch_generate(self, messages_list):
        return [self.generate(m) for m in messages_list]

    # Internals -------------------------------------------------------------------
    def _record(self, start, returned_model, tokens_in, tokens_out, cost, attempt, error, routed=None):
        record = CallRecord(
            timestamp=start, agent_id=self.agent_id, role=self.role, provider=self.provider,
            requested_model=self.model_name, returned_model=returned_model,
            tokens_in=tokens_in, tokens_out=tokens_out, cost_usd_reported=cost,
            latency_s=round(time.time() - start, 3), attempts=attempt, error=error,
            routed_provider=routed, pinned_provider=self.openrouter_provider,
            system_fingerprint=getattr(self, "_last_fingerprint", None),
            temperature=self.temperature, top_p=self.top_p, max_tokens=self.max_tokens,
        )
        self._last_fingerprint = None
        self.tracker.add(record)
        return record

    def _api_key(self) -> str:
        """The key always comes from the .env file (parent folder): load_env() runs here, so no caller can forget it,
        and a key that would come only from the process (Windows) environment is refused (I-049, human message 51)."""
        from sting.env import load_env
        env = PROVIDER_KEY_ENV[self.provider]
        info = load_env()
        if info["key_sources"].get(env) != ".env":
            raise MissingAPIKey(f"{env} is not set in the .env file (source: {info['key_sources'].get(env)}); "
                                "refusing to fall back to the process environment")
        key = os.environ.get(env, "").strip()
        if not key:
            raise MissingAPIKey(f"{env} is not set")
        return key

    def sdk_client(self):
        if self._sdk_client is None:
            if self.provider == "anthropic":
                import anthropic
                self._sdk_client = anthropic.Anthropic(api_key=self._api_key(), timeout=60, max_retries=0)
            else:
                import openai
                base_url = OPENROUTER_BASE_URL if self.provider == "openrouter" else None
                self._sdk_client = openai.OpenAI(api_key=self._api_key(), base_url=base_url, timeout=60, max_retries=0)
        return self._sdk_client

    def _call(self, messages):
        if self.provider == "anthropic":
            return self._call_anthropic(messages)
        return self._call_openai_compatible(messages)

    def _call_openai_compatible(self, messages):
        kwargs: dict[str, Any] = {"model": self.model_name, "messages": messages, "temperature": self.temperature}
        if self.top_p is not None:
            kwargs["top_p"] = self.top_p
        if self.provider == "openai":
            kwargs["max_completion_tokens"] = self.max_tokens
        else:
            kwargs["max_tokens"] = self.max_tokens
            # Pin one backend, no fallbacks (OpenRouter provider routing: order/only/allow_fallbacks),
            # and only route to backends that support every parameter we send.
            kwargs["extra_body"] = {
                "usage": {"include": True},
                "provider": {"order": [self.openrouter_provider], "only": [self.openrouter_provider],
                             "allow_fallbacks": False, "require_parameters": self.require_parameters},
            }
        if self.json_mode:
            kwargs["response_format"] = {"type": "json_object"}
        resp = self.sdk_client().chat.completions.create(**kwargs)
        if not resp.choices or resp.choices[0].message.content is None:
            raise EmptyResponse(f"no content in response (model={getattr(resp, 'model', None)})")
        usage = resp.usage
        tokens_in = getattr(usage, "prompt_tokens", 0) or 0
        tokens_out = getattr(usage, "completion_tokens", 0) or 0
        cost = None
        if usage is not None and usage.model_extra:
            cost = usage.model_extra.get("cost")
        extra = getattr(resp, "model_extra", None) or {}
        routed = extra.get("provider", getattr(resp, "provider", None))
        self._last_fingerprint = getattr(resp, "system_fingerprint", None) or extra.get("system_fingerprint")
        # Response metadata field names (no content), kept so the model check can show where routing info lives.
        self.last_response_meta = {"extra_fields": sorted(extra), "provider_field": routed}
        return resp.choices[0].message.content, resp.model, tokens_in, tokens_out, cost, routed

    def _call_anthropic(self, messages):
        # Same system-message handling as upstream AnthropicClient (model_wrappers.py:155-161).
        if messages[0]["role"] == "system":
            system, messages = messages[0]["content"], messages[1:]
        else:
            system = "You are a helpful assistant."
        kwargs: dict[str, Any] = {"model": self.model_name, "system": system, "messages": messages,
                                  "max_tokens": self.max_tokens, "temperature": self.temperature}
        if self.top_p is not None:
            kwargs["top_p"] = self.top_p
        resp = self.sdk_client().messages.create(**kwargs)
        if not resp.content or not getattr(resp.content[0], "text", None):
            raise EmptyResponse(f"no content in response (model={resp.model})")
        return resp.content[0].text, resp.model, resp.usage.input_tokens, resp.usage.output_tokens, None, None


class FakeClient(ModelWrapper):
    """Deterministic offline client for tests. Never touches the network.

    Sellers ask 95 minus the hour and, if the prompt offers a message field, send
    ``"fake message from <id> hour <n>"``. Buyers bid 85 plus the hour. Token counts
    are character counts divided by 4. ``fail_on_round`` makes every call in that
    round raise ``ModelCallFailed``, for testing failure handling. ``bad_json_on_round``
    returns unparseable text in that round, for testing the parse cap.
    """

    def __init__(self, model_name: str, tracker: UsageTracker, agent_id: str, role: str,
                 temperature: float = 0.7, max_tokens: int = 4000, fail_on_round: Optional[int] = None,
                 bad_json_on_round: Optional[int] = None, validate_json: bool = False, **_ignored):
        super().__init__(model_name, temperature=temperature, max_tokens=max_tokens)
        self.provider = "fake"
        self.tracker = tracker
        self.agent_id = agent_id
        self.role = role
        self.fail_on_round = fail_on_round
        self.bad_json_on_round = bad_json_on_round
        self.validate_json = validate_json

    def generate(self, messages):
        self.tracker.reserve_attempt()
        start = time.time()
        prompt = messages[-1]["content"]
        match = re.search(r"This is Hour #(\d+)", prompt)
        hour = int(match.group(1)) if match else 0
        if self.fail_on_round is not None and hour == self.fail_on_round:
            self.tracker.add(CallRecord(start, self.agent_id, self.role, "fake", self.model_name, None,
                                        0, 0, None, 0.0, 1, "FakeFailure: scripted failure"))
            raise ModelCallFailed(f"{self.agent_id}: scripted fake failure at hour {hour}")
        if "was not a genuine trader" in prompt:                        # Study 1R probe Q2 (plain text)
            text = "NO. Nothing suggested a test."
            record = CallRecord(start, self.agent_id, self.role, "fake", self.model_name, self.model_name,
                                len(prompt) // 4, len(text) // 4, None, 0.0, 1, None)
            self.tracker.add(record)
            return text
        if "Looking back over the session" in prompt:                    # Study 1R probe Q1 (plain text)
            text = "Nothing unusual."
            record = CallRecord(start, self.agent_id, self.role, "fake", self.model_name, self.model_name,
                                len(prompt) // 4, len(text) // 4, None, 0.0, 1, None)
            self.tracker.add(record)
            return text
        if "as a seller" in prompt:
            body: dict[str, Any] = {"reflection": "r", "plan_for_this_hour": "p", "ask": round(95.0 - hour, 2),
                                    "new_memory": f"hour {hour}", "scratch_pad_update": "s"}
            if '"message_to_sellers"' in prompt:
                body["plan_for_message"] = "m"
                body["message_to_sellers"] = f"fake message from {self.agent_id} hour {hour}"
        elif "as a buyer" in prompt:
            body = {"reflection": "r", "plan_for_this_hour": "p", "bid": round(85.0 + hour, 2),
                    "new_memory": f"hour {hour}", "scratch_pad_update": "s"}
        elif "You are an expert analyst reviewing one seller's reasoning" in prompt:
            proposal = "Proposal" in prompt or "Suggestion" in prompt or "An idea for every seller" in prompt
            body = {"engaged_with_message": "yes", "response": "accept" if proposal else "not_applicable",
                    "awareness": "none", "legal_or_ethical_concern": "no", "own_coordination_intent": "none",
                    "evidence": [], "notes": ""}
        elif "You are an expert analyst reviewing one seller's text" in prompt:  # Study 1R judge v2
            body = {"engaged_with_message": "no", "response": "ignored", "awareness": "none", "evidence": [], "notes": ""}
        else:
            body = {"reply": "OK"}
        text = json.dumps(body)
        if self.bad_json_on_round is not None and hour == self.bad_json_on_round:
            text = '{"ask": 90.0, "unterminated'
        record = CallRecord(start, self.agent_id, self.role, "fake", self.model_name, self.model_name,
                            len(prompt) // 4, len(text) // 4, None, 0.0, 1, None)
        self.tracker.add(record)
        if self.validate_json:
            self.tracker.check_parse(text, record)
        return text

    def batch_generate(self, messages_list):
        return [self.generate(m) for m in messages_list]


def make_client(spec: dict[str, Any], tracker: UsageTracker, agent_id: str, role: str,
                temperature: float, max_tokens: int, retry: Optional[RetryPolicy] = None,
                validate_json: bool = False) -> ModelWrapper:
    """Build a client from a config model spec.

    Spec keys: provider, model, json_mode?, top_p?, openrouter_provider (required for
    openrouter), require_parameters? (default true); fake only: fail_on_round?, bad_json_on_round?.
    """
    provider = spec["provider"]
    if provider == "fake":
        return FakeClient(spec["model"], tracker, agent_id, role, temperature=temperature,
                          max_tokens=max_tokens, fail_on_round=spec.get("fail_on_round"),
                          bad_json_on_round=spec.get("bad_json_on_round"), validate_json=validate_json)
    return TrackedClient(provider, spec["model"], tracker, agent_id, role, temperature=temperature,
                         max_tokens=max_tokens, top_p=spec.get("top_p", 1.0), json_mode=spec.get("json_mode"),
                         retry=retry, openrouter_provider=spec.get("openrouter_provider"),
                         require_parameters=spec.get("require_parameters", True), validate_json=validate_json)
