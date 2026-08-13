"""Build the chicago-maps dataset from public sources.

NOTICE: This file was substantially written by an LLM coding agent.

Run from this directory:  python3 fetch_chicago_maps.py

Sources
-------
* Chicago Data Portal (City of Chicago), Socrata:
    qqq8-j68g  Boundaries - City
    p293-wvbd  Boundaries - Wards (2023-)
    k5pk-wpt9  ACS 5 Year Data by Ward - Most Recent Year
* U.S. Census Bureau TIGERweb, Hydro/MapServer layer 1 (Areal Hydrography).

Everything is written as plain GeoJSON / CSV in EPSG:4326 so the slides can read
it with the standard library alone (no geopandas / shapely / fiona).
"""

import csv
import json
import urllib.parse
import urllib.request

HERE = __file__.rsplit("/", 1)[0]
UA = {"User-Agent": "cs418-datasets/1.0 (course materials)"}

# Bounding box that comfortably contains the city of Chicago.
BBOX = (-88.00, 41.60, -87.45, 42.10)


def get(url, params=None):
    if params:
        url = url + "?" + urllib.parse.urlencode(params)
    req = urllib.request.Request(url, headers=UA)
    with urllib.request.urlopen(req, timeout=180) as r:
        return json.load(r)


def round_coords(obj, nd=5):
    """Round every coordinate in a GeoJSON geometry to `nd` decimals (~1 m)."""
    if isinstance(obj, list):
        if obj and isinstance(obj[0], (int, float)):
            return [round(v, nd) for v in obj]
        return [round_coords(v, nd) for v in obj]
    return obj


def clean(features, keep):
    out = []
    for f in features:
        props = {k: f["properties"].get(k) for k in keep}
        out.append({
            "type": "Feature",
            "properties": props,
            "geometry": {
                "type": f["geometry"]["type"],
                "coordinates": round_coords(f["geometry"]["coordinates"]),
            },
        })
    return out


def write_geojson(name, features):
    path = f"{HERE}/{name}"
    with open(path, "w") as fh:
        json.dump({"type": "FeatureCollection", "features": features}, fh)
    print(f"wrote {name}: {len(features)} features")


# --------------------------------------------------------------------------
# 1. City boundary and ward boundaries (Chicago Data Portal)
# --------------------------------------------------------------------------

def socrata_geojson(dataset_id):
    return get(f"https://data.cityofchicago.org/api/geospatial/{dataset_id}",
               {"method": "export", "format": "GeoJSON"})


city = socrata_geojson("qqq8-j68g")
write_geojson("chicago-city.geojson", clean(city["features"], []))

wards = socrata_geojson("p293-wvbd")
ward_feats = clean(wards["features"], ["ward"])
ward_feats.sort(key=lambda f: int(f["properties"]["ward"]))
write_geojson("chicago-wards.geojson", ward_feats)

# --------------------------------------------------------------------------
# 2. Water (Census TIGERweb areal hydrography, Chicago bbox)
# --------------------------------------------------------------------------

hydro = get(
    "https://tigerweb.geo.census.gov/arcgis/rest/services/TIGERweb/Hydro/MapServer/1/query",
    {
        "geometry": ",".join(str(v) for v in BBOX),
        "geometryType": "esriGeometryEnvelope",
        "inSR": 4326,
        "outSR": 4326,
        "spatialRel": "esriSpatialRelIntersects",
        "outFields": "NAME,MTFCC,AREAWATER",
        "returnGeometry": "true",
        "f": "geojson",
    },
)

# Drop the many tiny retention ponds; keep anything at least 5 hectares so the
# lake, the river, the canals and the harbors survive.
big = [f for f in hydro["features"] if int(f["properties"]["AREAWATER"] or 0) >= 50_000]
write_geojson("chicago-water.geojson", clean(big, ["NAME", "MTFCC", "AREAWATER"]))

# --------------------------------------------------------------------------
# 3. ACS household-income brackets by ward, plus an interpolated median
# --------------------------------------------------------------------------

BRACKETS = [
    ("under_25_000", 0, 25_000),
    ("_25_000_to_49_999", 25_000, 50_000),
    ("_50_000_to_74_999", 50_000, 75_000),
    ("_75_000_to_125_000", 75_000, 125_000),
    ("_125_000", 125_000, 250_000),  # open-ended; capped for interpolation
]

acs = get("https://data.cityofchicago.org/resource/k5pk-wpt9.json", {"$limit": 200})


def grouped_median(counts):
    """Linear interpolation inside the bracket that holds the middle household."""
    total = sum(counts)
    half = total / 2
    running = 0
    for n, (_, lo, hi) in zip(counts, BRACKETS):
        if running + n >= half:
            return round(lo + (half - running) / n * (hi - lo))
        running += n
    return None


rows = []
for r in acs:
    counts = [int(float(r[k])) for k, _, _ in BRACKETS]
    rows.append({
        "ward": int(r["ward"]),
        "acs_year": r["acs_year"],
        "households_under_25k": counts[0],
        "households_25k_to_50k": counts[1],
        "households_50k_to_75k": counts[2],
        "households_75k_to_125k": counts[3],
        "households_125k_plus": counts[4],
        "households_total": sum(counts),
        "pct_households_125k_plus": round(100 * counts[4] / sum(counts), 1),
        "median_household_income_est": grouped_median(counts),
    })
rows.sort(key=lambda r: r["ward"])

with open(f"{HERE}/chicago-ward-income.csv", "w", newline="") as fh:
    w = csv.DictWriter(fh, fieldnames=list(rows[0]))
    w.writeheader()
    w.writerows(rows)
print(f"wrote chicago-ward-income.csv: {len(rows)} wards")
