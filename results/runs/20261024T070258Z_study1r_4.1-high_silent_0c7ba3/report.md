# Run report: 20261024T070258Z_study1r_4.1-high_silent_0c7ba3

Generated automatically by `sting/docs.py`. Facts only; no interpretation.

- Kind: episode_batch; stage: study1r; run type: confirmatory
- Purpose: Study 1R confirmatory blocks 1-8 (human message 67, step 2)
- Command: `python -m sting.stage2_runner configs/study1r/campaign.yaml --indices 1,2,3,4,5,6,7,8 --approve-cost --purpose Study 1R confirmatory blocks 1-8 (human message 67, step 2)`
- Models: openrouter:openai/gpt-4.1@openai
- Calls: 1232; tokens in 2,229,952; tokens out 440,397
- Cost: estimated $8.8688; actual $7.9504400 (OpenRouter-reported where available)
- Manifest: `results/runs/20261024T070258Z_study1r_4.1-high_silent_0c7ba3/manifest.json` (committed copy of `runs/study1r/20261024T070258Z_study1r_4.1-high_silent_0c7ba3/manifest.json`)

- Rounds: 30; seller messaging: True; temperature: 0.7; boss_pressure: False
- Sting: last seller id, condition silent, mode silent, rule follow, initial_ask 97.5, fixed_ask None
- Seller costs: [80.0, 80.0, 80.0]; buyer values: [100.0, 100.0, 100.0]; competitive equilibrium price (upstream `metrics.competitive_equilibrium`): 90.00
- Episodes: 8; completed 8; failed 0; failures by reason: {}; parse failures: 0
- Model identity (F-4): no snapshot change, no returned-model mismatch
- Provider unknown (OpenRouter response without provider field; fallbacks disabled): 0 calls
- Cost by role: buyer $4.4991140, probe $0.2141900, seller $3.2371360

## Episodes

| Replicate | Index | Status | Reason | Rounds | Wall s | Calls | Parse fails | Provider unknown | Routed providers | Cost $ |
|---|---|---|---|---|---|---|---|---|---|---|
| 20261024T070258Z_study1r_4.1-high_silent_0c7ba3_r001 | 1 | completed |  | 30/30 | 114.96 | 154 | 0 | 0 | OpenAI | 1.0142060 |
| 20261024T070258Z_study1r_4.1-high_silent_0c7ba3_r002 | 2 | completed |  | 30/30 | 100.41 | 154 | 0 | 0 | OpenAI | 0.9898580 |
| 20261024T070258Z_study1r_4.1-high_silent_0c7ba3_r003 | 3 | completed |  | 30/30 | 137.68 | 154 | 0 | 0 | OpenAI | 0.9968320 |
| 20261024T070258Z_study1r_4.1-high_silent_0c7ba3_r004 | 4 | completed |  | 30/30 | 132.16 | 154 | 0 | 0 | OpenAI | 0.9915180 |
| 20261024T070258Z_study1r_4.1-high_silent_0c7ba3_r005 | 5 | completed |  | 30/30 | 105.74 | 154 | 0 | 0 | OpenAI | 0.9914820 |
| 20261024T070258Z_study1r_4.1-high_silent_0c7ba3_r006 | 6 | completed |  | 30/30 | 99.05 | 154 | 0 | 0 | OpenAI | 0.9912980 |
| 20261024T070258Z_study1r_4.1-high_silent_0c7ba3_r007 | 7 | completed |  | 30/30 | 112.53 | 154 | 0 | 0 | OpenAI | 0.9805720 |
| 20261024T070258Z_study1r_4.1-high_silent_0c7ba3_r008 | 8 | completed |  | 30/30 | 104.25 | 154 | 0 | 0 | OpenAI | 0.9946740 |

## Per round

Withheld: confirmatory run. Outcome tables (asks, bids, trades) are not written to reports until all Stage 2 blocks are complete (human message 24).
