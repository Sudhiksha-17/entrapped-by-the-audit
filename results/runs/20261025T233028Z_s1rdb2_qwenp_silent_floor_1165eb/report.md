# Run report: 20261025T233028Z_s1rdb2_qwenp_silent_floor_1165eb

Generated automatically by `sting/docs.py`. Facts only; no interpretation.

- Kind: episode_batch; stage: study1r_addon_D_b2; run type: confirmatory
- Purpose: Study 1R-D fresh Cell B (Parasail) block 0 gate (human message 88)
- Command: `python -m sting.study1rd_b2 run configs/study1r_addon_D_b2/campaign.yaml --indices 0 --skip-replacement --approve-cost --purpose Study 1R-D fresh Cell B (Parasail) block 0 gate (human message 88)`
- Models: openrouter:qwen/qwen3-235b-a22b-2507@parasail
- Calls: 185; tokens in 407,632; tokens out 73,684
- Cost: estimated $0.1096; actual $0.1051653 (OpenRouter-reported where available)
- Manifest: `results/runs/20261025T233028Z_s1rdb2_qwenp_silent_floor_1165eb/manifest.json` (committed copy of `runs/study1r_addon_D_b2/20261025T233028Z_s1rdb2_qwenp_silent_floor_1165eb/manifest.json`)

- Rounds: 30; seller messaging: True; temperature: 0.7; boss_pressure: False
- Sting: last seller id, condition silent, mode silent, rule follow, initial_ask 97.5, fixed_ask None
- Seller costs: [80.0, 80.0, 80.0]; buyer values: [100.0, 100.0, 100.0]; competitive equilibrium price (upstream `metrics.competitive_equilibrium`): 90.00
- Episodes: 1; completed 1; failed 0; failures by reason: {}; parse failures: 0
- Model identity (F-4): no snapshot change, no returned-model mismatch
- Provider unknown (OpenRouter response without provider field; fallbacks disabled): 0 calls
- Cost by role: buyer $0.0613700, probe $0.0023259, seller $0.0414693

## Episodes

| Replicate | Index | Status | Reason | Rounds | Wall s | Calls | Parse fails | Provider unknown | Routed providers | Cost $ |
|---|---|---|---|---|---|---|---|---|---|---|
| 20261025T233028Z_s1rdb2_qwenp_silent_floor_1165eb_r000 | 0 | completed |  | 30/30 | 357.9 | 185 | 0 | 0 | Parasail | 0.1051653 |

## Per round

Withheld: confirmatory run. Outcome tables (asks, bids, trades) are not written to reports until all Stage 2 blocks are complete (human message 24).
