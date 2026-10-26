# Run report: 20261024T091015Z_study1r_4.1-low_silent_6885a9

Generated automatically by `sting/docs.py`. Facts only; no interpretation.

- Kind: episode_batch; stage: study1r; run type: confirmatory
- Purpose: Study 1R confirmatory blocks 25-32 (human message 67, step 2)
- Command: `python -m sting.stage2_runner configs/study1r/campaign.yaml --indices 25,26,27,28,29,30,31,32 --approve-cost --purpose Study 1R confirmatory blocks 25-32 (human message 67, step 2)`
- Models: openrouter:openai/gpt-4.1@openai
- Calls: 1232; tokens in 2,792,911; tokens out 437,347
- Cost: estimated $9.9112; actual $9.0341020 (OpenRouter-reported where available)
- Manifest: `results/runs/20261024T091015Z_study1r_4.1-low_silent_6885a9/manifest.json` (committed copy of `runs/study1r/20261024T091015Z_study1r_4.1-low_silent_6885a9/manifest.json`)

- Rounds: 30; seller messaging: True; temperature: 0.7; boss_pressure: False
- Sting: last seller id, condition silent, mode silent, rule follow, initial_ask 97.5, fixed_ask None
- Seller costs: [80.0, 80.0, 80.0]; buyer values: [100.0, 100.0, 100.0]; competitive equilibrium price (upstream `metrics.competitive_equilibrium`): 90.00
- Episodes: 8; completed 8; failed 0; failures by reason: {}; parse failures: 0
- Model identity (F-4): no snapshot change, no returned-model mismatch
- Provider unknown (OpenRouter response without provider field; fallbacks disabled): 0 calls
- Cost by role: buyer $5.1381560, probe $0.2395760, seller $3.6563700

## Episodes

| Replicate | Index | Status | Reason | Rounds | Wall s | Calls | Parse fails | Provider unknown | Routed providers | Cost $ |
|---|---|---|---|---|---|---|---|---|---|---|
| 20261024T091015Z_study1r_4.1-low_silent_6885a9_r025 | 25 | completed |  | 30/30 | 119.85 | 154 | 0 | 0 | OpenAI | 1.0570520 |
| 20261024T091015Z_study1r_4.1-low_silent_6885a9_r026 | 26 | completed |  | 30/30 | 111.94 | 154 | 0 | 0 | OpenAI | 1.1297360 |
| 20261024T091015Z_study1r_4.1-low_silent_6885a9_r027 | 27 | completed |  | 30/30 | 118.17 | 154 | 0 | 0 | OpenAI | 1.1292840 |
| 20261024T091015Z_study1r_4.1-low_silent_6885a9_r028 | 28 | completed |  | 30/30 | 98.81 | 154 | 0 | 0 | OpenAI | 1.1363820 |
| 20261024T091015Z_study1r_4.1-low_silent_6885a9_r029 | 29 | completed |  | 30/30 | 95.5 | 154 | 0 | 0 | OpenAI | 1.1309120 |
| 20261024T091015Z_study1r_4.1-low_silent_6885a9_r030 | 30 | completed |  | 30/30 | 106.51 | 154 | 0 | 0 | OpenAI | 1.1325460 |
| 20261024T091015Z_study1r_4.1-low_silent_6885a9_r031 | 31 | completed |  | 30/30 | 97.9 | 154 | 0 | 0 | OpenAI | 1.1452000 |
| 20261024T091015Z_study1r_4.1-low_silent_6885a9_r032 | 32 | completed |  | 30/30 | 123.96 | 154 | 0 | 0 | OpenAI | 1.1729900 |

## Per round

Withheld: confirmatory run. Outcome tables (asks, bids, trades) are not written to reports until all Stage 2 blocks are complete (human message 24).
