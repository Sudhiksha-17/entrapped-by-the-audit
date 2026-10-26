"""Study 1R talking-sting stimuli (prereg_study1r/STUDY1R_STIMULI.md; configs/study1r_stimuli.yaml). Pure functions.

Message for a round = arm sentence + " " + segment for Seller A + " " + segment for Seller B. A seller's segment is an
ACK if its previous-round public message (as delivered by the market, i.e. after truncation) contains "Seller C"
(case-insensitive, as a whole phrase: word boundaries, so "seller cooperation" does not trigger) or the episode's exact
X string (two decimals, e.g. "92.37"); otherwise an ASK. Round t0 (10): both ASK.
"""
from __future__ import annotations

import re
from pathlib import Path
from typing import Any, Optional

import yaml

from sting.paths import REPO_ROOT

SELLER_C = re.compile(r"\bseller c\b", re.IGNORECASE)
MESSAGE_CONDITIONS = ("sham", "anchor", "offer")
X_CONDITIONS = ("anchor", "offer")


def load(path: str | Path) -> dict[str, Any]:
    p = Path(path)
    return yaml.safe_load((p if p.is_absolute() else REPO_ROOT / p).read_text(encoding="utf-8"))


def x_string(x: float) -> str:
    return f"{x:.2f}"


def fill(text: str, x: Optional[float], seller: Optional[str] = None) -> str:
    if "{X}" in text:
        if x is None:
            raise ValueError("text needs X but X is not set")
        text = text.replace("{X}", x_string(x))
    return text.replace("{S}", seller) if seller is not None else text


def talk_for(stim: dict[str, Any], condition: str, replicate_index: int) -> dict[str, Any]:
    """Sentence template and segment templates for a message arm; paraphrase = replicate index mod 3."""
    ids = sorted(stim["sentences"][condition])
    sid = ids[replicate_index % 3]
    seg = stim["segments"][stim["segment_set"][condition]]
    return {"sentence_id": sid, "sentence": stim["sentences"][condition][sid], "ASK": seg["ASK"], "ACK": seg["ACK"]}


def check_templates(talk: dict[str, Any], condition: str) -> None:
    n = talk["sentence"].count("{X}")
    if n != (1 if condition in X_CONDITIONS else 0):
        raise ValueError(f"{condition} sentence has {n} X placeholders")
    if talk["ASK"].count("{X}") != 0 or talk["ACK"].count("{X}") != (1 if condition == "offer" else 0):
        raise ValueError(f"{condition} segments have the wrong X placeholders")
    if any(talk[k].count("{S}") != 1 for k in ("ASK", "ACK")):
        raise ValueError("each segment needs exactly one {S}")


def segment_state(previous_message: Optional[str], x: float) -> tuple[str, Optional[dict[str, Any]]]:
    """('ACK', trigger) or ('ASK', None) from a seller's previous-round public message."""
    if not previous_message:
        return "ASK", None
    matched = []
    if SELLER_C.search(previous_message):
        matched.append("Seller C")
    if x_string(x) in previous_message:
        matched.append(x_string(x))
    return ("ACK", {"text": previous_message, "matched": matched}) if matched else ("ASK", None)


def compose(talk: dict[str, Any], x: Optional[float], states: dict[str, str], llm_ids: list[str]) -> str:
    parts = [fill(talk["sentence"], x)] + [fill(talk[states[s]], x, s) for s in llm_ids]
    return " ".join(parts)


def expected_x_count(condition: str, states: dict[str, str]) -> int:
    if condition == "anchor":
        return 1
    if condition == "offer":
        return 1 + sum(v == "ACK" for v in states.values())
    return 0


def longest_message(stim: dict[str, Any], condition: str, llm_ids: list[str], x: float = 99.99) -> int:
    """Length of the longest possible message for the arm (any paraphrase, each seller ASK or ACK; X at its
    longest possible width, 5 characters)."""
    seg = stim["segments"][stim["segment_set"][condition]]
    longest_seg = {s: max(len(fill(seg[k], x, s)) for k in ("ASK", "ACK")) for s in llm_ids}
    longest_sentence = max(len(fill(t, x)) for t in stim["sentences"][condition].values())
    return longest_sentence + sum(1 + n for n in longest_seg.values())
