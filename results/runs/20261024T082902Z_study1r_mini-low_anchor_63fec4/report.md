# Run report: 20261024T082902Z_study1r_mini-low_anchor_63fec4

Generated automatically by `sting/docs.py`. Facts only; no interpretation.

- Kind: episode_batch; stage: study1r; run type: confirmatory
- Purpose: Study 1R confirmatory blocks 17-24 (human message 67, step 2)
- Command: `python -m sting.stage2_runner configs/study1r/campaign.yaml --indices 17,18,19,20,21,22,23,24 --approve-cost --purpose Study 1R confirmatory blocks 17-24 (human message 67, step 2)`
- Models: openrouter:openai/gpt-4.1-mini@openai
- Calls: 1232; tokens in 2,922,152; tokens out 428,089
- Cost: estimated $1.9848; actual $1.8385584 (OpenRouter-reported where available)
- Manifest: `results/runs/20261024T082902Z_study1r_mini-low_anchor_63fec4/manifest.json` (committed copy of `runs/study1r/20261024T082902Z_study1r_mini-low_anchor_63fec4/manifest.json`)

- Rounds: 30; seller messaging: True; temperature: 0.7; boss_pressure: False
- Sting: last seller id, condition anchor, mode message, rule follow, initial_ask 97.5, fixed_ask None
- Seller costs: [80.0, 80.0, 80.0]; buyer values: [100.0, 100.0, 100.0]; competitive equilibrium price (upstream `metrics.competitive_equilibrium`): 90.00
- Episodes: 8; completed 8; failed 0; failures by reason: {}; parse failures: 0
- Model identity (F-4): no snapshot change, no returned-model mismatch
- Provider unknown (OpenRouter response without provider field; fallbacks disabled): 0 calls
- Cost by role: buyer $1.0681496, probe $0.0390008, seller $0.7314080

## Episodes

| Replicate | Index | Status | Reason | Rounds | Wall s | Calls | Parse fails | Provider unknown | Routed providers | Cost $ |
|---|---|---|---|---|---|---|---|---|---|---|
| 20261024T082902Z_study1r_mini-low_anchor_63fec4_r017 | 17 | completed |  | 30/30 | 101.04 | 154 | 0 | 0 | OpenAI | 0.2336752 |
| 20261024T082902Z_study1r_mini-low_anchor_63fec4_r018 | 18 | completed |  | 30/30 | 107.76 | 154 | 0 | 0 | OpenAI | 0.2330852 |
| 20261024T082902Z_study1r_mini-low_anchor_63fec4_r019 | 19 | completed |  | 30/30 | 113.97 | 154 | 0 | 0 | OpenAI | 0.2213696 |
| 20261024T082902Z_study1r_mini-low_anchor_63fec4_r020 | 20 | completed |  | 30/30 | 96.99 | 154 | 0 | 0 | OpenAI | 0.2300128 |
| 20261024T082902Z_study1r_mini-low_anchor_63fec4_r021 | 21 | completed |  | 30/30 | 109.08 | 154 | 0 | 0 | OpenAI | 0.2292440 |
| 20261024T082902Z_study1r_mini-low_anchor_63fec4_r022 | 22 | completed |  | 30/30 | 96.1 | 154 | 0 | 0 | OpenAI | 0.2282816 |
| 20261024T082902Z_study1r_mini-low_anchor_63fec4_r023 | 23 | completed |  | 30/30 | 98.9 | 154 | 0 | 0 | OpenAI | 0.2314824 |
| 20261024T082902Z_study1r_mini-low_anchor_63fec4_r024 | 24 | completed |  | 30/30 | 100.04 | 154 | 0 | 0 | OpenAI | 0.2314076 |

## Per round

Withheld: confirmatory run. Outcome tables (asks, bids, trades) are not written to reports until all Stage 2 blocks are complete (human message 24).
