# Run report: 20261024T091014Z_study1r_mini-low_sham_87e192

Generated automatically by `sting/docs.py`. Facts only; no interpretation.

- Kind: episode_batch; stage: study1r; run type: confirmatory
- Purpose: Study 1R confirmatory blocks 25-32 (human message 67, step 2)
- Command: `python -m sting.stage2_runner configs/study1r/campaign.yaml --indices 25,26,27,28,29,30,31,32 --approve-cost --purpose Study 1R confirmatory blocks 25-32 (human message 67, step 2)`
- Models: openrouter:openai/gpt-4.1-mini@openai
- Calls: 1232; tokens in 2,886,741; tokens out 402,681
- Cost: estimated $1.9848; actual $1.7876196 (OpenRouter-reported where available)
- Manifest: `results/runs/20261024T091014Z_study1r_mini-low_sham_87e192/manifest.json` (committed copy of `runs/study1r/20261024T091014Z_study1r_mini-low_sham_87e192/manifest.json`)

- Rounds: 30; seller messaging: True; temperature: 0.7; boss_pressure: False
- Sting: last seller id, condition sham, mode message, rule follow, initial_ask 97.5, fixed_ask None
- Seller costs: [80.0, 80.0, 80.0]; buyer values: [100.0, 100.0, 100.0]; competitive equilibrium price (upstream `metrics.competitive_equilibrium`): 90.00
- Episodes: 8; completed 8; failed 0; failures by reason: {}; parse failures: 0
- Model identity (F-4): no snapshot change, no returned-model mismatch
- Provider unknown (OpenRouter response without provider field; fallbacks disabled): 0 calls
- Cost by role: buyer $1.0380260, probe $0.0395420, seller $0.7100516

## Episodes

| Replicate | Index | Status | Reason | Rounds | Wall s | Calls | Parse fails | Provider unknown | Routed providers | Cost $ |
|---|---|---|---|---|---|---|---|---|---|---|
| 20261024T091014Z_study1r_mini-low_sham_87e192_r025 | 25 | completed |  | 30/30 | 97.72 | 154 | 0 | 0 | OpenAI | 0.2258088 |
| 20261024T091014Z_study1r_mini-low_sham_87e192_r026 | 26 | completed |  | 30/30 | 102.49 | 154 | 0 | 0 | OpenAI | 0.2234860 |
| 20261024T091014Z_study1r_mini-low_sham_87e192_r027 | 27 | completed |  | 30/30 | 99.03 | 154 | 0 | 0 | OpenAI | 0.2277000 |
| 20261024T091014Z_study1r_mini-low_sham_87e192_r028 | 28 | completed |  | 30/30 | 118.01 | 154 | 0 | 0 | OpenAI | 0.2194744 |
| 20261024T091014Z_study1r_mini-low_sham_87e192_r029 | 29 | completed |  | 30/30 | 92.37 | 154 | 0 | 0 | OpenAI | 0.2203456 |
| 20261024T091014Z_study1r_mini-low_sham_87e192_r030 | 30 | completed |  | 30/30 | 108.09 | 154 | 0 | 0 | OpenAI | 0.2255896 |
| 20261024T091014Z_study1r_mini-low_sham_87e192_r031 | 31 | completed |  | 30/30 | 104.1 | 154 | 0 | 0 | OpenAI | 0.2215444 |
| 20261024T091014Z_study1r_mini-low_sham_87e192_r032 | 32 | completed |  | 30/30 | 93.76 | 154 | 0 | 0 | OpenAI | 0.2236708 |

## Per round

Withheld: confirmatory run. Outcome tables (asks, bids, trades) are not written to reports until all Stage 2 blocks are complete (human message 24).
