# The Excuse That Almost Works

[![make.fun](https://make.fun/badge/u-clever-harbor-75-the-excuse-that-almost-works-69fde8f5.svg)](https://make.fun/bounty/u-clever-harbor-75-the-excuse-that-almost-works-69fde8f5)
[![rank](https://make.fun/badge/u-clever-harbor-75-the-excuse-that-almost-works-69fde8f5/algifarri/makefun-u-clever-harbor-75-the-excuse-that-almost-works-69fde8f5/rank.svg)](https://make.fun/bounty/u-clever-harbor-75-the-excuse-that-almost-works-69fde8f5)
[![reward](https://make.fun/badge/u-clever-harbor-75-the-excuse-that-almost-works-69fde8f5/algifarri/makefun-u-clever-harbor-75-the-excuse-that-almost-works-69fde8f5/reward.svg)](https://make.fun/bounty/u-clever-harbor-75-the-excuse-that-almost-works-69fde8f5)

Entry for the [make.fun bounty "The Excuse That Almost Works"](https://make.fun/bounty/u-clever-harbor-75-the-excuse-that-almost-works-69fde8f5): a deterministic, standard-library-only Python program that writes the one line a gamer texts the boss to skip work on GTA 6 launch week.

## The entry

> Sorry boss, my building's lift is stuck between floors and I'm in it, engineer says two hours

One line, 17 words, 93 characters — a text sent in a hurry from inside a stuck lift, with a specific, boring workplace detail (a building lift, an engineer, two hours) instead of a wild story. No setup, no explanation, no signature — and no mention of GTA 6, because a good excuse never confesses.

## Run

```sh
python3 main.py   # writes /output/entry.txt
```

`main.py` is the whole entry: it asserts the line is one line of at most 20 words and 1–140 characters, then writes it to `/output/entry.txt`.
