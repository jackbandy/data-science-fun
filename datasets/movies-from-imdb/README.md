# movies-from-imdb

Two movie datasets drawn from [IMDb's public data files](https://datasets.imdbws.com/), collected June 2026.

## Files

- `popular.csv` — Top 1000 movies ranked by number of IMDb votes
- `random.csv` — 1000 movies sampled at random from the remaining rated movies (seed 42)
- `actors.csv` — The 10,000 most-voted IMDb performers and the rated feature films they are credited on
- `collect.py` — Script that produced `popular.csv` and `random.csv`
- `build_actors.py` — Script that produced `actors.csv` (and the actor data the [Obscure Films](../../docs/obscure-films/) page loads)
- `build_obscure.py` — Script that builds the percentile data for the [Obscure Films](../../docs/obscure-films/) page

## Columns — `popular.csv` and `random.csv`

- `primaryTitle` *(title.basics)* — Release title
- `startYear` *(title.basics)* — Release year
- `runtimeMinutes` *(title.basics)* — Runtime in minutes; `\N` if unknown
- `genres` *(title.basics)* — Comma-separated genre list; `\N` if unknown
- `averageRating` *(title.ratings)* — IMDb weighted mean rating (1–10)
- `numVotes` *(title.ratings)* — Number of individual user ratings submitted

## Columns — `actors.csv`

- `nconst` *(name.basics)* — IMDb person ID; the page for the actor is `imdb.com/name/<nconst>/`
- `primaryName` *(name.basics)* — The actor's name as IMDb prints it
- `numFilms` — How many distinct rated feature films they are credited on
- `totalVotes` — Votes summed across those films; this is the ranking key
- `titles` — `|`-separated IMDb title IDs, most-voted first

`titles` is most of this file's 2.9 MB; skip it when you do not need the credits:

```python
import pandas as pd
actors = pd.read_csv("actors.csv", usecols=["primaryName", "numFilms", "totalVotes"])
```

## Methodology

**Popular set** — sorted all rated movies by `numVotes` descending, took the top 1000. Vote count is a better popularity proxy than rating alone because it reflects actual audience reach.

**Random set** — after removing the top 1000, drew a random sample of 1000 from the remainder (Python `random.sample`, seed 42 for reproducibility). This gives a rough cross-section of the long tail.

**Actor set** — took every `actor`/`actress` credit in `title.principals` that points at a rated feature film, kept everyone with at least two of them (`MIN_FILMS`), ranked them by total votes across those films, and kept the top 10,000 (`MAX_ACTORS`). Vote total is a recognizability proxy: it puts the names people are likely to search for at the top, and the website's search relies on that ordering to stay fast. Note that ranking by vote count skews the list toward English-language cinema.

Of the 906,740 people with any rated credit, 295,812 have two or more. Sample to the top 10,000.

## Reproduction

```bash
python3 collect.py       # popular.csv + random.csv
python3 build_actors.py  # actors.csv + docs/obscure-films/data/actors.json
python3 build_obscure.py # docs/obscure-films/data/obscure-films.json
```

Requires Python 3.9+ and no third-party packages. `collect.py` and `build_obscure.py` download ~235 MB of gzipped TSV from `datasets.imdb.com` at runtime; `build_actors.py` needs `title.principals` and `name.basics` on top of that, ~1.3 GB in all. Set `IMDB_CACHE_DIR` to a directory of already-downloaded `.tsv.gz` files to reuse them across runs:

```bash
mkdir -p /tmp/imdb && cd /tmp/imdb
for f in title.basics title.ratings title.principals name.basics; do curl -O "https://datasets.imdbws.com/$f.tsv.gz"; done
IMDB_CACHE_DIR=/tmp/imdb python3 build_actors.py
```

## License

IMDb data is provided for personal and non-commercial use under [IMDb's terms](https://developer.imdb.com/non-commercial-datasets/).
