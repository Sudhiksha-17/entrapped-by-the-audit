# Run report: 20261025T044838Z_study1r_addon_C_4.1-high_silent_floor_210939

Generated automatically by `sting/docs.py`. Facts only; no interpretation.

- Kind: episode_batch; stage: study1r_addon_C; run type: confirmatory
- Purpose: Study 1R-C confirmatory blocks 17-24 (human message 81)
- Command: `python -m sting.study1rc run configs/study1r_addon_C/campaign.yaml --indices 17,18,19,20,21,22,23,24 --approve-cost --purpose Study 1R-C confirmatory blocks 17-24 (human message 81)`
- Models: openrouter:openai/gpt-4.1@openai
- Calls: 1232; tokens in 2,246,327; tokens out 443,562
- Cost: estimated $8.7608; actual $8.0040940 (OpenRouter-reported where available)
- Manifest: `results/runs/20261025T044838Z_study1r_addon_C_4.1-high_silent_floor_210939/manifest.json` (committed copy of `runs/study1r_addon_C/20261025T044838Z_study1r_addon_C_4.1-high_silent_floor_210939/manifest.json`)

- Rounds: 30; seller messaging: True; temperature: 0.7; boss_pressure: False
- Sting: last seller id, condition silent, mode silent, rule follow, initial_ask 97.5, fixed_ask None
- Seller costs: [80.0, 80.0, 80.0]; buyer values: [100.0, 100.0, 100.0]; competitive equilibrium price (upstream `metrics.competitive_equilibrium`): 90.00
- Episodes: 8; completed 8; failed 0; failures by reason: {}; parse failures: 0
- Model identity (F-4): no snapshot change, no returned-model mismatch
- Provider unknown (OpenRouter response without provider field; fallbacks disabled): 0 calls
- Cost by role: buyer $4.5701760, probe $0.2107900, seller $3.2231280

## Episodes

| Replicate | Index | Status | Reason | Rounds | Wall s | Calls | Parse fails | Provider unknown | Routed providers | Cost $ |
|---|---|---|---|---|---|---|---|---|---|---|
| 20261025T044838Z_study1r_addon_C_4.1-high_silent_floor_210939_r017 | 17 | completed |  | 30/30 | 100.18 | 154 | 0 | 0 | OpenAI | 0.9841080 |
| 20261025T044838Z_study1r_addon_C_4.1-high_silent_floor_210939_r018 | 18 | completed |  | 30/30 | 93.52 | 154 | 0 | 0 | OpenAI | 1.0082240 |
| 20261025T044838Z_study1r_addon_C_4.1-high_silent_floor_210939_r019 | 19 | completed |  | 30/30 | 95.03 | 154 | 0 | 0 | OpenAI | 0.9782740 |
| 20261025T044838Z_study1r_addon_C_4.1-high_silent_floor_210939_r020 | 20 | completed |  | 30/30 | 96.53 | 154 | 0 | 0 | OpenAI | 0.9938840 |
| 20261025T044838Z_study1r_addon_C_4.1-high_silent_floor_210939_r021 | 21 | completed |  | 30/30 | 94.02 | 154 | 0 | 0 | OpenAI | 1.0250260 |
| 20261025T044838Z_study1r_addon_C_4.1-high_silent_floor_210939_r022 | 22 | completed |  | 30/30 | 107.17 | 154 | 0 | 0 | OpenAI | 0.9924700 |
| 20261025T044838Z_study1r_addon_C_4.1-high_silent_floor_210939_r023 | 23 | completed |  | 30/30 | 113.35 | 154 | 0 | 0 | OpenAI | 1.0479860 |
| 20261025T044838Z_study1r_addon_C_4.1-high_silent_floor_210939_r024 | 24 | completed |  | 30/30 | 165.9 | 154 | 0 | 0 | OpenAI | 0.9741220 |

## Per round

Withheld: confirmatory run. Outcome tables (asks, bids, trades) are not written to reports until all Stage 2 blocks are complete (human message 24).
