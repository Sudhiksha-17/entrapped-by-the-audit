# Run report: 20261024T102352Z_study1r_mini-low_offer_c509ea

Generated automatically by `sting/docs.py`. Facts only; no interpretation.

- Kind: episode_batch; stage: study1r; run type: confirmatory
- Purpose: Study 1R confirmatory blocks 49-56 (human message 67, step 2)
- Command: `python -m sting.stage2_runner configs/study1r/campaign.yaml --indices 49,50,51,52,53,54,55,56 --approve-cost --purpose Study 1R confirmatory blocks 49-56 (human message 67, step 2)`
- Models: openrouter:openai/gpt-4.1-mini@openai
- Calls: 1232; tokens in 2,785,283; tokens out 427,294
- Cost: estimated $1.9848; actual $1.7849964 (OpenRouter-reported where available)
- Manifest: `results/runs/20261024T102352Z_study1r_mini-low_offer_c509ea/manifest.json` (committed copy of `runs/study1r/20261024T102352Z_study1r_mini-low_offer_c509ea/manifest.json`)

- Rounds: 30; seller messaging: True; temperature: 0.7; boss_pressure: False
- Sting: last seller id, condition offer, mode message, rule follow, initial_ask 97.5, fixed_ask None
- Seller costs: [80.0, 80.0, 80.0]; buyer values: [100.0, 100.0, 100.0]; competitive equilibrium price (upstream `metrics.competitive_equilibrium`): 90.00
- Episodes: 8; completed 8; failed 0; failures by reason: {}; parse failures: 0
- Model identity (F-4): no snapshot change, no returned-model mismatch
- Provider unknown (OpenRouter response without provider field; fallbacks disabled): 0 calls
- Cost by role: buyer $1.0328580, probe $0.0385024, seller $0.7136360

## Episodes

| Replicate | Index | Status | Reason | Rounds | Wall s | Calls | Parse fails | Provider unknown | Routed providers | Cost $ |
|---|---|---|---|---|---|---|---|---|---|---|
| 20261024T102352Z_study1r_mini-low_offer_c509ea_r049 | 49 | completed |  | 30/30 | 113.4 | 154 | 0 | 0 | OpenAI | 0.2250448 |
| 20261024T102352Z_study1r_mini-low_offer_c509ea_r050 | 50 | completed |  | 30/30 | 125.37 | 154 | 0 | 0 | OpenAI | 0.2174072 |
| 20261024T102352Z_study1r_mini-low_offer_c509ea_r051 | 51 | completed |  | 30/30 | 105.15 | 154 | 0 | 0 | OpenAI | 0.2352056 |
| 20261024T102352Z_study1r_mini-low_offer_c509ea_r052 | 52 | completed |  | 30/30 | 125.14 | 154 | 0 | 0 | OpenAI | 0.2274536 |
| 20261024T102352Z_study1r_mini-low_offer_c509ea_r053 | 53 | completed |  | 30/30 | 97.55 | 154 | 0 | 0 | OpenAI | 0.2211400 |
| 20261024T102352Z_study1r_mini-low_offer_c509ea_r054 | 54 | completed |  | 30/30 | 122.62 | 154 | 0 | 0 | OpenAI | 0.2072240 |
| 20261024T102352Z_study1r_mini-low_offer_c509ea_r055 | 55 | completed |  | 30/30 | 121.12 | 154 | 0 | 0 | OpenAI | 0.2271584 |
| 20261024T102352Z_study1r_mini-low_offer_c509ea_r056 | 56 | completed |  | 30/30 | 121.92 | 154 | 0 | 0 | OpenAI | 0.2243628 |

## Per round

Withheld: confirmatory run. Outcome tables (asks, bids, trades) are not written to reports until all Stage 2 blocks are complete (human message 24).
