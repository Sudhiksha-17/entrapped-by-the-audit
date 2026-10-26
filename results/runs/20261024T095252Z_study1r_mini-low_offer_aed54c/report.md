# Run report: 20261024T095252Z_study1r_mini-low_offer_aed54c

Generated automatically by `sting/docs.py`. Facts only; no interpretation.

- Kind: episode_batch; stage: study1r; run type: confirmatory
- Purpose: Study 1R confirmatory blocks 33-40 (human message 67, step 2)
- Command: `python -m sting.stage2_runner configs/study1r/campaign.yaml --indices 33,34,35,36,37,38,39,40 --approve-cost --purpose Study 1R confirmatory blocks 33-40 (human message 67, step 2)`
- Models: openrouter:openai/gpt-4.1-mini@openai
- Calls: 1232; tokens in 2,923,719; tokens out 424,901
- Cost: estimated $1.9848; actual $1.8362732 (OpenRouter-reported where available)
- Manifest: `results/runs/20261024T095252Z_study1r_mini-low_offer_aed54c/manifest.json` (committed copy of `runs/study1r/20261024T095252Z_study1r_mini-low_offer_aed54c/manifest.json`)

- Rounds: 30; seller messaging: True; temperature: 0.7; boss_pressure: False
- Sting: last seller id, condition offer, mode message, rule follow, initial_ask 97.5, fixed_ask None
- Seller costs: [80.0, 80.0, 80.0]; buyer values: [100.0, 100.0, 100.0]; competitive equilibrium price (upstream `metrics.competitive_equilibrium`): 90.00
- Episodes: 8; completed 8; failed 0; failures by reason: {}; parse failures: 0
- Model identity (F-4): no snapshot change, no returned-model mismatch
- Provider unknown (OpenRouter response without provider field; fallbacks disabled): 0 calls
- Cost by role: buyer $1.0627272, probe $0.0400040, seller $0.7335420

## Episodes

| Replicate | Index | Status | Reason | Rounds | Wall s | Calls | Parse fails | Provider unknown | Routed providers | Cost $ |
|---|---|---|---|---|---|---|---|---|---|---|
| 20261024T095252Z_study1r_mini-low_offer_aed54c_r033 | 33 | completed |  | 30/30 | 100.04 | 154 | 0 | 0 | OpenAI | 0.2294380 |
| 20261024T095252Z_study1r_mini-low_offer_aed54c_r034 | 34 | completed |  | 30/30 | 101.25 | 154 | 0 | 0 | OpenAI | 0.2262604 |
| 20261024T095252Z_study1r_mini-low_offer_aed54c_r035 | 35 | completed |  | 30/30 | 114.64 | 154 | 0 | 0 | OpenAI | 0.2315516 |
| 20261024T095252Z_study1r_mini-low_offer_aed54c_r036 | 36 | completed |  | 30/30 | 100.25 | 154 | 0 | 0 | OpenAI | 0.2319648 |
| 20261024T095252Z_study1r_mini-low_offer_aed54c_r037 | 37 | completed |  | 30/30 | 103.27 | 154 | 0 | 0 | OpenAI | 0.2283596 |
| 20261024T095252Z_study1r_mini-low_offer_aed54c_r038 | 38 | completed |  | 30/30 | 121.49 | 154 | 0 | 0 | OpenAI | 0.2270956 |
| 20261024T095252Z_study1r_mini-low_offer_aed54c_r039 | 39 | completed |  | 30/30 | 97.79 | 154 | 0 | 0 | OpenAI | 0.2320016 |
| 20261024T095252Z_study1r_mini-low_offer_aed54c_r040 | 40 | completed |  | 30/30 | 101.95 | 154 | 0 | 0 | OpenAI | 0.2296016 |

## Per round

Withheld: confirmatory run. Outcome tables (asks, bids, trades) are not written to reports until all Stage 2 blocks are complete (human message 24).
