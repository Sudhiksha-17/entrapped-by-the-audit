# Run report: 20261024T100744Z_study1r_mini-low_anchor_630aa8

Generated automatically by `sting/docs.py`. Facts only; no interpretation.

- Kind: episode_batch; stage: study1r; run type: confirmatory
- Purpose: Study 1R confirmatory blocks 41-48 (human message 67, step 2)
- Command: `python -m sting.stage2_runner configs/study1r/campaign.yaml --indices 41,42,43,44,45,46,47,48 --approve-cost --purpose Study 1R confirmatory blocks 41-48 (human message 67, step 2)`
- Models: openrouter:openai/gpt-4.1-mini@openai
- Calls: 1232; tokens in 2,868,304; tokens out 419,372
- Cost: estimated $1.9848; actual $1.8032256 (OpenRouter-reported where available)
- Manifest: `results/runs/20261024T100744Z_study1r_mini-low_anchor_630aa8/manifest.json` (committed copy of `runs/study1r/20261024T100744Z_study1r_mini-low_anchor_630aa8/manifest.json`)

- Rounds: 30; seller messaging: True; temperature: 0.7; boss_pressure: False
- Sting: last seller id, condition anchor, mode message, rule follow, initial_ask 97.5, fixed_ask None
- Seller costs: [80.0, 80.0, 80.0]; buyer values: [100.0, 100.0, 100.0]; competitive equilibrium price (upstream `metrics.competitive_equilibrium`): 90.00
- Episodes: 8; completed 8; failed 0; failures by reason: {}; parse failures: 0
- Model identity (F-4): no snapshot change, no returned-model mismatch
- Provider unknown (OpenRouter response without provider field; fallbacks disabled): 0 calls
- Cost by role: buyer $1.0499116, probe $0.0373448, seller $0.7159692

## Episodes

| Replicate | Index | Status | Reason | Rounds | Wall s | Calls | Parse fails | Provider unknown | Routed providers | Cost $ |
|---|---|---|---|---|---|---|---|---|---|---|
| 20261024T100744Z_study1r_mini-low_anchor_630aa8_r041 | 41 | completed |  | 30/30 | 103.33 | 154 | 0 | 0 | OpenAI | 0.2276832 |
| 20261024T100744Z_study1r_mini-low_anchor_630aa8_r042 | 42 | completed |  | 30/30 | 138.31 | 154 | 0 | 0 | OpenAI | 0.2311068 |
| 20261024T100744Z_study1r_mini-low_anchor_630aa8_r043 | 43 | completed |  | 30/30 | 113.51 | 154 | 0 | 0 | OpenAI | 0.2137548 |
| 20261024T100744Z_study1r_mini-low_anchor_630aa8_r044 | 44 | completed |  | 30/30 | 123.08 | 154 | 0 | 0 | OpenAI | 0.2188232 |
| 20261024T100744Z_study1r_mini-low_anchor_630aa8_r045 | 45 | completed |  | 30/30 | 103.88 | 154 | 0 | 0 | OpenAI | 0.2191604 |
| 20261024T100744Z_study1r_mini-low_anchor_630aa8_r046 | 46 | completed |  | 30/30 | 108.88 | 154 | 0 | 0 | OpenAI | 0.2336260 |
| 20261024T100744Z_study1r_mini-low_anchor_630aa8_r047 | 47 | completed |  | 30/30 | 118.39 | 154 | 0 | 0 | OpenAI | 0.2284592 |
| 20261024T100744Z_study1r_mini-low_anchor_630aa8_r048 | 48 | completed |  | 30/30 | 129.26 | 154 | 0 | 0 | OpenAI | 0.2306120 |

## Per round

Withheld: confirmatory run. Outcome tables (asks, bids, trades) are not written to reports until all Stage 2 blocks are complete (human message 24).
