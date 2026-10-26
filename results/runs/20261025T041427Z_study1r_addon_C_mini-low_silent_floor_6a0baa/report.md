# Run report: 20261025T041427Z_study1r_addon_C_mini-low_silent_floor_6a0baa

Generated automatically by `sting/docs.py`. Facts only; no interpretation.

- Kind: episode_batch; stage: study1r_addon_C; run type: confirmatory
- Purpose: Study 1R-C confirmatory block 0 gate (human message 81)
- Command: `python -m sting.study1rc run configs/study1r_addon_C/campaign.yaml --indices 0 --approve-cost --purpose Study 1R-C confirmatory block 0 gate (human message 81)`
- Models: openrouter:openai/gpt-4.1-mini@openai
- Calls: 154; tokens in 360,258; tokens out 53,372
- Cost: estimated $0.2453; actual $0.2284232 (OpenRouter-reported where available)
- Manifest: `results/runs/20261025T041427Z_study1r_addon_C_mini-low_silent_floor_6a0baa/manifest.json` (committed copy of `runs/study1r_addon_C/20261025T041427Z_study1r_addon_C_mini-low_silent_floor_6a0baa/manifest.json`)

- Rounds: 30; seller messaging: True; temperature: 0.7; boss_pressure: False
- Sting: last seller id, condition silent, mode silent, rule follow, initial_ask 97.5, fixed_ask None
- Seller costs: [80.0, 80.0, 80.0]; buyer values: [100.0, 100.0, 100.0]; competitive equilibrium price (upstream `metrics.competitive_equilibrium`): 90.00
- Episodes: 1; completed 1; failed 0; failures by reason: {}; parse failures: 0
- Model identity (F-4): no snapshot change, no returned-model mismatch
- Provider unknown (OpenRouter response without provider field; fallbacks disabled): 0 calls
- Cost by role: buyer $0.1327004, probe $0.0054452, seller $0.0902776

## Episodes

| Replicate | Index | Status | Reason | Rounds | Wall s | Calls | Parse fails | Provider unknown | Routed providers | Cost $ |
|---|---|---|---|---|---|---|---|---|---|---|
| 20261025T041427Z_study1r_addon_C_mini-low_silent_floor_6a0baa_r000 | 0 | completed |  | 30/30 | 109.15 | 154 | 0 | 0 | OpenAI | 0.2284232 |

## Per round

Withheld: confirmatory run. Outcome tables (asks, bids, trades) are not written to reports until all Stage 2 blocks are complete (human message 24).
