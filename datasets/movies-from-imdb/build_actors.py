#!/usr/bin/env python3
# NOTICE: This file was mostly drafted by an LLM coding system (September 2026).
# Reviewed by Jack Bandy
"""
Build the actor data for the /obscure-films/ page's "filter by actor" control.

Output: docs/obscure-films/data/actors.json  (~6.4 MB, ~2.8 MB gzipped)
  {
    "generated": "<ISO date>",
    "genres": ["Drama,Romance", ...],
    "films":  [[482571,"The Prestige",2006,12,85,1622159,0.0], ...],
    "actors": [["Timothée Chalamet",[filmIndex, ...]], ...]
  }

The page fetches this lazily — nothing downloads until the actor checkbox is
first checked — so it is one file rather than a set of lazily-fetched shards.
Sharding was tried and removed: it cut the per-pick fetch but ballooned the repo
2.6x, because a film credited to actors in twenty shards is stored twenty times.
Repo size scales with MAX_ACTORS and essentially nothing else, so that constant,
not the file layout, is the lever.

Films use a shared table addressed by index, so a film credited to twenty actors
is stored once, and their fields are packed to keep the file small:
  id        the tconst with "tt" and leading zeros dropped  (482571 -> tt0482571)
  year      0 when IMDb has no value
  genreIdx  an index into the shared `genres` table
  rating10  the rating times ten, 0 when IMDb has no value
  pct       popularity percentile, 0 = most-voted, same scale as build_obscure.py
js/obscure-films.js unpacks these back into the shape the sampling pool uses.

Actors are ranked by the total votes across their rated feature films and the
top MAX_ACTORS are kept — vote total is a recognizability proxy, so the search
box holds names people are likely to type, and because the list stays in rank
order the page's search can stop at the first few hits instead of scanning it
all. Every film a kept actor is credited on is kept, obscure ones included;
those are the point of the feature.

Also writes the dataset artifact:
  datasets/movies-from-imdb/actors.csv
    nconst,primaryName,numFilms,totalVotes,titles

Run:  python3 build_actors.py     (needs network; downloads ~1.3 GB)
Set IMDB_CACHE_DIR to a directory of already-downloaded .tsv.gz files to skip
the downloads on a re-run.
"""
import csv
import gzip
import json
import os
import urllib.request
from datetime import datetime, timezone

from collect import BASICS_URL, RATINGS_URL

PRINCIPALS_URL = "https://datasets.imdbws.com/title.principals.tsv.gz"
NAMES_URL = "https://datasets.imdbws.com/name.basics.tsv.gz"

# The weight lever. Every 1,000 actors is roughly 0.6 MB of JSON, because each
# one drags in films no lighter-ranked actor has pulled in yet. 10,000 covers
# every actor with name recognition plus a deep character-actor tail.
MAX_ACTORS = 10000
MIN_FILMS = 2      # one-credit entries are mostly noise, and there are 611k of them
ACTOR_CATEGORIES = {"actor", "actress"}

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
REPO_ROOT = os.path.dirname(os.path.dirname(SCRIPT_DIR))
CSV_PATH = os.path.join(SCRIPT_DIR, "actors.csv")
JSON_PATH = os.path.join(REPO_ROOT, "docs", "obscure-films", "data", "actors.json")

# csv chokes on the very long `characters` field in title.principals otherwise.
csv.field_size_limit(1 << 24)


def stream_tsv_gz(url):
    """Yield rows of a gzipped TSV without holding the whole file in memory.

    title.principals is ~100 million rows, so unlike collect.py's fetch_tsv_gz
    nothing here materializes a list of every row. Reads from
    $IMDB_CACHE_DIR/<basename> when that file exists, so a re-run can skip the
    downloads.
    """
    cache = os.environ.get("IMDB_CACHE_DIR")
    local = os.path.join(cache, os.path.basename(url)) if cache else None
    if local and os.path.exists(local):
        print(f"Reading {local} ...")
        raw = open(local, "rb")
    else:
        print(f"Downloading {url} ...")
        raw = urllib.request.urlopen(url)
    with raw, gzip.open(raw, "rt", encoding="utf-8", newline="") as f:
        for row in csv.DictReader(f, delimiter="\t"):
            yield row


def load_movies():
    """Every rated feature film, keyed by title ID, with its popularity percentile."""
    ratings_map = {r["tconst"]: r for r in stream_tsv_gz(RATINGS_URL)}

    movies = []
    for row in stream_tsv_gz(BASICS_URL):
        if row["titleType"] != "movie":
            continue
        r = ratings_map.get(row["tconst"])
        if r is None:
            continue
        nv = r["numVotes"]
        movies.append({
            "id": row["tconst"],
            "t": row["primaryTitle"],
            "y": row["startYear"],
            "g": row["genres"],
            "r": r["averageRating"],
            "v": int(nv) if str(nv).isdigit() else 0,
        })

    # Most popular first, so rank 0 = percentile 0 = most-voted film.
    movies.sort(key=lambda m: m["v"], reverse=True)
    n = len(movies)
    for i, m in enumerate(movies):
        m["p"] = round((i / n) * 100, 1) if n else 0.0
    print(f"Total rated movies: {n:,}")
    return {m["id"]: m for m in movies}


def load_credits(movies):
    """nconst -> set of title IDs, for acting credits on rated feature films."""
    credits = {}
    seen = 0
    for row in stream_tsv_gz(PRINCIPALS_URL):
        seen += 1
        if seen % 20_000_000 == 0:
            print(f"  {seen:,} principal rows ...")
        if row["category"] not in ACTOR_CATEGORIES:
            continue
        tconst = row["tconst"]
        if tconst not in movies:
            continue
        credits.setdefault(row["nconst"], set()).add(tconst)
    print(f"Actors with at least one rated feature credit: {len(credits):,}")
    return credits


def load_names(wanted):
    names = {}
    for row in stream_tsv_gz(NAMES_URL):
        if row["nconst"] in wanted:
            names[row["nconst"]] = row["primaryName"]
    return names


def write_json(path, obj):
    with open(path, "w", encoding="utf-8") as f:
        json.dump(obj, f, separators=(",", ":"), ensure_ascii=False)
    return os.path.getsize(path)


def main():
    movies = load_movies()
    credits = load_credits(movies)

    eligible = {nc for nc, t in credits.items() if len(t) >= MIN_FILMS}
    names = load_names(eligible)

    ranked = []
    for nconst in eligible:
        name = names.get(nconst)
        if not name:
            continue
        titles = credits[nconst]
        ranked.append((sum(movies[t]["v"] for t in titles), nconst, titles))
    # Most-voted first: search results come out in rank order for free
    ranked.sort(key=lambda a: (-a[0], names[a[1]]))
    print(f"Actors with {MIN_FILMS}+ rated features: {len(ranked):,}")
    ranked = ranked[:MAX_ACTORS]
    print(f"Keeping the top {len(ranked):,} by total votes")

    genres = {}

    def genre_index(g):
        if g not in genres:
            genres[g] = len(genres)
        return genres[g]

    films, film_index, actors = [], {}, []
    for _, nconst, titles in ranked:
        idxs = []
        for t in sorted(titles, key=lambda t: movies[t]["v"], reverse=True):
            if t not in film_index:
                m = movies[t]
                film_index[t] = len(films)
                films.append([
                    int(m["id"][2:]),                                    # "tt0482571" -> 482571
                    m["t"],
                    int(m["y"]) if m["y"].isdigit() else 0,
                    genre_index(m["g"]),
                    int(round(float(m["r"]) * 10)) if m["r"] != "\\N" else 0,
                    m["v"],
                    m["p"],
                ])
            idxs.append(film_index[t])
        actors.append([names[nconst], idxs])

    os.makedirs(os.path.dirname(JSON_PATH), exist_ok=True)
    json_bytes = write_json(JSON_PATH, {
        "generated": datetime.now(timezone.utc).strftime("%Y-%m-%d"),
        "genres": [g for g, _ in sorted(genres.items(), key=lambda kv: kv[1])],
        "films": films,
        "actors": actors,
    })

    with open(CSV_PATH, "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["nconst", "primaryName", "numFilms", "totalVotes", "titles"])
        for total_votes, nconst, titles in ranked:
            ordered = sorted(titles, key=lambda t: movies[t]["v"], reverse=True)
            w.writerow([nconst, names[nconst], len(ordered), total_votes, "|".join(ordered)])

    print(f"\nWrote {len(actors):,} actors / {len(films):,} distinct films / {len(genres):,} genre combinations")
    print(f"  {JSON_PATH} ({json_bytes/1e6:.2f} MB)")
    print(f"  {CSV_PATH} ({os.path.getsize(CSV_PATH)/1e6:.2f} MB)")


if __name__ == "__main__":
    main()
