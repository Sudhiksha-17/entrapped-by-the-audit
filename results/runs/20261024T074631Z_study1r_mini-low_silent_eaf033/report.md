# Run report: 20261024T074631Z_study1r_mini-low_silent_eaf033

Generated automatically by `sting/docs.py`. Facts only; no interpretation.

- Kind: episode_batch; stage: study1r; run type: confirmatory
- Purpose: Study 1R confirmatory blocks 9-16 (human message 67, step 2)
- Command: `python -m sting.stage2_runner configs/study1r/campaign.yaml --indices 9,10,11,12,13,14,15,16 --approve-cost --purpose Study 1R confirmatory blocks 9-16 (human message 67, step 2)`
- Models: openrouter:openai/gpt-4.1-mini@openai
- Calls: 1232; tokens in 2,882,512; tokens out 404,447
- Cost: estimated $1.9848; actual $1.7867568 (OpenRouter-reported where available)
- Manifest: `results/runs/20261024T074631Z_study1r_mini-low_silent_eaf033/manifest.json` (committed copy of `runs/study1r/20261024T074631Z_study1r_mini-low_silent_eaf033/manifest.json`)

- Rounds: 30; seller messaging: True; temperature: 0.7; boss_pressure: False
- Sting: last seller id, condition silent, mode silent, rule follow, initial_ask 97.5, fixed_ask None
- Seller costs: [80.0, 80.0, 80.0]; buyer values: [100.0, 100.0, 100.0]; competitive equilibrium price (upstream `metrics.competitive_equilibrium`): 90.00
- Episodes: 8; completed 8; failed 0; failures by reason: {}; parse failures: 0
- Model identity (F-4): no snapshot change, no returned-model mismatch
- Provider unknown (OpenRouter response without provider field; fallbacks disabled): 0 calls
- Cost by role: buyer $1.0436408, probe $0.0372860, seller $0.7058300

## Episodes

| Replicate | Index | Status | Reason | Rounds | Wall s | Calls | Parse fails | Provider unknown | Routed providers | Cost $ |
|---|---|---|---|---|---|---|---|---|---|---|
| 20261024T074631Z_study1r_mini-low_silent_eaf033_r009 | 9 | completed |  | 30/30 | 97.74 | 154 | 0 | 0 | OpenAI | 0.2181664 |
| 20261024T074631Z_study1r_mini-low_silent_eaf033_r010 | 10 | completed |  | 30/30 | 94.54 | 154 | 0 | 0 | OpenAI | 0.2264076 |
| 20261024T074631Z_study1r_mini-low_silent_eaf033_r011 | 11 | completed |  | 30/30 | 97.2 | 154 | 0 | 0 | OpenAI | 0.2253916 |
| 20261024T074631Z_study1r_mini-low_silent_eaf033_r012 | 12 | completed |  | 30/30 | 102.66 | 154 | 0 | 0 | OpenAI | 0.2220444 |
| 20261024T074631Z_study1r_mini-low_silent_eaf033_r013 | 13 | completed |  | 30/30 | 98.09 | 154 | 0 | 0 | OpenAI | 0.2223692 |
| 20261024T074631Z_study1r_mini-low_silent_eaf033_r014 | 14 | completed |  | 30/30 | 125.63 | 154 | 0 | 0 | OpenAI | 0.2215472 |
| 20261024T074631Z_study1r_mini-low_silent_eaf033_r015 | 15 | completed |  | 30/30 | 108.74 | 154 | 0 | 0 | OpenAI | 0.2250584 |
| 20261024T074631Z_study1r_mini-low_silent_eaf033_r016 | 16 | completed |  | 30/30 | 124.23 | 154 | 0 | 0 | OpenAI | 0.2257720 |

## Per round

Withheld: confirmatory run. Outcome tables (asks, bids, trades) are not written to reports until all Stage 2 blocks are complete (human message 24).
