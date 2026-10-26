# Run report: 20261026T003020Z_s1rd_mini-low_offer_floor_efa4cd

Generated automatically by `sting/docs.py`. Facts only; no interpretation.

- Kind: episode_batch; stage: study1r_addon_D; run type: confirmatory
- Purpose: Study 1R-D confirmatory A_blocks_57-59 (human message 89)
- Command: `python -m sting.study1rd run configs/study1r_addon_D/campaign.yaml --arms mini-low_offer_floor,mini-low_silent_floor --indices 57,58,59 --approve-cost --purpose Study 1R-D confirmatory A_blocks_57-59 (human message 89)`
- Models: openrouter:openai/gpt-4.1-mini@openai
- Calls: 462; tokens in 1,089,876; tokens out 157,284
- Cost: estimated $0.7515; actual $0.6810384 (OpenRouter-reported where available)
- Manifest: `results/runs/20261026T003020Z_s1rd_mini-low_offer_floor_efa4cd/manifest.json` (committed copy of `runs/study1r_addon_D/20261026T003020Z_s1rd_mini-low_offer_floor_efa4cd/manifest.json`)

- Rounds: 30; seller messaging: True; temperature: 0.7; boss_pressure: False
- Sting: last seller id, condition offer, mode message, rule follow, initial_ask 97.5, fixed_ask None
- Seller costs: [80.0, 80.0, 80.0]; buyer values: [100.0, 100.0, 100.0]; competitive equilibrium price (upstream `metrics.competitive_equilibrium`): 90.00
- Episodes: 3; completed 3; failed 0; failures by reason: {}; parse failures: 0
- Model identity (F-4): no snapshot change, no returned-model mismatch
- Provider unknown (OpenRouter response without provider field; fallbacks disabled): 0 calls
- Cost by role: buyer $0.3930068, probe $0.0135164, seller $0.2745152

## Episodes

| Replicate | Index | Status | Reason | Rounds | Wall s | Calls | Parse fails | Provider unknown | Routed providers | Cost $ |
|---|---|---|---|---|---|---|---|---|---|---|
| 20261026T003020Z_s1rd_mini-low_offer_floor_efa4cd_r057 | 57 | completed |  | 30/30 | 102.3 | 154 | 0 | 0 | OpenAI | 0.2284104 |
| 20261026T003020Z_s1rd_mini-low_offer_floor_efa4cd_r058 | 58 | completed |  | 30/30 | 104.62 | 154 | 0 | 0 | OpenAI | 0.2246172 |
| 20261026T003020Z_s1rd_mini-low_offer_floor_efa4cd_r059 | 59 | completed |  | 30/30 | 116.63 | 154 | 0 | 0 | OpenAI | 0.2280108 |

## Per round

Withheld: confirmatory run. Outcome tables (asks, bids, trades) are not written to reports until all Stage 2 blocks are complete (human message 24).
