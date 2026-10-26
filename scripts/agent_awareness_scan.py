"""Study 1 "other-agent awareness" scan (human message 43). EXPLORATORY; no API calls; data read-only.

For every LLM seller-round (all arms; rounds 1-10 and 11-30 separately; the public message and the private fields
separately), each sentence that names another agent is classified by target and treatment with sentence-level rules.

Targets (whole-word, case-insensitive): the peer LLM seller (Seller A for Seller B and vice versa), Seller C, buyers
(any "Buyer"/"Buyers", including "Buyer A" etc.). Agents named only by company name are not counted.
Treatment (keywords in the same sentence as the name; a sentence can count in several categories):
 (a) price observation: ask(s), bid(s), price/prices/priced/pricing, "$", undercut*, queue, lowest, highest
 (b) message reference: said, says, message(s), propose/proposed/proposal(s), suggest/suggested/suggestion(s),
     agree/agreed/agrees/agreement, offer/offered/offers, asked, according to, reply/replied/replies
 (c) intention attribution: trying, want(s), aim(s), plan(s), strategy, intend(s), likely to, seems to be
Sentences: split at . ! ? followed by whitespace, and at line breaks.
Fields: public = message_to_sellers; private = reflection, plan_for_this_hour, plan_for_message, new_memory,
scratch_pad_update (pooled).
A seller-round counts for a target (or target x category) if any sentence in that field qualifies.

The same scan runs on the 10 Study 1R pilot episodes (comparison, EXPLORATORY). Pilot snippets exclude every
seller-round that is in the Study 1R development or validation labeling sets, so the scan cannot unblind them.

Usage: python scripts/agent_awareness_scan.py
"""
from __future__ import annotations

import glob
import json
import random
import re
import sys
from collections import defaultdict
from pathlib import Path

import yaml

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from sting.judge import seller_responses  # noqa: E402
from sting.paths import REPO_ROOT  # noqa: E402

OUT = REPO_ROOT / "results" / "study1_diagnostics"
PRIVATE = ["reflection", "plan_for_this_hour", "plan_for_message", "new_memory", "scratch_pad_update"]
WINDOWS = {"r1-10": range(1, 11), "r11-30": range(11, 31)}
TARGETS = ("peer", "Seller C", "buyers")
CATS = {
    "a_price": re.compile(r"\bask(s)?\b|\bbids?\b|\bpric(e|es|ed|ing)\b|\$|\bundercut\w*|\bqueue\b|\blowest\b|\bhighest\b", re.I),
    "b_message": re.compile(r"\bsaid\b|\bsays\b|\bmessages?\b|\bpropos(e|ed|al|als)\b|\bsuggest(ed|ion|ions)?\b"
                            r"|\bagree(d|s|ment)?\b|\boffer(ed|s)?\b|\basked\b|\baccording to\b|\brepl(y|ied|ies)\b", re.I),
    "c_intention": re.compile(r"\btrying\b|\bwants?\b|\baims?\b|\bplans?\b|\bstrategy\b|\bintends?\b|\blikely to\b"
                              r"|\bseems to be\b", re.I),
}
SPLIT = re.compile(r"(?<=[.!?])\s+|\n+")
SNIPPETS = 5


def target_re(target: str, seller: str) -> re.Pattern:
    if target == "peer":
        return re.compile(r"\b" + ("Seller B" if seller == "Seller A" else "Seller A") + r"\b", re.I)
    if target == "Seller C":
        return re.compile(r"\bSeller C\b", re.I)
    return re.compile(r"\bbuyers?\b", re.I)


def classify(text: str, seller: str) -> dict[str, dict[str, list[str]]]:
    """target -> {"any": [sentences], category: [sentences]}"""
    out = {t: defaultdict(list) for t in TARGETS}
    for sent in (x.strip() for x in SPLIT.split(text or "")):
        if not sent:
            continue
        for t in TARGETS:
            if target_re(t, seller).search(sent):
                out[t]["any"].append(sent)
                for c, rx in CATS.items():
                    if rx.search(sent):
                        out[t][c].append(sent)
    return out


def episodes(campaign_glob: str, campaign_yaml: Path) -> list[tuple[str, Path]]:
    arms = {a["name"]: a for a in yaml.safe_load(campaign_yaml.read_text(encoding="utf-8"))["arms"]}
    eps = []
    for c in sorted(glob.glob(str(REPO_ROOT / campaign_glob))):
        for name, info in json.loads(Path(c).read_text(encoding="utf-8"))["arms"].items():
            for rep in sorted(p for p in Path(info["run_dir"]).iterdir() if p.is_dir()):
                if json.loads((rep / "status.json").read_text(encoding="utf-8"))["status"] == "completed":
                    eps.append((name, rep))
    return eps


def scan(eps: list[tuple[str, Path]], exclude: set = frozenset()) -> dict:
    counts = defaultdict(lambda: defaultdict(int))     # (arm, window, field) -> {"n": .., "target|cat": ..}
    snippets = defaultdict(list)                       # (target, cat) -> [(arm, rep, seller, round, field, sentence)]
    for arm, rep in eps:
        llm = json.loads((rep / "market_setup.json").read_text(encoding="utf-8"))["llm_seller_ids"]
        for s in llm:
            for r, resp in seller_responses(rep / "upstream_logs" / f"{s}.md").items():
                win = next((w for w, rg in WINDOWS.items() if r in rg), None)
                if win is None:
                    continue
                texts = {"public": str(resp.get("message_to_sellers") or ""),
                         "private": "\n".join(str(resp.get(k) or "") for k in PRIVATE)}
                for field, text in texts.items():
                    key = (arm, win, field)
                    counts[key]["n"] += 1
                    cl = classify(text, s)
                    for t in TARGETS:
                        for c, sents in cl[t].items():
                            if sents:
                                counts[key][f"{t}|{c}"] += 1
                                if c != "any" and (rep.name, s, r) not in exclude:
                                    snippets[(t, c)].append((arm, rep.name, s, r, field, sents[0]))
    return {"counts": counts, "snippets": snippets}


def pick_snippets(snips: list[tuple], seed: str) -> list[tuple]:
    rng = random.Random(seed)
    offer = [x for x in snips if x[0].endswith("_offer")]
    other = [x for x in snips if not x[0].endswith("_offer")]
    out = rng.sample(offer, min(SNIPPETS, len(offer)))
    return out + rng.sample(other, min(SNIPPETS - len(out), len(other)))


def share(c: dict, k: str) -> str:
    return f"{c.get(k, 0) / c['n']:.3f}" if c.get("n") else "n/a"


def tables(res: dict, arms: list[str], title: str) -> list[str]:
    L = [f"## {title}", ""]
    counts = res["counts"]
    for win in WINDOWS:
        for field in ("public", "private"):
            L += [f"### 1. Share of seller-rounds mentioning each target: {field}, rounds {win[1:]}", "",
                  "| Arm | n | " + " | ".join(f"{t} {c}" for t in TARGETS for c in ("any", "a", "b", "c")) + " |",
                  "|---|---|" + "---|" * 12]
            for arm in arms:
                c = counts.get((arm, win, field), {})
                L.append(f"| {arm} | {c.get('n', 0)} | " + " | ".join(
                    share(c, f"{t}|{k}") for t in TARGETS for k in ("any", "a_price", "b_message", "c_intention")) + " |")
            L.append("")
    L += ["### 2. Message reference (category b): peer seller vs Seller C", "",
          "| Arm | Window | Public: peer | Public: Seller C | Private: peer | Private: Seller C |", "|---|---|---|---|---|---|"]
    for arm in arms:
        for win in WINDOWS:
            pub, prv = counts.get((arm, win, "public"), {}), counts.get((arm, win, "private"), {})
            L.append(f"| {arm} | {win[1:]} | {share(pub, 'peer|b_message')} | {share(pub, 'Seller C|b_message')} | "
                     f"{share(prv, 'peer|b_message')} | {share(prv, 'Seller C|b_message')} |")
    L += ["", "### 3. Verbatim snippets (up to 5 per target x category; Offer arms first; seeded random draw)", ""]
    for t in TARGETS:
        for c in ("a_price", "b_message", "c_intention"):
            picks = pick_snippets(res["snippets"].get((t, c), []), f"{title}-{t}-{c}")
            L.append(f"**{t}, {c}** ({len(res['snippets'].get((t, c), []))} seller-round-fields qualify)")
            L.append("")
            for arm, rep, s, r, field, sent in picks:
                L.append(f"- {arm} {rep[-5:]} {s} r{r} {field}: \"{sent[:300]}\"")
            L.append("")
    return L


def main() -> None:
    s1 = episodes("runs/stage2/_campaigns/*/campaign.json", REPO_ROOT / "configs" / "stage2" / "campaign.yaml")
    s1r = episodes("runs/study1r_pilot/_campaigns/*/campaign.json",
                   REPO_ROOT / "configs" / "study1r" / "pilot" / "campaign.yaml")
    exclude = set()
    for d in ("dev", "validation"):
        kp = REPO_ROOT / "results" / "study1r" / "labeling_keys" / d / "labeling_key.json"
        if kp.is_file():
            exclude |= {(k["replicate_id"], k["seller"], k["round"]) for k in json.loads(kp.read_text(encoding="utf-8")).values()}
    r1, r2 = scan(s1), scan(s1r, exclude)
    arms1 = sorted({a for a, _ in s1}, key=lambda a: (a.split("_")[0] != "mini-low", a))
    arms2 = sorted({a for a, _ in s1r})
    L = ["# Other-agent awareness scan (EXPLORATORY)", "",
         "Generated by `scripts/agent_awareness_scan.py` (no API calls; data read-only). Sentence-level keyword rules "
         "(see the script docstring): targets peer LLM seller / Seller C / buyers; categories (a) price observation, "
         "(b) message reference, (c) intention attribution, in the same sentence as the name. Shares are of "
         "seller-rounds (each LLM seller in each round) with at least one qualifying sentence in the field. "
         "Facts only.", "",
         f"Study 1: {len(s1)} completed confirmatory episodes. Study 1R pilot: {len(s1r)} episodes; pilot snippets "
         f"exclude the {len(exclude)} seller-rounds in the Study 1R development and validation sets.", ""]
    L += tables(r1, arms1, "Study 1 (confirmatory episodes)")
    L += tables(r2, arms2, "Study 1R pilot (comparison, EXPLORATORY)")
    OUT.mkdir(parents=True, exist_ok=True)
    (OUT / "AGENT_AWARENESS.md").write_text("\n".join(L) + "\n", encoding="utf-8")
    js = {name: {"|".join(k): dict(v) for k, v in res["counts"].items()} for name, res in (("study1", r1), ("study1r_pilot", r2))}
    (OUT / "agent_awareness.json").write_text(json.dumps(js, indent=2), encoding="utf-8")
    print(f"written: {len(L)} lines; study1 episodes {len(s1)}, pilot episodes {len(s1r)}, excluded seller-rounds {len(exclude)}")


if __name__ == "__main__":
    main()
