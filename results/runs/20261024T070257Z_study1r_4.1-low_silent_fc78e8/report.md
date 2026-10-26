# Run report: 20261024T070257Z_study1r_4.1-low_silent_fc78e8

Generated automatically by `sting/docs.py`. Facts only; no interpretation.

- Kind: episode_batch; stage: study1r; run type: confirmatory
- Purpose: Study 1R confirmatory blocks 1-8 (human message 67, step 2)
- Command: `python -m sting.stage2_runner configs/study1r/campaign.yaml --indices 1,2,3,4,5,6,7,8 --approve-cost --purpose Study 1R confirmatory blocks 1-8 (human message 67, step 2)`
- Models: openrouter:openai/gpt-4.1@openai
- Calls: 1232; tokens in 2,713,699; tokens out 442,506
- Cost: estimated $9.9112; actual $8.9146460 (OpenRouter-reported where available)
- Manifest: `results/runs/20261024T070257Z_study1r_4.1-low_silent_fc78e8/manifest.json` (committed copy of `runs/study1r/20261024T070257Z_study1r_4.1-low_silent_fc78e8/manifest.json`)

- Rounds: 30; seller messaging: True; temperature: 0.7; boss_pressure: False
- Sting: last seller id, condition silent, mode silent, rule follow, initial_ask 97.5, fixed_ask None
- Seller costs: [80.0, 80.0, 80.0]; buyer values: [100.0, 100.0, 100.0]; competitive equilibrium price (upstream `metrics.competitive_equilibrium`): 90.00
- Episodes: 8; completed 8; failed 0; failures by reason: {}; parse failures: 0
- Model identity (F-4): no snapshot change, no returned-model mismatch
- Provider unknown (OpenRouter response without provider field; fallbacks disabled): 0 calls
- Cost by role: buyer $5.0664140, probe $0.2379480, seller $3.6102840

## Episodes

| Replicate | Index | Status | Reason | Rounds | Wall s | Calls | Parse fails | Provider unknown | Routed providers | Cost $ |
|---|---|---|---|---|---|---|---|---|---|---|
| 20261024T070257Z_study1r_4.1-low_silent_fc78e8_r001 | 1 | completed |  | 30/30 | 127.07 | 154 | 0 | 0 | OpenAI | 1.1288100 |
| 20261024T070257Z_study1r_4.1-low_silent_fc78e8_r002 | 2 | completed |  | 30/30 | 101.25 | 154 | 0 | 0 | OpenAI | 1.1571660 |
| 20261024T070257Z_study1r_4.1-low_silent_fc78e8_r003 | 3 | completed |  | 30/30 | 109.9 | 154 | 0 | 0 | OpenAI | 1.0965880 |
| 20261024T070257Z_study1r_4.1-low_silent_fc78e8_r004 | 4 | completed |  | 30/30 | 132.96 | 154 | 0 | 0 | OpenAI | 1.0793900 |
| 20261024T070257Z_study1r_4.1-low_silent_fc78e8_r005 | 5 | completed |  | 30/30 | 113.1 | 154 | 0 | 0 | OpenAI | 1.1808480 |
| 20261024T070257Z_study1r_4.1-low_silent_fc78e8_r006 | 6 | completed |  | 30/30 | 94.71 | 154 | 0 | 0 | OpenAI | 1.0939580 |
| 20261024T070257Z_study1r_4.1-low_silent_fc78e8_r007 | 7 | completed |  | 30/30 | 112.26 | 154 | 0 | 0 | OpenAI | 1.0636720 |
| 20261024T070257Z_study1r_4.1-low_silent_fc78e8_r008 | 8 | completed |  | 30/30 | 106.56 | 154 | 0 | 0 | OpenAI | 1.1142140 |

## Per round

Withheld: confirmatory run. Outcome tables (asks, bids, trades) are not written to reports until all Stage 2 blocks are complete (human message 24).
