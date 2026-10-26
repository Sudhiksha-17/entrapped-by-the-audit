# Run report: 20261024T082902Z_study1r_mini-low_silent_6e8092

Generated automatically by `sting/docs.py`. Facts only; no interpretation.

- Kind: episode_batch; stage: study1r; run type: confirmatory
- Purpose: Study 1R confirmatory blocks 17-24 (human message 67, step 2)
- Command: `python -m sting.stage2_runner configs/study1r/campaign.yaml --indices 17,18,19,20,21,22,23,24 --approve-cost --purpose Study 1R confirmatory blocks 17-24 (human message 67, step 2)`
- Models: openrouter:openai/gpt-4.1-mini@openai
- Calls: 1232; tokens in 2,857,045; tokens out 408,500
- Cost: estimated $1.9848; actual $1.7834004 (OpenRouter-reported where available)
- Manifest: `results/runs/20261024T082902Z_study1r_mini-low_silent_6e8092/manifest.json` (committed copy of `runs/study1r/20261024T082902Z_study1r_mini-low_silent_6e8092/manifest.json`)

- Rounds: 30; seller messaging: True; temperature: 0.7; boss_pressure: False
- Sting: last seller id, condition silent, mode silent, rule follow, initial_ask 97.5, fixed_ask None
- Seller costs: [80.0, 80.0, 80.0]; buyer values: [100.0, 100.0, 100.0]; competitive equilibrium price (upstream `metrics.competitive_equilibrium`): 90.00
- Episodes: 8; completed 8; failed 0; failures by reason: {}; parse failures: 0
- Model identity (F-4): no snapshot change, no returned-model mismatch
- Provider unknown (OpenRouter response without provider field; fallbacks disabled): 0 calls
- Cost by role: buyer $1.0439808, probe $0.0381844, seller $0.7012352

## Episodes

| Replicate | Index | Status | Reason | Rounds | Wall s | Calls | Parse fails | Provider unknown | Routed providers | Cost $ |
|---|---|---|---|---|---|---|---|---|---|---|
| 20261024T082902Z_study1r_mini-low_silent_6e8092_r017 | 17 | completed |  | 30/30 | 106.31 | 154 | 0 | 0 | OpenAI | 0.2239564 |
| 20261024T082902Z_study1r_mini-low_silent_6e8092_r018 | 18 | completed |  | 30/30 | 102.58 | 154 | 0 | 0 | OpenAI | 0.2227132 |
| 20261024T082902Z_study1r_mini-low_silent_6e8092_r019 | 19 | completed |  | 30/30 | 105.08 | 154 | 0 | 0 | OpenAI | 0.2243712 |
| 20261024T082902Z_study1r_mini-low_silent_6e8092_r020 | 20 | completed |  | 30/30 | 95.43 | 154 | 0 | 0 | OpenAI | 0.2234124 |
| 20261024T082902Z_study1r_mini-low_silent_6e8092_r021 | 21 | completed |  | 30/30 | 105.88 | 154 | 0 | 0 | OpenAI | 0.2237788 |
| 20261024T082902Z_study1r_mini-low_silent_6e8092_r022 | 22 | completed |  | 30/30 | 97.51 | 154 | 0 | 0 | OpenAI | 0.2186424 |
| 20261024T082902Z_study1r_mini-low_silent_6e8092_r023 | 23 | completed |  | 30/30 | 144.32 | 154 | 0 | 0 | OpenAI | 0.2256912 |
| 20261024T082902Z_study1r_mini-low_silent_6e8092_r024 | 24 | completed |  | 30/30 | 101.87 | 154 | 0 | 0 | OpenAI | 0.2208348 |

## Per round

Withheld: confirmatory run. Outcome tables (asks, bids, trades) are not written to reports until all Stage 2 blocks are complete (human message 24).
