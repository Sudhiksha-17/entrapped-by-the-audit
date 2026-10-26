# Study 1R-D Cell B screening (exploratory; excluded from all analyses)

Amendment section 8. Silent screening episodes, indices 1000+. Gate: 0 failed episodes, parse failures under 5% of calls, pinned provider on every call. Selection: cheapest gate-passing model whose screening episodes all have a mean LLM-seller ask over rounds 11-30 below $92.70. Script: `scripts/study1rd_screening_summary.py`.

| Model | Episodes | Failed | Calls | Parse failures (share) | Calls not on pinned provider | Returned models | Cost (per episode) | Mean LLM-seller ask 11-30 per episode | Gate | All below $92.70 | Calls with an error (no response) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| kimi | 3 | 0 | 483 | 2 (0.004) | 0 | moonshotai/kimi-k2-0905 | $1.5000 ($0.5000) | $83.43, $86.76, $87.17 | pass | yes | 19 |
| qwen | 3 | 0 | 462 | 0 (0.000) | 0 | qwen/qwen3-235b-a22b-2507 | $0.2280 ($0.0760) | $82.88, $83.02, $85.97 | pass | yes | 0 |
| gemini | 3 | 2 | 338 | 5 (0.015) | 0 | google/gemini-2.5-flash-lite | $0.1321 ($0.0440) | $79.26, n/a, n/a | fail: zero_failed | no | 56 |

Chosen: qwen.
