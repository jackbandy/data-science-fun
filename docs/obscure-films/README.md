
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

- Rebuild the data with `cd datasets/movies-from-imdb && python3 build_obscure.py` (downloads ~100 MB). IMDb data is for personal, non-commercial use.