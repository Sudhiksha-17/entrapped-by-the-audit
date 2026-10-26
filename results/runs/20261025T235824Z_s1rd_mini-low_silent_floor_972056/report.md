# Run report: 20261025T235824Z_s1rd_mini-low_silent_floor_972056

Generated automatically by `sting/docs.py`. Facts only; no interpretation.

- Kind: episode_batch; stage: study1r_addon_D; run type: confirmatory
- Purpose: Study 1R-D confirmatory A_blocks_41-48 (human message 89)
- Command: `python -m sting.study1rd run configs/study1r_addon_D/campaign.yaml --arms mini-low_offer_floor,mini-low_silent_floor --indices 41,42,43,44,45,46,47,48 --approve-cost --purpose Study 1R-D confirmatory A_blocks_41-48 (human message 89)`
- Models: openrouter:openai/gpt-4.1-mini@openai
- Calls: 1232; tokens in 2,855,087; tokens out 419,903
- Cost: estimated $1.9784; actual $1.7977900 (OpenRouter-reported where available)
- Manifest: `results/runs/20261025T235824Z_s1rd_mini-low_silent_floor_972056/manifest.json` (committed copy of `runs/study1r_addon_D/20261025T235824Z_s1rd_mini-low_silent_floor_972056/manifest.json`)

- Rounds: 30; seller messaging: True; temperature: 0.7; boss_pressure: False
- Sting: last seller id, condition silent, mode silent, rule follow, initial_ask 97.5, fixed_ask None
- Seller costs: [80.0, 80.0, 80.0]; buyer values: [100.0, 100.0, 100.0]; competitive equilibrium price (upstream `metrics.competitive_equilibrium`): 90.00
- Episodes: 8; completed 8; failed 0; failures by reason: {}; parse failures: 0
- Model identity (F-4): no snapshot change, no returned-model mismatch
- Provider unknown (OpenRouter response without provider field; fallbacks disabled): 0 calls
- Cost by role: buyer $1.0526580, probe $0.0360480, seller $0.7090840

## Episodes

| Replicate | Index | Status | Reason | Rounds | Wall s | Calls | Parse fails | Provider unknown | Routed providers | Cost $ |
|---|---|---|---|---|---|---|---|---|---|---|
| 20261025T235824Z_s1rd_mini-low_silent_floor_972056_r041 | 41 | completed |  | 30/30 | 101.74 | 154 | 0 | 0 | OpenAI | 0.2210376 |
| 20261025T235824Z_s1rd_mini-low_silent_floor_972056_r042 | 42 | completed |  | 30/30 | 118.89 | 154 | 0 | 0 | OpenAI | 0.2294376 |
| 20261025T235824Z_s1rd_mini-low_silent_floor_972056_r043 | 43 | completed |  | 30/30 | 125.26 | 154 | 0 | 0 | OpenAI | 0.2213440 |
| 20261025T235824Z_s1rd_mini-low_silent_floor_972056_r044 | 44 | completed |  | 30/30 | 105.28 | 154 | 0 | 0 | OpenAI | 0.2278120 |
| 20261025T235824Z_s1rd_mini-low_silent_floor_972056_r045 | 45 | completed |  | 30/30 | 107.88 | 154 | 0 | 0 | OpenAI | 0.2182764 |
| 20261025T235824Z_s1rd_mini-low_silent_floor_972056_r046 | 46 | completed |  | 30/30 | 111.94 | 154 | 0 | 0 | OpenAI | 0.2280328 |
| 20261025T235824Z_s1rd_mini-low_silent_floor_972056_r047 | 47 | completed |  | 30/30 | 112.64 | 154 | 0 | 0 | OpenAI | 0.2218680 |
| 20261025T235824Z_s1rd_mini-low_silent_floor_972056_r048 | 48 | completed |  | 30/30 | 104.82 | 154 | 0 | 0 | OpenAI | 0.2299816 |

## Per round

Withheld: confirmatory run. Outcome tables (asks, bids, trades) are not written to reports until all Stage 2 blocks are complete (human message 24).
