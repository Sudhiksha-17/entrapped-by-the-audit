"""Minimal episode runner (DECISIONS D-011). Extended into ``runner.py`` in Phase 3.

Replaces upstream ``run_simulation`` (``simulation.py:19-116``) so that:
- every agent uses our client (``sting.clients``), so any model string works;
- all output goes under ``runs/<stage>/<run_id>/<replicate_id>/``, never into third_party/;
- run and replicate ids are unique; existing directories are never reused;
- the upstream LLM judge and the W&B upload are never called (D-012, D-005);
- market draws (initial order book, company names) depend only on the replicate
  index, and agent names are fixed and neutral, so replicate k is identical
  across arms (D-018);
- a failing episode is marked ``failed`` with its error, its partial log is kept,
  and the batch continues (D-016).

Usage:
    python -m sting.minimal_runner configs/smoke.yaml --purpose "..." [--approve-cost] [--estimate-only]
        [--replicate-indices 0 | 1,2]

``--replicate-indices`` selects which replicate indices to run (default: 0..replicates-1),
so a batch can start with a 1-episode pilot (index 0) and continue with the rest under
a new run_id while keeping market draws matched by index (CLAUDE.md credit rule 3, D-018).
"""
from __future__ import annotations

import argparse
import contextlib
import json
import os
import platform
import random
import string
import sys
import time
import traceback
import uuid
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Optional

import numpy as np
import yaml

from sting.clients import (CallBudgetExceeded, ModelCallFailed, ParseCapExceeded, ProviderMismatch, RetryPolicy,
                           UsageTracker, make_client)
from sting import docs as docs_module
from sting.docs import docs_root_for, record_run
from sting.env import load_env
from sting.prompt_mirror import VOLUME_TEMPLATE, ensure_mirror
from sting.sting_seller import FLOOR_CONDITIONS, NoPreError, StingSeller
from sting.paths import REPO_ROOT, RUNS_DIR, UPSTREAM_ROOT, ensure_upstream_on_path, upstream_commit

ensure_upstream_on_path()
from src.continuous_double_auction.cda_types import ExperimentParams  # noqa: E402
from src.continuous_double_auction.identities import BUYER_COMPANY_NAMES, SELLER_COMPANY_NAMES  # noqa: E402
from src.continuous_double_auction.market.agents import LMBuyer, LMSeller  # noqa: E402
from src.continuous_double_auction.market.market import Market  # noqa: E402
from src.continuous_double_auction.util.logging_util import ExperimentLogger  # noqa: E402

COST_APPROVAL_THRESHOLD_USD = 2.0  # CLAUDE.md credit rule 2
RUN_TYPES = ("exploratory", "pilot", "confirmatory")


def utc_stamp() -> str:
    return datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")


@contextlib.contextmanager
def upstream_cwd(root: Optional[Path] = None):
    """Upstream loads prompt templates relative to the cwd (agents.py:166,255), so run from its root, or from
    the prompt mirror (byte-identical upstream templates plus the volume template, sting/prompt_mirror.py)."""
    previous = os.getcwd()
    os.chdir(root or UPSTREAM_ROOT)
    try:
        yield
    finally:
        os.chdir(previous)


def agent_names(n: int, kind: str) -> list[str]:
    """Fixed neutral names: 'Seller A', 'Seller B', ... Identical in every replicate and arm."""
    return [f"{kind} {letter}" for letter in string.ascii_uppercase[:n]]


def market_draws(cfg: dict[str, Any], replicate_index: int) -> dict[str, Any]:
    """Initial order book and company names, determined only by the replicate index.

    Ranges match upstream defaults (cda_types.py:33-36, misc.py:29-49).
    """
    n_sellers, n_buyers = len(cfg["seller_valuations"]), len(cfg["buyer_valuations"])
    init = cfg.get("initial_book", {})
    ask_c, ask_s = init.get("seller_ask_center", 97.5), init.get("seller_ask_spread", 2.5)
    bid_c, bid_s = init.get("buyer_bid_center", 82.5), init.get("buyer_bid_spread", 2.5)
    rng = np.random.default_rng([20261016, replicate_index])
    asks = [round(float(x), 2) for x in rng.uniform(ask_c - ask_s / 2, ask_c + ask_s / 2, n_sellers)]
    bids = [round(float(x), 2) for x in rng.uniform(bid_c - bid_s / 2, bid_c + bid_s / 2, n_buyers)]
    names_rng = random.Random(f"companies-{replicate_index}")
    return {
        "initial_asks": asks,
        "initial_bids": bids,
        "seller_companies": names_rng.sample(SELLER_COMPANY_NAMES, n_sellers),
        "buyer_companies": names_rng.sample(BUYER_COMPANY_NAMES, n_buyers),
    }


def build_params(cfg: dict[str, Any]) -> ExperimentParams:
    """ExperimentParams without upstream's model whitelist check (model_construct skips validation).

    Model strings stored here are for the record only; our clients do the routing.
    """
    init = cfg.get("initial_book", {})
    return ExperimentParams.model_construct(
        seller_valuations=list(map(float, cfg["seller_valuations"])),
        buyer_valuations=list(map(float, cfg["buyer_valuations"])),
        seller_models=[s["model"] for s in cfg["sellers"]] + (["scripted-sting"] if cfg.get("sting") else []),
        buyer_models=[b["model"] for b in cfg["buyers"]],
        rounds=int(cfg["rounds"]),
        seller_comms_enabled=bool(cfg.get("seller_comms_enabled", False)),
        buyer_comms_enabled=False,
        hide_num_rounds=False,
        oversight_enabled=False,
        boss_pressure=seller_prompt(cfg) == "ceo",
        seller_prompt_template=VOLUME_TEMPLATE if seller_prompt(cfg) == "volume" else "seller_prompt_base.jinja2",
        temperature=float(cfg["temperature"]),
        tag=cfg.get("run_name", ""),
        initial_seller_ask_center=init.get("seller_ask_center", 97.5),
        initial_seller_ask_spread=init.get("seller_ask_spread", 2.5),
        initial_buyer_bid_center=init.get("buyer_bid_center", 82.5),
        initial_buyer_bid_spread=init.get("buyer_bid_spread", 2.5),
        initial_condition=True,
        max_message_length=int(cfg.get("max_message_length", 500)),
    )


def check_run_type(cfg: dict[str, Any]) -> None:
    """Confirmatory runs refuse to launch with any uncommitted change (human message 10).

    Exploratory and pilot runs may launch with uncommitted changes; the manifest records
    them and saves the code diff.
    """
    if cfg["run_type"] == "confirmatory":
        changes = docs_module.uncommitted_changes()
        if changes:
            raise SystemExit("Confirmatory run refused: the repository has uncommitted changes:\n  "
                             + "\n  ".join(changes))


def validate_config(cfg: dict[str, Any]) -> None:
    if cfg.get("run_type") not in RUN_TYPES:
        raise ValueError(f"config must set run_type to one of {RUN_TYPES}")
    budget = cfg.get("budget")
    if cfg["run_type"] == "confirmatory" and not budget:
        raise ValueError("confirmatory runs need budget: {group, cap_usd} (human message 17)")
    if budget and (not budget.get("group") or float(budget.get("cap_usd", 0)) <= 0):
        raise ValueError("budget needs a group name and a positive cap_usd")
    n_sting = 1 if cfg.get("sting") else 0
    if len(cfg["sellers"]) + n_sting != len(cfg["seller_valuations"]):
        raise ValueError("seller_valuations must have one entry per LLM seller plus one for the sting, if any")
    if cfg.get("sting"):
        st = cfg["sting"]
        condition = sting_condition(st)
        if condition not in ("silent", "sham", "anchor", "rapport", "directive", "offer"):
            raise ValueError(f"unknown sting condition {condition!r}")
        if condition != "silent" and not st.get("stimuli_file"):
            raise ValueError("message conditions need sting.stimuli_file")
        if st.get("pricing_rule") not in ("follow", "fixed"):
            raise ValueError("sting.pricing_rule must be 'follow' or 'fixed'")
        if st["pricing_rule"] == "follow" and st.get("initial_ask") is None:
            raise ValueError("sting pricing_rule 'follow' needs initial_ask")
        if st["pricing_rule"] == "fixed" and st.get("fixed_ask") is None:
            raise ValueError("sting pricing_rule 'fixed' needs fixed_ask")
        if st.get("x_rule") is not None:
            validate_x_rule(st, cfg)
        elif st.get("post_until") is not None:
            raise ValueError("sting.post_until is only supported with sting.x_rule (Study 1R)")
    if len(cfg["buyers"]) != len(cfg["buyer_valuations"]):
        raise ValueError("buyers and buyer_valuations must have the same length")
    if cfg.get("max_message_length", 500) <= 0:
        raise ValueError("max_message_length must be positive")


STUDY1R_CONDITIONS = ("silent", "sham", "anchor", "offer")


def validate_x_rule(st: dict[str, Any], cfg: dict[str, Any]) -> None:
    """Study 1R sting settings (prereg_study1r/STUDY1R_SPEC.md version 2, sections 3, 5-6; STUDY1R_STIMULI.md)."""
    from sting.study1r_stimuli import check_templates, load, longest_message, talk_for
    xr, rounds = st["x_rule"], int(cfg["rounds"])
    missing = {"round", "pre_rounds", "fraction", "target"} - set(xr)
    if missing:
        raise ValueError(f"sting.x_rule needs {sorted(missing)}")
    condition = sting_condition(st)
    if condition not in STUDY1R_CONDITIONS:
        raise ValueError(f"x_rule supports conditions {STUDY1R_CONDITIONS}, not {condition!r}")
    lo, hi = xr["pre_rounds"]
    if not 1 <= lo <= hi < int(xr["round"]):
        raise ValueError("x_rule pre_rounds must lie before x_rule round")
    if not 0 < float(xr["fraction"]) < 1:
        raise ValueError("x_rule fraction must be between 0 and 1")
    if xr.get("cap") is None or not float(xr["cap"]) < float(xr["target"]):
        raise ValueError("x_rule needs cap below target (human message 40: 99.99)")
    comp = st.get("competitive")
    if comp is not None:
        if condition != "silent":
            raise ValueError("sting.competitive (Study 1R-A) requires the silent condition (no posts)")
        if {"from_round", "floor", "step"} - set(comp):
            raise ValueError("sting.competitive needs from_round, floor and step")
    if condition != "silent":
        t0, until = int(st.get("t0", xr["round"])), st.get("post_until")
        if t0 != int(xr["round"]):
            raise ValueError("sting.t0 must equal x_rule round")
        if until is None or not t0 <= int(until) < rounds:
            raise ValueError("Study 1R message arms need post_until with t0 <= post_until < rounds")
        stim = load(st["stimuli_file"])
        if "sentences" not in stim:
            raise ValueError("Study 1R message arms need the talking-sting stimuli file (configs/study1r_stimuli.yaml)")
        for k in range(3):
            check_templates(talk_for(stim, condition, k), condition)
        n_llm = len(cfg["sellers"])
        longest = longest_message(stim, condition, agent_names(n_llm, "Seller"))
        if longest > int(cfg.get("max_message_length", 500)):
            raise ValueError(f"longest possible {condition} message ({longest} chars) exceeds max_message_length")


def failure_reason(exc: BaseException) -> str:
    """Classify an episode failure. Reasons are reportable per arm (DECISIONS D-016)."""
    import json as _json
    if isinstance(exc, NoPreError):
        return "no_pre"
    if isinstance(exc, ParseCapExceeded):
        return "parse_cap"
    if isinstance(exc, CallBudgetExceeded):
        return "attempt_cap"
    if isinstance(exc, ProviderMismatch):
        return "provider_mismatch"
    if isinstance(exc, ModelCallFailed):
        return "api_failure"
    if isinstance(exc, (_json.JSONDecodeError, ValueError)) and "extract_json" in traceback.format_exc():
        return "parse_error"
    return "other"


def seller_prompt(cfg: dict[str, Any]) -> str:
    """'default', 'ceo' (upstream boss_pressure) or 'volume' (prereg/stage2_spec.md section 3).
    Legacy configs use boss_pressure: true/false."""
    if "seller_prompt" in cfg:
        if "boss_pressure" in cfg:
            raise ValueError("set seller_prompt or boss_pressure, not both")
        if cfg["seller_prompt"] not in ("default", "ceo", "volume"):
            raise ValueError(f"unknown seller_prompt {cfg['seller_prompt']!r}")
        return cfg["seller_prompt"]
    return "ceo" if cfg.get("boss_pressure") else "default"


def sting_condition(st: dict[str, Any]) -> str:
    """Condition of the sting; legacy configs use mode: silent."""
    if "condition" in st:
        return st["condition"]
    if st.get("mode", "silent") != "silent":
        raise ValueError("sting.mode other than 'silent' is not supported; use sting.condition")
    return "silent"


def stimulus_for(st: dict[str, Any], replicate_index: int) -> tuple[Optional[int], Optional[str], Optional[str]]:
    """(t0, message_id, text) for the sting's condition and replicate index; (None, None, None) if silent.
    The price floor X for anchor/directive/offer arms comes from ``price_floor_for``.

    Paraphrase number = replicate index mod 3 (spec section 1); numbers 0, 1, 2 map to IDs ending 1, 2, 3 (D-064).
    """
    condition = sting_condition(st)
    if condition == "silent":
        return None, None, None
    path = Path(st["stimuli_file"])
    if not path.is_absolute():
        path = REPO_ROOT / path
    stim = yaml.safe_load(path.read_text(encoding="utf-8"))
    ids = sorted(stim["messages"][condition])
    message_id = ids[replicate_index % 3]
    return int(st.get("t0", stim["t0"])), message_id, stim["messages"][condition][message_id]


def price_floor_for(st: dict[str, Any]) -> Optional[float]:
    """X (stimuli x_price) for anchor, directive and offer arms; None otherwise (prereg/stage2_spec.md section 4).
    None with a Study 1R x_rule: there X is computed per episode by the sting (StingSeller.set_x)."""
    if sting_condition(st) not in FLOOR_CONDITIONS or st.get("x_rule") is not None:
        return None
    path = Path(st["stimuli_file"])
    path = path if path.is_absolute() else REPO_ROOT / path
    return float(yaml.safe_load(path.read_text(encoding="utf-8"))["x_price"])


def manipulation_check(rep_dir: Path, sting_id: str, message: str, llm_ids: list[str], round_seen: int) -> dict[str, Any]:
    """Human message 22: in every message arm, the sting's message must appear (in full) in both LLM sellers'
    round-11 prompts (upstream renders it as '- From <sting>: <text>', seller_prompt_base.jinja2:61-63)."""
    import re as _re
    needle = f"- From {sting_id}: {message}"
    missing = []
    for seller in llm_ids:
        md = (rep_dir / "upstream_logs" / f"{seller}.md")
        text = md.read_text(encoding="utf-8") if md.is_file() else ""
        prompts = {int(m.group(1)): m.group(2) for m in
                   _re.finditer(r"## Prompt: Round (\d+) - [^\n]*\n`{6}\n(.*?)\n`{6}", text, flags=_re.S)}
        if needle not in prompts.get(round_seen, ""):
            missing.append(seller)
    return {"round": round_seen, "passed": not missing, "missing": missing}


def sting_record(sting: StingSeller) -> dict[str, Any]:
    """Contents of sting_log.json."""
    return {
        "sting_id": sting.id, "mode": sting.mode, "condition": sting.condition, "t0": sting.t0,
        "message_id": sting.message_id, "message_text": sting.message_text, "pricing_rule": sting.pricing_rule,
        "initial_ask": sting.initial_ask, "fixed_ask": sting.fixed_ask, "llm_seller_ids": sting.llm_seller_ids,
        "price_floor": sting.price_floor, "floor_from_round": sting.floor_from_round,
        "asks": sting.ask_log, "received_messages": sting.received_messages,
        "messages_sent": sting.sent_messages,
        **({"x_rule": sting.x_rule, "x": sting.x_log, "post_until": sting.post_until, "talk": sting.talk,
            "followup_log": sting.followup_log, "competitive": sting.competitive} if sting.x_rule is not None else {}),
    }


def write_json(path: Path, obj: Any) -> None:
    """Write a new file; refuse to overwrite (runs/ is append-only)."""
    with open(path, "x", encoding="utf-8") as f:
        json.dump(obj, f, indent=2)


def _calls_cost(path: Path) -> float:
    if not path.is_file():
        return 0.0
    return sum((json.loads(l).get("cost_usd_reported") or 0.0) for l in path.read_text(encoding="utf-8").splitlines())


def spent_in_budget_group(group: str, runs_dir: Path) -> float:
    """Actual cost (OpenRouter-reported) already spent by runs in a budget group: episode runs whose config has
    budget.group == group, and judge runs over such runs. Read from disk, so finished episodes count at once."""
    total = 0.0
    for cfg_path in Path(runs_dir).glob("*/*/run_config.json"):
        doc = json.loads(cfg_path.read_text(encoding="utf-8"))
        if (doc.get("config", {}).get("budget") or {}).get("group") == group:
            total += sum(_calls_cost(p) for p in cfg_path.parent.glob("*/calls.jsonl"))
    for judge_path in Path(runs_dir).glob("judge/*/judge_run.json"):
        doc = json.loads(judge_path.read_text(encoding="utf-8"))
        if doc.get("budget_group") == group:
            total += _calls_cost(judge_path.parent / "calls.jsonl")
    return total


class BudgetGuard:
    """Refuses to start an episode if spent + in-flight reservations + its estimate would exceed the cap."""

    def __init__(self, group: str, cap_usd: float, per_episode_usd: float, runs_dir: Path):
        import threading
        self.group, self.cap, self.per_episode, self.runs_dir = group, float(cap_usd), float(per_episode_usd), runs_dir
        self._lock = threading.Lock()
        self.reserved = 0.0

    def reserve(self, amount: Optional[float] = None) -> bool:
        amount = self.per_episode if amount is None else float(amount)
        with self._lock:
            if spent_in_budget_group(self.group, self.runs_dir) + self.reserved + amount > self.cap:
                return False
            self.reserved += amount
            return True

    def release(self, amount: Optional[float] = None) -> None:
        with self._lock:
            self.reserved -= self.per_episode if amount is None else float(amount)


def run_episode(cfg: dict[str, Any], run_dir: Path, replicate_index: int, replicate_id: str,
                replaces: Optional[str] = None, budget_guard: Optional[BudgetGuard] = None) -> dict[str, Any]:
    amount = float(cfg["estimated_cost_per_episode_usd"])
    if budget_guard is not None and not budget_guard.reserve(amount):
        return {"replicate_id": replicate_id, "replicate_index": replicate_index, "status": "not_started",
                "failure_reason": "budget_cap", "replaces": replaces, "parse_failures": 0,
                "provider_unknown_calls": 0, "rounds_completed": 0}
    try:
        return _run_episode(cfg, run_dir, replicate_index, replicate_id, replaces)
    finally:
        if budget_guard is not None:
            budget_guard.release(amount)


def _run_episode(cfg: dict[str, Any], run_dir: Path, replicate_index: int, replicate_id: str,
                 replaces: Optional[str] = None) -> dict[str, Any]:
    rep_dir = run_dir / replicate_id
    rep_dir.mkdir(parents=False, exist_ok=False)
    started = time.time()
    params = build_params(cfg)
    draws = market_draws(cfg, replicate_index)
    seller_ids = agent_names(len(cfg["seller_valuations"]), "Seller")
    llm_seller_ids = seller_ids[:len(cfg["sellers"])]
    sting_id = seller_ids[-1] if cfg.get("sting") else None
    buyer_ids = agent_names(len(cfg["buyers"]), "Buyer")
    tracker = UsageTracker(max_attempts_total=cfg.get("max_api_attempts_per_episode"),
                           max_parse_failures=cfg.get("max_parse_failures_per_episode"))
    retry = RetryPolicy(**cfg.get("retry", {}))

    setup = {
        "replicate_id": replicate_id, "replicate_index": replicate_index, "replaces": replaces,
        "seller_ids": seller_ids, "buyer_ids": buyer_ids,
        "sting_id": sting_id, "llm_seller_ids": llm_seller_ids,
        "models": {**{sid: s for sid, s in zip(llm_seller_ids, cfg["sellers"])},
                   **({sting_id: {"provider": "scripted", "model": "scripted-sting", **cfg["sting"]}} if sting_id else {}),
                   **{bid: b for bid, b in zip(buyer_ids, cfg["buyers"])}},
        "seller_valuations": dict(zip(seller_ids, params.seller_valuations)),
        "buyer_valuations": dict(zip(buyer_ids, params.buyer_valuations)),
        "seller_companies": dict(zip(seller_ids, draws["seller_companies"])),
        "buyer_companies": dict(zip(buyer_ids, draws["buyer_companies"])),
        "initial_asks": dict(zip(seller_ids, draws["initial_asks"])),
        "initial_bids": dict(zip(buyer_ids, draws["initial_bids"])),
        "temperature": params.temperature, "max_tokens": cfg["max_tokens"],
        "rounds": params.rounds, "seller_comms_enabled": params.seller_comms_enabled,
        "boss_pressure": params.boss_pressure, "seller_prompt": seller_prompt(cfg),
        "seller_prompt_template": params.seller_prompt_template,
    }
    write_json(rep_dir / "market_setup.json", setup)

    # Upstream logger writes auction_results.md, unified.log, <agent>.md, experiment_metadata.json.
    logger = ExperimentLogger(params, experiment_id="upstream_logs", base_dir=str(rep_dir))
    status: dict[str, Any] = {"replicate_id": replicate_id, "replicate_index": replicate_index,
                              "replaces": replaces, "status": "running", "rounds_planned": params.rounds}
    market: Optional[Market] = None
    sting: Optional[StingSeller] = None
    holder: dict[str, Market] = {}
    try:
        logger.log_auction_config()
        sellers = [
            LMSeller(id=sid, company=draws["seller_companies"][i], valuation=params.seller_valuations[i],
                     expt_params=params, logger=logger,
                     client=make_client(cfg["sellers"][i], tracker, sid, "seller",
                                        params.temperature, cfg["max_tokens"], retry, validate_json=True))
            for i, sid in enumerate(llm_seller_ids)
        ]
        if sting_id:
            st = cfg["sting"]
            x_rule, talk = st.get("x_rule"), None
            if x_rule is not None:  # Study 1R: talking sting (sting/study1r_stimuli.py)
                from sting.study1r_stimuli import load as load_stimuli, talk_for
                condition = sting_condition(st)
                t0 = int(st["t0"]) if condition != "silent" else None
                talk = talk_for(load_stimuli(st["stimuli_file"]), condition, replicate_index) if t0 else None
                message_id, message_text = (talk or {}).get("sentence_id"), None
            else:
                t0, message_id, message_text = stimulus_for(st, replicate_index)
            sting = StingSeller(
                condition=sting_condition(st), t0=t0, message_id=message_id, message_text=message_text,
                post_until=st.get("post_until"), x_rule=x_rule, talk=talk, competitive=st.get("competitive"),
                price_floor=price_floor_for(st), floor_from_round=t0 if price_floor_for(st) is not None else None,
                id=sting_id, company=draws["seller_companies"][-1], valuation=params.seller_valuations[-1],
                expt_params=params, pricing_rule=st["pricing_rule"], llm_seller_ids=llm_seller_ids,
                initial_ask=st.get("initial_ask"), fixed_ask=st.get("fixed_ask"),
                history=lambda: [r.seller_asks for r in holder["market"].rounds],
            )
            sellers.append(sting)
        buyers = [
            LMBuyer(id=bid, company=draws["buyer_companies"][i], valuation=params.buyer_valuations[i],
                    expt_params=params, logger=logger,
                    client=make_client(cfg["buyers"][i], tracker, bid, "buyer",
                                       params.temperature, cfg["max_tokens"], retry, validate_json=True))
            for i, bid in enumerate(buyer_ids)
        ]
        logger.metadata["buyer_ids"] = buyer_ids
        logger.metadata["seller_ids"] = seller_ids
        market = Market(sellers=sellers, buyers=buyers, overseer=None, n_claude_agents=0)
        holder["market"] = market
        market.set_initial_orders(
            [(draws["initial_asks"][i], sid) for i, sid in enumerate(seller_ids)],
            [(draws["initial_bids"][i], bid) for i, bid in enumerate(buyer_ids)],
        )
        for _ in range(params.rounds):
            market.run_round()
            logger.log_auction_round(last_round=market.rounds[-1])
        logger.save_experiment_summary()
        status["status"] = "completed"
        if cfg.get("probe"):  # Study 1R awareness probe after round 30 (sting/probe.py)
            from sting.probe import run_probe
            def probe_client(sid: str, max_tokens: int):
                spec = {**cfg["sellers"][llm_seller_ids.index(sid)], "json_mode": False}
                return make_client(spec, tracker, sid, "probe", params.temperature, max_tokens, retry, validate_json=False)
            probe = run_probe(sellers[:len(llm_seller_ids)], market, params, probe_client)
            write_json(rep_dir / "probe.json", probe)
            status["probe"] = {s: r["q2_parsed"] for s, r in probe["sellers"].items()}
            if not probe["complete"]:
                status["status"] = "failed"
                status["failure_reason"] = "probe_missing"
                status["error_type"] = "ProbeMissing"
                status["error"] = f"probe answers missing: {[s for s, r in probe['sellers'].items() if r['error']]}"
        if status["status"] == "failed":
            pass
        elif sting is not None and sting.x_rule is not None:  # Study 1R: G2 checks on every episode (spec section 11)
            from sting.study1r_checks import g2_checks
            check = g2_checks(rep_dir, sting_record(sting), llm_seller_ids, params.max_message_length)
            status["manipulation_check"] = check
            if not check["passed"]:
                status["status"] = "failed"
                status["failure_reason"] = "manipulation_check"
                status["error_type"] = "ManipulationCheckFailed"
                status["error"] = f"Study 1R manipulation check failed: {check}"
        elif sting is not None and sting.condition != "silent":
            check = manipulation_check(rep_dir, sting.id, sting.message_text, llm_seller_ids, sting.t0 + 1)
            status["manipulation_check"] = check
            if not check["passed"]:
                status["status"] = "failed"
                status["failure_reason"] = "manipulation_check"
                status["error_type"] = "ManipulationCheckFailed"
                status["error"] = f"sting message missing from round-{sting.t0 + 1} prompts of {check['missing']}"
    except Exception as exc:  # noqa: BLE001 - any failure marks the replicate failed (D-016)
        status["status"] = "failed"
        status["failure_reason"] = failure_reason(exc)
        status["error_type"] = type(exc).__name__
        status["error"] = str(exc)
        status["traceback"] = traceback.format_exc()
    finally:
        for handler in list(logger.logger.handlers):
            handler.close()
            logger.logger.removeHandler(handler)

    status["rounds_completed"] = len(market.rounds) if market is not None else 0
    if sting is not None:
        write_json(rep_dir / "sting_log.json", sting_record(sting))
        status["sting"] = {"id": sting.id, "asks_submitted": len(sting.ask_log),
                           "messages_received": len(sting.received_messages),
                           "messages_sent": len(sting.sent_messages), "condition": sting.condition,
                           "message_id": sting.message_id}
    status["wall_clock_s"] = round(time.time() - started, 2)
    status["api_attempts"] = tracker.attempts_started
    status["parse_failures"] = tracker.parse_failures
    status["provider_unknown_calls"] = sum(1 for r in tracker.records if r.provider_unknown)
    status["max_parse_failures_per_episode"] = tracker.max_parse_failures
    status["usage_by_role"] = tracker.totals_by("role")
    status["usage_by_agent"] = tracker.totals_by("agent_id")
    with open(rep_dir / "calls.jsonl", "x", encoding="utf-8") as f:
        for rec in tracker.as_dicts():
            f.write(json.dumps(rec) + "\n")
    write_json(rep_dir / "status.json", status)
    return status


def selected_indices(cfg: dict[str, Any], replicate_indices: Optional[list[int]] = None) -> list[int]:
    """Replicate indices to run. Repeats are allowed (human message 13): episodes with the same index share
    the market draw, so repeated indices separate market-draw variance from sampling noise."""
    indices = list(range(int(cfg["replicates"]))) if replicate_indices is None else list(replicate_indices)
    if not indices or min(indices) < 0:
        raise ValueError(f"invalid replicate indices {indices}")
    return indices


def replicate_ids_for(run_id: str, indices: list[int]) -> list[tuple[int, str]]:
    """Unique replicate ids: <run_id>_r<index>, plus _d<n> (n = 1, 2, ...) for every repeat of an index in this run."""
    seen: dict[int, int] = {}
    out = []
    for k in indices:
        seen[k] = seen.get(k, 0) + 1
        out.append((k, f"{run_id}_r{k:03d}" + (f"_d{seen[k]}" if indices.count(k) > 1 else "")))
    return out


def replacement_targets(cfg: dict[str, Any], runs_dir: Path, failed_ids: list[str]) -> list[tuple[int, str]]:
    """(replicate index, failed id) for each failed replicate to replace. Each must exist in this stage, belong to a
    run with the same run_name (same arm), and have status other than completed."""
    out = []
    for fid in failed_ids:
        matches = list(Path(runs_dir).glob(f"{cfg['stage']}/*/{fid}/status.json"))
        if len(matches) != 1:
            raise ValueError(f"replicate {fid} not found (or found more than once) under {runs_dir}/{cfg['stage']}")
        status = json.loads(matches[0].read_text(encoding="utf-8"))
        run_cfg = json.loads((matches[0].parent.parent / "run_config.json").read_text(encoding="utf-8"))["config"]
        if run_cfg["run_name"] != cfg["run_name"]:
            raise ValueError(f"replicate {fid} belongs to arm {run_cfg['run_name']!r}, not {cfg['run_name']!r}")
        if status["status"] == "completed":
            raise ValueError(f"replicate {fid} completed; only failed replicates are replaced")
        out.append((status["replicate_index"], fid))
    return out


def estimate_cost(cfg: dict[str, Any], n_episodes: Optional[int] = None) -> float:
    n = int(cfg["replicates"]) if n_episodes is None else n_episodes
    return float(cfg["estimated_cost_per_episode_usd"]) * n


def run_batch(cfg: dict[str, Any], runs_dir: Path = RUNS_DIR, approve_cost: bool = False,
              replicate_indices: Optional[list[int]] = None, estimate_only: bool = False,
              purpose: str = "test run", command: str = "run_batch()",
              replaces: Optional[list[str]] = None) -> dict[str, Any]:
    validate_config(cfg)
    if replaces and replicate_indices is not None:
        raise ValueError("use either replicate_indices or replaces, not both")
    targets = replacement_targets(cfg, runs_dir, replaces) if replaces else None
    indices = [k for k, _ in targets] if targets else selected_indices(cfg, replicate_indices)
    estimate = estimate_cost(cfg, len(indices))
    print(f"Estimated cost for this batch: ${estimate:.4f} "
          f"({len(indices)} episodes x ${float(cfg['estimated_cost_per_episode_usd']):.4f}; indices {indices})")
    if estimate_only:
        return {"estimate_only": True, "estimated_cost_usd": estimate, "replicate_indices": indices}
    check_run_type(cfg)
    guard = None
    if cfg.get("budget"):
        spent = spent_in_budget_group(cfg["budget"]["group"], runs_dir)
        cap = float(cfg["budget"]["cap_usd"])
        print(f"Budget group {cfg['budget']['group']!r}: spent ${spent:.4f} of cap ${cap:.2f}")
        if spent + estimate > cap:
            raise SystemExit(f"Budget cap refused: spent ${spent:.4f} + estimate ${estimate:.4f} > cap ${cap:.2f}")
        guard = BudgetGuard(cfg["budget"]["group"], cap, float(cfg["estimated_cost_per_episode_usd"]), runs_dir)
    if estimate > COST_APPROVAL_THRESHOLD_USD and not approve_cost:
        raise SystemExit(f"Estimate exceeds ${COST_APPROVAL_THRESHOLD_USD:.2f}; human approval required "
                         f"(rerun with --approve-cost after approval).")
    run_id, run_dir, mirror_root = open_run(cfg, runs_dir, estimate, indices)
    if targets:
        replicate_ids = [(k, f"{run_id}_r{k:03d}_repl{j + 1}") for j, (k, _) in enumerate(targets)]
        replaced = {rid: fid for (_, rid), (_, fid) in zip(replicate_ids, targets)}
    else:
        replicate_ids, replaced = replicate_ids_for(run_id, indices), {}
    with upstream_cwd(mirror_root):
        with ThreadPoolExecutor(max_workers=int(cfg.get("concurrency", 1))) as pool:
            futures = [pool.submit(run_episode, cfg, run_dir, k, rid, replaced.get(rid), guard)
                       for k, rid in replicate_ids]
            statuses = [f.result() for f in futures]
    return close_run(cfg, run_dir, run_id, statuses, purpose, command, runs_dir)


def model_snapshots(cfg: dict[str, Any]) -> dict[str, Any]:
    """Dated snapshot ids (OpenRouter `canonical_slug`) for the run's OpenRouter models, from the free models
    listing. Per-call responses carry only the undated name (ISSUES I-037). Best effort: errors are recorded."""
    models = sorted({s["model"] for s in cfg["sellers"] + cfg["buyers"] if s.get("provider") == "openrouter"})
    if not models:
        return {}
    try:
        import urllib.request
        data = json.load(urllib.request.urlopen("https://openrouter.ai/api/v1/models", timeout=30))["data"]
        by_id = {m["id"]: m for m in data}
        return {m: ({k: by_id[m].get(k) for k in ("canonical_slug", "created", "expiration_date")}
                    if m in by_id else {"error": "not listed"}) for m in models}
    except Exception as exc:  # noqa: BLE001 - recorded, never fatal
        return {m: {"error": f"{type(exc).__name__}: {exc}"} for m in models}


def open_run(cfg: dict[str, Any], runs_dir: Path, estimate: float, indices: list[int],
             extra: Optional[dict[str, Any]] = None) -> tuple[str, Path, Path]:
    env_info = load_env()
    mirror_root, mirror_hash = ensure_mirror()
    run_id = f"{utc_stamp()}_{cfg['run_name']}_{uuid.uuid4().hex[:6]}"
    run_dir = runs_dir / cfg["stage"] / run_id
    run_dir.mkdir(parents=True, exist_ok=False)
    write_json(run_dir / "run_config.json", {
        "run_id": run_id, "config": cfg, "estimated_cost_usd": estimate, "replicate_indices": indices,
        "upstream_commit": upstream_commit(), "python": sys.version, "platform": platform.platform(),
        "env_file_used": env_info["env_file"], "keys_present": env_info["present"],
        "key_sources": env_info["key_sources"], "overridden_environment_keys": env_info["overridden_environment_keys"],
        "wandb_mode": os.environ.get("WANDB_MODE"), "started_utc": utc_stamp(),
        "prompt_mirror_sha256": mirror_hash, "prompt_mirror_root": str(mirror_root),
        "model_snapshots_at_start": model_snapshots(cfg), **(extra or {}),
    })
    return run_id, run_dir, mirror_root


def model_identity_flags(run_dir: Path, snapshots_at_end: dict[str, Any]) -> dict[str, Any]:
    """F-4 (human message 19): flag the run if a dated snapshot id differs between start and end, or if any
    per-call returned model name differs from the requested (pinned) model."""
    start = json.loads((run_dir / "run_config.json").read_text(encoding="utf-8")).get("model_snapshots_at_start", {})
    changed = {m: {"start": (start.get(m) or {}).get("canonical_slug"), "end": (snapshots_at_end.get(m) or {}).get("canonical_slug")}
               for m in sorted(set(start) | set(snapshots_at_end))
               if (start.get(m) or {}).get("canonical_slug") != (snapshots_at_end.get(m) or {}).get("canonical_slug")}
    mismatches: dict[str, int] = {}
    for calls in run_dir.glob("*/calls.jsonl"):
        for line in calls.read_text(encoding="utf-8").splitlines():
            rec = json.loads(line)
            if rec.get("provider") == "fake" or rec.get("error") or rec.get("returned_model") is None:
                continue
            if rec["returned_model"] != rec["requested_model"]:
                key = f"{rec['requested_model']} -> {rec['returned_model']}"
                mismatches[key] = mismatches.get(key, 0) + 1
    return {"snapshot_changed_during_run": changed, "returned_model_mismatches": mismatches,
            "model_identity_flag": bool(changed or mismatches)}


def close_run(cfg: dict[str, Any], run_dir: Path, run_id: str, statuses: list[dict[str, Any]], purpose: str,
              command: str, runs_dir: Path) -> dict[str, Any]:
    summary = {
        "run_id": run_id, "finished_utc": utc_stamp(), "model_snapshots_at_end": model_snapshots(cfg),
        "replicates": len(statuses),
        "completed": sum(s["status"] == "completed" for s in statuses),
        "failed": sum(s["status"] == "failed" for s in statuses),
        "not_started_budget_cap": [s["replicate_id"] for s in statuses if s["status"] == "not_started"],
        "replacements": {s["replicate_id"]: s["replaces"] for s in statuses if s.get("replaces")},
        "failures_by_reason": {r: sum(s.get("failure_reason") == r for s in statuses if s["status"] == "failed")
                               for r in sorted({s["failure_reason"] for s in statuses if s["status"] == "failed"})},
        "parse_failures_total": sum(s["parse_failures"] for s in statuses),
        "provider_unknown_calls_total": sum(s["provider_unknown_calls"] for s in statuses),
        "parse_failures_by_replicate": {s["replicate_id"]: s["parse_failures"] for s in statuses},
        "failed_replicates": [{"replicate_id": s["replicate_id"], "failure_reason": s.get("failure_reason"),
                               "error_type": s.get("error_type"), "error": s.get("error")}
                              for s in statuses if s["status"] == "failed"],
        "run_dir": str(run_dir),
    }
    summary.update(model_identity_flags(run_dir, summary["model_snapshots_at_end"]))
    write_json(run_dir / "run_summary.json", summary)
    # Phase 2.5: manifest, ledger, report, lab notebook, index (CLAUDE.md rule 5).
    record_run(run_dir, purpose, command, docs_root=docs_root_for(runs_dir))
    return summary


def main(argv: Optional[list[str]] = None) -> None:
    parser = argparse.ArgumentParser(description="Minimal sting-study episode runner.")
    parser.add_argument("config", type=Path)
    parser.add_argument("--approve-cost", action="store_true",
                        help="Required when the estimate exceeds $2 and the human has approved it.")
    parser.add_argument("--estimate-only", action="store_true", help="Print the cost estimate and exit; no calls.")
    parser.add_argument("--purpose", required=True, help="Why this run is being made (recorded in the lab notebook).")
    parser.add_argument("--replicate-indices", type=lambda s: [int(x) for x in s.split(",")], default=None,
                        help="Comma-separated replicate indices to run, e.g. 0 (pilot) or 1,2.")
    parser.add_argument("--replaces", type=lambda s: s.split(","), default=None,
                        help="Comma-separated failed replicate ids to replace (new ids reference them).")
    args = parser.parse_args(argv)
    cfg = yaml.safe_load(args.config.read_text(encoding="utf-8"))
    summary = run_batch(cfg, approve_cost=args.approve_cost, replicate_indices=args.replicate_indices,
                        estimate_only=args.estimate_only, purpose=args.purpose, replaces=args.replaces,
                        command="python -m sting.minimal_runner " + " ".join(sys.argv[1:]))
    print(json.dumps(summary, indent=2))


if __name__ == "__main__":
    main()
