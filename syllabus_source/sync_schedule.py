#!/usr/bin/env python3
# NOTICE: This file modified by an LLM coding system on 2026-07-26.
"""Sync schedule.csv into the homepage table and the syllabus schedule table."""

from __future__ import annotations

import csv
import html
import re
from pathlib import Path


SOURCE_DIR = Path(__file__).resolve().parent
SCHEDULE_CSV = SOURCE_DIR / "schedule.csv"
SYLLABUS_MD = SOURCE_DIR / "syllabus.md"
INDEX_HTML = SOURCE_DIR.parent / "docs" / "index.html"

HTML_START = "<!-- SCHEDULE_TABLE_START -->"
HTML_END = "<!-- SCHEDULE_TABLE_END -->"
MD_START = "<!-- SCHEDULE_MARKDOWN_START -->"
MD_END = "<!-- SCHEDULE_MARKDOWN_END -->"
HEADERS = ["Week", "Class Day", "Topic", "Before Class", "In Class"]

# Blue Line stations, used as a per-week label on the homepage schedule.
STATIONS = {
    "1": "Harold Washington Library",
    "2": "LaSalle/Van Buren",
    "3": "Quincy",
    "4": "Washington/Wells",
    "5": "Clark/Lake",
    "6": "Washington/Wabash",
    "7": "Adams/Wabash",
    "8": "Roosevelt",
    "9": "Halsted",
    "10": "Ashland",
    "11": "35th/Archer",
    "12": "Western",
    "13": "Kedzie",
    "14": "Pulaski",
    "15": "Midway",
}


def read_schedule() -> list[list[str]]:
    """Return schedule.csv as a list of [week, class day, topic, before, in] rows."""
    with SCHEDULE_CSV.open(newline="", encoding="utf-8-sig") as handle:
        reader = csv.DictReader(handle)
        fieldnames = [name.strip() for name in reader.fieldnames or []]
        if fieldnames != HEADERS:
            raise SystemExit(f"{SCHEDULE_CSV} header must be: {', '.join(HEADERS)}")

        rows = []
        for line_number, row in enumerate(reader, start=2):
            values = [(row.get(field) or "").strip() for field in HEADERS]
            if not any(values):
                continue
            if not values[0]:
                raise SystemExit(f"Missing Week value in {SCHEDULE_CSV} at line {line_number}")
            rows.append(values)

    if not rows:
        raise SystemExit(f"No schedule rows found in {SCHEDULE_CSV}")
    return rows


def render_markdown_table(rows: list[list[str]]) -> str:
    lines = [
        "| " + " | ".join(HEADERS) + " |",
        "|:-----|:----------|:------|:-------------|:---------|",
    ]
    for row in rows:
        lines.append("| " + " | ".join(value.replace("|", r"\|") for value in row) + " |")
    return "\n".join(lines)


def render_homepage_table(rows: list[list[str]]) -> str:
    weeks_per_row: dict[str, int] = {}
    for week, *_ in rows:
        weeks_per_row[week] = weeks_per_row.get(week, 0) + 1

    seen: set[str] = set()
    out = [
        '<table class="schedule-table">',
        "  <thead>",
        "    <tr>",
        *[f'      <th scope="col">{header}</th>' for header in HEADERS],
        "    </tr>",
        "  </thead>",
        "  <tbody>",
    ]

    for week, *cells in rows:
        out.append("    <tr>")
        if week not in seen:
            seen.add(week)
            station = STATIONS.get(week, "")
            label = html.escape(f"Week {week}, {station}" if station else f"Week {week}")
            out.append(
                f'      <th scope="row" rowspan="{weeks_per_row[week]}">'
                f'<span class="schedule-week-dot" data-label="{label}" '
                f'aria-label="{label}" tabindex="0">{html.escape(week)}</span></th>'
            )
        out.extend(f"      <td>{html.escape(cell)}</td>" for cell in cells)
        out.append("    </tr>")

    out.extend(["  </tbody>", "</table>"])
    return "\n".join(out)


def replace_between_markers(path: Path, start: str, end: str, replacement: str) -> None:
    text = path.read_text(encoding="utf-8")
    if start not in text or end not in text:
        raise SystemExit(f"Could not find {start} / {end} markers in {path}")
    updated = re.sub(
        re.escape(start) + r".*?" + re.escape(end),
        lambda _: f"{start}\n{replacement}\n{end}",
        text,
        flags=re.DOTALL,
    )
    if updated != text:
        path.write_text(updated, encoding="utf-8")


def main() -> None:
    rows = read_schedule()
    replace_between_markers(INDEX_HTML, HTML_START, HTML_END, render_homepage_table(rows))
    replace_between_markers(SYLLABUS_MD, MD_START, MD_END, render_markdown_table(rows))


if __name__ == "__main__":
    main()
