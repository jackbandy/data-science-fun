#!/usr/bin/env python3
"""Bridges of Königsberg and Bridges of Shikaakwa, map -> graph in steps.

NOTICE: this file was substantially drafted by an LLM coding system and has not
yet been thoroughly reviewed.

Two parallel sets, each sharing one 1000 x 618 canvas so the frames line up in
an r-stack:

  konigsberg-v0.svg  the river and land, no bridges (redrawn after Euler's Fig. 1)
  konigsberg-v1.svg  + the seven bridges (Euler's a-g); land masses lettered by name
  konigsberg-v2.svg  + a node on each land mass, edges through the bridges; map faded
  konigsberg-v3.svg  the bare multigraph, with its adjacency matrix on the left
  konigsberg-v4.svg  + degrees (the matrix's row sums); odd ones in orange

  shikaakwa-v1.svg   Goose Island + Wolf Point stretch of the Chicago River with its walkable bridges, numbered, with a key; grey 'L' on Lake St
  shikaakwa-v2.svg   + nodes and edges over the faded map
  shikaakwa-v3.svg   + the multigraph beside the faded map
  shikaakwa-v4.svg   + degrees; odd-degree land masses in orange
  shikaakwa-v5.svg   one bridge closed (Halsted St over the North Branch) -> all even

Data:
  * Königsberg: the layout copies Euler's Fig. 1, hand-placed and schematic. Bridges
    keep Euler's letters a-g; land masses use name initials (Euler's letters in
    brackets): K Kneiphof (A), V Vorstadt (B), A Altstadt (C), L Lomse (D).
  * Shikaakwa: river centerlines are OpenStreetMap waterways (ODbL), clipped to
    the frame and simplified (Ramer-Douglas-Peucker, 6 m), hard-coded below with
    their way ids. Bridges come from shikaakwa-bridges.csv (rows with counted=yes),
    so edit that file, not the figures.
  * Captions are computed from the degrees, not typed by hand.

Usage:  python3 make_bridges_figures.py   (run in docs/slides/.venv, see SOURCES.md)
"""

from __future__ import annotations

import csv
import math
from collections import Counter
from pathlib import Path

import matplotlib

matplotlib.use("Agg")

import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
from matplotlib.patches import Circle, PathPatch, Rectangle
from matplotlib.path import Path as MPath

OUT_DIR = Path(__file__).resolve().parent
FONTS = OUT_DIR.parent / "fonts"
SMALL_FONT = FONTS / "libre-franklin" / "LibreFranklin-Regular.ttf"
TITLE_FONT = FONTS / "big-shoulders" / "BigShoulders-Bold.ttf"
TITLE_SIZE, SMALL_SIZE = 38, 15        # px
LINE = 22                               # px between lines of small text

PHI = (1 + 5**0.5) / 2
W, H = 1000, round(1000 / PHI)          # 1000 x 618
DPI = 100

PAPER = "#FFFFFF"
INK = "#111111"
TEXT = "#444444"
MUTED = "#777777"
QUIET = "#AAAAAA"
NEUTRAL = "#EEEEEE"
SOFT = "#F4F4F2"
BORDER = "#DDDDDD"
WATER = "#DADADA"                       # neutral gray: the river is an obstacle, not a feature
BANK = "#8A8A8A"
ORANGE = "#F9461C"
ORANGE_DARK = "#C83214"

FADE = 0.7                              # how far faded map layers mix toward white


# ---------------------------------------------------------------- helpers

def pt(px):
    """Pixels on the 1000 x 618 canvas -> matplotlib points."""
    return px * 72 / DPI


def fade(color, f):
    c = color.lstrip("#")
    r, g, b = (int(c[i:i + 2], 16) for i in (0, 2, 4))
    return "#{:02X}{:02X}{:02X}".format(*(round(v + (255 - v) * f) for v in (r, g, b)))


def text(ax, x, y, s, color=TEXT, title=False, **kw):
    """Only two text styles: the title, and one small style for everything else."""
    font = FontProperties(fname=str(TITLE_FONT if title else SMALL_FONT),
                          size=pt(TITLE_SIZE if title else SMALL_SIZE))
    kw.setdefault("zorder", 8)
    return ax.text(x, y, s, fontproperties=font, color=color, **kw)


def canvas():
    plt.rcParams["svg.fonttype"] = "path"
    fig = plt.figure(figsize=(W / DPI, H / DPI), dpi=DPI, facecolor=PAPER)
    ax = fig.add_axes((0, 0, 1, 1))
    ax.set_xlim(0, W)
    ax.set_ylim(H, 0)
    ax.set_aspect("equal")
    ax.axis("off")
    return fig, ax


def save(fig, name):
    out = OUT_DIR / f"{name}.svg"
    fig.savefig(out, format="svg", facecolor=PAPER)
    plt.close(fig)
    print(f"  wrote {out.name}")


def catmull(points, n=16):
    """Smooth a few control points into a polyline (Catmull-Rom)."""
    pts = [points[0], *points, points[-1]]
    out = []
    for i in range(1, len(pts) - 2):
        p0, p1, p2, p3 = pts[i - 1], pts[i], pts[i + 1], pts[i + 2]
        for j in range(n):
            t = j / n
            out.append(tuple(
                0.5 * (2 * p1[k] + (-p0[k] + p2[k]) * t
                       + (2 * p0[k] - 5 * p1[k] + 4 * p2[k] - p3[k]) * t * t
                       + (-p0[k] + 3 * p1[k] - 3 * p2[k] + p3[k]) * t ** 3)
                for k in (0, 1)))
    out.append(points[-1])
    return out


def locate(poly, p):
    """Nearest point on a polyline to p, and the unit tangent there."""
    best = None
    for a, b in zip(poly, poly[1:]):
        dx, dy = b[0] - a[0], b[1] - a[1]
        l2 = dx * dx + dy * dy or 1e-9
        t = max(0.0, min(1.0, ((p[0] - a[0]) * dx + (p[1] - a[1]) * dy) / l2))
        q = (a[0] + t * dx, a[1] + t * dy)
        d = math.dist(q, p)
        if best is None or d < best[0]:
            l = math.sqrt(l2)
            best = (d, q, (dx / l, dy / l))
    return best[1], best[2]


def draw_river(ax, channels, faded=False, clip=None):
    """channels: [(polyline, width_px)]. Banks first, then water, so confluences merge."""
    f = FADE if faded else 0
    for color, extra, z in ((BANK, 2.4, 1), (WATER, 0, 2)):
        for pts, w in channels:
            xs, ys = zip(*pts)
            (line,) = ax.plot(xs, ys, color=fade(color, f), lw=pt(w + extra),
                              solid_capstyle="round", solid_joinstyle="round", zorder=z)
            if clip is not None:
                line.set_clip_path(clip)


def draw_bridge(ax, center, tangent, water_w, lw=5, over=6, color=INK, dashed=False):
    nx, ny = -tangent[1], tangent[0]
    h = water_w / 2 + over
    ax.plot([center[0] - nx * h, center[0] + nx * h], [center[1] - ny * h, center[1] + ny * h],
            color=color, lw=pt(lw), solid_capstyle="butt", zorder=5,
            ls=(0, (1.2, 0.9)) if dashed else "-")
    return (nx, ny), h


def draw_node(ax, c, label, odd=False, r=20):
    fill, edge, ink = (ORANGE, ORANGE_DARK, PAPER) if odd else (NEUTRAL, INK, INK)
    ax.add_patch(Circle(c, r, facecolor=fill, edgecolor=edge, lw=pt(3), zorder=6))
    text(ax, c[0], c[1] + 1, label, color=ink,
         ha="center", va="center", zorder=7)


def draw_degree(ax, c, deg, r=20, odd=False):
    bx, by = c[0] + r * 0.85, c[1] - r * 0.85
    ax.add_patch(Circle((bx, by), 12.5, facecolor=PAPER,
                        edgecolor=ORANGE_DARK if odd else INK, lw=pt(1.5), zorder=8))
    text(ax, bx, by + 0.5, str(deg), color=ORANGE_DARK if odd else INK,
         ha="center", va="center", zorder=9)


def draw_edge(ax, p, q, offset=0.0, label=None, lw=3, color=INK, dashed=False,
              label_color=INK, faded=False):
    """Quadratic curve from p to q whose midpoint sits `offset` px off the chord."""
    mx, my = (p[0] + q[0]) / 2, (p[1] + q[1]) / 2
    dx, dy = q[0] - p[0], q[1] - p[1]
    length = math.hypot(dx, dy)
    nx, ny = -dy / length, dx / length
    ctrl = (mx + 2 * offset * nx, my + 2 * offset * ny)
    path = MPath([p, ctrl, q], [MPath.MOVETO, MPath.CURVE3, MPath.CURVE3])
    col = fade(color, FADE) if faded else color
    ax.add_patch(PathPatch(path, fill=False, edgecolor=col, lw=pt(lw), zorder=3,
                           ls=(0, (2, 1.6)) if dashed else "-", capstyle="round"))
    if label:
        text(ax, mx + offset * nx, my + offset * ny, label,
             color=label_color, ha="center", va="center", zorder=4,
             bbox=dict(boxstyle="round,pad=0.18", fc=PAPER, ec="none"))


def degrees(edges):
    deg = Counter()
    for u, v in edges:
        deg[u] += 1
        deg[v] += 1
    return deg


def lines(ax, x, y, rows, color=TEXT):
    for i, row in enumerate(rows):
        text(ax, x, y + i * LINE, row, color=color, va="baseline")


def title(ax, s, sub=None, x=24):
    text(ax, x, 50, s, color=INK, title=True, va="baseline")
    if sub:
        text(ax, x, 78, sub, color=MUTED, va="baseline")


def credit(ax, s):
    text(ax, W - 20, H - 12, s, color=MUTED, ha="right", va="baseline")


# ---------------------------------------------------------------- Königsberg

K_WATER = 24
K_WEST = catmull([(-30, 330), (120, 327), (215, 320)])
K_NORTH = catmull([(215, 320), (285, 215), (400, 172), (560, 172),
                   (652, 195), (770, 176), (890, 140), (1040, 104)])
K_SOUTH = catmull([(215, 320), (285, 432), (400, 474), (560, 474),
                   (652, 452), (770, 472), (890, 506), (1040, 540)])
K_LINK = catmull([(652, 195), (676, 323), (652, 452)])
K_CHANNELS = [(K_WEST, K_WATER), (K_NORTH, K_WATER), (K_SOUTH, K_WATER), (K_LINK, K_WATER)]

# Land masses get the first letter of their names (as in the Shikaakwa set):
# Kneiphof and Lomse are the islands, Altstadt and Vorstadt the mainland north and
# south. Euler's own letters were A = Kneiphof, B = Vorstadt, C = Altstadt, D = Lomse.
K_NAMES = {"A": "Altstadt", "K": "Kneiphof", "L": "Lomse", "V": "Vorstadt"}
K_ORDER = sorted(K_NAMES)

# bridge (Euler's letter): (channel, near point, endpoints, label side along the normal)
K_BRIDGES = {
    "a": (K_SOUTH, (325, 452), ("K", "V"), +1),
    "b": (K_SOUTH, (520, 476), ("K", "V"), +1),
    "c": (K_NORTH, (325, 192), ("K", "A"), -1),
    "d": (K_NORTH, (520, 170), ("K", "A"), -1),
    "e": (K_LINK, (676, 323), ("K", "L"), -1),
    "f": (K_SOUTH, (800, 478), ("V", "L"), +1),
    "g": (K_NORTH, (800, 170), ("A", "L"), -1),
}
K_LAND = {"A": (440, 110), "K": (440, 323), "L": (850, 323), "V": (440, 560)}
K_GRAPH = {"A": (600, 135), "K": (600, 320), "L": (860, 320), "V": (600, 505)}
# offsets put c left of d and a left of b, as in Euler's figure
K_OFFSETS = {"a": 46, "b": -46, "c": -46, "d": 46, "e": 0, "f": 0, "g": 0}
K_QUOTE = ("\u201c\u2026whether anyone could arrange a route in such a way that he would "
           "cross each bridge once and only once.\u201d \u2014 Euler (1736)")
K_CREDIT = "redrawn after Euler (1736), Fig. 1; quote trans. Biggs, Lloyd & Wilson (1976)"

# adjacency matrix, left of the graph
CELL = 40
MAT_X, MAT_Y = 64, 240                  # top-left of the first cell


def k_map(ax, bridges=True, labels=True, faded=False):
    draw_river(ax, K_CHANNELS, faded=faded)
    ink = fade(INK, FADE) if faded else INK
    ends = {}
    if bridges:
        for name, (chan, near, uv, side) in K_BRIDGES.items():
            c, tan = locate(chan, near)
            (nx, ny), h = draw_bridge(ax, c, tan, K_WATER, lw=10, over=8, color=ink)
            ends[name] = c
            if labels and not faded:
                text(ax, c[0] + side * nx * (h + 14), c[1] + side * ny * (h + 14), name,
                     color=INK, ha="center", va="center")
    if labels and not faded:
        for land, (x, y) in K_LAND.items():
            text(ax, x, y, f"{K_NAMES[land]} ({land})", color=MUTED, ha="center", va="center")
    return ends


def k_edges():
    return [uv for _, _, uv, _ in K_BRIDGES.values()]


def k_matrix(ax, deg=None):
    """Bridges between each pair of land masses; with deg, a row-sum (degree) column."""
    count = Counter()
    for u, v in k_edges():
        count[u, v] += 1
        count[v, u] += 1
    text(ax, 24, MAT_Y - 52, "Adjacency matrix: bridges between each pair",
         color=TEXT, va="baseline")
    for j, col in enumerate(K_ORDER):
        text(ax, MAT_X + (j + 0.5) * CELL, MAT_Y - 12, col, color=MUTED, ha="center",
             va="baseline")
    sum_x = MAT_X + len(K_ORDER) * CELL + 14
    if deg is not None:
        text(ax, sum_x + CELL / 2, MAT_Y - 12, "degree", color=MUTED, ha="center",
             va="baseline")
    for i, row in enumerate(K_ORDER):
        y = MAT_Y + i * CELL
        text(ax, MAT_X - 16, y + CELL / 2 + 1, row, color=MUTED, ha="center", va="center")
        for j, col in enumerate(K_ORDER):
            x = MAT_X + j * CELL
            n = count[row, col]
            ax.add_patch(Rectangle((x, y), CELL, CELL, facecolor=SOFT if i == j else PAPER,
                                   edgecolor=BORDER, lw=pt(1), zorder=2))
            text(ax, x + CELL / 2, y + CELL / 2 + 1, str(n), color=INK if n else QUIET,
                 ha="center", va="center")
        if deg is not None:
            odd = deg[row] % 2 == 1
            ax.add_patch(Rectangle((sum_x, y), CELL, CELL,
                                   facecolor=ORANGE if odd else NEUTRAL,
                                   edgecolor=ORANGE_DARK if odd else BORDER, lw=pt(1), zorder=2))
            text(ax, sum_x + CELL / 2, y + CELL / 2 + 1, str(deg[row]),
                 color=PAPER if odd else INK, ha="center", va="center")


def k_v0(ax):
    k_map(ax, bridges=False, labels=False)


def k_v1(ax):
    k_map(ax)


def k_v2(ax):
    ends = k_map(ax, faded=True)
    for name, (_, _, (u, v), _) in K_BRIDGES.items():
        b = ends[name]
        for land in (u, v):
            p = K_LAND[land]
            ax.plot([p[0], b[0]], [p[1], b[1]], color=INK, lw=pt(3), zorder=3,
                    solid_capstyle="round")
        text(ax, b[0] + 14, b[1] - 14, name, color=INK, ha="center", va="center",
             bbox=dict(boxstyle="round,pad=0.15", fc=PAPER, ec="none"))
    for land, c in K_LAND.items():
        draw_node(ax, c, land)


def k_graph(ax, show_degree=False):
    deg = degrees(k_edges())
    for name, (_, _, (u, v), _) in K_BRIDGES.items():
        draw_edge(ax, K_GRAPH[u], K_GRAPH[v], K_OFFSETS[name], label=name)
    for land, c in K_GRAPH.items():
        odd = show_degree and deg[land] % 2 == 1
        draw_node(ax, c, land, odd=odd)
        if show_degree:
            draw_degree(ax, c, deg[land], odd=odd)
        right = land == "L"
        text(ax, c[0] + (34 if right else -34), c[1], K_NAMES[land], color=MUTED,
             ha="left" if right else "right", va="center")
    return deg


def k_v3(ax):
    k_graph(ax)
    k_matrix(ax)
    lines(ax, 24, 560, ["4 land masses (nodes)", "7 bridges (edges)"])


def k_v4(ax):
    deg = k_graph(ax, show_degree=True)
    k_matrix(ax, deg)
    odd = [n for n in K_ORDER if deg[n] % 2]
    degs = ", ".join(f"{n} {deg[n]}" for n in K_ORDER)
    lines(ax, 24, 560, [
        f"Bridges touching each land mass: {degs}.",
        f"{len(odd)} land masses are odd, so no walk crosses every bridge exactly once.",
    ])


K_STEPS = {"v0": k_v0, "v1": k_v1, "v2": k_v2, "v3": k_v3, "v4": k_v4}


def make_konigsberg():
    for step, draw in K_STEPS.items():
        fig, ax = canvas()
        title(ax, "The Seven Bridges of Königsberg", K_QUOTE)
        draw(ax)
        credit(ax, K_CREDIT)
        save(fig, f"konigsberg-{step}")


# ---------------------------------------------------------------- Shikaakwa

# Frame (lat/lon) and where it lands on the canvas.
LAT_N, LAT_S = 41.9132, 41.8851
LON_W, LON_E = -87.6612, -87.6346
M_PER_DEG = 111_320
COS = math.cos(math.radians((LAT_N + LAT_S) / 2))
MAP_X, MAP_Y, MAP_H = 20, 16, 586
SCALE = MAP_H / ((LAT_N - LAT_S) * M_PER_DEG)                    # px per meter
MAP_W = (LON_E - LON_W) * COS * M_PER_DEG * SCALE


def proj(lat, lon):
    return (MAP_X + (lon - LON_W) * COS * M_PER_DEG * SCALE,
            MAP_Y + (LAT_N - lat) * M_PER_DEG * SCALE)


# OpenStreetMap waterway centerlines (lat, lon), split at the two Goose Island
# junctions and at Wolf Point.
S_RIVER = {
    # ways 1315569906 + 1315569907: North Branch above Goose Island
    "upper": [(41.91405, -87.65809), (41.91100, -87.65681), (41.91077, -87.65681),
              (41.91033, -87.65680)],
    # way 1317723635 + part of 164125005: North Branch, west of Goose Island
    "west": [(41.91033, -87.65680), (41.90909, -87.65744), (41.90827, -87.65782),
             (41.90486, -87.65822), (41.90398, -87.65787), (41.90256, -87.65650),
             (41.90146, -87.65613), (41.90118, -87.65591), (41.90076, -87.65529),
             (41.90038, -87.65414), (41.90007, -87.65206), (41.89977, -87.65143),
             (41.89825, -87.64933), (41.89814, -87.64905), (41.89799, -87.64806),
             (41.89776, -87.64505)],
    # way 1040130236: North Branch Canal, east of Goose Island
    "canal": [(41.91033, -87.65680), (41.91020, -87.65528), (41.91010, -87.65500),
              (41.90970, -87.65459), (41.90544, -87.65106), (41.90392, -87.64957),
              (41.90333, -87.64940), (41.90208, -87.64824), (41.90189, -87.64781),
              (41.90063, -87.64657), (41.89829, -87.64523), (41.89776, -87.64505)],
    # rest of 164125005 + 1317703968: North Branch down to Wolf Point
    "lower": [(41.89776, -87.64505), (41.89709, -87.64431), (41.89412, -87.64407),
              (41.89361, -87.64357), (41.89270, -87.64225), (41.89228, -87.64180),
              (41.89156, -87.64117), (41.89129, -87.64111), (41.89060, -87.64066),
              (41.88944, -87.63962), (41.88907, -87.63951), (41.88699, -87.63868),
              (41.88640, -87.63776)],
    # way 407267816: main stem, east from Wolf Point
    "main": [(41.88640, -87.63776), (41.88751, -87.63560), (41.88752, -87.63414)],
    # way 1308480104: South Branch, south from Wolf Point
    "south": [(41.88640, -87.63776), (41.88563, -87.63775), (41.88179, -87.63825)],
}
S_WIDTH = {"canal": 7}                  # the dug canal is narrower than the river
RIVER_W = 11
S_CHANNEL_OF = {"North Branch": ("upper", "west", "lower"), "North Branch Canal": ("canal",),
                "Main Stem": ("main",), "South Branch": ("south",)}

S_LAND = {  # node letter: (name, lat, lon of node / label)
    "G": ("Goose Island", 41.9043, -87.6536),
    "N": ("North Side", 41.9010, -87.6410),
    "W": ("West Side", 41.8935, -87.6540),
    "L": ("Loop", 41.8866, -87.6359),
}
S_GRAPH = {"G": (500, 175), "N": (740, 265), "W": (500, 405), "L": (740, 440)}
PANEL_X = 470                           # right-hand panel: title, prompt, caption
S_CLOSED = "6"                          # Halsted St over the North Branch, closed in v5
LAKE_ST_LAT = 41.88568                  # Green/Pink Line 'L' runs along Lake St
KEY_X, KEY_Y = 820, 150
S_CREDIT = "Map data © OpenStreetMap contributors (ODbL)"

# which side of the river each bridge's number goes on (+1 / -1 along the bridge)
S_LABEL_SIDE = {"1": +1, "2": -1, "3": -1, "4": +1, "5": +1, "6": -1, "7": +1,
                "8": +1, "9": +1, "10": -1, "11": +1}


def s_bridges():
    with open(OUT_DIR / "shikaakwa-bridges.csv", newline="", encoding="utf-8") as f:
        return [r for r in csv.DictReader(f) if r["counted"] == "yes"]


def s_place(row):
    """Snap a bridge to its channel: (center px, tangent, channel width)."""
    p = proj(float(row["lat"]), float(row["lon"]))
    best = None
    for name in S_CHANNEL_OF[row["crosses"]]:
        poly = [proj(*q) for q in S_RIVER[name]]
        c, tan = locate(poly, p)
        d = math.dist(c, p)
        if best is None or d < best[0]:
            best = (d, c, tan, S_WIDTH.get(name, RIVER_W))
    return best[1:]


def s_map(ax, bridges=True, labels=True, faded=False, closed=None):
    box = Rectangle((MAP_X, MAP_Y), MAP_W, MAP_H, transform=ax.transData)
    channels = [([proj(*q) for q in pts], S_WIDTH.get(name, RIVER_W))
                for name, pts in S_RIVER.items()]
    draw_river(ax, channels, faded=faded, clip=box)
    ax.add_patch(Rectangle((MAP_X, MAP_Y), MAP_W, MAP_H, fill=False,
                           edgecolor=fade(QUIET, FADE) if faded else QUIET, lw=pt(1), zorder=9))
    centers = {}
    if not bridges:
        if labels:
            s_land_labels(ax)
        return centers
    # the 'L' upper deck on Lake St: a nod to the course's transit motif, not a walking route
    y = proj(LAKE_ST_LAT, LON_W)[1]
    (track,) = ax.plot([MAP_X, MAP_X + MAP_W], [y, y], color=fade(QUIET, FADE) if faded else QUIET,
                       lw=pt(4), solid_capstyle="butt", zorder=4)
    track.set_clip_path(box)
    if not faded:
        text(ax, MAP_X + 6, y - 7, "Green & Pink Line ‘L’ (Lake St upper deck)", color=MUTED, va="baseline")
    for row in s_bridges():
        c, tan, w = s_place(row)
        centers[row["id"]] = c
        is_closed = row["id"] == closed
        color = QUIET if is_closed else (fade(INK, FADE) if faded else INK)
        (nx, ny), h = draw_bridge(ax, c, tan, w, lw=5, over=5, color=color, dashed=is_closed)
        if labels:
            side = S_LABEL_SIDE[row["id"]]
            ink = QUIET if (is_closed or faded) else INK
            text(ax, c[0] + side * nx * (h + 9), c[1] + side * ny * (h + 9), row["id"], color=ink, ha="center", va="center")
    if labels and not faded:
        s_land_labels(ax)
    return centers


def s_land_labels(ax):
    for name, lat, lon in S_LAND.values():
        x, y = proj(lat, lon)
        label = name.replace(" ", "\n") if name == "Goose Island" else name
        text(ax, x, y, label, color=MUTED, ha="center", va="center")


def s_key(ax, closed=None):
    text(ax, KEY_X, KEY_Y - 22, "Bridges", color=INK, va="baseline")
    rows = s_bridges()
    names = Counter(r["bridge"] for r in rows)
    for i, r in enumerate(rows):
        y = KEY_Y + i * LINE
        name = r["bridge"]
        if names[name] > 1:
            name += " (canal)" if "Canal" in r["crosses"] else " (river)"
        col = QUIET if r["id"] == closed else TEXT
        text(ax, KEY_X + 18, y, r["id"], color=INK if col == TEXT else col,
             ha="right", va="baseline")
        t = text(ax, KEY_X + 28, y, name, color=col, va="baseline")
        if r["id"] == closed:               # strike through: the bridge is out of the walk
            bb = t.get_window_extent(ax.figure.canvas.get_renderer())
            x0, x1 = (ax.transData.inverted().transform((bx, 0))[0] for bx in (bb.x0, bb.x1))
            ax.plot([x0 - 2, x1 + 2], [y - 5.5, y - 5.5], color=QUIET, lw=pt(1.5), zorder=9)


def s_edges(closed=None):
    return [(r["from"], r["to"]) for r in s_bridges() if r["id"] != closed]


def s_graph(ax, show_degree=False, closed=None):
    rows = s_bridges()
    groups = {}
    for r in rows:
        groups.setdefault(frozenset((r["from"], r["to"])), []).append(r)
    spacing = 34
    for group in groups.values():
        k = len(group)
        u, v = group[0]["from"], group[0]["to"]     # one direction per group, so offsets fan out
        for i, r in enumerate(group):
            offset = (i - (k - 1) / 2) * spacing
            is_closed = r["id"] == closed
            draw_edge(ax, S_GRAPH[u], S_GRAPH[v], offset, label=r["id"],
                      color=QUIET if is_closed else INK, dashed=is_closed,
                      label_color=QUIET if is_closed else INK)
    deg = degrees(s_edges(closed))
    for land, c in S_GRAPH.items():
        odd = show_degree and deg[land] % 2 == 1
        draw_node(ax, c, land, odd=odd)
        if show_degree:
            draw_degree(ax, c, deg[land], odd=odd)
        above = land in ("G", "N")
        dx = 22 if land == "N" else 0     # clear of the G-N edges arriving from the left
        text(ax, c[0] + dx, c[1] + (-34 if above else 38), S_LAND[land][0], color=MUTED,
             ha="center", va="center")
    return deg


def s_nodes_on_map(ax, centers):
    nodes = {land: proj(lat, lon) for land, (_, lat, lon) in S_LAND.items()}
    for r in s_bridges():
        b = centers[r["id"]]
        for land in (r["from"], r["to"]):
            p = nodes[land]
            ax.plot([p[0], b[0]], [p[1], b[1]], color=INK, lw=pt(1.8), zorder=6,
                    solid_capstyle="round")
    for land, c in nodes.items():
        draw_node(ax, c, land, r=12 if land == "L" else 13)


def s_status(deg):
    odd = sorted(n for n in deg if deg[n] % 2)
    degs = ", ".join(f"{n} {deg[n]}" for n in ("W", "N", "G", "L"))
    if not odd:
        verdict = ["Every land mass is even, so one walk can cross every",
                   "bridge exactly once and end where it started."]
    elif len(odd) == 2:
        a, b = (S_LAND[n][0] for n in odd)
        verdict = [f"Two are odd: a walk can cross every bridge once if it starts",
                   f"on {a} or {b} and ends on the other, but not as a loop."]
    else:
        verdict = [f"{len(odd)} land masses are odd, so no walk crosses every bridge once."]
    return [f"Bridges per land mass: {degs}.", *verdict]


def s_v1(ax):
    s_map(ax)
    s_key(ax)
    lines(ax, PANEL_X, 280, ["Can you walk across", "every bridge exactly once?"],
          color=INK)


def s_v2(ax):
    centers = s_map(ax, faded=True)
    s_nodes_on_map(ax, centers)
    s_key(ax)
    n = len(s_bridges())
    lines(ax, PANEL_X, 280, [f"{len(S_LAND)} land masses (nodes)", f"{n} bridges (edges)"], color=INK)


def s_v3(ax):
    s_map(ax, faded=True)
    s_key(ax)
    s_graph(ax)


def s_v4(ax):
    s_map(ax, faded=True)
    s_key(ax)
    deg = s_graph(ax, show_degree=True)
    text(ax, PANEL_X, 518, s_status(deg)[0], color=TEXT, va="baseline")
    lines(ax, PANEL_X, 518 + LINE, s_status(deg)[1:], color=INK)


def s_v5(ax):
    s_map(ax, faded=True, closed=S_CLOSED)
    centers = {r["id"]: s_place(r) for r in s_bridges()}
    c, tan, w = centers[S_CLOSED]
    draw_bridge(ax, c, tan, w, lw=5, over=5, color=QUIET, dashed=True)
    s_key(ax, closed=S_CLOSED)
    deg = s_graph(ax, show_degree=True, closed=S_CLOSED)
    text(ax, PANEL_X, 518, s_status(deg)[0], color=TEXT, va="baseline")
    lines(ax, PANEL_X, 518 + LINE, s_status(deg)[1:], color=INK)


S_STEPS = {"v1": s_v1, "v2": s_v2, "v3": s_v3, "v4": s_v4, "v5": s_v5}


def make_shikaakwa():
    for step, draw in S_STEPS.items():
        fig, ax = canvas()
        title(ax, "The Bridges of Shikaakwa",
              "Goose Island and Wolf Point on the Chicago River", x=PANEL_X)
        draw(ax)
        credit(ax, S_CREDIT)
        save(fig, f"shikaakwa-{step}")


def main():
    make_konigsberg()
    make_shikaakwa()


if __name__ == "__main__":
    main()
