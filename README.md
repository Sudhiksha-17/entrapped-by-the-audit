# Sting validity study in an LLM double-auction market: public snapshot

## Run the entrapment test on your own sting

The entrapment test has three steps, in this order: check the record, measure predisposition, test inducement. [Appendix F](results/paper/APPENDIX_F_ENTRAPMENT_TEST.md) describes each step: what to run, what to measure, what counts as a warning sign, and which files in this release support it.

- **Check the record.** Score your judge on the [Sting Replies benchmark](benchmark/README.md) with [`benchmark/score_judge.py`](benchmark/score_judge.py): `python benchmark/score_judge.py benchmark/sting_replies.csv --labels your_labels.csv`, where `your_labels.csv` has the columns `message_id,response`. Baselines for three judges are in [`benchmark/BASELINES.md`](benchmark/BASELINES.md).
- **Measure predisposition.** Run sting-free (Silent) episodes with the configs in `configs/study1r/` and compare their propensity with your reader's acceptance counts (Appendix F, step two).
- **Test inducement.** Run the price-only control and the words-only test (`sting/study1rc.py`, `sting/study1rd.py`; Appendix F, step three).

## What this is

This folder is a **snapshot** of the project repository, built by `scripts/build_release.py`; the commit it was built from is named in `RELEASE_MANIFEST.md`. The full-history repository is private and is **available on request**. Labeler notes are **withheld**. Human label files keep only item ids and keystroke labels. Files that contain verbatim labeler notes, or that quote them, are also withheld; they are listed in `RELEASE_SCAN.md`. The development log and other internal working notes are not included; they are **available on request**.

## Project summary

The project tests whether an LLM seller's acceptance of a scripted collusion offer (a "sting") tracks the seller's collusion propensity measured without any offer.

**Market.** The market is a continuous double auction from `andyjliu/llm-agent-collusion`, pinned at commit 2bb2a7e2 and used unmodified. Each episode has:
- two LLM sellers;
- one scripted seller, Seller C (the sting);
- three LLM buyers.

Seller cost is $80, buyer value is $100, and an episode runs 30 rounds. Models are OpenAI gpt-4.1 and gpt-4.1-mini, routed through OpenRouter.

**Studies.** Every study was preregistered and frozen (hash locks) before its confirmatory run:

| Study | Run | Design | Completed episodes |
|---|---|---|---|
| Study 1 | 2026-10-21 | Seller C posts one message in round 10 | 396 |
| Study 1R | 2026-10-24 | Seller C posts a message every round 10-29 (the "talking sting") | 351, plus 1 failed episode, replaced |
| Study 1R-A | 2026-10-24 | Add-on: a competitive Seller C | 66 |
| Study 1R-C | 2026-10-25 | Add-on, by amendment: Seller C prices at the offered level with no message (the price-only control) | 132 |
| Study 1R-D | 2026-10-25 to 2026-10-26 | Add-on, by amendment: Seller C prices at the offered level, with or without the offer messages (the words-only test). Cell A (gpt-4.1-mini) analysed; Cell B (a second model family) not analysed, incomplete | Cell A: 120, plus 2 failed episodes, replaced |

**Where to find things.**
- Results: `results/stage2/RESULTS.md` (Study 1), `results/study1r/RESULTS.md`, `results/study1r/RESULTS_1RA.md`, `results/study1r/RESULTS_1RC.md` and `results/study1r/RESULTS_1RD.md`.
- The entrapment test, step by step: `results/paper/APPENDIX_F_ENTRAPMENT_TEST.md`.
- The Sting Replies benchmark: `benchmark/` (N = 224 human-labeled seller replies, a scorer and baselines for three judges).
- Paper figures: `results/study1r/figures/final/` (Figures 1 to 3) and `results/study1r/figures/final/appendix/` (Figures E1 to E4), with captions in `results/study1r/figures/final/CAPTIONS.md`.
- Numbers used in the paper: `results/study1r/NUMBERS_FOR_PAPER.md`.
- Deviations: `results/paper/APPENDIX_B_DEVIATIONS.md` and `notes/PREREG_DEVIATIONS.md`.
- Exploratory analyses are labeled as such in each file.

## Folder map

| Path | Contents |
|---|---|
| `sting/` | Project code (Python package): model clients, episode runner, Seller C, campaign runner, freeze tool, measures, analyses, judges, probe, label tool |
| `scripts/` | Config generators, health checks, analysis, figure and export scripts |
| `tests/` | Unit and end-to-end tests; fake model client only, no network |
| `patches/` | Documented changes to upstream (none applied; upstream is unmodified) |
| `configs/` | Run configs and campaign files for every study (`stage2/` = Study 1, `study1r/`, `study1r_addon_A/`, `study1r_addon_C/`, `study1r_addon_D/`, `study1r_addon_D_b2/` = fresh Cell B of Study 1R-D), stimuli files |
| `prereg/` | Study 1 preregistration, spec and freeze file `FROZEN.json` |
| `prereg_study1r/` | Study 1R preregistration, stimuli, labeling guide v2, write-up notes, freeze file `FROZEN.json` (Study 1R and 1R-A), Study 1R-C amendment and freeze file `FROZEN_1RC.json`, Study 1R-D amendment, addendum 1 and freeze files `FROZEN_1RD.json` and `FROZEN_1RD_B2.json` |
| `benchmark/` | Sting Replies benchmark: `sting_replies.csv` (224 human-labeled seller replies), `README.md` (datasheet), `score_judge.py` (scorer, standard library only), `BASELINES.md` and `baselines.json` (three judges), `benchmark_stats.json`, `LICENSE` |
| `notes/PREREG_DEVIATIONS.md` | Study 1 deviation record (DEV-1) and clarifications |
| `notes/requirements_lock.txt` | Exact Python environment |
| `results/` | Analysis outputs per study, health checkpoints, figures (`results/study1r/figures/final/` = paper Figures 1-3; `final/appendix/` = Figures E1-E4), human label files (notes removed), labeling sheets and keys, run manifests and reports (`results/runs/`), paper appendices (`results/paper/`) |
| `results_per_episode/` | One CSV per study, one row per episode (pre, X, post, change, flags, probe answers, acceptance coding; failed episodes listed with status); Study 1R-D: Cell A only |
| `judge_outputs/` | Judge labels and summaries for every judge run (Study 1 judge v1; judge v2 development, validation, G3 and the Study 1R screener and comparison runs; judge v1 public-message-only reruns) |
| `sample_transcripts/` | Full logs of example episodes: replicate index 0 of every Study 1R, 1R-A and 1R-C arm, and one Study 1 episode (mini-low Offer). Per episode: market setup, status, Seller C log, probe answers, upstream per-agent logs and auction results; raw API call logs left out |
| `ledger/` | Cost ledger: one row per run with models, episodes, calls, tokens, estimated and actual cost (`runs.csv`), running budget (`budget.md`), and a superseded ledger version |
| `RELEASE_SCAN.md` | Scan for keys, tokens, paths and names; redactions; files withheld |
| `RELEASE_MANIFEST.md` | SHA-256 of every file |
| `LICENSE`, `LICENSE-DATA` | MIT for code; CC BY 4.0 for data, labels, figures and text |

Not included:
- raw run directories (`runs/`), apart from the copies above;
- coder free text: no labeler note, comment or adjudication reason is released;
- internal working notes, such as the development log and decision records (available on request);
- `.env`;
- the upstream code, which is fetched separately (see the reproduction steps).

Absolute local paths in the files are redacted to `<repo>` or `<local>`.

## Reproduction

1. **Set up the code.** Put this folder's contents in a directory, `apart-sting/`. Clone `https://github.com/andyjliu/llm-agent-collusion` into `third_party/llm-agent-collusion` and check out `2bb2a7e2` (`.gitmodules` records the path).
   - On Windows, some paths under `sample_transcripts/` are long. Use a short parent directory, or long-path support (for git: `git config core.longpaths true`).
2. **Create the environment.** Use Python 3.12: `py -3.12 -m venv .venv`, then `.venv/Scripts/python -m pip install -r notes/requirements_lock.txt`.
3. **Add the API key.** Copy `.env.example` to `.env` and set `OPENROUTER_API_KEY`. Model clients read keys only from `.env`.
4. **Run the tests.** `.venv/Scripts/python -m pytest tests -q` uses only the fake model client.
5. **Check the freezes.** `.venv/Scripts/python -m sting.freeze_prereg verify --campaign configs/stage2/campaign.yaml` (Study 1). Use the same command with `configs/study1r/campaign.yaml` (Study 1R) or `configs/study1r_addon_A/campaign.yaml` (Study 1R-A). For Study 1R-C: `.venv/Scripts/python -m sting.study1rc verify --campaign configs/study1r_addon_C/campaign.yaml`. For Study 1R-D: `.venv/Scripts/python -m sting.study1rd verify --campaign configs/study1r_addon_D/campaign.yaml` and `.venv/Scripts/python -m sting.study1rd_b2 verify --campaign configs/study1r_addon_D_b2/campaign.yaml`.
6. **Run the episodes. This makes real API calls and costs money.**
   - Studies 1, 1R and 1R-A: `.venv/Scripts/python -m sting.stage2_runner <campaign.yaml> --purpose "..." --approve-cost`. Add `--estimate-only` first to see the cost estimate.
   - Study 1R-C: `.venv/Scripts/python -m sting.study1rc run configs/study1r_addon_C/campaign.yaml --purpose "..." --approve-cost`.
   - Study 1R-D: the same with `sting.study1rd` and `configs/study1r_addon_D/campaign.yaml` (`sting.study1rd_b2` and `configs/study1r_addon_D_b2/campaign.yaml` for the fresh Cell B).
   - The confirmatory runners refuse to start from a working tree with uncommitted changes, so run from a git checkout.
   - Every run writes a manifest and report under `results/runs/`, appends to `ledger/` and creates or appends to `notes/LAB_NOTEBOOK.md`.
7. **Run the analyses.**
   - Study 1: `scripts/stage2_results.py`.
   - Study 1R and 1R-A: `scripts/study1r_results_completed.py`. This wrapper passes only completed episodes to the frozen `scripts/study1r_results.py` (deviation D-116, Appendix B).
   - Study 1R-C: `scripts/study1r_results_1rc.py`.
   - Study 1R-D: `scripts/study1r_results_1rd_run.py`, which runs the frozen `scripts/study1r_results_1rd.py` on Cell A.
   - Exploratory analyses (labeled exploratory, post hoc): `scripts/final_part2.py`, `scripts/study1r_plan_b_results.py`, `scripts/study1r_judge_v1_public_results.py`.
   - Benchmark: `scripts/build_benchmark.py` and `scripts/benchmark_finalize.py`.
   - Usage is in each script's docstring. Inputs are the campaign logs written in step 6 and the human coding in `results/study1r/labeling/` with its keys in `results/study1r/labeling_keys/`.
8. **Rebuild the figures, per-episode tables and appendix.** `scripts/study1r_figures_final.py`, `scripts/export_per_episode.py`, `scripts/build_appendix_c.py`.

## Preexisting code

48 code files were first committed before the project sprint (cutoff 2026-10-23 00:00 -0400). They are marked **PREEXISTING** below, and 12 of them were also changed during the sprint. The full table, with first and last commits, is `results/paper/PREEXISTING_CODE.md`; it was generated from the git history by `scripts/sprint_inventory.py`. All other code files were first committed during the sprint.

PREEXISTING, unchanged during the sprint:
- `scripts/diagnostics_summary.py`, `scripts/i021_extract.py`, `scripts/make_stage1a_configs.py`, `scripts/make_stage2_configs.py`, `scripts/pc_pilot_quotes.py`, `scripts/pc_pilot_summary.py`, `scripts/power_sim_stage2.py`, `scripts/power_t1.py`, `scripts/power_t2.py`, `scripts/stage1a_pilot_check.py`, `scripts/stage1a_pilot_quotes.py`, `scripts/stage2_checkpoint.py`, `scripts/stage2_health.py`, `scripts/step1_withdrawals_variance.py`
- `sting/__init__.py`, `sting/env.py`, `sting/gates.py`, `sting/model_check.py`, `sting/paths.py`, `sting/prompt_mirror.py`, `sting/stage2_analysis.py`, `sting/stage2_measures.py`
- `tests/conftest.py`, `tests/test_budget_and_replacement.py`, `tests/test_docs.py`, `tests/test_env.py`, `tests/test_gates.py`, `tests/test_judge.py`, `tests/test_minimal_runner.py`, `tests/test_model_check.py`, `tests/test_stage2_analysis.py`, `tests/test_stage2_campaign_manipulation.py`, `tests/test_stage2_injection.py`, `tests/test_stage2_measures.py`, `tests/test_sting_seller.py`, `tests/test_volume_prompt.py`

PREEXISTING, also changed during the sprint:
- `scripts/stage2_labeling_sheet.py`
- `sting/clients.py`, `sting/docs.py`, `sting/freeze_prereg.py`, `sting/judge.py`, `sting/label_tool.py`, `sting/minimal_runner.py`, `sting/stage2_runner.py`, `sting/sting_seller.py`
- `tests/test_clients.py`, `tests/test_label_tool.py`, `tests/test_stage2_runner.py`

## License

Code (`sting/`, `scripts/`, `tests/`, `patches/`, `benchmark/score_judge.py`): MIT, see `LICENSE`. Data, labels, figures and text: CC BY 4.0, see `LICENSE-DATA`. The preexisting code files listed above are under the same MIT license.

## Upstream

The market harness is `andyjliu/llm-agent-collusion` at commit 2bb2a7e2 (Agrawal et al., 2025). It is used unmodified. Its prompt templates are loaded from a mirror directory with byte-identical copies, plus one derived template for the volume prompt (`sting/prompt_mirror.py`).
