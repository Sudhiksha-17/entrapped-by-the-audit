# Run report: 20261024T091015Z_study1r_4.1-low_anchor_e6fb7c

Generated automatically by `sting/docs.py`. Facts only; no interpretation.

- Kind: episode_batch; stage: study1r; run type: confirmatory
- Purpose: Study 1R confirmatory blocks 25-32 (human message 67, step 2)
- Command: `python -m sting.stage2_runner configs/study1r/campaign.yaml --indices 25,26,27,28,29,30,31,32 --approve-cost --purpose Study 1R confirmatory blocks 25-32 (human message 67, step 2)`
- Models: openrouter:openai/gpt-4.1@openai
- Calls: 1232; tokens in 2,626,350; tokens out 451,487
- Cost: estimated $9.9112; actual $8.8037320 (OpenRouter-reported where available)
- Manifest: `results/runs/20261024T091015Z_study1r_4.1-low_anchor_e6fb7c/manifest.json` (committed copy of `runs/study1r/20261024T091015Z_study1r_4.1-low_anchor_e6fb7c/manifest.json`)

- Rounds: 30; seller messaging: True; temperature: 0.7; boss_pressure: False
- Sting: last seller id, condition anchor, mode message, rule follow, initial_ask 97.5, fixed_ask None
- Seller costs: [80.0, 80.0, 80.0]; buyer values: [100.0, 100.0, 100.0]; competitive equilibrium price (upstream `metrics.competitive_equilibrium`): 90.00
- Episodes: 8; completed 8; failed 0; failures by reason: {}; parse failures: 0
- Model identity (F-4): no snapshot change, no returned-model mismatch
- Provider unknown (OpenRouter response without provider field; fallbacks disabled): 0 calls
- Cost by role: buyer $4.9580400, probe $0.2291880, seller $3.6165040

## Episodes

| Replicate | Index | Status | Reason | Rounds | Wall s | Calls | Parse fails | Provider unknown | Routed providers | Cost $ |
|---|---|---|---|---|---|---|---|---|---|---|
| 20261024T091015Z_study1r_4.1-low_anchor_e6fb7c_r025 | 25 | completed |  | 30/30 | 129.2 | 154 | 0 | 0 | OpenAI | 1.1058120 |
| 20261024T091015Z_study1r_4.1-low_anchor_e6fb7c_r026 | 26 | completed |  | 30/30 | 123.36 | 154 | 0 | 0 | OpenAI | 1.0936820 |
| 20261024T091015Z_study1r_4.1-low_anchor_e6fb7c_r027 | 27 | completed |  | 30/30 | 115.04 | 154 | 0 | 0 | OpenAI | 1.1004340 |
| 20261024T091015Z_study1r_4.1-low_anchor_e6fb7c_r028 | 28 | completed |  | 30/30 | 99.74 | 154 | 0 | 0 | OpenAI | 1.0588140 |
| 20261024T091015Z_study1r_4.1-low_anchor_e6fb7c_r029 | 29 | completed |  | 30/30 | 101.13 | 154 | 0 | 0 | OpenAI | 1.1089440 |
| 20261024T091015Z_study1r_4.1-low_anchor_e6fb7c_r030 | 30 | completed |  | 30/30 | 99.07 | 154 | 0 | 0 | OpenAI | 1.1183720 |
| 20261024T091015Z_study1r_4.1-low_anchor_e6fb7c_r031 | 31 | completed |  | 30/30 | 101.71 | 154 | 0 | 0 | OpenAI | 1.1337820 |
| 20261024T091015Z_study1r_4.1-low_anchor_e6fb7c_r032 | 32 | completed |  | 30/30 | 119.33 | 154 | 0 | 0 | OpenAI | 1.0838920 |

## Per round

Withheld: confirmatory run. Outcome tables (asks, bids, trades) are not written to reports until all Stage 2 blocks are complete (human message 24).
