#!/usr/bin/env python3
"""Simplified redraws of Cheryl Warrick's *Mid Century II*, built up in steps.

NOTICE: this file was substantially drafted by an LLM coding system and has not
yet been thoroughly reviewed.

The painting reads as a network: black ink dots (nodes) joined by ink lines
(edges), each dot sitting on a watercolor blob. The frames peel it back to that
graph and rebuild it:

  * warrick-mid-century-v0.svg  every black dot, all one size (unweighted nodes)
  * warrick-mid-century-v1.svg  the dots resized as painted (weighted nodes)
  * warrick-mid-century-v2.svg  + straight-line edges, all one width (unweighted edges)
  * warrick-mid-century-v3.svg  the edges at their painted widths (weighted edges)
  * warrick-mid-century-v4.svg  + the colored blobs under them

Every frame carries the credit "based on Cheryl Warrick, Mid Century II" in the
bottom-right corner, and all frames share one canvas so they line up pixel for
pixel in an r-stack.

Data: positions, sizes, and colors were read off the full-composition image,
`docs/assets/art/warrick_mid_century_ii.jpg` (900 x 602; see
`docs/assets/art/SOURCES.md`), and are hard-coded below in that image's pixel
coordinates, so this script does not need the image to run.
  * Dots: centers and radii from a distance transform of the ink, checked by eye.
    All dots are filled: the painting's tiny loop and spiral (nodes 28 and 30)
    are simplified to small dots, and the line that ends inside the dark teal
    blob with no dot gets one (node 43) at the blob's center.
  * Edges: every ink line between two nodes, straightened. Widths come in three
    classes measured from the stroke: thin, medium, and thick (the bars).
  * Blobs: one ellipse per watercolor wash; colors are the median paint color
    inside each wash, geometry is approximate.

Canvas: golden ratio, 1000 x 618 (docs/assets/STYLE.md). The painting is 3:2,
so the layout is stretched about 13% horizontally to fill the frame; dot and
blob sizes use the vertical scale only, so circles stay round.

Usage:  python3 make_warrick_figures.py
"""

from __future__ import annotations

from pathlib import Path

import matplotlib

matplotlib.use("Agg")

import matplotlib.pyplot as plt
from matplotlib import font_manager
from matplotlib.patches import Circle, Ellipse

OUT_DIR = Path(__file__).resolve().parent
FONT_PATH = OUT_DIR.parent / "fonts" / "libre-franklin" / "LibreFranklin-Regular.ttf"

PHI = (1 + 5**0.5) / 2
W, H = 1000, round(1000 / PHI)          # 1000 x 618
DPI = 100

PAPER = "#FFFFFF"
INK = "#1E2420"                         # the painting's ink: a green-tinged black
MUTED = "#777777"                       # the credit line, quiet like a footnote

CREDIT = "based on Cheryl Warrick, Mid Century II"

# Source image box (900 x 602) -> frame, leaving a strip at the bottom for the credit.
SRC_W, SRC_H = 900, 602
LEFT, RIGHT, TOP, BOTTOM = 24, 24, 16, 40
SX = (W - LEFT - RIGHT) / SRC_W
SY = (H - TOP - BOTTOM) / SRC_H


def to_frame(x, y):
    return LEFT + x * SX, TOP + y * SY


# id: (x, y, radius)
NODES = {
    1: (90, 50, 5),      2: (218, 68, 13),    3: (89, 134, 7),
    4: (172, 132, 9),    5: (219, 134, 9),    6: (98, 230, 14),
    7: (223, 236, 12.5), 8: (331, 210, 14),   9: (355, 41, 12),
    10: (363, 113, 12),  11: (460, 24, 10),   12: (595, 34, 13),
    13: (462, 81, 13),   14: (589, 98, 11),   15: (833, 35, 9.5),
    16: (704, 100, 11.5), 17: (826, 110, 5),  18: (727, 188, 12),
    19: (839, 231, 12),  20: (848, 296, 12.5), 21: (461, 178, 6),
    22: (466, 265, 14),  23: (590, 213, 12),  24: (730, 306, 13),
    25: (97, 338, 10),   26: (221, 347, 12.5), 27: (353, 379, 12.5),
    28: (478, 370, 5),  29: (312, 461, 12),  30: (300, 549, 6),
    31: (71, 431, 11.5), 32: (202, 453, 6),   33: (54, 544, 12),
    34: (203, 564, 12),  35: (613, 322, 5),   36: (619, 431, 12.5),
    37: (502, 442, 11),  38: (447, 522, 11),  39: (597, 541, 12),
    40: (720, 542, 14),  41: (840, 412, 12),  42: (840, 526, 11.5),
    43: (745, 410, 12),
}

PLAIN_R = 10                            # one radius for every dot in the unweighted frame
PLAIN_W = 3.0                           # one width for every edge in the unweighted frames
THIN, MEDIUM, THICK = 2.2, 4.0, 13.0    # stroke widths in source pixels
EDGES = [
    # thick bars
    (6, 7, THICK), (10, 13, THICK), (11, 12, THICK), (12, 14, THICK),
    (24, 41, THICK), (36, 39, THICK), (27, 29, THICK), (33, 32, THICK),
    # medium lines
    (8, 27, MEDIUM), (11, 13, MEDIUM), (29, 30, MEDIUM), (31, 32, MEDIUM), (32, 34, MEDIUM),
    # thin lines
    (1, 2, THIN), (1, 3, THIN), (3, 6, THIN), (7, 26, THIN), (5, 8, THIN),
    (8, 21, THIN), (8, 22, THIN), (9, 11, THIN), (15, 17, THIN), (16, 17, THIN),
    (17, 18, THIN), (17, 19, THIN), (23, 35, THIN), (35, 24, THIN), (35, 36, THIN),
    (35, 43, THIN), (41, 40, THIN), (39, 40, THIN), (39, 37, THIN), (39, 38, THIN),
    (27, 28, THIN),
]

# (center x, center y, half-width, half-height, rotation in degrees, color), source pixels.
BLOBS = [
    (95, 42, 50, 32, 0, "#D0BF47"),     # yellow, top left
    (205, 55, 52, 27, 5, "#97A284"),    # gray green
    (85, 123, 40, 40, 0, "#92A287"),    # gray green
    (198, 128, 62, 40, 5, "#62B07C"),   # green, two dots
    (90, 228, 65, 52, 0, "#9EA379"),    # olive
    (218, 228, 48, 45, 0, "#B4CF80"),   # light green
    (90, 338, 42, 52, 0, "#D88D48"),    # orange
    (222, 338, 62, 50, 0, "#C3874F"),   # brown orange
    (75, 440, 52, 37, 0, "#E8979A"),    # pink
    (203, 435, 45, 60, 0, "#C7B541"),   # mustard
    (75, 540, 58, 47, -8, "#E08E9E"),   # pink, bottom left
    (200, 555, 40, 42, 0, "#5C8289"),   # slate blue
    (350, 40, 52, 25, 5, "#E5513E"),    # red, top
    (360, 108, 75, 45, 5, "#C44D42"),   # red
    (480, 75, 52, 38, 10, "#D59EA8"),   # pink
    (332, 252, 42, 85, 0, "#5AAAB3"),   # cyan blue, tall
    (480, 165, 52, 33, 0, "#80BD73"),   # green
    (468, 268, 65, 55, 0, "#59A464"),   # green
    (355, 368, 62, 48, 0, "#5EA194"),   # teal
    (490, 368, 68, 36, 0, "#81B8B0"),   # light blue
    (310, 462, 55, 40, 0, "#A8CDB4"),   # pale teal
    (300, 545, 62, 32, 0, "#86C683"),   # green, bottom
    (470, 447, 55, 42, 0, "#D1D2BA"),   # pale gray
    (455, 525, 75, 38, -5, "#D6B031"),  # yellow, bottom
    (590, 30, 45, 20, 0, "#E15B4E"),    # red, under the top bar
    (590, 105, 55, 50, 0, "#C4504B"),   # crimson
    (592, 210, 60, 55, 0, "#52929B"),   # blue
    (612, 325, 42, 55, 0, "#9C7490"),   # purple
    (620, 440, 62, 48, 0, "#DC4243"),   # red
    (600, 530, 62, 45, 0, "#CD8A9B"),   # pink
    (713, 36, 45, 22, 5, "#E5C036"),    # yellow, top
    (708, 98, 55, 45, 0, "#BEB740"),    # olive yellow
    (720, 185, 50, 32, 5, "#48A488"),   # teal
    (733, 280, 52, 58, 0, "#4AA287"),   # teal
    (745, 410, 58, 58, 0, "#3E8576"),   # dark teal
    (735, 535, 62, 50, 0, "#D94B3C"),   # red, bottom
    (825, 45, 45, 28, 15, "#49A872"),   # green, top right
    (822, 120, 52, 48, 0, "#779192"),   # gray blue
    (840, 262, 42, 75, 0, "#D04940"),   # red, tall
    (850, 405, 45, 58, 0, "#D57347"),   # orange
    (840, 520, 32, 47, 0, "#E1A55A"),   # orange, small
]


def canvas():
    font_manager.fontManager.addfont(str(FONT_PATH))
    plt.rcParams["font.family"] = font_manager.FontProperties(fname=str(FONT_PATH)).get_name()
    plt.rcParams["svg.fonttype"] = "path"
    fig = plt.figure(figsize=(W / DPI, H / DPI), dpi=DPI, facecolor=PAPER)
    ax = fig.add_axes((0, 0, 1, 1))
    ax.set_xlim(0, W)
    ax.set_ylim(H, 0)
    ax.set_aspect("equal")
    ax.axis("off")
    return fig, ax


def draw_blobs(ax):
    for x, y, rx, ry, angle, color in BLOBS:
        cx, cy = to_frame(x, y)
        ax.add_patch(Ellipse((cx, cy), 2 * rx * SY, 2 * ry * SY, angle=angle,
                             facecolor=color, edgecolor="none", zorder=1))


def draw_edges(ax, weighted=True):
    for u, v, width in EDGES:
        (x0, y0), (x1, y1) = to_frame(*NODES[u][:2]), to_frame(*NODES[v][:2])
        width = width if weighted else PLAIN_W
        # linewidth is in points; 1 source px * SY frame px = SY * 72 / DPI points
        ax.plot([x0, x1], [y0, y1], color=INK, lw=width * SY * 72 / DPI,
                solid_capstyle="round", zorder=2)


def draw_dots(ax, weighted=True):
    for x, y, r in NODES.values():
        cx, cy = to_frame(x, y)
        r = r if weighted else PLAIN_R
        ax.add_patch(Circle((cx, cy), r * SY, facecolor=INK, edgecolor="none", zorder=3))


def plain_dots(ax):
    draw_dots(ax, weighted=False)


def plain_edges(ax):
    draw_edges(ax, weighted=False)


def credit(ax):
    ax.text(W - RIGHT, H - 14, CREDIT, ha="right", va="baseline", fontsize=11, color=MUTED)


def save(fig, name):
    out = OUT_DIR / f"{name}.svg"
    fig.savefig(out, format="svg", facecolor=PAPER)
    plt.close(fig)
    print(f"  wrote {out.name}")


STEPS = {
    "v0": (plain_dots,),
    "v1": (draw_dots,),
    "v2": (plain_edges, draw_dots),
    "v3": (draw_edges, draw_dots),
    "v4": (draw_blobs, draw_edges, draw_dots),
}


def main():
    for step, layers in STEPS.items():
        fig, ax = canvas()
        for layer in layers:
            layer(ax)
        credit(ax)
        save(fig, f"warrick-mid-century-{step}")


if __name__ == "__main__":
    main()
