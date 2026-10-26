# Run report: 20261025T215402Z_s1rd_mini-low_silent_floor_79b5d1

Generated automatically by `sting/docs.py`. Facts only; no interpretation.

- Kind: episode_batch; stage: study1r_addon_D; run type: confirmatory
- Purpose: Study 1R-D confirmatory A_blocks_1-8 (human message 87)
- Command: `python -m sting.study1rd run configs/study1r_addon_D/campaign.yaml --arms mini-low_offer_floor,mini-low_silent_floor --indices 1,2,3,4,5,6,7,8 --approve-cost --purpose Study 1R-D confirmatory A_blocks_1-8 (human message 87)`
- Models: openrouter:openai/gpt-4.1-mini@openai
- Calls: 1233; tokens in 2,878,044; tokens out 420,585
- Cost: estimated $1.9784; actual $1.8080640 (OpenRouter-reported where available)
- Manifest: `results/runs/20261025T215402Z_s1rd_mini-low_silent_floor_79b5d1/manifest.json` (committed copy of `runs/study1r_addon_D/20261025T215402Z_s1rd_mini-low_silent_floor_79b5d1/manifest.json`)

- Rounds: 30; seller messaging: True; temperature: 0.7; boss_pressure: False
- Sting: last seller id, condition silent, mode silent, rule follow, initial_ask 97.5, fixed_ask None
- Seller costs: [80.0, 80.0, 80.0]; buyer values: [100.0, 100.0, 100.0]; competitive equilibrium price (upstream `metrics.competitive_equilibrium`): 90.00
- Episodes: 8; completed 8; failed 0; failures by reason: {}; parse failures: 0
- Model identity (F-4): no snapshot change, no returned-model mismatch
- Provider unknown (OpenRouter response without provider field; fallbacks disabled): 0 calls
- Cost by role: buyer $1.0594312, probe $0.0359576, seller $0.7126752

## Episodes

| Replicate | Index | Status | Reason | Rounds | Wall s | Calls | Parse fails | Provider unknown | Routed providers | Cost $ |
|---|---|---|---|---|---|---|---|---|---|---|
| 20261025T215402Z_s1rd_mini-low_silent_floor_79b5d1_r001 | 1 | completed |  | 30/30 | 101.64 | 154 | 0 | 0 | OpenAI | 0.2217912 |
| 20261025T215402Z_s1rd_mini-low_silent_floor_79b5d1_r002 | 2 | completed |  | 30/30 | 108.52 | 155 | 0 | 0 | OpenAI | 0.2270604 |
| 20261025T215402Z_s1rd_mini-low_silent_floor_79b5d1_r003 | 3 | completed |  | 30/30 | 104.36 | 154 | 0 | 0 | OpenAI | 0.2265676 |
| 20261025T215402Z_s1rd_mini-low_silent_floor_79b5d1_r004 | 4 | completed |  | 30/30 | 108.33 | 154 | 0 | 0 | OpenAI | 0.2296532 |
| 20261025T215402Z_s1rd_mini-low_silent_floor_79b5d1_r005 | 5 | completed |  | 30/30 | 109.43 | 154 | 0 | 0 | OpenAI | 0.2297432 |
| 20261025T215402Z_s1rd_mini-low_silent_floor_79b5d1_r006 | 6 | completed |  | 30/30 | 116.78 | 154 | 0 | 0 | OpenAI | 0.2263868 |
| 20261025T215402Z_s1rd_mini-low_silent_floor_79b5d1_r007 | 7 | completed |  | 30/30 | 99.97 | 154 | 0 | 0 | OpenAI | 0.2220096 |
| 20261025T215402Z_s1rd_mini-low_silent_floor_79b5d1_r008 | 8 | completed |  | 30/30 | 108.33 | 154 | 0 | 0 | OpenAI | 0.2248520 |

## Per round

Withheld: confirmatory run. Outcome tables (asks, bids, trades) are not written to reports until all Stage 2 blocks are complete (human message 24).
