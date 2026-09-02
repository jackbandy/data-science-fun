
# Obscure Films

Inspired by [obscuretube.com](https://obscuretube.com)

## How it works

- Data comes from IMDb's public TSV files (`title.basics` + `title.ratings`)
	- downloaded and distilled by `datasets/movies-from-imdb/build_obscure.py`
- Every rated film (≈350,000) is ranked by vote count, most-voted first, so rank 0 is the most popular
- The most-voted 0.1% and the least-voted 0.1% are excluded, so the visible range is the 0.1% mark to the 99.9% mark
- That range is split into 10 percentile buckets (`0.1–10`, `10–20`, …, `90–99.9`) — the 10 bars of the chart
- Each bar's height is the **total votes** cast for the films in that bucket; the y-axis is log-scaled
- A stratified sampling pool of ~5,000 films (500 per bucket) is shipped to the page;
	- each film carries its **exact percentile** so any span filters correctly
- Two draggable bars set the selected percentile span; dragging snaps to 1% steps (integer percents 1–99)
- Double-click a bars to type an exact value, validated to keep the bounds ordered and within the 0.1–99.9 range
- The eligible-film count updates live as the bars move.
- The **Sample films** button picks 8 distinct random films from the selected span.
- Each gallery card shows the title, year, genres, ★ rating, vote count, the percentile the film sits at, and a link to its IMDb page.
- Everything the reader sees is phrased the standard way: **more votes than N% of other films**. The x-axis runs `99.9%` on the left down to `0.1%` on the right, the gate tabs and the type-in prompt read the same way, and so do the tooltips and the cards. Internally the gates still work in popularity-percentile space (`0` = most-voted), and `moreThan(p)` is the single place the two directions are reconciled.
- The "films in range" readout counts **every rated film** in the span, prorated from the band counts — not the ~5,000-film sampling pool, which is a stratified subsample and would understate the population a hundredfold. The **Sample films** button, though, is enabled from the pool, since that is what can actually be drawn.

## Filter by actor

- The **Filter by actor** checkbox under the chart reveals a search box over the 10,000 most-voted IMDb performers.
- Matching folds case and strips diacritics, so `timothee chalamet` finds *Timothée Chalamet*. The list is stored in descending vote order, so the first hits are the recognizable ones and the search loop can stop at eight rather than scanning the whole list.
- Picking an actor swaps the sampling universe: instead of the stratified pool it draws from **every** rated feature that actor is credited on. The pool holds only ~50 films per band and would almost never contain a given actor, so this has to be a separate dataset.
- That dataset is `docs/obscure-films/data/actors.json` — 6.4 MB, 2.9 MB over the wire — and it is **fetched lazily**: nothing downloads until the checkbox is first checked, and once loaded it serves every search and every pick with no further requests.
- Famous actors cluster at the popular end, so an obscure span can hold none of a given actor's films; the page says so and disables **Sample films** rather than showing a stale gallery.


## Rebuilding

```bash
cd datasets/movies-from-imdb
python3 build_obscure.py   # the chart + sampling pool (~235 MB of downloads)
python3 build_actors.py    # the actor filter (~1.3 GB of downloads)
```

`MAX_ACTORS` in `build_actors.py` sets both the breadth of the search box and the weight of the download; `MIN_FILMS` sets how deep the tail goes.

Run both against the same IMDb snapshot — the actor films' percentiles have to be on the same scale as the gates that select them. See `datasets/movies-from-imdb/README.md` for the `IMDB_CACHE_DIR` trick that makes a re-run cheap. IMDb data is for personal, non-commercial use.