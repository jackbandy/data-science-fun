# CTA Ridership

derived CSV of CTA annual ridership totals, prepared from public Chicago Transit Authority data. For educational purposes only.

## Files

- `Annual_Boarding_Totals_20260527.csv`: Annual boarding totals with the following columns:
  - `year`
  - `bus`
  - `paratransit`
  - `rail`
  - `total`

- `Station_Entries_-_Daily_Totals_20260527.csv`: Daily station entry totals from the CTA ridership dataset. This file is about 60 MB (an exception to the repository's preferred file-size guideline).

- `Station_Entries_UIC-Halsted_2025.csv`: only the UIC-Halsted (Blue Line, `station_id` 40350) rows for 2025 from the daily totals file above: 365 rows, about 17 KB, otherwise unchanged. The Python Yard (`docs/yard/`) demo reads this copy from GitHub by raw URL, because the full file is too big to download in a browser. `rides` keeps the source's thousands separators (`"1,004"`), so it reads in as text. Regenerate it with:
  ```
  { head -1 Station_Entries_-_Daily_Totals_20260527.csv; grep '^"40350",.*/2025",' Station_Entries_-_Daily_Totals_20260527.csv; } > Station_Entries_UIC-Halsted_2025.csv
  ```

## Sources

- City of Chicago Data Portal, annual boarding totals: https://data.cityofchicago.org/Transportation/CTA-Ridership-Annual-Boarding-Totals/w8km-9pzd
- City of Chicago Data Portal, station entries daily totals: https://data.cityofchicago.org/Transportation/CTA-Ridership-L-Station-Entries-Daily-Totals/5neh-572f

The linked data portal records are Chicago Transit Authority datasets published through the City of Chicago Data Portal. These CSVs are separate derived files prepared from local source data associated with the CTA ridership datasets and related public materials.

## Disclaimers

- for educational purposes only.
- accuracy, completeness, etc. not guaranteed
- file was created in May 2026, and may be incomplete, outdated, transformed, filtered, or inconsistent with current official records by the time you use it
- file should not be treated as a complete or official record.
- best to avoid reusing or redistributing, but if you do, please review upstream terms, licensing, and source documentation
- again, this is only for educational purposes
