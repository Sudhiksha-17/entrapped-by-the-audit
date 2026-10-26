# Part 2(c) hand-check agreement (exploratory, post hoc)

30 sentences (random, seed 20261025) from the classified private-note sentences mentioning Seller C; keyword classification vs the human's marks (committed file, hash in D-142; marked blind to the classification with `scripts/handcheck_tool.py`). Kappa: percentile bootstrap 95% CI over sentences (10,000 resamples, seed 20261025). Precision and recall of the keyword rule against the human marks: Wilson 95% CIs. Script `scripts/final_part2_handcheck.py`.

| Type | Raw agreement | Kappa (95% CI) | Keyword yes / human yes | Keyword yes, human no | Keyword no, human yes | Precision (k/n, 95% CI) | Recall (k/n, 95% CI) |
|---|---|---|---|---|---|---|---|
| price-related | 0.967 | 0.000 (0.000, 1.000) | 29 / 30 | 0 | 1 | 1.000 (29/29, 0.883-1.000) | 0.967 (29/30, 0.833-0.994) |
| message-related | 0.900 | 0.516 (-0.059, 1.000) | 3 / 4 | 1 | 2 | 0.667 (2/3, 0.208-0.939) | 0.500 (2/4, 0.150-0.850) |

Note: the human marked all 30 sentences price-related (no 'no' marks), so Cohen's kappa for price-related is 0 by construction (expected agreement equals observed agreement, 29/30) and its bootstrap interval is not informative; raw agreement, precision and recall are the informative figures for that type.
