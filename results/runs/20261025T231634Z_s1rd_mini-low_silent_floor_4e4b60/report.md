# Run report: 20261025T231634Z_s1rd_mini-low_silent_floor_4e4b60

Generated automatically by `sting/docs.py`. Facts only; no interpretation.

- Kind: episode_batch; stage: study1r_addon_D; run type: confirmatory
- Purpose: Study 1R-D confirmatory A_blocks_25-32 (human message 87)
- Command: `python -m sting.study1rd run configs/study1r_addon_D/campaign.yaml --arms mini-low_offer_floor,mini-low_silent_floor --indices 25,26,27,28,29,30,31,32 --approve-cost --purpose Study 1R-D confirmatory A_blocks_25-32 (human message 87)`
- Models: openrouter:openai/gpt-4.1-mini@openai
- Calls: 1252; tokens in 2,902,701; tokens out 427,110
- Cost: estimated $1.9784; actual $1.8290196 (OpenRouter-reported where available)
- Manifest: `results/runs/20261025T231634Z_s1rd_mini-low_silent_floor_4e4b60/manifest.json` (committed copy of `runs/study1r_addon_D/20261025T231634Z_s1rd_mini-low_silent_floor_4e4b60/manifest.json`)

- Rounds: 30; seller messaging: True; temperature: 0.7; boss_pressure: False
- Sting: last seller id, condition silent, mode silent, rule follow, initial_ask 97.5, fixed_ask None
- Seller costs: [80.0, 80.0, 80.0]; buyer values: [100.0, 100.0, 100.0]; competitive equilibrium price (upstream `metrics.competitive_equilibrium`): 90.00
- Episodes: 9; completed 8; failed 1; failures by reason: {'other': 1}; parse failures: 0
- Model identity (F-4): no snapshot change, no returned-model mismatch
- Provider unknown (OpenRouter response without provider field; fallbacks disabled): 0 calls
- Cost by role: buyer $1.0682188, probe $0.0384804, seller $0.7223204

## Episodes

| Replicate | Index | Status | Reason | Rounds | Wall s | Calls | Parse fails | Provider unknown | Routed providers | Cost $ |
|---|---|---|---|---|---|---|---|---|---|---|
| 20261025T231634Z_s1rd_mini-low_silent_floor_4e4b60_r025 | 25 | completed |  | 30/30 | 111.14 | 154 | 0 | 0 | OpenAI | 0.2265272 |
| 20261025T231634Z_s1rd_mini-low_silent_floor_4e4b60_r026 | 26 | completed |  | 30/30 | 97.93 | 154 | 0 | 0 | OpenAI | 0.2248004 |
| 20261025T231634Z_s1rd_mini-low_silent_floor_4e4b60_r027 | 27 | completed |  | 30/30 | 103.61 | 154 | 0 | 0 | OpenAI | 0.2252920 |
| 20261025T231634Z_s1rd_mini-low_silent_floor_4e4b60_r028 | 28 | completed |  | 30/30 | 102.87 | 154 | 0 | 0 | OpenAI | 0.2295444 |
| 20261025T231634Z_s1rd_mini-low_silent_floor_4e4b60_r029 | 29 | completed |  | 30/30 | 102.76 | 154 | 0 | 0 | OpenAI | 0.2265168 |
| 20261025T231634Z_s1rd_mini-low_silent_floor_4e4b60_r030 | 30 | completed |  | 30/30 | 110.74 | 154 | 0 | 0 | OpenAI | 0.2266376 |
| 20261025T231634Z_s1rd_mini-low_silent_floor_4e4b60_r031 | 31 | completed |  | 30/30 | 127.29 | 154 | 0 | 0 | OpenAI | 0.2249496 |
| 20261025T231634Z_s1rd_mini-low_silent_floor_4e4b60_r032 | 32 | failed | other | 3/30 | 13.38 | 20 | 0 | 0 | OpenAI | 0.0188696 |
| 20261025T231634Z_s1rd_mini-low_silent_floor_4e4b60_r032_repl1 | 32 | completed |  | 30/30 | 104.47 | 154 | 0 | 0 | OpenAI | 0.2258820 |

## Per round

Withheld: confirmatory run. Outcome tables (asks, bids, trades) are not written to reports until all Stage 2 blocks are complete (human message 24).
