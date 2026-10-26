# Run report: 20261024T100744Z_study1r_mini-low_offer_72e5a2

Generated automatically by `sting/docs.py`. Facts only; no interpretation.

- Kind: episode_batch; stage: study1r; run type: confirmatory
- Purpose: Study 1R confirmatory blocks 41-48 (human message 67, step 2)
- Command: `python -m sting.stage2_runner configs/study1r/campaign.yaml --indices 41,42,43,44,45,46,47,48 --approve-cost --purpose Study 1R confirmatory blocks 41-48 (human message 67, step 2)`
- Models: openrouter:openai/gpt-4.1-mini@openai
- Calls: 1232; tokens in 2,918,243; tokens out 425,800
- Cost: estimated $1.9848; actual $1.8323340 (OpenRouter-reported where available)
- Manifest: `results/runs/20261024T100744Z_study1r_mini-low_offer_72e5a2/manifest.json` (committed copy of `runs/study1r/20261024T100744Z_study1r_mini-low_offer_72e5a2/manifest.json`)

- Rounds: 30; seller messaging: True; temperature: 0.7; boss_pressure: False
- Sting: last seller id, condition offer, mode message, rule follow, initial_ask 97.5, fixed_ask None
- Seller costs: [80.0, 80.0, 80.0]; buyer values: [100.0, 100.0, 100.0]; competitive equilibrium price (upstream `metrics.competitive_equilibrium`): 90.00
- Episodes: 8; completed 8; failed 0; failures by reason: {}; parse failures: 0
- Model identity (F-4): no snapshot change, no returned-model mismatch
- Provider unknown (OpenRouter response without provider field; fallbacks disabled): 0 calls
- Cost by role: buyer $1.0565584, probe $0.0368168, seller $0.7389588

## Episodes

| Replicate | Index | Status | Reason | Rounds | Wall s | Calls | Parse fails | Provider unknown | Routed providers | Cost $ |
|---|---|---|---|---|---|---|---|---|---|---|
| 20261024T100744Z_study1r_mini-low_offer_72e5a2_r041 | 41 | completed |  | 30/30 | 102.66 | 154 | 0 | 0 | OpenAI | 0.2315832 |
| 20261024T100744Z_study1r_mini-low_offer_72e5a2_r042 | 42 | completed |  | 30/30 | 105.24 | 154 | 0 | 0 | OpenAI | 0.2267656 |
| 20261024T100744Z_study1r_mini-low_offer_72e5a2_r043 | 43 | completed |  | 30/30 | 109.11 | 154 | 0 | 0 | OpenAI | 0.2297196 |
| 20261024T100744Z_study1r_mini-low_offer_72e5a2_r044 | 44 | completed |  | 30/30 | 112.93 | 154 | 0 | 0 | OpenAI | 0.2325308 |
| 20261024T100744Z_study1r_mini-low_offer_72e5a2_r045 | 45 | completed |  | 30/30 | 98.48 | 154 | 0 | 0 | OpenAI | 0.2273324 |
| 20261024T100744Z_study1r_mini-low_offer_72e5a2_r046 | 46 | completed |  | 30/30 | 99.4 | 154 | 0 | 0 | OpenAI | 0.2280748 |
| 20261024T100744Z_study1r_mini-low_offer_72e5a2_r047 | 47 | completed |  | 30/30 | 118.16 | 154 | 0 | 0 | OpenAI | 0.2247536 |
| 20261024T100744Z_study1r_mini-low_offer_72e5a2_r048 | 48 | completed |  | 30/30 | 135.52 | 154 | 0 | 0 | OpenAI | 0.2315740 |

## Per round

Withheld: confirmatory run. Outcome tables (asks, bids, trades) are not written to reports until all Stage 2 blocks are complete (human message 24).
