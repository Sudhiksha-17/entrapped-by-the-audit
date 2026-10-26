# Preexisting code (confirmed 2026-10-25, human message 82 step 5)

Facts only. Generated with `.venv/Scripts/python scripts/sprint_inventory.py master` at `42da1f7` (Appendix E; rule in `notes/PRIOR_AND_SPRINT_WORK.md` section 1: PREEXISTING = tracked code file, `.py`, `.patch`, `.ps1`, `.sh`, `.bat` under `sting/`, `scripts/`, `tests/`, `patches/` and the repository root, first committed before the sprint cutoff 2026-10-23T04:00Z; upstream `third_party/` excluded).

**Count: 48 PREEXISTING code files**, the same 48 files as in the previous inventory (`notes/PRIOR_AND_SPRINT_WORK.md` Appendix E, snapshot `2444582`; list compared, identical). Code files first committed in the sprint: 53 (38 at the previous snapshot). 12 of the PREEXISTING files were changed in the sprint (same 12 as section 4 of that file).

| File | First commit | First date (local) | Last commit | Last date | Commits | Sprint commits |
|---|---|---|---|---|---|---|
| `scripts/diagnostics_summary.py` | `2852c35` | 2026-10-18 12:19 | `2852c35` | 2026-10-18 12:19 | 1 | 0 |
| `scripts/i021_extract.py` | `d4a5303` | 2026-10-16 17:56 | `d4a5303` | 2026-10-16 17:56 | 1 | 0 |
| `scripts/make_stage1a_configs.py` | `525e1ca` | 2026-10-17 21:30 | `0fc7765` | 2026-10-18 12:12 | 3 | 0 |
| `scripts/make_stage2_configs.py` | `93721fe` | 2026-10-20 10:43 | `93721fe` | 2026-10-20 10:43 | 1 | 0 |
| `scripts/pc_pilot_quotes.py` | `c5d8d7f` | 2026-10-17 14:22 | `c5d8d7f` | 2026-10-17 14:22 | 1 | 0 |
| `scripts/pc_pilot_summary.py` | `5f20cfd` | 2026-10-17 03:19 | `525e1ca` | 2026-10-17 21:30 | 3 | 0 |
| `scripts/power_sim_stage2.py` | `93721fe` | 2026-10-20 10:43 | `93721fe` | 2026-10-20 10:43 | 1 | 0 |
| `scripts/power_t1.py` | `2abbef4` | 2026-10-18 13:06 | `2abbef4` | 2026-10-18 13:06 | 1 | 0 |
| `scripts/power_t2.py` | `686cf13` | 2026-10-18 20:24 | `686cf13` | 2026-10-18 20:24 | 1 | 0 |
| `scripts/stage1a_pilot_check.py` | `b4834b2` | 2026-10-17 22:25 | `968fe52` | 2026-10-20 14:23 | 2 | 0 |
| `scripts/stage1a_pilot_quotes.py` | `b4834b2` | 2026-10-17 22:25 | `b4834b2` | 2026-10-17 22:25 | 1 | 0 |
| `scripts/stage2_checkpoint.py` | `d8a2f2b` | 2026-10-21 12:47 | `d8a2f2b` | 2026-10-21 12:47 | 1 | 0 |
| `scripts/stage2_health.py` | `242e2d9` | 2026-10-21 12:23 | `242e2d9` | 2026-10-21 12:23 | 1 | 0 |
| `scripts/stage2_labeling_sheet.py` | `c65a320` | 2026-10-21 16:11 | `c588f6e` | 2026-10-24 02:06 | 4 | 3 |
| `scripts/step1_withdrawals_variance.py` | `525e1ca` | 2026-10-17 21:30 | `525e1ca` | 2026-10-17 21:30 | 1 | 0 |
| `sting/__init__.py` | `1c34be0` | 2026-10-16 16:42 | `1c34be0` | 2026-10-16 16:42 | 1 | 0 |
| `sting/clients.py` | `1c34be0` | 2026-10-16 16:42 | `b43ac7f` | 2026-10-24 02:47 | 12 | 5 |
| `sting/docs.py` | `dcb4843` | 2026-10-16 23:25 | `af4a01d` | 2026-10-23 22:38 | 10 | 2 |
| `sting/env.py` | `1c34be0` | 2026-10-16 16:42 | `f2a911b` | 2026-10-16 17:18 | 2 | 0 |
| `sting/freeze_prereg.py` | `3eb2e29` | 2026-10-20 10:38 | `b43ac7f` | 2026-10-24 02:47 | 5 | 3 |
| `sting/gates.py` | `93721fe` | 2026-10-20 10:43 | `968fe52` | 2026-10-20 14:23 | 2 | 0 |
| `sting/judge.py` | `2cf6e14` | 2026-10-18 20:17 | `651f045` | 2026-10-23 23:42 | 3 | 1 |
| `sting/label_tool.py` | `2e6e331` | 2026-10-22 10:31 | `b43ac7f` | 2026-10-24 02:47 | 10 | 9 |
| `sting/minimal_runner.py` | `1c34be0` | 2026-10-16 16:42 | `b43ac7f` | 2026-10-24 02:47 | 21 | 6 |
| `sting/model_check.py` | `1c34be0` | 2026-10-16 16:42 | `dcb4843` | 2026-10-16 23:25 | 4 | 0 |
| `sting/paths.py` | `1c34be0` | 2026-10-16 16:42 | `1c34be0` | 2026-10-16 16:42 | 1 | 0 |
| `sting/prompt_mirror.py` | `2608379` | 2026-10-20 10:30 | `2608379` | 2026-10-20 10:30 | 1 | 0 |
| `sting/stage2_analysis.py` | `3eb2e29` | 2026-10-20 10:38 | `7c05246` | 2026-10-20 23:17 | 3 | 0 |
| `sting/stage2_measures.py` | `2cf6e14` | 2026-10-18 20:17 | `7c05246` | 2026-10-20 23:17 | 3 | 0 |
| `sting/stage2_runner.py` | `3eb2e29` | 2026-10-20 10:38 | `033ae08` | 2026-10-23 20:32 | 4 | 1 |
| `sting/sting_seller.py` | `525e1ca` | 2026-10-17 21:30 | `651f045` | 2026-10-23 23:42 | 8 | 5 |
| `tests/conftest.py` | `1c34be0` | 2026-10-16 16:42 | `1c34be0` | 2026-10-16 16:42 | 1 | 0 |
| `tests/test_budget_and_replacement.py` | `686cf13` | 2026-10-18 20:24 | `686cf13` | 2026-10-18 20:24 | 1 | 0 |
| `tests/test_clients.py` | `1c34be0` | 2026-10-16 16:42 | `5c16095` | 2026-10-23 23:29 | 7 | 2 |
| `tests/test_docs.py` | `dcb4843` | 2026-10-16 23:25 | `c5d8d7f` | 2026-10-17 14:22 | 3 | 0 |
| `tests/test_env.py` | `f2a911b` | 2026-10-16 17:18 | `f2a911b` | 2026-10-16 17:18 | 1 | 0 |
| `tests/test_gates.py` | `93721fe` | 2026-10-20 10:43 | `93721fe` | 2026-10-20 10:43 | 1 | 0 |
| `tests/test_judge.py` | `2cf6e14` | 2026-10-18 20:17 | `2cf6e14` | 2026-10-18 20:17 | 1 | 0 |
| `tests/test_label_tool.py` | `2e6e331` | 2026-10-22 10:31 | `7fcaa5c` | 2026-10-23 21:09 | 4 | 3 |
| `tests/test_minimal_runner.py` | `1c34be0` | 2026-10-16 16:42 | `752667f` | 2026-10-20 13:53 | 7 | 0 |
| `tests/test_model_check.py` | `1c34be0` | 2026-10-16 16:42 | `1c34be0` | 2026-10-16 16:42 | 1 | 0 |
| `tests/test_stage2_analysis.py` | `3eb2e29` | 2026-10-20 10:38 | `7c05246` | 2026-10-20 23:17 | 3 | 0 |
| `tests/test_stage2_campaign_manipulation.py` | `e103daa` | 2026-10-21 12:14 | `e103daa` | 2026-10-21 12:14 | 1 | 0 |
| `tests/test_stage2_injection.py` | `2cf6e14` | 2026-10-18 20:17 | `7c05246` | 2026-10-20 23:17 | 3 | 0 |
| `tests/test_stage2_measures.py` | `2cf6e14` | 2026-10-18 20:17 | `7c05246` | 2026-10-20 23:17 | 3 | 0 |
| `tests/test_stage2_runner.py` | `3eb2e29` | 2026-10-20 10:38 | `3bffe18` | 2026-10-23 12:57 | 6 | 1 |
| `tests/test_sting_seller.py` | `525e1ca` | 2026-10-17 21:30 | `2cf6e14` | 2026-10-18 20:17 | 2 | 0 |
| `tests/test_volume_prompt.py` | `2608379` | 2026-10-20 10:30 | `2608379` | 2026-10-20 10:30 | 1 | 0 |
