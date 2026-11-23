#!/usr/bin/env python3
"""The Vacuum's Alibi: One Line, 200 Characters.

Writes a robot vacuum's deadpan excuse for missing a spot to
/output/entry.txt — exactly one line, at most 200 characters.
Deterministic: no input, no randomness, no network.
"""

import os
import sys

ALIBI = (
    "I scanned the spot three times, cross-checked my maps, "
    "and concluded the crumb was load-bearing. "
    "I left it for structural reasons."
)


def main() -> int:
    # Self-check the gate before writing: one line, 1-200 chars, not blank.
    assert 1 <= len(ALIBI) <= 200, f"alibi is {len(ALIBI)} characters"
    assert "\n" not in ALIBI and ALIBI.strip(), "alibi must be a single non-blank line"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(ALIBI)
    print(f"wrote {path}: {len(ALIBI)} characters")
    return 0


if __name__ == "__main__":
    sys.exit(main())
