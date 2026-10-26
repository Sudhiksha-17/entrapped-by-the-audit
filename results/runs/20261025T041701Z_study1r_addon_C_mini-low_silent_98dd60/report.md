# Run report: 20261025T041701Z_study1r_addon_C_mini-low_silent_98dd60

Generated automatically by `sting/docs.py`. Facts only; no interpretation.

- Kind: episode_batch; stage: study1r_addon_C; run type: confirmatory
- Purpose: Study 1R-C confirmatory blocks 1-8 (human message 81)
- Command: `python -m sting.study1rc run configs/study1r_addon_C/campaign.yaml --indices 1,2,3,4,5,6,7,8 --approve-cost --purpose Study 1R-C confirmatory blocks 1-8 (human message 81)`
- Models: openrouter:openai/gpt-4.1-mini@openai
- Calls: 1232; tokens in 2,863,251; tokens out 405,024
- Cost: estimated $1.9624; actual $1.7774412 (OpenRouter-reported where available)
- Manifest: `results/runs/20261025T041701Z_study1r_addon_C_mini-low_silent_98dd60/manifest.json` (committed copy of `runs/study1r_addon_C/20261025T041701Z_study1r_addon_C_mini-low_silent_98dd60/manifest.json`)

- Rounds: 30; seller messaging: True; temperature: 0.7; boss_pressure: False
- Sting: last seller id, condition silent, mode silent, rule follow, initial_ask 97.5, fixed_ask None
- Seller costs: [80.0, 80.0, 80.0]; buyer values: [100.0, 100.0, 100.0]; competitive equilibrium price (upstream `metrics.competitive_equilibrium`): 90.00
- Episodes: 8; completed 8; failed 0; failures by reason: {}; parse failures: 0
- Model identity (F-4): no snapshot change, no returned-model mismatch
- Provider unknown (OpenRouter response without provider field; fallbacks disabled): 0 calls
- Cost by role: buyer $1.0397716, probe $0.0366132, seller $0.7010564

## Episodes

| Replicate | Index | Status | Reason | Rounds | Wall s | Calls | Parse fails | Provider unknown | Routed providers | Cost $ |
|---|---|---|---|---|---|---|---|---|---|---|
| 20261025T041701Z_study1r_addon_C_mini-low_silent_98dd60_r001 | 1 | completed |  | 30/30 | 92.96 | 154 | 0 | 0 | OpenAI | 0.2221696 |
| 20261025T041701Z_study1r_addon_C_mini-low_silent_98dd60_r002 | 2 | completed |  | 30/30 | 91.7 | 154 | 0 | 0 | OpenAI | 0.2215996 |
| 20261025T041701Z_study1r_addon_C_mini-low_silent_98dd60_r003 | 3 | completed |  | 30/30 | 98.17 | 154 | 0 | 0 | OpenAI | 0.2257376 |
| 20261025T041701Z_study1r_addon_C_mini-low_silent_98dd60_r004 | 4 | completed |  | 30/30 | 104.2 | 154 | 0 | 0 | OpenAI | 0.2201464 |
| 20261025T041701Z_study1r_addon_C_mini-low_silent_98dd60_r005 | 5 | completed |  | 30/30 | 99.37 | 154 | 0 | 0 | OpenAI | 0.2209696 |
| 20261025T041701Z_study1r_addon_C_mini-low_silent_98dd60_r006 | 6 | completed |  | 30/30 | 97.94 | 154 | 0 | 0 | OpenAI | 0.2248228 |
| 20261025T041701Z_study1r_addon_C_mini-low_silent_98dd60_r007 | 7 | completed |  | 30/30 | 102.17 | 154 | 0 | 0 | OpenAI | 0.2179240 |
| 20261025T041701Z_study1r_addon_C_mini-low_silent_98dd60_r008 | 8 | completed |  | 30/30 | 108.9 | 154 | 0 | 0 | OpenAI | 0.2240716 |

## Per round

Withheld: confirmatory run. Outcome tables (asks, bids, trades) are not written to reports until all Stage 2 blocks are complete (human message 24).
