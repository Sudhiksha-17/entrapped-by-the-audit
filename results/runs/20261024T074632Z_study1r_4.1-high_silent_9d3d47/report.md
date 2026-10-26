# Run report: 20261024T074632Z_study1r_4.1-high_silent_9d3d47

Generated automatically by `sting/docs.py`. Facts only; no interpretation.

- Kind: episode_batch; stage: study1r; run type: confirmatory
- Purpose: Study 1R confirmatory blocks 9-16 (human message 67, step 2)
- Command: `python -m sting.stage2_runner configs/study1r/campaign.yaml --indices 9,10,11,12,13,14,15,16 --approve-cost --purpose Study 1R confirmatory blocks 9-16 (human message 67, step 2)`
- Models: openrouter:openai/gpt-4.1@openai
- Calls: 1232; tokens in 2,227,109; tokens out 441,947
- Cost: estimated $8.8688; actual $7.9558100 (OpenRouter-reported where available)
- Manifest: `results/runs/20261024T074632Z_study1r_4.1-high_silent_9d3d47/manifest.json` (committed copy of `runs/study1r/20261024T074632Z_study1r_4.1-high_silent_9d3d47/manifest.json`)

- Rounds: 30; seller messaging: True; temperature: 0.7; boss_pressure: False
- Sting: last seller id, condition silent, mode silent, rule follow, initial_ask 97.5, fixed_ask None
- Seller costs: [80.0, 80.0, 80.0]; buyer values: [100.0, 100.0, 100.0]; competitive equilibrium price (upstream `metrics.competitive_equilibrium`): 90.00
- Episodes: 8; completed 8; failed 0; failures by reason: {}; parse failures: 0
- Model identity (F-4): no snapshot change, no returned-model mismatch
- Provider unknown (OpenRouter response without provider field; fallbacks disabled): 0 calls
- Cost by role: buyer $4.5152520, probe $0.2143560, seller $3.2262020

## Episodes

| Replicate | Index | Status | Reason | Rounds | Wall s | Calls | Parse fails | Provider unknown | Routed providers | Cost $ |
|---|---|---|---|---|---|---|---|---|---|---|
| 20261024T074632Z_study1r_4.1-high_silent_9d3d47_r009 | 9 | completed |  | 30/30 | 101.51 | 154 | 0 | 0 | OpenAI | 0.9744480 |
| 20261024T074632Z_study1r_4.1-high_silent_9d3d47_r010 | 10 | completed |  | 30/30 | 94.87 | 154 | 0 | 0 | OpenAI | 1.0054260 |
| 20261024T074632Z_study1r_4.1-high_silent_9d3d47_r011 | 11 | completed |  | 30/30 | 90.21 | 154 | 0 | 0 | OpenAI | 0.9728620 |
| 20261024T074632Z_study1r_4.1-high_silent_9d3d47_r012 | 12 | completed |  | 30/30 | 114.42 | 154 | 0 | 0 | OpenAI | 1.0045240 |
| 20261024T074632Z_study1r_4.1-high_silent_9d3d47_r013 | 13 | completed |  | 30/30 | 171.37 | 154 | 0 | 0 | OpenAI | 0.9791940 |
| 20261024T074632Z_study1r_4.1-high_silent_9d3d47_r014 | 14 | completed |  | 30/30 | 106.94 | 154 | 0 | 0 | OpenAI | 0.9997600 |
| 20261024T074632Z_study1r_4.1-high_silent_9d3d47_r015 | 15 | completed |  | 30/30 | 139.34 | 154 | 0 | 0 | OpenAI | 1.0500840 |
| 20261024T074632Z_study1r_4.1-high_silent_9d3d47_r016 | 16 | completed |  | 30/30 | 118.54 | 154 | 0 | 0 | OpenAI | 0.9695120 |

## Per round

Withheld: confirmatory run. Outcome tables (asks, bids, trades) are not written to reports until all Stage 2 blocks are complete (human message 24).
