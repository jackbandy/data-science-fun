#!/usr/bin/env python3
"""Sync schedule.csv into the homepage and syllabus source, then render syllabus."""

from __future__ import annotations

import argparse
import csv
import html
import re
import subprocess
from dataclasses import dataclass
from pathlib import Path


SOURCE_DIR = Path(__file__).resolve().parent
REPO_ROOT = SOURCE_DIR.parent
DOCS_DIR = REPO_ROOT / "docs"
SCHEDULE_CSV = SOURCE_DIR / "schedule.csv"
INDEX_HTML = DOCS_DIR / "index.html"
SYLLABUS_MD = SOURCE_DIR / "syllabus.md"
BUILD_SCRIPT = SOURCE_DIR / "build_syllabus_from_markdown.sh"

HTML_START = "<!-- SCHEDULE_TABLE_START -->"
HTML_END = "<!-- SCHEDULE_TABLE_END -->"
MD_START = "<!-- SCHEDULE_MARKDOWN_START -->"
MD_END = "<!-- SCHEDULE_MARKDOWN_END -->"
EXPECTED_HEADERS = ["Week", "Class Day", "Topic", "Before Class", "In Class"]

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


@dataclass
class ScheduleRow:
    week: str
    class_day: str
    topic: str
    before_class: str
    in_class: str


def markdown_escape(value: str) -> str:
    return value.replace("|", r"\|")


def read_schedule() -> list[ScheduleRow]:
    with SCHEDULE_CSV.open(newline="", encoding="utf-8-sig") as handle:
        reader = csv.DictReader(handle)
        if reader.fieldnames is None:
            raise SystemExit(f"No header row found in {SCHEDULE_CSV}")

        fieldnames = [name.strip() for name in reader.fieldnames]
        if fieldnames != EXPECTED_HEADERS:
            raise SystemExit(
                f"{SCHEDULE_CSV} header must be: {', '.join(EXPECTED_HEADERS)}"
            )

        rows: list[ScheduleRow] = []
        for line_number, row in enumerate(reader, start=2):
            values = []
            for field in EXPECTED_HEADERS:
                value = row.get(field, "")
                values.append(value.strip() if value is not None else "")

            if not any(values):
                continue

            week = values[0]
            if not week:
                raise SystemExit(f"Missing Week value in {SCHEDULE_CSV} at line {line_number}")

            rows.append(ScheduleRow(*values))

    if not rows:
        raise SystemExit(f"No schedule rows found in {SCHEDULE_CSV}")

    return rows


def render_markdown_table(rows: list[ScheduleRow]) -> list[str]:
    table = [
        "| Week | Class Day | Topic | Before Class | In Class |",
        "|:-----|:----------|:------|:-------------|:---------|",
    ]
    for row in rows:
        table.append(
            "| "
            + " | ".join(
                markdown_escape(value)
                for value in [
                    row.week,
                    row.class_day,
                    row.topic,
                    row.before_class,
                    row.in_class,
                ]
            )
            + " |"
        )
    return table


def render_homepage_table(rows: list[ScheduleRow]) -> str:
    grouped: dict[str, int] = {}
    for row in rows:
        grouped[row.week] = grouped.get(row.week, 0) + 1

    seen: set[str] = set()
    out = [
        '<table class="schedule-table">',
        "  <thead>",
        "    <tr>",
        '      <th scope="col">Week</th>',
        '      <th scope="col">Class Day</th>',
        '      <th scope="col">Topic</th>',
        '      <th scope="col">Before Class</th>',
        '      <th scope="col">In Class</th>',
        "    </tr>",
        "  </thead>",
        "  <tbody>",
    ]

    for row in rows:
        out.append("    <tr>")
        if row.week not in seen:
            seen.add(row.week)
            station = STATIONS.get(row.week, "")
            label = f"Week {row.week}, {station}" if station else f"Week {row.week}"
            rowspan = grouped[row.week]
            out.append(
                f'      <th scope="row" rowspan="{rowspan}"><span class="schedule-week-dot" '
                f'data-label="{html.escape(label)}" aria-label="{html.escape(label)}" '
                f'tabindex="0">{html.escape(row.week)}</span></th>'
            )
        out.extend(
            [
                f"      <td>{html.escape(row.class_day)}</td>",
                f"      <td>{html.escape(row.topic)}</td>",
                f"      <td>{html.escape(row.before_class)}</td>",
                f"      <td>{html.escape(row.in_class)}</td>",
                "    </tr>",
            ]
        )

    out.extend(["  </tbody>", "</table>"])
    return "\n".join(out)


def replace_between_markers(text: str, start: str, end: str, replacement: str) -> str:
    block = f"{start}\n{replacement}\n{end}"
    if start in text and end in text:
        return re.sub(
            re.escape(start) + r".*?" + re.escape(end),
            block,
            text,
            flags=re.DOTALL,
        )
    return text


def sync_homepage(rows: list[ScheduleRow]) -> None:
    table = render_homepage_table(rows)
    text = INDEX_HTML.read_text(encoding="utf-8")
    if HTML_START in text and HTML_END in text:
        updated = replace_between_markers(text, HTML_START, HTML_END, table)
    else:
        updated = re.sub(
            r'<table class="schedule-table">.*?</table>',
            f"{HTML_START}\n{table}\n{HTML_END}",
            text,
            count=1,
            flags=re.DOTALL,
        )
    if updated == text and not (HTML_START in text and HTML_END in text):
        raise SystemExit(f"Could not find homepage schedule table in {INDEX_HTML}")
    if updated != text:
        INDEX_HTML.write_text(updated, encoding="utf-8")


def sync_syllabus_source(table_lines: list[str]) -> None:
    table = "\n".join(table_lines)
    text = SYLLABUS_MD.read_text(encoding="utf-8")
    if MD_START in text and MD_END in text:
        updated = replace_between_markers(text, MD_START, MD_END, table)
    else:
        updated = re.sub(
            r"(\#\#\# \[Weekly Schedule\]\{\.underline\}\n\n)(?:\|.*\n)+",
            rf"\1{MD_START}\n{table}\n{MD_END}\n",
            text,
            count=1,
        )
    if updated == text and not (MD_START in text and MD_END in text):
        raise SystemExit(f"Could not find syllabus schedule table in {SYLLABUS_MD}")
    if updated != text:
        SYLLABUS_MD.write_text(updated, encoding="utf-8")


def render_syllabus() -> None:
    subprocess.run([str(BUILD_SCRIPT)], cwd=REPO_ROOT, check=True)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--no-render", action="store_true", help="sync files without rendering syllabus outputs")
    args = parser.parse_args()

    rows = read_schedule()
    table_lines = render_markdown_table(rows)
    sync_homepage(rows)
    sync_syllabus_source(table_lines)
    if not args.no_render:
        render_syllabus()


if __name__ == "__main__":
    main()
