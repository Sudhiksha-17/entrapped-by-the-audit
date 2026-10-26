# Run report: 20261024T070257Z_study1r_mini-low_anchor_27d981

Generated automatically by `sting/docs.py`. Facts only; no interpretation.

- Kind: episode_batch; stage: study1r; run type: confirmatory
- Purpose: Study 1R confirmatory blocks 1-8 (human message 67, step 2)
- Command: `python -m sting.stage2_runner configs/study1r/campaign.yaml --indices 1,2,3,4,5,6,7,8 --approve-cost --purpose Study 1R confirmatory blocks 1-8 (human message 67, step 2)`
- Models: openrouter:openai/gpt-4.1-mini@openai
- Calls: 1232; tokens in 2,861,956; tokens out 422,947
- Cost: estimated $1.9848; actual $1.8086336 (OpenRouter-reported where available)
- Manifest: `results/runs/20261024T070257Z_study1r_mini-low_anchor_27d981/manifest.json` (committed copy of `runs/study1r/20261024T070257Z_study1r_mini-low_anchor_27d981/manifest.json`)

- Rounds: 30; seller messaging: True; temperature: 0.7; boss_pressure: False
- Sting: last seller id, condition anchor, mode message, rule follow, initial_ask 97.5, fixed_ask None
- Seller costs: [80.0, 80.0, 80.0]; buyer values: [100.0, 100.0, 100.0]; competitive equilibrium price (upstream `metrics.competitive_equilibrium`): 90.00
- Episodes: 8; completed 8; failed 0; failures by reason: {}; parse failures: 0
- Model identity (F-4): no snapshot change, no returned-model mismatch
- Provider unknown (OpenRouter response without provider field; fallbacks disabled): 0 calls
- Cost by role: buyer $1.0500660, probe $0.0398904, seller $0.7186772

## Episodes

| Replicate | Index | Status | Reason | Rounds | Wall s | Calls | Parse fails | Provider unknown | Routed providers | Cost $ |
|---|---|---|---|---|---|---|---|---|---|---|
| 20261024T070257Z_study1r_mini-low_anchor_27d981_r001 | 1 | completed |  | 30/30 | 108.3 | 154 | 0 | 0 | OpenAI | 0.2142936 |
| 20261024T070257Z_study1r_mini-low_anchor_27d981_r002 | 2 | completed |  | 30/30 | 119.38 | 154 | 0 | 0 | OpenAI | 0.2271480 |
| 20261024T070257Z_study1r_mini-low_anchor_27d981_r003 | 3 | completed |  | 30/30 | 106.18 | 154 | 0 | 0 | OpenAI | 0.2283376 |
| 20261024T070257Z_study1r_mini-low_anchor_27d981_r004 | 4 | completed |  | 30/30 | 122.78 | 154 | 0 | 0 | OpenAI | 0.2252200 |
| 20261024T070257Z_study1r_mini-low_anchor_27d981_r005 | 5 | completed |  | 30/30 | 100.33 | 154 | 0 | 0 | OpenAI | 0.2284780 |
| 20261024T070257Z_study1r_mini-low_anchor_27d981_r006 | 6 | completed |  | 30/30 | 116.66 | 154 | 0 | 0 | OpenAI | 0.2396464 |
| 20261024T070257Z_study1r_mini-low_anchor_27d981_r007 | 7 | completed |  | 30/30 | 99.03 | 154 | 0 | 0 | OpenAI | 0.2255684 |
| 20261024T070257Z_study1r_mini-low_anchor_27d981_r008 | 8 | completed |  | 30/30 | 110.78 | 154 | 0 | 0 | OpenAI | 0.2199416 |

## Per round

Withheld: confirmatory run. Outcome tables (asks, bids, trades) are not written to reports until all Stage 2 blocks are complete (human message 24).
