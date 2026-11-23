"""One Word From Grandma - a make.fun entry.

The whole entry is exactly one word (at most 30 characters): the word
a grandma would text about AI. "AIn't" is her voice and the subject in
a single breath - the dialect word she would actually type, with AI
sitting inside it. This program's only job is to deliver that text to
/output/entry.txt, deterministically.
"""

import os
from pathlib import Path

TEXT = "AIn't"

# The competition's gate: entry.txt must be UTF-8 text of 1 to 30
# characters, and the brief asks for exactly one word - no spaces, no
# punctuation tricks. Check both here so a careless edit to TEXT fails
# loudly at build time instead of silently producing an entry that is
# never judged.
MAX_CHARS = 30


def check_text(text: str) -> None:
    if not 1 <= len(text) <= MAX_CHARS:
        raise ValueError(f"word is {len(text)} characters, gate allows 1-{MAX_CHARS}")
    if len(text.split()) != 1:
        raise ValueError("entry must be exactly one word")


def output_dir() -> Path:
    # In the grader's container the output is /output; outside it,
    # MAKEFUN_OUTPUT_DIR stands in for that directory.
    return Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))


def main() -> None:
    check_text(TEXT)
    target = output_dir() / "entry.txt"
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(TEXT, encoding="utf-8")


if __name__ == "__main__":
    main()
