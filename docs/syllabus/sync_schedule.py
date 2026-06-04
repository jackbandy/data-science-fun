#!/usr/bin/env python3
"""Sync schedule.md into the homepage and syllabus source, then render syllabus."""

from __future__ import annotations

import argparse
import html
import re
import subprocess
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
from zoneinfo import ZoneInfo


SYLLABUS_DIR = Path(__file__).resolve().parent
ROOT = SYLLABUS_DIR.parent
SCHEDULE_MD = SYLLABUS_DIR / "schedule.md"
INDEX_HTML = ROOT / "index.html"
SYLLABUS_MD = SYLLABUS_DIR / "syllabus.md"
SYLLABUS_HTML = SYLLABUS_DIR / "index.html"
SYLLABUS_PDF = SYLLABUS_DIR / "syllabus.pdf"
UPSTREAM_SYLLABUS = ROOT.parent / "syllabus"

HTML_START = "<!-- SCHEDULE_TABLE_START -->"
HTML_END = "<!-- SCHEDULE_TABLE_END -->"
MD_START = "<!-- SCHEDULE_MARKDOWN_START -->"
MD_END = "<!-- SCHEDULE_MARKDOWN_END -->"

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


def split_markdown_row(line: str) -> list[str]:
    return [cell.strip() for cell in line.strip().strip("|").split("|")]


def read_schedule() -> tuple[list[str], list[ScheduleRow]]:
    lines = SCHEDULE_MD.read_text(encoding="utf-8").splitlines()
    table = [line for line in lines if line.strip().startswith("|")]
    if len(table) < 3:
        raise SystemExit(f"No markdown table found in {SCHEDULE_MD}")

    header = split_markdown_row(table[0])
    expected = ["Week", "Class Day", "Topic", "Before Class", "In Class"]
    if header != expected:
        raise SystemExit(f"{SCHEDULE_MD} header must be: {' | '.join(expected)}")

    rows: list[ScheduleRow] = []
    for line in table[2:]:
        cells = split_markdown_row(line)
        if len(cells) != 5:
            raise SystemExit(f"Expected 5 cells in schedule row: {line}")
        rows.append(ScheduleRow(*cells))

    return table, rows


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
    if updated == text:
        raise SystemExit(f"Could not find homepage schedule table in {INDEX_HTML}")
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
    if updated == text:
        raise SystemExit(f"Could not find syllabus schedule table in {SYLLABUS_MD}")
    SYLLABUS_MD.write_text(updated, encoding="utf-8")


def render_syllabus() -> None:
    created = datetime.now(ZoneInfo("America/Chicago")).strftime("%m/%d/%Y, %H:%M")
    common = [
        "pandoc",
        str(SYLLABUS_MD.relative_to(ROOT)),
        "--from",
        "markdown+smart",
        "--lua-filter",
        str(UPSTREAM_SYLLABUS / "filters" / "underline.lua"),
        "--metadata",
        f"created={created}",
    ]

    subprocess.run(
        common
        + [
            "--template",
            str(UPSTREAM_SYLLABUS / "syllabus_html_template.html"),
            "--standalone",
            "--toc",
            "-o",
            str(SYLLABUS_HTML.relative_to(ROOT)),
        ],
        cwd=ROOT,
        check=True,
    )

    subprocess.run(
        common
        + [
            "--template",
            str(UPSTREAM_SYLLABUS / "pandoc-syllabus-template.tex"),
            "--pdf-engine=xelatex",
            "--metadata",
            "logo_pdf=syllabus/uic-black-logo.pdf",
            "--metadata",
            "main_font=Arial",
            "--resource-path",
            "syllabus",
            "-V",
            "secnumdepth=0",
            "-o",
            str(SYLLABUS_PDF.relative_to(ROOT)),
        ],
        cwd=ROOT,
        check=True,
    )


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--no-render", action="store_true", help="sync files without rendering syllabus outputs")
    args = parser.parse_args()

    table, rows = read_schedule()
    sync_homepage(rows)
    sync_syllabus_source(table)
    if not args.no_render:
        render_syllabus()


if __name__ == "__main__":
    main()
