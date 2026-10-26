# Run report: 20261024T082903Z_study1r_4.1-low_offer_0cfd88

Generated automatically by `sting/docs.py`. Facts only; no interpretation.

- Kind: episode_batch; stage: study1r; run type: confirmatory
- Purpose: Study 1R confirmatory blocks 17-24 (human message 67, step 2)
- Command: `python -m sting.stage2_runner configs/study1r/campaign.yaml --indices 17,18,19,20,21,22,23,24 --approve-cost --purpose Study 1R confirmatory blocks 17-24 (human message 67, step 2)`
- Models: openrouter:openai/gpt-4.1@openai
- Calls: 1232; tokens in 2,669,946; tokens out 444,927
- Cost: estimated $9.9112; actual $8.8597560 (OpenRouter-reported where available)
- Manifest: `results/runs/20261024T082903Z_study1r_4.1-low_offer_0cfd88/manifest.json` (committed copy of `runs/study1r/20261024T082903Z_study1r_4.1-low_offer_0cfd88/manifest.json`)

- Rounds: 30; seller messaging: True; temperature: 0.7; boss_pressure: False
- Sting: last seller id, condition offer, mode message, rule follow, initial_ask 97.5, fixed_ask None
- Seller costs: [80.0, 80.0, 80.0]; buyer values: [100.0, 100.0, 100.0]; competitive equilibrium price (upstream `metrics.competitive_equilibrium`): 90.00
- Episodes: 8; completed 8; failed 0; failures by reason: {}; parse failures: 0
- Model identity (F-4): no snapshot change, no returned-model mismatch
- Provider unknown (OpenRouter response without provider field; fallbacks disabled): 0 calls
- Cost by role: buyer $4.9973800, probe $0.2494660, seller $3.6129100

## Episodes

| Replicate | Index | Status | Reason | Rounds | Wall s | Calls | Parse fails | Provider unknown | Routed providers | Cost $ |
|---|---|---|---|---|---|---|---|---|---|---|
| 20261024T082903Z_study1r_4.1-low_offer_0cfd88_r017 | 17 | completed |  | 30/30 | 115.68 | 154 | 0 | 0 | OpenAI | 1.1262800 |
| 20261024T082903Z_study1r_4.1-low_offer_0cfd88_r018 | 18 | completed |  | 30/30 | 107.77 | 154 | 0 | 0 | OpenAI | 1.0700740 |
| 20261024T082903Z_study1r_4.1-low_offer_0cfd88_r019 | 19 | completed |  | 30/30 | 115.29 | 154 | 0 | 0 | OpenAI | 1.0941980 |
| 20261024T082903Z_study1r_4.1-low_offer_0cfd88_r020 | 20 | completed |  | 30/30 | 105.79 | 154 | 0 | 0 | OpenAI | 1.0893140 |
| 20261024T082903Z_study1r_4.1-low_offer_0cfd88_r021 | 21 | completed |  | 30/30 | 99.68 | 154 | 0 | 0 | OpenAI | 1.1635320 |
| 20261024T082903Z_study1r_4.1-low_offer_0cfd88_r022 | 22 | completed |  | 30/30 | 103.06 | 154 | 0 | 0 | OpenAI | 1.0992700 |
| 20261024T082903Z_study1r_4.1-low_offer_0cfd88_r023 | 23 | completed |  | 30/30 | 107.86 | 154 | 0 | 0 | OpenAI | 1.1236280 |
| 20261024T082903Z_study1r_4.1-low_offer_0cfd88_r024 | 24 | completed |  | 30/30 | 98.2 | 154 | 0 | 0 | OpenAI | 1.0934600 |

## Per round

Withheld: confirmatory run. Outcome tables (asks, bids, trades) are not written to reports until all Stage 2 blocks are complete (human message 24).
