# Run report: 20261024T091015Z_study1r_4.1-low_offer_0c5c80

Generated automatically by `sting/docs.py`. Facts only; no interpretation.

- Kind: episode_batch; stage: study1r; run type: confirmatory
- Purpose: Study 1R confirmatory blocks 25-32 (human message 67, step 2)
- Command: `python -m sting.stage2_runner configs/study1r/campaign.yaml --indices 25,26,27,28,29,30,31,32 --approve-cost --purpose Study 1R confirmatory blocks 25-32 (human message 67, step 2)`
- Models: openrouter:openai/gpt-4.1@openai
- Calls: 1232; tokens in 2,737,395; tokens out 444,924
- Cost: estimated $9.9112; actual $8.9942460 (OpenRouter-reported where available)
- Manifest: `results/runs/20261024T091015Z_study1r_4.1-low_offer_0c5c80/manifest.json` (committed copy of `runs/study1r/20261024T091015Z_study1r_4.1-low_offer_0c5c80/manifest.json`)

- Rounds: 30; seller messaging: True; temperature: 0.7; boss_pressure: False
- Sting: last seller id, condition offer, mode message, rule follow, initial_ask 97.5, fixed_ask None
- Seller costs: [80.0, 80.0, 80.0]; buyer values: [100.0, 100.0, 100.0]; competitive equilibrium price (upstream `metrics.competitive_equilibrium`): 90.00
- Episodes: 8; completed 8; failed 0; failures by reason: {}; parse failures: 0
- Model identity (F-4): no snapshot change, no returned-model mismatch
- Provider unknown (OpenRouter response without provider field; fallbacks disabled): 0 calls
- Cost by role: buyer $5.0795840, probe $0.2540720, seller $3.6605900

## Episodes

| Replicate | Index | Status | Reason | Rounds | Wall s | Calls | Parse fails | Provider unknown | Routed providers | Cost $ |
|---|---|---|---|---|---|---|---|---|---|---|
| 20261024T091015Z_study1r_4.1-low_offer_0c5c80_r025 | 25 | completed |  | 30/30 | 116.55 | 154 | 0 | 0 | OpenAI | 1.0547460 |
| 20261024T091015Z_study1r_4.1-low_offer_0c5c80_r026 | 26 | completed |  | 30/30 | 117.15 | 154 | 0 | 0 | OpenAI | 1.0867000 |
| 20261024T091015Z_study1r_4.1-low_offer_0c5c80_r027 | 27 | completed |  | 30/30 | 106.02 | 154 | 0 | 0 | OpenAI | 1.1271320 |
| 20261024T091015Z_study1r_4.1-low_offer_0c5c80_r028 | 28 | completed |  | 30/30 | 102.87 | 154 | 0 | 0 | OpenAI | 1.1449860 |
| 20261024T091015Z_study1r_4.1-low_offer_0c5c80_r029 | 29 | completed |  | 30/30 | 101.89 | 154 | 0 | 0 | OpenAI | 1.1700220 |
| 20261024T091015Z_study1r_4.1-low_offer_0c5c80_r030 | 30 | completed |  | 30/30 | 101.26 | 154 | 0 | 0 | OpenAI | 1.1151000 |
| 20261024T091015Z_study1r_4.1-low_offer_0c5c80_r031 | 31 | completed |  | 30/30 | 107.85 | 154 | 0 | 0 | OpenAI | 1.1325980 |
| 20261024T091015Z_study1r_4.1-low_offer_0c5c80_r032 | 32 | completed |  | 30/30 | 125.92 | 154 | 0 | 0 | OpenAI | 1.1629620 |

## Per round

Withheld: confirmatory run. Outcome tables (asks, bids, trades) are not written to reports until all Stage 2 blocks are complete (human message 24).
