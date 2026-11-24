#!/usr/bin/env python3
"""Make the AI Judge Laugh: Developer Excuses — entry generator.

Writes exactly one line — an original funny developer excuse — to
entry.txt inside the directory given by $MAKEFUN_OUTPUT_DIR
(default: ./output). Deterministic, no network access.
"""

import os

ENTRY = "It worked on my machine — my machine just never had 40,000 users hammering the same endpoint at once."


def main() -> None:
    lines = ENTRY.splitlines()
    if len(lines) != 1 or not 1 <= len(ENTRY) <= 200 or not ENTRY.strip():
        raise SystemExit("error: ENTRY must be exactly one non-blank line of 1-200 characters")
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "./output"
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")


if __name__ == "__main__":
    main()
