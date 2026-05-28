#!/usr/bin/env python3
# Modified by an LLM coding system.

from datetime import datetime, timezone
from html import unescape
from pathlib import Path
import re

import numpy as np
import requests


BASE = Path(__file__).resolve().parent
OUT = BASE / "us-national-parks.csv"

NPS_LAYER_URL = (
    "https://services6.arcgis.com/ZncoPpp4shVCg1II/arcgis/rest/services/"
    "Administrative_Boundaries_of_National_Park_System_Units_gdb/FeatureServer/0/query"
)
WIKIPEDIA_URL = "https://en.wikipedia.org/wiki/List_of_national_parks_of_the_United_States"
HEADERS = {"User-Agent": "data-adventures-dataset-script/1.0"}
COLUMNS = [
    "unit_code",
    "unit_name",
    "park_name",
    "state",
    "region",
    "unit_type",
    "established_date",
    "date_edit",
    "longitude",
    "latitude",
]

NPS_PARAMS = {
    "where": "(UNIT_TYPE='National Parks' OR UNIT_CODE='NERI')",
    "outFields": "UNIT_CODE,UNIT_NAME,PARKNAME,STATE,REGION,UNIT_TYPE,DATE_EDIT",
    "returnGeometry": "false",
    "returnCentroid": "true",
    "outSR": "4326",
    "orderByFields": "UNIT_NAME",
    "f": "json",
}

NAME_ALIASES = {
    "Haleakala": "Haleakalā",
    "Hawaii Volcanoes": "Hawaiʻi Volcanoes",
    "National Park of American Samoa": "American Samoa",
    "Wrangell - St Elias": "Wrangell-St. Elias",
}


def clean(value):
    value = re.sub(r"<[^>]+>", "", unescape(str(value)))
    value = re.sub(r"\[[^\]]+\]", "", value)
    value = value.replace("†", "").replace("‡", "").replace("*", "").replace("\xa0", " ")
    value = value.replace("–", "-")
    value = re.sub(r"\s+", " ", value)
    return value.strip()


def established_dates():
    response = requests.get(WIKIPEDIA_URL, headers=HEADERS, timeout=60)
    response.raise_for_status()
    table = re.search(r'<table class="wikitable.*?</table>', response.text, re.S).group(0)
    dates = {}
    for row_html in re.findall(r"<tr[^>]*>(.*?)</tr>", table, re.S)[1:]:
        cells = [clean(c) for c in re.findall(r"<t[dh][^>]*>(.*?)</t[dh]>", row_html, re.S)]
        dates[cells[0]] = datetime.strptime(cells[3], "%B %d, %Y").date().isoformat()
    return dates


def date_from_ms(value):
    if value is None:
        return ""
    return datetime.fromtimestamp(value / 1000, tz=timezone.utc).date().isoformat()


def csv_escape(value):
    value = "" if value is None else str(value)
    return '"' + value.replace('"', '""') + '"' if any(c in value for c in ',\"\n') else value


def fetch_nps_rows():
    response = requests.get(NPS_LAYER_URL, params=NPS_PARAMS, headers=HEADERS, timeout=60)
    response.raise_for_status()
    data = response.json()
    if "error" in data:
        raise RuntimeError(data["error"])
    return data.get("features", [])


def build_rows():
    dates = established_dates()
    rows = []
    for feature in fetch_nps_rows():
        attr = feature["attributes"]
        centroid = feature.get("centroid") or {}
        park_name = attr.get("PARKNAME") or ""
        date_key = NAME_ALIASES.get(park_name, park_name)
        rows.append([
            attr.get("UNIT_CODE") or "",
            attr.get("UNIT_NAME") or "",
            park_name,
            attr.get("STATE") or "",
            attr.get("REGION") or "",
            attr.get("UNIT_TYPE") or "",
            dates.get(date_key, ""),
            date_from_ms(attr.get("DATE_EDIT")),
            f"{centroid.get('x'):.6f}" if centroid.get("x") is not None else "",
            f"{centroid.get('y'):.6f}" if centroid.get("y") is not None else "",
        ])
    return sorted(rows, key=lambda row: row[1])


def main():
    rows = build_rows()
    missing = [row[1] for row in rows if not row[6]]
    if missing:
        raise RuntimeError(f"Missing established dates for: {', '.join(missing)}")
    data = [[csv_escape(value) for value in row] for row in rows]
    np.savetxt(OUT, np.array([COLUMNS] + data, dtype=object), fmt="%s", delimiter=",")
    print(f"{OUT.name}: rows={len(rows)}")


if __name__ == "__main__":
    main()
