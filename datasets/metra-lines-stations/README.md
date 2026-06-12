# Metra Lines and Stations

Derived CSV files of Metra line and station attributes, prepared from local shapefile source data. For educational purposes only.

## Files

- `metra_lines.csv`: Line-segment records extracted from `Metra_Lines/MetraLinesshp.dbf`, with geometry omitted.
- `metra_stations.csv`: Station records extracted from `Metra_Stations/MetraStations.dbf`, with geometry omitted.
- `extract_metra_data.py`: Script that reads the DBF attribute tables and writes the derived CSV files.

## Sources

- `Metra_Lines/`: Local shapefile source files for Metra line features.
- `Metra_Stations/`: Local shapefile source files for Metra station features.

The CSVs are derived from the local shapefile attribute tables. The extraction script drops `GEOMETRY_WKT` and keeps the remaining DBF attributes as plain CSV for classroom use.

## Disclaimers

- For educational purposes only.
- Accuracy, completeness, etc. not guaranteed.
- Files may be incomplete, outdated, transformed, filtered, or inconsistent with current official records by the time you use them.
- Files should not be treated as complete or official records.
- Review upstream terms, licensing, and source documentation before reusing or redistributing.
