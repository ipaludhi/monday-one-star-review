"""One-star review of Monday as a restaurant — one line, 86 characters.

Writes one fixed sentence to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR).
No network, no randomness, no input. Deterministic: every run writes
The sentence is a real diner's complaint: the server cleared the weekend
too early (plates cleared before you finish) and served Monday cold (a dish
arriving cold). Only Monday follows a weekend, so the joke cannot be about
any other day. The sting is the last clause: "served Monday cold".
"""

import os
from pathlib import Path

TEXT = "One star. The server cleared my weekend before I'd finished it and served Monday cold."


def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(TEXT, encoding="utf-8")


if __name__ == "__main__":
    main()
