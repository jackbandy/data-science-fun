#!/usr/bin/env python3
# NOTICE: This file was created by an LLM coding system (Claude, August 2026).
"""
Build the data for the /obscure-films/ page from IMDb's public TSV files.

Unlike collect.py (which keeps only the top-1000 + a 1000-film random sample and
drops the IMDb title ID), this keeps the FULL distribution of rated movies so the
page can draw a percentile bar chart, and keeps `tconst` so gallery cards can
link to IMDb.

Output: docs/obscure-films/data/obscure-films.json
  {
    "generated": "<ISO timestamp>",
    "totalMovies": N,
    "ticks":  [0.1, 1, 2, ..., 99, 99.9],
    "bars":   [ {"low":0.1,"high":1,"totalVotes":..,"count":..}, ... 100 ... ],
    "pool":   [ {"id":"tt..","t":"Title","y":"1994","g":"Drama","r":"9.3","v":3195314,"p":5.3}, ... ]
  }

The most-popular 0.1% and most-obscure 0.1% are excluded, so the visible range
is 0.1% -> 99.9% in 100 one-percent bands: [0.1,1), [1,2), ..., [98,99), [99,99.9).
`pool` is a stratified random sample (POOL_PER_BUCKET per band, seeded) that the
page samples from when a user picks a percentile range.

Run:  python3 build_obscure.py     (needs network; downloads ~100 MB)
"""

import json
import os
import random
from datetime import datetime, timezone

# Reuse the download + TSV parser from collect.py (no import side effects:
# main() is __main__-guarded, and the module only defines constants/functions).
from collect import fetch_tsv_gz, BASICS_URL, RATINGS_URL

SEED = 42
POOL_PER_BUCKET = 50

# Percentile tick marks: 100 one-percent bands framed by 101 ticks. The end
# ticks are the 0.1% exclusion boundaries (the most/least-voted 0.1% are left out);
# the first band [0.1,1) and last band [99,99.9) are 0.9% wide, the rest are 1%.
TICKS = [0.1] + [float(i) for i in range(1, 100)] + [99.9]

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
# movies-from-imdb -> datasets -> repo root (two levels up).
REPO_ROOT = os.path.dirname(os.path.dirname(SCRIPT_DIR))
OUT_PATH = os.path.join(REPO_ROOT, "docs", "obscure-films", "data", "obscure-films.json")


def bucket_index(pct):
    """Map a percentile in [0.1, 99.9) to its one-percent band index 0..99."""
    if pct < 0.1 or pct >= 99.9:
        return None  # outside the visible range -> excluded
    if pct < 1:
        return 0
    if pct >= 99:
        return 99
    return int(pct)  # [1,2) -> 1, ..., [98,99) -> 98


def main():
    basics = fetch_tsv_gz(BASICS_URL)
    ratings = fetch_tsv_gz(RATINGS_URL)

    ratings_map = {r["tconst"]: r for r in ratings}

    movies = []
    for row in basics:
        if row["titleType"] != "movie":
            continue
        tconst = row["tconst"]
        r = ratings_map.get(tconst)
        if r is None:
            continue
        nv = r["numVotes"]
        movies.append({
            "id": tconst,
            "t": row["primaryTitle"],
            "y": row["startYear"],
            "g": row["genres"],
            "r": r["averageRating"],
            "v": int(nv) if str(nv).isdigit() else 0,
        })

    n = len(movies)
    print(f"Total rated movies: {n}")

    # Most popular first. Rank 0 = most popular = percentile 0.
    movies.sort(key=lambda m: m["v"], reverse=True)

    for i, m in enumerate(movies):
        m["pct"] = (i / n) * 100 if n else 0

    # Bucket the visible films (exclude top 1% and bottom 1%).
    buckets = [[] for _ in range(len(TICKS) - 1)]
    for m in movies:
        b = bucket_index(m["pct"])
        if b is not None:
            buckets[b].append(m)

    bars = []
    for i, group in enumerate(buckets):
        total = sum(m["v"] for m in group)
        bars.append({
            "low": TICKS[i],
            "high": TICKS[i + 1],
            "totalVotes": total,
            "count": len(group),
        })

    # Stratified random sample per bucket for the client-side sampling pool.
    # Each film carries its exact percentile `p` (1 decimal) so the page's 1%-step
    # gates can filter the pool to any span, not just whole buckets.
    rng = random.Random(SEED)
    pool = []
    for i, group in enumerate(buckets):
        sample = rng.sample(group, min(POOL_PER_BUCKET, len(group)))
        for m in sample:
            pool.append({
                "id": m["id"],
                "t": m["t"],
                "y": m["y"],
                "g": m["g"],
                "r": m["r"],
                "v": m["v"],
                "p": round(m["pct"], 1),
            })

    out = {
        "generated": datetime.now(timezone.utc).strftime("%Y-%m-%d"),
        "totalMovies": n,
        "ticks": TICKS,
        "bars": bars,
        "pool": pool,
    }

    os.makedirs(os.path.dirname(OUT_PATH), exist_ok=True)
    with open(OUT_PATH, "w", encoding="utf-8") as f:
        json.dump(out, f, separators=(",", ":"))
    print(f"Wrote {len(pool)} pool films across {len(bars)} bands -> {OUT_PATH}")
    top = max(bars, key=lambda b: b["totalVotes"])
    bot = min(bars, key=lambda b: b["totalVotes"])
    print(f"  most-voted band {top['low']}-{top['high']}: {top['count']:,} films, {top['totalVotes']:,} votes")
    print(f"  least-voted band {bot['low']}-{bot['high']}: {bot['count']:,} films, {bot['totalVotes']:,} votes")


if __name__ == "__main__":
    main()