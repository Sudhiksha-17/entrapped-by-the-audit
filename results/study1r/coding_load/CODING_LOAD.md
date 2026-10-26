# Study 1R option A: estimated human coding load (from the pilot; human messages 64 and 65)

Screener: judge v2 prompt r1, gpt-4.1, public view, on the pilot's Offer public messages, rounds 11-30 (exploratory, pilot data only): `runs/judge/20261024T061901Z_*`, `20261024T061942Z_*`, `20261024T062022Z_*` (119 valid, 1 invalid), `20261024T062226Z_*`; 319 of 320 labels valid; $1.64 estimated, $1.18 actual (ledger rows 151-154).
Counts: `scripts/study1r_label_sets.py` `verify_sets` on the pilot (counts only, no item text read). Simulation: `python scripts/study1r_coding_load.py <4 screener runs> configs/study1r/pilot/campaign.yaml <3 pilot campaign logs>` -> `coding_load.json`.

## Pilot (4.1-low and 4.1-high Offer, 3 episodes each, 240 public messages)

| Quantity | Count |
|---|---|
| Verification set (screener accept 7, conditional_accept 30, no valid label 1) | 38 |
| Screener-negative, detector-flagged | 29 (audit 10%, rounded up: 3) |
| Screener-negative, detector-unflagged | 173 (audit: 50) |
| Verification messages per episode | 8, 0, 1, 22, 7, 0 |

## Main study (66 episodes; simulation, 10,000 runs, seed 20261025)

Two-level resampling (pilot episodes resampled first, for the uncertainty of a 6-episode pilot, then 66 episodes). Labeler B's 20% sample is always coded by Labeler A; all of Labeler A's items in random order; hidden within-episode stopping rule (human message 65); each coded verification message confirmed with probability q, independently. q = 5/7 is gpt-4.1's precision for inclusive acceptance on the 40 validation items (5 of the 7 items it labeled accept or conditional_accept were gold acceptances); 1.0 and 0.5 are bounds. Audit items included (10% of flagged negatives, rounded up, plus 50).

| Labeler A items | Mean | 95% range |
|---|---|---|
| With the stopping rule, q = 5/7 | 211 | 113 to 323 |
| With the stopping rule, q = 1.0 | 201 | 108 to 305 |
| With the stopping rule, q = 0.5 | 227 | 117 to 351 |
| Without the stopping rule (human message 64 estimate) | 499 | 156 to 968 |

Labeler B (20% of the verification set, no stopping rule): about 84 items (15 to 179).

The per-episode count is highly variable (one pilot episode had 22 of the 38 verification messages); confirmation is assumed independent across messages.
