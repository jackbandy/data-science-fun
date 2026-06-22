# USA Migration Data: IRS Statistics of Income (SOI)

State-level migration flows for the United States, derived from IRS individual income tax return address changes. Covers 12 consecutive year pairs from 2011–2023. For educational purposes only.

## Background

Each year, the IRS Statistics of Income (SOI) division compares the address on a taxpayer's return from one year to the next. When the state changes, that counts as a migration event. The result is a large dataset of interstate and international migration flows, measured in number of tax returns (households), number of individuals, and aggregate adjusted gross income (AGI).

The data captures both **immigration** (inflows from foreign addresses) and an **emigration proxy** (outflows to foreign addresses) — the closest available federal approximation, since the US has no formal exit-tracking system.

This is not a complete count of all migration: it only covers tax filers, excluding undocumented immigrants and non-filers.

## Files

- `state-inflow.csv` — 34,155 rows: for each state, who moved in and where they came from
- `state-outflow.csv` — 34,154 rows: for each state, who moved out and where they went
- `collect.py` — script that produced both CSVs from the IRS public download portal

## Columns

Both files share the same structure, with `y1` referring to the earlier year (origin) and `y2` to the later year (destination).

| Column | Description |
|---|---|
| `y1_year` | Earlier tax filing year |
| `y2_year` | Later tax filing year |
| `y1_statefips` / `y2_statefips` | FIPS code for origin / destination state (see special codes below) |
| `y1_state` / `y2_state` | State abbreviation |
| `y1_state_name` / `y2_state_name` | State name or row description |
| `n1` | Number of tax returns (proxy for households) |
| `n2` | Number of individuals |
| `AGI` | Aggregate adjusted gross income (in thousands of dollars) |

**In `state-inflow.csv`**, the focal (destination) state is `y2_statefips`, and each row shows flows arriving from `y1_statefips`.

**In `state-outflow.csv`**, the focal (origin) state is `y1_statefips`, and each row shows flows leaving to `y2_statefips`.

### Special FIPS codes

| Code | Meaning |
|---|---|
| `96` | Total migration — US and foreign combined |
| `97` | Total US migration / same-state migration |
| `98` | Foreign migration — **immigration** in inflow files, **emigration proxy** in outflow files |
| same as focal state | Non-migrants (filed from the same state both years) |

## Year Coverage

| Years | Notes |
|---|---|
| 2011–2012 through 2022–2023 | Modern consistent format, downloaded here |
| 1990–1991 through 2010–2011 | Available from IRS in an older format (ZIP archives); not included |

## County-Level Data

The IRS also publishes **county-to-county** migration files using the same structure. These are much larger (~4.5 MB per direction per year) and are not committed to this repository to keep it lean. To download them, modify `collect.py` to fetch `countyinflow{tag}.csv` and `countyoutflow{tag}.csv` from the same base URL.

## Reproduction

```bash
python3 collect.py
```

Requires Python 3.9+ and no third-party packages. Downloads ~3 MB from the IRS public server.

## Sources

- IRS SOI Migration Data: https://www.irs.gov/statistics/soi-tax-stats-migration-data
- IRS SOI County-to-County files: https://www.irs.gov/statistics/soi-tax-stats-county-to-county-migration-data-files
- IRS migration data users guide (2022–2023): https://www.irs.gov/pub/irs-soi/2223inpublicmigdoc.pdf
- Data collected June 2026

## Disclaimers

- For educational purposes only.
- Accuracy, completeness, etc. not guaranteed.
- Only covers tax filers; excludes undocumented immigrants, non-filers, and low-income non-filers.
- "Emigration" (foreign outflow) is a proxy based on filers who switched to a foreign address — not a direct count.
- Files downloaded June 2026; may be outdated or inconsistent with current upstream records.
- Should not be treated as a complete or official record.
- Best to avoid reusing or redistributing; if you do, review IRS terms and source documentation.
