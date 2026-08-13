# Chicago Maps

Boundary, water, and ward-income layers for Chicago, stored as plain GeoJSON and
CSV in EPSG:4326 (WGS 84 longitude/latitude) so they can be read with nothing but
Python's standard library.

### Files

- `chicago-city.geojson` — the City of Chicago boundary, one `MultiPolygon`
  feature. No attributes.
- `chicago-wards.geojson` — the 50 city wards in effect since 2023, one feature
  each with a `ward` property (`"1"`–`"50"`).
- `chicago-water.geojson` — areal hydrography in a bounding box around the city:
  Lake Michigan, the Chicago River and its branches, the North Shore Channel, the
  Cal-Sag Channel, the Calumet River, and the harbors and lagoons. Properties are
  `NAME`, `MTFCC` (Census feature class), and `AREAWATER` (square meters).
  Features smaller than 5 hectares were dropped.
- `chicago-ward-income.csv` — one row per ward:
  `ward`, `acs_year`, five household-income bracket counts
  (`households_under_25k`, `households_25k_to_50k`, `households_50k_to_75k`,
  `households_75k_to_125k`, `households_125k_plus`), `households_total`,
  `pct_households_125k_plus`, and `median_household_income_est`.
- `fetch_chicago_maps.py` — the script that rebuilds all four files from source.

### A caveat about the income column

The city's published ACS-by-ward table reports **household income in five
brackets**, not a median. Wards are not a Census geography, so the Census Bureau
does not publish a median household or median family income for them, and no such
figure exists to download.

`median_household_income_est` is therefore *derived*: it is the standard grouped
median, found by linear interpolation inside whichever bracket contains the
middle household. The top bracket is open-ended (`$125,000+`) and is capped at
`$250,000` for the interpolation, which makes the estimate least trustworthy in
the highest-income wards. The bracket counts are included so you can check the
derivation or compute something else. Treat the column as a teaching-grade
estimate, not an official statistic.

### Sources

- City of Chicago, [Chicago Data Portal](https://data.cityofchicago.org/):
  - [Boundaries — City](https://data.cityofchicago.org/d/qqq8-j68g) (`qqq8-j68g`)
  - [Boundaries — Wards (2023-)](https://data.cityofchicago.org/d/p293-wvbd) (`p293-wvbd`)
  - [ACS 5 Year Data by Ward — Most Recent Year](https://data.cityofchicago.org/d/k5pk-wpt9) (`k5pk-wpt9`),
    the city's aggregation of U.S. Census Bureau American Community Survey
    5-year estimates to ward boundaries.
- U.S. Census Bureau, [TIGERweb](https://tigerweb.geo.census.gov/) —
  `TIGERweb/Hydro/MapServer` layer 1, Areal Hydrography. Public domain.

Coordinates are rounded to five decimal places (about one meter).
