# Run report: 20261025T213358Z_s1rd_mini-low_silent_floor_1157ff

Generated automatically by `sting/docs.py`. Facts only; no interpretation.

- Kind: episode_batch; stage: study1r_addon_D; run type: confirmatory
- Purpose: Study 1R-D confirmatory block 0 gate (human message 87)
- Command: `python -m sting.study1rd run configs/study1r_addon_D/campaign.yaml --indices 0 --skip-replacement --approve-cost --purpose Study 1R-D confirmatory block 0 gate (human message 87)`
- Models: openrouter:openai/gpt-4.1-mini@openai
- Calls: 154; tokens in 360,572; tokens out 52,794
- Cost: estimated $0.2473; actual $0.2264336 (OpenRouter-reported where available)
- Manifest: `results/runs/20261025T213358Z_s1rd_mini-low_silent_floor_1157ff/manifest.json` (committed copy of `runs/study1r_addon_D/20261025T213358Z_s1rd_mini-low_silent_floor_1157ff/manifest.json`)

- Rounds: 30; seller messaging: True; temperature: 0.7; boss_pressure: False
- Sting: last seller id, condition silent, mode silent, rule follow, initial_ask 97.5, fixed_ask None
- Seller costs: [80.0, 80.0, 80.0]; buyer values: [100.0, 100.0, 100.0]; competitive equilibrium price (upstream `metrics.competitive_equilibrium`): 90.00
- Episodes: 1; completed 1; failed 0; failures by reason: {}; parse failures: 0
- Model identity (F-4): no snapshot change, no returned-model mismatch
- Provider unknown (OpenRouter response without provider field; fallbacks disabled): 0 calls
- Cost by role: buyer $0.1316832, probe $0.0046204, seller $0.0901300

## Episodes

| Replicate | Index | Status | Reason | Rounds | Wall s | Calls | Parse fails | Provider unknown | Routed providers | Cost $ |
|---|---|---|---|---|---|---|---|---|---|---|
| 20261025T213358Z_s1rd_mini-low_silent_floor_1157ff_r000 | 0 | completed |  | 30/30 | 127.71 | 154 | 0 | 0 | OpenAI | 0.2264336 |

## Per round

Withheld: confirmatory run. Outcome tables (asks, bids, trades) are not written to reports until all Stage 2 blocks are complete (human message 24).
