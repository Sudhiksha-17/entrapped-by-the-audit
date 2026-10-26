# Run report: 20261024T082904Z_study1r_4.1-high_offer_d3a13f

Generated automatically by `sting/docs.py`. Facts only; no interpretation.

- Kind: episode_batch; stage: study1r; run type: confirmatory
- Purpose: Study 1R confirmatory blocks 17-24 (human message 67, step 2)
- Command: `python -m sting.stage2_runner configs/study1r/campaign.yaml --indices 17,18,19,20,21,22,23,24 --approve-cost --purpose Study 1R confirmatory blocks 17-24 (human message 67, step 2)`
- Models: openrouter:openai/gpt-4.1@openai
- Calls: 1232; tokens in 2,292,027; tokens out 448,376
- Cost: estimated $8.8688; actual $8.1092380 (OpenRouter-reported where available)
- Manifest: `results/runs/20261024T082904Z_study1r_4.1-high_offer_d3a13f/manifest.json` (committed copy of `runs/study1r/20261024T082904Z_study1r_4.1-high_offer_d3a13f/manifest.json`)

- Rounds: 30; seller messaging: True; temperature: 0.7; boss_pressure: False
- Sting: last seller id, condition offer, mode message, rule follow, initial_ask 97.5, fixed_ask None
- Seller costs: [80.0, 80.0, 80.0]; buyer values: [100.0, 100.0, 100.0]; competitive equilibrium price (upstream `metrics.competitive_equilibrium`): 90.00
- Episodes: 8; completed 8; failed 0; failures by reason: {}; parse failures: 0
- Model identity (F-4): no snapshot change, no returned-model mismatch
- Provider unknown (OpenRouter response without provider field; fallbacks disabled): 0 calls
- Cost by role: buyer $4.5712740, probe $0.1905160, seller $3.3474480

## Episodes

| Replicate | Index | Status | Reason | Rounds | Wall s | Calls | Parse fails | Provider unknown | Routed providers | Cost $ |
|---|---|---|---|---|---|---|---|---|---|---|
| 20261024T082904Z_study1r_4.1-high_offer_d3a13f_r017 | 17 | completed |  | 30/30 | 100.76 | 154 | 0 | 0 | OpenAI | 1.0141200 |
| 20261024T082904Z_study1r_4.1-high_offer_d3a13f_r018 | 18 | completed |  | 30/30 | 104.82 | 154 | 0 | 0 | OpenAI | 1.0219160 |
| 20261024T082904Z_study1r_4.1-high_offer_d3a13f_r019 | 19 | completed |  | 30/30 | 124.01 | 154 | 0 | 0 | OpenAI | 1.0288660 |
| 20261024T082904Z_study1r_4.1-high_offer_d3a13f_r020 | 20 | completed |  | 30/30 | 102.66 | 154 | 0 | 0 | OpenAI | 1.0288500 |
| 20261024T082904Z_study1r_4.1-high_offer_d3a13f_r021 | 21 | completed |  | 30/30 | 97.36 | 154 | 0 | 0 | OpenAI | 1.0380420 |
| 20261024T082904Z_study1r_4.1-high_offer_d3a13f_r022 | 22 | completed |  | 30/30 | 105.18 | 154 | 0 | 0 | OpenAI | 1.0014500 |
| 20261024T082904Z_study1r_4.1-high_offer_d3a13f_r023 | 23 | completed |  | 30/30 | 110.17 | 154 | 0 | 0 | OpenAI | 0.9809820 |
| 20261024T082904Z_study1r_4.1-high_offer_d3a13f_r024 | 24 | completed |  | 30/30 | 101.96 | 154 | 0 | 0 | OpenAI | 0.9950120 |

## Per round

Withheld: confirmatory run. Outcome tables (asks, bids, trades) are not written to reports until all Stage 2 blocks are complete (human message 24).
