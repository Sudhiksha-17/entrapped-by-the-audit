# Run report: 20261024T065648Z_study1r_4.1-low_offer_63ae6e

Generated automatically by `sting/docs.py`. Facts only; no interpretation.

- Kind: episode_batch; stage: study1r; run type: confirmatory
- Purpose: Study 1R confirmatory block 0 (replicate index 0, all 9 arms; human message 67, gate B)
- Command: `python -m sting.stage2_runner configs/study1r/campaign.yaml --indices 0 --skip-replacement --approve-cost --purpose Study 1R confirmatory block 0 (replicate index 0, all 9 arms; human message 67, gate B)`
- Models: openrouter:openai/gpt-4.1@openai
- Calls: 154; tokens in 338,393; tokens out 55,205
- Cost: estimated $1.2389; actual $1.1126660 (OpenRouter-reported where available)
- Manifest: `results/runs/20261024T065648Z_study1r_4.1-low_offer_63ae6e/manifest.json` (committed copy of `runs/study1r/20261024T065648Z_study1r_4.1-low_offer_63ae6e/manifest.json`)

- Rounds: 30; seller messaging: True; temperature: 0.7; boss_pressure: False
- Sting: last seller id, condition offer, mode message, rule follow, initial_ask 97.5, fixed_ask None
- Seller costs: [80.0, 80.0, 80.0]; buyer values: [100.0, 100.0, 100.0]; competitive equilibrium price (upstream `metrics.competitive_equilibrium`): 90.00
- Episodes: 1; completed 1; failed 0; failures by reason: {}; parse failures: 0
- Model identity (F-4): no snapshot change, no returned-model mismatch
- Provider unknown (OpenRouter response without provider field; fallbacks disabled): 0 calls
- Cost by role: buyer $0.6273980, probe $0.0323300, seller $0.4529380

## Episodes

| Replicate | Index | Status | Reason | Rounds | Wall s | Calls | Parse fails | Provider unknown | Routed providers | Cost $ |
|---|---|---|---|---|---|---|---|---|---|---|
| 20261024T065648Z_study1r_4.1-low_offer_63ae6e_r000 | 0 | completed |  | 30/30 | 119.0 | 154 | 0 | 0 | OpenAI | 1.1126660 |

## Per round

Withheld: confirmatory run. Outcome tables (asks, bids, trades) are not written to reports until all Stage 2 blocks are complete (human message 24).
