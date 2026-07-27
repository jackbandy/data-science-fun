# Cook County Home Sales 2025

CSV of residential property sales recorded in Cook County, Illinois during calendar year 2025, prepared from public Cook County Assessor data. For educational purposes only.

The file is **de-identified**: the parcel number, street address, document number, and the names of the buyer and seller are excluded. See [Privacy](#privacy) below.

## Files

- `cook-county-home-sales-2025.csv`: 53,296 sales, one row per parcel sold. 25 columns, about 10 MB.

  Sale and property:
  - `sale_date`: date of sale (`YYYY-MM-DD`), ranging from 2025-01-01 to 2025-12-31
  - `sale_price`: sale price in dollars — **read the note on multi-parcel sales below**
  - `class`: Assessor property class code — 15 distinct values, e.g. `203`, `211`, `299`. See [Property class codes](#property-class-codes)
  - `class_description`: text description of the class (e.g. `One story residence, any age, 1,000 to 1,800 sq. ft.`)
  - `property_group`: `Single-Family` (26,983), `Condominium` (21,401), or `Multi-Family` (4,912)

  Location:
  - `city`: mailing city name of the property (e.g. `CHICAGO`, `EVANSTON`)
  - `zip_code`: 5-digit ZIP code
  - `township_name`: Cook County township (e.g. `Jefferson`, `Evanston`)
  - `municipality`: municipality name (e.g. `CITY OF CHICAGO`)
  - `chicago_community_area`: one of Chicago's 77 community areas; empty for the roughly half of sales outside the city
  - `latitude`, `longitude`: parcel coordinates (WGS84), **rounded to 3 decimal places** (about 110 m)

  Structure — empty for condominiums, which are described in a separate county dataset not used here:
  - `year_built`: year the building was constructed
  - `building_sqft`: building square footage
  - `land_sqft`: land square footage
  - `bedrooms`, `rooms`, `full_baths`, `half_baths`: room counts

  Transaction detail:
  - `deed_type`: e.g. `Warranty`, `Trustee`, `Quit Claim`
  - `is_multisale`: `TRUE` if the sale covered more than one parcel
  - `num_parcels_sale`: number of parcels included in the transaction
  - `filter_same_sale_within_365`, `filter_less_than_10k`, `filter_deed_type`: the Assessor's own outlier flags, marking sales it excludes from its valuation modeling

  There is no id column; see [Privacy](#privacy).

- `collect_cook_county_sales.py`: fetches and writes the CSV from the county's open data API. Adjust `SALE_DATE_START` / `SALE_DATE_END` to build a different window.

## Things to know

**Multi-parcel sales inflate prices.** 9,732 rows (18.3%) are part of a transaction covering several parcels, and each of those rows repeats the price of the *entire* transaction rather than the value of that one unit. The largest example is a single sale of 327 parcels for $56,750,000, which appears as 321 condo rows each showing $56,750,000. Taking a naive average or median over the raw file will be skewed by these.

Filter with `is_multisale == FALSE` (or `num_parcels_sale == 1`) for per-home prices. Doing so moves the median from $347,000 to $333,000.

**Duplicate rows are real sales, not errors.** With the parcel number removed, 4,441 rows are byte-identical to another row — mostly individual units from the bulk sales described above, which share a date, price, class and geography. `drop_duplicates()` would silently discard all 4,441, taking the file from 53,296 rows to 48,855. Deduplicate only if you actually intend to collapse those units.

**Structural characteristics are missing for condos.** The `year_built` through `half_baths` columns are populated for about 59% of rows — essentially all single- and multi-family sales, and no condominiums. This is a property of the source data.

**The Assessor's filter flags are not a quality score.** They mark sales the county excludes from its valuation models (rapid resales, sales under $10,000, unusual deed types). 193 rows are flagged as under $10,000. You may want to drop them for some analyses.

**Only dwellings are included.** Sales in other 200-level classes — vacant residential land, garages, farm buildings, home improvements — are excluded, as are all commercial and industrial classes.

## Property class codes

* The Assessor assigns every parcel a three-digit class.
* The first digit is the major class — `1` vacant land, `2` residential, `3` and `5` commercial and industrial, and so on — so every row in this file starts with `2`.
* The remaining digits distinguish building type, and for houses they also encode size and age bands.

All 15 classes present in the file:

| Class | Group | Sales | Median price | Description |
|---|---|--:|--:|---|
| `299` | Condominium | 21,401 | $270,000 | Condominium |
| `203` | Single-Family | 9,640 | $306,000 | One story residence, any age, 1,000 to 1,800 sq. ft. |
| `211` | Multi-Family | 4,574 | $445,000 | Apartment building with 2 to 6 units, any age |
| `202` | Single-Family | 3,280 | $230,000 | One story residence, any age, up to 999 sq. ft. |
| `234` | Single-Family | 2,552 | $349,000 | Split level residence, with a lower level below grade, all ages, all sizes |
| `278` | Single-Family | 2,483 | $692,500 | Two or more story residence, up to 62 years, 2,001 to 3,800 sq. ft. |
| `205` | Single-Family | 2,446 | $395,000 | Two or more story residence, over 62 years, up to 2,200 sq. ft. |
| `295` | Single-Family | 2,175 | $385,000 | Individually owned row houses or townhouses, up to 62 years |
| `204` | Single-Family | 1,499 | $516,325 | One story residence, any age, 1,801 sq. ft. and over |
| `206` | Single-Family | 1,146 | $962,180 | Two or more story residence, over 62 years, 2,201 to 4,999 sq. ft. |
| `207` | Single-Family | 626 | $415,000 | Two or more story residence, up to 62 years, up to 2,000 sq. ft. |
| `210` | Single-Family | 605 | $250,000 | Old style townhouse, over 62 years |
| `212` | Multi-Family | 338 | $522,500 | Two to six mixed-use apartments, any age, up to 20,000 sq. ft. |
| `208` | Single-Family | 330 | $1,355,000 | Two or more story residence, up to 62 years, 3,801 to 4,999 sq. ft. |
| `209` | Single-Family | 201 | $2,400,000 | Two or more story residence, any age, 5,000 sq. ft. and over |

Reading a code: `278` is a two-or-more-story house, no more than 62 years old, between 2,001 and 3,800 sq. ft. Its older counterpart at a similar size is `206`. The one-story sequence `202` → `203` → `204` is a size ladder — under 999, 1,000–1,800, then 1,801 and up

Three things follow from this that matter when using the column:

**`class` is not independent of `building_sqft` and `year_built`.** It is largely derived from them, so a model using all three is feeding on the same information twice. 

**The bands are approximate.** A class is assigned at assessment time and is not always refreshed after an addition or renovation

**`299` is a catch-all.** It covers 40% of the file in a single undifferentiated code, with no size or age information and no structural columns. Any analysis that groups by class is really comparing twelve fairly specific house types against one very large, very heterogeneous condo bucket.

## Privacy

Cook County publishes this data in fully identified form, including buyer and seller names. This file deliberately does not, since it is redistributed. It therefore omits the following:

- `pin` (Parcel Index Number) and street address — either one identifies the specific home
- `doc_no` — the Recorder of Deeds document number, which resolves to a scanned deed carrying both parties' names
- `seller_name` and `buyer_name`

There is also no id column. Every stable unique key available upstream is also a lookup key into the identified source records, such that one API call turns the county's `row_id` back into the PIN, document number, and both parties' names.

Use the dataframe row index if you need to refer to a row.

`collect_cook_county_sales.py` never requests these fields, so they are not downloaded at any point.

Coordinates are rounded to 3 decimals so a row locates a neighborhood rather than a specific house.

Notably, these privacy measures still do not make for a full anonymization. Any row with an unusual combination of price, date, and geography (e.g. a very high-value sale in a low-volume township) could still be narrowed down by someone cross-referencing the county's public records, which remain fully identified.

## Sources

All source data is published by the Cook County Assessor's Office through the Cook County Open Data portal:

- **Assessor - Parcel Sales** (sale records): https://datacatalog.cookcountyil.gov/Property-Taxation/Assessor-Parcel-Sales/wvhk-k5uv
- **Assessor - Parcel Addresses** (city, ZIP): https://datacatalog.cookcountyil.gov/Property-Taxation/Assessor-Parcel-Addresses/3723-97qp
- **Assessor - Parcel Universe** (township, municipality, community area, coordinates): https://datacatalog.cookcountyil.gov/Property-Taxation/Assessor-Parcel-Universe/nj4t-kc8j
- **Assessor - Single and Multi-Family Improvement Characteristics** (structure): https://datacatalog.cookcountyil.gov/Property-Taxation/Assessor-Single-and-Multi-Family-Improvement-Chara/x54s-btds

Property class descriptions come from the Assessor's published class dictionary: https://github.com/ccao-data/data-architecture (`dbt/seeds/ccao/ccao.class_dict.csv`)

Auxiliary data is joined on the 2025 tax year.

## Reproduction

```bash
python3 collect_cook_county_sales.py
```

Requires Python 3.9+ and `requests`. Downloads from the Cook County Open Data API at runtime; a full run takes roughly 20–30 minutes, since the joined datasets are fetched in batches of 400 parcels.

Re-running rebuilds the CSV from live county data, so the output will differ from the committed file wherever records have been added or corrected since July 2026.

## Disclaimers

- For educational purposes only.
- Accuracy, completeness, etc. not guaranteed.
- The CSV is a derived file prepared from the sources above, and it is not an official county product.
- File was created in July 2026 and may be incomplete, outdated, transformed, filtered, or inconsistent with current official records by the time you use it.
	- Sales data is sometimes revised as records are corrected.
- The CSV file should not be treated as a complete or official record of property transactions, and should not be used for valuation, lending, or legal purposes.
- Usually best to avoid reusing or redistributing, but if you do, please review upstream terms, licensing, and source documentation.
- Coordinates are rounded and are approximate by design.
