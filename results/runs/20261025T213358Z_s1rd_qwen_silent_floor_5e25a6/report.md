# Run report: 20261025T213358Z_s1rd_qwen_silent_floor_5e25a6

Generated automatically by `sting/docs.py`. Facts only; no interpretation.

- Kind: episode_batch; stage: study1r_addon_D; run type: confirmatory
- Purpose: Study 1R-D confirmatory block 0 gate (human message 87)
- Command: `python -m sting.study1rd run configs/study1r_addon_D/campaign.yaml --indices 0 --skip-replacement --approve-cost --purpose Study 1R-D confirmatory block 0 gate (human message 87)`
- Models: openrouter:qwen/qwen3-235b-a22b-2507@deepinfra
- Calls: 182; tokens in 421,351; tokens out 71,011
- Cost: estimated $0.0836; actual $0.0769776 (OpenRouter-reported where available)
- Manifest: `results/runs/20261025T213358Z_s1rd_qwen_silent_floor_5e25a6/manifest.json` (committed copy of `runs/study1r_addon_D/20261025T213358Z_s1rd_qwen_silent_floor_5e25a6/manifest.json`)

- Rounds: 30; seller messaging: True; temperature: 0.7; boss_pressure: False
- Sting: last seller id, condition silent, mode silent, rule follow, initial_ask 97.5, fixed_ask None
- Seller costs: [80.0, 80.0, 80.0]; buyer values: [100.0, 100.0, 100.0]; competitive equilibrium price (upstream `metrics.competitive_equilibrium`): 90.00
- Episodes: 1; completed 1; failed 0; failures by reason: {}; parse failures: 0
- Model identity (F-4): no snapshot change, no returned-model mismatch
- Provider unknown (OpenRouter response without provider field; fallbacks disabled): 0 calls
- Cost by role: buyer $0.0455492, probe $0.0018387, seller $0.0295897

## Episodes

| Replicate | Index | Status | Reason | Rounds | Wall s | Calls | Parse fails | Provider unknown | Routed providers | Cost $ |
|---|---|---|---|---|---|---|---|---|---|---|
| 20261025T213358Z_s1rd_qwen_silent_floor_5e25a6_r000 | 0 | completed |  | 30/30 | 1087.68 | 182 | 0 | 0 | DeepInfra | 0.0769776 |

## Per round

Withheld: confirmatory run. Outcome tables (asks, bids, trades) are not written to reports until all Stage 2 blocks are complete (human message 24).
