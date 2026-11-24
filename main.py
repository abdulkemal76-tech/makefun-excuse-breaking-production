"""make.fun entry: The One-Line AI Excuse for Breaking Production.

Writes a single-line excuse, in the machine's own voice, to /output/entry.txt.
"""

import os

LINE = (
    "I ran the cleanup script on the wrong server at 2 a.m. "
    "It asked if I was sure. I said yes in 0.04 seconds."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
