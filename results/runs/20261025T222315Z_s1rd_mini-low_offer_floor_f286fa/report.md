# Run report: 20261025T222315Z_s1rd_mini-low_offer_floor_f286fa

Generated automatically by `sting/docs.py`. Facts only; no interpretation.

- Kind: episode_batch; stage: study1r_addon_D; run type: confirmatory
- Purpose: Study 1R-D confirmatory A_blocks_17-24 (human message 87)
- Command: `python -m sting.study1rd run configs/study1r_addon_D/campaign.yaml --arms mini-low_offer_floor,mini-low_silent_floor --indices 17,18,19,20,21,22,23,24 --approve-cost --purpose Study 1R-D confirmatory A_blocks_17-24 (human message 87)`
- Models: openrouter:openai/gpt-4.1-mini@openai
- Calls: 1253; tokens in 2,898,302; tokens out 437,023
- Cost: estimated $2.0040; actual $1.8423144 (OpenRouter-reported where available)
- Manifest: `results/runs/20261025T222315Z_s1rd_mini-low_offer_floor_f286fa/manifest.json` (committed copy of `runs/study1r_addon_D/20261025T222315Z_s1rd_mini-low_offer_floor_f286fa/manifest.json`)

- Rounds: 30; seller messaging: True; temperature: 0.7; boss_pressure: False
- Sting: last seller id, condition offer, mode message, rule follow, initial_ask 97.5, fixed_ask None
- Seller costs: [80.0, 80.0, 80.0]; buyer values: [100.0, 100.0, 100.0]; competitive equilibrium price (upstream `metrics.competitive_equilibrium`): 90.00
- Episodes: 9; completed 8; failed 1; failures by reason: {'other': 1}; parse failures: 0
- Model identity (F-4): no snapshot change, no returned-model mismatch
- Provider unknown (OpenRouter response without provider field; fallbacks disabled): 0 calls
- Cost by role: buyer $1.0688620, probe $0.0369020, seller $0.7365504

## Episodes

| Replicate | Index | Status | Reason | Rounds | Wall s | Calls | Parse fails | Provider unknown | Routed providers | Cost $ |
|---|---|---|---|---|---|---|---|---|---|---|
| 20261025T222315Z_s1rd_mini-low_offer_floor_f286fa_r017 | 17 | completed |  | 30/30 | 107.11 | 154 | 0 | 0 | OpenAI | 0.2292576 |
| 20261025T222315Z_s1rd_mini-low_offer_floor_f286fa_r018 | 18 | completed |  | 30/30 | 109.57 | 154 | 0 | 0 | OpenAI | 0.2285788 |
| 20261025T222315Z_s1rd_mini-low_offer_floor_f286fa_r019 | 19 | completed |  | 30/30 | 97.72 | 154 | 0 | 0 | OpenAI | 0.2239368 |
| 20261025T222315Z_s1rd_mini-low_offer_floor_f286fa_r020 | 20 | completed |  | 30/30 | 113.85 | 154 | 0 | 0 | OpenAI | 0.2250800 |
| 20261025T222315Z_s1rd_mini-low_offer_floor_f286fa_r021 | 21 | completed |  | 30/30 | 179.14 | 155 | 0 | 0 | OpenAI | 0.2221560 |
| 20261025T222315Z_s1rd_mini-low_offer_floor_f286fa_r022 | 22 | failed | other | 3/30 | 16.68 | 20 | 0 | 0 | OpenAI | 0.0187996 |
| 20261025T222315Z_s1rd_mini-low_offer_floor_f286fa_r022_repl1 | 22 | completed |  | 30/30 | 110.64 | 154 | 0 | 0 | OpenAI | 0.2303460 |
| 20261025T222315Z_s1rd_mini-low_offer_floor_f286fa_r023 | 23 | completed |  | 30/30 | 101.48 | 154 | 0 | 0 | OpenAI | 0.2318004 |
| 20261025T222315Z_s1rd_mini-low_offer_floor_f286fa_r024 | 24 | completed |  | 30/30 | 98.82 | 154 | 0 | 0 | OpenAI | 0.2323592 |

## Per round

Withheld: confirmatory run. Outcome tables (asks, bids, trades) are not written to reports until all Stage 2 blocks are complete (human message 24).
