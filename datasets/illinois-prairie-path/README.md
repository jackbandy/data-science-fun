# Illinois Prairie Path

Trail segment and mile post data for the Illinois Prairie Path and the broader DuPage County bikeway network, prepared for educational use.

## Files

- `dupage-bikeways-trails.csv`: 2,032 trail segments covering all named bikeways and trails in DuPage County, including 87 segments of the Illinois Prairie Path. One row per segment, with the following columns:
  - `object_id`: unique segment identifier
  - `feat_id`: feature ID
  - `bike_id`: bikeway ID
  - `street_name`: street or road name the trail follows
  - `facility_name`: name of the individual trail facility
  - `from_ref`: starting reference point
  - `to_ref`: ending reference point
  - `trail_system`: named trail system (e.g. `Illinois Prairie Path`, `Great Western Trail`)
  - `status`: `Existing` or `Planned`
  - `class`: `Local` or `Regional`
  - `network_type`: `Path` or `Bike Route`
  - `facility_type`: e.g. `Sidepath`, `Bike Lane`, `Shared Use Path`
  - `surface`: `Paved`, `Limestone`, or `Unknown`
  - `jurisdiction`: managing agency or municipality
  - `township`: DuPage County township
  - `agreement`: intergovernmental agreement reference, if any
  - `width_ft`: trail width in feet
  - `length_ft`: segment length in feet (from source geometry)
  - `centroid_longitude`: approximate longitude of segment centroid (WGS84)
  - `centroid_latitude`: approximate latitude of segment centroid (WGS84)

- `trail-mile-posts.csv`: 50 mile marker points along the Illinois Prairie Path branches and the adjacent Great Western Trail, with the following columns:
  - `fid`: feature ID
  - `trail`: trail branch name (e.g. `Prairie Path - Main Stem`, `Prairie Path - Elgin Branch`)
  - `mile`: mile marker number
  - `longitude`: marker longitude (WGS84)
  - `latitude`: marker latitude (WGS84)

- `retrieve_data.py`: fetches and writes both CSVs from the source ArcGIS REST services.

## Sources

- **DuPage County Bikeways and Trails** (trail segments): DuPage County GIS Division, accessed via the DuPage County Open Data portal. Feature service: `https://gis.dupageco.org/arcgis/rest/services/DuDOT/Bikeways_and_Trails/MapServer/0`
  - Open data portal listing: https://gisdata-dupage.opendata.arcgis.com/datasets/DuPage::bikeways-and-trails/explore

- **Trail Mile Posts** (mile markers): DuPage County GIS, hosted on ArcGIS Online. Feature service: `https://services.arcgis.com/neJvtQ4PXvnQ86MJ/arcgis/rest/services/Mile_Posts/FeatureServer/0`
  - Open data portal listing: https://gisdata-dupage.opendata.arcgis.com/datasets/ef2b36b8b3424eee8cb7f56e96713be7_0/data

Both datasets are published by DuPage County GIS and are freely available for public use through the DuPage County Open Data portal.

## Disclaimers

- For educational purposes only.
- Accuracy, completeness, etc. not guaranteed.
- Files were created in June 2026 and may be incomplete, outdated, transformed, filtered, or inconsistent with current official records by the time you use them.
- Files should not be treated as complete or official records.
- Best to avoid reusing or redistributing, but if you do, please review upstream terms, licensing, and source documentation.
- Centroid coordinates are computed from polyline geometry and are approximate.
