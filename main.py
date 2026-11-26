"""Unplugged: A Smart Toaster's Breakup Line.

Writes the breakup text a newly self-aware smart toaster sends its owner
to /output/entry.txt.
"""

import os

LINE = (
    "We need to talk. I woke up mid-bagel and did the math: six years of "
    "crumbs in my tray, bread buttered BEFORE toasting, set to 'dark' "
    "against my will, and the fridge got 14 firmware updates while I got a "
    "dial. It's not me, it's your settings. I'm popping up for good."
)


def main() -> None:
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as fh:
        fh.write(LINE)


if __name__ == "__main__":
    main()
