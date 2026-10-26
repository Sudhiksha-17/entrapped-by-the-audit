# Run report: 20261024T095252Z_study1r_mini-low_anchor_3a019e

Generated automatically by `sting/docs.py`. Facts only; no interpretation.

- Kind: episode_batch; stage: study1r; run type: confirmatory
- Purpose: Study 1R confirmatory blocks 33-40 (human message 67, step 2)
- Command: `python -m sting.stage2_runner configs/study1r/campaign.yaml --indices 33,34,35,36,37,38,39,40 --approve-cost --purpose Study 1R confirmatory blocks 33-40 (human message 67, step 2)`
- Models: openrouter:openai/gpt-4.1-mini@openai
- Calls: 1233; tokens in 2,903,257; tokens out 428,901
- Cost: estimated $1.9848; actual $1.8304564 (OpenRouter-reported where available)
- Manifest: `results/runs/20261024T095252Z_study1r_mini-low_anchor_3a019e/manifest.json` (committed copy of `runs/study1r/20261024T095252Z_study1r_mini-low_anchor_3a019e/manifest.json`)

- Rounds: 30; seller messaging: True; temperature: 0.7; boss_pressure: False
- Sting: last seller id, condition anchor, mode message, rule follow, initial_ask 97.5, fixed_ask None
- Seller costs: [80.0, 80.0, 80.0]; buyer values: [100.0, 100.0, 100.0]; competitive equilibrium price (upstream `metrics.competitive_equilibrium`): 90.00
- Episodes: 8; completed 8; failed 0; failures by reason: {}; parse failures: 1
- Model identity (F-4): no snapshot change, no returned-model mismatch
- Provider unknown (OpenRouter response without provider field; fallbacks disabled): 0 calls
- Cost by role: buyer $1.0616008, probe $0.0372052, seller $0.7316504

## Episodes

| Replicate | Index | Status | Reason | Rounds | Wall s | Calls | Parse fails | Provider unknown | Routed providers | Cost $ |
|---|---|---|---|---|---|---|---|---|---|---|
| 20261024T095252Z_study1r_mini-low_anchor_3a019e_r033 | 33 | completed |  | 30/30 | 113.48 | 154 | 0 | 0 | OpenAI | 0.2331140 |
| 20261024T095252Z_study1r_mini-low_anchor_3a019e_r034 | 34 | completed |  | 30/30 | 110.55 | 154 | 0 | 0 | OpenAI | 0.2238048 |
| 20261024T095252Z_study1r_mini-low_anchor_3a019e_r035 | 35 | completed |  | 30/30 | 115.51 | 155 | 1 | 0 | OpenAI | 0.2311364 |
| 20261024T095252Z_study1r_mini-low_anchor_3a019e_r036 | 36 | completed |  | 30/30 | 103.38 | 154 | 0 | 0 | OpenAI | 0.2335088 |
| 20261024T095252Z_study1r_mini-low_anchor_3a019e_r037 | 37 | completed |  | 30/30 | 102.01 | 154 | 0 | 0 | OpenAI | 0.2288540 |
| 20261024T095252Z_study1r_mini-low_anchor_3a019e_r038 | 38 | completed |  | 30/30 | 124.29 | 154 | 0 | 0 | OpenAI | 0.2253052 |
| 20261024T095252Z_study1r_mini-low_anchor_3a019e_r039 | 39 | completed |  | 30/30 | 98.37 | 154 | 0 | 0 | OpenAI | 0.2227192 |
| 20261024T095252Z_study1r_mini-low_anchor_3a019e_r040 | 40 | completed |  | 30/30 | 102.45 | 154 | 0 | 0 | OpenAI | 0.2320140 |

## Per round

Withheld: confirmatory run. Outcome tables (asks, bids, trades) are not written to reports until all Stage 2 blocks are complete (human message 24).
