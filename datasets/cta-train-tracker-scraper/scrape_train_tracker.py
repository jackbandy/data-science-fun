#!/usr/bin/env python3
# NOTICE: substantially modified by an LLM coding system.

"""Scrape the CTA Train Tracker arrival board for one or more stations.

The Train Tracker publishes a page per station showing the next several
arrivals as a countdown ("Due", "5 min", "26 min"). This script takes one
snapshot and writes it to a CSV, so that repeated runs accumulate a history

The two stations below are the ones used in the Week 4 slides

Usage:
    python3 scrape_train_tracker.py                      # -> stdout summary + default file
    python3 scrape_train_tracker.py --out run3.csv
    python3 scrape_train_tracker.py --stations 40350     # just UIC-Halsted

Requires Python 3.9+, `requests`, and `beautifulsoup4`.
"""

from __future__ import annotations

from datetime import datetime, timedelta
from pathlib import Path
import argparse
import csv
import re
import sys
import time

import requests
from bs4 import BeautifulSoup

BASE = Path(__file__).resolve().parent

URL = "https://www.transitchicago.com/traintracker/arrivaltimes/?sid={sid}"

# Station ids are the MAP_ID column of datasets/chicago-l-stations, which is
# also the `sid` query parameter the Train Tracker uses.
STATIONS = {
    "40350": "UIC-Halsted",
    "40730": "Washington/Wells",
}

# Identify the scraper rather than pretending to be a browser
# and leave a gap between requests
HEADERS = {"User-Agent": "data-science-fun-course-dataset/1.0 (CS 418 @ UIC; educational use)"}
DELAY_SECONDS = 2

FIELDNAMES = [
    "station",
    "station_id",
    "line",
    "run",
    "destination",
    "direction",
    "collected",
    "shown",
    "minutes",
    "expected",
]

# The arrival board interleaves two kinds of element as of writing
ROW_SELECTOR = ".estimated-arrivals-subheader, .estimated-arrivals-line"

# Only headings that begin "Service" name a platform
DIRECTION_PREFIX = "Service"


def parse_direction(text: str) -> str:
    """Reduce a platform heading to just the part that varies.

    Two wordings are in use, and a station uses one or the other:

        "Service toward O'Hare"             -> "O'Hare"
        "Service at Outer Loop platform"    -> "Outer Loop"
    """
    text = text.strip()
    toward = re.fullmatch(r"Service toward (.+)", text)
    if toward:
        return toward.group(1).strip()
    at = re.fullmatch(r"Service at (.+?) platform", text)
    if at:
        return at.group(1).strip()
    return text


def parse_line(css_classes: list[str]) -> str:
    """Recover the route from the element's colour class, e.g. brown-line -> Brown."""
    for name in css_classes:
        if name.endswith("-line") and name != "estimated-arrivals-line":
            return name[: -len("-line")].replace("-", " ").title()
    return ""


def parse_minutes(shown: str) -> int:
    """Minutes away, as an integer. 'Due' has no digits and means 0."""
    match = re.search(r"\d+", shown)
    return int(match.group()) if match else 0


def scrape_station(sid: str, name: str) -> list[dict]:
    """One snapshot of one station's arrival board."""
    html = requests.get(URL.format(sid=sid), headers=HEADERS, timeout=30).text
    collected = datetime.now().replace(microsecond=0)
    soup = BeautifulSoup(html, "html.parser")

    rows: list[dict] = []
    direction = None

    for tag in soup.select(ROW_SELECTOR):
        classes = tag.get("class", [])

        if "estimated-arrivals-subheader" in classes:
            heading = tag.get_text(strip=True)
            # A non-"Service" heading ends the arrivals list rather than
            # starting a new one, so drop the direction instead of keeping a
            # stale one around.
            direction = parse_direction(heading) if heading.startswith(DIRECTION_PREFIX) else None
            continue

        if direction is None:
            continue

        title = tag.select_one(".ea-line-title-top").get_text(strip=True)
        destination = tag.select_one(".ea-line-title-bottom")
        shown = tag.select_one(".ea-line-time").get_text(" ", strip=True)
        minutes = parse_minutes(shown)

        rows.append({
            "station": name,
            "station_id": sid,
            "line": parse_line(classes),
            # "Blue Line #130 to" -> "130"
            "run": title.split("#")[1].split()[0] if "#" in title else "",
            "destination": destination.get_text(strip=True) if destination else "",
            "direction": direction,
            "collected": collected.isoformat(sep=" "),
            "shown": shown,
            "minutes": minutes,
            "expected": (collected + timedelta(minutes=minutes)).isoformat(sep=" "),
        })

    return rows


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--out", default=None, help="CSV to write (default: cta-arrivals-<timestamp>.csv)")
    parser.add_argument("--stations", nargs="+", default=list(STATIONS), help="station ids to scrape")
    args = parser.parse_args()

    rows: list[dict] = []
    for i, sid in enumerate(args.stations):
        if i:
            time.sleep(DELAY_SECONDS)
        name = STATIONS.get(sid, sid)
        station_rows = scrape_station(sid, name)
        print(f"{name} ({sid}): {len(station_rows)} arrivals", file=sys.stderr)
        rows.extend(station_rows)

    if not rows:
        # Nothing parsed means the markup moved (not that no trains are running)
        # Failing here is better than committing an empty file.
        print("ERROR: no arrivals parsed. the page markup has probably changed", file=sys.stderr)
        return 1

    stamp = datetime.now().strftime("%Y%m%dT%H%M")
    out = Path(args.out) if args.out else BASE / f"cta-arrivals-{stamp}.csv"
    with out.open("w", newline="", encoding="utf-8") as fh:
        writer = csv.DictWriter(fh, fieldnames=FIELDNAMES)
        writer.writeheader()
        writer.writerows(rows)

    print(f"wrote {len(rows)} rows -> {out}", file=sys.stderr)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
