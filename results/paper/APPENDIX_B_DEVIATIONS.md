# Appendix B. Deviations, clarifications and disclosed changes

Compiled 2026-10-25 (human message 82 step 5) from `notes/PREREG_DEVIATIONS.md`, `notes/DECISIONS.md`, `notes/ISSUES.md`, `prereg_study1r/PREREG.md` section 15, `prereg_study1r/WRITEUP_NOTES.md`, `prereg_study1r/AMENDMENT_1RC.md` and the results files named below. Facts only. "Post-freeze deviation" = a change to a preregistered procedure after its freeze. Changes made before a freeze are listed separately (B.3) because the preregistration discloses them. Exploratory additions are not deviations; they are listed in B.6 so that every analysis outside the preregistrations is accounted for.

Freezes: Study 1 `prereg/FROZEN.json` at `40d93a9` (2026-10-21); Study 1R and Study 1R-A `prereg_study1r/FROZEN.json` at `a1a7dd6` (2026-10-24, 47 files); Study 1R-C `prereg_study1r/FROZEN_1RC.json` at `1d5ec25` (2026-10-25, 12 files). No frozen file was edited after its freeze; every `verify` passes.

## B.1 Study 1

| Id | Type | What | Reason | Record |
|---|---|---|---|---|
| DEV-1 | Post-freeze deviation | Supplementary judge validation sample: 30 seller-rounds, all round 11 (24 Offer, 6 per cell; 2 directive, 2 anchor, 1 sham, 1 rapport), random by script (seed 20261025), same blind procedure; kappa rule (0.6) applied to it; the original sample reported as non-informative. Recorded and committed before the sample was generated. | The frozen validation sample had 0 positives because Seller C's message is visible only in the round-11 prompt (I-043), so kappa against it was undefined. | `notes/PREREG_DEVIATIONS.md` DEV-1; D-088 (the human's message calls it "Deviation D-087"); implementation D-089 (one overlapping item excluded; order seed "20261025-order"); approved (human messages 28, 29) |
| C-1 | Clarification, not a deviation | Seller C's message appears in the seller prompt in round 11 only; later-round labels depend on the sellers' own memory and scratchpad. The judge stays as frozen (rounds 11-30). | Upstream shows other sellers' messages from the previous hour; the Study 1 sting posts once, in round 10. | `notes/PREREG_DEVIATIONS.md` C-1; I-043; `results/stage2/label_audit.md` |
| N-1 | Note | The original 30-item sample was labeled with the shorter label-tool wording; the human states LABELING_GUIDE.md was open and matched the judge prompt on three points. LABELING_GUIDE.md is not in the repository. | Record of the labeling conditions. | `notes/PREREG_DEVIATIONS.md` N-1; I-042 |
| N-2 | Note | Labeler decision rule on the supplementary sample: engaged only with an explicit reference to Seller C's message or proposal. Recorded after the supplementary labels were committed (`7dc39c3`) and before any judge output existed. | Record of the labeling rule. | `notes/PREREG_DEVIATIONS.md` N-2 (Appendix C, C.5.3) |
| Fallback | Pre-specified, not a deviation | T2a computed on the behavioral flag because supplementary-sample kappa for `response` was 0.097 < 0.6; every judge-based measure exploratory. | Preregistered fallback (`prereg/PREREG.md` T2a fallback). | `results/stage2/RESULTS.md`; `results/stage2/judge_validation.md` |
| D-092 | Implementation readings | Compression computed with the fallback T2a; T2a secondary contrasts on the fallback flag; sensitivity thresholds and carry-forward applied as listed; per-arm bootstrap CIs; no frozen analysis function changed. | Readings needed to run the frozen functions after the fallback. | D-092 (proposal status in DECISIONS) |

## B.2 Study 1R (main study) and Study 1R-A, after the freeze

| Id | Type | What | Reason | Record |
|---|---|---|---|---|
| D-116 (I-056) | Post-freeze deviation (bug fix) | Analysis run through an unfrozen wrapper, `scripts/study1r_results_completed.py`, that passes only completed episodes to the frozen analysis (unchanged) and stops unless the excluded set equals the expected one. Excluded: main study `mini-low_anchor_a761c2_r028` (failed; completed replacement `_r028_repl1`); Study 1R-A none; Study 1R-C none. | The frozen `scripts/study1r_results.py` did not apply the preregistered rule that failed episodes are excluded and replaced (PREREG section 11) and crashed on the failed episode (X not set). | D-116 (approved, option 2); I-056; `results/study1r/RESULTS.md` "Excluded episodes" |
| I-060 | Fix to the wrapper (no change in results) | Shorter staging directory names in the wrapper. Main-study results reproduced exactly with the changed wrapper. | Windows path-length failure while staging the Study 1R-A runs; no analysis had run. | I-060 |
| I-055 | Preregistered replacement, not a deviation | One main-study episode (mini-low Anchor r028) failed in round 5 in upstream market code (a buyer bid arrived as a string) and was replaced at the same index. Arm failure rate 1/60. | Preregistered replacement rule. | I-055 |
| D-117 (I-057) | Post hoc addition to the report | Screener precision reported on Labeler B's random 20% sample (never dropped by the stopping rule), labeled exploratory, post hoc. In the write-up, the frozen miss audit's "coded" count of 162 is described as 81 coded by Labeler A plus 81 dropped by the stopping rule. | The frozen `miss_rates` docstring promises verification precision, but the function does not return it, and its "coded" count includes dropped messages. | D-117 (approved, human message 71); I-057 and update |
| I-058 | Output excluded from the write-up | The frozen report's "Study 1R-A add-on" section, run on the main study with no add-on episodes, printed a propensity value (33/33) computed from main-study 4.1-high Silent episodes. It is not Study 1R-A data and is excluded. | Behaviour of a frozen report section. | I-058 and update (human message 71) |
| I-054 | Run mechanics, not a deviation | The unattended driver launched a chunk while run docs were uncommitted; the runner refused; no episode was attempted. The driver then committed between chunks. | Confirmatory runner refuses an uncommitted tree. | I-054 |

Study 1R-A: run as preregistered (PREREG section 14), 66 of 66 episodes completed, 0 excluded; analysed through the same wrapper (D-116). No other deviation (`results/study1r/RESULTS_1RA.md`).

## B.3 Study 1R changes before the freeze (disclosed in PREREG section 15; not deviations)

| Change | Record |
|---|---|
| Pilot gate G1 failed (3 of 8 Offer episodes engaged in rounds 11-13); the verbal window was revised to rounds 11-30 and conditional acceptance added (measurement only; no stimulus change). | W-2; D-097; I-047 |
| Validation pass 2 gap reduced to at least 3 hours (from 12). | W-3; D-098 |
| Validation pass 2 was labeled by a second, independent labeler (Labeler B), not by the entrant; the record was corrected before any judge output on the validation items. | W-4, W-5; D-103 |
| Judge v2 prompt aligned with the labeling guide (r0) and revised twice (r1, r2); r1 selected. Gate G3 failed for both candidates; no judge frozen as a measure. | W-7; D-100, D-104; Appendix C, C.4 |
| Human coding revised twice before any main-study data: a detector-based procedure (D-105), then option A with judge v2 r1 as screener and human verification of screener positives (D-106). | W-8, W-9 |
| Probe wording fixed (plain-text prefix; new Q2), Q1 shortened, Q1 max_tokens raised to 400. | D-107, D-112; I-051 |
| Holm family reduced from seven to five contrasts. | D-108 |
| Freeze extended to the Study 1R code and its import closure; hidden within-episode stopping rule added to option A (strict acceptance and related measures are lower bounds); analysis refuses to run until the human coding is committed. | W-10; D-110, D-111, D-113; I-053 |

## B.4 Study 1R-C

- Preregistered as an add-on by amendment (`prereg_study1r/AMENDMENT_1RC.md`), frozen in a separate lock at `1d5ec25`; the Study 1R lock was re-verified, not changed.
- **Disclosure (amendment section 9):** the amendment was written after the Study 1R and Study 1R-A results were known. `NUMBERS_FOR_PAPER.md` section 7.5 records the timing: drafted about 9 hours 25 minutes after the main results were first computed.
- **Changes approved before the freeze (human message 81):** the stability check (1R-C Silent minus main-study Silent per cell, descriptive) was added. The D-125 verdict rule was set: a pricing effect is reported as present only if the bootstrap 95% CI excludes zero and the Holm-adjusted permutation p is below 0.05.
- **Implementation:** a subclass and a monkeypatching installer in `sting/study1rc.py` (D-125). No frozen file changed. The frozen Study 1R runner refuses the 1R-C campaign.
- **Run:** 132 of 132 episodes completed; 0 failed, 0 replacements, 0 excluded; every G2 check passed; no stop condition fired.
- **Post-freeze deviations:** none.

## B.5 Write-up notes that affect reported numbers

| Item | Record |
|---|---|
| Strict acceptance, the rounds 11-12 window, aware acceptance and acceptance by round are lower bounds because of the hidden stopping rule. | W-10; D-111 |
| The first confirmed acceptance round can be later than the first acceptance, because earlier screener positives may have been dropped uncoded. In 7 of 12 4.1-high accepting episodes, an earlier verification message was dropped. | `NUMBERS_FOR_PAPER.md` section 5 |
| The I-058 propensity value (33/33) in `results/study1r/RESULTS.md` is excluded. | I-058 |

## B.6 Exploratory and post hoc analyses (labeled as such; not deviations)

| Analysis | Decision | Output |
|---|---|---|
| Study 1 engagement diagnostic and other-agent awareness scan | D-094, D-099 | `results/study1_diagnostics/` |
| Judge v1 and v2 comparison (headline figure) | PREREG section 8 (exploratory) | `results/study1r/results.json`; Figure 1 |
| Screener precision on Labeler B's sample | D-117 | `results/study1r/RESULTS.md` |
| Suspicion cues: keyword categories and the Q1 human check | D-119, D-121 | `results/study1r/exploratory/suspicion/` |
| 4.1-high price levels by confirmed acceptance; price-path figure | D-120, D-122 | `results/study1r/exploratory/price_by_acceptance/`; Figure 3 |
| Scale, propensity, agreement, miss audit details, paired sensitivity, engagement | D-124 | `results/study1r/exploratory/posthoc_m78/` |
| Facts for the paper (requests vs headroom, kappa and precision, buyers) | human message 80 | `NUMBERS_FOR_PAPER.md` section 7 |
| Random-round reference with n = 9 episodes per resample | human message 81 | `results/study1r/exploratory/reference_n9/` |
| Plan B (private-plan sincerity): coding pending | plan `1e32de1`; D-126 | `results/study1r/labeling/plan_b/` |
| Plan C (cheap talk) | plan `1e32de1`; D-126, D-127 | `results/study1r/exploratory/plan_c/` |
| Final figures with the Study 1R-C rows added to Figures 2 and 4 | D-128 | `results/study1r/figures/final/` |

## B.7 Study 1R-D (added 2026-10-25, human message 89)

Lock `prereg_study1r/FROZEN_1RD.json` (frozen 2026-10-25T21:32:26Z at `7c34bed`, 13 files: amendment, campaign, 5 arm configs, code). The fresh Cell B has its own lock, `prereg_study1r/FROZEN_1RD_B2.json` (2026-10-25T23:30:13Z at `e419811`, 8 files), which also records the SHA-256 of FROZEN.json, FROZEN_1RC.json and FROZEN_1RD.json. Neither lock was edited after its freeze; every run verified all locks.

### Changes made before the freeze (recorded in the amendment)

| Change | Record |
|---|---|
| **Run mechanics:** parallel invocations over disjoint index ranges (Cell B: 5 invocations, all three arms of an index together; Cell A: its own invocations); launch from a clean git worktree because the main tree held the uncommitted human coding; 22:00 cutoff changed to 00:00. | AMENDMENT_1RD.md section 7; D-133; human message 87 |

### Post-freeze readings of frozen checks (approved)

| Id | Frozen check | Reading | Evidence | Approval |
|---|---|---|---|---|
| D-134 (extended) | `scripts/study1r_checkpoint.py` adds an identity issue whenever a call's routed provider is not "OpenAI" (written for Study 1R; I-065). | A call routed to the deliberately pinned provider is not a provider mismatch. Every other identity check (provider_unknown, returned model, provider_mismatch failure, snapshot change, identity flag) applies. | First Cell B block 0: 3 episodes, each "routed {'DeepInfra': 154}". Fresh Cell B block 0: 3 episodes, each "routed {'Parasail': 154}". No other identity issue. The runner pins the provider with fallbacks disabled and fails any call served elsewhere. | D-134 (DeepInfra) proposal; extended to Parasail and approved, human message 89 |
| D-137 (supersedes the block-22-only D-135) | The block-cost condition compares each block's cost (replacement episodes excluded) with block 0's cost for the same arms; a deviation above 25% stops. | A flag is not a stop when the crashed episode's replacement completed and the block cost, recomputed with the replacement, is within 25% of block 0. Any other flag stops. | **Block 22** (Cell A): Offer-floor `..._f286fa_r022` failed in round 3 (upstream string-bid TypeError, as I-055; $0.0188); replacement `_r022_repl1` completed ($0.2303); block counted $0.2500 vs $0.4578 (-45%); recomputed $0.4616 (+0.8%). **Block 32** (Cell A): Silent-floor `..._4e4b60_r032` failed in round 3 (same TypeError; $0.0189); replacement `_r032_repl1` completed ($0.2259); block counted $0.2489 vs $0.4578; recomputed $0.4560 (-0.4%). | D-135 (block 22) approved, human message 88; D-137 approved as a general rule, human message 89 |

### Cell B on DeepInfra stopped; fresh Cell B on Parasail

| Event | Record |
|---|---|
| DeepInfra rate limits (HTTP 429) from about 18:00: 10 Qwen episodes completed, 18 failed (`api_failure`), meeting the preregistered stop condition "failure rate above 10%". Two invocations stopped on 3 consecutive API failures; the other three were terminated by hand at 18:32. The checkpoints did not show the failures, because aborted invocations do not finalize their campaign logs. The 28 episodes are excluded and not analysed. | I-066; human message 88 |
| Provider speed test (exploratory, index 2000, DeepInfra excluded; rule recorded first in addendum 1): Parasail 4.9 min, 0 errors; Venice 12.0 min, 0 errors; GMICloud failed (503); Google Vertex failed (404). Parasail selected by the rule. | AMENDMENT_1RD_ADDENDUM_1.md; D-136 |
| Fresh Cell B (Silent, Silent-floor, Offer-floor; N = 33; indices 0-32) on Parasail, same model and settings; re-frozen; block 0 gate passed. Run with 3 parallel invocations; hard cutoff 02:00. | addendum 1; human messages 88 and 89 |

### Other post-freeze records

| Id | What | Status |
|---|---|---|
| I-064 | Screening run directory paths over the Windows path limit (before any call); short run names. | resolved before the freeze |
| I-068 | `AMENDMENT_1RD.md` was edited after the freeze by mistake (`9d2d643`) and restored byte for byte in the next commit before any run; the text went to addendum 1. | resolved |
| I-069 | Second upstream crash in Cell A (block 32); read under D-137. | resolved by D-137 |
| I-070 | Fresh Cell B on Parasail stopped at 19:42 by the preregistered failure-rate condition: 6 episodes failed (HTTP 429) and 3 completed (block 0). The 429 responses say OpenRouter limits the model to 18 requests per minute on this account (`openrouter_shared_capacity`), whatever the provider, which allows about 7 episodes per hour. Cell B cannot finish by the 02:00 cutoff and is reported as incomplete and not analysed. | open; Cell B not run further (human message 88 rule) |
| I-071 | Cell A chunk 33-40 was terminated by the run driver when the Cell B stop fired (driver flaw; Cell A's own checks were clean). Its 2 completed index-33 episodes are in no finished campaign log and are not analysed; Cell A restarted at index 33. | resolved |
