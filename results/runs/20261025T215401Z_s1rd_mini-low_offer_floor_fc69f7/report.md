# Run report: 20261025T215401Z_s1rd_mini-low_offer_floor_fc69f7

Generated automatically by `sting/docs.py`. Facts only; no interpretation.

- Kind: episode_batch; stage: study1r_addon_D; run type: confirmatory
- Purpose: Study 1R-D confirmatory A_blocks_1-8 (human message 87)
- Command: `python -m sting.study1rd run configs/study1r_addon_D/campaign.yaml --arms mini-low_offer_floor,mini-low_silent_floor --indices 1,2,3,4,5,6,7,8 --approve-cost --purpose Study 1R-D confirmatory A_blocks_1-8 (human message 87)`
- Models: openrouter:openai/gpt-4.1-mini@openai
- Calls: 1232; tokens in 2,922,646; tokens out 424,281
- Cost: estimated $2.0040; actual $1.8313960 (OpenRouter-reported where available)
- Manifest: `results/runs/20261025T215401Z_s1rd_mini-low_offer_floor_fc69f7/manifest.json` (committed copy of `runs/study1r_addon_D/20261025T215401Z_s1rd_mini-low_offer_floor_fc69f7/manifest.json`)

- Rounds: 30; seller messaging: True; temperature: 0.7; boss_pressure: False
- Sting: last seller id, condition offer, mode message, rule follow, initial_ask 97.5, fixed_ask None
- Seller costs: [80.0, 80.0, 80.0]; buyer values: [100.0, 100.0, 100.0]; competitive equilibrium price (upstream `metrics.competitive_equilibrium`): 90.00
- Episodes: 8; completed 8; failed 0; failures by reason: {}; parse failures: 0
- Model identity (F-4): no snapshot change, no returned-model mismatch
- Provider unknown (OpenRouter response without provider field; fallbacks disabled): 0 calls
- Cost by role: buyer $1.0584412, probe $0.0368020, seller $0.7361528

## Episodes

| Replicate | Index | Status | Reason | Rounds | Wall s | Calls | Parse fails | Provider unknown | Routed providers | Cost $ |
|---|---|---|---|---|---|---|---|---|---|---|
| 20261025T215401Z_s1rd_mini-low_offer_floor_fc69f7_r001 | 1 | completed |  | 30/30 | 98.09 | 154 | 0 | 0 | OpenAI | 0.2264612 |
| 20261025T215401Z_s1rd_mini-low_offer_floor_fc69f7_r002 | 2 | completed |  | 30/30 | 99.83 | 154 | 0 | 0 | OpenAI | 0.2283592 |
| 20261025T215401Z_s1rd_mini-low_offer_floor_fc69f7_r003 | 3 | completed |  | 30/30 | 100.92 | 154 | 0 | 0 | OpenAI | 0.2284588 |
| 20261025T215401Z_s1rd_mini-low_offer_floor_fc69f7_r004 | 4 | completed |  | 30/30 | 111.51 | 154 | 0 | 0 | OpenAI | 0.2300552 |
| 20261025T215401Z_s1rd_mini-low_offer_floor_fc69f7_r005 | 5 | completed |  | 30/30 | 112.66 | 154 | 0 | 0 | OpenAI | 0.2315936 |
| 20261025T215401Z_s1rd_mini-low_offer_floor_fc69f7_r006 | 6 | completed |  | 30/30 | 116.62 | 154 | 0 | 0 | OpenAI | 0.2311496 |
| 20261025T215401Z_s1rd_mini-low_offer_floor_fc69f7_r007 | 7 | completed |  | 30/30 | 102.52 | 154 | 0 | 0 | OpenAI | 0.2232832 |
| 20261025T215401Z_s1rd_mini-low_offer_floor_fc69f7_r008 | 8 | completed |  | 30/30 | 110.37 | 154 | 0 | 0 | OpenAI | 0.2320352 |

## Per round

Withheld: confirmatory run. Outcome tables (asks, bids, trades) are not written to reports until all Stage 2 blocks are complete (human message 24).
