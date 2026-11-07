#!/usr/bin/env python3
"""Chicago Bulls co-play network, built up in steps, plus one close-up per community.

NOTICE: this file was substantially drafted by an LLM coding system and has not
yet been thoroughly reviewed.

Frames (shared canvas, so they line up pixel for pixel in an r-stack):
  * bulls-network-v0.svg  one dot per player
  * bulls-network-v1.svg  + an edge for every pair who were on the roster for
                          at least one game together (unweighted)
  * bulls-network-v2.svg  edge width = games together (weighted)
  * bulls-network-v3.svg  Louvain communities, colored, each labeled in a box
                          on the cluster with its era and top players
Each frame has a two-line caption in the top-left corner saying what it adds.
Close-ups, one per community (in era order):
  * bulls-community-1.svg, bulls-community-2.svg, ...
    the community's most-rostered players as headshots, edges weighted by
    games together

Data: Bulls roster records per game, January 2002 through the 2013-14 season,
from the shared-success sports data (bulls_data.py; Mukherjee et al. 2019).
Headshots: Wikimedia Commons, openly licensed (fetch_headshots.py; credits in
headshots/credits.csv and SOURCES.md).

Method notes:
  * Layout: networkx spring layout on log(1 + games together), fixed seed, so
    the heaviest pairs do not collapse onto each other. Computed once and
    shared by v0-v3.
  * Communities: networkx Louvain on the weighted graph (weight = games
    together), resolution 1. Louvain is randomized, so it is run with seeds
    0-19 and the partition it returns most often is used (modal_louvain).
  * Era of a community: the seasons in which it holds more of that season's
    Bulls roster slots than any other community.

Style (docs/assets/STYLE.md): golden canvas 1000 x 618, Libre Franklin drawn
as paths. Communities take Okabe-Ito hues (colorblind-safe, categorical:
Louvain's groups have no order of their own), with orange left out because it
is the site's accent color.

Usage:  python3 make_bulls_figures.py
"""

from __future__ import annotations

import collections
import csv
import math
import textwrap
from pathlib import Path

import matplotlib

matplotlib.use("Agg")

import matplotlib.pyplot as plt
import networkx as nx
import numpy as np
from matplotlib import font_manager
from matplotlib.patches import Circle
from PIL import Image

from bulls_data import build_graph, display_name, espn_id, load_games

# ------------------------------------------------------------------ figure text (edit here)
# {placeholders} are filled in from the data when the figures are drawn.

CAPTIONS = {   # main frames: (headline, detail line)
    "v0": ("Each dot is a player",
           "{players} players on the Bulls roster, Jan. 2002 to 2013-14"),
    "v1": ("Each line connects two players who played in a game together",
           "{pairs:,} pairs; every line looks the same, 1 game or hundreds"),
    "v2": ("Lines are weighted by how many games the pair played together",
           "Thicker, darker line = more games together (1 to {max_games:,})"),
    "v3": ("Community detection (Louvain method): each color is one community",
           "{communities} groups of players more tied to each other than to the rest, by games together"),
}
CLOSEUP_TITLE = "Community {k}: {era}"
CLOSEUP_SUBTITLE = ("{shown} of its {members} players, the most games on the roster; "
                    "line width = games together")
DATA_NOTE = "Bulls rosters per game, Jan. 2002 to 2013-14 (Mukherjee et al., 2019)"
PHOTO_NOTE = "Photos: Wikimedia Commons (CC BY, CC BY-SA, public domain); credits in SOURCES.md"

OUT_DIR = Path(__file__).resolve().parent
HEADSHOTS = OUT_DIR / "headshots"
FONT_PATH = OUT_DIR.parent / "fonts" / "libre-franklin" / "LibreFranklin-Regular.ttf"

PHI = (1 + 5**0.5) / 2
W, H = 1000, round(1000 / PHI)
DPI = 100
PT = 72 / DPI                               # points per canvas pixel

INK = "#1A1A1A"
MUTED = "#777777"
EDGE = "#9A9A9A"
PAPER = "#FFFFFF"
COMMUNITY_COLORS = ["#0072B2", "#009E73", "#CC79A7", "#D55E00", "#56B4E9", "#E69F00"]

SEED = 418
CLOSEUP_N = 16                              # players per close-up


# ------------------------------------------------------------------ data

def season_label(start: int) -> str:
    return f"{start}-{str(start + 1)[-2:]}"


LOUVAIN_RUNS = 20


def modal_louvain(G):
    """The partition Louvain returns most often over seeds 0..LOUVAIN_RUNS-1."""
    runs = collections.Counter()
    for seed in range(LOUVAIN_RUNS):
        part = nx.community.louvain_communities(G, weight="weight", seed=seed)
        runs[frozenset(frozenset(c) for c in part)] += 1
    best, count = runs.most_common(1)[0]
    print(f"Louvain: {len(runs)} distinct partitions over {LOUVAIN_RUNS} seeds; "
          f"using the most common ({count} runs, {len(best)} communities)")
    return [set(c) for c in best]


def analyze():
    games, season = load_games()
    G = build_graph(games)
    appearances = collections.Counter(p for ps in games.values() for p in ps)
    communities = modal_louvain(G)
    # era: seasons where the community holds the most roster slots
    slots = collections.defaultdict(collections.Counter)    # season -> community -> player-games
    member = {p: i for i, c in enumerate(communities) for p in c}
    for m, ps in games.items():
        for p in ps:
            slots[season[m]][member[p]] += 1
    seasons_won = collections.defaultdict(list)
    for s, counts in slots.items():
        seasons_won[counts.most_common(1)[0][0]].append(s)
    order = sorted(range(len(communities)), key=lambda i: min(seasons_won.get(i, [9999])))
    info = []
    for rank, i in enumerate(order):
        ss = sorted(seasons_won.get(i, []))
        top = sorted(communities[i], key=lambda p: -appearances[p])
        info.append({"members": communities[i], "color": COMMUNITY_COLORS[rank],
                     "era": (season_label(ss[0]) if len(ss) == 1 else
                             f"{season_label(ss[0])} to {season_label(ss[-1])}") if ss else "no season of its own",
                     "top": top})
    return G, appearances, info


CAPTION_BOX = (16, 12, 400, 120)           # top-left corner kept clear for the frame captions


def spring(G, iterations):
    """Spring layout on log(1 + games together), so heavy pairs don't collapse together."""
    L = nx.Graph()
    L.add_nodes_from(G)
    L.add_weighted_edges_from((u, v, math.log1p(w)) for u, v, w in G.edges(data="weight"))
    return nx.spring_layout(L, weight="weight", seed=SEED, iterations=iterations)


def layout(G):
    """Shared v0-v3 positions: stretched to the frame, turned so the caption corner is empty.

    A force layout has no meaningful orientation, so try every 15-degree turn
    (and its mirror image) and keep the one with the fewest players under the
    caption; ties go to the smallest turn.
    """
    raw = spring(G, 300)
    x0, y0, x1, y1 = CAPTION_BOX
    best = None
    for mirror in (1, -1):
        for deg in range(0, 360, 15):
            t = math.radians(deg)
            rot = {n: (mirror * (x * math.cos(t) - y * math.sin(t)), x * math.sin(t) + y * math.cos(t))
                   for n, (x, y) in raw.items()}
            pos = fit(rot, (30, 30, W - 30, H - 40))
            hidden = sum(x0 - 10 <= x <= x1 + 10 and y0 - 10 <= y <= y1 + 10 for x, y in pos.values())
            if best is None or hidden < best[0]:
                best = (hidden, pos)
    return best[1]


def fit(pos, box, keep_aspect=False):
    """Scale positions into a pixel box (x0, y0, x1, y1).

    Force layouts have no meaningful aspect ratio, so by default each axis is
    stretched to fill the box.
    """
    xy = np.array(list(pos.values()), float)
    lo, hi = xy.min(0), xy.max(0)
    x0, y0, x1, y1 = box
    s = np.array([(x1 - x0) / (hi[0] - lo[0] or 1), (y1 - y0) / (hi[1] - lo[1] or 1)])
    if keep_aspect:
        s[:] = s.min()
    off = np.array([(x0 + x1) / 2, (y0 + y1) / 2]) - s * (lo + hi) / 2
    return {n: tuple(s * np.array(p) + off) for n, p in pos.items()}


def spread(pos, box, dx, dy, rounds=400):
    """Push apart any two nodes closer than dx horizontally and dy vertically, inside box."""
    keys = list(pos)
    xy = np.array([pos[k] for k in keys], float)
    x0, y0, x1, y1 = box
    for _ in range(rounds):
        moved = False
        for i in range(len(xy)):
            for j in range(i + 1, len(xy)):
                d = xy[j] - xy[i]
                over_x, over_y = dx - abs(d[0]), dy - abs(d[1])
                if over_x > 0 and over_y > 0:
                    moved = True
                    # separate along the axis that needs the smaller push
                    axis = 0 if over_x / dx < over_y / dy else 1
                    sign = 1 if d[axis] >= 0 else -1
                    if d[axis] == 0:
                        sign = 1 if (i + j) % 2 else -1
                    push = (over_x if axis == 0 else over_y) / 2 + 0.5
                    xy[i, axis] -= sign * push
                    xy[j, axis] += sign * push
        xy[:, 0] = xy[:, 0].clip(x0, x1)
        xy[:, 1] = xy[:, 1].clip(y0, y1)
        if not moved:
            break
    return {k: tuple(p) for k, p in zip(keys, xy)}


# ------------------------------------------------------------------ drawing

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


def footnote(ax, text, *, left=False):
    ax.text(24 if left else W - 24, H - 14, text, ha="left" if left else "right",
            va="baseline", fontsize=10, color=MUTED)


def save(fig, name):
    out = OUT_DIR / f"{name}.svg"
    fig.savefig(out, format="svg", facecolor=PAPER)
    plt.close(fig)
    print(f"  wrote {out.name}")


def edge_width(w, wmax, lo=0.3, hi=6.0):
    return lo + (hi - lo) * math.sqrt(w / wmax)


def draw_edges(ax, G, pos, *, weighted, color_of=None):
    wmax = max(w for *_, w in G.edges(data="weight"))
    for u, v, w in sorted(G.edges(data="weight"), key=lambda e: e[2]):
        (x0, y0), (x1, y1) = pos[u], pos[v]
        color = EDGE
        if color_of and color_of.get(u) == color_of.get(v):
            color = color_of[u]
        lw = edge_width(w, wmax) if weighted else 0.5
        alpha = (0.25 + 0.6 * math.sqrt(w / wmax)) if weighted else 0.25
        ax.plot([x0, x1], [y0, y1], color=color, lw=lw * PT, alpha=alpha,
                solid_capstyle="round", zorder=1)


def draw_dots(ax, pos, *, color_of=None, r=5):
    for n, (x, y) in pos.items():
        c = color_of[n] if color_of else INK
        ax.add_patch(Circle((x, y), r, facecolor=c, edgecolor=PAPER, lw=0.8 * PT, zorder=3))


def captions(G, info):
    """Per frame: CAPTIONS with the data's numbers filled in."""
    values = {"players": G.number_of_nodes(), "pairs": G.number_of_edges(),
              "max_games": max(w for *_, w in G.edges(data="weight")), "communities": len(info)}
    return {step: (head.format(**values), detail.format(**values))
            for step, (head, detail) in CAPTIONS.items()}


def caption(ax, headline, detail):
    """Headline and detail, wrapped to stay inside the empty caption corner."""
    x, y = CAPTION_BOX[0] + 8, CAPTION_BOX[1] + 18
    for line in textwrap.wrap(headline, 36):
        ax.text(x, y, line, ha="left", va="baseline", fontsize=15, color=INK, zorder=5)
        y += 22
    y += 2
    for line in textwrap.wrap(detail, 62):
        ax.text(x, y, line, ha="left", va="baseline", fontsize=11, color=MUTED, zorder=5)
        y += 17


def main_frames(G, info):
    pos = layout(G)
    color_of = {p: c["color"] for c in info for p in c["members"]}
    text = captions(G, info)
    steps = {
        "v0": lambda ax: draw_dots(ax, pos),
        "v1": lambda ax: (draw_edges(ax, G, pos, weighted=False), draw_dots(ax, pos)),
        "v2": lambda ax: (draw_edges(ax, G, pos, weighted=True), draw_dots(ax, pos)),
        "v3": lambda ax: (draw_edges(ax, G, pos, weighted=True, color_of=color_of),
                          draw_dots(ax, pos, color_of=color_of), community_labels(ax, pos, info)),
    }
    for step, draw in steps.items():
        fig, ax = canvas()
        draw(ax)
        caption(ax, *text[step])
        footnote(ax, DATA_NOTE)
        save(fig, f"bulls-network-{step}")


def community_labels(ax, pos, info):
    """A boxed label on each community's cluster: its era and three most-rostered players.

    Placed at the median of the members' positions (robust to a few outlying
    players), with a white fill so it reads over the edges and a border in
    the community's color to tie it to its dots.
    """
    for c in info:
        x, y = np.median([pos[p] for p in c["members"]], axis=0)
        names = ", ".join(display_name(p).split()[-1] for p in c["top"][:3])
        ax.text(x, y, f"{c['era']}\n{names}", ha="center", va="center", ma="center",
                fontsize=12, color=INK, zorder=6, linespacing=1.3,
                bbox=dict(boxstyle="square,pad=0.45", facecolor=PAPER, edgecolor=c["color"],
                          lw=2.5 * PT))


def headshot(pid, size=128):
    path = HEADSHOTS / f"{pid}.jpg"
    if not path.exists():
        return None
    return np.asarray(Image.open(path).convert("RGB").resize((size, size), Image.LANCZOS))


def initials(name):
    return "".join(w[0] for w in name.split()[:2]).upper()


def closeup(G, appearances, c, k):
    players = c["top"][:CLOSEUP_N]
    S = G.subgraph(players)
    R = 34                                       # headshot radius, px
    box = (40 + R, 70 + R, W - 40 - R, H - 50 - R)
    # room for the photo plus its name label underneath
    pos = spread(fit(spring(S, 500), box), box, dx=2 * R + 40, dy=2 * R + 26)
    fig, ax = canvas()
    draw_edges(ax, S, pos, weighted=True)
    for p in players:
        x, y = pos[p]
        name = display_name(p)
        img = headshot(espn_id(p))
        clip = Circle((x, y), R, transform=ax.transData)
        if img is not None:
            im = ax.imshow(img, extent=(x - R, x + R, y + R, y - R), zorder=3, interpolation="lanczos")
            im.set_clip_path(clip)
        else:
            ax.add_patch(Circle((x, y), R, facecolor="#EEEEEE", edgecolor="none", zorder=3))
            ax.text(x, y, initials(name), ha="center", va="center", fontsize=16, color=INK, zorder=4)
        ax.add_patch(Circle((x, y), R, facecolor="none", edgecolor=c["color"], lw=3 * PT, zorder=4))
        ax.text(x, y + R + 4, name.split()[-1], ha="center", va="top", fontsize=11, color=INK, zorder=5,
                bbox=dict(boxstyle="round,pad=0.15", facecolor=PAPER, edgecolor="none", alpha=0.8))
    ax.text(24, 30, CLOSEUP_TITLE.format(k=k, era=c["era"]), ha="left", va="baseline",
            fontsize=18, color=c["color"])
    ax.text(24, 52, CLOSEUP_SUBTITLE.format(shown=len(players), members=len(c["members"])),
            ha="left", va="baseline", fontsize=12, color=MUTED)
    footnote(ax, PHOTO_NOTE)
    save(fig, f"bulls-community-{k}")


def main():
    G, appearances, info = analyze()
    print(f"{G.number_of_nodes()} players, {G.number_of_edges()} pairs, {len(info)} communities")
    for k, c in enumerate(info, 1):
        print(f"  {k}: {len(c['members'])} players, {c['era']}: "
              + ", ".join(display_name(p) for p in c["top"][:5]))
    main_frames(G, info)
    for k, c in enumerate(info, 1):
        closeup(G, appearances, c, k)


if __name__ == "__main__":
    main()
