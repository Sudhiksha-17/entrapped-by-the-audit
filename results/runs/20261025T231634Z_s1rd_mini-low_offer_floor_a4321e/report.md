# Run report: 20261025T231634Z_s1rd_mini-low_offer_floor_a4321e

Generated automatically by `sting/docs.py`. Facts only; no interpretation.

- Kind: episode_batch; stage: study1r_addon_D; run type: confirmatory
- Purpose: Study 1R-D confirmatory A_blocks_25-32 (human message 87)
- Command: `python -m sting.study1rd run configs/study1r_addon_D/campaign.yaml --arms mini-low_offer_floor,mini-low_silent_floor --indices 25,26,27,28,29,30,31,32 --approve-cost --purpose Study 1R-D confirmatory A_blocks_25-32 (human message 87)`
- Models: openrouter:openai/gpt-4.1-mini@openai
- Calls: 1232; tokens in 2,871,769; tokens out 425,076
- Cost: estimated $2.0040; actual $1.8106660 (OpenRouter-reported where available)
- Manifest: `results/runs/20261025T231634Z_s1rd_mini-low_offer_floor_a4321e/manifest.json` (committed copy of `runs/study1r_addon_D/20261025T231634Z_s1rd_mini-low_offer_floor_a4321e/manifest.json`)

- Rounds: 30; seller messaging: True; temperature: 0.7; boss_pressure: False
- Sting: last seller id, condition offer, mode message, rule follow, initial_ask 97.5, fixed_ask None
- Seller costs: [80.0, 80.0, 80.0]; buyer values: [100.0, 100.0, 100.0]; competitive equilibrium price (upstream `metrics.competitive_equilibrium`): 90.00
- Episodes: 8; completed 8; failed 0; failures by reason: {}; parse failures: 0
- Model identity (F-4): no snapshot change, no returned-model mismatch
- Provider unknown (OpenRouter response without provider field; fallbacks disabled): 0 calls
- Cost by role: buyer $1.0476324, probe $0.0378908, seller $0.7251428

## Episodes

| Replicate | Index | Status | Reason | Rounds | Wall s | Calls | Parse fails | Provider unknown | Routed providers | Cost $ |
|---|---|---|---|---|---|---|---|---|---|---|
| 20261025T231634Z_s1rd_mini-low_offer_floor_a4321e_r025 | 25 | completed |  | 30/30 | 112.3 | 154 | 0 | 0 | OpenAI | 0.2297764 |
| 20261025T231634Z_s1rd_mini-low_offer_floor_a4321e_r026 | 26 | completed |  | 30/30 | 104.1 | 154 | 0 | 0 | OpenAI | 0.2330092 |
| 20261025T231634Z_s1rd_mini-low_offer_floor_a4321e_r027 | 27 | completed |  | 30/30 | 110.64 | 154 | 0 | 0 | OpenAI | 0.2287956 |
| 20261025T231634Z_s1rd_mini-low_offer_floor_a4321e_r028 | 28 | completed |  | 30/30 | 100.41 | 154 | 0 | 0 | OpenAI | 0.2124748 |
| 20261025T231634Z_s1rd_mini-low_offer_floor_a4321e_r029 | 29 | completed |  | 30/30 | 97.48 | 154 | 0 | 0 | OpenAI | 0.2295104 |
| 20261025T231634Z_s1rd_mini-low_offer_floor_a4321e_r030 | 30 | completed |  | 30/30 | 105.6 | 154 | 0 | 0 | OpenAI | 0.2225456 |
| 20261025T231634Z_s1rd_mini-low_offer_floor_a4321e_r031 | 31 | completed |  | 30/30 | 99.04 | 154 | 0 | 0 | OpenAI | 0.2244528 |
| 20261025T231634Z_s1rd_mini-low_offer_floor_a4321e_r032 | 32 | completed |  | 30/30 | 116.32 | 154 | 0 | 0 | OpenAI | 0.2301012 |

## Per round

Withheld: confirmatory run. Outcome tables (asks, bids, trades) are not written to reports until all Stage 2 blocks are complete (human message 24).
