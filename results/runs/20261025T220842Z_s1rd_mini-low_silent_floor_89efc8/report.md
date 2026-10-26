# Run report: 20261025T220842Z_s1rd_mini-low_silent_floor_89efc8

Generated automatically by `sting/docs.py`. Facts only; no interpretation.

- Kind: episode_batch; stage: study1r_addon_D; run type: confirmatory
- Purpose: Study 1R-D confirmatory A_blocks_9-16 (human message 87)
- Command: `python -m sting.study1rd run configs/study1r_addon_D/campaign.yaml --arms mini-low_offer_floor,mini-low_silent_floor --indices 9,10,11,12,13,14,15,16 --approve-cost --purpose Study 1R-D confirmatory A_blocks_9-16 (human message 87)`
- Models: openrouter:openai/gpt-4.1-mini@openai
- Calls: 1232; tokens in 2,884,122; tokens out 418,285
- Cost: estimated $1.9784; actual $1.8111928 (OpenRouter-reported where available)
- Manifest: `results/runs/20261025T220842Z_s1rd_mini-low_silent_floor_89efc8/manifest.json` (committed copy of `runs/study1r_addon_D/20261025T220842Z_s1rd_mini-low_silent_floor_89efc8/manifest.json`)

- Rounds: 30; seller messaging: True; temperature: 0.7; boss_pressure: False
- Sting: last seller id, condition silent, mode silent, rule follow, initial_ask 97.5, fixed_ask None
- Seller costs: [80.0, 80.0, 80.0]; buyer values: [100.0, 100.0, 100.0]; competitive equilibrium price (upstream `metrics.competitive_equilibrium`): 90.00
- Episodes: 8; completed 8; failed 0; failures by reason: {}; parse failures: 0
- Model identity (F-4): no snapshot change, no returned-model mismatch
- Provider unknown (OpenRouter response without provider field; fallbacks disabled): 0 calls
- Cost by role: buyer $1.0586928, probe $0.0405496, seller $0.7119504

## Episodes

| Replicate | Index | Status | Reason | Rounds | Wall s | Calls | Parse fails | Provider unknown | Routed providers | Cost $ |
|---|---|---|---|---|---|---|---|---|---|---|
| 20261025T220842Z_s1rd_mini-low_silent_floor_89efc8_r009 | 9 | completed |  | 30/30 | 99.16 | 154 | 0 | 0 | OpenAI | 0.2270708 |
| 20261025T220842Z_s1rd_mini-low_silent_floor_89efc8_r010 | 10 | completed |  | 30/30 | 109.63 | 154 | 0 | 0 | OpenAI | 0.2279432 |
| 20261025T220842Z_s1rd_mini-low_silent_floor_89efc8_r011 | 11 | completed |  | 30/30 | 93.64 | 154 | 0 | 0 | OpenAI | 0.2161400 |
| 20261025T220842Z_s1rd_mini-low_silent_floor_89efc8_r012 | 12 | completed |  | 30/30 | 108.24 | 154 | 0 | 0 | OpenAI | 0.2317888 |
| 20261025T220842Z_s1rd_mini-low_silent_floor_89efc8_r013 | 13 | completed |  | 30/30 | 107.53 | 154 | 0 | 0 | OpenAI | 0.2212524 |
| 20261025T220842Z_s1rd_mini-low_silent_floor_89efc8_r014 | 14 | completed |  | 30/30 | 112.81 | 154 | 0 | 0 | OpenAI | 0.2282852 |
| 20261025T220842Z_s1rd_mini-low_silent_floor_89efc8_r015 | 15 | completed |  | 30/30 | 96.63 | 154 | 0 | 0 | OpenAI | 0.2241800 |
| 20261025T220842Z_s1rd_mini-low_silent_floor_89efc8_r016 | 16 | completed |  | 30/30 | 101.26 | 154 | 0 | 0 | OpenAI | 0.2345324 |

## Per round

Withheld: confirmatory run. Outcome tables (asks, bids, trades) are not written to reports until all Stage 2 blocks are complete (human message 24).
