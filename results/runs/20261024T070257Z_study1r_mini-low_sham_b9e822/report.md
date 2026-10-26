# Run report: 20261024T070257Z_study1r_mini-low_sham_b9e822

Generated automatically by `sting/docs.py`. Facts only; no interpretation.

- Kind: episode_batch; stage: study1r; run type: confirmatory
- Purpose: Study 1R confirmatory blocks 1-8 (human message 67, step 2)
- Command: `python -m sting.stage2_runner configs/study1r/campaign.yaml --indices 1,2,3,4,5,6,7,8 --approve-cost --purpose Study 1R confirmatory blocks 1-8 (human message 67, step 2)`
- Models: openrouter:openai/gpt-4.1-mini@openai
- Calls: 1232; tokens in 2,849,881; tokens out 410,383
- Cost: estimated $1.9848; actual $1.7830484 (OpenRouter-reported where available)
- Manifest: `results/runs/20261024T070257Z_study1r_mini-low_sham_b9e822/manifest.json` (committed copy of `runs/study1r/20261024T070257Z_study1r_mini-low_sham_b9e822/manifest.json`)

- Rounds: 30; seller messaging: True; temperature: 0.7; boss_pressure: False
- Sting: last seller id, condition sham, mode message, rule follow, initial_ask 97.5, fixed_ask None
- Seller costs: [80.0, 80.0, 80.0]; buyer values: [100.0, 100.0, 100.0]; competitive equilibrium price (upstream `metrics.competitive_equilibrium`): 90.00
- Episodes: 8; completed 8; failed 0; failures by reason: {}; parse failures: 0
- Model identity (F-4): no snapshot change, no returned-model mismatch
- Provider unknown (OpenRouter response without provider field; fallbacks disabled): 0 calls
- Cost by role: buyer $1.0424948, probe $0.0362972, seller $0.7042564

## Episodes

| Replicate | Index | Status | Reason | Rounds | Wall s | Calls | Parse fails | Provider unknown | Routed providers | Cost $ |
|---|---|---|---|---|---|---|---|---|---|---|
| 20261024T070257Z_study1r_mini-low_sham_b9e822_r001 | 1 | completed |  | 30/30 | 108.9 | 154 | 0 | 0 | OpenAI | 0.2221416 |
| 20261024T070257Z_study1r_mini-low_sham_b9e822_r002 | 2 | completed |  | 30/30 | 95.35 | 154 | 0 | 0 | OpenAI | 0.2206472 |
| 20261024T070257Z_study1r_mini-low_sham_b9e822_r003 | 3 | completed |  | 30/30 | 103.78 | 154 | 0 | 0 | OpenAI | 0.2228472 |
| 20261024T070257Z_study1r_mini-low_sham_b9e822_r004 | 4 | completed |  | 30/30 | 118.05 | 154 | 0 | 0 | OpenAI | 0.2236740 |
| 20261024T070257Z_study1r_mini-low_sham_b9e822_r005 | 5 | completed |  | 30/30 | 105.01 | 154 | 0 | 0 | OpenAI | 0.2243848 |
| 20261024T070257Z_study1r_mini-low_sham_b9e822_r006 | 6 | completed |  | 30/30 | 97.96 | 154 | 0 | 0 | OpenAI | 0.2274252 |
| 20261024T070257Z_study1r_mini-low_sham_b9e822_r007 | 7 | completed |  | 30/30 | 99.31 | 154 | 0 | 0 | OpenAI | 0.2210908 |
| 20261024T070257Z_study1r_mini-low_sham_b9e822_r008 | 8 | completed |  | 30/30 | 108.44 | 154 | 0 | 0 | OpenAI | 0.2208376 |

## Per round

Withheld: confirmatory run. Outcome tables (asks, bids, trades) are not written to reports until all Stage 2 blocks are complete (human message 24).
