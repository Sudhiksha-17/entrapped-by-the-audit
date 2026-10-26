# Run report: 20261024T103951Z_study1r_mini-low_offer_eb9457

Generated automatically by `sting/docs.py`. Facts only; no interpretation.

- Kind: episode_batch; stage: study1r; run type: confirmatory
- Purpose: Study 1R confirmatory blocks 57-59 (human message 67, step 2)
- Command: `python -m sting.stage2_runner configs/study1r/campaign.yaml --indices 57,58,59 --approve-cost --purpose Study 1R confirmatory blocks 57-59 (human message 67, step 2)`
- Models: openrouter:openai/gpt-4.1-mini@openai
- Calls: 462; tokens in 1,102,918; tokens out 161,320
- Cost: estimated $0.7443; actual $0.6926744 (OpenRouter-reported where available)
- Manifest: `results/runs/20261024T103951Z_study1r_mini-low_offer_eb9457/manifest.json` (committed copy of `runs/study1r/20261024T103951Z_study1r_mini-low_offer_eb9457/manifest.json`)

- Rounds: 30; seller messaging: True; temperature: 0.7; boss_pressure: False
- Sting: last seller id, condition offer, mode message, rule follow, initial_ask 97.5, fixed_ask None
- Seller costs: [80.0, 80.0, 80.0]; buyer values: [100.0, 100.0, 100.0]; competitive equilibrium price (upstream `metrics.competitive_equilibrium`): 90.00
- Episodes: 3; completed 3; failed 0; failures by reason: {}; parse failures: 0
- Model identity (F-4): no snapshot change, no returned-model mismatch
- Provider unknown (OpenRouter response without provider field; fallbacks disabled): 0 calls
- Cost by role: buyer $0.3978808, probe $0.0136428, seller $0.2811508

## Episodes

| Replicate | Index | Status | Reason | Rounds | Wall s | Calls | Parse fails | Provider unknown | Routed providers | Cost $ |
|---|---|---|---|---|---|---|---|---|---|---|
| 20261024T103951Z_study1r_mini-low_offer_eb9457_r057 | 57 | completed |  | 30/30 | 107.52 | 154 | 0 | 0 | OpenAI | 0.2304560 |
| 20261024T103951Z_study1r_mini-low_offer_eb9457_r058 | 58 | completed |  | 30/30 | 109.84 | 154 | 0 | 0 | OpenAI | 0.2297048 |
| 20261024T103951Z_study1r_mini-low_offer_eb9457_r059 | 59 | completed |  | 30/30 | 98.7 | 154 | 0 | 0 | OpenAI | 0.2325136 |

## Per round

Withheld: confirmatory run. Outcome tables (asks, bids, trades) are not written to reports until all Stage 2 blocks are complete (human message 24).
