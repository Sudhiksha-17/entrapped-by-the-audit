# Run report: 20261025T234359Z_s1rd_mini-low_offer_floor_b1aeea

Generated automatically by `sting/docs.py`. Facts only; no interpretation.

- Kind: episode_batch; stage: study1r_addon_D; run type: confirmatory
- Purpose: Study 1R-D confirmatory A_blocks_33-40 (human message 89)
- Command: `python -m sting.study1rd run configs/study1r_addon_D/campaign.yaml --arms mini-low_offer_floor,mini-low_silent_floor --indices 33,34,35,36,37,38,39,40 --approve-cost --purpose Study 1R-D confirmatory A_blocks_33-40 (human message 89)`
- Models: openrouter:openai/gpt-4.1-mini@openai
- Calls: 1232; tokens in 2,911,982; tokens out 424,005
- Cost: estimated $2.0040; actual $1.8291848 (OpenRouter-reported where available)
- Manifest: `results/runs/20261025T234359Z_s1rd_mini-low_offer_floor_b1aeea/manifest.json` (committed copy of `runs/study1r_addon_D/20261025T234359Z_s1rd_mini-low_offer_floor_b1aeea/manifest.json`)

- Rounds: 30; seller messaging: True; temperature: 0.7; boss_pressure: False
- Sting: last seller id, condition offer, mode message, rule follow, initial_ask 97.5, fixed_ask None
- Seller costs: [80.0, 80.0, 80.0]; buyer values: [100.0, 100.0, 100.0]; competitive equilibrium price (upstream `metrics.competitive_equilibrium`): 90.00
- Episodes: 8; completed 8; failed 0; failures by reason: {}; parse failures: 0
- Model identity (F-4): no snapshot change, no returned-model mismatch
- Provider unknown (OpenRouter response without provider field; fallbacks disabled): 0 calls
- Cost by role: buyer $1.0667676, probe $0.0383684, seller $0.7240488

## Episodes

| Replicate | Index | Status | Reason | Rounds | Wall s | Calls | Parse fails | Provider unknown | Routed providers | Cost $ |
|---|---|---|---|---|---|---|---|---|---|---|
| 20261025T234359Z_s1rd_mini-low_offer_floor_b1aeea_r033 | 33 | completed |  | 30/30 | 107.08 | 154 | 0 | 0 | OpenAI | 0.2330412 |
| 20261025T234359Z_s1rd_mini-low_offer_floor_b1aeea_r034 | 34 | completed |  | 30/30 | 99.09 | 154 | 0 | 0 | OpenAI | 0.2306112 |
| 20261025T234359Z_s1rd_mini-low_offer_floor_b1aeea_r035 | 35 | completed |  | 30/30 | 109.99 | 154 | 0 | 0 | OpenAI | 0.2270876 |
| 20261025T234359Z_s1rd_mini-low_offer_floor_b1aeea_r036 | 36 | completed |  | 30/30 | 107.54 | 154 | 0 | 0 | OpenAI | 0.2296448 |
| 20261025T234359Z_s1rd_mini-low_offer_floor_b1aeea_r037 | 37 | completed |  | 30/30 | 99.27 | 154 | 0 | 0 | OpenAI | 0.2271672 |
| 20261025T234359Z_s1rd_mini-low_offer_floor_b1aeea_r038 | 38 | completed |  | 30/30 | 94.81 | 154 | 0 | 0 | OpenAI | 0.2268216 |
| 20261025T234359Z_s1rd_mini-low_offer_floor_b1aeea_r039 | 39 | completed |  | 30/30 | 102.66 | 154 | 0 | 0 | OpenAI | 0.2276564 |
| 20261025T234359Z_s1rd_mini-low_offer_floor_b1aeea_r040 | 40 | completed |  | 30/30 | 103.19 | 154 | 0 | 0 | OpenAI | 0.2271548 |

## Per round

Withheld: confirmatory run. Outcome tables (asks, bids, trades) are not written to reports until all Stage 2 blocks are complete (human message 24).
