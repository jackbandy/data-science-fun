#!/usr/bin/env python3
"""Generate left-to-right data science lifecycle SVG variants."""

from __future__ import annotations

import base64
import shutil
from pathlib import Path
from xml.sax.saxutils import escape


PHI = (1 + 5**0.5) / 2
WIDTH = 1000
HEIGHT = round(WIDTH / PHI)
NODE_WIDTH = 145
NODE_HEIGHT = 78

OUT_DIR = Path(__file__).resolve().parent
NEUTRAL = "#EEEEEE"
HIGHLIGHT = "#222222"
STROKE = "#111111"
TEXT = "#111111"
TEXT_ON_DARK = "#FFFFFF"
ARROW_SIZE = 5
FONT_FAMILY = "Libre Franklin"
FONT_FILE = "LibreFranklin.woff2"
FONT_SOURCE = OUT_DIR / "../../../slides/theme/fonts/libre-franklin" / FONT_FILE


NODES = [
    ("ask_question", "Ask a\nquestion"),
    ("obtain_data", "Obtain\ndata"),
    ("understand_data", "Understand\nthe data"),
    ("understand_world", "Understand\nthe world"),
    ("reports", "Reports,\ndecisions,\nsolutions"),
]

NODE_POSITIONS = {
    node_id: (110 + index * 195, 300) for index, (node_id, _) in enumerate(NODES)
}

# Directed relationships copied from ds-lifecycle.svg and laid out on one row.
EDGES = [
    ("ask_question", "obtain_data", "straight", 0),
    ("obtain_data", "understand_data", "straight", 0),
    ("understand_data", "obtain_data", "lower", 106),
    ("ask_question", "understand_data", "upper", 190),
    ("understand_data", "understand_world", "straight", 0),
    ("understand_world", "ask_question", "lower", 245),
    ("understand_data", "reports", "upper", 165),
    ("understand_world", "reports", "straight", 0),
]

ENTRY_POINTS = ["ask_question", "obtain_data"]


def line_endpoint(source: tuple[int, int], target: tuple[int, int]) -> tuple[float, float]:
    sx, sy = source
    tx, ty = target
    if tx > sx:
        return sx + NODE_WIDTH / 2, sy
    if tx < sx:
        return sx - NODE_WIDTH / 2, sy
    if ty > sy:
        return sx, sy + NODE_HEIGHT / 2
    return sx, sy - NODE_HEIGHT / 2


def draw_edge(source_id: str, target_id: str, route: str, offset: int) -> str:
    source = NODE_POSITIONS[source_id]
    target = NODE_POSITIONS[target_id]

    if route == "straight":
        x1, y1 = line_endpoint(source, target)
        x2, y2 = line_endpoint(target, source)
        return (
            f'<line x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}" '
            'stroke="#111111" stroke-width="3" marker-end="url(#arrow)"/>'
        )

    sx, sy = source
    tx, ty = target
    top = route == "upper"
    y_edge = sy - NODE_HEIGHT / 2 if top else sy + NODE_HEIGHT / 2
    control_y = sy - offset if top else sy + offset
    x1 = sx
    y1 = y_edge
    x2 = tx
    y2 = y_edge
    c1x = sx + (tx - sx) * 0.35
    c2x = sx + (tx - sx) * 0.65

    return (
        f'<path d="M {x1:.1f} {y1:.1f} C {c1x:.1f} {control_y:.1f}, '
        f'{c2x:.1f} {control_y:.1f}, {x2:.1f} {y2:.1f}" fill="none" '
        'stroke="#111111" stroke-width="3" marker-end="url(#arrow)"/>'
    )


def draw_entry_point(node_id: str) -> str:
    x, y = NODE_POSITIONS[node_id]
    y1 = 0
    y2 = y - NODE_HEIGHT / 2
    return (
        f'<line x1="{x:.1f}" y1="{y1:.1f}" x2="{x:.1f}" y2="{y2:.1f}" '
        'stroke="#111111" stroke-width="3" stroke-dasharray="9 8" '
        'marker-end="url(#arrow)"/>'
    )


def draw_node(node_id: str, label: str, highlighted: bool) -> str:
    x, y = NODE_POSITIONS[node_id]
    fill = HIGHLIGHT if highlighted else NEUTRAL
    title_color = TEXT_ON_DARK if highlighted else TEXT
    lines = label.split("\n")
    line_height = 22
    first_y = y - ((len(lines) - 1) * line_height) / 2 + 7
    tspans = "\n".join(
        f'<tspan x="{x}" y="{first_y + index * line_height:.1f}">{escape(line)}</tspan>'
        for index, line in enumerate(lines)
    )

    return f"""
  <rect x="{x - NODE_WIDTH / 2:.1f}" y="{y - NODE_HEIGHT / 2:.1f}" width="{NODE_WIDTH}"
        height="{NODE_HEIGHT}" rx="6" fill="{fill}" stroke="{STROKE}" stroke-width="3"/>
  <text text-anchor="middle" font-family="{FONT_FAMILY}" font-size="20"
        font-weight="700" fill="{title_color}">{tspans}</text>"""


def font_data_url() -> str:
    encoded = base64.b64encode(FONT_SOURCE.read_bytes()).decode("ascii")
    return f"data:font/woff2;base64,{encoded}"


def make_svg(highlight_index: int | None) -> str:
    edge_markup = "\n  ".join(draw_edge(*edge) for edge in EDGES)
    entry_markup = "\n  ".join(draw_entry_point(node_id) for node_id in ENTRY_POINTS)
    node_markup = "\n".join(
        draw_node(node_id, label, index == highlight_index)
        for index, (node_id, label) in enumerate(NODES)
    )

    return f"""<svg width="{WIDTH}" height="{HEIGHT}" viewBox="0 0 {WIDTH} {HEIGHT}" fill="none" xmlns="http://www.w3.org/2000/svg">
  <rect width="{WIDTH}" height="{HEIGHT}" fill="white"/>
  <style>
    @font-face {{
      font-family: '{FONT_FAMILY}';
      src: url('{font_data_url()}') format('woff2');
      font-weight: 100 900;
      font-style: normal;
    }}
  </style>
  <defs>
    <marker id="arrow" markerWidth="{ARROW_SIZE}" markerHeight="{ARROW_SIZE}" refX="{ARROW_SIZE}" refY="{ARROW_SIZE / 2}"
            orient="auto" markerUnits="strokeWidth">
      <path d="M 0 0 L {ARROW_SIZE} {ARROW_SIZE / 2} L 0 {ARROW_SIZE} z" fill="#111111"/>
    </marker>
  </defs>
  {entry_markup}
  {edge_markup}
{node_markup}
</svg>
"""


def main() -> None:
    shutil.copy2(FONT_SOURCE, OUT_DIR / FONT_FILE)
    for version in range(6):
        highlight_index = None if version == 0 else version - 1
        path = OUT_DIR / f"ds-lifecycle-v{version}.svg"
        path.write_text(make_svg(highlight_index), encoding="utf-8")
        print(path.name)


if __name__ == "__main__":
    main()
