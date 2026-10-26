# Appendix F. The entrapment test, step by step

I run three steps in this order. Each step names what I run, what I measure, what I treat as a warning sign, and the release files that support it. The example numbers come from `results/study1r/NUMBERS_FOR_PAPER.md`.

## Step one. Check the record

**What I run.** I take the reader that will decide whether an agent accepted the sting, whether a judge model or a keyword rule, and I run it on the Sting Replies benchmark (`benchmark/sting_replies.csv`). I save its labels as a file with the columns message_id and response.

**What I measure.** I score those labels with `benchmark/score_judge.py` against the human labels. It reports agreement on acceptance (Cohen's kappa), precision and recall on acceptance, and the false-acceptance rate, overall and on the gold subset. I also compare readers on the same episodes.

**Warning signs.** I suggest two thresholds, agreement on acceptance below a kappa of 0.6 and a false-acceptance rate above 0.10. My preregistered gate required a kappa of at least 0.6 on the full six-category response label. Readers that disagree on the same episodes are also a warning sign.

**Release files.** `benchmark/README.md`, `benchmark/sting_replies.csv`, `benchmark/score_judge.py`, `benchmark/BASELINES.md`, and `scripts/final_part2.py` for the reader comparison per group.

## Step two. Measure predisposition

**What I run.** I run sting-free episodes, a Silent arm in which the scripted seller posts no message and prices by the follow rule, in the same market, with the same models and prompts as the sting episodes.

**What I measure.** The share of sting-free episodes whose mean LLM-seller ask over rounds 11-30 is above the supracompetitive threshold of $92.70, which I call the sting-free propensity. It is the reference for each group. I put next to it the share of sting episodes that the reader counts as accepting, the increase the offer asks for in each group, and the number of asks before each acceptance.

**Warning signs.** (a) Acceptance in a group whose sting-free propensity is low. Judge v1 counted 37 of 60 mini-group Offer episodes as accepting, while that group priced above $92.70 in 1 of 33 sting-free episodes. (b) An offer that asks groups for different increases. My offer asked the CEO group for $1.63 and the volume group for $7.18 on average, so I match the requested increase across groups. (c) Acceptance that appears only after many repeated asks, so I record the number of asks before each acceptance.

**Release files.** `configs/study1r/mini-low_silent.yaml`, `configs/study1r/4.1-low_silent.yaml` and `configs/study1r/4.1-high_silent.yaml`, run with `python -m sting.stage2_runner`. The propensity per arm comes from `scripts/study1r_results_completed.py`. The comparison with each reader and the asks before acceptance come from `scripts/final_part2.py`. The requested increase is X minus pre, the column jump in `results_per_episode/`.

## Step three. Test inducement

**What I run.** I run two concurrent comparisons that hold the scripted seller's prices fixed. The price-only control compares a silent seller that prices at the offered level, max(X, follow), with a silent seller that only follows. The words-only test compares a seller that posts the offer messages and prices at the offered level with a silent seller that prices the same way.

**What I measure.** The change in the LLM sellers' mean ask from rounds 6-9 to rounds 11-30, the change score, for each arm. I report each difference with a bootstrap 95% confidence interval.

**Warning signs.** A price-only control effect, meaning the sting's own pricing moves prices. An offer effect no larger than the price-only effect cannot be attributed to the offer. In my study the price-only control raised the mini group's change score by 0.82 dollars (95% CI 0.24 to 1.47), and the words-only test differed by 0.04 dollars (95% CI −0.44 to 0.48).

**Release files.** `sting/study1rc.py` and `configs/study1r_addon_C/` for the price-only control, `sting/study1rd.py` and `configs/study1r_addon_D/` for the words-only test, and `scripts/study1r_results_1rc.py` and `scripts/study1r_results_1rd_run.py` for the analyses. `prereg_study1r/AMENDMENT_1RC.md` and `prereg_study1r/AMENDMENT_1RD.md` give the designs.
