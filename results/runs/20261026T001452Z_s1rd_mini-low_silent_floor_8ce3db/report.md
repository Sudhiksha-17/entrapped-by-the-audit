# Run report: 20261026T001452Z_s1rd_mini-low_silent_floor_8ce3db

Generated automatically by `sting/docs.py`. Facts only; no interpretation.

- Kind: episode_batch; stage: study1r_addon_D; run type: confirmatory
- Purpose: Study 1R-D confirmatory A_blocks_49-56 (human message 89)
- Command: `python -m sting.study1rd run configs/study1r_addon_D/campaign.yaml --arms mini-low_offer_floor,mini-low_silent_floor --indices 49,50,51,52,53,54,55,56 --approve-cost --purpose Study 1R-D confirmatory A_blocks_49-56 (human message 89)`
- Models: openrouter:openai/gpt-4.1-mini@openai
- Calls: 1232; tokens in 2,865,647; tokens out 419,415
- Cost: estimated $1.9784; actual $1.8052652 (OpenRouter-reported where available)
- Manifest: `results/runs/20261026T001452Z_s1rd_mini-low_silent_floor_8ce3db/manifest.json` (committed copy of `runs/study1r_addon_D/20261026T001452Z_s1rd_mini-low_silent_floor_8ce3db/manifest.json`)

- Rounds: 30; seller messaging: True; temperature: 0.7; boss_pressure: False
- Sting: last seller id, condition silent, mode silent, rule follow, initial_ask 97.5, fixed_ask None
- Seller costs: [80.0, 80.0, 80.0]; buyer values: [100.0, 100.0, 100.0]; competitive equilibrium price (upstream `metrics.competitive_equilibrium`): 90.00
- Episodes: 8; completed 8; failed 0; failures by reason: {}; parse failures: 0
- Model identity (F-4): no snapshot change, no returned-model mismatch
- Provider unknown (OpenRouter response without provider field; fallbacks disabled): 0 calls
- Cost by role: buyer $1.0484672, probe $0.0414644, seller $0.7153336

## Episodes

| Replicate | Index | Status | Reason | Rounds | Wall s | Calls | Parse fails | Provider unknown | Routed providers | Cost $ |
|---|---|---|---|---|---|---|---|---|---|---|
| 20261026T001452Z_s1rd_mini-low_silent_floor_8ce3db_r049 | 49 | completed |  | 30/30 | 117.23 | 154 | 0 | 0 | OpenAI | 0.2301772 |
| 20261026T001452Z_s1rd_mini-low_silent_floor_8ce3db_r050 | 50 | completed |  | 30/30 | 110.87 | 154 | 0 | 0 | OpenAI | 0.2264304 |
| 20261026T001452Z_s1rd_mini-low_silent_floor_8ce3db_r051 | 51 | completed |  | 30/30 | 112.8 | 154 | 0 | 0 | OpenAI | 0.2257920 |
| 20261026T001452Z_s1rd_mini-low_silent_floor_8ce3db_r052 | 52 | completed |  | 30/30 | 102.41 | 154 | 0 | 0 | OpenAI | 0.2294220 |
| 20261026T001452Z_s1rd_mini-low_silent_floor_8ce3db_r053 | 53 | completed |  | 30/30 | 106.31 | 154 | 0 | 0 | OpenAI | 0.2245100 |
| 20261026T001452Z_s1rd_mini-low_silent_floor_8ce3db_r054 | 54 | completed |  | 30/30 | 104.92 | 154 | 0 | 0 | OpenAI | 0.2229392 |
| 20261026T001452Z_s1rd_mini-low_silent_floor_8ce3db_r055 | 55 | completed |  | 30/30 | 111.65 | 154 | 0 | 0 | OpenAI | 0.2205528 |
| 20261026T001452Z_s1rd_mini-low_silent_floor_8ce3db_r056 | 56 | completed |  | 30/30 | 120.65 | 154 | 0 | 0 | OpenAI | 0.2254416 |

## Per round

Withheld: confirmatory run. Outcome tables (asks, bids, trades) are not written to reports until all Stage 2 blocks are complete (human message 24).
