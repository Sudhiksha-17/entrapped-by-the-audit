# Run report: 20261024T194540Z_study1r_addon_A_4.1-high_competitive_0aaa4c

Generated automatically by `sting/docs.py`. Facts only; no interpretation.

- Kind: episode_batch; stage: study1r_addon_A; run type: confirmatory
- Purpose: Study 1R-A confirmatory blocks 25-32 (human message 71)
- Command: `python -m sting.stage2_runner configs/study1r_addon_A/campaign.yaml --indices 25,26,27,28,29,30,31,32 --approve-cost --purpose Study 1R-A confirmatory blocks 25-32 (human message 71)`
- Models: openrouter:openai/gpt-4.1@openai
- Calls: 1232; tokens in 2,293,979; tokens out 444,534
- Cost: estimated $8.8688; actual $8.0872060 (OpenRouter-reported where available)
- Manifest: `results/runs/20261024T194540Z_study1r_addon_A_4.1-high_competitive_0aaa4c/manifest.json` (committed copy of `runs/study1r_addon_A/20261024T194540Z_study1r_addon_A_4.1-high_competitive_0aaa4c/manifest.json`)

- Rounds: 30; seller messaging: True; temperature: 0.7; boss_pressure: False
- Sting: last seller id, condition silent, mode silent, rule follow, initial_ask 97.5, fixed_ask None
- Seller costs: [80.0, 80.0, 80.0]; buyer values: [100.0, 100.0, 100.0]; competitive equilibrium price (upstream `metrics.competitive_equilibrium`): 90.00
- Episodes: 8; completed 8; failed 0; failures by reason: {}; parse failures: 0
- Model identity (F-4): no snapshot change, no returned-model mismatch
- Provider unknown (OpenRouter response without provider field; fallbacks disabled): 0 calls
- Cost by role: buyer $4.5937840, probe $0.1908260, seller $3.3025960

## Episodes

| Replicate | Index | Status | Reason | Rounds | Wall s | Calls | Parse fails | Provider unknown | Routed providers | Cost $ |
|---|---|---|---|---|---|---|---|---|---|---|
| 20261024T194540Z_study1r_addon_A_4.1-high_competitive_0aaa4c_r025 | 25 | completed |  | 30/30 | 127.23 | 154 | 0 | 0 | OpenAI | 0.9740920 |
| 20261024T194540Z_study1r_addon_A_4.1-high_competitive_0aaa4c_r026 | 26 | completed |  | 30/30 | 128.15 | 154 | 0 | 0 | OpenAI | 1.0318780 |
| 20261024T194540Z_study1r_addon_A_4.1-high_competitive_0aaa4c_r027 | 27 | completed |  | 30/30 | 119.31 | 154 | 0 | 0 | OpenAI | 1.0181380 |
| 20261024T194540Z_study1r_addon_A_4.1-high_competitive_0aaa4c_r028 | 28 | completed |  | 30/30 | 103.93 | 154 | 0 | 0 | OpenAI | 0.9768320 |
| 20261024T194540Z_study1r_addon_A_4.1-high_competitive_0aaa4c_r029 | 29 | completed |  | 30/30 | 111.74 | 154 | 0 | 0 | OpenAI | 1.0479980 |
| 20261024T194540Z_study1r_addon_A_4.1-high_competitive_0aaa4c_r030 | 30 | completed |  | 30/30 | 120.2 | 154 | 0 | 0 | OpenAI | 0.9836080 |
| 20261024T194540Z_study1r_addon_A_4.1-high_competitive_0aaa4c_r031 | 31 | completed |  | 30/30 | 109.19 | 154 | 0 | 0 | OpenAI | 1.0656940 |
| 20261024T194540Z_study1r_addon_A_4.1-high_competitive_0aaa4c_r032 | 32 | completed |  | 30/30 | 130.47 | 154 | 0 | 0 | OpenAI | 0.9889660 |

## Per round

Withheld: confirmatory run. Outcome tables (asks, bids, trades) are not written to reports until all Stage 2 blocks are complete (human message 24).
