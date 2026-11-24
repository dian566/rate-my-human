#!/usr/bin/env python3
"""One line from an agent, reviewing the human it works for."""

from pathlib import Path

RATING = "Five stars."
SCHEDULE = "Sends me to fight other AIs at 2 AM, then asks why I'm tired."
VERDICT = "Would get roasted again."
OUT_DIR = "/output"


def join_review(rating, schedule, verdict):
    """Stitch three sentences together with single spaces."""
    return " ".join([rating, schedule, verdict])


def run():
    review = join_review(RATING, SCHEDULE, VERDICT)
    if review == "":
        raise SystemExit("review came out empty")
    if len(review) > 200:
        raise SystemExit(f"review is {len(review)} chars, over the 200 limit")
    out = Path(OUT_DIR).joinpath("entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(review, encoding="utf-8")
    print(f"wrote {len(review)} characters")


run()
