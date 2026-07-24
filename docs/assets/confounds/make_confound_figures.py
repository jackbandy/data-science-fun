#!/usr/bin/env python3
"""Generate SVGs for the four elemental confounds (fork, pipe, collider, descendant).

Follows docs/assets/STYLE.md: golden-ratio canvas, rounded-rect nodes, #111 arrows
with a filled triangle head, embedded Libre Franklin.

Highlight convention (see the Week 6 slides): the node in the middle of each
relation is filled dark when stratifying on it *closes* the path (fork, pipe), and
orange when stratifying on it *opens* a spurious one (collider, descendant).
"""

from __future__ import annotations

import base64
from pathlib import Path
from xml.sax.saxutils import escape

PHI = (1 + 5**0.5) / 2
WIDTH = 1000
HEIGHT = round(WIDTH / PHI)
NODE_W = 145
NODE_H = 100

OUT_DIR = Path(__file__).resolve().parent
NEUTRAL = "#EEEEEE"
CLOSE = "#222222"   # stratify here and the backdoor path closes
OPEN = "#F9461C"    # stratify here and a spurious association opens
STROKE = "#111111"
TEXT = "#111111"
TEXT_ON_DARK = "#FFFFFF"
ARROW_SIZE = 5
STROKE_WIDTH = 3
ARROW_GAP = 4
PULLBACK = ARROW_SIZE / 2 * STROKE_WIDTH + ARROW_GAP

FONT_SOURCE = OUT_DIR / ".." / "fonts" / "libre-franklin" / "LibreFranklin.woff2"

# (filename, {node: (x, y, fill)}, [(from, to)])
FIGURES = {
    "fork": (
        {"Z": (500, 160, CLOSE), "X": (265, 458, NEUTRAL), "Y": (735, 458, NEUTRAL)},
        [("Z", "X"), ("Z", "Y")],
    ),
    "pipe": (
        {"X": (200, 309, NEUTRAL), "Z": (500, 309, CLOSE), "Y": (800, 309, NEUTRAL)},
        [("X", "Z"), ("Z", "Y")],
    ),
    "collider": (
        {"Z": (500, 160, OPEN), "X": (265, 458, NEUTRAL), "Y": (735, 458, NEUTRAL)},
        [("X", "Z"), ("Y", "Z")],
    ),
    "descendant": (
        {
            "X": (200, 215, NEUTRAL),
            "Z": (500, 215, CLOSE),
            "Y": (800, 215, NEUTRAL),
            "D": (500, 480, OPEN),
        },
        [("X", "Z"), ("Z", "Y"), ("Z", "D")],
    ),
}


def clip_to_box(cx: float, cy: float, dx: float, dy: float) -> tuple[float, float]:
    """Walk from a node center along (dx, dy) to where it exits the node box."""
    scales = []
    if dx:
        scales.append((NODE_W / 2) / abs(dx))
    if dy:
        scales.append((NODE_H / 2) / abs(dy))
    s = min(scales)
    return cx + dx * s, cy + dy * s


def edge_path(a: tuple[float, float], b: tuple[float, float]) -> tuple[float, float, float, float]:
    dx, dy = b[0] - a[0], b[1] - a[1]
    length = (dx**2 + dy**2) ** 0.5
    ux, uy = dx / length, dy / length
    x1, y1 = clip_to_box(a[0], a[1], dx, dy)
    x1, y1 = x1 + ux * ARROW_GAP, y1 + uy * ARROW_GAP
    x2, y2 = clip_to_box(b[0], b[1], -dx, -dy)
    x2, y2 = x2 - ux * PULLBACK, y2 - uy * PULLBACK
    return x1, y1, x2, y2


def render(name: str, nodes: dict, edges: list) -> str:
    font_b64 = base64.b64encode(FONT_SOURCE.read_bytes()).decode("ascii")
    parts = [
        f'<svg width="{WIDTH}" height="{HEIGHT}" viewBox="0 0 {WIDTH} {HEIGHT}" '
        'fill="none" xmlns="http://www.w3.org/2000/svg" role="img" '
        f'aria-label="{escape(name)} DAG">',
        f'<rect width="{WIDTH}" height="{HEIGHT}" fill="white"/>',
        "<style>@font-face { font-family: 'Libre Franklin'; "
        f"src: url('data:font/woff2;base64,{font_b64}') format('woff2'); "
        "font-weight: 400 700; }</style>",
        '<defs><marker id="arrow" viewBox="0 0 5 5" refX="2.5" refY="2.5" '
        'markerWidth="5" markerHeight="5" markerUnits="strokeWidth" orient="auto">'
        f'<path d="M 0 0 L 5 2.5 L 0 5 z" fill="{STROKE}"/></marker></defs>',
    ]

    for src, dst in edges:
        x1, y1, x2, y2 = edge_path(nodes[src][:2], nodes[dst][:2])
        parts.append(
            f'<line x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}" '
            f'stroke="{STROKE}" stroke-width="{STROKE_WIDTH}" marker-end="url(#arrow)"/>'
        )

    for label, (cx, cy, fill) in nodes.items():
        text_fill = TEXT if fill == NEUTRAL else TEXT_ON_DARK
        parts.append(
            f'<rect x="{cx - NODE_W / 2:.1f}" y="{cy - NODE_H / 2:.1f}" '
            f'width="{NODE_W}" height="{NODE_H}" rx="6" fill="{fill}" '
            f'stroke="{STROKE}" stroke-width="{STROKE_WIDTH}"/>'
            f'<text x="{cx:.1f}" y="{cy:.1f}" fill="{text_fill}" '
            'font-family="Libre Franklin, Arial, sans-serif" font-size="44" '
            'font-weight="700" text-anchor="middle" dominant-baseline="central">'
            f"{escape(label)}</text>"
        )

    parts.append("</svg>")
    return "\n".join(parts)


# Discussion prompt: unknown causes of ridership. Blue matches the networkx DAGs
# rendered later in the Week 6 deck, so the answers slot into the same picture.
BLUE_FILL = "#DCE6F2"
BLUE_STROKE = "#33526E"
CTA_BLUE = "#00A1DE"
CIRCLE_R = 56
QUESTION_YS = (95, 240, 385, 530)
OUTCOME = (760, 309)
OUTCOME_W, OUTCOME_H = 250, 120


def render_question_dag() -> str:
    font_b64 = base64.b64encode(FONT_SOURCE.read_bytes()).decode("ascii")
    parts = [
        f'<svg width="{WIDTH}" height="{HEIGHT}" viewBox="0 0 {WIDTH} {HEIGHT}" '
        'fill="none" xmlns="http://www.w3.org/2000/svg" role="img" '
        'aria-label="Four unlabeled causes pointing at ridership">',
        f'<rect width="{WIDTH}" height="{HEIGHT}" fill="white"/>',
        "<style>@font-face { font-family: 'Libre Franklin'; "
        f"src: url('data:font/woff2;base64,{font_b64}') format('woff2'); "
        "font-weight: 400 700; }</style>",
        '<defs><marker id="arrow" viewBox="0 0 5 5" refX="2.5" refY="2.5" '
        'markerWidth="5" markerHeight="5" markerUnits="strokeWidth" orient="auto">'
        f'<path d="M 0 0 L 5 2.5 L 0 5 z" fill="{BLUE_STROKE}"/></marker></defs>',
    ]

    for cy in QUESTION_YS:
        cx = 190
        dx, dy = OUTCOME[0] - cx, OUTCOME[1] - cy
        length = (dx**2 + dy**2) ** 0.5
        ux, uy = dx / length, dy / length
        x1, y1 = cx + ux * (CIRCLE_R + ARROW_GAP), cy + uy * (CIRCLE_R + ARROW_GAP)
        sx = min((OUTCOME_W / 2) / abs(dx), (OUTCOME_H / 2) / abs(dy) if dy else 1e9)
        x2, y2 = OUTCOME[0] - dx * sx - ux * PULLBACK, OUTCOME[1] - dy * sx - uy * PULLBACK
        parts.append(
            f'<line x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}" '
            f'stroke="{BLUE_STROKE}" stroke-width="{STROKE_WIDTH}" marker-end="url(#arrow)"/>'
        )

    for cy in QUESTION_YS:
        parts.append(
            f'<circle cx="190" cy="{cy}" r="{CIRCLE_R}" fill="{BLUE_FILL}" '
            f'stroke="{BLUE_STROKE}" stroke-width="{STROKE_WIDTH}"/>'
            f'<text x="190" y="{cy}" fill="{BLUE_STROKE}" '
            'font-family="Libre Franklin, Arial, sans-serif" font-size="52" '
            'font-weight="700" text-anchor="middle" dominant-baseline="central">?</text>'
        )

    parts.append(
        f'<rect x="{OUTCOME[0] - OUTCOME_W / 2}" y="{OUTCOME[1] - OUTCOME_H / 2}" '
        f'width="{OUTCOME_W}" height="{OUTCOME_H}" rx="6" fill="{CTA_BLUE}" '
        f'stroke="{BLUE_STROKE}" stroke-width="{STROKE_WIDTH}"/>'
        f'<text x="{OUTCOME[0]}" y="{OUTCOME[1]}" fill="{TEXT_ON_DARK}" '
        'font-family="Libre Franklin, Arial, sans-serif" font-size="36" '
        'font-weight="700" text-anchor="middle" dominant-baseline="central">Ridership</text>'
    )
    parts.append("</svg>")
    return "\n".join(parts)


if __name__ == "__main__":
    for name, (nodes, edges) in FIGURES.items():
        path = OUT_DIR / f"{name}.svg"
        path.write_text(render(name, nodes, edges))
        print(f"wrote {path}")

    path = OUT_DIR / "ridership-unknown-causes.svg"
    path.write_text(render_question_dag())
    print(f"wrote {path}")
