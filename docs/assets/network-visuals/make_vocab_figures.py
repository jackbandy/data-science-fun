#!/usr/bin/env python3
"""Graph vocabulary figures for the Week 12 vocab slides (Days 1 and 2).

NOTICE: this file was substantially drafted by an LLM coding system and has not
yet been reviewed. Check every figure against the slide it illustrates.

Most figures reuse the running example from Leskovec, Rajaraman & Ullman,
*Mining of Massive Datasets* (3rd ed.), Ch. 10, Fig. 10.1: seven people A-G and
nine friendships. Its adjacency matrix (Fig. 10.13), degree matrix (Fig. 10.14),
and neighborhoods of A (Example 10.26) match the book, so students can check
the slides against the reading.

  * vocab-graph.svg              nodes, edges, degree, plus a self-loop at C (MMDS Fig. 10.1)
  * vocab-directed.svg           a toy directed, weighted graph; in- and out-degree
  * vocab-neighborhood-v0..v3    N(A, d) for d = 0..3 (MMDS Example 10.26)
  * vocab-closure-v0, v1         a toy directed graph, then its transitive closure
  * vocab-matrices.svg           adjacency and degree matrices (MMDS Figs. 10.13-10.14)
  * vocab-communities.svg        MMDS Fig. 10.1 as two communities, with densities
  * vocab-overlap.svg            two overlapping communities (based on MMDS Fig. 10.19)
  * vocab-bipartite-v0, v1       K_{3,2} alone, then inside a dense community
  * vocab-triadic-v0, v1         worksheet checkpoint 5's friendship graph, then its shared-friend counts

Shares the 900 x 700 split-slide canvas and helpers of make_project_network_figures.py.

Usage:  python3 make_vocab_figures.py [figure-name ...]   (run in docs/slides/.venv)
"""
from __future__ import annotations

import math
import sys
from itertools import combinations

import matplotlib.pyplot as plt
from matplotlib import font_manager
from matplotlib.patches import Circle, Ellipse, Rectangle

import make_project_network_figures as base
from make_project_network_figures import (
    BORDER,
    CIRCLE,
    INK,
    ORANGE,
    PAPER,
    QUIET,
    SOFT_GRAY,
    STEEL,
    callout,
    canvas,
    edge,
    mid,
    side_label,
)

LIGHT_ORANGE = "#FDD9CF"   # ORANGE faded 80% toward white

FIGURES: dict[str, callable] = {}


def figure(name: str):
    def wrap(fn):
        FIGURES[name] = fn
        return fn
    return wrap


# MMDS Fig. 10.1: B is friends with A, C, and D (Example 10.1).
MMDS_POS = {"A": (1.0, 6.0), "B": (4.0, 6.0), "D": (6.6, 6.0), "E": (9.4, 6.0),
            "C": (2.5, 2.8), "G": (6.6, 2.8), "F": (9.4, 2.8)}
MMDS_EDGES = [("A", "B"), ("A", "C"), ("B", "C"), ("B", "D"), ("D", "E"),
              ("D", "F"), ("D", "G"), ("E", "F"), ("F", "G")]
ORDER = "ABCDEFG"


def dots(ax, pos, names, *, fill=None, size=CIRCLE, fontsize=15):
    """Labeled circles; `fill` maps a name to 'steel' (default), 'orange', or 'hollow'."""
    fill = fill or {}
    for n in names:
        kind = fill.get(n, "steel")
        face = {"steel": STEEL, "orange": ORANGE, "hollow": PAPER}[kind]
        rim = INK if kind == "hollow" else PAPER
        ax.scatter(*pos[n], marker="o", s=size, color=face, edgecolor=rim,
                   lw=2.0 if kind == "hollow" else 1.2, zorder=3)
        ax.text(*pos[n], n, ha="center", va="center_baseline", fontsize=fontsize,
                color=INK if kind == "hollow" else PAPER, zorder=4)


def degree(edges, n):
    return sum(n in e for e in edges)


def bfs(edges, start):
    """Distance from `start` to every reachable node, treating edges as undirected."""
    nbrs = {}
    for a, b in edges:
        nbrs.setdefault(a, set()).add(b)
        nbrs.setdefault(b, set()).add(a)
    dist, frontier = {start: 0}, [start]
    while frontier:
        nxt = []
        for u in frontier:
            for v in sorted(nbrs[u]):
                if v not in dist:
                    dist[v] = dist[u] + 1
                    nxt.append(v)
        frontier = nxt
    return dist


def node_note(ax, xy, s, color=STEEL):
    """A small note above a top-row node, or below a bottom-row one, clear of its edges."""
    x, y = xy
    top = y > 4
    side_label(ax, (x, y + (0.62 if top else -0.62)), s, ha="center",
               va="bottom" if top else "top", color=color)


def footer(ax, lines, y=0.9, x=0.2, color=INK):
    for i, s in enumerate(lines):
        ax.text(x, y - 0.55 * i, s, ha="left", va="center", fontsize=15, color=color, zorder=5)


# ------------------------------------------------------------------ figures

# The self-loop is not in MMDS Fig. 10.1; it only illustrates the term on the slide.
LOOP_NODE, LOOP_ANGLE = "C", 200


@figure("vocab-graph")
def graph():
    fig, ax = canvas("A small social network: 7 nodes, 10 edges",
                     "Based on MMDS Fig. 10.1, plus a self-loop at C. Gray number = the node's degree")
    for a, b in MMDS_EDGES:
        on_d = "D" in (a, b)
        edge(ax, MMDS_POS, a, b, lw=3.0 if on_d else 2.0, color=ORANGE if on_d else QUIET,
             zorder=2 if on_d else 1)
    x, y = MMDS_POS[LOOP_NODE]
    t = math.radians(LOOP_ANGLE)
    ax.add_patch(Circle((x + 0.55 * math.cos(t), y + 0.55 * math.sin(t)), 0.4, fill=False,
                        edgecolor=QUIET, lw=2.0, zorder=1))
    side_label(ax, (x - 1.15, y - 0.75), "self-loop", ha="center", va="top", color=STEEL)
    dots(ax, MMDS_POS, ORDER, fill={"D": "orange"})
    for n, (x, y) in MMDS_POS.items():
        # A self-loop touches its node twice, so it adds 2 to the degree.
        d = degree(MMDS_EDGES, n) + (2 if n == LOOP_NODE else 0)
        node_note(ax, (x, y), str(d), color=ORANGE if n == "D" else STEEL)
    callout(ax, mid(MMDS_POS, "D", "G", 0.5), "D has degree 4:\nfour edges", (4.3, 1.4))
    return fig


@figure("vocab-directed")
def directed():
    pos = {"A": (1.2, 5.8), "B": (1.6, 1.6), "C": (5.0, 3.8), "D": (4.6, 0.6),
           "E": (8.8, 5.6), "F": (8.6, 1.6)}
    arcs = {("A", "C"): 3, ("B", "C"): 1, ("D", "C"): 2, ("C", "E"): 4,
            ("E", "A"): 1, ("B", "D"): 2, ("E", "F"): 3}
    fig, ax = canvas("Directed and weighted",
                     "Arrow = direction; width and number = weight")
    for (a, b), w in arcs.items():
        on_c = "C" in (a, b)
        rad = -0.18 if (a, b) == ("E", "A") else 0.0
        edge(ax, pos, a, b, arrow=True, lw=1.4 * w, color=ORANGE if on_c else QUIET,
             rad=rad, zorder=2 if on_c else 1)
        (x0, y0), (x1, y1) = pos[a], pos[b]
        # arc3 bows by rad * length; the curve's midpoint sits halfway to its control point.
        x, y = (x0 + x1) / 2 + rad * (y1 - y0) / 2, (y0 + y1) / 2 - rad * (x1 - x0) / 2
        ax.text(x, y, str(w), ha="center", va="center", fontsize=14, color=INK, zorder=5,
                bbox=dict(boxstyle="square,pad=0.15", facecolor=PAPER, edgecolor="none"))
    dots(ax, pos, pos, fill={"C": "orange"})
    callout(ax, (pos["C"][0] + 0.3, pos["C"][1] - 0.3), "C: in-degree 3,\nout-degree 1",
            (7.3, 3.4))
    return fig


def neighborhood(d):
    dist = bfs(MMDS_EDGES, "A")
    inside = sorted(n for n, k in dist.items() if k <= d)
    fig, ax = canvas(f"The neighborhood of radius {d} around A",
                     "Orange = reachable from A along a path of length at most "
                     f"{d}")
    for a, b in MMDS_EDGES:
        both = a in inside and b in inside
        edge(ax, MMDS_POS, a, b, lw=3.0 if both else 2.0, color=ORANGE if both else QUIET,
             zorder=2 if both else 1)
    dots(ax, MMDS_POS, ORDER, fill={n: "orange" if n in inside else "hollow" for n in ORDER})
    for n, (x, y) in MMDS_POS.items():
        if dist[n] <= d:
            node_note(ax, (x, y), f"{dist[n]} step" + ("" if dist[n] == 1 else "s"))
    profile = [sum(k <= r for k in dist.values()) for r in range(1, d + 1)]
    lines = [f"N(A, {d}) = {{{', '.join(inside)}}}"]
    lines.append("Neighborhood profile of A: " + (", ".join(map(str, profile)) if profile
                                                  else "starts at radius 1"))
    if len(inside) == len(ORDER):
        lines.append("Diameter: 3. Every node reaches every other in 3 steps or fewer")
    footer(ax, lines, y=1.4 if len(lines) == 3 else 1.1)
    return fig


for _d in range(4):
    FIGURES[f"vocab-neighborhood-v{_d}"] = (lambda d=_d: neighborhood(d))


CLOSURE_POS = {"A": (1.0, 6.0), "B": (4.4, 6.0), "C": (8.0, 6.0), "D": (8.0, 2.6),
               "E": (4.4, 2.6)}
CLOSURE_ARCS = [("A", "B"), ("B", "C"), ("C", "B"), ("C", "D"), ("E", "D")]


def reach(arcs):
    out = {}
    for a, b in arcs:
        out.setdefault(a, set()).add(b)
    pairs = set()
    for v in CLOSURE_POS:
        seen, stack = set(), [v]
        while stack:
            for u in out.get(stack.pop(), ()):
                if u not in seen:
                    seen.add(u)
                    stack.append(u)
        pairs |= {(v, u) for u in seen if u != v}
    return sorted(pairs)


def closure(show):
    fig, ax = canvas("Reachability and transitive closure",
                     "Solid arrow = an edge; dashed = reachable, but not an edge"
                     if show else "Five directed edges. Who can reach whom?")
    pairs = reach(CLOSURE_ARCS)
    for a, b in CLOSURE_ARCS:
        rad = 0.25 if {a, b} == {"B", "C"} else 0.0
        edge(ax, CLOSURE_POS, a, b, arrow=True, lw=2.5, color=INK, rad=rad)
    added = [p for p in pairs if p not in CLOSURE_ARCS]
    if show:
        for a, b in added:
            rad = -0.45 if (a, b) == ("A", "C") else 0.0
            ax.annotate("", xy=CLOSURE_POS[b], xytext=CLOSURE_POS[a], zorder=2,
                        arrowprops=dict(arrowstyle="-|>,head_length=0.7,head_width=0.4",
                                        color=ORANGE, lw=2.5, ls=(0, (4, 3)),
                                        shrinkA=base.radius_pts(CIRCLE) + 1,
                                        shrinkB=base.radius_pts(CIRCLE) + 4,
                                        connectionstyle=f"arc3,rad={rad}",
                                        mutation_scale=16))
        footer(ax, [f"{len(pairs)} pairs (v, u) where v can reach u, {len(added)} not edges:",
                    "  ".join(f"({a}, {b})" for a, b in pairs),
                    "D reaches no one: every arrow at D points in"], y=1.4)
    else:
        footer(ax, ["Which nodes can A reach? Which can D reach?"], y=1.1)
    dots(ax, CLOSURE_POS, CLOSURE_POS)
    return fig


FIGURES["vocab-closure-v0"] = lambda: closure(False)
FIGURES["vocab-closure-v1"] = lambda: closure(True)


def draw_matrix(ax, x0, y_top, cell, title, value, highlight="D"):
    """A 7 x 7 matrix in MMDS order, the `highlight` row in orange."""
    ax.text(x0, y_top + 1.05, title, ha="left", va="center", fontsize=15, color=INK)
    for j, c in enumerate(ORDER):
        ax.text(x0 + (j + 0.5) * cell, y_top + 0.3, c, ha="center", va="center",
                fontsize=12, color=STEEL)
    for i, r in enumerate(ORDER):
        y = y_top - (i + 1) * cell
        hot = r == highlight
        ax.text(x0 - 0.25, y + cell / 2, r, ha="center", va="center", fontsize=12,
                color=ORANGE if hot else STEEL)
        for j, c in enumerate(ORDER):
            v = value(r, c)
            face = LIGHT_ORANGE if hot else (SOFT_GRAY if i == j else PAPER)
            ax.add_patch(Rectangle((x0 + j * cell, y), cell, cell, facecolor=face,
                                   edgecolor=BORDER, lw=1.0, zorder=1))
            ax.text(x0 + (j + 0.5) * cell, y + cell / 2, str(v), ha="center",
                    va="center_baseline", fontsize=13, zorder=2,
                    color=(INK if v else QUIET) if not hot else (ORANGE if v else QUIET))


@figure("vocab-matrices")
def matrices():
    pos = {"A": (1.4, 7.0), "B": (3.8, 7.0), "D": (6.2, 7.0), "E": (8.6, 7.0),
           "C": (2.6, 5.3), "G": (6.2, 5.3), "F": (8.6, 5.3)}
    fig, ax = canvas("The same 7 nodes, as matrices",
                     "Based on MMDS Figs. 10.13 and 10.14. Rows and columns in order A to G")
    for a, b in MMDS_EDGES:
        on_d = "D" in (a, b)
        edge(ax, pos, a, b, lw=2.5 if on_d else 1.6, color=ORANGE if on_d else QUIET,
             size_a=500, size_b=500, zorder=2 if on_d else 1)
    dots(ax, pos, ORDER, fill={"D": "orange"}, size=500, fontsize=13)
    adj = {frozenset(e) for e in MMDS_EDGES}
    cell = 0.46
    draw_matrix(ax, 0.6, 3.45, cell, "Adjacency matrix A",
                lambda r, c: int(frozenset((r, c)) in adj))
    draw_matrix(ax, 6.2, 3.45, cell, "Degree matrix D",
                lambda r, c: degree(MMDS_EDGES, r) if r == c else 0)
    return fig


@figure("vocab-communities")
def communities():
    fig, ax = canvas("Two communities", "Shaded groups have far more edges inside than between")
    for (cx, cy), w, h in [((2.45, 4.75), 5.0, 4.9), ((8.0, 4.4), 4.6, 5.2)]:
        ax.add_patch(Ellipse((cx, cy), w, h, facecolor=SOFT_GRAY, edgecolor=BORDER, lw=1.5,
                             zorder=0))
    for a, b in MMDS_EDGES:
        bridge = (a, b) == ("B", "D")
        edge(ax, MMDS_POS, a, b, lw=3.0 if bridge else 2.0, color=ORANGE if bridge else INK,
             zorder=2 if bridge else 1)
    dots(ax, MMDS_POS, ORDER)

    def density(group):
        pairs = list(combinations(group, 2))
        inside = sum(frozenset(p) in {frozenset(e) for e in MMDS_EDGES} for p in pairs)
        return inside, len(pairs)

    i1, p1 = density("ABC")
    i2, p2 = density("DEFG")
    side_label(ax, (2.45, 1.75), f"{{A, B, C}}: {i1} of {p1} pairs\ndensity {i1 / p1:.2f}, a clique",
               ha="center", va="center", color=STEEL)
    side_label(ax, (8.0, 1.25), f"{{D, E, F, G}}: {i2} of {p2} pairs\ndensity {i2 / p2:.2f}",
               ha="center", va="center", color=STEEL)
    n = len(MMDS_EDGES)
    side_label(ax, (5.25, 7.55), f"whole graph: {n} of 21 pairs, density {n / 21:.2f}",
               ha="center", va="center", color=STEEL)
    callout(ax, mid(MMDS_POS, "B", "D"), "one edge\nbetween", (5.3, 4.4))
    return fig


@figure("vocab-overlap")
def overlap():
    pos = {"c1": (0.9, 5.4), "c2": (1.7, 3.0), "c3": (2.4, 5.9), "c4": (1.3, 1.9),
           "c5": (2.7, 1.6),
           "x1": (4.6, 5.0), "x2": (5.6, 5.4), "x3": (4.7, 2.8), "x4": (5.7, 2.4),
           "s1": (8.0, 6.0), "s2": (9.0, 4.4), "s3": (7.6, 3.4), "s4": (9.3, 2.0),
           "s5": (7.9, 1.2)}
    links = [("c1", "c3"), ("c1", "c2"), ("c2", "c4"), ("c4", "c5"), ("c3", "x1"),
             ("c2", "x3"), ("c5", "x3"),
             ("s1", "s2"), ("s2", "s4"), ("s3", "s5"), ("s4", "s5"), ("s1", "x2"),
             ("s3", "x4"), ("s2", "x2"),
             ("x1", "x2"), ("x1", "x3"), ("x1", "x4"), ("x2", "x3"), ("x2", "x4"),
             ("x3", "x4"), ("c3", "x2"), ("s3", "x3")]
    fig, ax = canvas("Overlapping communities",
                     "Based on MMDS Fig. 10.19: the overlap is denser than either club alone")
    for (cx, cy), w in [((3.4, 3.8), 6.4), ((6.8, 3.8), 6.4)]:
        ax.add_patch(Ellipse((cx, cy), w, 6.4, facecolor="none", edgecolor=STEEL, lw=2.0,
                             zorder=0))
    for a, b in links:
        both = a[0] == "x" and b[0] == "x"
        edge(ax, pos, a, b, lw=2.5 if both else 1.6, color=ORANGE if both else QUIET,
             size_a=400, size_b=400, zorder=2 if both else 1)
    for n, (x, y) in pos.items():
        ax.scatter(x, y, s=400, color=ORANGE if n[0] == "x" else STEEL, edgecolor=PAPER,
                   lw=1.2, zorder=3)
    side_label(ax, (0.4, 7.25), "Chess Club", va="center", color=INK)
    side_label(ax, (9.8, 7.25), "Spanish Club", ha="right", va="center", color=INK)
    side_label(ax, (5.1, 0.55), "Both clubs", ha="center", va="center", color=ORANGE)
    return fig


K_LEFT = {"L1": (2.2, 6.2), "L2": (2.2, 3.9), "L3": (2.2, 1.6)}
K_RIGHT = {"R1": (7.6, 5.2), "R2": (7.6, 2.6)}
K_EXTRA = {"x1": (4.9, 7.1), "x2": (4.9, 0.6), "x3": (9.6, 3.9)}
K_OTHER_EDGES = [("L1", "L2"), ("L2", "L3"), ("R1", "R2"), ("x1", "L1"), ("x1", "R1"),
                 ("x2", "L3"), ("x2", "R2"), ("x3", "R1"), ("x3", "R2"), ("x1", "L2"),
                 ("x2", "L2"), ("L1", "L3")]


def bipartite_figure(inside):
    fig, ax = canvas("A dense community contains a $K_{3,2}$" if inside
                     else "The complete bipartite graph $K_{3,2}$",
                     "Gray = the rest of the community; orange = the $K_{3,2}$ inside it"
                     if inside else "Every left node joins every right node; none join their own side")
    pos = {**K_LEFT, **K_RIGHT, **(K_EXTRA if inside else {})}
    if inside:
        for a, b in K_OTHER_EDGES:
            edge(ax, pos, a, b, lw=1.6, color=QUIET, size_a=700, size_b=700,
                 rad=0.35 if (a, b) == ("L1", "L3") else 0.0)
    for a in K_LEFT:
        for b in K_RIGHT:
            edge(ax, pos, a, b, lw=2.6, color=ORANGE, size_a=700, size_b=700, zorder=2)
    for n, (x, y) in pos.items():
        ax.scatter(x, y, s=700, color=ORANGE if n[0] in "LR" else STEEL, edgecolor=PAPER,
                   lw=1.2, zorder=3)
    if not inside:
        side_label(ax, (2.2, 7.25), "s = 3", ha="center", va="center", color=STEEL)
        side_label(ax, (7.6, 7.25), "t = 2", ha="center", va="center", color=STEEL)
    return fig


FIGURES["vocab-bipartite-v0"] = lambda: bipartite_figure(False)
FIGURES["vocab-bipartite-v1"] = lambda: bipartite_figure(True)


# Worksheet checkpoint 5's friendship graph, with the same node layout.
TRIAD_POS = {"E": (1.0, 4.2), "A": (3.4, 4.2), "B": (5.8, 6.2), "C": (5.8, 2.2), "D": (8.2, 4.2)}
TRIAD_EDGES = [("A", "B"), ("A", "C"), ("B", "C"), ("B", "D"), ("C", "D"), ("A", "E")]


def shared_friends(a, b):
    nbrs = {n: {v for e in TRIAD_EDGES if n in e for v in e if v != n} for n in TRIAD_POS}
    return nbrs[a] & nbrs[b]


def triadic_figure(show):
    fig, ax = canvas("Which missing edge is most likely to form next?",
                     "Dashed = a missing edge, labeled with the friends its two ends share"
                     if show else "A toy friendship graph (worksheet checkpoint 5)")
    for a, b in TRIAD_EDGES:
        edge(ax, TRIAD_POS, a, b, lw=2.0, color=QUIET)
    if show:
        missing = [(a, b) for a, b in combinations(sorted(TRIAD_POS), 2)
                   if (a, b) not in TRIAD_EDGES and (b, a) not in TRIAD_EDGES]
        for a, b in missing:
            k = len(shared_friends(a, b))
            best = (a, b) == ("A", "D")
            rad = -0.9 if (a, b) == ("D", "E") else 0.0  # bend E-D below C instead of through A
            ax.annotate("", xy=TRIAD_POS[b], xytext=TRIAD_POS[a], zorder=2 if best else 1,
                        arrowprops=dict(arrowstyle="-", color=ORANGE if best else STEEL,
                                        lw=2.8 if best else 1.6, linestyle="--",
                                        shrinkA=16, shrinkB=16, connectionstyle=f"arc3,rad={rad}"))
            label = {("A", "D"): (4.6, 4.55), ("B", "E"): (3.0, 5.5),
                     ("C", "E"): (3.0, 2.9), ("D", "E"): (4.6, 0.55)}[(a, b)]
            side_label(ax, label, f"{k} shared", ha="center", va="center",
                       color=ORANGE if best else STEEL)
    dots(ax, TRIAD_POS, TRIAD_POS, fill={"A": "orange", "D": "orange"} if show else {})
    return fig


FIGURES["vocab-triadic-v0"] = lambda: triadic_figure(False)
FIGURES["vocab-triadic-v1"] = lambda: triadic_figure(True)


# --------------------------------------------------------------------- main

def main(argv: list[str]) -> None:
    if base.FONT_PATH.exists():
        font_manager.fontManager.addfont(str(base.FONT_PATH))
        family = font_manager.FontProperties(fname=str(base.FONT_PATH)).get_name()
        plt.rcParams["font.family"] = [family, "DejaVu Sans"]
    plt.rcParams["svg.fonttype"] = "path"
    wanted = argv or list(FIGURES)
    unknown = [name for name in wanted if name not in FIGURES]
    if unknown:
        raise SystemExit(f"unknown figure(s): {', '.join(unknown)}\navailable: {', '.join(FIGURES)}")
    for name in wanted:
        base.save(FIGURES[name](), name)


if __name__ == "__main__":
    main(sys.argv[1:])
