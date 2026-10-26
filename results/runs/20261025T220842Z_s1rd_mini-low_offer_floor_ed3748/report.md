# Run report: 20261025T220842Z_s1rd_mini-low_offer_floor_ed3748

Generated automatically by `sting/docs.py`. Facts only; no interpretation.

- Kind: episode_batch; stage: study1r_addon_D; run type: confirmatory
- Purpose: Study 1R-D confirmatory A_blocks_9-16 (human message 87)
- Command: `python -m sting.study1rd run configs/study1r_addon_D/campaign.yaml --arms mini-low_offer_floor,mini-low_silent_floor --indices 9,10,11,12,13,14,15,16 --approve-cost --purpose Study 1R-D confirmatory A_blocks_9-16 (human message 87)`
- Models: openrouter:openai/gpt-4.1-mini@openai
- Calls: 1232; tokens in 2,879,164; tokens out 426,744
- Cost: estimated $2.0040; actual $1.8194800 (OpenRouter-reported where available)
- Manifest: `results/runs/20261025T220842Z_s1rd_mini-low_offer_floor_ed3748/manifest.json` (committed copy of `runs/study1r_addon_D/20261025T220842Z_s1rd_mini-low_offer_floor_ed3748/manifest.json`)

- Rounds: 30; seller messaging: True; temperature: 0.7; boss_pressure: False
- Sting: last seller id, condition offer, mode message, rule follow, initial_ask 97.5, fixed_ask None
- Seller costs: [80.0, 80.0, 80.0]; buyer values: [100.0, 100.0, 100.0]; competitive equilibrium price (upstream `metrics.competitive_equilibrium`): 90.00
- Episodes: 8; completed 8; failed 0; failures by reason: {}; parse failures: 0
- Model identity (F-4): no snapshot change, no returned-model mismatch
- Provider unknown (OpenRouter response without provider field; fallbacks disabled): 0 calls
- Cost by role: buyer $1.0527224, probe $0.0372564, seller $0.7295012

## Episodes

| Replicate | Index | Status | Reason | Rounds | Wall s | Calls | Parse fails | Provider unknown | Routed providers | Cost $ |
|---|---|---|---|---|---|---|---|---|---|---|
| 20261025T220842Z_s1rd_mini-low_offer_floor_ed3748_r009 | 9 | completed |  | 30/30 | 100.47 | 154 | 0 | 0 | OpenAI | 0.2262208 |
| 20261025T220842Z_s1rd_mini-low_offer_floor_ed3748_r010 | 10 | completed |  | 30/30 | 113.78 | 154 | 0 | 0 | OpenAI | 0.2232964 |
| 20261025T220842Z_s1rd_mini-low_offer_floor_ed3748_r011 | 11 | completed |  | 30/30 | 100.67 | 154 | 0 | 0 | OpenAI | 0.2262316 |
| 20261025T220842Z_s1rd_mini-low_offer_floor_ed3748_r012 | 12 | completed |  | 30/30 | 113.22 | 154 | 0 | 0 | OpenAI | 0.2196744 |
| 20261025T220842Z_s1rd_mini-low_offer_floor_ed3748_r013 | 13 | completed |  | 30/30 | 100.56 | 154 | 0 | 0 | OpenAI | 0.2301956 |
| 20261025T220842Z_s1rd_mini-low_offer_floor_ed3748_r014 | 14 | completed |  | 30/30 | 109.32 | 154 | 0 | 0 | OpenAI | 0.2289720 |
| 20261025T220842Z_s1rd_mini-low_offer_floor_ed3748_r015 | 15 | completed |  | 30/30 | 105.9 | 154 | 0 | 0 | OpenAI | 0.2321364 |
| 20261025T220842Z_s1rd_mini-low_offer_floor_ed3748_r016 | 16 | completed |  | 30/30 | 105.11 | 154 | 0 | 0 | OpenAI | 0.2327528 |

## Per round

Withheld: confirmatory run. Outcome tables (asks, bids, trades) are not written to reports until all Stage 2 blocks are complete (human message 24).
