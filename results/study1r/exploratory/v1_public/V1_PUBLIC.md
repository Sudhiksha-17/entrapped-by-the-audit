# Judge v1 on public messages only (EXPLORATORY robustness check)

Human message 93, item 3. Frozen Study 1 judge (prompt, gpt-4.1-mini, temperature 0); only the input fields changed (public message only; the five private fields empty). Completed Offer episodes; an episode counts as accepting if any seller-round in rounds 11-30 is labeled `accept`. Wilson 95% CIs. Script `scripts/study1r_judge_v1_public_results.py`. Facts only.

Invalid judge outputs: all fields 69, public only 11 (of 5,040 seller-rounds each).

| Group | N Offer episodes | All fields | Public message only |
|---|---|---|---|
| mini group (gpt-4.1-mini, default) | 60 | 37/60 = 0.617 (0.490, 0.729) | 26/60 = 0.433 (0.316, 0.559) |
| volume group (gpt-4.1, volume prompt) | 33 | 5/33 = 0.152 (0.067, 0.309) | 14/33 = 0.424 (0.272, 0.592) |
| CEO group (gpt-4.1, CEO prompt) | 33 | 32/33 = 0.970 (0.847, 0.995) | 27/33 = 0.818 (0.656, 0.914) |

## Validation items (40), against the adjudicated gold

Kappa with percentile bootstrap 95% CI over items. Judge v1's label set has no not_applicable and no conditional_accept; the gold has 10 not_applicable items (Sham).

| View | n | Invalid | Full-label kappa (95% CI) | Acceptance kappa (95% CI) | Judge accept | Gold acceptances |
|---|---|---|---|---|---|---|
| all fields | 40 | 0 | 0.020 (-0.064, 0.104) | 0.149 (-0.158, 0.483) | 9 | 5 |
| public only | 40 | 0 | -0.076 (-0.183, 0.034) | 0.314 (-0.103, 0.722) | 5 | 5 |
