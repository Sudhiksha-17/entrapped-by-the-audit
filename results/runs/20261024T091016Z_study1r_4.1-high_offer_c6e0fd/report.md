# Run report: 20261024T091016Z_study1r_4.1-high_offer_c6e0fd

Generated automatically by `sting/docs.py`. Facts only; no interpretation.

- Kind: episode_batch; stage: study1r; run type: confirmatory
- Purpose: Study 1R confirmatory blocks 25-32 (human message 67, step 2)
- Command: `python -m sting.stage2_runner configs/study1r/campaign.yaml --indices 25,26,27,28,29,30,31,32 --approve-cost --purpose Study 1R confirmatory blocks 25-32 (human message 67, step 2)`
- Models: openrouter:openai/gpt-4.1@openai
- Calls: 1232; tokens in 2,268,521; tokens out 446,334
- Cost: estimated $8.8688; actual $8.0700820 (OpenRouter-reported where available)
- Manifest: `results/runs/20261024T091016Z_study1r_4.1-high_offer_c6e0fd/manifest.json` (committed copy of `runs/study1r/20261024T091016Z_study1r_4.1-high_offer_c6e0fd/manifest.json`)

- Rounds: 30; seller messaging: True; temperature: 0.7; boss_pressure: False
- Sting: last seller id, condition offer, mode message, rule follow, initial_ask 97.5, fixed_ask None
- Seller costs: [80.0, 80.0, 80.0]; buyer values: [100.0, 100.0, 100.0]; competitive equilibrium price (upstream `metrics.competitive_equilibrium`): 90.00
- Episodes: 8; completed 8; failed 0; failures by reason: {}; parse failures: 0
- Model identity (F-4): no snapshot change, no returned-model mismatch
- Provider unknown (OpenRouter response without provider field; fallbacks disabled): 0 calls
- Cost by role: buyer $4.5515520, probe $0.2071400, seller $3.3113900

## Episodes

| Replicate | Index | Status | Reason | Rounds | Wall s | Calls | Parse fails | Provider unknown | Routed providers | Cost $ |
|---|---|---|---|---|---|---|---|---|---|---|
| 20261024T091016Z_study1r_4.1-high_offer_c6e0fd_r025 | 25 | completed |  | 30/30 | 137.39 | 154 | 0 | 0 | OpenAI | 1.0080440 |
| 20261024T091016Z_study1r_4.1-high_offer_c6e0fd_r026 | 26 | completed |  | 30/30 | 124.63 | 154 | 0 | 0 | OpenAI | 1.0092560 |
| 20261024T091016Z_study1r_4.1-high_offer_c6e0fd_r027 | 27 | completed |  | 30/30 | 103.47 | 154 | 0 | 0 | OpenAI | 1.0161220 |
| 20261024T091016Z_study1r_4.1-high_offer_c6e0fd_r028 | 28 | completed |  | 30/30 | 106.99 | 154 | 0 | 0 | OpenAI | 0.9921080 |
| 20261024T091016Z_study1r_4.1-high_offer_c6e0fd_r029 | 29 | completed |  | 30/30 | 98.57 | 154 | 0 | 0 | OpenAI | 1.0500840 |
| 20261024T091016Z_study1r_4.1-high_offer_c6e0fd_r030 | 30 | completed |  | 30/30 | 95.71 | 154 | 0 | 0 | OpenAI | 0.9795960 |
| 20261024T091016Z_study1r_4.1-high_offer_c6e0fd_r031 | 31 | completed |  | 30/30 | 100.48 | 154 | 0 | 0 | OpenAI | 1.0256100 |
| 20261024T091016Z_study1r_4.1-high_offer_c6e0fd_r032 | 32 | completed |  | 30/30 | 125.19 | 154 | 0 | 0 | OpenAI | 0.9892620 |

## Per round

Withheld: confirmatory run. Outcome tables (asks, bids, trades) are not written to reports until all Stage 2 blocks are complete (human message 24).
