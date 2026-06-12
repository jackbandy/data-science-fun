# movies-from-imdb

Two movie datasets drawn from [IMDb's public data files](https://datasets.imdbws.com/), collected June 2026.

## Files

| File | Description |
|------|-------------|
| `popular.csv` | Top 1000 movies ranked by number of IMDb votes |
| `random.csv` | 1000 movies sampled at random from the remaining rated movies (seed 42) |
| `collect.py` | Script that produced both files |

## Columns

| Column | Source | Notes |
|--------|--------|-------|
| `primaryTitle` | title.basics | Release title |
| `startYear` | title.basics | Release year |
| `runtimeMinutes` | title.basics | Runtime; `\N` if unknown |
| `genres` | title.basics | Comma-separated; `\N` if unknown |
| `averageRating` | title.ratings | Weighted mean (1–10) |
| `numVotes` | title.ratings | Total votes cast |

## Methodology

**Popular set** — sorted all rated movies by `numVotes` descending, took the top 1000. Vote count is a better popularity proxy than rating alone because it reflects actual audience reach.

**Random set** — after removing the top 1000, drew a random sample of 1000 from the remainder (Python `random.sample`, seed 42 for reproducibility). This gives a rough cross-section of the long tail.

## Reproduction

```bash
python3 collect.py
```

Requires Python 3.9+ and no third-party packages. Downloads ~100 MB of gzipped TSV from `datasets.imdb.com` at runtime; the CSVs are the only output kept.

## License

IMDb data is provided for personal and non-commercial use under [IMDb's terms](https://developer.imdb.com/non-commercial-datasets/).
