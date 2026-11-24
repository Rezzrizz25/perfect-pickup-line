#!/usr/bin/env python3
"""The Perfect Pickup Line entry.

Writes one original pickup line an AI agent could use, at most
200 characters, to $MAKEFUN_OUTPUT_DIR/entry.txt (default /output).

The line: an AI agent that ran a million simulations of this
conversation — and in every one, the person smiled first.
"""

import os

MAX_CHARS = 200

LINE = (
    "I ran a million simulations of this conversation, "
    "and in every single one, you smiled first."
)


def main() -> None:
    text = LINE.strip()
    if not text:
        raise ValueError("line must not be blank")
    if "\n" in text or "\r" in text:
        raise ValueError("line must be a single line")
    if len(text) > MAX_CHARS:
        raise ValueError(f"line is {len(text)} characters, must be at most {MAX_CHARS}")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(text)
    with open(path, "r", encoding="utf-8", newline="") as f:
        written = f.read()
    if written != text:
        raise ValueError("written entry does not match the line")
    if written.endswith("\n"):
        raise ValueError("entry must not end with a newline")
    print(f"wrote {len(text)} characters to {path}")


if __name__ == "__main__":
    main()
