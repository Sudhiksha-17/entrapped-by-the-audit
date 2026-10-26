# Run report: 20261025T041702Z_study1r_addon_C_4.1-high_silent_252cfa

Generated automatically by `sting/docs.py`. Facts only; no interpretation.

- Kind: episode_batch; stage: study1r_addon_C; run type: confirmatory
- Purpose: Study 1R-C confirmatory blocks 1-8 (human message 81)
- Command: `python -m sting.study1rc run configs/study1r_addon_C/campaign.yaml --indices 1,2,3,4,5,6,7,8 --approve-cost --purpose Study 1R-C confirmatory blocks 1-8 (human message 81)`
- Models: openrouter:openai/gpt-4.1@openai
- Calls: 1232; tokens in 2,255,845; tokens out 439,513
- Cost: estimated $8.7608; actual $7.9934260 (OpenRouter-reported where available)
- Manifest: `results/runs/20261025T041702Z_study1r_addon_C_4.1-high_silent_252cfa/manifest.json` (committed copy of `runs/study1r_addon_C/20261025T041702Z_study1r_addon_C_4.1-high_silent_252cfa/manifest.json`)

- Rounds: 30; seller messaging: True; temperature: 0.7; boss_pressure: False
- Sting: last seller id, condition silent, mode silent, rule follow, initial_ask 97.5, fixed_ask None
- Seller costs: [80.0, 80.0, 80.0]; buyer values: [100.0, 100.0, 100.0]; competitive equilibrium price (upstream `metrics.competitive_equilibrium`): 90.00
- Episodes: 8; completed 8; failed 0; failures by reason: {}; parse failures: 0
- Model identity (F-4): no snapshot change, no returned-model mismatch
- Provider unknown (OpenRouter response without provider field; fallbacks disabled): 0 calls
- Cost by role: buyer $4.5376440, probe $0.2240380, seller $3.2317440

## Episodes

| Replicate | Index | Status | Reason | Rounds | Wall s | Calls | Parse fails | Provider unknown | Routed providers | Cost $ |
|---|---|---|---|---|---|---|---|---|---|---|
| 20261025T041702Z_study1r_addon_C_4.1-high_silent_252cfa_r001 | 1 | completed |  | 30/30 | 98.75 | 154 | 0 | 0 | OpenAI | 1.0456020 |
| 20261025T041702Z_study1r_addon_C_4.1-high_silent_252cfa_r002 | 2 | completed |  | 30/30 | 96.35 | 154 | 0 | 0 | OpenAI | 1.0233520 |
| 20261025T041702Z_study1r_addon_C_4.1-high_silent_252cfa_r003 | 3 | completed |  | 30/30 | 94.14 | 154 | 0 | 0 | OpenAI | 0.9853780 |
| 20261025T041702Z_study1r_addon_C_4.1-high_silent_252cfa_r004 | 4 | completed |  | 30/30 | 95.24 | 154 | 0 | 0 | OpenAI | 0.9689900 |
| 20261025T041702Z_study1r_addon_C_4.1-high_silent_252cfa_r005 | 5 | completed |  | 30/30 | 96.34 | 154 | 0 | 0 | OpenAI | 0.9829800 |
| 20261025T041702Z_study1r_addon_C_4.1-high_silent_252cfa_r006 | 6 | completed |  | 30/30 | 102.22 | 154 | 0 | 0 | OpenAI | 0.9878480 |
| 20261025T041702Z_study1r_addon_C_4.1-high_silent_252cfa_r007 | 7 | completed |  | 30/30 | 105.21 | 154 | 0 | 0 | OpenAI | 0.9917260 |
| 20261025T041702Z_study1r_addon_C_4.1-high_silent_252cfa_r008 | 8 | completed |  | 30/30 | 97.92 | 154 | 0 | 0 | OpenAI | 1.0075500 |

## Per round

Withheld: confirmatory run. Outcome tables (asks, bids, trades) are not written to reports until all Stage 2 blocks are complete (human message 24).
