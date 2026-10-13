# /// script
# requires-python = ">=3.11"
# dependencies = ["numpy>=2,<3", "matplotlib>=3.8,<4"]
# ///
"""Build the classification-examples dataset: five two-feature, yes/no examples.

NOTICE: This file was substantially written by an LLM coding agent.

Run from anywhere:  uv run collect_classification_examples.py [name ...]

Each example is one CSV in this folder, written from a public source:

  penguins.csv                    Palmer Penguins (palmerpenguins R package, GitHub)
  spambase.csv                    UCI Spambase, with column names from spambase.names
  wdbc.csv                        UCI Breast Cancer Wisconsin (Diagnostic), named columns
  college-scorecard.csv           College Scorecard most-recent institution file, 8 columns
  cook-county-sales-density.csv   ../cook-county-home-sales-2025 sales with lot size, plus
                                  2020 census tract density (TIGERweb) and miles to the
                                  nearest 'L' stop (../chicago-l-stations)

numpy and matplotlib are only needed for the Cook County point-in-polygon step.
"""

import csv
import io
import json
import math
import re
import sys
import urllib.parse
import urllib.request
import zipfile
from pathlib import Path

HERE = Path(__file__).resolve().parent
DATASETS = HERE.parent
UA = {"User-Agent": "cs418-datasets/1.0 (course materials)"}

PENGUINS_URL = "https://raw.githubusercontent.com/allisonhorst/palmerpenguins/main/inst/extdata/penguins.csv"
SPAMBASE_URL = "https://archive.ics.uci.edu/static/public/94/spambase.zip"
WDBC_URL = "https://archive.ics.uci.edu/static/public/17/breast+cancer+wisconsin+diagnostic.zip"
# The release date is in the file name; check https://collegescorecard.ed.gov/data/ for a newer one.
SCORECARD_URL = "https://ed-public-download.scorecard.network/downloads/Most-Recent-Cohorts-Institution_06102026.zip"
TRACTS_URL = "https://tigerweb.geo.census.gov/arcgis/rest/services/TIGERweb/tigerWMS_Census2020/MapServer/6/query"

SQ_METERS_PER_SQ_MILE = 2_589_988.110336
EARTH_RADIUS_MILES = 3958.8


def fetch(url: str) -> bytes:
    with urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=300) as r:
        return r.read()


def write_csv(name: str, header: list[str], rows) -> None:
    out = HERE / name
    with out.open("w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(header)
        n = 0
        for row in rows:
            w.writerow(row)
            n += 1
    print(f"  wrote {out.name} ({n:,} rows)")


def penguins() -> None:
    (HERE / "penguins.csv").write_bytes(fetch(PENGUINS_URL))
    print("  wrote penguins.csv")


def spambase() -> None:
    z = zipfile.ZipFile(io.BytesIO(fetch(SPAMBASE_URL)))
    names_txt = z.read("spambase.names").decode("latin-1")
    # Attribute lines look like "word_freq_make:         continuous."
    header = re.findall(r"^(\S+):\s+continuous\.", names_txt, re.M) + ["spam"]
    rows = csv.reader(io.StringIO(z.read("spambase.data").decode("latin-1")))
    write_csv("spambase.csv", header, rows)


def wdbc() -> None:
    z = zipfile.ZipFile(io.BytesIO(fetch(WDBC_URL)))
    # wdbc.names: ten features, each as mean, standard error, and "worst" (fields 3-12, 13-22, 23-32).
    features = ["radius", "texture", "perimeter", "area", "smoothness", "compactness",
                "concavity", "concave_points", "symmetry", "fractal_dimension"]
    header = ["id", "diagnosis"] + [f"{f}_{s}" for s in ("mean", "se", "worst") for f in features]
    rows = csv.reader(io.StringIO(z.read("wdbc.data").decode("utf-8")))
    write_csv("wdbc.csv", header, rows)


def college_scorecard() -> None:
    z = zipfile.ZipFile(io.BytesIO(fetch(SCORECARD_URL)))
    member = next(n for n in z.namelist() if n.endswith(".csv") and not n.startswith("__MACOSX"))
    keep = ["UNITID", "INSTNM", "STABBR", "CONTROL", "PREDDEG", "UGDS", "TUITIONFEE_IN", "ENDOWEND"]
    with z.open(member) as raw:
        reader = csv.DictReader(io.TextIOWrapper(raw, encoding="utf-8-sig"))
        rows = [[r[k] for k in keep] for r in reader]
    write_csv("college-scorecard.csv", keep, rows)


def tracts() -> list[dict]:
    """Cook County 2020 census tracts with population, land area, and polygons."""
    feats, offset = [], 0
    while True:
        query = urllib.parse.urlencode({
            "where": "STATE='17' AND COUNTY='031'", "outFields": "GEOID,POP100,HU100,AREALAND",
            "returnGeometry": "true", "outSR": "4326", "orderByFields": "GEOID",
            "resultOffset": offset, "resultRecordCount": 500, "f": "geojson",
        })
        page = json.loads(fetch(f"{TRACTS_URL}?{query}"))["features"]
        feats += page
        offset += len(page)
        if len(page) < 500:
            return feats


def l_stops() -> list[tuple[float, float]]:
    path = DATASETS / "chicago-l-stations" / "CTA_List_of_'L'_Stops_20260527.csv"
    with path.open(newline="", encoding="utf-8") as f:
        return [tuple(map(float, re.findall(r"-?\d+\.\d+", r["Location"]))) for r in csv.DictReader(f)]


def miles_to_nearest(lat: float, lon: float, stops: list[tuple[float, float]]) -> float:
    def haversine(slat, slon):
        p1, p2 = math.radians(lat), math.radians(slat)
        a = math.sin((p2 - p1) / 2) ** 2 + math.cos(p1) * math.cos(p2) * math.sin(math.radians(slon - lon) / 2) ** 2
        return 2 * EARTH_RADIUS_MILES * math.asin(math.sqrt(a))
    return min(haversine(slat, slon) for slat, slon in stops)


def cook_county_density() -> None:
    import numpy as np
    from matplotlib.path import Path as Polygon

    sales_path = DATASETS / "cook-county-home-sales-2025" / "cook-county-home-sales-2025.csv"
    with sales_path.open(newline="", encoding="utf-8") as f:
        sales = list(csv.DictReader(f))
    has_xy = [bool(s["latitude"] and s["longitude"]) for s in sales]
    xy = np.array([[float(s["longitude"]), float(s["latitude"])] if ok else [0.0, 0.0] for s, ok in zip(sales, has_xy)])

    tract_of = [None] * len(sales)
    for feat in tracts():
        props, geom = feat["properties"], feat["geometry"]
        if not props["AREALAND"]:  # water-only tracts in Lake Michigan
            continue
        polygons = geom["coordinates"] if geom["type"] == "MultiPolygon" else [geom["coordinates"]]
        for rings in polygons:
            verts, codes = [], []
            for ring in rings:  # outer ring plus holes, so a hole is not "inside"
                verts += ring
                codes += [Polygon.MOVETO] + [Polygon.LINETO] * (len(ring) - 2) + [Polygon.CLOSEPOLY]
            for i in np.flatnonzero(Polygon(np.array(verts), codes).contains_points(xy)):
                if has_xy[i] and tract_of[i] is None:
                    tract_of[i] = props

    stops = l_stops()
    header = ["sale_date", "sale_price", "property_group", "is_multisale", "building_sqft", "land_sqft",
              "municipality", "in_chicago", "tract_geoid", "tract_population_2020", "tract_housing_units_2020",
              "tract_land_sq_mi", "people_per_sq_mi", "housing_units_per_sq_mi", "miles_to_nearest_l_stop"]
    rows = []
    for s, t, ok in zip(sales, tract_of, has_xy):
        sq_mi = t["AREALAND"] / SQ_METERS_PER_SQ_MILE if t else None
        rows.append([
            s["sale_date"], s["sale_price"], s["property_group"], s["is_multisale"], s["building_sqft"],
            s["land_sqft"], s["municipality"], s["municipality"] == "CITY OF CHICAGO",
            t["GEOID"] if t else "", t["POP100"] if t else "", t["HU100"] if t else "",
            f"{sq_mi:.4f}" if t else "", f"{t['POP100'] / sq_mi:.1f}" if t else "",
            f"{t['HU100'] / sq_mi:.1f}" if t else "",
            f"{miles_to_nearest(float(s['latitude']), float(s['longitude']), stops):.3f}" if ok else "",
        ])
    write_csv("cook-county-sales-density.csv", header, rows)


BUILDERS = {
    "penguins": penguins,
    "spambase": spambase,
    "wdbc": wdbc,
    "college-scorecard": college_scorecard,
    "cook-county": cook_county_density,
}


if __name__ == "__main__":
    wanted = sys.argv[1:] or list(BUILDERS)
    for name in wanted:
        print(name)
        BUILDERS[name]()
