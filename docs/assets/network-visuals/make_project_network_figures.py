#!/usr/bin/env python3
"""Toy network sketches of six CS 418 group projects' data (Week 12, Day 1).

NOTICE: this file was substantially drafted by an LLM coding system and has not
yet been reviewed. Check every figure against the slide it illustrates.

Every graph here is hand-made toy data: a handful of nodes and edges that show
the *shape* of the network hiding in each group's dataset, not its contents.
Nothing is read from the groups' files.

  * project-ufc.svg        fighters; arrow = a fight, winner -> loser
  * project-soccer.svg     national teams; edge width = matches played
  * project-nfl.svg        QBs and receivers; arrow width = pass targets
  * project-yelp.svg       reviewers and restaurants (bipartite); edge = a review
  * project-flock.svg      agencies and technologies (bipartite); edge = "uses"
  * project-fakenews.svg   two sharing cascades; edge = a share or retweet

Follows docs/assets/STYLE.md and the karate-club figures in
clustering-visuals/make_clustering_figures.py: same 900 x 700 split-slide
canvas, grayscale neutrals, Libre Franklin drawn as paths.

Encoding, the same on all six:
  * gray circle = a person or team; ink square = the other node type in a
    two-type (bipartite) network: a restaurant, a technology, an article.
  * orange = one example edge, labeled in words, so the slide's "Edge:" bullet
    has a picture to point at.

Usage:  python3 make_project_network_figures.py [figure-name ...]
"""
from __future__ import annotations

import sys
from pathlib import Path

import matplotlib

matplotlib.use("Agg")

import matplotlib.pyplot as plt
from matplotlib import font_manager

OUT_DIR = Path(__file__).resolve().parent
REPO_ROOT = OUT_DIR.parents[2]
FONT_PATH = OUT_DIR.parent / "fonts" / "libre-franklin" / "LibreFranklin-Regular.ttf"

# STYLE.md palette
INK = "#1A1A1A"
STEEL = "#565A5C"
QUIET = "#AAAAAA"
BORDER = "#DDDDDD"
SOFT_GRAY = "#F4F4F2"
PAPER = "#FFFFFF"
ORANGE = "#F9461C"

DPI = 100
SPLIT = (900, 700)
XLIM, YLIM = (-0.3, 10.3), (-0.5, 7.7)

CIRCLE = 900   # scatter size (points^2) of a labeled node
SQUARE = 820
SMALL = 260    # unlabeled node

FIGURES: dict[str, callable] = {}


def figure(name: str):
    def wrap(fn):
        FIGURES[name] = fn
        return fn
    return wrap


# ------------------------------------------------------------------ helpers

def canvas(headline, subline=None):
    """The karate-club canvas: headline at top-left, bare equal-aspect axes."""
    width, height = SPLIT
    top, side, bottom = 110, 30, 30
    fig = plt.figure(figsize=(width / DPI, height / DPI), dpi=DPI)
    fig.patch.set_facecolor(PAPER)
    ax = fig.add_axes([side / width, bottom / height,
                       (width - 2 * side) / width, (height - top - bottom) / height])
    ax.set_facecolor(PAPER)
    ax.set_xlim(*XLIM)
    ax.set_ylim(*YLIM)
    ax.set_aspect("equal", adjustable="box")
    ax.set_xticks([])
    ax.set_yticks([])
    for s in ax.spines.values():
        s.set_visible(False)
    fig.text(0.03, 0.985, headline, fontsize=18, color=INK, ha="left", va="top")
    if subline:
        fig.text(0.03, 0.93, subline, fontsize=14, color=STEEL, ha="left", va="top")
    return fig, ax


def radius_pts(size):
    return size ** 0.5 / 2


def edge(ax, pos, a, b, *, lw=2.0, color=QUIET, arrow=False, size_a=CIRCLE, size_b=CIRCLE,
         rad=0.0, zorder=1):
    """A line (or arrow) from a to b that stops at each node's rim."""
    style = "-|>,head_length=0.7,head_width=0.4" if arrow else "-"
    ax.annotate("", xy=pos[b], xytext=pos[a], zorder=zorder,
                arrowprops=dict(arrowstyle=style, color=color, lw=lw,
                                shrinkA=radius_pts(size_a) + 1,
                                shrinkB=radius_pts(size_b) + (4 if arrow else 1),
                                connectionstyle=f"arc3,rad={rad}",
                                mutation_scale=10 + 2.5 * lw))


def nodes(ax, pos, names, *, kind="circle", size=None, labels=True, hollow=(), fontsize=15):
    """Gray circles or ink squares; `hollow` names get a white fill."""
    marker = "o" if kind == "circle" else "s"
    size = size or (CIRCLE if kind == "circle" else SQUARE)
    fill = STEEL if kind == "circle" else INK
    for n in names:
        x, y = pos[n]
        open_ = n in hollow
        ax.scatter([x], [y], marker=marker, s=size, color=PAPER if open_ else fill,
                   edgecolor=INK if open_ else PAPER, lw=2.0 if open_ else 1.2, zorder=3)
        if labels:
            ax.text(x, y, n, ha="center", va="center_baseline", fontsize=fontsize,
                    color=INK if open_ else PAPER, zorder=4)


def side_label(ax, xy, text, *, ha="left", va="center", color=INK, size=15):
    ax.text(*xy, text, ha=ha, va=va, fontsize=size, color=color, zorder=5)


def callout(ax, xy, text, xytext):
    """Orange words pointing at the example edge."""
    ax.annotate(text, xy=xy, xytext=xytext, fontsize=15, color=ORANGE, ha="center",
                va="center", zorder=6,
                arrowprops=dict(arrowstyle="-", color=ORANGE, lw=1.2, shrinkA=4, shrinkB=2),
                bbox=dict(boxstyle="square,pad=0.15", facecolor=PAPER, edgecolor="none"))


def mid(pos, a, b, t=0.5):
    (x0, y0), (x1, y1) = pos[a], pos[b]
    return (x0 + t * (x1 - x0), y0 + t * (y1 - y0))


# ------------------------------------------------------------------ figures

@figure("project-ufc")
def ufc():
    pos = {"A": (2.0, 5.6), "B": (4.6, 6.3), "C": (7.6, 5.8), "D": (1.4, 3.0),
           "E": (4.2, 3.6), "F": (7.2, 3.3), "G": (2.6, 0.8), "H": (6.0, 0.8)}
    fights = [("A", "B"), ("A", "D"), ("A", "E"), ("B", "C"), ("B", "E"), ("C", "F"),
              ("D", "E"), ("D", "G"), ("E", "F"), ("G", "H"), ("F", "H"), ("H", "E")]
    fig, ax = canvas("Toy example: 8 fighters, 12 fights",
                     "Arrow points from the winner to the loser")
    for a, b in fights:
        example = (a, b) == ("A", "B")
        edge(ax, pos, a, b, arrow=True, lw=3.0 if example else 2.0,
             color=ORANGE if example else QUIET, zorder=2 if example else 1)
    nodes(ax, pos, pos)
    callout(ax, mid(pos, "A", "B", 0.45), "A beat B", (3.0, 7.0))
    return fig


@figure("project-soccer")
def soccer():
    pos = {  # three regions, four teams each
        "e1": (1.2, 5.8), "e2": (2.9, 6.5), "e3": (3.3, 4.8), "e4": (1.6, 4.1),
        "s1": (6.8, 6.4), "s2": (8.6, 6.0), "s3": (8.2, 4.4), "s4": (6.6, 4.7),
        "a1": (3.6, 1.6), "a2": (5.2, 2.4), "a3": (6.5, 1.2), "a4": (4.6, 0.5)}
    matches = {  # (team, team): matches played
        ("e1", "e2"): 9, ("e1", "e3"): 6, ("e1", "e4"): 8, ("e2", "e3"): 7, ("e2", "e4"): 5,
        ("e3", "e4"): 9, ("s1", "s2"): 9, ("s1", "s3"): 6, ("s1", "s4"): 8, ("s2", "s3"): 9,
        ("s3", "s4"): 7, ("s2", "s4"): 5, ("a1", "a2"): 8, ("a1", "a4"): 7, ("a2", "a3"): 9,
        ("a3", "a4"): 6, ("a2", "a4"): 5, ("a1", "a3"): 4,
        ("e3", "s4"): 2, ("e2", "s1"): 1, ("e3", "a2"): 1, ("s4", "a2"): 2, ("e4", "a1"): 1}
    fig, ax = canvas("Toy example: 12 national teams in 3 regions",
                     "Line width = number of matches the pair has played")
    for (a, b), n in matches.items():
        example = (a, b) == ("e1", "e4")
        edge(ax, pos, a, b, lw=0.6 * n, color=ORANGE if example else QUIET,
             size_a=SMALL * 2, size_b=SMALL * 2, zorder=2 if example else 1)
    nodes(ax, pos, pos, size=SMALL * 2, labels=False)
    side_label(ax, (0.2, 7.0), "Europe", va="top", color=STEEL)
    side_label(ax, (9.8, 7.0), "South America", ha="right", va="top", color=STEEL)
    side_label(ax, (7.4, 0.5), "Africa", color=STEEL)
    callout(ax, mid(pos, "e1", "e4"), "played 8 times", (0.9, 2.6))
    return fig


@figure("project-nfl")
def nfl():
    pos = {"QB1": (2.0, 4.6), "QB2": (2.0, 1.6), "WR1": (7.6, 6.6), "WR2": (8.4, 4.9),
           "TE": (8.4, 3.1), "RB": (7.6, 1.3), "WR3": (5.4, 0.4)}
    targets = {("QB1", "WR1"): 140, ("QB1", "WR2"): 95, ("QB1", "TE"): 70, ("QB1", "RB"): 45,
               ("QB1", "WR3"): 30, ("QB2", "WR1"): 20, ("QB2", "TE"): 15, ("QB2", "RB"): 10,
               ("QB2", "WR3"): 12}
    fig, ax = canvas("Toy example: one team's passing game",
                     "Arrow from passer to target; width = number of targets")
    qbs = ["QB1", "QB2"]
    for (a, b), n in targets.items():
        example = (a, b) == ("QB1", "WR1")
        edge(ax, pos, a, b, arrow=True, lw=0.045 * n + 0.6,
             color=ORANGE if example else QUIET, size_a=SQUARE * 1.4, size_b=CIRCLE * 1.4,
             zorder=2 if example else 1)
    nodes(ax, pos, qbs, kind="square", size=SQUARE * 1.4, fontsize=14)
    nodes(ax, pos, [n for n in pos if n not in qbs], size=CIRCLE * 1.4, fontsize=14)
    callout(ax, mid(pos, "QB1", "WR1", 0.5), "140 targets", (3.4, 6.7))
    return fig


@figure("project-yelp")
def yelp():
    users = [f"u{i}" for i in range(7)]
    shops = ["R1", "R2", "R3", "R4"]
    pos = {u: (1.6, 6.6 - i * 1.0) for i, u in enumerate(users)}
    pos |= {r: (7.8, 5.9 - i * 1.6) for i, r in enumerate(shops)}
    reviews = [("u0", "R1"), ("u0", "R2"), ("u1", "R1"), ("u2", "R2"), ("u2", "R3"),
               ("u3", "R1"), ("u3", "R3"), ("u4", "R3"), ("u4", "R4"), ("u5", "R4"),
               ("u6", "R2"), ("u6", "R4")]
    fig, ax = canvas("Toy example: 7 reviewers, 4 restaurants",
                     "Line = one review; a hollow square is a restaurant that closed")
    for a, b in reviews:
        example = (a, b) == ("u3", "R1")
        edge(ax, pos, a, b, lw=3.0 if example else 2.0, color=ORANGE if example else QUIET,
             size_a=SMALL, size_b=SQUARE, zorder=2 if example else 1)
    nodes(ax, pos, users, size=SMALL, labels=False)
    nodes(ax, pos, shops, kind="square", hollow={"R3"})
    side_label(ax, (1.6, 7.05), "Reviewers", ha="center", va="bottom", color=STEEL)
    side_label(ax, (7.8, 7.05), "Restaurants", ha="center", va="bottom", color=STEEL)
    side_label(ax, (8.4, pos["R3"][1]), "closed", color=STEEL)
    callout(ax, mid(pos, "u3", "R1", 0.55), "one review", (5.0, 7.0))
    return fig


@figure("project-flock")
def flock():
    agencies = list("ABCDEF")
    tech = ["ALPR", "Face recognition", "Drones", "Gunshot detection", "Body cameras"]
    pos = {a: (1.4, 6.6 - i * 1.25) for i, a in enumerate(agencies)}
    pos |= {t: (5.6, 6.4 - i * 1.45) for i, t in enumerate(tech)}
    uses = [("A", "ALPR"), ("A", "Drones"), ("A", "Body cameras"), ("B", "ALPR"),
            ("B", "Face recognition"), ("C", "Body cameras"), ("D", "ALPR"),
            ("D", "Gunshot detection"), ("D", "Drones"), ("E", "Gunshot detection"),
            ("E", "Body cameras"), ("F", "ALPR"), ("F", "Face recognition")]
    fig, ax = canvas("Toy example: 6 agencies, 5 technologies",
                     "Line = the agency uses that technology")
    for a, b in uses:
        example = (a, b) == ("B", "ALPR")
        edge(ax, pos, a, b, lw=3.0 if example else 2.0, color=ORANGE if example else QUIET,
             size_b=SQUARE * 0.6, zorder=2 if example else 1)
    nodes(ax, pos, agencies)
    nodes(ax, pos, tech, kind="square", size=SQUARE * 0.6, labels=False)
    for t in tech:
        side_label(ax, (pos[t][0] + 0.45, pos[t][1]), t)
    side_label(ax, (1.4, 7.05), "Agencies", ha="center", va="bottom", color=STEEL)
    side_label(ax, (5.6, 7.05), "Technologies", ha="center", va="bottom", color=STEEL)
    callout(ax, mid(pos, "B", "ALPR", 0.45), "B uses ALPR", (3.4, 7.0))
    return fig


@figure("project-fakenews")
def fakenews():
    # Two sharing trees: parent -> child means "child shared it from parent".
    fake = {"F": (2.5, 6.0), "f1": (1.0, 4.4), "f2": (2.5, 4.4), "f3": (4.0, 4.4),
            "f4": (0.6, 2.8), "f5": (1.4, 2.8), "f6": (4.0, 2.8), "f7": (4.0, 1.2),
            "f8": (3.2, 0.2), "f9": (4.8, 0.2)}
    fake_edges = [("F", "f1"), ("F", "f2"), ("F", "f3"), ("f1", "f4"), ("f1", "f5"),
                  ("f3", "f6"), ("f6", "f7"), ("f7", "f8"), ("f7", "f9")]
    real = {"R": (7.5, 6.0), "r1": (5.9, 4.4), "r2": (6.7, 4.4), "r3": (7.5, 4.4),
            "r4": (8.3, 4.4), "r5": (9.1, 4.4), "r6": (6.7, 2.8), "r7": (8.3, 2.8),
            "r8": (9.1, 2.8)}
    real_edges = [("R", "r1"), ("R", "r2"), ("R", "r3"), ("R", "r4"), ("R", "r5"),
                  ("r2", "r6"), ("r4", "r7"), ("r5", "r8")]
    pos = fake | real
    fig, ax = canvas("Toy example: two articles' sharing cascades",
                     "Square = article; circle = a tweet; line = shared from")
    for a, b in fake_edges + real_edges:
        example = (a, b) == ("f6", "f7")
        edge(ax, pos, a, b, lw=3.0 if example else 2.0, color=ORANGE if example else QUIET,
             size_a=SQUARE if a in "FR" else SMALL, size_b=SMALL, zorder=2 if example else 1)
    nodes(ax, pos, ["F", "R"], kind="square", labels=False)
    nodes(ax, pos, [n for n in pos if n not in "FR"], size=SMALL, labels=False)
    side_label(ax, (2.5, 6.6), "Fake article", ha="center", va="bottom")
    side_label(ax, (7.5, 6.6), "Real article", ha="center", va="bottom")
    callout(ax, mid(pos, "f6", "f7"), "a retweet\nof a retweet", (6.3, 1.2))
    return fig


# --------------------------------------------------------------------- main

def save(fig, name):
    out = OUT_DIR / f"{name}.svg"
    fig.savefig(out, format="svg", facecolor=PAPER)
    plt.close(fig)
    print(f"  wrote {out.relative_to(REPO_ROOT)}")


def main(argv: list[str]) -> None:
    if FONT_PATH.exists():
        font_manager.fontManager.addfont(str(FONT_PATH))
        family = font_manager.FontProperties(fname=str(FONT_PATH)).get_name()
        plt.rcParams["font.family"] = [family, "DejaVu Sans"]
    # Text as paths, per STYLE.md: the SVG stays self-contained.
    plt.rcParams["svg.fonttype"] = "path"

    wanted = argv or list(FIGURES)
    unknown = [name for name in wanted if name not in FIGURES]
    if unknown:
        raise SystemExit(f"unknown figure(s): {', '.join(unknown)}\n"
                         f"available: {', '.join(FIGURES)}")
    print(f"writing {len(wanted)} figure(s) to {OUT_DIR.relative_to(REPO_ROOT)}")
    for name in wanted:
        save(FIGURES[name](), name)


if __name__ == "__main__":
    main(sys.argv[1:])
