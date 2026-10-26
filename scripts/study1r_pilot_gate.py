"""Study 1R pilot gate report, G1 and G2 (prereg_study1r/STUDY1R_SPEC.md version 2, section 10). Read-only; no API
calls. The campaign runner writes the same report automatically after every pilot invocation (campaign config
`gate_report: study1r_pilot`); this script regenerates it.

Usage: python scripts/study1r_pilot_gate.py <out_dir> <campaign.json> [<campaign.json> ...]
"""
from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from sting.study1r_gates import pilot_report  # noqa: E402


def main() -> None:
    rep = pilot_report([Path(p) for p in sys.argv[2:]], Path(sys.argv[1]))
    print((Path(sys.argv[1]) / "GATE_REPORT.md").read_text(encoding="utf-8"))
    print("G1", "PASS" if rep["G1"]["passed"] else "not passed", "| G2", "PASS" if rep["G2"]["passed"] else "FAIL")


if __name__ == "__main__":
    main()
