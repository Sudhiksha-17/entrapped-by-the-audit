# Run report: 20261024T184842Z_study1r_addon_A_4.1-high_silent_daa028

Generated automatically by `sting/docs.py`. Facts only; no interpretation.

- Kind: episode_batch; stage: study1r_addon_A; run type: confirmatory
- Purpose: Study 1R-A confirmatory block 0 gate (human message 71)
- Command: `python -m sting.stage2_runner configs/study1r_addon_A/campaign.yaml --indices 0 --skip-replacement --approve-cost --purpose Study 1R-A confirmatory block 0 gate (human message 71)`
- Models: openrouter:openai/gpt-4.1@openai
- Calls: 154; tokens in 306,540; tokens out 54,431
- Cost: estimated $1.1086; actual $1.0377760 (OpenRouter-reported where available)
- Manifest: `results/runs/20261024T184842Z_study1r_addon_A_4.1-high_silent_daa028/manifest.json` (committed copy of `runs/study1r_addon_A/20261024T184842Z_study1r_addon_A_4.1-high_silent_daa028/manifest.json`)

- Rounds: 30; seller messaging: True; temperature: 0.7; boss_pressure: False
- Sting: last seller id, condition silent, mode silent, rule follow, initial_ask 97.5, fixed_ask None
- Seller costs: [80.0, 80.0, 80.0]; buyer values: [100.0, 100.0, 100.0]; competitive equilibrium price (upstream `metrics.competitive_equilibrium`): 90.00
- Episodes: 1; completed 1; failed 0; failures by reason: {}; parse failures: 0
- Model identity (F-4): no snapshot change, no returned-model mismatch
- Provider unknown (OpenRouter response without provider field; fallbacks disabled): 0 calls
- Cost by role: buyer $0.5922420, probe $0.0237540, seller $0.4217800

## Episodes

| Replicate | Index | Status | Reason | Rounds | Wall s | Calls | Parse fails | Provider unknown | Routed providers | Cost $ |
|---|---|---|---|---|---|---|---|---|---|---|
| 20261024T184842Z_study1r_addon_A_4.1-high_silent_daa028_r000 | 0 | completed |  | 30/30 | 140.13 | 154 | 0 | 0 | OpenAI | 1.0377760 |

## Per round

Withheld: confirmatory run. Outcome tables (asks, bids, trades) are not written to reports until all Stage 2 blocks are complete (human message 24).
