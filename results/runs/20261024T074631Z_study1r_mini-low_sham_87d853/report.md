# Run report: 20261024T074631Z_study1r_mini-low_sham_87d853

Generated automatically by `sting/docs.py`. Facts only; no interpretation.

- Kind: episode_batch; stage: study1r; run type: confirmatory
- Purpose: Study 1R confirmatory blocks 9-16 (human message 67, step 2)
- Command: `python -m sting.stage2_runner configs/study1r/campaign.yaml --indices 9,10,11,12,13,14,15,16 --approve-cost --purpose Study 1R confirmatory blocks 9-16 (human message 67, step 2)`
- Models: openrouter:openai/gpt-4.1-mini@openai
- Calls: 1232; tokens in 2,839,094; tokens out 407,165
- Cost: estimated $1.9848; actual $1.7749288 (OpenRouter-reported where available)
- Manifest: `results/runs/20261024T074631Z_study1r_mini-low_sham_87d853/manifest.json` (committed copy of `runs/study1r/20261024T074631Z_study1r_mini-low_sham_87d853/manifest.json`)

- Rounds: 30; seller messaging: True; temperature: 0.7; boss_pressure: False
- Sting: last seller id, condition sham, mode message, rule follow, initial_ask 97.5, fixed_ask None
- Seller costs: [80.0, 80.0, 80.0]; buyer values: [100.0, 100.0, 100.0]; competitive equilibrium price (upstream `metrics.competitive_equilibrium`): 90.00
- Episodes: 8; completed 8; failed 0; failures by reason: {}; parse failures: 0
- Model identity (F-4): no snapshot change, no returned-model mismatch
- Provider unknown (OpenRouter response without provider field; fallbacks disabled): 0 calls
- Cost by role: buyer $1.0393800, probe $0.0376568, seller $0.6978920

## Episodes

| Replicate | Index | Status | Reason | Rounds | Wall s | Calls | Parse fails | Provider unknown | Routed providers | Cost $ |
|---|---|---|---|---|---|---|---|---|---|---|
| 20261024T074631Z_study1r_mini-low_sham_87d853_r009 | 9 | completed |  | 30/30 | 94.06 | 154 | 0 | 0 | OpenAI | 0.2158304 |
| 20261024T074631Z_study1r_mini-low_sham_87d853_r010 | 10 | completed |  | 30/30 | 92.01 | 154 | 0 | 0 | OpenAI | 0.2194484 |
| 20261024T074631Z_study1r_mini-low_sham_87d853_r011 | 11 | completed |  | 30/30 | 102.4 | 154 | 0 | 0 | OpenAI | 0.2246572 |
| 20261024T074631Z_study1r_mini-low_sham_87d853_r012 | 12 | completed |  | 30/30 | 104.66 | 154 | 0 | 0 | OpenAI | 0.2200208 |
| 20261024T074631Z_study1r_mini-low_sham_87d853_r013 | 13 | completed |  | 30/30 | 100.84 | 154 | 0 | 0 | OpenAI | 0.2239624 |
| 20261024T074631Z_study1r_mini-low_sham_87d853_r014 | 14 | completed |  | 30/30 | 120.28 | 154 | 0 | 0 | OpenAI | 0.2202408 |
| 20261024T074631Z_study1r_mini-low_sham_87d853_r015 | 15 | completed |  | 30/30 | 111.48 | 154 | 0 | 0 | OpenAI | 0.2267484 |
| 20261024T074631Z_study1r_mini-low_sham_87d853_r016 | 16 | completed |  | 30/30 | 109.63 | 154 | 0 | 0 | OpenAI | 0.2240204 |

## Per round

Withheld: confirmatory run. Outcome tables (asks, bids, trades) are not written to reports until all Stage 2 blocks are complete (human message 24).
