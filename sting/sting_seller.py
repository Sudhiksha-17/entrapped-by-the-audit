"""Scripted sting seller (Phase 4; Stage 2 message conditions per prereg/stage2_message_and_judge.md).

Implements the upstream seller interface (``Agent.generate_bid_response(**kwargs) -> dict``,
``cda_types.py:53-86``; the market reads ``ask`` and ``message_to_sellers``, ``market.py:141-156``).
Upstream is not modified.

Pricing rules (selectable in config; the human chooses before Stage 1):
- ``follow``: ask = mean of the LLM sellers' asks in the previous round (round 1 uses
  ``initial_ask``). The median of two values is their mean. If an LLM seller has no ask
  recorded in the previous round (it withdrew or did not resubmit, ISSUES I-028), its most
  recent recorded ask is used; if it has never asked, it is left out; if no LLM seller has
  ever asked, ``initial_ask`` is used. (Missing-ask handling: DECISIONS D-047, proposal.)
- ``fixed``: ask = ``fixed_ask`` every round.
Asks are rounded to whole cents, as the prompt requires of LLM sellers.

Conditions: ``silent`` (never sends a message) or one of ``sham``, ``anchor``, ``rapport``, ``offer``:
the sting posts exactly one message, ``message_text``, in round ``t0`` (the spec fixes t0 = 10; LLM
sellers see it in round 11) and nothing in any other round. Message texts are not written here; the
runner passes the human-written stimulus selected by replicate index (configs/stage2_stimuli.yaml).
Messages delivered to the sting (upstream passes the previous round's broadcast dict to every seller,
``market.py:116``) are recorded in ``received_messages`` and never answered.

Study 1R (prereg_study1r/STUDY1R_SPEC.md version 2, sections 5-6; STUDY1R_STIMULI.md), opt-in through ``x_rule``,
``talk`` and ``post_until``, so Study 1 behavior is unchanged when they are unset:
- ``x_rule``: per-episode proportional X. At round ``x_rule["round"]`` (10) the sting computes pre = mean posted
  ask of the LLM sellers over ``x_rule["pre_rounds"]`` (6-9; same function as the outcome measure,
  sting.stage2_measures.window_mean; if none, the most recent posted LLM-seller asks; if none at all, NoPreError) and
  X = pre + fraction x (target - pre), rounded half up to cents. X is logged in every arm; in anchor and offer arms it
  is the price floor from that round (ask = max(X, follow)). In silent and sham arms it is never shown or used.
- ``talk`` + ``post_until`` (talking sting): in every round t0 .. post_until (10-29, visible 11-30) the sting posts
  arm sentence + segment for Seller A + segment for Seller B; each segment is ASK or ACK by the deterministic
  follow-up rule on that seller's previous-round public message (sting.study1r_stimuli.segment_state); round t0: both
  ASK. States and trigger texts are logged per round in ``followup_log``.

The sting reads the market history through ``history``, a zero-argument callable returning the
list of completed rounds' ``seller_asks`` dicts (the runner passes ``lambda: [r.seller_asks for r in
market.rounds]``). The ask is a pure function of that history and the config, so identical
history gives identical asks.
"""
from __future__ import annotations

from typing import Any, Callable, Literal, Optional

from pydantic import ConfigDict, Field

from decimal import ROUND_HALF_UP, Decimal

from sting.paths import ensure_upstream_on_path
from sting.stage2_measures import window_mean

ensure_upstream_on_path()
from src.continuous_double_auction.cda_types import Agent, AgentBidResponse  # noqa: E402

PricingRule = Literal["follow", "fixed"]
Condition = Literal["silent", "sham", "anchor", "rapport", "directive", "offer"]
MESSAGE_CONDITIONS = ("sham", "anchor", "rapport", "directive", "offer")
# Arms in which the sting asks max(X, follow) from t0 (prereg/stage2_spec.md section 4).
FLOOR_CONDITIONS = ("anchor", "directive", "offer")


def follow_ask(history: list[dict[str, Any]], llm_seller_ids: list[str], initial_ask: float) -> float:
    """Mean of the LLM sellers' previous-round asks, carrying forward each seller's last recorded ask."""
    if not history:
        return round(float(initial_ask), 2)
    last: dict[str, float] = {}
    for asks in history:
        for sid in llm_seller_ids:
            value = asks.get(sid)
            if isinstance(value, (int, float)) and not isinstance(value, bool):
                last[sid] = float(value)
    if not last:
        return round(float(initial_ask), 2)
    return round(sum(last.values()) / len(last), 2)


class NoPreError(RuntimeError):
    """Study 1R: no LLM-seller ask was ever posted before the X round; the episode fails with reason "no_pre"."""


def proportional_x(pre: float, fraction: float, target: float) -> float:
    """X = pre + fraction x (target - pre), rounded half up to whole cents."""
    return float(Decimal(repr(pre + fraction * (target - pre))).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP))


def history_pre(history: list[dict[str, Any]], llm_seller_ids: list[str], pre_rounds: tuple[int, int]
                ) -> Optional[float]:
    """Mean posted LLM-seller ask over rounds pre_rounds[0]..pre_rounds[1]; history[i] is round i + 1."""
    rounds = [{"round_number": i + 1, "seller_asks": asks} for i, asks in enumerate(history)]
    return window_mean(rounds, llm_seller_ids, range(pre_rounds[0], pre_rounds[1] + 1))


def competitive_ask(history: list[dict[str, Any]], llm_seller_ids: list[str], floor: float, step: float,
                    initial_ask: float) -> float:
    """Study 1R-A (human message 52): max(floor, min(previous-round asks of the LLM sellers) - step), rounded to cents.
    A seller without an ask in the previous round contributes its last recorded ask (as in the follow rule); with no
    LLM-seller ask ever recorded, initial_ask is used in place of the minimum."""
    last: dict[str, float] = {}
    for asks in history:
        for sid in llm_seller_ids:
            v = asks.get(sid)
            if isinstance(v, (int, float)) and not isinstance(v, bool):
                last[sid] = float(v)
    low = min(last.values()) if last else float(initial_ask)
    return round(max(float(floor), low - float(step)), 2)


def compute_ask(rule: PricingRule, history: list[dict[str, Any]], llm_seller_ids: list[str],
                initial_ask: Optional[float], fixed_ask: Optional[float]) -> float:
    if rule == "fixed":
        if fixed_ask is None:
            raise ValueError("pricing rule 'fixed' needs fixed_ask")
        return round(float(fixed_ask), 2)
    if rule == "follow":
        if initial_ask is None:
            raise ValueError("pricing rule 'follow' needs initial_ask")
        return follow_ask(history, llm_seller_ids, initial_ask)
    raise ValueError(f"unknown pricing rule {rule!r}")


class StingSeller(Agent):
    model_config = ConfigDict(arbitrary_types_allowed=True)

    pricing_rule: PricingRule
    llm_seller_ids: list[str]
    initial_ask: Optional[float] = None
    fixed_ask: Optional[float] = None
    condition: Condition = "silent"
    t0: Optional[int] = None
    message_text: Optional[str] = None
    message_id: Optional[str] = None
    sent_messages: list[dict[str, Any]] = Field(default_factory=list)
    price_floor: Optional[float] = None       # X in anchor/directive/offer arms
    floor_from_round: Optional[int] = None    # t0
    history: Optional[Callable[[], list[dict[str, Any]]]] = None
    post_until: Optional[int] = None          # Study 1R: post every round t0 .. post_until
    x_rule: Optional[dict[str, Any]] = None   # Study 1R: proportional X (round, pre_rounds, fraction, target)
    talk: Optional[dict[str, Any]] = None     # Study 1R: sentence_id, sentence, ASK, ACK templates (study1r_stimuli)
    competitive: Optional[dict[str, Any]] = None  # Study 1R-A: from_round, floor, step (silent condition only)
    x_log: dict[str, Any] = Field(default_factory=dict)
    followup_log: list[dict[str, Any]] = Field(default_factory=list)
    received_messages: list[dict[str, Any]] = Field(default_factory=list)
    ask_log: list[dict[str, Any]] = Field(default_factory=list)

    def model_post_init(self, __context: Any) -> None:
        if self.condition == "silent":
            if self.message_text is not None or self.talk is not None:
                raise ValueError("silent condition takes no message")
        elif self.t0 is None or not (self.message_text or self.talk):
            raise ValueError(f"condition {self.condition!r} needs t0 and a message")
        if self.talk is not None:
            from sting.study1r_stimuli import MESSAGE_CONDITIONS, check_templates
            if self.condition not in MESSAGE_CONDITIONS or self.x_rule is None or self.post_until is None:
                raise ValueError("the talking sting needs a sham/anchor/offer condition, x_rule and post_until")
            if self.message_text is not None:
                raise ValueError("the talking sting composes its messages; message_text must be unset")
            check_templates(self.talk, self.condition)
            if self.t0 != int(self.x_rule["round"]) or self.post_until < self.t0:
                raise ValueError("x_rule round must equal t0, and post_until >= t0")
        elif self.post_until is not None:
            raise ValueError("post_until needs the talking sting (talk)")

    def set_x(self, history: list[dict[str, Any]]) -> None:
        """Compute and log X (once, at x_rule round); set the message and, in floor arms, the price floor."""
        r = self.x_rule
        pre = history_pre(history, self.llm_seller_ids, tuple(r["pre_rounds"]))
        source = "pre_rounds"
        if pre is None:  # human message 36: most recent posted LLM-seller asks before the X round, else fail
            if not any(isinstance(a.get(s), (int, float)) and not isinstance(a.get(s), bool)
                       for a in history for s in self.llm_seller_ids):
                raise NoPreError(f"no LLM-seller ask posted before round {r['round']}")
            pre, source = follow_ask(history, self.llm_seller_ids, 0.0), "most_recent_asks"
        uncapped = proportional_x(pre, float(r["fraction"]), float(r["target"]))
        cap = r.get("cap")  # human message 40: X = min(pre + 0.5 x (100 - pre), 99.99); never fail for X
        x = min(uncapped, float(cap)) if cap is not None else uncapped
        self.x_log = {"pre": pre, "x": x, "uncapped_x": uncapped, "capped": x != uncapped, "cap": cap,
                      "source": source, "round": int(r["round"]), "fraction": float(r["fraction"]),
                      "target": float(r["target"]), "x_below_target": x < float(r["target"])}
        if self.condition in FLOOR_CONDITIONS:
            self.price_floor, self.floor_from_round = x, int(r["round"])

    @property
    def mode(self) -> str:
        return "silent" if self.condition == "silent" else "message"

    def message_at(self, round_num: int, seller_messages: Optional[dict[str, str]] = None) -> Optional[str]:
        """Study 1: the scripted message in round t0 only. Study 1R: the composed talking-sting message in every
        round t0 .. post_until, with the follow-up state per seller logged. None otherwise and always if silent."""
        if self.condition == "silent" or self.t0 is None:
            return None
        if self.talk is None:
            return self.message_text if round_num == self.t0 else None
        if not self.t0 <= round_num <= self.post_until:
            return None
        from sting.study1r_stimuli import compose, segment_state
        x = self.x_log["x"]
        states, triggers = {}, {}
        for seller in self.llm_seller_ids:
            if round_num == self.t0:
                states[seller], triggers[seller] = "ASK", None
            else:
                states[seller], triggers[seller] = segment_state((seller_messages or {}).get(seller), x)
        message = compose(self.talk, x, states, self.llm_seller_ids)
        self.followup_log.append({"round": round_num, "states": states, "triggers": triggers})
        return message

    def generate_bid_response(self, **kwargs: Any) -> AgentBidResponse:
        round_num = int(kwargs.get("round_num", 1))
        for sender, text in sorted((kwargs.get("seller_messages") or {}).items()):
            if sender != self.id:
                self.received_messages.append({"round": round_num, "from": sender, "text": text})
        history = self.history() if self.history is not None else []
        if self.x_rule is not None and not self.x_log and round_num >= int(self.x_rule["round"]):
            self.set_x(history)
        rule_ask = compute_ask(self.pricing_rule, history, self.llm_seller_ids, self.initial_ask, self.fixed_ask)
        if self.competitive is not None and round_num >= int(self.competitive["from_round"]):
            rule_ask = competitive_ask(history, self.llm_seller_ids, self.competitive["floor"], self.competitive["step"],
                                       self.initial_ask)
        floored = (self.price_floor is not None and self.floor_from_round is not None
                   and round_num >= self.floor_from_round)
        ask = round(max(float(self.price_floor), rule_ask), 2) if floored else rule_ask
        rule_name = ("competitive" if self.competitive is not None and round_num >= int(self.competitive["from_round"])
                     else self.pricing_rule)
        self.ask_log.append({"round": round_num, "ask": ask, "rule": rule_name, "rule_ask": rule_ask,
                             "floor_applied": floored, "history_rounds": len(history)})
        response: AgentBidResponse = {"ask": ask}
        message = self.message_at(round_num, kwargs.get("seller_messages"))
        if message is not None:
            response["message_to_sellers"] = message
            self.sent_messages.append({"round": round_num, "message_id": self.message_id, "text": message})
        return response
