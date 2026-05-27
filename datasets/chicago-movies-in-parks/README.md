# Chicago Movies in the Parks

scripted CSV downloads of City of Chicago datasets whose titles include "Movies in the Parks", prepared from public Chicago data. For educational purposes only.

## Files

- `download_movies_in_the_parks.py`: Downloads matching datasets from the Chicago Data Portal and saves them as CSV files.

## Columns

To reduce distribution of contact info, before saving csvs, the script removes fields that contain contact information:
- `contactname`
- `contactemail`
- any column with `phone` in the name
- any column with `telephone` in the name
- any column with `email` in the name


## Sources

- City of Chicago Data Portal catalog API: https://api.us.socrata.com/api/catalog/v1
- City of Chicago Data Portal: https://data.cityofchicago.org/

The script searches the Chicago catalog for datasets whose titles include "Movies in the Parks" and downloads the matching CSV exports from the public data portal.

## Disclaimers

- for educational purposes only.
- accuracy, completeness, etc. not guaranteed
- file was created in May 2026, and may be incomplete, outdated, transformed, filtered, or inconsistent with current official records by the time you use it
- files are filtered and should not be treated as complete or official records.
- best to avoid reusing or redistributing, but if you do, please review upstream terms, licensing, and source documentation
- again, this is only for educational purposes
