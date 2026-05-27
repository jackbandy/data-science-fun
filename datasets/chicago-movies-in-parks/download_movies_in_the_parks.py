#!/usr/bin/env python3
# Modified by an LLM coding system.

from pathlib import Path
import re

import pandas as pd
import requests


CATALOG_URL = "https://api.us.socrata.com/api/catalog/v1"
DOMAIN = "data.cityofchicago.org"
TITLE_RE = re.compile(r"movies in the parks", re.I)
DROP_RE = re.compile(r"(phone|telephone|contact.*name|contact.*email|email)", re.I)


def slug(text):
    return re.sub(r"^Chicago_Park_District_?", "", re.sub(r"[^A-Za-z0-9]+", "_", text).strip("_"))


def matches():
    r = requests.get(CATALOG_URL, params={"search_context": DOMAIN, "q": "Movies in the Parks", "only": "datasets", "limit": 100}, timeout=30)
    r.raise_for_status()
    return [x["resource"] for x in r.json().get("results", []) if TITLE_RE.search(x.get("resource", {}).get("name", ""))]


def write_csv(resource, out_dir):
    df = pd.read_csv(f"https://{DOMAIN}/resource/{resource['id']}.csv?$limit=5000000", low_memory=False)
    dropped = [c for c in df.columns if DROP_RE.search(c)]
    df = df.drop(columns=dropped)
    out = out_dir / f"{slug(resource['name'])}.csv"
    df.to_csv(out, index=False)
    print(f"{out.name}: rows={len(df)}, dropped={', '.join(dropped) or 'none'}")


def main():
    out_dir = Path(".").resolve()
    out_dir.mkdir(parents=True, exist_ok=True)
    found = matches()
    if not found:
        print('No datasets found with "Movies in the Parks" in the title.')
        return
    print(f"Found {len(found)} matching dataset(s).")
    for resource in found:
        write_csv(resource, out_dir)


if __name__ == "__main__":
    main()
