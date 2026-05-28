# U.S. National Parks Info

CSV of the 63 U.S. national parks, prepared for educational use.

## Files

- `us-national-parks.csv`: park code, names, state/territory, NPS region, unit type, established date, source edit date, and approximate centroid coordinates.
- `retrieve_national_parks.py`: downloads the source data and builds the CSV.

## Sources

- NPS ArcGIS boundary layer: https://services6.arcgis.com/ZncoPpp4shVCg1II/arcgis/rest/services/Administrative_Boundaries_of_National_Park_System_Units_gdb/FeatureServer
- Establishment dates: https://en.wikipedia.org/wiki/List_of_national_parks_of_the_United_States

The script selects `UNIT_TYPE = 'National Parks'` from the NPS layer and also includes New River Gorge (`NERI`), which the layer stores as `National Preserves`.

For educational purposes only. Accuracy, completeness, etc. not guaranteed (e.g. centroid coordinates are approximate).
