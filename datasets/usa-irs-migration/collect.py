"""
Download IRS SOI state-level migration data (2011-2023) and combine into tidy CSVs.

Produces:
  state-inflow.csv  — people moving INTO each state, by origin state
  state-outflow.csv — people moving OUT OF each state, by destination state

County-level files also exist (~4.5 MB each) but are not downloaded here to
keep the repository small. See the README for how to fetch them if needed.
"""

import csv
import urllib.request
from io import StringIO

BASE_URL = "https://www.irs.gov/pub/irs-soi"

# Year pairs in the modern consistent format (2011-12 through 2022-23)
YEAR_PAIRS = [
    (2011, 2012), (2012, 2013), (2013, 2014), (2014, 2015),
    (2015, 2016), (2016, 2017), (2017, 2018), (2018, 2019),
    (2019, 2020), (2020, 2021), (2021, 2022), (2022, 2023),
]


def fetch_csv(url):
    print(f"  fetching {url}")
    with urllib.request.urlopen(url) as resp:
        return resp.read().decode("utf-8")


def download_direction(direction):
    """Download and combine all year pairs for 'inflow' or 'outflow'."""
    all_rows = []
    header = None

    for y1, y2 in YEAR_PAIRS:
        tag = f"{str(y1)[2:]}{str(y2)[2:]}"  # e.g. "2223"
        url = f"{BASE_URL}/state{direction}{tag}.csv"
        text = fetch_csv(url)

        reader = csv.DictReader(StringIO(text))
        if header is None:
            header = ["y1_year", "y2_year"] + reader.fieldnames

        for row in reader:
            all_rows.append({"y1_year": y1, "y2_year": y2, **row})

    out_file = f"state-{direction}.csv"
    with open(out_file, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=header)
        writer.writeheader()
        writer.writerows(all_rows)

    print(f"wrote {out_file} ({len(all_rows):,} rows)")


if __name__ == "__main__":
    print("downloading state inflow...")
    download_direction("inflow")
    print("downloading state outflow...")
    download_direction("outflow")
    print("done.")
