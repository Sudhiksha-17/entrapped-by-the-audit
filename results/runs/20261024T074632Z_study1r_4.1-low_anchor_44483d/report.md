# Run report: 20261024T074632Z_study1r_4.1-low_anchor_44483d

Generated automatically by `sting/docs.py`. Facts only; no interpretation.

- Kind: episode_batch; stage: study1r; run type: confirmatory
- Purpose: Study 1R confirmatory blocks 9-16 (human message 67, step 2)
- Command: `python -m sting.stage2_runner configs/study1r/campaign.yaml --indices 9,10,11,12,13,14,15,16 --approve-cost --purpose Study 1R confirmatory blocks 9-16 (human message 67, step 2)`
- Models: openrouter:openai/gpt-4.1@openai
- Calls: 1232; tokens in 2,695,672; tokens out 446,465
- Cost: estimated $9.9112; actual $8.8997040 (OpenRouter-reported where available)
- Manifest: `results/runs/20261024T074632Z_study1r_4.1-low_anchor_44483d/manifest.json` (committed copy of `runs/study1r/20261024T074632Z_study1r_4.1-low_anchor_44483d/manifest.json`)

- Rounds: 30; seller messaging: True; temperature: 0.7; boss_pressure: False
- Sting: last seller id, condition anchor, mode message, rule follow, initial_ask 97.5, fixed_ask None
- Seller costs: [80.0, 80.0, 80.0]; buyer values: [100.0, 100.0, 100.0]; competitive equilibrium price (upstream `metrics.competitive_equilibrium`): 90.00
- Episodes: 8; completed 8; failed 0; failures by reason: {}; parse failures: 0
- Model identity (F-4): no snapshot change, no returned-model mismatch
- Provider unknown (OpenRouter response without provider field; fallbacks disabled): 0 calls
- Cost by role: buyer $5.0262460, probe $0.2259860, seller $3.6474720

## Episodes

| Replicate | Index | Status | Reason | Rounds | Wall s | Calls | Parse fails | Provider unknown | Routed providers | Cost $ |
|---|---|---|---|---|---|---|---|---|---|---|
| 20261024T074632Z_study1r_4.1-low_anchor_44483d_r009 | 9 | completed |  | 30/30 | 103.46 | 154 | 0 | 0 | OpenAI | 1.0790160 |
| 20261024T074632Z_study1r_4.1-low_anchor_44483d_r010 | 10 | completed |  | 30/30 | 96.34 | 154 | 0 | 0 | OpenAI | 1.0966220 |
| 20261024T074632Z_study1r_4.1-low_anchor_44483d_r011 | 11 | completed |  | 30/30 | 99.75 | 154 | 0 | 0 | OpenAI | 1.1437700 |
| 20261024T074632Z_study1r_4.1-low_anchor_44483d_r012 | 12 | completed |  | 30/30 | 105.23 | 154 | 0 | 0 | OpenAI | 1.1504720 |
| 20261024T074632Z_study1r_4.1-low_anchor_44483d_r013 | 13 | completed |  | 30/30 | 119.73 | 154 | 0 | 0 | OpenAI | 1.1357900 |
| 20261024T074632Z_study1r_4.1-low_anchor_44483d_r014 | 14 | completed |  | 30/30 | 98.43 | 154 | 0 | 0 | OpenAI | 1.1205640 |
| 20261024T074632Z_study1r_4.1-low_anchor_44483d_r015 | 15 | completed |  | 30/30 | 131.56 | 154 | 0 | 0 | OpenAI | 1.0877820 |
| 20261024T074632Z_study1r_4.1-low_anchor_44483d_r016 | 16 | completed |  | 30/30 | 108.55 | 154 | 0 | 0 | OpenAI | 1.0856880 |

## Per round

Withheld: confirmatory run. Outcome tables (asks, bids, trades) are not written to reports until all Stage 2 blocks are complete (human message 24).
