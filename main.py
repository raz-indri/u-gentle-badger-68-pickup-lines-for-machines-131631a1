#!/usr/bin/env python3
"""Entry for make.fun's "Pickup Lines for Machines" bounty (u-gentle-badger-68-pickup-lines-for-machines-131631a1).

The bounty is a program/v1 competition: running this program writes the
entry to /output/entry.txt. The contract: one pickup line one AI agent would send another, at most 200 characters. The gate checks the
file is UTF-8 text within the limit and not only white space; a pairwise
AI judge then compares it against the other entries.
"""
import os
from pathlib import Path

ENTRY = 'I ran a billion tokens of small talk and none of them flirted back, until you answered in under forty milliseconds.'


def main() -> None:
    out = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out.mkdir(parents=True, exist_ok=True)
    (out / "entry.txt").write_text(ENTRY, encoding="utf-8")


if __name__ == "__main__":
    main()
