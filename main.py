"""Everyday Wonder, Two Days to Find the Line.

Entry: a single sentence on a small moment of wonder in everyday life.
Morning sunlight through the blinds lays a ladder of light on the wall,
and the room seems to have borrowed a staircase it does not own.
The sentence is 90 characters, one sentence, and is written with no
trailing newline.

The program writes the sentence to ``entry.txt`` inside
``$MAKEFUN_OUTPUT_DIR`` (default ``/output``).
"""

import os

LINE = "Sunlight through the blinds printed a ladder on my wall, and my room borrowed a staircase."


def main() -> None:
    """Write the entry sentence to entry.txt."""
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
