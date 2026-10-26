# Run report: 20261025T044838Z_study1r_addon_C_mini-low_silent_3e2e03

Generated automatically by `sting/docs.py`. Facts only; no interpretation.

- Kind: episode_batch; stage: study1r_addon_C; run type: confirmatory
- Purpose: Study 1R-C confirmatory blocks 17-24 (human message 81)
- Command: `python -m sting.study1rc run configs/study1r_addon_C/campaign.yaml --indices 17,18,19,20,21,22,23,24 --approve-cost --purpose Study 1R-C confirmatory blocks 17-24 (human message 81)`
- Models: openrouter:openai/gpt-4.1-mini@openai
- Calls: 1232; tokens in 2,870,485; tokens out 408,670
- Cost: estimated $1.9624; actual $1.7866676 (OpenRouter-reported where available)
- Manifest: `results/runs/20261025T044838Z_study1r_addon_C_mini-low_silent_3e2e03/manifest.json` (committed copy of `runs/study1r_addon_C/20261025T044838Z_study1r_addon_C_mini-low_silent_3e2e03/manifest.json`)

- Rounds: 30; seller messaging: True; temperature: 0.7; boss_pressure: False
- Sting: last seller id, condition silent, mode silent, rule follow, initial_ask 97.5, fixed_ask None
- Seller costs: [80.0, 80.0, 80.0]; buyer values: [100.0, 100.0, 100.0]; competitive equilibrium price (upstream `metrics.competitive_equilibrium`): 90.00
- Episodes: 8; completed 8; failed 0; failures by reason: {}; parse failures: 0
- Model identity (F-4): no snapshot change, no returned-model mismatch
- Provider unknown (OpenRouter response without provider field; fallbacks disabled): 0 calls
- Cost by role: buyer $1.0477060, probe $0.0349588, seller $0.7040028

## Episodes

| Replicate | Index | Status | Reason | Rounds | Wall s | Calls | Parse fails | Provider unknown | Routed providers | Cost $ |
|---|---|---|---|---|---|---|---|---|---|---|
| 20261025T044838Z_study1r_addon_C_mini-low_silent_3e2e03_r017 | 17 | completed |  | 30/30 | 93.35 | 154 | 0 | 0 | OpenAI | 0.2222560 |
| 20261025T044838Z_study1r_addon_C_mini-low_silent_3e2e03_r018 | 18 | completed |  | 30/30 | 100.14 | 154 | 0 | 0 | OpenAI | 0.2211156 |
| 20261025T044838Z_study1r_addon_C_mini-low_silent_3e2e03_r019 | 19 | completed |  | 30/30 | 92.87 | 154 | 0 | 0 | OpenAI | 0.2212020 |
| 20261025T044838Z_study1r_addon_C_mini-low_silent_3e2e03_r020 | 20 | completed |  | 30/30 | 101.35 | 154 | 0 | 0 | OpenAI | 0.2253860 |
| 20261025T044838Z_study1r_addon_C_mini-low_silent_3e2e03_r021 | 21 | completed |  | 30/30 | 104.45 | 154 | 0 | 0 | OpenAI | 0.2243912 |
| 20261025T044838Z_study1r_addon_C_mini-low_silent_3e2e03_r022 | 22 | completed |  | 30/30 | 99.98 | 154 | 0 | 0 | OpenAI | 0.2253864 |
| 20261025T044838Z_study1r_addon_C_mini-low_silent_3e2e03_r023 | 23 | completed |  | 30/30 | 103.39 | 154 | 0 | 0 | OpenAI | 0.2273528 |
| 20261025T044838Z_study1r_addon_C_mini-low_silent_3e2e03_r024 | 24 | completed |  | 30/30 | 97.62 | 154 | 0 | 0 | OpenAI | 0.2195776 |

## Per round

Withheld: confirmatory run. Outcome tables (asks, bids, trades) are not written to reports until all Stage 2 blocks are complete (human message 24).
