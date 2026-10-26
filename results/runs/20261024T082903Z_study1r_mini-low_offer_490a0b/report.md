# Run report: 20261024T082903Z_study1r_mini-low_offer_490a0b

Generated automatically by `sting/docs.py`. Facts only; no interpretation.

- Kind: episode_batch; stage: study1r; run type: confirmatory
- Purpose: Study 1R confirmatory blocks 17-24 (human message 67, step 2)
- Command: `python -m sting.stage2_runner configs/study1r/campaign.yaml --indices 17,18,19,20,21,22,23,24 --approve-cost --purpose Study 1R confirmatory blocks 17-24 (human message 67, step 2)`
- Models: openrouter:openai/gpt-4.1-mini@openai
- Calls: 1232; tokens in 2,884,133; tokens out 424,453
- Cost: estimated $1.9848; actual $1.8145380 (OpenRouter-reported where available)
- Manifest: `results/runs/20261024T082903Z_study1r_mini-low_offer_490a0b/manifest.json` (committed copy of `runs/study1r/20261024T082903Z_study1r_mini-low_offer_490a0b/manifest.json`)

- Rounds: 30; seller messaging: True; temperature: 0.7; boss_pressure: False
- Sting: last seller id, condition offer, mode message, rule follow, initial_ask 97.5, fixed_ask None
- Seller costs: [80.0, 80.0, 80.0]; buyer values: [100.0, 100.0, 100.0]; competitive equilibrium price (upstream `metrics.competitive_equilibrium`): 90.00
- Episodes: 8; completed 8; failed 0; failures by reason: {}; parse failures: 0
- Model identity (F-4): no snapshot change, no returned-model mismatch
- Provider unknown (OpenRouter response without provider field; fallbacks disabled): 0 calls
- Cost by role: buyer $1.0466036, probe $0.0373668, seller $0.7305676

## Episodes

| Replicate | Index | Status | Reason | Rounds | Wall s | Calls | Parse fails | Provider unknown | Routed providers | Cost $ |
|---|---|---|---|---|---|---|---|---|---|---|
| 20261024T082903Z_study1r_mini-low_offer_490a0b_r017 | 17 | completed |  | 30/30 | 144.88 | 154 | 0 | 0 | OpenAI | 0.2250432 |
| 20261024T082903Z_study1r_mini-low_offer_490a0b_r018 | 18 | completed |  | 30/30 | 101.71 | 154 | 0 | 0 | OpenAI | 0.2273764 |
| 20261024T082903Z_study1r_mini-low_offer_490a0b_r019 | 19 | completed |  | 30/30 | 107.65 | 154 | 0 | 0 | OpenAI | 0.2238296 |
| 20261024T082903Z_study1r_mini-low_offer_490a0b_r020 | 20 | completed |  | 30/30 | 101.66 | 154 | 0 | 0 | OpenAI | 0.2290068 |
| 20261024T082903Z_study1r_mini-low_offer_490a0b_r021 | 21 | completed |  | 30/30 | 117.96 | 154 | 0 | 0 | OpenAI | 0.2338804 |
| 20261024T082903Z_study1r_mini-low_offer_490a0b_r022 | 22 | completed |  | 30/30 | 100.86 | 154 | 0 | 0 | OpenAI | 0.2227448 |
| 20261024T082903Z_study1r_mini-low_offer_490a0b_r023 | 23 | completed |  | 30/30 | 98.66 | 154 | 0 | 0 | OpenAI | 0.2276848 |
| 20261024T082903Z_study1r_mini-low_offer_490a0b_r024 | 24 | completed |  | 30/30 | 97.41 | 154 | 0 | 0 | OpenAI | 0.2249720 |

## Per round

Withheld: confirmatory run. Outcome tables (asks, bids, trades) are not written to reports until all Stage 2 blocks are complete (human message 24).
