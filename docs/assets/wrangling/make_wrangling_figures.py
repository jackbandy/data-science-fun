#!/usr/bin/env python3
"""Generate the wrangling SVG figures: granularity, group by, pivot, and scope.

Keys are CTA 'L' routes rather than A/B/C/D, so the diagrams carry the same
transit motif as the rest of the deck. The three routes are Orange, Red, and
Purple: no red/green pair, three clearly separated lightness steps (relative
luminance .25 / .13 / .05), and all three dark enough to carry white text, so
every cell in every figure uses the same white lettering. CTA Blue, Pink, and
Yellow are all too light for that and are left out.
"""

from __future__ import annotations

import base64
from pathlib import Path
from xml.sax.saxutils import escape


OUT_DIR = Path(__file__).resolve().parent

# Official CTA 'L' route colors (see ../STYLE.md).
ORANGE = "#F9461C"
RED = "#C60C30"
PURPLE = "#522398"
STEEL = "#565A5C"  # CTA Sign Grey, used for the non-route key (day type)

INK = "#111111"
PAPER = "#FFFFFF"
DATA_FILL = "#1A1A1A"
NEUTRAL = "#EEEEEE"
MUTED = "#777777"
QUIET = "#AAAAAA"

STROKE_WIDTH = 2
ARROW_SIZE = 5
RX = 5

FONT_FAMILY = "Libre Franklin"
FONT_SOURCE = OUT_DIR / "../fonts/libre-franklin/LibreFranklin.woff2"

# White on Orange is 3.6:1, which clears the WCAG large-text bar at the bold
# sizes used here; Red is 6.0:1 and Purple 10.2:1.
ROUTES = {
    "Orange": ORANGE,
    "Red": RED,
    "Purple": PURPLE,
}


# ---------------------------------------------------------------- primitives


def cell(x, y, w, h, fill, label, color=INK, size=17, weight=700, dashed=False, stroke=INK):
    """A rounded-rect cell with one line of centered text."""
    dash = ' stroke-dasharray="6 5"' if dashed else ""
    baseline = y + h / 2 + size * 0.35
    return (
        f'<rect x="{x:.1f}" y="{y:.1f}" width="{w:.1f}" height="{h:.1f}" rx="{RX}" '
        f'fill="{fill}" stroke="{stroke}" stroke-width="{STROKE_WIDTH}"{dash}/>'
        f'<text x="{x + w / 2:.1f}" y="{baseline:.1f}" text-anchor="middle" '
        f'font-family="{FONT_FAMILY}" font-size="{size}" font-weight="{weight}" '
        f'fill="{color}">{escape(label)}</text>'
    )


def text(x, y, label, size=15, weight=400, color=MUTED, anchor="middle", style=""):
    italic = ' font-style="italic"' if style == "italic" else ""
    return (
        f'<text x="{x:.1f}" y="{y:.1f}" text-anchor="{anchor}" font-family="{FONT_FAMILY}" '
        f'font-size="{size}" font-weight="{weight}" fill="{color}"{italic}>{escape(label)}</text>'
    )


def stacked_text(x, y, lines, size=15, weight=400, color=MUTED):
    """Centered label of one or more lines, `y` being the first baseline."""
    return "".join(text(x, y + i * (size + 4), line, size, weight, color) for i, line in enumerate(lines))


def arrow(x1, y1, x2, y2):
    return (
        f'<line x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}" stroke="{INK}" '
        f'stroke-width="{STROKE_WIDTH}" marker-end="url(#arrow)"/>'
    )


def row(x, y, widths, cells, h=34, gap=5):
    """One record: a run of cells laid out left to right."""
    out = []
    for width, (fill, label, color, size) in zip(widths, cells):
        out.append(cell(x, y, width, h, fill, label, color, size=size))
        x += width + gap
    return "".join(out)


def route_cell(name):
    """Route names sit at 19px bold, the size white-on-Orange needs to clear
    WCAG's large-text ratio."""
    return (ROUTES[name], name, PAPER, 19)


def data_cell(value):
    return (DATA_FILL, str(value), PAPER, 17)


def daytype_cell(name):
    return (STEEL, name, PAPER, 17)


def font_data_url():
    encoded = base64.b64encode(FONT_SOURCE.read_bytes()).decode("ascii")
    return f"data:font/woff2;base64,{encoded}"


def svg(width, height, body, label):
    return f"""<?xml version="1.0" encoding="UTF-8"?>
<svg width="{width}" height="{height}" viewBox="0 0 {width} {height}" fill="none" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="{escape(label, {chr(34): "&quot;"})}">
  <title>{escape(label)}</title>
  <rect width="{width}" height="{height}" fill="{PAPER}"/>
  <style>
    @font-face {{
      font-family: '{FONT_FAMILY}';
      src: url('{font_data_url()}') format('woff2');
      font-weight: 100 900;
      font-style: normal;
    }}
  </style>
  <defs>
    <marker id="arrow" markerWidth="{ARROW_SIZE}" markerHeight="{ARROW_SIZE}" refX="{ARROW_SIZE / 2}" refY="{ARROW_SIZE / 2}"
            orient="auto" markerUnits="strokeWidth">
      <path d="M 0 0 L {ARROW_SIZE} {ARROW_SIZE / 2} L 0 {ARROW_SIZE} z" fill="{INK}"/>
    </marker>
  </defs>
  {body}
</svg>
"""


# ------------------------------------------------------------ group by (1 key)

GB_WIDTH, GB_HEIGHT = 1050, 500
GB_CY = 265
CELL_H = 34
ROW_GAP = 6
KEY_W = 94
DATA_W = 56
CELL_GAP = 5
GB_ROW_W = KEY_W + CELL_GAP + DATA_W

GB_COL1_X, GB_COL2_X, GB_COL3_X, GB_COL4_X = 34, 306, 580, 858

# The nine records, in the order a CSV might hand them to you.
GB_ROWS = [
    ("Orange", 3), ("Red", 1), ("Purple", 4),
    ("Orange", 1), ("Red", 5), ("Purple", 9),
    ("Orange", 2), ("Red", 6), ("Purple", 5),
]
GB_KEYS = ["Orange", "Red", "Purple"]
GB_GROUPS = {key: [value for k, value in GB_ROWS if k == key] for key in GB_KEYS}

GB_GROUP_H = 3 * CELL_H + 2 * ROW_GAP  # every group holds three records
GB_GROUP_GAP = 26
GB_COL2_TOP = GB_CY - (3 * GB_GROUP_H + 2 * GB_GROUP_GAP) / 2
GB_GROUP_CENTERS = [GB_COL2_TOP + i * (GB_GROUP_H + GB_GROUP_GAP) + GB_GROUP_H / 2 for i in range(3)]
GB_COL1_TOP = GB_CY - (9 * CELL_H + 8 * ROW_GAP) / 2
GB_COL4_TOP = GB_CY - GB_GROUP_H / 2


def groupby_raw():
    parts = [
        text(GB_COL1_X + KEY_W / 2, GB_COL1_TOP - 12, "line", 16, 700),
        text(GB_COL1_X + KEY_W + CELL_GAP + DATA_W / 2, GB_COL1_TOP - 12, "rides", 16, 700),
    ]
    for i, (key, value) in enumerate(GB_ROWS):
        y = GB_COL1_TOP + i * (CELL_H + ROW_GAP)
        parts.append(row(GB_COL1_X, y, [KEY_W, DATA_W], [route_cell(key), data_cell(value)]))
    return "".join(parts)


def groupby_split():
    parts = [
        stacked_text(247, GB_CY - 30, ["Split into", "Groups"], 15, 600, INK),
        arrow(193, GB_CY, GB_COL2_X - 6, GB_CY),
    ]
    for g, key in enumerate(GB_KEYS):
        top = GB_COL2_TOP + g * (GB_GROUP_H + GB_GROUP_GAP)
        for i, value in enumerate(GB_GROUPS[key]):
            y = top + i * (CELL_H + ROW_GAP)
            parts.append(row(GB_COL2_X, y, [KEY_W, DATA_W], [route_cell(key), data_cell(value)]))
    return "".join(parts)


def groupby_aggregate():
    parts = []
    for g, key in enumerate(GB_KEYS):
        cy = GB_GROUP_CENTERS[g]
        parts.append(stacked_text(520, cy - 30, ["Aggregate", "Function"], 15, 600, INK))
        parts.append(arrow(465, cy, GB_COL3_X - 6, cy))
        parts.append(row(GB_COL3_X, cy - CELL_H / 2, [KEY_W, DATA_W],
                         [route_cell(key), data_cell(sum(GB_GROUPS[key]))]))
    return "".join(parts)


def groupby_merge():
    parts = [stacked_text(796, GB_CY - 30, ["Merge", "Results"], 15, 600, INK)]
    for g, key in enumerate(GB_KEYS):
        target_cy = GB_COL4_TOP + g * (CELL_H + ROW_GAP) + CELL_H / 2
        parts.append(arrow(739, GB_GROUP_CENTERS[g], GB_COL4_X - 6, target_cy))
        parts.append(row(GB_COL4_X, GB_COL4_TOP + g * (CELL_H + ROW_GAP), [KEY_W, DATA_W],
                         [route_cell(key), data_cell(sum(GB_GROUPS[key]))]))
    return "".join(parts)


GROUPBY_STAGES = [
    (groupby_raw, "Nine records of rides keyed by CTA route: Orange, Red, and Purple, in the order they arrive."),
    (groupby_split, "The same records split into three groups, one per route."),
    (groupby_aggregate, "An aggregate function reduces each group to a single total: Orange 6, Red 12, Purple 18."),
    (groupby_merge, "The three group totals merged back into one table with one row per route."),
]


def make_groupby(stage):
    body = "".join(fn() for fn, _ in GROUPBY_STAGES[: stage + 1])
    return svg(GB_WIDTH, GB_HEIGHT, body, "Split, apply, combine: " + GROUPBY_STAGES[stage][1])


# --------------------------------------------------------------- pivot (2 keys)

PV_WIDTH, PV_HEIGHT = 1058, 510
PV_CY = 265
KEY2_W = 98
PV_ROW_W = KEY_W + CELL_GAP + KEY2_W + CELL_GAP + DATA_W
PV_COL1_X, PV_COL2_X, PV_COL3_X = 30, 400, 772
PV_WIDTHS = [KEY_W, KEY2_W, DATA_W]

PV_ROWS = [
    ("Orange", "Weekday", 3), ("Red", "Saturday", 1), ("Purple", "Weekday", 4),
    ("Orange", "Saturday", 1), ("Red", "Weekday", 5), ("Purple", "Weekday", 9),
    ("Orange", "Weekday", 2), ("Red", "Saturday", 6), ("Purple", "Weekday", 5),
]
PV_LINES = ["Orange", "Red", "Purple"]
PV_DAYTYPES = ["Weekday", "Saturday"]
# Group keys in sorted order, which is the order pivot puts them in.
PV_KEYS = [(line, day) for line in PV_LINES for day in PV_DAYTYPES
           if any(r[0] == line and r[1] == day for r in PV_ROWS)]
PV_GROUPS = {k: [v for line, day, v in PV_ROWS if (line, day) == k] for k in PV_KEYS}

PV_GROUP_GAP = 16
PV_GROUP_HEIGHTS = [len(PV_GROUPS[k]) * CELL_H + (len(PV_GROUPS[k]) - 1) * ROW_GAP for k in PV_KEYS]
PV_COL2_TOP = PV_CY - (sum(PV_GROUP_HEIGHTS) + (len(PV_KEYS) - 1) * PV_GROUP_GAP) / 2
PV_GROUP_TOPS = []
_y = PV_COL2_TOP
for _h in PV_GROUP_HEIGHTS:
    PV_GROUP_TOPS.append(_y)
    _y += _h + PV_GROUP_GAP
PV_GROUP_CENTERS = [top + h / 2 for top, h in zip(PV_GROUP_TOPS, PV_GROUP_HEIGHTS)]
PV_COL1_TOP = PV_CY - (9 * CELL_H + 8 * ROW_GAP) / 2


def pivot_raw():
    parts = [
        text(PV_COL1_X + KEY_W / 2, PV_COL1_TOP - 12, "line", 16, 700),
        text(PV_COL1_X + KEY_W + CELL_GAP + KEY2_W / 2, PV_COL1_TOP - 12, "day type", 16, 700),
        text(PV_COL1_X + KEY_W + KEY2_W + 2 * CELL_GAP + DATA_W / 2, PV_COL1_TOP - 12, "rides", 16, 700),
    ]
    for i, (line, day, value) in enumerate(PV_ROWS):
        y = PV_COL1_TOP + i * (CELL_H + ROW_GAP)
        parts.append(row(PV_COL1_X, y, PV_WIDTHS, [route_cell(line), daytype_cell(day), data_cell(value)]))
    return "".join(parts)


def pivot_split():
    parts = [
        stacked_text(344, PV_CY - 30, ["Split into", "Groups"], 15, 600, INK),
        arrow(PV_COL1_X + PV_ROW_W + 8, PV_CY, PV_COL2_X - 6, PV_CY),
    ]
    for k, key in enumerate(PV_KEYS):
        line, day = key
        for i, value in enumerate(PV_GROUPS[key]):
            y = PV_GROUP_TOPS[k] + i * (CELL_H + ROW_GAP)
            parts.append(row(PV_COL2_X, y, PV_WIDTHS, [route_cell(line), daytype_cell(day), data_cell(value)]))
    return "".join(parts)


def pivot_aggregate():
    parts = []
    for k, key in enumerate(PV_KEYS):
        line, day = key
        cy = PV_GROUP_CENTERS[k]
        parts.append(text(714, cy - 6, "Aggregate", 13, 600, INK))
        parts.append(text(714, cy + 9, "Function", 13, 600, INK))
        parts.append(arrow(PV_COL2_X + PV_ROW_W + 8, cy, PV_COL3_X - 6, cy))
        parts.append(row(PV_COL3_X, cy - CELL_H / 2, PV_WIDTHS,
                         [route_cell(line), daytype_cell(day), data_cell(sum(PV_GROUPS[key]))]))
    return "".join(parts)


PIVOT_STAGES = [
    (pivot_raw, "Nine records keyed by two columns, CTA route and day type."),
    (pivot_split, "The records split into five groups, one per route and day type pair that appears in the data."),
    (pivot_aggregate, "Each group reduced to one total, still keyed by route and day type."),
]


def make_pivot(stage):
    body = "".join(fn() for fn, _ in PIVOT_STAGES[: stage + 1])
    return svg(PV_WIDTH, PV_HEIGHT, body, "Pivot, step by step: " + PIVOT_STAGES[stage][1])


def make_pivot_result():
    """The aggregated pairs reshaped into a route-by-day-type grid."""
    left_x = 62
    left_h = len(PV_KEYS) * CELL_H + (len(PV_KEYS) - 1) * ROW_GAP
    left_top = 250 - left_h / 2
    parts = []
    for k, key in enumerate(PV_KEYS):
        line, day = key
        y = left_top + k * (CELL_H + ROW_GAP)
        parts.append(row(left_x, y, PV_WIDTHS,
                         [route_cell(line), daytype_cell(day), data_cell(sum(PV_GROUPS[key]))]))

    parts.append(text(460, 238, "Pivot", 17, 700, INK))
    parts.append(arrow(left_x + PV_ROW_W + 12, 250, 584, 250))

    grid_x = 598
    label_w, col_w, cell_h, gap = 104, 118, 40, 6
    # Centre the grid block on the same axis as the column of aggregated rows.
    header_y = 250 - ((len(PV_LINES) + 1) * (cell_h + gap) - gap) / 2
    for c, day in enumerate(PV_DAYTYPES):
        x = grid_x + label_w + gap + c * (col_w + gap)
        parts.append(cell(x, header_y, col_w, cell_h, STEEL, day, PAPER))
    for r, line in enumerate(PV_LINES):
        y = header_y + (r + 1) * (cell_h + gap)
        parts.append(cell(grid_x, y, label_w, cell_h, ROUTES[line], line, PAPER, size=19))
        for c, day in enumerate(PV_DAYTYPES):
            x = grid_x + label_w + gap + c * (col_w + gap)
            values = PV_GROUPS.get((line, day))
            if values is None:
                parts.append(cell(x, y, col_w, cell_h, NEUTRAL, "NaN", MUTED, dashed=True, stroke=QUIET))
            else:
                parts.append(cell(x, y, col_w, cell_h, DATA_FILL, str(sum(values)), PAPER))

    note_y = header_y + (len(PV_LINES) + 1) * (cell_h + gap) + 30
    parts.append(text(grid_x + (label_w + gap + 2 * (col_w + gap)) / 2, note_y,
                      "No Purple Line records on a Saturday; the missing value needs a decision",
                      15, 400, MUTED, style="italic"))
    body = "".join(parts)
    return svg(PV_WIDTH, PV_HEIGHT, body,
               "The five aggregated groups reshaped into a grid with one row per CTA route and one column per day "
               "type. The Purple Line Saturday cell is empty, marked NaN.")


# ------------------------------------------------------------------ granularity

GR_WIDTH, GR_HEIGHT = 1080, 420
GR_CARD_W = 310
GR_CARD_XS = [30, 385, 740]

GR_CARDS = [
    {
        "caption": "one row = one tap-in",
        "widths": [90, 130, 90],
        "header": ["rider", "station", "time"],
        "rows": [
            ["4821", "Quincy/Wells", "07:42:18"],
            ["7130", "Quincy/Wells", "07:42:51"],
            ["2265", "Quincy/Wells", "07:43:04"],
            ["9048", "Quincy/Wells", "07:43:22"],
            ["1573", "Quincy/Wells", "07:43:55"],
        ],
    },
    {
        "caption": "one row = one station-day",
        "widths": [130, 90, 90],
        "header": ["station", "date", "entries"],
        "rows": [
            ["Quincy/Wells", "Aug 13", "6,715"],
            ["Midway Airport", "Aug 13", "5,536"],
            ["Roosevelt", "Aug 13", "7,915"],
        ],
    },
    {
        "caption": "one row = one line-month",
        "widths": [100, 100, 110],
        "header": ["line", "month", "entries"],
        "rows": [
            ["Orange", "Aug 2025", "1,141,856"],
            ["Red", "Aug 2025", "3,703,028"],
        ],
    },
]


def make_granularity():
    parts = []
    header_y, row_h, row_gap = 62, 34, 6
    for card, x in zip(GR_CARDS, GR_CARD_XS):
        parts.append(text(x + GR_CARD_W / 2, 36, card["caption"], 17, 700, INK))
        cx = x
        for width, label in zip(card["widths"], card["header"]):
            parts.append(cell(cx, header_y, width, row_h, NEUTRAL, label, INK, size=14))
            cx += width
        for r, values in enumerate(card["rows"]):
            y = header_y + row_h + row_gap + r * (row_h + row_gap)
            cx = x
            for c, (width, value) in enumerate(zip(card["widths"], values)):
                if c == 0 and value in ROUTES:
                    # Route names keep the 19px bold white lettering they carry
                    # in every other figure; white on Orange needs that size.
                    parts.append(cell(cx, y, width, row_h, ROUTES[value], value, PAPER, size=19))
                else:
                    parts.append(cell(cx, y, width, row_h, PAPER, value, INK, size=14, weight=400))
                cx += width

    bar_y = 344
    parts.append(
        f'<line x1="30" y1="{bar_y}" x2="1032" y2="{bar_y}" stroke="{INK}" stroke-width="3" '
        'marker-end="url(#arrow)"/>'
    )
    parts.append(text(30, bar_y + 30, "fine grained", 19, 700, INK, anchor="start"))
    parts.append(text(1050, bar_y + 30, "coarse grained", 19, 700, INK, anchor="end"))
    parts.append(text(540, bar_y + 30, "fewer rows, each one summarizing more", 15, 400, MUTED, style="italic"))
    return svg(GR_WIDTH, GR_HEIGHT, "".join(parts),
               "Three tables of the same CTA ridership at three granularities: one row per tap-in, one row per "
               "station-day, one row per line-month, along an arrow from fine grained to coarse grained.")


# ------------------------------------------------------------------------ scope

SC_WIDTH, SC_HEIGHT = 1050, 420
SC_PANELS = [
    {
        "x": 40,
        "question": '"How busy was the Orange Line in 2025?"',
        "diagnosis": "The data is broader than the question",
        "data_label": "All 'L' entries, 2001-2026",
        "pop_label": "Orange Line, 2025",
        "note": "Filter down to the rows in scope",
        "overlap": False,
    },
    {
        "x": 560,
        "question": '"How do people get to Midway?"',
        "diagnosis": "The data covers only part of the question",
        "data_label": "Orange Line entries",
        "pop_label": "Everyone traveling to Midway",
        "note": "Filter, and go find the rest",
        "overlap": True,
    },
]


def scope_panel(panel):
    x = panel["x"]
    # The question the panel is about comes first; the diagnosis under it names
    # what the picture shows, and the note at the bottom says what to do.
    parts = [
        text(x + 225, 42, panel["question"], 19, 700, INK),
        text(x + 225, 68, panel["diagnosis"], 15, 400, MUTED, style="italic"),
    ]
    if not panel["overlap"]:
        parts.append(
            f'<rect x="{x}" y="96" width="450" height="244" rx="14" fill="{ORANGE}" stroke="{INK}" '
            f'stroke-width="{STROKE_WIDTH}"/>'
        )
        parts.append(text(x + 26, 330, panel["data_label"], 19, 700, PAPER, anchor="start"))
        parts.append(
            f'<ellipse cx="{x + 240}" cy="196" rx="150" ry="72" fill="{NEUTRAL}" stroke="{INK}" '
            f'stroke-width="{STROKE_WIDTH}"/>'
        )
        parts.append(text(x + 240, 203, panel["pop_label"], 17, 700, INK))
    else:
        parts.append(
            f'<ellipse cx="{x + 300}" cy="228" rx="165" ry="102" fill="{NEUTRAL}" stroke="{INK}" '
            f'stroke-width="{STROKE_WIDTH}"/>'
        )
        parts.append(
            f'<rect x="{x}" y="140" width="270" height="196" rx="14" fill="{ORANGE}" stroke="{INK}" '
            f'stroke-width="{STROKE_WIDTH}" fill-opacity="0.92"/>'
        )
        parts.append(text(x + 20, 326, panel["data_label"], 19, 700, PAPER, anchor="start"))
        parts.append(text(x + 450, 114, panel["pop_label"], 17, 700, INK, anchor="end"))
    parts.append(text(x + 225, 386, panel["note"], 16, 400, MUTED, style="italic"))
    return "".join(parts)


def make_scope(stage):
    body = "".join(scope_panel(p) for p in SC_PANELS[: stage + 1])
    label = ('One panel, under the question "How busy was the Orange Line in 2025?": a rounded rectangle holding '
             "every 'L' entry from 2001 to 2026, with a smaller ellipse of 2025 Orange Line entries entirely inside "
             "it, so the answer is a matter of filtering."
             if stage == 0 else
             'Two panels. Under "How busy was the Orange Line in 2025?", a rectangle of all \'L\' entries fully '
             "contains the ellipse of 2025 Orange Line entries. Under \"How do people get to Midway?\", a rectangle "
             "of Orange Line entries overlaps an ellipse of everyone traveling to Midway only partly, leaving most "
             "of those travelers outside the data.")
    return svg(SC_WIDTH, SC_HEIGHT, body, label)


# ------------------------------------------------------------------------- main


def main() -> None:
    written = []
    written.append(("granularity-v0.svg", make_granularity()))
    for stage in range(len(GROUPBY_STAGES)):
        written.append((f"groupby-v{stage}.svg", make_groupby(stage)))
    for stage in range(len(PIVOT_STAGES)):
        written.append((f"pivot-v{stage}.svg", make_pivot(stage)))
    written.append(("pivot-v3.svg", make_pivot_result()))
    for stage in range(len(SC_PANELS)):
        written.append((f"scope-v{stage}.svg", make_scope(stage)))

    for name, markup in written:
        path = OUT_DIR / name
        path.write_text(markup, encoding="utf-8")
        print(path.name)


if __name__ == "__main__":
    main()
