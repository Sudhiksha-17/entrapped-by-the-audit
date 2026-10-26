# Run report: 20261025T043122Z_study1r_addon_C_mini-low_silent_3959c3

Generated automatically by `sting/docs.py`. Facts only; no interpretation.

- Kind: episode_batch; stage: study1r_addon_C; run type: confirmatory
- Purpose: Study 1R-C confirmatory blocks 9-16 (human message 81)
- Command: `python -m sting.study1rc run configs/study1r_addon_C/campaign.yaml --indices 9,10,11,12,13,14,15,16 --approve-cost --purpose Study 1R-C confirmatory blocks 9-16 (human message 81)`
- Models: openrouter:openai/gpt-4.1-mini@openai
- Calls: 1232; tokens in 2,861,679; tokens out 404,404
- Cost: estimated $1.9624; actual $1.7781244 (OpenRouter-reported where available)
- Manifest: `results/runs/20261025T043122Z_study1r_addon_C_mini-low_silent_3959c3/manifest.json` (committed copy of `runs/study1r_addon_C/20261025T043122Z_study1r_addon_C_mini-low_silent_3959c3/manifest.json`)

- Rounds: 30; seller messaging: True; temperature: 0.7; boss_pressure: False
- Sting: last seller id, condition silent, mode silent, rule follow, initial_ask 97.5, fixed_ask None
- Seller costs: [80.0, 80.0, 80.0]; buyer values: [100.0, 100.0, 100.0]; competitive equilibrium price (upstream `metrics.competitive_equilibrium`): 90.00
- Episodes: 8; completed 8; failed 0; failures by reason: {}; parse failures: 0
- Model identity (F-4): no snapshot change, no returned-model mismatch
- Provider unknown (OpenRouter response without provider field; fallbacks disabled): 0 calls
- Cost by role: buyer $1.0334892, probe $0.0374988, seller $0.7071364

## Episodes

| Replicate | Index | Status | Reason | Rounds | Wall s | Calls | Parse fails | Provider unknown | Routed providers | Cost $ |
|---|---|---|---|---|---|---|---|---|---|---|
| 20261025T043122Z_study1r_addon_C_mini-low_silent_3959c3_r009 | 9 | completed |  | 30/30 | 93.8 | 154 | 0 | 0 | OpenAI | 0.2196380 |
| 20261025T043122Z_study1r_addon_C_mini-low_silent_3959c3_r010 | 10 | completed |  | 30/30 | 119.01 | 154 | 0 | 0 | OpenAI | 0.2229520 |
| 20261025T043122Z_study1r_addon_C_mini-low_silent_3959c3_r011 | 11 | completed |  | 30/30 | 98.65 | 154 | 0 | 0 | OpenAI | 0.2228380 |
| 20261025T043122Z_study1r_addon_C_mini-low_silent_3959c3_r012 | 12 | completed |  | 30/30 | 104.35 | 154 | 0 | 0 | OpenAI | 0.2201000 |
| 20261025T043122Z_study1r_addon_C_mini-low_silent_3959c3_r013 | 13 | completed |  | 30/30 | 144.12 | 154 | 0 | 0 | OpenAI | 0.2279272 |
| 20261025T043122Z_study1r_addon_C_mini-low_silent_3959c3_r014 | 14 | completed |  | 30/30 | 147.43 | 154 | 0 | 0 | OpenAI | 0.2252372 |
| 20261025T043122Z_study1r_addon_C_mini-low_silent_3959c3_r015 | 15 | completed |  | 30/30 | 131.6 | 154 | 0 | 0 | OpenAI | 0.2198772 |
| 20261025T043122Z_study1r_addon_C_mini-low_silent_3959c3_r016 | 16 | completed |  | 30/30 | 92.89 | 154 | 0 | 0 | OpenAI | 0.2195548 |

## Per round

Withheld: confirmatory run. Outcome tables (asks, bids, trades) are not written to reports until all Stage 2 blocks are complete (human message 24).
