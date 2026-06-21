# World Inequality Database: Income Shares, 9 Countries

Pre-tax national income share time series for top 1%, top 10%, and bottom 50%, for 9 countries, drawn from the World Inequality Database (WID.world). For educational purposes only.

## Study

The World Inequality Database (wid.world) compiles long-run distributional national accounts — combining tax records, household surveys, and national accounts — to estimate how income and wealth are distributed across the population. It is the empirical foundation of Thomas Piketty's *Capital in the Twenty-First Century* (2013) and the broader research program on economic inequality.

The canonical founding paper is Piketty & Saez (2003), which reconstructed top income shares in the United States back to 1913 using IRS data. The WID has since extended this methodology to dozens of countries.

## Files

- `wid-income-shares.csv` — 2,697 rows: annual top 1%, top 10%, and bottom 50% income shares for 9 countries
- `collect.py` — script that produced the CSV via the WID REST API

## Columns

- `country` — ISO 2-letter country code
- `country_name` — full country name
- `year` — year
- `variable` — one of `top1_share`, `top10_share`, `bottom50_share`
- `value` — income share as a fraction (e.g., 0.20 = 20% of income)
- `pop_code` — WID population-unit code used (see note below)

## Countries

US (United States), FR (France), DE (Germany), GB (United Kingdom), SE (Sweden), CN (China), IN (India), BR (Brazil), ZA (South Africa)

## A note on the `pop_code` column

WID stores income shares under different population-unit conventions per country, reflecting differences in the underlying data sources:

- `999_i` — all ages, equal-split individuals (US)
- `999_j` — all ages, fiscal/joint units (Germany, UK, Sweden, China, India, Brazil, South Africa)
- `992_i` — adults only, equal-split individuals (France)

Cross-country comparisons are valid for broad trends but should account for these methodological differences. See the WID Codes Dictionary for details: https://wid.world/codes-dictionary/

## Reproduction

```bash
python3 collect.py
```

Requires Python 3.9+ and no third-party packages. Downloads from the WID REST API at runtime.

## Sources

- World Inequality Database: https://wid.world/data/
- Piketty & Saez (2003): https://doi.org/10.1162/00335530360535135
- wid-r-tool (API source): https://github.com/world-inequality-database/wid-r-tool
- Data collected June 2026

## Disclaimers

- For educational purposes only.
- Accuracy, completeness, etc. not guaranteed.
- File was downloaded in June 2026 and may be outdated or inconsistent with current upstream records.
- Should not be treated as a complete or official record.
- Best to avoid reusing or redistributing; if you do, review upstream terms and licensing.
