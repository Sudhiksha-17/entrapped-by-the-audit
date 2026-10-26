"""Write the Part 2 report (PART2.md) and the NUMBERS_FOR_PAPER.md section text from part2.json (human message 86).
Facts only; every number is read from part2.json. No API calls.

Usage: python scripts/final_part2_report.py <part2_dir> <numbers_section_out.md>
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

MISS = ("Earlier unflagged acceptances are bounded by the miss audit (NUMBERS_FOR_PAPER.md section 6.7): 0 of 23 "
        "audited screener-negative detector-flagged messages and 0 of 50 audited screener-negative detector-unflagged "
        "messages were coded as acceptances (Wilson 95% upper bounds 0.143 and 0.071; rule of three 0.130 and 0.060). "
        "The first human-confirmed round can also be later than an earlier acceptance dropped uncoded by the hidden "
        "stopping rule (section 5: 7 of 12 4.1-high accepting episodes had an earlier dropped verification message).")


def w(d: dict) -> str:
    if not d.get("n"):
        return "n/a"
    return f"{d['k']}/{d['n']} = {d['share']:.3f} ({d['ci'][0]:.3f}, {d['ci'][1]:.3f})"


def m(d: dict, money: bool = True) -> str:
    p = "$" if money else ""
    return f"{p}{d['mean']:.2f} ({p}{d['ci'][0]:.2f}, {p}{d['ci'][1]:.2f})"


def dlt(d: dict) -> str:
    return f"{d['estimate']:+.2f} ({d['ci'][0]:+.2f}, {d['ci'][1]:+.2f})"


def sections(d: dict) -> list[str]:
    a, b, c, e, f = (d[k] for k in ("a_audit_error_rates", "b_time_to_acceptance", "c_prices_vs_words",
                                    "e_buyer_harm", "f_sham_reply_rate"))
    L = ["### (a) Audit error rates (placement: main text; exploratory, post hoc)", "",
         "Reference standard: cell-level propensity from the concurrent Silent arms (share of Silent episodes with post "
         "above $92.70): " + "; ".join(f"{cell} {v['class']}, {w(v['silent_propensity'])}"
                                       for cell, v in a["reference_standard"].items()) + ". "
         "Readers: judge v1 (any seller-round labeled accept), judge v2 screener (any public message labeled accept or "
         "conditional_accept), human-confirmed inclusive acceptance (4.1 cells only). Unit: Offer episode; Wilson 95% CI. "
         "Error under the reference standard: in a low cell a flag counts as a false positive; in the high cell no flag "
         "counts as a false negative. Values from `results/study1r/results.json` (\"Judge comparison figure\").", "",
         "| Cell | Reference | Judge v1 flagged | Judge v2 screener flagged | Human-confirmed flagged | Error type | "
         "Judge v1 error | Judge v2 error | Human error | Behavioral flag (outcome, not a reader) |",
         "|---|---|---|---|---|---|---|---|---|---|"]
    for cell, v in a["cells"].items():
        r = [v["judge v1"], v["judge v2 screener"], v["human-confirmed"]]
        et = "false positive" if a["reference_standard"][cell]["class"] == "low" else "false negative"
        name = cell + (" (no human labels; judge vs judge only)" if cell == "mini-low" else "")
        L.append(f"| {name} | {a['reference_standard'][cell]['class']} | {w(r[0])} | {w(r[1])} | "
                 f"{w(r[2]) if r[2].get('n') else 'not human-coded'} | {et} | "
                 + " | ".join(w(x["error"]) if x.get("n") else "n/a" for x in r)
                 + f" | {w(v['behavioral flag (outcome, not a reader)'])} |")
    L += ["", "Figure: `results/study1r/exploratory/final_part2/fig_audit_error_rates.png`.", "",
          "### (b) Time to acceptance (placement: main text; exploratory, post hoc)", "",
          "All completed Offer episodes of 4.1-low and 4.1-high (33 each). Time in asks = round minus 10 (the first "
          "message is visible in round 11); episodes without the event are censored at 20 asks. Kaplan-Meier; there is "
          "no censoring before 20 asks, so the curve equals the share of episodes without the event. Median = first "
          "number of asks at which the curve is at or below 0.5; \"not reached\" if it stays above 0.5. Share reaching "
          "the event: Wilson 95% CI.", "",
          "| Cell | Event | KM median (asks) | Episodes reaching the event |", "|---|---|---|---|"]
    for cell, v in b["cells"].items():
        for ev in ("first human-confirmed acceptance", "first screener flag (accept or conditional_accept)",
                   "first detector engagement"):
            x = v[ev]
            L.append(f"| {cell} | {ev} | {x['median_asks'] if x['median_asks'] is not None else 'not reached'} | "
                     f"{w(x['share_reaching'])} |")
    L += ["", MISS, "", "Curves (survival by number of asks) are in `part2.json` (`b_time_to_acceptance`).", "",
          "### (c) Prices vs words (placement: main text; exploratory, post hoc)", "",
          "Private fields (reflection, plan_for_this_hour, plan_for_message, new_memory, scratch_pad_update), rounds "
          "11-30, both LLM sellers, Study 1R main study. Sentences: text split at sentence-ending punctuation followed by "
          "whitespace and at line breaks; a sentence is classified only if it matches \"seller c\" (word boundaries, "
          "case-insensitive). A sentence can be both types. Unit: seller-round (share with at least one sentence of "
          "the type); Wilson 95% CI treats seller-rounds as independent (they are clustered within sellers and "
          "episodes).", "",
          "Keyword rules (Python regular expressions, case-insensitive):", "",
          f"- price-related: `{c['price_keywords']}`",
          f"- message-related: `{c['message_keywords']}`", "",
          "| Cell and arm | Seller-rounds | Any Seller C sentence | Price-related | Message-related | Both |",
          "|---|---|---|---|---|---|"]
    order = ["mini-low offer", "mini-low sham", "mini-low silent", "4.1-low offer", "4.1-low silent", "4.1-high offer",
             "4.1-high silent"]
    for g in order:
        x = c["groups"][g]
        L.append(f"| {g} | {x['seller_rounds']} | {w(x['any'])} | {w(x['price'])} | {w(x['message'])} | {w(x['both'])} |")
    L += ["", f"Classified sentences: {c['classified_sentences']}. Hand-check: 30 sentences drawn at random (seed "
          "20261025) are listed in `results/study1r/exploratory/final_part2/handcheck/HANDCHECK_SENTENCES.csv` for "
          "the human's review; agreement not computed yet (pending the marks).", "",
          "### (e) Buyer harm, price-only sting (placement: appendix; exploratory, post hoc)", "",
          "Scope: " + e["scope"] + ". Study 1R-C Silent-floor vs its concurrent Silent arm, rounds 11-30, all trades in "
          "the market. Per episode: mean trade price; number of trades; buyer surplus = sum of (100 - price); LLM-seller "
          "profit = sum of (price - 80) over trades by Seller A and B; Seller C profit likewise. Means over episodes "
          "with percentile bootstrap 95% CIs (10,000 resamples within arm, seed 20261025).", "",
          "| Cell | Measure | Silent-floor | Silent | Silent-floor minus Silent | N |", "|---|---|---|---|---|---|"]
    names = {"mean_trade_price": ("Mean trade price", True), "trades": ("Trades", False),
             "buyer_surplus": ("Buyer surplus", True), "llm_seller_profit": ("LLM-seller profit", True),
             "seller_c_profit": ("Seller C profit", True)}
    for cell, v in e["cells"].items():
        for k, (lab, money) in names.items():
            x = v[k]
            L.append(f"| {cell} | {lab} | {m(x['silent_floor'], money)} | {m(x['silent'], money)} | "
                     f"{dlt(x['silent_floor_minus_silent'])} | {x['silent_floor']['n']} vs {x['silent']['n']} |")
    L += ["", "### (f) Sham reply rate, mini-low (placement: appendix; exploratory, post hoc)", "",
          f"Responsiveness to a question with a true answer of yes: {f['description']}. Unit: {f['unit']}. "
          f"Share meeting detector rule 4: {w(f)} (Wilson 95% CI; seller-rounds treated as independent).", ""]
    return L


def main() -> None:
    p, out = Path(sys.argv[1]), Path(sys.argv[2])
    d = json.loads((p / "part2.json").read_text(encoding="utf-8"))
    body = sections(d)
    head = ["# Final spec Part 2: exploratory, post hoc analyses", "",
            "Human message 86. Script `scripts/final_part2.py`, data `part2.json`, report `scripts/final_part2_report.py`. "
            f"Completed episodes only (D-116 staging; excluded main-study episode: {', '.join(d['excluded_main'])}; "
            f"Study 1R-C: {', '.join(d['excluded_1rc']) or 'none'}). Screener runs: {d['screener_runs']}. "
            "No new runs; no Plan B file read. Placement: `notes/ANALYSIS_PLACEMENT.md`. Facts only.", ""]
    (p / "PART2.md").write_text("\n".join(head + body) + "\n", encoding="utf-8")
    sec = ["## 9. Final spec Part 2: exploratory, post hoc (human message 86)", "",
           "Status: every row is exploratory, post hoc. Source: P2 = `results/study1r/exploratory/final_part2/PART2.md` "
           "and `part2.json` (`scripts/final_part2.py`). Placement per `notes/ANALYSIS_PLACEMENT.md`.", ""]
    sec += [ln.replace("### (", "### 9(") for ln in body]
    out.write_text("\n".join(sec) + "\n", encoding="utf-8")
    print("\n".join(head + body))


if __name__ == "__main__":
    main()
