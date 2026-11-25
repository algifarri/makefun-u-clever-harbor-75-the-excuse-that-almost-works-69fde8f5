#!/usr/bin/env python3
"""The Excuse That Almost Works — the one line a gamer texts the boss.

Writes the excuse to /output/entry.txt (UTF-8, one line, 17 words,
93 characters). Deterministic, standard library only, no network.

The line: "Sorry boss, my building's lift is stuck between floors and
I'm in it, engineer says two hours"

Why this line: it is the text of someone typing from inside a stuck
lift, in a hurry, to a manager who has heard every excuse twice. The
detail is specific and boring — a building lift, an engineer, two
hours — instead of a wild story, so a tired manager would almost
believe it. The laugh comes from the excuse's own logic: he is texting
from inside the lift, which is exactly where a person in that mess
would be texting from. No dead grandmother, no flat tyre, no sudden
fever, no mention of GTA 6 at all — naming the game would be a
confession, and a good excuse never confesses. No setup, no
explanation, no signature: one line, plain words, sent in a hurry.
"""

import os

EXCUSE = (
    "Sorry boss, my building's lift is stuck between floors "
    "and I'm in it, engineer says two hours"
)
# One line, at most 20 words, 1 to 140 characters per the gate.


def main() -> None:
    words = EXCUSE.split()
    assert len(words) <= 20, f"expected at most 20 words, got {len(words)}"
    assert 1 <= len(EXCUSE) <= 140, (
        f"expected 1-140 characters, got {len(EXCUSE)}"
    )
    assert EXCUSE.strip() == EXCUSE and EXCUSE, (
        "entry must not be only whitespace"
    )
    assert "\n" not in EXCUSE, "entry must be a single line"
    assert EXCUSE.count("GTA") == 0, "a good excuse never names the game"
    # The grader mounts /output; create it defensively for local runs too.
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as fh:
        fh.write(EXCUSE)


if __name__ == "__main__":
    main()
