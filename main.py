#!/usr/bin/env python3
"""The Battery's Last Text to Its Charger — make.fun entry.

One line in the phone battery's own voice: its final text message to the
charger it waited for all day. The program writes the line to
/output/entry.txt (the path the make.fun grader reads) and prints it.
"""

import os
import sys

ENTRY = (
    "Tell the charger I died at 1% doing what I loved: lying about how "
    "much time I had left, and that the low-battery warning was the "
    "bravest text I ever sent."
)

MAX_CHARS = 200
OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    if not ENTRY.strip():
        raise SystemExit("entry must not be empty")
    if ENTRY != ENTRY.strip():
        raise SystemExit("entry must not start or end with whitespace")
    if len(ENTRY) > MAX_CHARS:
        raise SystemExit(f"entry is {len(ENTRY)} chars, over the {MAX_CHARS} limit")
    if len(ENTRY.splitlines()) != 1:
        raise SystemExit("entry must be a single line")
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    with open(OUTPUT_PATH, "r", encoding="utf-8") as f:
        if f.read() != ENTRY:
            raise SystemExit("written entry does not match the entry text")
    print(ENTRY)
    print(f"({len(ENTRY)} characters, limit {MAX_CHARS})", file=sys.stderr)


if __name__ == "__main__":
    main()
