#!/usr/bin/env python3
"""Redraws of Granovetter's "The Strength of Weak Ties" (1973) Figs. 1 and 2a for the Week 12, Day 2 slides.

NOTICE: this file was drafted by an LLM coding system and has not yet been reviewed. Check every figure against the slide it illustrates.

Node letters and ties copy the paper's figures (AJS 78(6), pp. 1363 and 1365); positions are hand-placed from the printed figures. Solid = strong tie, dashed = weak tie, as in the paper's Fig. 2 legend.

  * weak-ties-v0.svg   Fig. 1, the "forbidden triad": A-B and A-C strong, B-C absent
  * weak-ties-v1.svg   + the B-C tie Granovetter supposes is "always present (whether weak or strong)"
  * weak-ties-v2.svg   Fig. 2a relabeled as two student organizations (WiCS left, ACM right; hypothetical members): strong ties only
  * weak-ties-v3.svg   + weak ties within each club
  * weak-ties-v4.svg   + the weak tie E-I between the clubs, with the average WiCS-to-ACM distance
  * weak-ties-v5.svg   + the weak tie A-B, a local bridge of degree 3; the average distance drops

Shares the 900 x 700 split-slide canvas and helpers of make_project_network_figures.py and make_vocab_figures.py.

Usage:  python3 make_weak_ties_figures.py [figure-name ...]   (run in docs/slides/.venv)
"""
from __future__ import annotations

import sys

import matplotlib.pyplot as plt
from matplotlib import font_manager

import make_project_network_figures as base
from matplotlib.patches import Ellipse

from make_project_network_figures import BORDER, INK, ORANGE, SOFT_GRAY, STEEL, canvas, mid, side_label
from make_vocab_figures import bfs, dots, footer

FIGURES: dict[str, callable] = {}

# Fig. 1: C above and right of A, B level with A.
TRIAD_POS = {"A": (2.4, 1.9), "B": (7.6, 1.9), "C": (4.3, 6.3)}

# Fig. 2a, measured off the printed figure (pixels at 300 dpi) and rescaled to the canvas.
_PX = {"E": (310, 83), "C": (195, 198), "F": (342, 163), "A": (432, 198), "D": (310, 310),
       "I": (797, 78), "J": (767, 163), "B": (683, 196), "G": (913, 198), "H": (795, 305)}
BRIDGE_POS = {n: (0.4 + (x - 195) / (913 - 195) * 9.2, 6.6 - (y - 78) / (310 - 78) * 4.4) for n, (x, y) in _PX.items()}
STRONG = [("E", "D"), ("E", "F"), ("C", "F"), ("C", "A"), ("F", "D"), ("D", "A"),
          ("I", "B"), ("I", "G"), ("I", "H"), ("B", "J"), ("J", "G"), ("J", "H"), ("H", "G")]
WEAK = [("E", "C"), ("E", "A"), ("C", "D"), ("F", "A"), ("I", "J"), ("B", "H"), ("E", "I"), ("A", "B")]


def figure(name: str):
    def wrap(fn):
        FIGURES[name] = fn
        return fn
    return wrap


def tie(ax, pos, a, b, *, weak, color=INK, lw=2.4, zorder=1):
    """A strong (solid) or weak (dashed) tie that stops at each node's rim."""
    ax.annotate("", xy=pos[b], xytext=pos[a], zorder=zorder,
                arrowprops=dict(arrowstyle="-", color=color, lw=lw, linestyle=(0, (5, 4)) if weak else "-",
                                shrinkA=base.radius_pts(base.CIRCLE) + 1, shrinkB=base.radius_pts(base.CIRCLE) + 1))


def triad(show):
    fig, ax = canvas("The forbidden triad",
                     "Based on Granovetter (1973), Fig. 1. Solid = strong tie; dashed = weak tie")
    tie(ax, TRIAD_POS, "A", "B", weak=False)
    tie(ax, TRIAD_POS, "A", "C", weak=False)
    if show:
        tie(ax, TRIAD_POS, "C", "B", weak=True, color=ORANGE, lw=2.8)
        side_label(ax, mid(TRIAD_POS, "C", "B", 0.45), "  B–C: weak or strong,\n  but present", color=ORANGE)
        footer(ax, ["If A–B and A–C are strong, B and C are tied too"], y=0.6)
    else:
        side_label(ax, mid(TRIAD_POS, "C", "B", 0.45), "  no B–C tie", color=STEEL)
        footer(ax, ["A–B strong, A–C strong, B–C absent"], y=0.6)
    dots(ax, TRIAD_POS, TRIAD_POS, fill={"B": "orange", "C": "orange"} if show else {})
    return fig


FIGURES["weak-ties-v0"] = lambda: triad(False)
FIGURES["weak-ties-v1"] = lambda: triad(True)


WICS, ACM = "ACDEF", "BGHIJ"
CLUB_BRIDGES = [("E", "I"), ("A", "B")]   # weak ties between the clubs, in the order they are added
WITHIN_WEAK = [e for e in WEAK if e not in CLUB_BRIDGES]


def mean_cross_distance(edges):
    """Average number of steps from a WiCS member to an ACM member."""
    steps = [bfs(edges, a)[b] for a in WICS for b in ACM]
    return sum(steps) / len(steps)


def clubs(step):
    """Fig. 2a as two student organizations, built up in four steps (0-3)."""
    fig, ax = canvas("Two student organizations",
                     "Based on Granovetter (1973), Fig. 2a, with hypothetical club members")
    for (x, y), name in [((2.1, 4.4), "WiCS"), ((7.95, 4.4), "ACM")]:
        ax.add_patch(Ellipse((x, y), 4.5, 5.9, facecolor=SOFT_GRAY, edgecolor=BORDER, lw=1.5, zorder=0))
        side_label(ax, (x, 7.55), name, ha="center", va="center", color=STEEL, size=17)
    for a, b in STRONG:
        tie(ax, BRIDGE_POS, a, b, weak=False)
    if step >= 1:
        for a, b in WITHIN_WEAK:
            tie(ax, BRIDGE_POS, a, b, weak=True, color=STEEL, lw=2.0)
    bridges = CLUB_BRIDGES[:max(step - 1, 0)]
    for a, b in bridges:
        tie(ax, BRIDGE_POS, a, b, weak=True, color=ORANGE, lw=3.2, zorder=2)
    within = STRONG + WITHIN_WEAK
    if step == 0:
        lines = ["Close friends (strong ties) cluster inside each club.", "No path connects WiCS and ACM."]
    elif step == 1:
        lines = ["Acquaintances (weak ties) fill in each club.", "Still no path between the clubs."]
    elif step == 2:
        d = mean_cross_distance(within + bridges)
        lines = ["One weak tie, E–I, joins the clubs. A WiCS member", f"is now {d:.2f} steps from an ACM member, on average."]
    else:
        d0, d = mean_cross_distance(within + CLUB_BRIDGES[:1]), mean_cross_distance(within + bridges)
        assert bfs(within + CLUB_BRIDGES[:1], "A")["B"] == 3
        lines = [f"A second weak tie, A–B: average {d0:.2f} → {d:.2f} steps.", "Without A–B, A to B takes 3 steps (A–E–I–B): a local bridge."]
    footer(ax, lines, y=1.0)
    ends = {n for e in bridges for n in e}
    dots(ax, BRIDGE_POS, BRIDGE_POS, fill={n: "orange" for n in ends})
    return fig


for _step in range(4):
    FIGURES[f"weak-ties-v{_step + 2}"] = lambda step=_step: clubs(step)


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
