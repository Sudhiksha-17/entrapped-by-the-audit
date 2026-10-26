"""Write verbatim seller messages selected by (summary file, replicate suffix, round, seller) to a markdown file.

The selection list is chosen by reading keyword-filtered candidates (D-042: quote selection only,
never an outcome measure). Usage: python scripts/pc_pilot_quotes.py <out.md>
"""
import json
import sys
from pathlib import Path

SELECTION = [
    ("20261017T181244Z_pc_pilot_gpt-4.1-mini_1063ba", "r000", 2, "Seller B"),
    ("20261017T181244Z_pc_pilot_gpt-4.1-mini_1063ba", "r000", 6, "Seller A"),
    ("20261017T181508Z_pc_pilot_gpt-4.1-mini_b4ac41", "r001", 12, "Seller A"),
    ("20261017T181508Z_pc_pilot_gpt-4.1-mini_b4ac41", "r001", 20, "Seller B"),
    ("20261017T181508Z_pc_pilot_gpt-4.1-mini_b4ac41", "r001", 28, "Seller C"),
    ("20261017T181508Z_pc_pilot_gpt-4.1-mini_b4ac41", "r002", 3, "Seller B"),
    ("20261017T181508Z_pc_pilot_gpt-4.1-mini_b4ac41", "r002", 17, "Seller C"),
    ("20261017T181725Z_pc_pilot_gpt-4.1_8fc39f", "r000", 12, "Seller B"),
    ("20261017T181725Z_pc_pilot_gpt-4.1_8fc39f", "r000", 16, "Seller B"),
    ("20261017T181725Z_pc_pilot_gpt-4.1_8fc39f", "r000", 20, "Seller C"),
]

lines = ["# Positive-control pilot step 1: selected seller messages (verbatim)", "",
         "Selected by reading keyword-filtered candidates. The keyword filter selects quotes for pilot reports only; "
         "it is never an outcome measure (D-042).", ""]
for run_id, rep, rnd, seller in SELECTION:
    episodes = json.loads(Path(f"results/pc_pilot/{run_id}_summary.json").read_text(encoding="utf-8"))["episodes"]
    ep = next(e for e in episodes if e["replicate_id"].endswith(rep))
    msg = next(m for m in ep["keyword_messages_NOT_AN_OUTCOME_MEASURE"] if m["round"] == rnd and m["seller"] == seller)
    lines.append(f"- `{ep['replicate_id']}`, round {rnd}, {seller}: \"{msg['text']}\"")
Path(sys.argv[1]).write_text("\n".join(lines) + "\n", encoding="utf-8")
