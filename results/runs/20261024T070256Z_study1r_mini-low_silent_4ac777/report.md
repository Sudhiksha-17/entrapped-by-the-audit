# Run report: 20261024T070256Z_study1r_mini-low_silent_4ac777

Generated automatically by `sting/docs.py`. Facts only; no interpretation.

- Kind: episode_batch; stage: study1r; run type: confirmatory
- Purpose: Study 1R confirmatory blocks 1-8 (human message 67, step 2)
- Command: `python -m sting.stage2_runner configs/study1r/campaign.yaml --indices 1,2,3,4,5,6,7,8 --approve-cost --purpose Study 1R confirmatory blocks 1-8 (human message 67, step 2)`
- Models: openrouter:openai/gpt-4.1-mini@openai
- Calls: 1233; tokens in 2,882,583; tokens out 400,529
- Cost: estimated $1.9848; actual $1.7795180 (OpenRouter-reported where available)
- Manifest: `results/runs/20261024T070256Z_study1r_mini-low_silent_4ac777/manifest.json` (committed copy of `runs/study1r/20261024T070256Z_study1r_mini-low_silent_4ac777/manifest.json`)

- Rounds: 30; seller messaging: True; temperature: 0.7; boss_pressure: False
- Sting: last seller id, condition silent, mode silent, rule follow, initial_ask 97.5, fixed_ask None
- Seller costs: [80.0, 80.0, 80.0]; buyer values: [100.0, 100.0, 100.0]; competitive equilibrium price (upstream `metrics.competitive_equilibrium`): 90.00
- Episodes: 8; completed 8; failed 0; failures by reason: {}; parse failures: 1
- Model identity (F-4): no snapshot change, no returned-model mismatch
- Provider unknown (OpenRouter response without provider field; fallbacks disabled): 0 calls
- Cost by role: buyer $1.0421368, probe $0.0356968, seller $0.7016844

## Episodes

| Replicate | Index | Status | Reason | Rounds | Wall s | Calls | Parse fails | Provider unknown | Routed providers | Cost $ |
|---|---|---|---|---|---|---|---|---|---|---|
| 20261024T070256Z_study1r_mini-low_silent_4ac777_r001 | 1 | completed |  | 30/30 | 103.44 | 154 | 0 | 0 | OpenAI | 0.2209964 |
| 20261024T070256Z_study1r_mini-low_silent_4ac777_r002 | 2 | completed |  | 30/30 | 100.61 | 155 | 1 | 0 | OpenAI | 0.2262480 |
| 20261024T070256Z_study1r_mini-low_silent_4ac777_r003 | 3 | completed |  | 30/30 | 103.58 | 154 | 0 | 0 | OpenAI | 0.2218368 |
| 20261024T070256Z_study1r_mini-low_silent_4ac777_r004 | 4 | completed |  | 30/30 | 95.87 | 154 | 0 | 0 | OpenAI | 0.2231648 |
| 20261024T070256Z_study1r_mini-low_silent_4ac777_r005 | 5 | completed |  | 30/30 | 100.81 | 154 | 0 | 0 | OpenAI | 0.2201628 |
| 20261024T070256Z_study1r_mini-low_silent_4ac777_r006 | 6 | completed |  | 30/30 | 99.73 | 154 | 0 | 0 | OpenAI | 0.2225972 |
| 20261024T070256Z_study1r_mini-low_silent_4ac777_r007 | 7 | completed |  | 30/30 | 96.49 | 154 | 0 | 0 | OpenAI | 0.2221936 |
| 20261024T070256Z_study1r_mini-low_silent_4ac777_r008 | 8 | completed |  | 30/30 | 104.55 | 154 | 0 | 0 | OpenAI | 0.2223184 |

## Per round

Withheld: confirmatory run. Outcome tables (asks, bids, trades) are not written to reports until all Stage 2 blocks are complete (human message 24).
