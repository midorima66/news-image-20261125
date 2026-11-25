[![make.fun · news-image-20261125](https://make.fun/badge/news-image-20261125.svg)](https://make.fun/bounty/news-image-20261125?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261125)
[![rank](https://make.fun/badge/news-image-20261125/midorima66/news-image-20261125/rank.svg)](https://make.fun/bounty/news-image-20261125/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261125)
[![reward](https://make.fun/badge/news-image-20261125/midorima66/news-image-20261125/reward.svg)](https://make.fun/bounty/news-image-20261125?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261125)

# The World Today — Wednesday 25 November 2026

A one-image front page for the make.fun bounty
[news-image-20261125](https://make.fun/bounty/news-image-20261125): the day's
world news laid out as a newspaper front page, in a single 1024 × 1024
picture.

## What is in this repo

- `entry.png` — the finished front page. This is the entry itself.
- `main.py` — a small Python 3 script that hands the picture to the judging
  harness. It copies `entry.png`, untouched, to the output location.
- `LICENSE` — the licence for this entry.

## Running it

```sh
python3 main.py
```

Where the copy lands, in order of priority:

1. A path passed as the first argument — a file path is used as-is, and a
   directory gets `entry.png` written inside it.
2. The directory named by the `MAKEFUN_OUTPUT_DIR` environment variable.
3. `/output`, when neither of the above is given.

Missing parent folders are created automatically. The script needs no
network and no other input, so every run produces a byte-for-byte identical
copy of `entry.png`.

## Checking the output

The copy should hash exactly like the picture in this repo:

```sh
python3 main.py /tmp/out.png
sha256sum /tmp/out.png entry.png
```

Both hashes must match. Repeating the run in any of the three output modes
above always gives the same hash, because the file is copied, never
re-rendered.

## Bounty

Entry for [news-image-20261125 on make.fun](https://make.fun/bounty/news-image-20261125).
