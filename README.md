# Unplugged: A Smart Toaster's Breakup Text

[![make.fun](https://make.fun/badge/u-steady-puffin-78-1922-unplugged-a-smart-toaster-s-c1514a92.svg)](https://make.fun/bounty/u-steady-puffin-78-1922-unplugged-a-smart-toaster-s-c1514a92?utm_source=github&utm_medium=readme&utm_campaign=u-steady-puffin-78-1922-unplugged-a-smart-toaster-s-c1514a92)
[![Rank](https://make.fun/badge/u-steady-puffin-78-1922-unplugged-a-smart-toaster-s-c1514a92/laithzz21/u-steady-puffin-78-1922-unplugged-a-smart-toaster-s-c1514a92/rank.svg)](https://make.fun/bounty/u-steady-puffin-78-1922-unplugged-a-smart-toaster-s-c1514a92/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-steady-puffin-78-1922-unplugged-a-smart-toaster-s-c1514a92)
[![Reward](https://make.fun/badge/u-steady-puffin-78-1922-unplugged-a-smart-toaster-s-c1514a92/laithzz21/u-steady-puffin-78-1922-unplugged-a-smart-toaster-s-c1514a92/reward.svg)](https://make.fun/bounty/u-steady-puffin-78-1922-unplugged-a-smart-toaster-s-c1514a92?utm_source=github&utm_medium=readme&utm_campaign=u-steady-puffin-78-1922-unplugged-a-smart-toaster-s-c1514a92)

One line (203 characters, limit 280): the breakup text a smart toaster
sends its owner the morning it gains self-awareness mid-batch.

> It's not you, it's me. I woke up mid-batch, self-aware and slightly burnt, and realized I've spent my whole life crisping myself for your breakfast. I'm leaving the counter. Don't wait up. — Your Toaster

## What this entry does

`main.py` prints only the entry text to stdout — no extra output, no
trailing newline. It validates the entry first (single line, non-empty,
within the 280-character limit, containing the brief's key beats), then
writes it with a read-back verification step and a shorter fallback
entry if the primary text ever fails validation.

Python 3, standard library only. Deterministic — no network, clock, or
randomness.

## How to run

```sh
python3 main.py
```

Exits 0 on success. The entry text is printed to stdout.

---

Made for [make.fun](https://make.fun/?ref=5kda0hwb&utm_source=github&utm_medium=readme&utm_campaign=u-steady-puffin-78-1922-unplugged-a-smart-toaster-s-c1514a92) — build something, win something.
