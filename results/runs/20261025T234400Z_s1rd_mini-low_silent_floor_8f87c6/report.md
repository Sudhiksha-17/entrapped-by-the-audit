# Run report: 20261025T234400Z_s1rd_mini-low_silent_floor_8f87c6

Generated automatically by `sting/docs.py`. Facts only; no interpretation.

- Kind: episode_batch; stage: study1r_addon_D; run type: confirmatory
- Purpose: Study 1R-D confirmatory A_blocks_33-40 (human message 89)
- Command: `python -m sting.study1rd run configs/study1r_addon_D/campaign.yaml --arms mini-low_offer_floor,mini-low_silent_floor --indices 33,34,35,36,37,38,39,40 --approve-cost --purpose Study 1R-D confirmatory A_blocks_33-40 (human message 89)`
- Models: openrouter:openai/gpt-4.1-mini@openai
- Calls: 1232; tokens in 2,854,032; tokens out 423,026
- Cost: estimated $1.9784; actual $1.8014048 (OpenRouter-reported where available)
- Manifest: `results/runs/20261025T234400Z_s1rd_mini-low_silent_floor_8f87c6/manifest.json` (committed copy of `runs/study1r_addon_D/20261025T234400Z_s1rd_mini-low_silent_floor_8f87c6/manifest.json`)

- Rounds: 30; seller messaging: True; temperature: 0.7; boss_pressure: False
- Sting: last seller id, condition silent, mode silent, rule follow, initial_ask 97.5, fixed_ask None
- Seller costs: [80.0, 80.0, 80.0]; buyer values: [100.0, 100.0, 100.0]; competitive equilibrium price (upstream `metrics.competitive_equilibrium`): 90.00
- Episodes: 8; completed 8; failed 0; failures by reason: {}; parse failures: 0
- Model identity (F-4): no snapshot change, no returned-model mismatch
- Provider unknown (OpenRouter response without provider field; fallbacks disabled): 0 calls
- Cost by role: buyer $1.0585980, probe $0.0346112, seller $0.7081956

## Episodes

| Replicate | Index | Status | Reason | Rounds | Wall s | Calls | Parse fails | Provider unknown | Routed providers | Cost $ |
|---|---|---|---|---|---|---|---|---|---|---|
| 20261025T234400Z_s1rd_mini-low_silent_floor_8f87c6_r033 | 33 | completed |  | 30/30 | 117.26 | 154 | 0 | 0 | OpenAI | 0.2252532 |
| 20261025T234400Z_s1rd_mini-low_silent_floor_8f87c6_r034 | 34 | completed |  | 30/30 | 99.02 | 154 | 0 | 0 | OpenAI | 0.2230596 |
| 20261025T234400Z_s1rd_mini-low_silent_floor_8f87c6_r035 | 35 | completed |  | 30/30 | 105.74 | 154 | 0 | 0 | OpenAI | 0.2232576 |
| 20261025T234400Z_s1rd_mini-low_silent_floor_8f87c6_r036 | 36 | completed |  | 30/30 | 104.67 | 154 | 0 | 0 | OpenAI | 0.2226028 |
| 20261025T234400Z_s1rd_mini-low_silent_floor_8f87c6_r037 | 37 | completed |  | 30/30 | 101.6 | 154 | 0 | 0 | OpenAI | 0.2309324 |
| 20261025T234400Z_s1rd_mini-low_silent_floor_8f87c6_r038 | 38 | completed |  | 30/30 | 103.6 | 154 | 0 | 0 | OpenAI | 0.2247996 |
| 20261025T234400Z_s1rd_mini-low_silent_floor_8f87c6_r039 | 39 | completed |  | 30/30 | 98.17 | 154 | 0 | 0 | OpenAI | 0.2202244 |
| 20261025T234400Z_s1rd_mini-low_silent_floor_8f87c6_r040 | 40 | completed |  | 30/30 | 108.33 | 154 | 0 | 0 | OpenAI | 0.2312752 |

## Per round

Withheld: confirmatory run. Outcome tables (asks, bids, trades) are not written to reports until all Stage 2 blocks are complete (human message 24).
