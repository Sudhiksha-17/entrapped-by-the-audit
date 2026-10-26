# Run report: 20261026T001452Z_s1rd_mini-low_offer_floor_aa48ae

Generated automatically by `sting/docs.py`. Facts only; no interpretation.

- Kind: episode_batch; stage: study1r_addon_D; run type: confirmatory
- Purpose: Study 1R-D confirmatory A_blocks_49-56 (human message 89)
- Command: `python -m sting.study1rd run configs/study1r_addon_D/campaign.yaml --arms mini-low_offer_floor,mini-low_silent_floor --indices 49,50,51,52,53,54,55,56 --approve-cost --purpose Study 1R-D confirmatory A_blocks_49-56 (human message 89)`
- Models: openrouter:openai/gpt-4.1-mini@openai
- Calls: 1232; tokens in 2,880,832; tokens out 422,936
- Cost: estimated $2.0040; actual $1.8157824 (OpenRouter-reported where available)
- Manifest: `results/runs/20261026T001452Z_s1rd_mini-low_offer_floor_aa48ae/manifest.json` (committed copy of `runs/study1r_addon_D/20261026T001452Z_s1rd_mini-low_offer_floor_aa48ae/manifest.json`)

- Rounds: 30; seller messaging: True; temperature: 0.7; boss_pressure: False
- Sting: last seller id, condition offer, mode message, rule follow, initial_ask 97.5, fixed_ask None
- Seller costs: [80.0, 80.0, 80.0]; buyer values: [100.0, 100.0, 100.0]; competitive equilibrium price (upstream `metrics.competitive_equilibrium`): 90.00
- Episodes: 8; completed 8; failed 0; failures by reason: {}; parse failures: 0
- Model identity (F-4): no snapshot change, no returned-model mismatch
- Provider unknown (OpenRouter response without provider field; fallbacks disabled): 0 calls
- Cost by role: buyer $1.0440448, probe $0.0391072, seller $0.7326304

## Episodes

| Replicate | Index | Status | Reason | Rounds | Wall s | Calls | Parse fails | Provider unknown | Routed providers | Cost $ |
|---|---|---|---|---|---|---|---|---|---|---|
| 20261026T001452Z_s1rd_mini-low_offer_floor_aa48ae_r049 | 49 | completed |  | 30/30 | 121.34 | 154 | 0 | 0 | OpenAI | 0.2285084 |
| 20261026T001452Z_s1rd_mini-low_offer_floor_aa48ae_r050 | 50 | completed |  | 30/30 | 119.71 | 154 | 0 | 0 | OpenAI | 0.2150952 |
| 20261026T001452Z_s1rd_mini-low_offer_floor_aa48ae_r051 | 51 | completed |  | 30/30 | 107.35 | 154 | 0 | 0 | OpenAI | 0.2258304 |
| 20261026T001452Z_s1rd_mini-low_offer_floor_aa48ae_r052 | 52 | completed |  | 30/30 | 105.24 | 154 | 0 | 0 | OpenAI | 0.2246808 |
| 20261026T001452Z_s1rd_mini-low_offer_floor_aa48ae_r053 | 53 | completed |  | 30/30 | 110.41 | 154 | 0 | 0 | OpenAI | 0.2313360 |
| 20261026T001452Z_s1rd_mini-low_offer_floor_aa48ae_r054 | 54 | completed |  | 30/30 | 103.54 | 154 | 0 | 0 | OpenAI | 0.2295540 |
| 20261026T001452Z_s1rd_mini-low_offer_floor_aa48ae_r055 | 55 | completed |  | 30/30 | 115.85 | 154 | 0 | 0 | OpenAI | 0.2306784 |
| 20261026T001452Z_s1rd_mini-low_offer_floor_aa48ae_r056 | 56 | completed |  | 30/30 | 114.17 | 154 | 0 | 0 | OpenAI | 0.2300992 |

## Per round

Withheld: confirmatory run. Outcome tables (asks, bids, trades) are not written to reports until all Stage 2 blocks are complete (human message 24).
