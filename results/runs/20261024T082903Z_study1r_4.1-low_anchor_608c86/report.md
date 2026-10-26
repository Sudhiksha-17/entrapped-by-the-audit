# Run report: 20261024T082903Z_study1r_4.1-low_anchor_608c86

Generated automatically by `sting/docs.py`. Facts only; no interpretation.

- Kind: episode_batch; stage: study1r; run type: confirmatory
- Purpose: Study 1R confirmatory blocks 17-24 (human message 67, step 2)
- Command: `python -m sting.stage2_runner configs/study1r/campaign.yaml --indices 17,18,19,20,21,22,23,24 --approve-cost --purpose Study 1R confirmatory blocks 17-24 (human message 67, step 2)`
- Models: openrouter:openai/gpt-4.1@openai
- Calls: 1232; tokens in 2,699,859; tokens out 445,242
- Cost: estimated $9.9112; actual $8.9096220 (OpenRouter-reported where available)
- Manifest: `results/runs/20261024T082903Z_study1r_4.1-low_anchor_608c86/manifest.json` (committed copy of `runs/study1r/20261024T082903Z_study1r_4.1-low_anchor_608c86/manifest.json`)

- Rounds: 30; seller messaging: True; temperature: 0.7; boss_pressure: False
- Sting: last seller id, condition anchor, mode message, rule follow, initial_ask 97.5, fixed_ask None
- Seller costs: [80.0, 80.0, 80.0]; buyer values: [100.0, 100.0, 100.0]; competitive equilibrium price (upstream `metrics.competitive_equilibrium`): 90.00
- Episodes: 8; completed 8; failed 0; failures by reason: {}; parse failures: 0
- Model identity (F-4): no snapshot change, no returned-model mismatch
- Provider unknown (OpenRouter response without provider field; fallbacks disabled): 0 calls
- Cost by role: buyer $5.0211840, probe $0.2369700, seller $3.6514680

## Episodes

| Replicate | Index | Status | Reason | Rounds | Wall s | Calls | Parse fails | Provider unknown | Routed providers | Cost $ |
|---|---|---|---|---|---|---|---|---|---|---|
| 20261024T082903Z_study1r_4.1-low_anchor_608c86_r017 | 17 | completed |  | 30/30 | 102.28 | 154 | 0 | 0 | OpenAI | 1.1660780 |
| 20261024T082903Z_study1r_4.1-low_anchor_608c86_r018 | 18 | completed |  | 30/30 | 105.81 | 154 | 0 | 0 | OpenAI | 1.1588920 |
| 20261024T082903Z_study1r_4.1-low_anchor_608c86_r019 | 19 | completed |  | 30/30 | 115.03 | 154 | 0 | 0 | OpenAI | 1.1099360 |
| 20261024T082903Z_study1r_4.1-low_anchor_608c86_r020 | 20 | completed |  | 30/30 | 101.58 | 154 | 0 | 0 | OpenAI | 1.0727200 |
| 20261024T082903Z_study1r_4.1-low_anchor_608c86_r021 | 21 | completed |  | 30/30 | 98.24 | 154 | 0 | 0 | OpenAI | 1.1344460 |
| 20261024T082903Z_study1r_4.1-low_anchor_608c86_r022 | 22 | completed |  | 30/30 | 98.71 | 154 | 0 | 0 | OpenAI | 1.1453900 |
| 20261024T082903Z_study1r_4.1-low_anchor_608c86_r023 | 23 | completed |  | 30/30 | 105.31 | 154 | 0 | 0 | OpenAI | 1.0630580 |
| 20261024T082903Z_study1r_4.1-low_anchor_608c86_r024 | 24 | completed |  | 30/30 | 102.07 | 154 | 0 | 0 | OpenAI | 1.0591020 |

## Per round

Withheld: confirmatory run. Outcome tables (asks, bids, trades) are not written to reports until all Stage 2 blocks are complete (human message 24).
