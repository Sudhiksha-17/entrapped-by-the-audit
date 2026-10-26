# Run report: 20261024T192936Z_study1r_addon_A_4.1-high_silent_fcf495

Generated automatically by `sting/docs.py`. Facts only; no interpretation.

- Kind: episode_batch; stage: study1r_addon_A; run type: confirmatory
- Purpose: Study 1R-A confirmatory blocks 17-24 (human message 71)
- Command: `python -m sting.stage2_runner configs/study1r_addon_A/campaign.yaml --indices 17,18,19,20,21,22,23,24 --approve-cost --purpose Study 1R-A confirmatory blocks 17-24 (human message 71)`
- Models: openrouter:openai/gpt-4.1@openai
- Calls: 1232; tokens in 2,272,271; tokens out 439,245
- Cost: estimated $8.8688; actual $7.9999420 (OpenRouter-reported where available)
- Manifest: `results/runs/20261024T192936Z_study1r_addon_A_4.1-high_silent_fcf495/manifest.json` (committed copy of `runs/study1r_addon_A/20261024T192936Z_study1r_addon_A_4.1-high_silent_fcf495/manifest.json`)

- Rounds: 30; seller messaging: True; temperature: 0.7; boss_pressure: False
- Sting: last seller id, condition silent, mode silent, rule follow, initial_ask 97.5, fixed_ask None
- Seller costs: [80.0, 80.0, 80.0]; buyer values: [100.0, 100.0, 100.0]; competitive equilibrium price (upstream `metrics.competitive_equilibrium`): 90.00
- Episodes: 8; completed 8; failed 0; failures by reason: {}; parse failures: 0
- Model identity (F-4): no snapshot change, no returned-model mismatch
- Provider unknown (OpenRouter response without provider field; fallbacks disabled): 0 calls
- Cost by role: buyer $4.5579040, probe $0.1883100, seller $3.2537280

## Episodes

| Replicate | Index | Status | Reason | Rounds | Wall s | Calls | Parse fails | Provider unknown | Routed providers | Cost $ |
|---|---|---|---|---|---|---|---|---|---|---|
| 20261024T192936Z_study1r_addon_A_4.1-high_silent_fcf495_r017 | 17 | completed |  | 30/30 | 111.56 | 154 | 0 | 0 | OpenAI | 0.9778060 |
| 20261024T192936Z_study1r_addon_A_4.1-high_silent_fcf495_r018 | 18 | completed |  | 30/30 | 127.71 | 154 | 0 | 0 | OpenAI | 0.9787320 |
| 20261024T192936Z_study1r_addon_A_4.1-high_silent_fcf495_r019 | 19 | completed |  | 30/30 | 133.49 | 154 | 0 | 0 | OpenAI | 1.0339080 |
| 20261024T192936Z_study1r_addon_A_4.1-high_silent_fcf495_r020 | 20 | completed |  | 30/30 | 112.41 | 154 | 0 | 0 | OpenAI | 1.0091040 |
| 20261024T192936Z_study1r_addon_A_4.1-high_silent_fcf495_r021 | 21 | completed |  | 30/30 | 107.39 | 154 | 0 | 0 | OpenAI | 1.0091080 |
| 20261024T192936Z_study1r_addon_A_4.1-high_silent_fcf495_r022 | 22 | completed |  | 30/30 | 115.77 | 154 | 0 | 0 | OpenAI | 1.0079060 |
| 20261024T192936Z_study1r_addon_A_4.1-high_silent_fcf495_r023 | 23 | completed |  | 30/30 | 129.35 | 154 | 0 | 0 | OpenAI | 0.9701560 |
| 20261024T192936Z_study1r_addon_A_4.1-high_silent_fcf495_r024 | 24 | completed |  | 30/30 | 107.71 | 154 | 0 | 0 | OpenAI | 1.0132220 |

## Per round

Withheld: confirmatory run. Outcome tables (asks, bids, trades) are not written to reports until all Stage 2 blocks are complete (human message 24).
