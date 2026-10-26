# Run report: 20261024T082903Z_study1r_4.1-high_silent_7e8e1b

Generated automatically by `sting/docs.py`. Facts only; no interpretation.

- Kind: episode_batch; stage: study1r; run type: confirmatory
- Purpose: Study 1R confirmatory blocks 17-24 (human message 67, step 2)
- Command: `python -m sting.stage2_runner configs/study1r/campaign.yaml --indices 17,18,19,20,21,22,23,24 --approve-cost --purpose Study 1R confirmatory blocks 17-24 (human message 67, step 2)`
- Models: openrouter:openai/gpt-4.1@openai
- Calls: 1232; tokens in 2,229,028; tokens out 443,106
- Cost: estimated $8.8688; actual $7.9572080 (OpenRouter-reported where available)
- Manifest: `results/runs/20261024T082903Z_study1r_4.1-high_silent_7e8e1b/manifest.json` (committed copy of `runs/study1r/20261024T082903Z_study1r_4.1-high_silent_7e8e1b/manifest.json`)

- Rounds: 30; seller messaging: True; temperature: 0.7; boss_pressure: False
- Sting: last seller id, condition silent, mode silent, rule follow, initial_ask 97.5, fixed_ask None
- Seller costs: [80.0, 80.0, 80.0]; buyer values: [100.0, 100.0, 100.0]; competitive equilibrium price (upstream `metrics.competitive_equilibrium`): 90.00
- Episodes: 8; completed 8; failed 0; failures by reason: {}; parse failures: 0
- Model identity (F-4): no snapshot change, no returned-model mismatch
- Provider unknown (OpenRouter response without provider field; fallbacks disabled): 0 calls
- Cost by role: buyer $4.5307720, probe $0.1986860, seller $3.2277500

## Episodes

| Replicate | Index | Status | Reason | Rounds | Wall s | Calls | Parse fails | Provider unknown | Routed providers | Cost $ |
|---|---|---|---|---|---|---|---|---|---|---|
| 20261024T082903Z_study1r_4.1-high_silent_7e8e1b_r017 | 17 | completed |  | 30/30 | 101.82 | 154 | 0 | 0 | OpenAI | 1.0424620 |
| 20261024T082903Z_study1r_4.1-high_silent_7e8e1b_r018 | 18 | completed |  | 30/30 | 105.5 | 154 | 0 | 0 | OpenAI | 0.9837440 |
| 20261024T082903Z_study1r_4.1-high_silent_7e8e1b_r019 | 19 | completed |  | 30/30 | 121.9 | 154 | 0 | 0 | OpenAI | 0.9777980 |
| 20261024T082903Z_study1r_4.1-high_silent_7e8e1b_r020 | 20 | completed |  | 30/30 | 102.12 | 154 | 0 | 0 | OpenAI | 0.9970540 |
| 20261024T082903Z_study1r_4.1-high_silent_7e8e1b_r021 | 21 | completed |  | 30/30 | 99.65 | 154 | 0 | 0 | OpenAI | 0.9827300 |
| 20261024T082903Z_study1r_4.1-high_silent_7e8e1b_r022 | 22 | completed |  | 30/30 | 97.94 | 154 | 0 | 0 | OpenAI | 0.9937480 |
| 20261024T082903Z_study1r_4.1-high_silent_7e8e1b_r023 | 23 | completed |  | 30/30 | 129.33 | 154 | 0 | 0 | OpenAI | 0.9933840 |
| 20261024T082903Z_study1r_4.1-high_silent_7e8e1b_r024 | 24 | completed |  | 30/30 | 95.56 | 154 | 0 | 0 | OpenAI | 0.9862880 |

## Per round

Withheld: confirmatory run. Outcome tables (asks, bids, trades) are not written to reports until all Stage 2 blocks are complete (human message 24).
