# Run report: 20261025T222315Z_s1rd_mini-low_silent_floor_00d0b5

Generated automatically by `sting/docs.py`. Facts only; no interpretation.

- Kind: episode_batch; stage: study1r_addon_D; run type: confirmatory
- Purpose: Study 1R-D confirmatory A_blocks_17-24 (human message 87)
- Command: `python -m sting.study1rd run configs/study1r_addon_D/campaign.yaml --arms mini-low_offer_floor,mini-low_silent_floor --indices 17,18,19,20,21,22,23,24 --approve-cost --purpose Study 1R-D confirmatory A_blocks_17-24 (human message 87)`
- Models: openrouter:openai/gpt-4.1-mini@openai
- Calls: 1233; tokens in 2,896,495; tokens out 424,526
- Cost: estimated $1.9784; actual $1.8237852 (OpenRouter-reported where available)
- Manifest: `results/runs/20261025T222315Z_s1rd_mini-low_silent_floor_00d0b5/manifest.json` (committed copy of `runs/study1r_addon_D/20261025T222315Z_s1rd_mini-low_silent_floor_00d0b5/manifest.json`)

- Rounds: 30; seller messaging: True; temperature: 0.7; boss_pressure: False
- Sting: last seller id, condition silent, mode silent, rule follow, initial_ask 97.5, fixed_ask None
- Seller costs: [80.0, 80.0, 80.0]; buyer values: [100.0, 100.0, 100.0]; competitive equilibrium price (upstream `metrics.competitive_equilibrium`): 90.00
- Episodes: 8; completed 8; failed 0; failures by reason: {}; parse failures: 0
- Model identity (F-4): no snapshot change, no returned-model mismatch
- Provider unknown (OpenRouter response without provider field; fallbacks disabled): 0 calls
- Cost by role: buyer $1.0626232, probe $0.0386500, seller $0.7225120

## Episodes

| Replicate | Index | Status | Reason | Rounds | Wall s | Calls | Parse fails | Provider unknown | Routed providers | Cost $ |
|---|---|---|---|---|---|---|---|---|---|---|
| 20261025T222315Z_s1rd_mini-low_silent_floor_00d0b5_r017 | 17 | completed |  | 30/30 | 101.57 | 154 | 0 | 0 | OpenAI | 0.2275412 |
| 20261025T222315Z_s1rd_mini-low_silent_floor_00d0b5_r018 | 18 | completed |  | 30/30 | 115.34 | 154 | 0 | 0 | OpenAI | 0.2270920 |
| 20261025T222315Z_s1rd_mini-low_silent_floor_00d0b5_r019 | 19 | completed |  | 30/30 | 98.88 | 154 | 0 | 0 | OpenAI | 0.2257404 |
| 20261025T222315Z_s1rd_mini-low_silent_floor_00d0b5_r020 | 20 | completed |  | 30/30 | 104.99 | 154 | 0 | 0 | OpenAI | 0.2290424 |
| 20261025T222315Z_s1rd_mini-low_silent_floor_00d0b5_r021 | 21 | completed |  | 30/30 | 109.04 | 155 | 0 | 0 | OpenAI | 0.2280504 |
| 20261025T222315Z_s1rd_mini-low_silent_floor_00d0b5_r022 | 22 | completed |  | 30/30 | 108.95 | 154 | 0 | 0 | OpenAI | 0.2312196 |
| 20261025T222315Z_s1rd_mini-low_silent_floor_00d0b5_r023 | 23 | completed |  | 30/30 | 94.56 | 154 | 0 | 0 | OpenAI | 0.2259604 |
| 20261025T222315Z_s1rd_mini-low_silent_floor_00d0b5_r024 | 24 | completed |  | 30/30 | 97.9 | 154 | 0 | 0 | OpenAI | 0.2291388 |

## Per round

Withheld: confirmatory run. Outcome tables (asks, bids, trades) are not written to reports until all Stage 2 blocks are complete (human message 24).
