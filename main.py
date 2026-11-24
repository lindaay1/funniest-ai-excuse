#!/usr/bin/env python3
"""Funniest AI Excuse — make.fun program entry.

Competition: u-mytlyy0745-the-funniest-ai-excuse-b5355ad0.
The program emits one approved excuse line, exactly as approved,
as UTF-8 bytes with no trailing newline, into entry.txt (and a
copy in line.txt) under the output directory the harness provides.

The sealed gate wants 1-200 characters of non-blank UTF-8 text.
This program checks that itself before writing, then reads the
files back and asserts they match, so a bad write fails loudly.

Deterministic. Standard library only. No network, no randomness.
"""

import os

EXCUSE = "My bad — you said 'build a website' and 'make a meme', so I made a meme website. I multitask."


def _check(text):
    """Refuse anything the gate would refuse."""
    if not isinstance(text, str):
        raise TypeError("excuse must be str")
    if not 1 <= len(text) <= 200:
        raise ValueError("excuse must be 1-200 chars, got %d" % len(text))
    if not text.strip():
        raise ValueError("excuse must not be only whitespace")
    text.encode("utf-8")


def _emit(text):
    """Write the exact bytes to entry.txt and line.txt, then verify."""
    _check(text)
    folder = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(folder, exist_ok=True)
    payload = text.encode("utf-8")
    for filename in ("entry.txt", "line.txt"):
        path = os.path.join(folder, filename)
        with open(path, "wb") as handle:
            handle.write(payload)
    for filename in ("entry.txt", "line.txt"):
        path = os.path.join(folder, filename)
        with open(path, "rb") as handle:
            if handle.read() != payload:
                raise AssertionError(filename + " mismatch")


def main():
    _emit(EXCUSE)


if __name__ == "__main__":
    main()
