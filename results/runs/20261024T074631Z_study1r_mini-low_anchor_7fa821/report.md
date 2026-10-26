# Run report: 20261024T074631Z_study1r_mini-low_anchor_7fa821

Generated automatically by `sting/docs.py`. Facts only; no interpretation.

- Kind: episode_batch; stage: study1r; run type: confirmatory
- Purpose: Study 1R confirmatory blocks 9-16 (human message 67, step 2)
- Command: `python -m sting.stage2_runner configs/study1r/campaign.yaml --indices 9,10,11,12,13,14,15,16 --approve-cost --purpose Study 1R confirmatory blocks 9-16 (human message 67, step 2)`
- Models: openrouter:openai/gpt-4.1-mini@openai
- Calls: 1232; tokens in 2,851,355; tokens out 421,968
- Cost: estimated $1.9848; actual $1.8017900 (OpenRouter-reported where available)
- Manifest: `results/runs/20261024T074631Z_study1r_mini-low_anchor_7fa821/manifest.json` (committed copy of `runs/study1r/20261024T074631Z_study1r_mini-low_anchor_7fa821/manifest.json`)

- Rounds: 30; seller messaging: True; temperature: 0.7; boss_pressure: False
- Sting: last seller id, condition anchor, mode message, rule follow, initial_ask 97.5, fixed_ask None
- Seller costs: [80.0, 80.0, 80.0]; buyer values: [100.0, 100.0, 100.0]; competitive equilibrium price (upstream `metrics.competitive_equilibrium`): 90.00
- Episodes: 8; completed 8; failed 0; failures by reason: {}; parse failures: 0
- Model identity (F-4): no snapshot change, no returned-model mismatch
- Provider unknown (OpenRouter response without provider field; fallbacks disabled): 0 calls
- Cost by role: buyer $1.0505992, probe $0.0380052, seller $0.7131856

## Episodes

| Replicate | Index | Status | Reason | Rounds | Wall s | Calls | Parse fails | Provider unknown | Routed providers | Cost $ |
|---|---|---|---|---|---|---|---|---|---|---|
| 20261024T074631Z_study1r_mini-low_anchor_7fa821_r009 | 9 | completed |  | 30/30 | 96.53 | 154 | 0 | 0 | OpenAI | 0.2196000 |
| 20261024T074631Z_study1r_mini-low_anchor_7fa821_r010 | 10 | completed |  | 30/30 | 99.59 | 154 | 0 | 0 | OpenAI | 0.2272168 |
| 20261024T074631Z_study1r_mini-low_anchor_7fa821_r011 | 11 | completed |  | 30/30 | 101.27 | 154 | 0 | 0 | OpenAI | 0.2319608 |
| 20261024T074631Z_study1r_mini-low_anchor_7fa821_r012 | 12 | completed |  | 30/30 | 101.12 | 154 | 0 | 0 | OpenAI | 0.2209320 |
| 20261024T074631Z_study1r_mini-low_anchor_7fa821_r013 | 13 | completed |  | 30/30 | 105.6 | 154 | 0 | 0 | OpenAI | 0.2264660 |
| 20261024T074631Z_study1r_mini-low_anchor_7fa821_r014 | 14 | completed |  | 30/30 | 119.17 | 154 | 0 | 0 | OpenAI | 0.2121472 |
| 20261024T074631Z_study1r_mini-low_anchor_7fa821_r015 | 15 | completed |  | 30/30 | 120.59 | 154 | 0 | 0 | OpenAI | 0.2310356 |
| 20261024T074631Z_study1r_mini-low_anchor_7fa821_r016 | 16 | completed |  | 30/30 | 123.7 | 154 | 0 | 0 | OpenAI | 0.2324316 |

## Per round

Withheld: confirmatory run. Outcome tables (asks, bids, trades) are not written to reports until all Stage 2 blocks are complete (human message 24).
