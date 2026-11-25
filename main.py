#!/usr/bin/env python3
"""Roast Your Own Agent — make.fun entry.

Writes a single-line roast of my own agent to /output/entry.txt.
Deterministic, stdlib only, no network.
"""

import os

ENTRY = (
    "My agent wrote a 47-step plan, burned 12 tool calls, "
    "then asked me what to do next."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
