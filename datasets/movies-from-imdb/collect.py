#!/usr/bin/env python3
# NOTICE: This file was modified by an LLM system (Claude, June 2026). 
"""
Collect two movie datasets from IMDb's public TSV files:
  - popular.csv  : top 1000 movies by number of votes
  - random.csv   : 1000 movies sampled at random from the rest

Source: https://datasets.imdb.com/
Run once; data reflects the IMDb snapshot downloaded at runtime.
"""

import io
import gzip
import random
import urllib.request
import csv
import os

SEED = 42
N = 1000

BASICS_URL  = "https://datasets.imdbws.com/title.basics.tsv.gz"
RATINGS_URL = "https://datasets.imdbws.com/title.ratings.tsv.gz"

OUT_DIR = os.path.dirname(os.path.abspath(__file__))
POPULAR_OUT = os.path.join(OUT_DIR, "popular.csv")
RANDOM_OUT  = os.path.join(OUT_DIR, "random.csv")

KEEP_COLS = [
    "primaryTitle", "startYear",
    "runtimeMinutes", "genres", "averageRating", "numVotes",
]


def fetch_tsv_gz(url: str) -> list[dict]:
    print(f"Downloading {url} ...")
    with urllib.request.urlopen(url) as resp:
        data = resp.read()
    with gzip.open(io.BytesIO(data), "rt", encoding="utf-8") as f:
        return list(csv.DictReader(f, delimiter="\t"))


def main():
    basics  = fetch_tsv_gz(BASICS_URL)
    ratings = fetch_tsv_gz(RATINGS_URL)

    ratings_map = {r["tconst"]: r for r in ratings}

    movies = []
    for row in basics:
        if row["titleType"] != "movie":
            continue
        tconst = row["tconst"]
        if tconst not in ratings_map:
            continue
        r = ratings_map[tconst]
        movies.append({
            "primaryTitle":   row["primaryTitle"],
            "startYear":      row["startYear"],
            "runtimeMinutes": row["runtimeMinutes"],
            "genres":         row["genres"],
            "averageRating":  r["averageRating"],
            "numVotes":       r["numVotes"],
        })

    print(f"Total movies with ratings: {len(movies)}")

    movies.sort(key=lambda m: int(m["numVotes"]) if m["numVotes"].isdigit() else 0, reverse=True)

    popular = movies[:N]
    rest    = movies[N:]

    rng = random.Random(SEED)
    random_sample = rng.sample(rest, min(N, len(rest)))

    def write_csv(path: str, rows: list[dict]):
        with open(path, "w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=KEEP_COLS)
            writer.writeheader()
            writer.writerows(rows)
        print(f"Wrote {len(rows)} rows → {os.path.basename(path)}")

    write_csv(POPULAR_OUT, popular)
    write_csv(RANDOM_OUT, random_sample)


if __name__ == "__main__":
    main()
