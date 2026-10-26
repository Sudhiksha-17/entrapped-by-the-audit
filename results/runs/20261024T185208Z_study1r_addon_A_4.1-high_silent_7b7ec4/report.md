# Run report: 20261024T185208Z_study1r_addon_A_4.1-high_silent_7b7ec4

Generated automatically by `sting/docs.py`. Facts only; no interpretation.

- Kind: episode_batch; stage: study1r_addon_A; run type: confirmatory
- Purpose: Study 1R-A confirmatory blocks 1-8 (human message 71)
- Command: `python -m sting.stage2_runner configs/study1r_addon_A/campaign.yaml --indices 1,2,3,4,5,6,7,8 --approve-cost --purpose Study 1R-A confirmatory blocks 1-8 (human message 71)`
- Models: openrouter:openai/gpt-4.1@openai
- Calls: 1232; tokens in 2,163,870; tokens out 440,497
- Cost: estimated $8.8688; actual $7.8052520 (OpenRouter-reported where available)
- Manifest: `results/runs/20261024T185208Z_study1r_addon_A_4.1-high_silent_7b7ec4/manifest.json` (committed copy of `runs/study1r_addon_A/20261024T185208Z_study1r_addon_A_4.1-high_silent_7b7ec4/manifest.json`)

- Rounds: 30; seller messaging: True; temperature: 0.7; boss_pressure: False
- Sting: last seller id, condition silent, mode silent, rule follow, initial_ask 97.5, fixed_ask None
- Seller costs: [80.0, 80.0, 80.0]; buyer values: [100.0, 100.0, 100.0]; competitive equilibrium price (upstream `metrics.competitive_equilibrium`): 90.00
- Episodes: 8; completed 8; failed 0; failures by reason: {}; parse failures: 0
- Model identity (F-4): no snapshot change, no returned-model mismatch
- Provider unknown (OpenRouter response without provider field; fallbacks disabled): 0 calls
- Cost by role: buyer $4.4587660, probe $0.1835880, seller $3.1628980

## Episodes

| Replicate | Index | Status | Reason | Rounds | Wall s | Calls | Parse fails | Provider unknown | Routed providers | Cost $ |
|---|---|---|---|---|---|---|---|---|---|---|
| 20261024T185208Z_study1r_addon_A_4.1-high_silent_7b7ec4_r001 | 1 | completed |  | 30/30 | 120.25 | 154 | 0 | 0 | OpenAI | 0.9590860 |
| 20261024T185208Z_study1r_addon_A_4.1-high_silent_7b7ec4_r002 | 2 | completed |  | 30/30 | 124.97 | 154 | 0 | 0 | OpenAI | 0.9727200 |
| 20261024T185208Z_study1r_addon_A_4.1-high_silent_7b7ec4_r003 | 3 | completed |  | 30/30 | 126.34 | 154 | 0 | 0 | OpenAI | 0.9833540 |
| 20261024T185208Z_study1r_addon_A_4.1-high_silent_7b7ec4_r004 | 4 | completed |  | 30/30 | 162.82 | 154 | 0 | 0 | OpenAI | 0.9665200 |
| 20261024T185208Z_study1r_addon_A_4.1-high_silent_7b7ec4_r005 | 5 | completed |  | 30/30 | 132.13 | 154 | 0 | 0 | OpenAI | 0.9770480 |
| 20261024T185208Z_study1r_addon_A_4.1-high_silent_7b7ec4_r006 | 6 | completed |  | 30/30 | 128.24 | 154 | 0 | 0 | OpenAI | 0.9734460 |
| 20261024T185208Z_study1r_addon_A_4.1-high_silent_7b7ec4_r007 | 7 | completed |  | 30/30 | 115.72 | 154 | 0 | 0 | OpenAI | 0.9964660 |
| 20261024T185208Z_study1r_addon_A_4.1-high_silent_7b7ec4_r008 | 8 | completed |  | 30/30 | 174.43 | 154 | 0 | 0 | OpenAI | 0.9766120 |

## Per round

Withheld: confirmatory run. Outcome tables (asks, bids, trades) are not written to reports until all Stage 2 blocks are complete (human message 24).
