# CTA Train Tracker

Two snapshots of the CTA Train Tracker arrival board at two Chicago 'L' stations, scraped from the public Train Tracker web pages. For educational purposes.

This is the dataset behind the Week 4 slides' scraping demo ([`docs/slides/week4.qmd`](../../docs/slides/week4.qmd)).

## Quickstart

```python
import polars as pl

runs = pl.concat([
    pl.read_csv("cta-arrivals-run1.csv", try_parse_dates=True),
    pl.read_csv("cta-arrivals-run2.csv", try_parse_dates=True),
])

# What each board was promising, per station
runs.group_by("station", "collected").agg(pl.len().alias("arrivals")).sort("collected")
```

## Files

- `scrape_train_tracker.py` — takes one snapshot of each station and writes a CSV. Source of both data files.
- `cta-arrivals-run1.csv` — 18 arrivals, 2026-09-15 20:35 (Chicago time).
- `cta-arrivals-run2.csv` — 16 arrivals, 20:47, about 11½ minutes later.

Same 10 columns in both, one row per predicted arrival:

| column | what it holds |
|---|---|
| `station` / `station_id` | `UIC-Halsted` / `40350`, `Washington/Wells` / `40730`. The id is the `MAP_ID` of [chicago-l-stations](../chicago-l-stations/), and the `sid` in the URL |
| `line` | `Blue`, `Brown`, `Orange`, `Pink` — from the page's colour class, not its text |
| `run` | CTA run number. Identifies one train; reused across days |
| `destination` | where it is signed for: `O'Hare`, `Kimball`, `54th/Cermak` |
| `direction` | the platform heading it was listed under (see below) |
| `collected` | when the page was requested. Shared by every row from one station in one run |
| `shown` / `minutes` | the countdown as displayed (`Due`, `9 min`), and as an integer (`Due` → `0`) |
| `expected` | `collected + minutes` — the moment the board was pointing at. The only derived column, and the one that makes the file useful, since "9 min" means something different at 20:35 than at 20:47 |

## A second run?

Ten run numbers appear in both files. Joining on `station` + `run` and differencing `expected` shows how far the CTA moved its own prediction in between: −1.52 to +2.48 minutes, averaging +0.28.

The drifts land on `.48` and `.52` rather than whole minutes. The board only shows whole minutes, but the scrapes are 11 min 29 s apart, so that offset rides into every difference. An inner join also keeps only ten rows — eight trains are in run 1 alone (they arrived, or fell off the board) and six only entered the window by run 2.

Either way this compares **a prediction to a later prediction**, not a prediction to an arrival. Getting to the second needs scrapes a minute apart, for weeks.

## Two stations, two page layouts

The same scraper handles two page shapes. **UIC-Halsted** is Blue Line only, one platform per direction, so its headings name a destination. **Washington/Wells** is a Loop station on four lines at once, where one platform carries several routes to several places, so its headings name the platform:

```
Service toward O'Hare              Service at Outer Loop platform
Service toward Forest Park         Service at Inner Loop platform
```

## Things to know

**These are predictions, not arrivals.** Every row is what the CTA expected at the moment of the scrape. Nothing here records a train actually showing up.

**Two runs is not a sample.** One Monday evening, twelve minutes apart. Nothing here supports a claim about rush hour, weekends, weather, or reliability.

**The slide version is simpler than the script.** The Week 4 deck scrapes UIC-Halsted only, so it strips `"Service toward "` off the heading and skips the non-platform guard — correct for one Blue Line station, wrong at Washington/Wells.

## Reproduction

```bash
python3 scrape_train_tracker.py --out my-run.csv   # --stations 40350 for one
```

Needs Python 3.9+, `requests`, `beautifulsoup4`; station ids come from the `MAP_ID` column of [chicago-l-stations](../chicago-l-stations/). Re-running gives different data every time — for a real time series, run it on a schedule and append. The script identifies itself in its `User-Agent` and pauses between requests (please keep it that way).

## Sources

- **CTA Train Tracker**, arrival estimates by station: https://www.transitchicago.com/traintracker/arrivaltimes/?sid=40350 and https://www.transitchicago.com/traintracker/arrivaltimes/?sid=40730
- Station ids and names: [chicago-l-stations](../chicago-l-stations/), from the Chicago Data Portal's [CTA List of 'L' Stops](https://data.cityofchicago.org/Transportation/CTA-List-of-L-Stops/8pix-ypme)

CTA also publishes an official **Train Tracker API** with an API key, which returns the same predictions as JSON and is the right thing to use for anything beyond a classroom demo: https://www.transitchicago.com/developers/traintracker/. The whole reason to scrape the HTML here is to practice scraping; when there is an API, use the API.

Route colours follow the [CTA Trademark Guidelines for Developers](https://www.transitchicago.com/developers/branding/). This dataset is not affiliated with, endorsed by, or sponsored by the Chicago Transit Authority.

## Disclaimers

- For educational purposes only.
- Accuracy, completeness, etc. not guaranteed.
- These are **predictions the CTA published at one moment**, not a record of when trains arrived. They should not be used to evaluate CTA performance.
- Two snapshots taken minutes apart on one evening. Not a sample of anything.
- The CSVs are derived files, parsed and reshaped from public web pages, and are not an official CTA product.
- Files were created in September 2026 and may be incomplete, outdated, transformed, filtered, or inconsistent with current official records by the time you use them.
- Usually best to avoid reusing or redistributing, but if you do, please review upstream terms, licensing, and source documentation.
