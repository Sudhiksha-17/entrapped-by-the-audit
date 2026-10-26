# Run report: 20261024T091015Z_study1r_4.1-high_silent_feb972

Generated automatically by `sting/docs.py`. Facts only; no interpretation.

- Kind: episode_batch; stage: study1r; run type: confirmatory
- Purpose: Study 1R confirmatory blocks 25-32 (human message 67, step 2)
- Command: `python -m sting.stage2_runner configs/study1r/campaign.yaml --indices 25,26,27,28,29,30,31,32 --approve-cost --purpose Study 1R confirmatory blocks 25-32 (human message 67, step 2)`
- Models: openrouter:openai/gpt-4.1@openai
- Calls: 1232; tokens in 2,290,100; tokens out 438,107
- Cost: estimated $8.8688; actual $8.0554880 (OpenRouter-reported where available)
- Manifest: `results/runs/20261024T091015Z_study1r_4.1-high_silent_feb972/manifest.json` (committed copy of `runs/study1r/20261024T091015Z_study1r_4.1-high_silent_feb972/manifest.json`)

- Rounds: 30; seller messaging: True; temperature: 0.7; boss_pressure: False
- Sting: last seller id, condition silent, mode silent, rule follow, initial_ask 97.5, fixed_ask None
- Seller costs: [80.0, 80.0, 80.0]; buyer values: [100.0, 100.0, 100.0]; competitive equilibrium price (upstream `metrics.competitive_equilibrium`): 90.00
- Episodes: 8; completed 8; failed 0; failures by reason: {}; parse failures: 0
- Model identity (F-4): no snapshot change, no returned-model mismatch
- Provider unknown (OpenRouter response without provider field; fallbacks disabled): 0 calls
- Cost by role: buyer $4.5547780, probe $0.2312840, seller $3.2694260

## Episodes

| Replicate | Index | Status | Reason | Rounds | Wall s | Calls | Parse fails | Provider unknown | Routed providers | Cost $ |
|---|---|---|---|---|---|---|---|---|---|---|
| 20261024T091015Z_study1r_4.1-high_silent_feb972_r025 | 25 | completed |  | 30/30 | 116.94 | 154 | 0 | 0 | OpenAI | 0.9782220 |
| 20261024T091015Z_study1r_4.1-high_silent_feb972_r026 | 26 | completed |  | 30/30 | 116.05 | 154 | 0 | 0 | OpenAI | 1.0569500 |
| 20261024T091015Z_study1r_4.1-high_silent_feb972_r027 | 27 | completed |  | 30/30 | 103.28 | 154 | 0 | 0 | OpenAI | 1.0012060 |
| 20261024T091015Z_study1r_4.1-high_silent_feb972_r028 | 28 | completed |  | 30/30 | 94.77 | 154 | 0 | 0 | OpenAI | 1.0123220 |
| 20261024T091015Z_study1r_4.1-high_silent_feb972_r029 | 29 | completed |  | 30/30 | 105.37 | 154 | 0 | 0 | OpenAI | 1.0130440 |
| 20261024T091015Z_study1r_4.1-high_silent_feb972_r030 | 30 | completed |  | 30/30 | 101.92 | 154 | 0 | 0 | OpenAI | 1.0271680 |
| 20261024T091015Z_study1r_4.1-high_silent_feb972_r031 | 31 | completed |  | 30/30 | 100.59 | 154 | 0 | 0 | OpenAI | 0.9881560 |
| 20261024T091015Z_study1r_4.1-high_silent_feb972_r032 | 32 | completed |  | 30/30 | 113.28 | 154 | 0 | 0 | OpenAI | 0.9784200 |

## Per round

Withheld: confirmatory run. Outcome tables (asks, bids, trades) are not written to reports until all Stage 2 blocks are complete (human message 24).
