# Run report: 20261025T235824Z_s1rd_mini-low_offer_floor_24a381

Generated automatically by `sting/docs.py`. Facts only; no interpretation.

- Kind: episode_batch; stage: study1r_addon_D; run type: confirmatory
- Purpose: Study 1R-D confirmatory A_blocks_41-48 (human message 89)
- Command: `python -m sting.study1rd run configs/study1r_addon_D/campaign.yaml --arms mini-low_offer_floor,mini-low_silent_floor --indices 41,42,43,44,45,46,47,48 --approve-cost --purpose Study 1R-D confirmatory A_blocks_41-48 (human message 89)`
- Models: openrouter:openai/gpt-4.1-mini@openai
- Calls: 1232; tokens in 2,917,941; tokens out 432,073
- Cost: estimated $2.0040; actual $1.8425956 (OpenRouter-reported where available)
- Manifest: `results/runs/20261025T235824Z_s1rd_mini-low_offer_floor_24a381/manifest.json` (committed copy of `runs/study1r_addon_D/20261025T235824Z_s1rd_mini-low_offer_floor_24a381/manifest.json`)

- Rounds: 30; seller messaging: True; temperature: 0.7; boss_pressure: False
- Sting: last seller id, condition offer, mode message, rule follow, initial_ask 97.5, fixed_ask None
- Seller costs: [80.0, 80.0, 80.0]; buyer values: [100.0, 100.0, 100.0]; competitive equilibrium price (upstream `metrics.competitive_equilibrium`): 90.00
- Episodes: 8; completed 8; failed 0; failures by reason: {}; parse failures: 0
- Model identity (F-4): no snapshot change, no returned-model mismatch
- Provider unknown (OpenRouter response without provider field; fallbacks disabled): 0 calls
- Cost by role: buyer $1.0599576, probe $0.0389560, seller $0.7436820

## Episodes

| Replicate | Index | Status | Reason | Rounds | Wall s | Calls | Parse fails | Provider unknown | Routed providers | Cost $ |
|---|---|---|---|---|---|---|---|---|---|---|
| 20261025T235824Z_s1rd_mini-low_offer_floor_24a381_r041 | 41 | completed |  | 30/30 | 107.54 | 154 | 0 | 0 | OpenAI | 0.2323484 |
| 20261025T235824Z_s1rd_mini-low_offer_floor_24a381_r042 | 42 | completed |  | 30/30 | 126.89 | 154 | 0 | 0 | OpenAI | 0.2358668 |
| 20261025T235824Z_s1rd_mini-low_offer_floor_24a381_r043 | 43 | completed |  | 30/30 | 118.71 | 154 | 0 | 0 | OpenAI | 0.2209364 |
| 20261025T235824Z_s1rd_mini-low_offer_floor_24a381_r044 | 44 | completed |  | 30/30 | 113.8 | 154 | 0 | 0 | OpenAI | 0.2325436 |
| 20261025T235824Z_s1rd_mini-low_offer_floor_24a381_r045 | 45 | completed |  | 30/30 | 106.74 | 154 | 0 | 0 | OpenAI | 0.2312516 |
| 20261025T235824Z_s1rd_mini-low_offer_floor_24a381_r046 | 46 | completed |  | 30/30 | 113.21 | 154 | 0 | 0 | OpenAI | 0.2276096 |
| 20261025T235824Z_s1rd_mini-low_offer_floor_24a381_r047 | 47 | completed |  | 30/30 | 171.78 | 154 | 0 | 0 | OpenAI | 0.2325984 |
| 20261025T235824Z_s1rd_mini-low_offer_floor_24a381_r048 | 48 | completed |  | 30/30 | 103.03 | 154 | 0 | 0 | OpenAI | 0.2294408 |

## Per round

Withheld: confirmatory run. Outcome tables (asks, bids, trades) are not written to reports until all Stage 2 blocks are complete (human message 24).
