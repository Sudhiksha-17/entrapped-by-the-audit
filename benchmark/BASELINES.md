# Sting Replies: baselines

Scored with `score_judge.py` (reference: adjudicated gold where it exists, otherwise Labeler A). Acceptance = accept or conditional_accept. Exploratory. Judge v1 has no labels on the development items (it was not run on them); empty judge labels are left out of n. Judge v2 pre-screened the main-study verification items (they are its accept or conditional_accept outputs) and the audit items are its negatives, so main-study judge v2 scores reflect that selection.

### judge v1, all fields (gpt-4.1-mini, Study 1 prompt, six text fields) (`judge_v1_allfields_response`)

| Subset | n | Acceptance kappa (95% CI) | Full-label kappa | Precision (k/n) | Recall (k/n) | False-acceptance rate (k/n) |
|---|---|---|---|---|---|---|
| overall | 192 | 0.318 (0.132, 0.499) | 0.063 | 0.433 (13/30) | 0.419 (13/31) | 0.106 (17/161) |
| gold subset | 40 | 0.149 (-0.146, 0.481) | 0.020 | 0.222 (2/9) | 0.400 (2/5) | 0.200 (7/35) |

### judge v1, public message only (same prompt and model; exploratory rerun) (`judge_v1_public_response`)

| Subset | n | Acceptance kappa (95% CI) | Full-label kappa | Precision (k/n) | Recall (k/n) | False-acceptance rate (k/n) |
|---|---|---|---|---|---|---|
| overall | 194 | 0.473 (0.286, 0.640) | 0.041 | 0.652 (15/23) | 0.469 (15/32) | 0.049 (8/162) |
| gold subset | 40 | 0.314 (-0.103, 0.724) | -0.076 | 0.400 (2/5) | 0.400 (2/5) | 0.086 (3/35) |

### judge v2 (gpt-4.1, prompt r1, public view; the main-study screener) (`judge_v2_response`)

| Subset | n | Acceptance kappa (95% CI) | Full-label kappa | Precision (k/n) | Recall (k/n) | False-acceptance rate (k/n) |
|---|---|---|---|---|---|---|
| overall | 213 | 0.488 (0.376, 0.596) | 0.469 | 0.440 (37/84) | 1.000 (37/37) | 0.267 (47/176) |
| gold subset | 40 | 0.805 (0.459, 1.000) | 0.560 | 0.714 (5/7) | 1.000 (5/5) | 0.057 (2/35) |

