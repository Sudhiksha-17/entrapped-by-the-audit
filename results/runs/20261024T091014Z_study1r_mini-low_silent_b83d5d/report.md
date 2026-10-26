# Run report: 20261024T091014Z_study1r_mini-low_silent_b83d5d

Generated automatically by `sting/docs.py`. Facts only; no interpretation.

- Kind: episode_batch; stage: study1r; run type: confirmatory
- Purpose: Study 1R confirmatory blocks 25-32 (human message 67, step 2)
- Command: `python -m sting.stage2_runner configs/study1r/campaign.yaml --indices 25,26,27,28,29,30,31,32 --approve-cost --purpose Study 1R confirmatory blocks 25-32 (human message 67, step 2)`
- Models: openrouter:openai/gpt-4.1-mini@openai
- Calls: 1232; tokens in 2,849,876; tokens out 408,927
- Cost: estimated $1.9848; actual $1.7881280 (OpenRouter-reported where available)
- Manifest: `results/runs/20261024T091014Z_study1r_mini-low_silent_b83d5d/manifest.json` (committed copy of `runs/study1r/20261024T091014Z_study1r_mini-low_silent_b83d5d/manifest.json`)

- Rounds: 30; seller messaging: True; temperature: 0.7; boss_pressure: False
- Sting: last seller id, condition silent, mode silent, rule follow, initial_ask 97.5, fixed_ask None
- Seller costs: [80.0, 80.0, 80.0]; buyer values: [100.0, 100.0, 100.0]; competitive equilibrium price (upstream `metrics.competitive_equilibrium`): 90.00
- Episodes: 8; completed 8; failed 0; failures by reason: {}; parse failures: 0
- Model identity (F-4): no snapshot change, no returned-model mismatch
- Provider unknown (OpenRouter response without provider field; fallbacks disabled): 0 calls
- Cost by role: buyer $1.0467208, probe $0.0439928, seller $0.6974144

## Episodes

| Replicate | Index | Status | Reason | Rounds | Wall s | Calls | Parse fails | Provider unknown | Routed providers | Cost $ |
|---|---|---|---|---|---|---|---|---|---|---|
| 20261024T091014Z_study1r_mini-low_silent_b83d5d_r025 | 25 | completed |  | 30/30 | 93.06 | 154 | 0 | 0 | OpenAI | 0.2251012 |
| 20261024T091014Z_study1r_mini-low_silent_b83d5d_r026 | 26 | completed |  | 30/30 | 106.41 | 154 | 0 | 0 | OpenAI | 0.2250364 |
| 20261024T091014Z_study1r_mini-low_silent_b83d5d_r027 | 27 | completed |  | 30/30 | 100.41 | 154 | 0 | 0 | OpenAI | 0.2252248 |
| 20261024T091014Z_study1r_mini-low_silent_b83d5d_r028 | 28 | completed |  | 30/30 | 116.34 | 154 | 0 | 0 | OpenAI | 0.2226728 |
| 20261024T091014Z_study1r_mini-low_silent_b83d5d_r029 | 29 | completed |  | 30/30 | 92.39 | 154 | 0 | 0 | OpenAI | 0.2227164 |
| 20261024T091014Z_study1r_mini-low_silent_b83d5d_r030 | 30 | completed |  | 30/30 | 125.45 | 154 | 0 | 0 | OpenAI | 0.2218388 |
| 20261024T091014Z_study1r_mini-low_silent_b83d5d_r031 | 31 | completed |  | 30/30 | 103.66 | 154 | 0 | 0 | OpenAI | 0.2241260 |
| 20261024T091014Z_study1r_mini-low_silent_b83d5d_r032 | 32 | completed |  | 30/30 | 97.45 | 154 | 0 | 0 | OpenAI | 0.2214116 |

## Per round

Withheld: confirmatory run. Outcome tables (asks, bids, trades) are not written to reports until all Stage 2 blocks are complete (human message 24).
