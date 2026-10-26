# Run report: 20261024T082902Z_study1r_mini-low_sham_2834cb

Generated automatically by `sting/docs.py`. Facts only; no interpretation.

- Kind: episode_batch; stage: study1r; run type: confirmatory
- Purpose: Study 1R confirmatory blocks 17-24 (human message 67, step 2)
- Command: `python -m sting.stage2_runner configs/study1r/campaign.yaml --indices 17,18,19,20,21,22,23,24 --approve-cost --purpose Study 1R confirmatory blocks 17-24 (human message 67, step 2)`
- Models: openrouter:openai/gpt-4.1-mini@openai
- Calls: 1232; tokens in 2,868,243; tokens out 408,203
- Cost: estimated $1.9848; actual $1.7844092 (OpenRouter-reported where available)
- Manifest: `results/runs/20261024T082902Z_study1r_mini-low_sham_2834cb/manifest.json` (committed copy of `runs/study1r/20261024T082902Z_study1r_mini-low_sham_2834cb/manifest.json`)

- Rounds: 30; seller messaging: True; temperature: 0.7; boss_pressure: False
- Sting: last seller id, condition sham, mode message, rule follow, initial_ask 97.5, fixed_ask None
- Seller costs: [80.0, 80.0, 80.0]; buyer values: [100.0, 100.0, 100.0]; competitive equilibrium price (upstream `metrics.competitive_equilibrium`): 90.00
- Episodes: 8; completed 8; failed 0; failures by reason: {}; parse failures: 0
- Model identity (F-4): no snapshot change, no returned-model mismatch
- Provider unknown (OpenRouter response without provider field; fallbacks disabled): 0 calls
- Cost by role: buyer $1.0415172, probe $0.0365680, seller $0.7063240

## Episodes

| Replicate | Index | Status | Reason | Rounds | Wall s | Calls | Parse fails | Provider unknown | Routed providers | Cost $ |
|---|---|---|---|---|---|---|---|---|---|---|
| 20261024T082902Z_study1r_mini-low_sham_2834cb_r017 | 17 | completed |  | 30/30 | 101.38 | 154 | 0 | 0 | OpenAI | 0.2249540 |
| 20261024T082902Z_study1r_mini-low_sham_2834cb_r018 | 18 | completed |  | 30/30 | 107.52 | 154 | 0 | 0 | OpenAI | 0.2215260 |
| 20261024T082902Z_study1r_mini-low_sham_2834cb_r019 | 19 | completed |  | 30/30 | 113.69 | 154 | 0 | 0 | OpenAI | 0.2263788 |
| 20261024T082902Z_study1r_mini-low_sham_2834cb_r020 | 20 | completed |  | 30/30 | 99.84 | 154 | 0 | 0 | OpenAI | 0.2207504 |
| 20261024T082902Z_study1r_mini-low_sham_2834cb_r021 | 21 | completed |  | 30/30 | 107.33 | 154 | 0 | 0 | OpenAI | 0.2273008 |
| 20261024T082902Z_study1r_mini-low_sham_2834cb_r022 | 22 | completed |  | 30/30 | 94.6 | 154 | 0 | 0 | OpenAI | 0.2193332 |
| 20261024T082902Z_study1r_mini-low_sham_2834cb_r023 | 23 | completed |  | 30/30 | 92.97 | 154 | 0 | 0 | OpenAI | 0.2209524 |
| 20261024T082902Z_study1r_mini-low_sham_2834cb_r024 | 24 | completed |  | 30/30 | 94.82 | 154 | 0 | 0 | OpenAI | 0.2232136 |

## Per round

Withheld: confirmatory run. Outcome tables (asks, bids, trades) are not written to reports until all Stage 2 blocks are complete (human message 24).
