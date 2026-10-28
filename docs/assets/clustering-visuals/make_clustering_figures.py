#!/usr/bin/env python3
"""Clustering figures: k-means, hierarchical clustering, DBSCAN, and cluster evaluation.

NOTICE: this file was substantially drafted by an LLM coding system and has not
yet been reviewed. Check every figure against the slide it illustrates.

Follows docs/assets/STYLE.md and mirrors week9/make_week9_figures.py: grayscale
neutrals, vendored Libre Franklin drawn as paths so each SVG is self-contained,
numbered step sets (`name-v0.svg`, `name-v1.svg`, ...) for r-stack fragments.

Color carries one meaning throughout:
  * orange = what the algorithm computes or is asked about: centroids,
    medoids, the newest merge, the point whose silhouette we compute.
  * clusters are grays plus a shape (circle, square, triangle), so they
    survive grayscale printing and never look like a "true" label.
  * true species, when shown, follow Week 9: Chinstrap is the orange
    triangle; Adélie a steel circle; Gentoo an ink square.
  * CTA route colors appear only on the one "ground truth" map of the lines,
    per the CTA developer branding guidelines quoted in STYLE.md.
  * The one exception to gray clusters is the condo-sales map: thousands of
    dots hide shapes, so its three largest clusters take Okabe-Ito hues (blue, bluish green, reddish purple), with orange left out so it stays the accent. The last map (Eps = 1 km) also gives its four smaller clusters in view the rest of Okabe-Ito (sky blue, vermilion, yellow, black), each labeled.

Canvases:
  * SPLIT (900 x 700) for the right column of a `.golden-figure` split slide;
    the penguin plot is nearly square, so a golden rectangle would waste width.
  * MAP (640 x 860) for the L-station maps, which are taller than wide.
  * GOLDEN (1000 x 618) for full-width `.image-frame-slide` figures.
  Step sets are saved uncropped so frames line up pixel for pixel.

Data:
  * Palmer Penguins, `datasets/classification-examples/penguins.csv`: the 342
    penguins with all measurements; bill length and flipper length,
    standardized, following DSFI ch. 9.
  * CTA L stops, `datasets/chicago-l-stations/`: one point per station
    (MAP_ID), 144 stations, projected to kilometers from the mean latitude.
  * The k-medoids, linkage, agglomerative-step, DBSCAN-point, DBSCAN-walkthrough,
    cohesion, and shape-comparison points are synthetic or hand-placed.
  Appendix examples:
  * CTA daily station entries, `datasets/cta-ridership/`: 2025 medians per
    station (weekday size, weekend and seasonal ratios, spikiness, 2025 vs. 2019),
    standardized, K = 4.
  * Movie reviews, `datasets/movie-reviews/`: TF-IDF, LSA to 100 dimensions, K = 6;
    also positive and negative word counts (Hu and Liu's opinion lexicon), K = 3.
  * Zachary's karate club, as packaged by networkx; spectral split in two (Week 12).
  * Two Ashland photos, `orange-line-stops-better/stop11-ashland-a.jpg` (CC BY-SA 3.0)
    and `-b.jpg` (CC BY-SA 4.0), recolored by k-means in CIELAB; saved as PNG/JPG.
  See SOURCES.md in this folder.

Usage:  python3 make_clustering_figures.py [name ...]
"""

from __future__ import annotations

import html
import re
import sys
from functools import lru_cache, partial
from pathlib import Path

import matplotlib

matplotlib.use("Agg")

import matplotlib.dates
import matplotlib.text
import matplotlib.pyplot as plt
import networkx as nx
import numpy as np
import polars as pl
from matplotlib import font_manager
from matplotlib.patches import Circle, Rectangle
from scipy.cluster.hierarchy import dendrogram, linkage
from scipy.optimize import linear_sum_assignment
from sklearn.cluster import DBSCAN, AgglomerativeClustering, KMeans
from sklearn.datasets import make_blobs, make_circles, make_moons
from sklearn.decomposition import TruncatedSVD
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics import adjusted_rand_score, silhouette_samples, silhouette_score
from sklearn.neighbors import NearestNeighbors
from sklearn.preprocessing import normalize

OUT_DIR = Path(__file__).resolve().parent
REPO_ROOT = OUT_DIR.parents[2]
FONT_PATH = OUT_DIR.parent / "fonts" / "libre-franklin" / "LibreFranklin-Regular.ttf"
PENGUIN_CSV = REPO_ROOT / "datasets" / "classification-examples" / "penguins.csv"
L_STOPS_CSV = REPO_ROOT / "datasets" / "chicago-l-stations" / "CTA_List_of_'L'_Stops_20260527.csv"

# STYLE.md palette
INK = "#1A1A1A"
STEEL = "#565A5C"
MUTED = "#777777"
QUIET = "#AAAAAA"
BORDER = "#DDDDDD"
SOFT_GRAY = "#F4F4F2"
PAPER = "#FFFFFF"
ORANGE = "#F9461C"
ORANGE_TINT = "#FDE3DA"

# Official CTA 'L' route colors (STYLE.md), for the ground-truth map only.
CTA = {"RED": "#C60C30", "BLUE": "#00A1DE", "BRN": "#62361B", "G": "#009B3A",
       "O": "#F9461C", "P": "#522398", "Pnk": "#E27EA6", "Y": "#F9E300"}

PHI = (1 + 5**0.5) / 2
DPI = 100
GOLDEN = (1000, round(1000 / PHI))
SPLIT = (900, 700)
MAP = (640, 860)

SPECIES_STYLE = {"Adelie": ("o", STEEL, PAPER, "Adélie"),
                 "Chinstrap": ("^", ORANGE, PAPER, "Chinstrap"),
                 "Gentoo": ("s", INK, PAPER, "Gentoo")}
SPECIES_ORDER = ["Adelie", "Chinstrap", "Gentoo"]

FIGURES: dict[str, callable] = {}


def figure(name: str):
    def wrap(fn):
        FIGURES[name] = fn
        return fn
    return wrap


def steps(name: str, n: int):
    def wrap(fn):
        for i in range(n):
            FIGURES[f"{name}-v{i}"] = (lambda i=i: fn(i))
        return fn
    return wrap


# ------------------------------------------------------------------ canvases

def fixed_fig(size, left, right, top, bottom):
    """A fixed canvas with one axes inset by pixel margins, saved uncropped."""
    width, height = size
    fig = plt.figure(figsize=(width / DPI, height / DPI), dpi=DPI)
    fig.patch.set_facecolor(PAPER)
    ax = fig.add_axes([left / width, bottom / height,
                       (width - left - right) / width, (height - top - bottom) / height])
    ax.set_facecolor(PAPER)
    fig.fixed_layout = True
    return fig, ax


def equal_fig(size, xlim, ylim, *, top=60, bottom=64, side_min=70):
    """`fixed_fig` whose plot area has the data's aspect, centered left-right."""
    width, height = size
    h = height - top - bottom
    w = h * (xlim[1] - xlim[0]) / (ylim[1] - ylim[0])
    if w > width - 2 * side_min:  # too wide: shrink height instead
        w = width - 2 * side_min
        h = w * (ylim[1] - ylim[0]) / (xlim[1] - xlim[0])
        bottom = height - top - h
    side = (width - w) / 2
    fig, ax = fixed_fig(size, side, side, top, bottom)
    ax.set_xlim(*xlim)
    ax.set_ylim(*ylim)
    ax.set_aspect("equal")
    return fig, ax


def tidy(ax, *, grid="both", spines=("left", "bottom")):
    for side in ("top", "right", "left", "bottom"):
        ax.spines[side].set_visible(side in spines)
        ax.spines[side].set_color(BORDER)
    if grid:
        ax.grid(axis=grid, color=BORDER, linewidth=0.8, alpha=0.7)
    ax.set_axisbelow(True)
    ax.tick_params(colors=STEEL, labelsize=13, length=0)
    for lbl in (ax.xaxis.label, ax.yaxis.label):
        lbl.set_color(STEEL)
        lbl.set_fontsize(15)
    return ax


def ylabel_top(ax, text):
    """STYLE.md: horizontal y-label, left-aligned above the axis."""
    ax.set_ylabel(text, rotation=0, ha="left", va="bottom", color=STEEL, fontsize=15)
    ax.yaxis.set_label_coords(0, 1.02)


def bare(ax):
    ax.set_xticks([])
    ax.set_yticks([])
    for s in ax.spines.values():
        s.set_visible(False)


def note(ax, text, *, x=0.03, y=0.985, color=INK, size=18, ha="left", va="top", fig=True):
    """Headline text; by default at the top-left of the canvas, clear of the y-label."""
    tr = ax.figure.transFigure if fig else ax.transAxes
    ax.text(x, y, text, transform=tr, fontsize=size, color=color, ha=ha, va=va)


def save(fig, name):
    raster = getattr(fig, "raster", None)  # photo figures: "png" or "jpg"
    out = OUT_DIR / f"{name}.{raster or 'svg'}"
    if raster:
        kw = {"pil_kwargs": {"quality": 92}} if raster == "jpg" else {}
        fig.savefig(out, format="jpeg" if raster == "jpg" else raster, facecolor=PAPER, dpi=DPI, **kw)
    elif getattr(fig, "fixed_layout", False):
        fig.savefig(out, format="svg", facecolor=PAPER)
    else:
        fig.savefig(out, format="svg", facecolor=PAPER, bbox_inches="tight", pad_inches=0.12)
    plt.close(fig)
    print(f"  wrote {out.relative_to(REPO_ROOT)}")


# --------------------------------------------------------------------- marks

def cluster_points(ax, X, labels, *, size=70, alpha=1.0, zorder=3):
    """Gray shapes by cluster; label -1 (noise) as small hollow rings."""
    X, labels = np.asarray(X), np.asarray(labels)
    noise = labels < 0
    if noise.any():
        ax.scatter(X[noise, 0], X[noise, 1], s=size * 0.6, facecolor=PAPER,
                   edgecolor=QUIET, linewidth=1.3, zorder=zorder - 0.5)
    for k in np.unique(labels[~noise]):
        m, fill, edge = CLUSTER_STYLE[k % 3]
        pts = X[labels == k]
        ax.scatter(pts[:, 0], pts[:, 1], marker=m, s=size * (1.25 if m == "^" else 1.0),
                   color=fill, edgecolor=edge, linewidth=0.7, alpha=alpha, zorder=zorder)


def unassigned(ax, X, *, size=70, zorder=2):
    ax.scatter(X[:, 0], X[:, 1], s=size, facecolor=PAPER, edgecolor=QUIET,
               linewidth=1.3, zorder=zorder)


def species_points(ax, X, species, *, size=70, zorder=3):
    for sp in SPECIES_ORDER:
        m, fill, edge, _ = SPECIES_STYLE[sp]
        pts = X[species == sp]
        ax.scatter(pts[:, 0], pts[:, 1], marker=m, s=size * (1.25 if m == "^" else 1.0),
                   color=fill, edgecolor=edge, linewidth=0.7, zorder=zorder)


def species_legend(ax, *, x=0.03, y=0.985, size=17, fig=True, va="top"):
    """Species names after their glyphs, left to right (default: top-left of the canvas)."""
    glyph = {"o": "●", "^": "▲", "s": "■"}
    tr = ax.figure.transFigure if fig else ax.transAxes
    for sp in SPECIES_ORDER:
        m, fill, _, name = SPECIES_STYLE[sp]
        ax.text(x, y, glyph[m], transform=tr, color=fill, fontsize=size, ha="left", va=va)
        ax.text(x + 0.035, y, name, transform=tr, color=INK, fontsize=size, ha="left", va=va)
        x += 0.06 + 0.014 * len(name)


def centroids(ax, C, *, size=420, zorder=6):
    C = np.atleast_2d(C)
    ax.scatter(C[:, 0], C[:, 1], marker="X", s=size, color=ORANGE, edgecolor=INK,
               linewidth=1.4, zorder=zorder)


def arrow(ax, a, b, *, color=INK, lw=2.0, ls="-", zorder=5):
    ax.annotate("", xy=b, xytext=a, zorder=zorder,
                arrowprops=dict(arrowstyle="-|>,head_length=0.6,head_width=0.3",
                                color=color, lw=lw, linestyle=ls, shrinkA=0, shrinkB=10))


# ------------------------------------------------------------------- penguins

PENG_LIM = ((-2.5, 3.2), (-2.4, 2.5))


def penguins(cols=("bill_length_mm", "flipper_length_mm")):
    """Penguins with all four measurements: standardized X, species, raw mean and SD."""
    df = pl.read_csv(PENGUIN_CSV, null_values="NA").drop_nulls(
        ["bill_length_mm", "bill_depth_mm", "flipper_length_mm", "body_mass_g"])
    X = df.select(cols).to_numpy().astype(float)
    mu, sd = X.mean(axis=0), X.std(axis=0)
    return (X - mu) / sd, df["species"].to_numpy(), mu, sd


def penguin_fig(size=SPLIT):
    return equal_fig(size, *PENG_LIM, top=110)


def penguin_axes(ax, mu, sd):
    """Standardized axes, labeled in millimeters."""
    tidy(ax, grid=None)
    xt, yt = np.arange(35, 61, 5), np.arange(180, 231, 10)
    ax.set_xticks((xt - mu[0]) / sd[0], [str(v) for v in xt])
    ax.set_yticks((yt - mu[1]) / sd[1], [str(v) for v in yt])
    ax.set_xlabel("Bill length (mm)")
    ylabel_top(ax, "Flipper length (mm)")


def match_to_species(labels, species):
    """Relabel clusters so cluster k is the one most like SPECIES_ORDER[k] (when K = 3).

    Keeps a cluster's shape the same as its matching species, for every figure."""
    k = labels.max() + 1
    if k != 3:
        return labels
    from itertools import permutations
    best = max(permutations(range(3)),
               key=lambda p: sum(np.sum((labels == p[i]) & (species == SPECIES_ORDER[i]))
                                 for i in range(3)))
    out = np.empty_like(labels)
    for i, c in enumerate(best):
        out[labels == c] = i
    return out


# Cluster k is drawn with CLUSTER_STYLE[k % 3]: (marker, fill, edge), the shape of
# SPECIES_ORDER[k] (Adélie circle, Chinstrap triangle, Gentoo square) in grays.
CLUSTER_STYLE = [("o", STEEL, PAPER), ("^", QUIET, STEEL), ("s", INK, PAPER)]


@steps("penguins-labels", 2)
def penguins_labels(step):
    Z, species, mu, sd = penguins()
    fig, ax = penguin_fig()
    penguin_axes(ax, mu, sd)
    if step == 0:
        species_points(ax, Z, species)
        species_legend(ax)
    else:
        ax.scatter(Z[:, 0], Z[:, 1], s=70, color=STEEL, edgecolor=PAPER, linewidth=0.7)
        note(ax, "Unsupervised: the same 342 penguins, no labels")
    return fig


# k-means by hand (Lloyd's algorithm) from three fixed starting penguins.
# Rows 321, 213, 233: the start (seed 7 of a search) that takes the most
# visible path to the K = 3 solution, SSE 381 -> 158.
KMEANS_START = [321, 213, 233]


def lloyd_history(Z, start, iters=3):
    """[(centers, labels)] for: start, then each (assign, refit) pair."""
    C = Z[start].copy()
    hist = [(C.copy(), None)]
    for _ in range(iters):
        lab = ((Z[:, None, :] - C[None]) ** 2).sum(-1).argmin(1)
        hist.append((C.copy(), lab))
        C = np.array([Z[lab == k].mean(axis=0) for k in range(len(C))])
        hist.append((C.copy(), lab))
    return hist


def sse(Z, C, lab):
    return float(((Z - C[lab]) ** 2).sum())


@steps("kmeans-penguins", 8)
def kmeans_penguins(step):
    Z, species, mu, sd = penguins()
    hist = lloyd_history(Z, KMEANS_START, iters=3)
    final = KMeans(3, n_init=10, random_state=0).fit(Z)
    fig, ax = penguin_fig()
    penguin_axes(ax, mu, sd)
    if step == 0:
        unassigned(ax, Z)
        note(ax, "342 penguins, K = 3")
        return fig
    if step == 7:
        lab = match_to_species(final.labels_, species)
        C = np.array([Z[lab == k].mean(axis=0) for k in range(3)])
        cluster_points(ax, Z, lab)
        centroids(ax, C)
        note(ax, f"Converged: assignments stop changing. SSE = {sse(Z, C, lab):.1f}")
        return fig
    C, lab = hist[step - 1]
    # Keep each cluster's shape fixed across frames: use the final matching.
    order = match_to_species(final.labels_, species)
    if lab is None:
        unassigned(ax, Z)
        centroids(ax, C)
        note(ax, "Start: pick 3 penguins at random as centroids")
        return fig
    # Map this frame's cluster ids onto the final ids by majority overlap.
    remap = {k: np.bincount(order[lab == k], minlength=3).argmax() for k in range(3)}
    shown = np.array([remap[k] for k in lab])
    cluster_points(ax, Z, shown)
    it = step // 2
    if step % 2 == 0:  # assignment
        centroids(ax, C)
        note(ax, f"Iteration {it}, assign: each penguin joins its nearest centroid. "
                 f"SSE = {sse(Z, C, lab):.1f}", size=16)
    else:  # refit
        C_old = hist[step - 2][0]
        for a, b in zip(C_old, C):
            arrow(ax, a, b, color=INK, lw=2.2, ls="--")
        centroids(ax, C)
        note(ax, f"Iteration {it}, refit: move each centroid to its cluster's mean. "
                 f"SSE = {sse(Z, C, lab):.1f}", size=16)
    return fig


@steps("kmeans-restarts", 2)
def kmeans_restarts(step):
    """Same data, same K, two random starts: a local optimum, then the better one."""
    Z, species, mu, sd = penguins()
    seed = {0: 16, 1: 0}[step]  # seed 16 is the first of 200 that gets stuck
    km = KMeans(3, init="random", n_init=1, random_state=seed).fit(Z)
    lab = match_to_species(km.labels_, species)
    C = np.array([Z[lab == k].mean(axis=0) for k in range(3)])
    fig, ax = penguin_fig()
    penguin_axes(ax, mu, sd)
    cluster_points(ax, Z, lab)
    centroids(ax, C)
    msg = {0: "Run A: stuck in a local optimum", 1: "Run B: a better optimum"}[step]
    note(ax, f"{msg}. SSE = {km.inertia_:.1f}")
    return fig


@steps("ffh-penguins", 3)
def ffh_penguins(step):
    """Furthest-first: each new centroid is the penguin farthest from those chosen."""
    Z, species, mu, sd = penguins()
    chosen = [int(np.argmin(((Z - Z.mean(0)) ** 2).sum(1)))]  # start near the middle
    for _ in range(2):
        d = np.min([((Z - Z[c]) ** 2).sum(1) for c in chosen], axis=0)
        chosen.append(int(np.argmax(d)))
    fig, ax = penguin_fig()
    penguin_axes(ax, mu, sd)
    unassigned(ax, Z)
    centroids(ax, Z[chosen[: step + 1]])
    if step >= 1:
        far = chosen[step]
        nearest = chosen[int(np.argmin([((Z[far] - Z[c]) ** 2).sum() for c in chosen[:step]]))]
        arrow(ax, Z[nearest], Z[far], color=INK, lw=2, ls="--")
    msg = {0: "Centroid 1: a random penguin",
           1: "Centroid 2: the penguin farthest from centroid 1",
           2: "Centroid 3: farthest from both. Often an outlier"}[step]
    note(ax, msg)
    return fig


@steps("elbow-penguins", 2)
def elbow_penguins(step):
    Z, *_ = penguins()
    ks = np.arange(1, 10)
    sses = [KMeans(k, n_init=10, random_state=0).fit(Z).inertia_ for k in ks]
    fig, ax = fixed_fig(SPLIT, 110, 50, 80, 80)
    tidy(ax, grid="y")
    ax.plot(ks, sses, color=STEEL, lw=2.5, marker="o", ms=9, mfc=STEEL, mec=PAPER, zorder=3)
    ax.set_xticks(ks)
    ax.set_xlim(0.5, 9.5)
    ax.set_ylim(0, 720)
    ax.set_xlabel("Number of clusters, K")
    ylabel_top(ax, "Total SSE (standardized units²)")
    if step == 1:
        ax.scatter([3], [sses[2]], s=600, facecolor="none", edgecolor=ORANGE, lw=3, zorder=4)
        ax.annotate("the elbow: K = 3", xy=(3, sses[2]), xytext=(4.2, 330), fontsize=17,
                    color=INK, arrowprops=dict(arrowstyle="-", color=INK, lw=1.5))
        ax.annotate(f"K = 9 is lower still ({sses[-1]:.0f})", xy=(9, sses[-1]), xytext=(6.2, 170),
                    fontsize=15, color=STEEL, arrowprops=dict(arrowstyle="-", color=STEEL, lw=1.2))
    return fig


@steps("scaling-penguins", 2)
def scaling_penguins(step):
    """k-means on bill length (mm) and body mass (g): raw units vs. standardized."""
    Zs, species, mu, sd = penguins(("bill_length_mm", "body_mass_g"))
    X = Zs * sd + mu
    fit_on = X if step == 0 else Zs
    km = KMeans(3, n_init=10, random_state=0).fit(fit_on)
    lab = match_to_species(km.labels_, species)
    ari = adjusted_rand_score(species, lab)
    fig, ax = fixed_fig(SPLIT, 110, 50, 130, 80)
    tidy(ax, grid=None)
    if step == 0:
        cluster_points(ax, X, lab)
        ax.set_xlabel("Bill length (mm)")
        ylabel_top(ax, "Body mass (g)")
        ax.set_xlim(31, 61)
        ax.set_ylim(2600, 6400)
    else:
        # plot what k-means saw: both axes in SDs from the mean, one unit the same length on each
        cluster_points(ax, Zs, lab)
        ax.set_xlabel("Bill length (SDs from mean)")
        ylabel_top(ax, "Body mass (SDs from mean)")
        ax.set_xlim(-2.6, 3.2)
        ax.set_ylim(-2.2, 2.8)
        ax.set_aspect("equal")
        ax.set_xticks(range(-2, 4))
        ax.set_yticks(range(-2, 3))
    msg = {0: "Raw units: grams swamp millimeters",
           1: "Standardized: both features count"}[step]
    note(ax, f"{msg}\n(agreement with species: ARI = {ari:.2f})")
    return fig


# ------------------------------------------------------------------ k-medoids

KMED_PTS = np.array([(1.0, 1.2), (1.6, 0.8), (1.3, 1.9), (2.0, 1.5), (0.7, 1.7),
                     (1.8, 2.2), (2.3, 1.0), (8.6, 1.6)])


@steps("kmedoids", 2)
def kmedoids(step):
    X = KMED_PTS
    fig, ax = equal_fig(SPLIT, (0, 9.5), (-0.6, 3.6), top=90, bottom=40)
    bare(ax)
    ax.scatter(X[:, 0], X[:, 1], s=160, color=STEEL, edgecolor=PAPER, lw=1, zorder=3)
    ax.annotate("one outlier", xy=X[-1], xytext=(7.2, 3.0), fontsize=16, color=STEEL,
                arrowprops=dict(arrowstyle="-", color=STEEL, lw=1.2))
    c = X.mean(axis=0)
    centroids(ax, c)
    ax.annotate("centroid (mean)\npulled toward the outlier", xy=c, xytext=(3.4, -0.45),
                fontsize=16, color=INK, arrowprops=dict(arrowstyle="-", color=INK, lw=1.2))
    if step == 1:
        cost = [np.linalg.norm(X - x, axis=1).sum() for x in X]
        m = X[int(np.argmin(cost))]
        ax.scatter([m[0]], [m[1]], s=900, facecolor="none", edgecolor=ORANGE, lw=3.5, zorder=5)
        ax.annotate("medoid: a real point,\nstays with the group", xy=m, xytext=(-0.1, 3.0),
                    fontsize=16, color=INK, arrowprops=dict(arrowstyle="-", color=INK, lw=1.2))
    return fig


def medoids(ax, M, *, zorder=6):
    """A medoid is a real penguin: an orange dot, ringed so it reads as chosen."""
    M = np.atleast_2d(M)
    ax.scatter(M[:, 0], M[:, 1], s=150, color=ORANGE, edgecolor=INK, linewidth=1.2, zorder=zorder)
    ax.scatter(M[:, 0], M[:, 1], s=650, facecolor="none", edgecolor=ORANGE, lw=3, zorder=zorder)


def medoid_history(Z, start, iters=3):
    """[(medoid rows, labels)] for: start, then each (assign, update) pair, Euclidean."""
    D = np.linalg.norm(Z[:, None, :] - Z[None], axis=-1)
    med = list(start)
    hist = [(med, None)]
    for _ in range(iters):
        lab = D[:, med].argmin(1)
        hist.append((med, lab))
        # New medoid: the member with the smallest total distance to its cluster.
        med = [int(np.flatnonzero(lab == k)[D[np.ix_(lab == k, lab == k)].sum(1).argmin()])
               for k in range(len(med))]
        hist.append((med, lab))
    return hist, D


@steps("kmedoids-penguins", 8)
def kmedoids_penguins(step):
    """k-medoids by alternating assign/update, from the same start as kmeans-penguins."""
    Z, species, mu, sd = penguins()
    hist, D = medoid_history(Z, KMEANS_START, iters=3)
    fig, ax = penguin_fig(GOLDEN)
    penguin_axes(ax, mu, sd)
    med, lab = hist[min(step, 6)]
    if lab is None:
        unassigned(ax, Z)
        medoids(ax, Z[med])
        note(ax, "Start: the same 3 random penguins as k-means, now as medoids")
        return fig
    if step == 7:  # one more assignment: 6 penguins move, the medoids do not
        lab = D[:, med].argmin(1)
    final = match_to_species(lab if step == 7 else hist[6][1], species)
    remap = {k: np.bincount(final[lab == k], minlength=3).argmax() for k in range(3)}
    cluster_points(ax, Z, np.array([remap[k] for k in lab]))
    cost = D[np.arange(len(Z)), np.array(med)[lab]].sum()
    it = (step + 1) // 2
    if step == 7:
        medoids(ax, Z[med])
        note(ax, f"Converged: the medoids stop changing. Total distance = {cost:.1f}", size=16)
    elif step % 2 == 1:  # assignment
        medoids(ax, Z[med])
        note(ax, f"Iteration {it}, assign: each penguin joins its nearest medoid.\n"
                 f"Total distance = {cost:.1f}", size=16)
    else:  # update
        for a, b in zip(hist[step - 1][0], med):
            if a != b:
                arrow(ax, Z[a], Z[b], color=INK, lw=2.2, ls="--")
        medoids(ax, Z[med])
        note(ax, f"Iteration {it}, update: the member closest to the rest of its cluster "
                 f"is the new medoid.\nTotal distance = {cost:.1f}", size=16)
    return fig


# ------------------------------------------------------------------- linkage

LINK_A = np.array([(1.0, 1.0), (1.6, 2.2), (2.2, 1.7)])
LINK_B = np.array([(4.4, 2.3), (5.2, 2.8), (5.6, 1.3), (6.3, 2.3)])


@steps("linkage", 4)
def linkage_fig(step):
    A, B = LINK_A, LINK_B
    fig, ax = equal_fig(SPLIT, (0.2, 7.1), (0.0, 3.8), top=90, bottom=40)
    bare(ax)
    for P, name, xy in ((A, "Cluster A", (1.0, 3.2)), (B, "Cluster B", (5.0, 3.6))):
        c = P.mean(axis=0)
        r = np.max(np.linalg.norm(P - c, axis=1)) + 0.45
        ax.add_patch(Circle(c, r, fill=False, edgecolor=QUIET, lw=1.5, ls="--"))
        ax.text(*xy, name, fontsize=16, color=STEEL)
    ax.scatter(A[:, 0], A[:, 1], s=170, marker="o", color=STEEL, edgecolor=PAPER, zorder=4)
    ax.scatter(B[:, 0], B[:, 1], s=170, marker="s", color=INK, edgecolor=PAPER, zorder=4)
    D = np.linalg.norm(A[:, None] - B[None], axis=2)
    if step == 0:
        i, j = np.unravel_index(D.argmin(), D.shape)
        ax.plot(*zip(A[i], B[j]), color=ORANGE, lw=3.5, zorder=3)
        note(ax, f"Single link (MIN): closest pair, {D.min():.1f}")
    elif step == 1:
        i, j = np.unravel_index(D.argmax(), D.shape)
        ax.plot(*zip(A[i], B[j]), color=ORANGE, lw=3.5, zorder=3)
        note(ax, f"Complete link (MAX): farthest pair, {D.max():.1f}")
    elif step == 2:
        for a in A:
            for b in B:
                ax.plot(*zip(a, b), color=ORANGE, lw=1.4, alpha=0.75, zorder=3)
        note(ax, f"Average link: mean of all {D.size} pairs, {D.mean():.1f}")
    else:
        ca, cb, cab = A.mean(0), B.mean(0), np.r_[A, B].mean(0)
        sse = lambda P, c: ((P - c) ** 2).sum()
        inc = sse(np.r_[A, B], cab) - sse(A, ca) - sse(B, cb)
        for P, c in ((A, ca), (B, cb)):
            for p in P:
                ax.plot(*zip(p, c), color=QUIET, lw=1.2, zorder=2)
        for p in np.r_[A, B]:
            ax.plot(*zip(p, cab), color=ORANGE, lw=1.2, ls="--", zorder=2)
        centroids(ax, np.r_[[ca], [cb]], size=260)
        centroids(ax, cab, size=420)
        note(ax, f"Ward's: how much SSE grows if A and B merge, +{inc:.1f}",
             )
    return fig


# --------------------------------------------------- agglomerative, step by step

AGG_PTS = np.array([(1.0, 3.6), (1.6, 3.1), (4.0, 3.5), (3.3, 1.2), (4.5, 0.9), (1.2, 0.6)])


def link_tree(Lm, n, upto):
    """Leaf x positions and the U-shapes of the first `upto` merges of linkage matrix Lm."""
    order = dendrogram(Lm, no_plot=True)["leaves"]
    xpos = {leaf: i for i, leaf in enumerate(order)}
    height = {i: 0.0 for i in range(n)}
    shapes = []
    for k, (a, b, h, _) in enumerate(Lm[:upto]):
        a, b, new = int(a), int(b), n + k
        shapes.append((xpos[a], height[a], xpos[b], height[b], h))
        xpos[new] = (xpos[a] + xpos[b]) / 2
        height[new] = h
    return order, shapes


@steps("agglomerative-steps", 6)
def agglomerative_steps(step):
    X = AGG_PTS
    n = len(X)
    Lm = linkage(X, method="single")
    fig = plt.figure(figsize=(GOLDEN[0] / DPI, GOLDEN[1] / DPI), dpi=DPI)
    fig.patch.set_facecolor(PAPER)
    fig.fixed_layout = True
    ax = fig.add_axes([0.04, 0.08, 0.46, 0.8])
    ax.set_xlim(0.2, 5.3)
    ax.set_ylim(0.0, 4.3)
    ax.set_aspect("equal")
    bare(ax)
    # Which points are already joined: union the first `step` merges.
    members = {i: [i] for i in range(n)}
    for k, (a, b, h, _) in enumerate(Lm[:step]):
        members[n + k] = members[int(a)] + members[int(b)]
        # single link: draw the closest pair that made this merge
        P, Q = members[int(a)], members[int(b)]
        D = np.linalg.norm(X[P][:, None] - X[Q][None], axis=2)
        i, j = np.unravel_index(D.argmin(), D.shape)
        newest = k == step - 1
        ax.plot(*zip(X[P[i]], X[Q[j]]), color=ORANGE if newest else INK,
                lw=3.5 if newest else 2.2, zorder=2)
    ax.scatter(X[:, 0], X[:, 1], s=520, color=PAPER, edgecolor=INK, lw=2.2, zorder=3)
    for i, (x, y) in enumerate(X):
        ax.text(x, y, str(i + 1), ha="center", va="center_baseline", fontsize=17, color=INK, zorder=4)
    note(ax, "Points", x=0.0, y=1.03, fig=False, va="bottom")

    dx = fig.add_axes([0.58, 0.16, 0.38, 0.72])
    tidy(dx, grid="y", spines=("left",))
    order, shapes = link_tree(Lm, n, step)
    for k, (xa, ha, xb, hb, h) in enumerate(shapes):
        newest = k == step - 1
        dx.plot([xa, xa, xb, xb], [ha, h, h, hb], color=ORANGE if newest else INK,
                lw=3.5 if newest else 2.2)
    dx.set_xlim(-0.6, n - 0.4)
    dx.set_ylim(0, Lm[:, 2].max() * 1.1)
    dx.set_xticks(range(n), [str(i + 1) for i in order], fontsize=16)
    dx.tick_params(axis="x", colors=INK)
    ylabel_top(dx, "Merge distance (single link)")
    note(ax, ["Start: every point is its own cluster",
              "Merge the closest pair", "Merge the next closest",
              "Keep merging", "Keep merging", "One cluster left"][step],
         size=19)
    return fig


@steps("dendrogram-penguins", 3)
def dendrogram_penguins(step):
    """30 penguins (10 per species), three linkages."""
    Z, species, mu, sd = penguins()
    rng = np.random.default_rng(418)
    idx = np.concatenate([rng.choice(np.flatnonzero(species == s), 10, replace=False)
                          for s in SPECIES_ORDER])
    X, sp = Z[idx], species[idx]
    method = ["single", "average", "ward"][step]
    Lm = linkage(X, method=method)
    fig, ax = fixed_fig(GOLDEN, 90, 40, 100, 90)
    tidy(ax, grid="y", spines=("left",))
    d = dendrogram(Lm, ax=ax, no_labels=True, color_threshold=0,
                   above_threshold_color=INK, link_color_func=lambda k: INK)
    for coll in ax.collections:
        coll.set_linewidth(1.8)
    leaves = d["leaves"]
    xs = 5 + 10 * np.arange(len(leaves))
    top = Lm[:, 2].max()
    for x, leaf in zip(xs, leaves):
        m, fill, edge, _ = SPECIES_STYLE[sp[leaf]]
        ax.scatter([x], [-0.06 * top], marker=m, s=150, color=fill, edgecolor=edge,
                   clip_on=False, zorder=4)
    ax.set_ylim(-0.11 * top, top * 1.05)
    ylabel_top(ax, "Merge distance")
    species_legend(ax, x=0.0, y=-0.2, size=15, fig=False, va="bottom")
    title = {"single": "Single link: long chains, one late straggler at a time",
             "average": "Average link: compact groups, close to the species",
             "ward": "Ward's: the most even, compact groups"}[method]
    note(ax, title, size=19)
    return fig


# ---------------------------------------------------------------- L stations

def l_stations():
    """One row per station: km coordinates, name, Orange Line flag, line flags."""
    df = pl.read_csv(L_STOPS_CSV, infer_schema_length=0)
    lines = list(CTA)
    st = (df.group_by("MAP_ID")
            .agg(pl.first("STATION_NAME"), pl.first("Location"),
                 *[(pl.col(c) == "true").any().alias(c) for c in lines])
            .sort("MAP_ID"))
    ll = np.array([[float(v) for v in re.findall(r"-?\d+\.\d+", s)] for s in st["Location"]])
    lat0, lon0 = ll[:, 0].mean(), ll[:, 1].mean()
    X = np.c_[(ll[:, 1] - lon0) * 111.32 * np.cos(np.radians(lat0)), (ll[:, 0] - lat0) * 110.57]
    return X, st


L_LIM = ((-19.5, 7.5), (-20.5, 20.5))


def ashland_orange(st):
    return int(np.flatnonzero((st["STATION_NAME"] == "Ashland").to_numpy() & st["O"].to_numpy())[0])


def map_fig():
    fig, ax = equal_fig(MAP, *L_LIM, top=70, bottom=30, side_min=20)
    bare(ax)
    # 5 km scale bar, lower left
    x0, y0 = L_LIM[0][0] + 0.5, L_LIM[1][0] + 1.0
    ax.plot([x0, x0 + 5], [y0, y0], color=INK, lw=3, solid_capstyle="butt")
    ax.text(x0 + 2.5, y0 + 0.6, "5 km", ha="center", va="bottom", fontsize=14, color=INK)
    return fig, ax


def mark_ashland(ax, X, st, *, label=True):
    a = X[ashland_orange(st)]
    ax.scatter([a[0]], [a[1]], s=380, facecolor="none", edgecolor=ORANGE, lw=3, zorder=6)
    if label:
        ax.annotate("Ashland\n(Orange Line)", xy=a, xytext=(a[0] - 12.5, a[1] - 7.5), fontsize=14,
                    color=INK, arrowprops=dict(arrowstyle="-", color=INK, lw=1.2))


@steps("l-stations", 2)
def l_stations_fig(step):
    X, st = l_stations()
    fig, ax = map_fig()
    if step == 0:
        ax.scatter(X[:, 0], X[:, 1], s=40, color=STEEL, edgecolor=PAPER, lw=0.6, zorder=3)
        note(ax, f"{len(X)} 'L' stations, no line labels")
    else:
        flags = np.c_[[st[c].to_numpy() for c in CTA]].T
        multi = flags.sum(1) > 1
        for j, c in enumerate(CTA):
            only = flags[:, j] & ~multi
            ax.scatter(X[only, 0], X[only, 1], s=40, color=CTA[c], edgecolor=PAPER, lw=0.6, zorder=3)
        ax.scatter(X[multi, 0], X[multi, 1], s=40, color=PAPER, edgecolor=INK, lw=1.2, zorder=4)
        note(ax, "The 'answer' we never gave it: CTA lines\n(white = several lines)", size=16)
    mark_ashland(ax, X, st)
    return fig


@figure("l-kmeans")
def l_kmeans():
    X, st = l_stations()
    km = KMeans(8, n_init=10, random_state=0).fit(X)
    fig, ax = map_fig()
    cluster_points(ax, X, km.labels_, size=40)
    centroids(ax, km.cluster_centers_, size=220)
    note(ax, "k-means, K = 8: round blobs\nthat cut across the lines", size=17)
    return fig


@steps("l-linkage", 2)
def l_linkage(step):
    X, st = l_stations()
    method = ["single", "ward"][step]
    lab = AgglomerativeClustering(8, linkage=method).fit_predict(X)
    # Biggest cluster first, so the giant chain is always the steel circles.
    sizes = np.bincount(lab)
    rank = {c: r for r, c in enumerate(np.argsort(-sizes))}
    lab = np.array([rank[c] for c in lab])
    fig, ax = map_fig()
    cluster_points(ax, X, lab, size=40)
    msg = {"single": f"Single link, 8 clusters: one chain of\n{sizes.max()} stations, plus stragglers",
           "ward": "Ward's, 8 clusters: compact\nneighborhoods"}[method]
    note(ax, msg, size=17)
    return fig


DB_MINPTS = 3
DB_EPS = [0.8, 1.2, 2.0]


@figure("l-kdist")
def l_kdist():
    X, _ = l_stations()
    # n_neighbors counts the station itself, matching scikit-learn's min_samples.
    d = np.sort(NearestNeighbors(n_neighbors=DB_MINPTS).fit(X).kneighbors(X)[0][:, -1])
    fig, ax = fixed_fig(SPLIT, 110, 60, 80, 80)
    tidy(ax, grid="y")
    ax.plot(np.arange(len(d)), d, color=STEEL, lw=2.5)
    ax.set_xlim(0, len(d))
    ax.set_ylim(0, 5)
    for eps in DB_EPS:
        ax.axhline(eps, color=ORANGE if eps == 1.2 else QUIET, lw=2 if eps == 1.2 else 1.4, ls="--")
        ax.text(3, eps + 0.07, f"Eps = {eps} km", fontsize=14, color=INK if eps == 1.2 else STEEL)
    ax.set_xlabel("Stations, sorted by that distance")
    ylabel_top(ax, f"Distance to 2nd-nearest other station (km)")
    return fig


@steps("l-dbscan", 3)
def l_dbscan(step):
    X, st = l_stations()
    eps = DB_EPS[step]
    db = DBSCAN(eps=eps, min_samples=DB_MINPTS).fit(X)
    lab = db.labels_
    sizes = np.bincount(lab[lab >= 0])
    rank = {c: r for r, c in enumerate(np.argsort(-sizes))}
    lab = np.array([rank.get(c, -1) for c in lab])
    fig, ax = map_fig()
    cluster_points(ax, X, lab, size=40)
    a = ashland_orange(st)
    status = "noise" if lab[a] < 0 else "in a cluster"
    note(ax, f"Eps = {eps} km, MinPts = {DB_MINPTS}\n{len(sizes)} clusters, "
             f"{(lab < 0).sum()} noise (hollow)\nAshland: {status}",
         size=16)
    mark_ashland(ax, X, st, label=False)
    return fig


# --------------------------------------------------- condo sales, Cook County

SALES_CSV = REPO_ROOT / "datasets" / "cook-county-home-sales-2025" / "cook-county-home-sales-2025.csv"
CONDO_MINPTS = 40
CONDO_EPS = [None, 0.1, 0.2, 0.3, 0.5, 1.0]
CONDO_LIM = ((-43, 46), (-50, 26))  # the whole county, for the establishing shot
CONDO_ZOOM = ((-14, 28), (-13.5, 9))  # Rogers Park to Hyde Park, Oak Park in the west; labels sit in the lake
CONDO_NAMED = ["#0072B2", "#009E73", "#CC79A7"]  # Okabe-Ito, for the 3 largest clusters
CONDO_MORE = ["#56B4E9", "#D55E00", "#E6C700", INK]  # rest of Okabe-Ito (yellow darkened to show on white), for the other clusters on the last map


@lru_cache(maxsize=None)
def condo_sales():
    """2025 condo sales, one parcel per sale, projected to km from the mean location.

    Bulk sales repeat one row per unit (one 2025 sale covers 321 condo rows), so they
    would make a dense 'cluster' out of a single transaction; num_parcels_sale == 1 drops
    them. Coordinates are rounded to 3 decimals (~110 m), so some sales stack exactly.
    """
    df = (pl.read_csv(SALES_CSV, infer_schema_length=10000)
            .filter((pl.col("property_group") == "Condominium") & (pl.col("num_parcels_sale") == 1))
            .drop_nulls(["latitude", "longitude"]))
    lat, lon = df["latitude"].to_numpy(), df["longitude"].to_numpy()
    X = np.c_[(lon - lon.mean()) * 111.32 * np.cos(np.radians(lat.mean())), (lat - lat.mean()) * 110.57]
    area = [a.title().replace("Ohare", "O'Hare") if a else c.title()  # the data spells it OHARE
            for a, c in zip(df["chicago_community_area"], df["city"])]
    return X, np.array(area)


@steps("condos-dbscan", len(CONDO_EPS))
def condos_dbscan(step):
    """v0: the whole county, with the lakefront boxed; v1 on: DBSCAN by Eps, zoomed to that box."""
    X, area = condo_sales()
    eps = CONDO_EPS[step]
    lim = CONDO_LIM if eps is None else CONDO_ZOOM
    fig, ax = equal_fig(GOLDEN, *lim, top=80, bottom=20, side_min=20)
    bare(ax)
    bar = 10 if eps is None else 2
    pad = 0.02 * (lim[1][1] - lim[1][0])
    x0, y0 = lim[0][0] + pad, lim[1][0] + 2 * pad
    ax.plot([x0, x0 + bar], [y0, y0], color=INK, lw=3, solid_capstyle="butt")
    ax.text(x0 + bar / 2, y0 + pad, f"{bar} km", ha="center", va="bottom", fontsize=14, color=INK)
    if eps is None:
        ax.scatter(*X.T, s=4, color=STEEL, alpha=0.35, lw=0, zorder=3, rasterized=True)
        (zx0, zx1), (zy0, zy1) = CONDO_ZOOM
        ax.add_patch(Rectangle((zx0, zy0), zx1 - zx0, zy1 - zy0, fill=False, edgecolor=ORANGE,
                               lw=2, zorder=5))
        ax.text(zx1 + pad, zy1, "Next: the lakefront", ha="left", va="top", fontsize=14,
                color=INK)
        note(ax, f"{len(X):,} condo sales in Cook County, 2025\n(one unit per sale)", size=16)
        return fig
    lab = DBSCAN(eps=eps, min_samples=CONDO_MINPTS).fit_predict(X)
    sizes = np.bincount(lab[lab >= 0])
    rank = {c: r for r, c in enumerate(np.argsort(-sizes))}
    lab = np.array([rank.get(c, -1) for c in lab])
    noise = lab < 0
    named = len(CONDO_NAMED)
    (lx0, lx1), (ly0, ly1) = lim
    inside = (X[:, 0] > lx0) & (X[:, 0] < lx1) & (X[:, 1] > ly0) & (X[:, 1] < ly1)
    # on the last map few enough clusters are in view that each can take its own hue
    extra = [k for k in np.unique(lab[inside]) if k >= named] if eps == CONDO_EPS[-1] else []
    # 14,000 dots: raster keeps the SVG small; text stays vector
    ax.scatter(*X[noise].T, s=4, color=QUIET, alpha=0.35, lw=0, zorder=2, rasterized=True)
    ax.scatter(*X[(lab >= named) & ~np.isin(lab, extra)].T, s=7, color=MUTED, lw=0, zorder=3, rasterized=True)
    for k, color in [*enumerate(CONDO_NAMED), *zip(extra, CONDO_MORE[:len(extra)], strict=True)]:
        ax.scatter(*X[lab == k].T, s=9, color=color, lw=0, zorder=4, rasterized=True)

    def label(k, others=True):
        names, counts = np.unique(area[lab == k], return_counts=True)
        big = counts >= 0.02 * counts.sum()  # areas with at least 2% of the cluster
        more = (f" + {big.sum() - 1} more area{'s' if big.sum() > 2 else ''}"
                if others and big.sum() > 1 else "")
        return f"{names[counts.argmax()]}{more}\n{(lab == k).sum():,} sales"

    def anchor(seen):
        # the visible member nearest the visible median: matplotlib drops
        # an annotation whose anchor falls outside the axes
        return seen[np.argmin(((seen - np.median(seen, axis=0)) ** 2).sum(1))]

    def annotate(text, c, xy, color, **kw):
        return ax.annotate(text, c, xytext=xy, fontsize=13, color=INK, zorder=7, va="center",
                           multialignment="left", **kw,
                           bbox=dict(boxstyle="round,pad=0.3", facecolor=PAPER, edgecolor=color, lw=1.5),
                           arrowprops=dict(arrowstyle="-", color=color, lw=1.5, shrinkB=4))

    # name the three biggest clusters; a label goes out in the lake (east) unless
    # another named cluster lies east of it at that latitude, then inland (west)
    sides = {"east": [], "west": []}
    for k, color in enumerate(CONDO_NAMED):
        seen = X[(lab == k) & inside]
        if not len(seen):
            continue
        c = anchor(seen)
        other = (lab >= 0) & (lab < named) & (lab != k)
        east_blocked = np.any(other & (np.abs(X[:, 1] - c[1]) < 1) & (X[:, 0] > c[0]))
        sides["west" if east_blocked else "east"].append((c, seen, color, label(k)))
    renderer = fig.canvas.get_renderer()
    to_data = ax.transData.inverted()
    taken = [(lx0, ly0, x0 + bar + pad, y0 + 3 * pad)]  # label boxes so far, in km; the scale bar first
    for side, spots in sides.items():
        spots.sort(key=lambda t: -t[0][1])  # north to south, at least 3 km apart
        y = np.inf
        for c, seen, color, text in spots:
            y = min(y - 3, c[1], ly1 - 1.5)
            x = 15 if side == "east" else seen[:, 0].min() - 3
            ann = annotate(text, c, (x, y), color, ha="left" if side == "east" else "right")
            # a label that would run off the map slides back in; one pushed in
            # from the west edge drops below its cluster so it doesn't cover it
            # measure the text's size only (before drawing it reports no position;
            # its rounded box adds about 0.3 em, inside the 0.3 km margin below)
            box = matplotlib.text.Text.get_window_extent(ann, renderer)
            px, py = ax.transData.transform((x, y))
            px0 = px if side == "east" else px - box.width
            (bx0, by0), (bx1, by1) = to_data.transform(
                [(px0, py - box.height / 2), (px0 + box.width, py + box.height / 2)])
            dx = max(0, lx0 + 0.3 - bx0) - max(0, bx1 - (lx1 - 0.3))
            if side == "west" and dx > 0:
                y = min(y, seen[:, 1].min() - 2)
            y = max(y, ly0 + (by1 - by0) / 2 + 0.3)
            ann.set_position((x + dx, y))
            left = x + dx - (0 if side == "east" else bx1 - bx0)
            taken.append((left, y - (by1 - by0) / 2, left + bx1 - bx0, y + (by1 - by0) / 2))
    # the other clusters crowd the west side, with no lake to hold their labels:
    # each takes a short label in the open spot nearest its cluster, clear of every cluster's dots
    dots = X[(lab >= 0) & inside]
    for k, color in zip(extra, CONDO_MORE):
        seen = X[(lab == k) & inside]
        c = anchor(seen)
        ann = annotate(label(k, others=False), c, c, color, ha="center")
        box = matplotlib.text.Text.get_window_extent(ann, renderer)
        (bx0, by0), (bx1, by1) = to_data.transform([(0, 0), (box.width, box.height)])
        hw, hh = (bx1 - bx0) / 2 + 0.3, (by1 - by0) / 2 + 0.3
        gx, gy = np.meshgrid(np.arange(lx0 + hw, lx1 - hw, 0.25), np.arange(ly0 + hh, ly1 - hh, 0.25))
        gx, gy = gx.ravel(), gy.ravel()
        free = ~np.any((np.abs(dots[:, 0] - gx[:, None]) < hw) & (np.abs(dots[:, 1] - gy[:, None]) < hh), axis=1)
        for tx0, ty0, tx1, ty1 in taken:  # 0.3 more each side for the placed box's own padding
            free &= (gx + hw < tx0 - 0.3) | (gx - hw > tx1 + 0.3) | (gy + hh < ty0 - 0.3) | (gy - hh > ty1 + 0.3)
        gap = np.hypot(np.maximum(np.abs(gx - c[0]) - hw, 0), np.maximum(np.abs(gy - c[1]) - hh, 0))
        best = np.flatnonzero(free)[np.argmin(gap[free])]
        ann.set_position((gx[best], gy[best]))
        taken.append((gx[best] - hw, gy[best] - hh, gx[best] + hw, gy[best] + hh))
    shown = "on this map in color" if extra else "the 3 largest in color"
    note(ax, f"Eps = {eps} km, MinPts = {CONDO_MINPTS}\n{len(sizes)} clusters county-wide, "
             f"{shown}; {noise.mean():.0%} of sales are noise (light)", size=16)
    return fig


# Hand-placed so that with Eps = 1 and MinPts = 4 (counting the point itself):
# A is core, B is border (near A, too few neighbors of its own), C is noise.
DB_PTS = np.array([(2.0, 2.0), (2.6, 2.4), (1.5, 2.5), (2.3, 1.4), (1.6, 1.6),
                   (5.6, 1.6), (4.9, 0.9)])
DB_ROLE = {"core": 0, "border": 1, "noise": 5}


@steps("dbscan-points", 4)
def dbscan_points(step):
    X = DB_PTS
    eps, minpts = 1.0, 4
    n_near = (np.linalg.norm(X[:, None] - X[None], axis=2) <= eps).sum(1)
    core = n_near >= minpts
    fig, ax = equal_fig(SPLIT, (0.3, 7.0), (0.0, 4.4), top=100, bottom=30)
    bare(ax)
    ax.scatter(X[:, 0], X[:, 1], s=170, color=STEEL, edgecolor=PAPER, zorder=4)
    shows = ["core", "border", "noise"][:step]
    labels = {"core": f"Core: ≥ {minpts} points within Eps\n(counting itself)",
              "border": "Border: not core, but within\nEps of a core point",
              "noise": "Noise: neither"}
    offsets = {"core": (0.4, 3.85), "border": (3.5, 3.6), "noise": (5.0, 3.0)}
    for role in shows:
        i = DB_ROLE[role]
        ax.add_patch(Circle(X[i], eps, facecolor=ORANGE_TINT if role == "core" else "none",
                            edgecolor=ORANGE if role == "core" else INK, lw=2.2,
                            ls="-" if role == "core" else "--", alpha=0.9, zorder=2))
        ax.scatter(*X[i], s=320, facecolor="none", edgecolor=INK, lw=2.4, zorder=5)
        ax.annotate(labels[role], xy=X[i], xytext=offsets[role], fontsize=15, color=INK,
                    arrowprops=dict(arrowstyle="-", color=INK, lw=1.2))
    note(ax, f"Eps = {eps}, MinPts = {minpts}")
    assert core[DB_ROLE["core"]] and not core[DB_ROLE["border"]] and not core[DB_ROLE["noise"]]
    assert np.linalg.norm(X[DB_ROLE["border"]] - X[core], axis=1).min() <= eps
    assert np.linalg.norm(X[DB_ROLE["noise"]] - X[core], axis=1).min() > eps
    return fig


# DBSCAN walkthrough, shown before Eps and MinPts are named: a smile-shaped arc
# (14 points, 0.48 apart), a tight blob with one straggler, and two loners. A point
# is "crowded" (core) when its radius-1 circle holds at least 4 points, itself included.
_th = np.radians(np.linspace(195, 345, 14))
WALK_PTS = np.r_[np.c_[3 + 2.4 * np.cos(_th), 3.8 + 2.4 * np.sin(_th)],
                 [(8.0, 3.4), (8.5, 3.7), (7.6, 3.8), (8.3, 3.0), (7.7, 3.1), (8.6, 3.25),
                  (8.95, 4.25)],
                 [(3.1, 0.3), (6.2, 1.2)]]
WALK_R, WALK_MIN = 1.0, 4
WALK_SEEDS = [6, 14]  # where each cluster starts: the arc's middle, then the blob
WALK_RULE = f"Crowded: at least {WALK_MIN} points inside its circle (counting itself)"


def dbscan_waves(X, r, minpts, seeds):
    """[(cluster, expanding points, points they add, labels after)], one entry per wave.

    Labels: -2 not yet reached, else the cluster number. Growth stops at points
    that are not crowded: they join, but never expand."""
    D = np.linalg.norm(X[:, None] - X[None], axis=2)
    core = (D <= r).sum(1) >= minpts
    lab = np.full(len(X), -2)
    waves = []
    for k, seed in enumerate(seeds):
        lab[seed] = k
        grow = [seed]
        while grow:
            new = list(dict.fromkeys(q for p in grow for q in np.flatnonzero(D[p] <= r)
                                     if lab[q] == -2))
            lab[new] = k
            waves.append((k, grow, new, lab.copy()))
            grow = [q for q in new if core[q]]
    return waves, D, core


def walk_fig():
    fig, ax = equal_fig(GOLDEN, (-0.5, 9.8), (-0.8, 5.6), top=90, bottom=20)
    bare(ax)
    return fig, ax


def walk_points(ax, X, lab, *, rings=(), ring_color=INK):
    """Not-yet-reached points hollow; cluster 1 circles, cluster 2 squares; -1 noise."""
    unassigned(ax, X[lab == -2], size=150, zorder=3)
    seen = lab >= -1
    cluster_points(ax, X[seen], np.where(lab[seen] >= 0, 2 * lab[seen], -1), size=150, zorder=4)
    for i in rings:
        ax.scatter(*X[i], s=420, facecolor="none", edgecolor=ring_color, lw=2.4, zorder=5)


def walk_circles(ax, X, idx):
    """Each expanding point's circle: tinted fills first, then every outline on top."""
    for i in idx:
        ax.add_patch(Circle(X[i], WALK_R, facecolor=ORANGE_TINT, edgecolor="none", zorder=1))
    for i in idx:
        ax.add_patch(Circle(X[i], WALK_R, facecolor="none", edgecolor=ORANGE, lw=2, zorder=2))


@steps("dbscan-walk-count", 5)
def dbscan_walk_count(step):
    X = WALK_PTS
    _, D, core = dbscan_waves(X, WALK_R, WALK_MIN, WALK_SEEDS)
    n = (D <= WALK_R).sum(1)
    fig, ax = walk_fig()
    lab = np.full(len(X), -2)
    if step == 4:
        ax.scatter(*X[core].T, s=150, color=INK, edgecolor=PAPER, lw=0.7, zorder=4)
        unassigned(ax, X[~core], size=150, zorder=3)
        note(ax, f"{WALK_RULE}\nEvery point checked: {core.sum()} crowded (filled), "
                 f"{(~core).sum()} not (hollow)", size=16)
        return fig
    if step == 0:
        walk_points(ax, X, lab)
        note(ax, f"{WALK_RULE}\n{len(X)} points. Which ones are crowded?", size=16)
        return fig
    i = {1: 6, 2: 0, 3: 21}[step]
    walk_circles(ax, X, [i])
    walk_points(ax, X, lab, rings=[i])
    verdict = "crowded" if core[i] else "not crowded"
    where = {1: "A point on the arc", 2: "The arc's tip", 3: "A loner"}[step]
    note(ax, f"{WALK_RULE}\n{where}: {n[i]} point{'s' if n[i] > 1 else ''} inside, "
             f"so {verdict}", size=16)
    return fig


@steps("dbscan-walk-grow", 5)
def dbscan_walk_grow(step):
    X = WALK_PTS
    waves, _, core = dbscan_waves(X, WALK_R, WALK_MIN, WALK_SEEDS)
    arc = [w for w in waves if w[0] == 0]
    fig, ax = walk_fig()
    if step < len(arc):
        _, grow, new, lab = arc[step]
        walk_circles(ax, X, grow)
        walk_points(ax, X, lab, rings=new, ring_color=ORANGE)
        if step == 0:
            msg = ("Step 1: start at any crowded point; everything in its circle joins cluster 1\n"
                   f"{len(new)} points join (orange rings)")
        else:
            tips = [i for i in np.flatnonzero(lab == 0) if not core[i]]
            msg = (f"Step {step + 1}: each crowded newcomer draws its own circle; "
                   f"{len(new)} more {'points join' if len(new) > 1 else 'point joins'}")
            msg += ("\nThe tips are not crowded: they join, but draw no circle"
                    if len(tips) == 2 else "")
        note(ax, msg, size=16)
        return fig
    lab = arc[-1][3]
    tips = [i for i in np.flatnonzero(lab == 0) if not core[i]]
    walk_points(ax, X, lab, rings=tips)
    for i in tips:
        ax.annotate("", xy=X[i], xytext=(3.0, 4.75), arrowprops=dict(
            arrowstyle="-", color=INK, lw=1.2, shrinkA=0, shrinkB=12))
    ax.text(3.0, 4.8, "tips: in the cluster, but not crowded", ha="center", va="bottom",
            fontsize=15, color=INK)
    note(ax, f"No crowded newcomers left: cluster 1 is done ({(lab == 0).sum()} points)\n"
             "It follows the curve, because it grows point to point", size=16)
    return fig


@steps("dbscan-walk-finish", 3)
def dbscan_walk_finish(step):
    X = WALK_PTS
    waves, _, core = dbscan_waves(X, WALK_R, WALK_MIN, WALK_SEEDS)
    blob = [w for w in waves if w[0] == 1]
    fig, ax = walk_fig()
    if step == 0:
        _, grow, new, lab = blob[0]
        walk_circles(ax, X, grow)
        walk_points(ax, X, lab, rings=new, ring_color=ORANGE)
        note(ax, "Pick a crowded point no cluster has reached: it starts cluster 2\n"
                 f"{len(new)} points join", size=16)
        return fig
    lab = blob[-1][3].copy()
    if step == 1:
        grow = [p for w in blob[1:] for p in w[1]]
        new = [q for w in blob[1:] for q in w[2]]
        walk_circles(ax, X, grow)
        walk_points(ax, X, lab, rings=new, ring_color=ORANGE)
        note(ax, f"Cluster 2 grows the same way ({(lab == 1).sum()} points)\n"
                 "Its straggler joins, but is not crowded", size=16)
        return fig
    lab[lab == -2] = -1
    walk_points(ax, X, lab, rings=np.flatnonzero(lab == -1))
    for i in np.flatnonzero(lab == -1):
        ax.text(X[i, 0] + 0.3, X[i, 1], "noise", ha="left", va="center", fontsize=15, color=INK)
    note(ax, f"No crowded points left: whatever no cluster reached is noise\n"
             f"2 clusters and {(lab == -1).sum()} noise points, with no K chosen in advance",
         size=16)
    return fig


# ---------------------------------------------------- which technique when?

def shape_datasets():
    rng = np.random.default_rng(418)
    blobs, _ = make_blobs(n_samples=240, centers=3, cluster_std=0.6, random_state=8)
    moons, _ = make_moons(n_samples=240, noise=0.06, random_state=418)
    rings, _ = make_circles(n_samples=240, factor=0.45, noise=0.05, random_state=418)
    dense = np.r_[rng.normal((0, 0), 0.25, (150, 2)), rng.normal((3, 1.5), 1.1, (90, 2))]
    out = []
    for name, X in (("Round blobs", blobs), ("Moons", moons), ("Rings", rings),
                    ("Mixed density", dense)):
        out.append((name, (X - X.mean(0)) / X.std(0)))
    return out


SHAPE_METHODS = [
    ("k-means", lambda X, k: KMeans(k, n_init=10, random_state=0).fit_predict(X)),
    ("Ward's", lambda X, k: AgglomerativeClustering(k, linkage="ward").fit_predict(X)),
    ("Single link", lambda X, k: AgglomerativeClustering(k, linkage="single").fit_predict(X)),
    ("DBSCAN", lambda X, k: DBSCAN(eps=0.3, min_samples=5).fit_predict(X)),
]
SHAPE_K = {"Round blobs": 3, "Moons": 2, "Rings": 2, "Mixed density": 2}


@figure("cluster-shapes")
def cluster_shapes():
    data = shape_datasets()
    fig, axs = plt.subplots(len(data), len(SHAPE_METHODS),
                            figsize=(GOLDEN[0] / DPI, GOLDEN[1] / DPI), dpi=DPI)
    fig.patch.set_facecolor(PAPER)
    fig.subplots_adjust(left=0.15, right=0.99, top=0.92, bottom=0.01, wspace=0.06, hspace=0.08)
    for r, (name, X) in enumerate(data):
        for c, (mname, fn) in enumerate(SHAPE_METHODS):
            ax = axs[r, c]
            bare(ax)
            ax.set_facecolor(SOFT_GRAY)
            lab = fn(X, SHAPE_K[name])
            cluster_points(ax, X, lab, size=16)
            if r == 0:
                ax.set_title(mname, fontsize=16, color=INK)
            if c == 0:
                ax.text(-0.06, 0.5, name, transform=ax.transAxes, fontsize=15, color=INK,
                        ha="right", va="center")
    fig.fixed_layout = True
    return fig


# ------------------------------------------------- which clustering is better?

def by_x(lab, X):
    """Relabel clusters left to right by mean x, so cluster shapes are stable."""
    order = np.argsort([X[lab == k, 0].mean() for k in range(lab.max() + 1)])
    return np.argsort(order)[lab]


def match_labels(lab, ref):
    """Relabel `lab` so each cluster takes the id of the `ref` cluster it overlaps most."""
    k = ref.max() + 1
    overlap = np.array([[np.sum((lab == i) & (ref == j)) for j in range(k)] for i in range(k)])
    rows, cols = linear_sum_assignment(-overlap)
    relabel = dict(zip(rows, cols))
    return np.array([relabel[c] for c in lab])


def which_better(step, X, lab_a, lab_b, headline, *, pad=0.6, size=60, unit=""):
    """Two K = 3 clusterings of the same points, side by side; v1 reveals each one's SSE."""
    labs = [lab_a, lab_b]
    Cs = [np.array([X[lab == k].mean(axis=0) for k in range(3)]) for lab in labs]
    sses = [sse(X, C, lab) for C, lab in zip(Cs, labs)]
    lo, hi = X.min(0) - pad, X.max(0) + pad
    W, H = GOLDEN
    top, bottom, gap = 130, 80, 70
    h = H - top - bottom
    w = h * (hi[0] - lo[0]) / (hi[1] - lo[1])
    if w > (W - 3 * gap) / 2:  # too wide: shrink height instead
        w = (W - 3 * gap) / 2
        h = w * (hi[1] - lo[1]) / (hi[0] - lo[0])
    left, y0 = (W - 2 * w - gap) / 2, bottom + (H - top - bottom - h) / 2
    fig = plt.figure(figsize=(W / DPI, H / DPI), dpi=DPI)
    fig.patch.set_facecolor(PAPER)
    fig.fixed_layout = True
    for i, name in enumerate("AB"):
        ax = fig.add_axes([(left + i * (w + gap)) / W, y0 / H, w / W, h / H])
        bare(ax)
        ax.set_facecolor(SOFT_GRAY)
        ax.set_xlim(lo[0], hi[0])
        ax.set_ylim(lo[1], hi[1])
        cluster_points(ax, X, labs[i], size=size)
        ax.text(0, 1.02, f"Clustering {name}", transform=ax.transAxes, fontsize=19, color=INK,
                ha="left", va="bottom")
        if step == 1:
            centroids(ax, Cs[i], size=size * 4)
            lower = sses[i] == min(sses)
            ax.text(0.5, -0.03, f"SSE = {sses[i]:,.0f}{unit}" + ("  (lower)" if lower else ""),
                    transform=ax.transAxes, fontsize=20, color=ORANGE if lower else STEEL,
                    ha="center", va="top")
    note(fig.axes[0], headline)
    if step == 1:
        note(fig.axes[0], "SSE: squared distance from each point to its cluster's mean (×), summed",
             y=0.925, size=15, color=STEEL)
    return fig


@steps("which-better-blobs", 2)
def which_better_blobs(step):
    X, _ = make_blobs(n_samples=150, centers=[(-4, -2), (0, 3), (4, -2)], cluster_std=1.0,
                      random_state=418)
    a = by_x(KMeans(3, init="random", n_init=1, random_state=2).fit_predict(X), X)  # seed 2 gets stuck
    b = match_labels(KMeans(3, n_init=10, random_state=0).fit_predict(X), a)
    return which_better(step, X, a, b, "Example 1: 150 points, K = 3 both times")


@steps("which-better-penguins", 2)
def which_better_penguins(step):
    Z, *_ = penguins()
    a = by_x(KMeans(3, n_init=10, random_state=0).fit_predict(Z), Z)
    b = match_labels(AgglomerativeClustering(3, linkage="ward").fit_predict(Z), a)
    return which_better(step, Z, a, b, f"Example 2: {len(Z)} penguins (bill and flipper length, "
                        "standardized), K = 3 both times", pad=0.3, size=34)


@steps("which-better-stripes", 2)
def which_better_stripes(step):
    rng = np.random.default_rng(418)
    X = np.vstack([np.c_[rng.uniform(0, 8, 50), rng.normal(y, 0.15, 50)] for y in (0, 2, 4)])
    a = by_x(KMeans(3, n_init=10, random_state=0).fit_predict(X), X)
    b = np.repeat([0, 1, 2], 50)  # one cluster per stripe
    return which_better(step, X, a, b, "Example 3: 150 points, K = 3 both times", size=50)


# --------------------------------------------- four cohesion/separation cases

# name: (spread of each cluster, distance between centers, label, plain-words reading)
COH_SEP = {
    "high-high": (0.45, 7.0, "High cohesion, high separation", "Each cluster is tight, and the clusters are far apart"),
    "low-low": (1.2, 2.2, "Low cohesion, low separation", "Each cluster is spread out, and the clusters overlap"),
    "high-low": (0.45, 2.2, "High cohesion, low separation", "Each cluster is tight, but the clusters sit close together"),
    "low-high": (1.2, 7.0, "Low cohesion, high separation", "Each cluster is spread out, but the clusters are far apart"),
}


def coh_sep(step, key):
    """v0: two clusters alone. v1: name the case. Same 2 x 25 draws every time, scaled and moved."""
    sd, gap, label, reading = COH_SEP[key]
    base = np.random.default_rng(418).standard_normal((2, 25, 2))
    A, B = base[0] * sd + (-gap / 2, 0), base[1] * sd + (gap / 2, 0)
    fig, ax = equal_fig(GOLDEN, (-7.5, 7.5), (-3.6, 3.6), top=120, bottom=30)
    bare(ax)
    ax.scatter(A[:, 0], A[:, 1], s=150, marker="o", color=STEEL, edgecolor=PAPER, zorder=4)
    ax.scatter(B[:, 0], B[:, 1], s=150, marker="s", color=INK, edgecolor=PAPER, zorder=4)
    if step == 1:
        note(ax, label, size=22)
        note(ax, reading, y=0.915, size=17, color=STEEL)
    return fig


for _key in COH_SEP:
    steps(f"coh-sep-{_key}", 2)(partial(coh_sep, key=_key))


# ---------------------------------------------------------- cluster evaluation

CE_A =np.array([(1.0, 1.4), (1.7, 2.3), (2.1, 1.1), (1.3, 2.4)])
CE_B = np.array([(4.6, 1.6), (5.4, 2.4), (5.6, 1.0), (4.9, 2.9)])


@steps("cohesion-separation", 3)
def cohesion_separation(step):
    A, B = CE_A, CE_B
    fig, ax = equal_fig(SPLIT, (0.3, 6.4), (0.3, 3.7), top=110, bottom=30)
    bare(ax)
    if step == 0:
        for i in range(len(A)):
            for j in range(i + 1, len(A)):
                ax.plot(*zip(A[i], A[j]), color=ORANGE, lw=2, zorder=2)
        d = [np.linalg.norm(A[i] - A[j]) for i in range(4) for j in range(i + 1, 4)]
        note(ax, f"Cohesion of A: average of the {len(d)} distances\ninside A = {np.mean(d):.2f}",
             size=17)
    elif step == 1:
        for a in A:
            for b in B:
                ax.plot(*zip(a, b), color=ORANGE, lw=1.4, alpha=0.8, zorder=2)
        D = np.linalg.norm(A[:, None] - B[None], axis=2)
        note(ax, f"Separation of A and B: average of the {D.size}\ndistances between them = {D.mean():.2f}",
             size=17)
    else:
        p = A[2]
        own = [q for q in A if not np.allclose(q, p)]
        for q in own:
            ax.plot(*zip(p, q), color=STEEL, lw=2, zorder=2)
        for q in B:
            ax.plot(*zip(p, q), color=ORANGE, lw=2, ls="--", zorder=2)
        a = np.mean([np.linalg.norm(p - q) for q in own])
        b = np.mean([np.linalg.norm(p - q) for q in B])
        s = (b - a) / max(a, b)
        ax.scatter(*p, s=600, facecolor="none", edgecolor=ORANGE, lw=3, zorder=5)
        note(ax, f"One point: a = {a:.2f} (own cluster, solid)\n"
                 f"b = {b:.2f} (nearest other cluster, dashed)\n"
                 f"s = (b − a) / max(a, b) = {s:.2f}",
             size=17)
    ax.scatter(A[:, 0], A[:, 1], s=170, marker="o", color=STEEL, edgecolor=PAPER, zorder=4)
    ax.scatter(B[:, 0], B[:, 1], s=170, marker="s", color=INK, edgecolor=PAPER, zorder=4)
    ax.text(1.0, 3.0, "A", fontsize=18, color=STEEL)
    ax.text(5.9, 3.0, "B", fontsize=18, color=INK)
    return fig


@figure("silhouette-penguins")
def silhouette_penguins():
    Z, species, *_ = penguins()
    lab = match_to_species(KMeans(3, n_init=10, random_state=0).fit_predict(Z), species)
    s = silhouette_samples(Z, lab)
    fig, ax = fixed_fig(SPLIT, 150, 50, 80, 80)
    tidy(ax, grid="x", spines=("bottom",))
    y = 0
    names = ["circles", "triangles", "squares"]
    for k in range(3):
        vals = np.sort(s[lab == k])
        _, fill, edge = CLUSTER_STYLE[k]
        ax.barh(np.arange(y, y + len(vals)), vals, height=1.0, color=fill, edgecolor="none")
        ax.text(-0.04, y + len(vals) / 2, f"Cluster {k + 1}\n({names[k]})", ha="right",
                va="center", fontsize=14, color=INK, transform=ax.get_yaxis_transform())
        y += len(vals) + 12
    mean = s.mean()
    ax.axvline(mean, color=ORANGE, lw=2.5, ls="--")
    ax.text(mean + 0.015, -12, f"mean s = {mean:.2f}", fontsize=15, color=INK, va="center")
    ax.set_xlim(-0.2, 0.85)
    ax.set_ylim(y, -22)
    ax.set_yticks([])
    ax.set_xlabel("Silhouette coefficient s, one bar per penguin")
    return fig


@steps("choose-k", 2)
def choose_k(step):
    Z, *_ = penguins()
    ks = np.arange(2, 10)
    fits = [KMeans(k, n_init=10, random_state=0).fit(Z) for k in ks]
    sses = [f.inertia_ for f in fits]
    sils = [silhouette_score(Z, f.labels_) for f in fits]
    W, H = SPLIT
    fig = plt.figure(figsize=(W / DPI, H / DPI), dpi=DPI)
    fig.patch.set_facecolor(PAPER)
    fig.fixed_layout = True
    top = fig.add_axes([0.13, 0.58, 0.82, 0.33])
    bot = fig.add_axes([0.13, 0.1, 0.82, 0.33])
    for ax in (top, bot):
        tidy(ax, grid="y")
        ax.set_xticks(ks)
        ax.set_xlim(1.5, 9.5)
    top.plot(ks, sses, color=STEEL, lw=2.5, marker="o", ms=9, mec=PAPER)
    top.scatter([3], [sses[1]], s=420, facecolor="none", edgecolor=ORANGE, lw=3)
    ylabel_top(top, "Total SSE (lower is better), Monday's elbow at K = 3")
    top.set_ylim(0, 280)
    if step == 1:
        bot.plot(ks, sils, color=STEEL, lw=2.5, marker="o", ms=9, mec=PAPER)
        best = int(np.argmax(sils))
        bot.scatter([ks[best]], [sils[best]], s=420, facecolor="none", edgecolor=ORANGE, lw=3)
        bot.annotate(f"best: K = {ks[best]} ({sils[best]:.2f})", xy=(ks[best], sils[best]),
                     xytext=(4.0, 0.53), fontsize=15, color=INK,
                     arrowprops=dict(arrowstyle="-", color=INK, lw=1.2))
        bot.annotate(f"K = 3: {sils[1]:.2f}", xy=(3, sils[1]), xytext=(3.4, 0.39), fontsize=15,
                     color=STEEL, arrowprops=dict(arrowstyle="-", color=STEEL, lw=1.2))
    else:
        bot.set_yticklabels([])
    ylabel_top(bot, "Mean silhouette (higher is better)")
    bot.set_ylim(0.3, 0.6)
    bot.set_xlabel("Number of clusters, K")
    return fig


@figure("contingency-penguins")
def contingency_penguins():
    Z, species, *_ = penguins()
    lab = match_to_species(KMeans(3, n_init=10, random_state=0).fit_predict(Z), species)
    M = np.array([[np.sum((species == s) & (lab == k)) for k in range(3)] for s in SPECIES_ORDER])
    fig, ax = fixed_fig(SPLIT, 230, 40, 150, 90)
    ax.set_xlim(0, 3)
    ax.set_ylim(3, 0)
    bare(ax)
    for i in range(3):
        for j in range(3):
            v = M[i, j]
            frac = v / M[i].sum()
            fill = ORANGE_TINT if i == j else (SOFT_GRAY if v else PAPER)
            ax.add_patch(plt.Rectangle((j, i), 1, 1, facecolor=fill, edgecolor=BORDER, lw=2))
            ax.text(j + 0.5, i + 0.5, str(v), ha="center", va="center", fontsize=28 if v > 20 else 22,
                    color=INK if i == j else STEEL)
    glyph = {"o": "●", "^": "▲", "s": "■"}
    for i, s in enumerate(SPECIES_ORDER):
        m, fill, _, name = SPECIES_STYLE[s]
        ax.text(-0.08, i + 0.5, f"{name} {glyph[m]}", ha="right", va="center", fontsize=18, color=INK)
    for j in range(3):
        ax.text(j + 0.5, -0.12, f"Cluster {j + 1}\n{glyph[CLUSTER_STYLE[j][0]]}", ha="center",
                va="bottom", fontsize=17, color=INK)
    ax.text(-0.08, -0.12, "True species ↓\nk-means cluster →", ha="right", va="bottom",
            fontsize=14, color=STEEL)
    ari = adjusted_rand_score(species, lab)
    ax.text(1.5, 3.2, f"Adjusted Rand index = {ari:.2f}   (0 = chance, 1 = identical)",
            ha="center", va="top", fontsize=16, color=INK)
    return fig


# ------------------------------------------- appendix: L stations by ridership

CTA_DAILY_CSV = REPO_ROOT / "datasets" / "cta-ridership" / "Station_Entries_-_Daily_Totals_20260527.csv"
RIDER_FEATURES = ["size", "sat_r", "sun_r", "season", "spike", "recov"]
RIDER_NAMES = ["Size: typical weekday (log)", "Saturday ÷ weekday", "Sunday ÷ weekday",
               "Summer ÷ winter weekday", "Busiest day ÷ typical day", "2025 ÷ 2019 weekday"]
# four clusters need a fourth gray shape; the diamond is hollow so it reads apart
RIDER_STYLE = [("o", STEEL, PAPER), ("^", QUIET, STEEL), ("s", INK, PAPER), ("D", PAPER, INK)]
RIDER_GROUPS = ["Loop commuter", "Busy all week", "Neighborhood", "Event & destination"]
GLYPH = {"o": "●", "^": "▲", "s": "■", "D": "◇"}


@lru_cache(maxsize=None)
def cta_daily():
    df = pl.read_csv(CTA_DAILY_CSV, infer_schema=False)
    return df.with_columns(pl.col("date").str.strptime(pl.Date, "%m/%d/%Y"),
                           pl.col("rides").str.replace_all(",", "").cast(pl.Int64))


@lru_cache(maxsize=None)
def ridership_clusters():
    """One row per station: six 2025 ridership features (medians), K = 4 k-means.

    Stations without a usable 2025 or 2019 weekday median are left out: Damen-Lake
    (first entries Aug. 2024), Lawrence and Berwyn (no entries May 2021 to mid-July
    2025, so their 2025 weekday median is 0), and the closed Randolph/Wabash.
    """
    d = cta_daily()
    yr, mo, r = pl.col("date").dt.year(), pl.col("date").dt.month(), pl.col("rides")
    W, A, U = [pl.col("daytype") == t for t in "WAU"]
    y25 = yr == 2025
    g = (d.filter(yr.is_in([2019, 2025])).group_by("station_id")
          .agg(pl.first("stationname"), y25.sum().alias("days"),
               r.filter(W & y25).median().alias("wk"),
               r.filter(A & y25).median().alias("sat"),
               r.filter(U & y25).median().alias("sun"),
               r.filter(W & y25 & mo.is_in([6, 7, 8])).median().alias("summer"),
               r.filter(W & y25 & mo.is_in([12, 1, 2])).median().alias("winter"),
               r.filter(y25).quantile(0.99).alias("p99"),
               r.filter(y25).median().alias("med"),
               r.filter(W & (yr == 2019)).median().alias("wk19"))
          .with_columns(pl.col("wk").log10().alias("size"),
                        (pl.col("sat") / pl.col("wk")).alias("sat_r"),
                        (pl.col("sun") / pl.col("wk")).alias("sun_r"),
                        (pl.col("summer") / pl.col("winter")).alias("season"),
                        (pl.col("p99") / pl.col("med")).alias("spike"),
                        (pl.col("wk") / pl.col("wk19")).alias("recov"))
          .sort("station_id"))
    X = g.select(RIDER_FEATURES).to_numpy().astype(float)
    ok = np.isfinite(X).all(axis=1) & (g["days"].to_numpy() >= 360)
    dropped = g.filter(~pl.Series(ok))["stationname"].to_list()
    g, X = g.filter(pl.Series(ok)), X[ok]
    Z = (X - X.mean(axis=0)) / X.std(axis=0)
    lab = KMeans(4, n_init=20, random_state=418).fit_predict(Z)
    # name clusters by profile, not by k-means' arbitrary numbering
    med = np.array([np.median(Z[lab == k], axis=0) for k in range(4)])
    f = {name: i for i, name in enumerate(RIDER_FEATURES)}
    event = int(med[:, f["spike"]].argmax())
    commuter = int(med[:, f["sat_r"]].argmin())
    rest = [k for k in range(4) if k not in (event, commuter)]
    hood = min(rest, key=lambda k: med[k, f["size"]])
    busy = next(k for k in rest if k != hood)
    order = [commuter, busy, hood, event]
    assert len(set(order)) == 4, "cluster profiles changed; revisit the naming rule"
    lab = np.array([order.index(k) for k in lab])
    return g, Z, lab, dropped


def rider_subset(feats, k=4):
    """k-means on a subset of the ridership features; shapes matched to the 6-feature groups."""
    g, Z, lab6, _ = ridership_clusters()
    idx = [RIDER_FEATURES.index(f) for f in feats]
    km = KMeans(k, n_init=20, random_state=418).fit(Z[:, idx])
    overlap = np.array([[np.sum((km.labels_ == a) & (lab6 == b)) for b in range(4)] for a in range(k)])
    rows, cols = linear_sum_assignment(-overlap)
    relabel = dict(zip(rows, cols))
    lab = np.array([relabel[c] for c in km.labels_])
    C = np.array([km.cluster_centers_[a] for a in sorted(relabel, key=relabel.get)])
    return g, Z[:, idx], lab, C


def rider_points(ax, P, lab, *, size=70, zorder=3, **kw):
    for k, (m, fill, edge) in enumerate(RIDER_STYLE):
        pts = P[lab == k]
        ax.scatter(*pts.T, marker=m, s=size * (0.8 if m == "D" else 1.0), color=fill,
                   edgecolor=edge, linewidth=0.9, zorder=zorder, **kw)


RIDER_CALLOUTS = {"Clark/Lake": (-12, -12), "O'Hare Airport": (-10, 10), "Addison-North Main": (10, 6),
                  "Kimball": (-10, -14), "Midway Airport": (10, -14)}


@steps("l-ridership-2d", 2)
def l_ridership_2d(step):
    """Two features: typical weekday entries (log) and Saturday ÷ weekday; then K = 4."""
    g, P, lab, C = rider_subset(["size", "sat_r"])
    raw = g.select("size", "sat_r").to_numpy()
    mu, sd = raw.mean(axis=0), raw.std(axis=0)
    fig, ax = fixed_fig(SPLIT, 100, 40, 120, 90)
    tidy(ax)
    xt = np.array([300, 1000, 3000, 10000])
    ax.set_xticks((np.log10(xt) - mu[0]) / sd[0], ["300", "1,000", "3,000", "10,000"])
    yt = np.array([0.25, 0.5, 0.75, 1.0, 1.25, 1.5])
    ax.set_yticks((yt - mu[1]) / sd[1], [f"{v:g}" for v in yt])
    ax.set_xlabel("Typical weekday entries, 2025 (log scale)")
    ylabel_top(ax, "Saturday ÷ weekday")
    if step == 0:
        ax.scatter(*P.T, s=60, color=STEEL, edgecolor=PAPER, lw=0.7, zorder=3)
        note(ax, f"{len(P)} stations, two features each", size=18)
    else:
        rider_points(ax, P, lab)
        centroids(ax, C, size=300)
        note(ax, "k-means, K = 4, on these two features", size=18)
    names = g["stationname"].to_list()
    for name, off in RIDER_CALLOUTS.items():
        i = names.index(name)
        ax.annotate(name.replace("-North Main", "").replace(" Airport", ""), P[i], xytext=off,
                    textcoords="offset points", fontsize=13, color=INK,
                    ha="left" if off[0] > 0 else "right", va="center")
    return fig


@steps("l-ridership-3d", 2)
def l_ridership_3d(step):
    """Add busiest day ÷ typical day as a third axis: first the 2-D clusters, then K = 4 again."""
    feats = ["size", "sat_r", "spike"]
    g, P, lab3, C = rider_subset(feats)
    _, _, lab2, _ = rider_subset(["size", "sat_r"])
    lab = lab2 if step == 0 else lab3
    fig = plt.figure(figsize=(SPLIT[0] / DPI, SPLIT[1] / DPI), dpi=DPI)
    fig.patch.set_facecolor(PAPER)
    fig.fixed_layout = True
    ax = fig.add_axes([0.02, 0.0, 0.96, 0.9], projection="3d")
    ax.set_facecolor(PAPER)
    for axis in (ax.xaxis, ax.yaxis, ax.zaxis):
        axis.set_pane_color((1, 1, 1, 0))
        axis._axinfo["grid"].update(color=BORDER, linewidth=0.8)
        axis.label.set_color(STEEL)
    ax.tick_params(colors=STEEL, labelsize=11)
    rider_points(ax, P, lab, size=55, depthshade=False)
    if step == 1:
        ax.scatter(*C.T, marker="X", s=260, color=ORANGE, edgecolor=INK, linewidth=1.2,
                   depthshade=False, zorder=6)
    ax.set_xlabel("Typical weekday (std. units)", fontsize=13, labelpad=8)
    ax.set_ylabel("Saturday ÷ weekday (std.)", fontsize=13, labelpad=8)
    ax.set_zlabel("Busiest ÷ typical day (std.)", fontsize=13, labelpad=8)
    ax.view_init(elev=18, azim=-58)
    names = g["stationname"].to_list()
    for name, label, dx in (("Addison-North Main", "Addison", 0.15), ("Sox-35th-Dan Ryan", "Sox-35th", 0.15),
                            ("UIC-Halsted", "UIC-Halsted", 0.3)):
        i = names.index(name)
        ax.text(*P[i] + [dx, 0, 0.1], label, fontsize=12, color=INK, zorder=7)
    head = ("Add a third feature: the same 2-D clusters, lifted" if step == 0
            else "k-means again, K = 4, now in three dimensions")
    fig.text(0.03, 0.985, head, fontsize=18, color=INK, ha="left", va="top")  # note() needs a 2-D axes
    return fig


@figure("l-ridership-map")
def l_ridership_map():
    X, st = l_stations()
    g, Z, lab, dropped = ridership_clusters()
    pos = {mid: i for i, mid in enumerate(st["MAP_ID"].to_list())}
    idx = np.array([pos[s] for s in g["station_id"].to_list()])
    fig, ax = map_fig()
    rest = np.setdiff1d(np.arange(len(X)), idx)
    unassigned(ax, X[rest], size=30)
    for k, (m, fill, edge) in enumerate(RIDER_STYLE):
        pts = X[idx[lab == k]]
        ax.scatter(pts[:, 0], pts[:, 1], marker=m, s=46 if m != "D" else 34, color=fill,
                   edgecolor=edge, linewidth=0.9, zorder=3 + (k == 3))
    # legend in the empty northwest corner, as text glyphs (data-free, so no autoscale)
    rows = [(GLYPH[m], fill if m != "D" else INK, f"{name} ({(lab == k).sum()})", INK)
            for k, ((m, fill, _), name) in enumerate(zip(RIDER_STYLE, RIDER_GROUPS))]
    rows.append(("○", QUIET, f"Left out ({len(rest)})", STEEL))
    for i, (glyph, gcolor, text, tcolor) in enumerate(rows):
        y = 0.885 - 0.034 * i
        ax.text(0.03, y, glyph, transform=fig.transFigure, fontsize=15, color=gcolor, va="center")
        ax.text(0.075, y, text, transform=fig.transFigure, fontsize=14, color=tcolor, va="center")
    note(ax, "Clustered by ridership pattern,\nnot by location", size=17)
    return fig


@figure("l-ridership-profiles")
def l_ridership_profiles():
    g, Z, lab, dropped = ridership_clusters()
    fig, ax = fixed_fig(SPLIT, 300, 40, 150, 90)
    tidy(ax, grid="x", spines=())
    y = np.arange(len(RIDER_FEATURES))[::-1]
    ax.axvline(0, color=STEEL, lw=1.2, zorder=1)
    for k, (m, fill, edge) in enumerate(RIDER_STYLE):
        med = np.median(Z[lab == k], axis=0)
        ax.scatter(med, y + (1.5 - k) * 0.12, marker=m, s=150 if m != "D" else 110, color=fill,
                   edgecolor=edge, linewidth=1.0, zorder=3)
    ax.set_yticks(y, RIDER_NAMES, fontsize=15, color=INK)
    ax.set_xlim(-2.2, 3.2)
    ax.set_ylim(-0.6, len(y) - 0.4)
    ax.set_xlabel("Cluster median, in standard deviations from the average station")
    x = 0.03
    for k, name in enumerate(RIDER_GROUPS):
        m = RIDER_STYLE[k][0]
        ax.text(x, 0.9, GLYPH[m], transform=fig.transFigure, fontsize=17,
                color=RIDER_STYLE[k][1] if m != "D" else INK, ha="left", va="center")
        ax.text(x + 0.03, 0.9, name, transform=fig.transFigure, fontsize=15, color=INK,
                ha="left", va="center")
        x += 0.07 + 0.0125 * len(name)
    note(ax, "What makes each cluster different", size=18)
    return fig


@figure("l-ridership-spikes")
def l_ridership_spikes():
    d = cta_daily().filter(pl.col("date").dt.year() == 2025)
    fig, ax = fixed_fig(SPLIT, 90, 40, 130, 80)
    tidy(ax, grid="y", spines=("bottom",))
    for name, color, lw, z in (("Clark/Lake", QUIET, 1.4, 2), ("Addison-North Main", ORANGE, 1.6, 3)):
        s = d.filter(pl.col("stationname") == name).sort("date")
        r = s["rides"].to_numpy()
        ax.plot(s["date"].to_numpy(), r / np.median(r), color=color, lw=lw, zorder=z)
    ax.axhline(1, color=STEEL, lw=1, ls="--", zorder=1)
    ax.set_ylim(0, 5)
    ax.xaxis.set_major_formatter(matplotlib.dates.DateFormatter("%b"))
    ylabel_top(ax, "Daily entries ÷ the station's median day, 2025")
    ax.text(0.99, 0.97, "Addison (Red Line)", transform=ax.transAxes, color=ORANGE, fontsize=16,
            ha="right", va="top")
    ax.text(0.99, 0.90, "Clark/Lake (Loop)", transform=ax.transAxes, color=STEEL, fontsize=16,
            ha="right", va="top")
    note(ax, "A Loop commuter stop vs. the spikiest station", size=17)
    return fig


# ------------------------------------------------- appendix: movie review text

REVIEWS_CSV = REPO_ROOT / "datasets" / "movie-reviews" / "reviews.csv"
SENTIMENTS = ["negative", "meh", "positive"]


@lru_cache(maxsize=None)
def review_clusters(k=6):
    """TF-IDF on review text, reduced to 100 dimensions (LSA), K = 6 k-means.

    Clusters are numbered by their share of positive reviews, highest first.
    """
    df = pl.read_csv(REVIEWS_CSV)
    text = [html.unescape(t) for t in df["text"]]  # the source keeps &#34; for quotes
    vec = TfidfVectorizer(stop_words="english", min_df=5, max_df=0.5, ngram_range=(1, 2),
                          sublinear_tf=True)
    X = vec.fit_transform(text)
    Z = normalize(TruncatedSVD(100, random_state=418).fit_transform(X))
    lab = KMeans(k, n_init=10, random_state=418).fit_predict(Z)
    sent = df["sentiment"].to_numpy()
    pos = [np.mean(sent[lab == c] == "positive") for c in range(k)]
    order = list(np.argsort(pos)[::-1])
    lab = np.array([order.index(c) for c in lab])
    terms = np.array(vec.get_feature_names_out())
    top = [terms[np.asarray(X[lab == c].mean(axis=0)).ravel().argsort()[::-1][:5]] for c in range(k)]
    return lab, sent, top, X.shape


@steps("reviews-clusters", 2)
def reviews_clusters(step):
    lab, sent, top, shape = review_clusters()
    k = len(top)
    fig, ax = fixed_fig(GOLDEN, 30, 30, 90, 20)
    ax.set_xlim(0, 1)
    ax.set_ylim(k + 0.2, -0.9)
    bare(ax)
    xs = [0.70, 0.80, 0.90]
    ax.text(0.0, -0.6, "Cluster", fontsize=15, color=STEEL, va="center")
    ax.text(0.17, -0.6, "Top words and phrases (TF-IDF)", fontsize=15, color=STEEL, va="center")
    if step == 1:
        for x, s in zip(xs, SENTIMENTS):
            ax.text(x, -0.6, s, fontsize=15, color=STEEL, ha="center", va="center")
    for c in range(k):
        n = int((lab == c).sum())
        ax.axhline(c + 0.5, color=BORDER, lw=1)
        ax.text(0.0, c, f"{c + 1}  ({n:,})", fontsize=16, color=INK, va="center")
        ax.text(0.17, c, ", ".join(top[c]), fontsize=16, color=INK, va="center")
        if step == 0:
            continue
        shares = [np.mean(sent[lab == c] == s) for s in SENTIMENTS]
        for x, sh in zip(xs, shares):
            strong = sh >= 0.55
            ax.add_patch(plt.Rectangle((x - 0.045, c - 0.38), 0.09, 0.76,
                                       facecolor=ORANGE_TINT if strong else SOFT_GRAY,
                                       edgecolor="none"))
            ax.text(x, c, f"{sh:.0%}", fontsize=16, color=INK if strong else STEEL,
                    ha="center", va="center")
    head = (f"{shape[0]:,} reviews, {shape[1]:,} terms, K = {k}: grouped without the labels"
            if step == 0 else "Reveal the labels: most clusters are not about sentiment")
    note(ax, head, size=18)
    return fig


@lru_cache(maxsize=None)
def review_plane():
    """TF-IDF directions 2 and 3 (truncated SVD); K = 3 k-means in that plane.

    Direction 1 mostly tracks how much common vocabulary a review uses, so the plane
    that shows structure is 2 x 3.
    """
    df = pl.read_csv(REVIEWS_CSV)
    text = [html.unescape(t) for t in df["text"]]
    vec = TfidfVectorizer(stop_words="english", min_df=5, max_df=0.5, ngram_range=(1, 2),
                          sublinear_tf=True)
    X = vec.fit_transform(text)
    svd = TruncatedSVD(3, random_state=418).fit(X)
    P = svd.transform(X)[:, 1:3]
    km = KMeans(3, n_init=10, random_state=418).fit(P)
    terms = np.array(vec.get_feature_names_out())
    W = svd.components_[1:3]
    ends = [(terms[c.argsort()[::-1][:2]], terms[c.argsort()[:2]]) for c in W]
    return P, km.labels_, km.cluster_centers_, df["sentiment"].to_numpy(), ends, W, terms, text


# real reviews, quoted as written, that show where a review lands
REVIEW_EXAMPLES = ["I love this show.", "It was OK a little far out", "Julianne Moore did an fantastic job"]


@figure("reviews-directions")
def reviews_directions():
    """Directions 2 and 3: the terms with the largest positive and negative weights."""
    *_, W, terms, _ = review_plane()
    fig = plt.figure(figsize=(SPLIT[0] / DPI, SPLIT[1] / DPI), dpi=DPI)
    fig.patch.set_facecolor(PAPER)
    fig.fixed_layout = True
    for r, (w, color) in enumerate(zip(W, (ORANGE, INK))):
        top = np.r_[w.argsort()[::-1][:5], w.argsort()[:5][::-1]]
        ax = fig.add_axes([0.3, 0.52 - 0.45 * r, 0.62, 0.33])
        tidy(ax, grid="x", spines=())
        y = np.arange(len(top))[::-1]
        ax.barh(y, w[top], height=0.65, color=color)
        ax.axvline(0, color=STEEL, lw=1.2)
        ax.set_yticks(y, terms[top], fontsize=14, color=INK)
        lim = np.abs(w[top]).max() * 1.35
        ax.set_xlim(-lim, lim)
        for yy, v in zip(y, w[top]):
            ax.text(v + (0.01 if v >= 0 else -0.01), yy, f"{v:+.2f}", va="center",
                    ha="left" if v >= 0 else "right", fontsize=11, color=STEEL)
        ax.text(-0.42, 1.04, f"Direction {r + 2}: a weight for each of {len(w):,} terms (top 5 each way)",
                transform=ax.transAxes, fontsize=15, color=INK, ha="left", va="bottom")
    fig.text(0.03, 0.985, "How the two directions are built", fontsize=18, color=INK, va="top")
    return fig


@steps("reviews-2d", 3)
def reviews_2d(step):
    P, lab, C, sent, ends, _, _, text = review_plane()
    fig, ax = fixed_fig(SPLIT, 90, 40, 120, 90)
    tidy(ax)
    (x_pos, x_neg), (y_pos, y_neg) = ends
    ax.set_xlabel(f"← {', '.join(x_neg)}      Direction 2      {', '.join(x_pos)} →")
    ylabel_top(ax, f"Direction 3:  ↑ {', '.join(y_pos)}   ↓ {', '.join(y_neg)}")
    order = np.argsort([-(lab == k).sum() for k in range(3)])  # biggest cluster drawn first
    if step == 0:
        ax.scatter(*P.T, s=10, color=STEEL, alpha=0.5, lw=0, zorder=3)
        for quote, spot in zip(REVIEW_EXAMPLES, [(0.62, 0.62), (0.30, 0.86), (0.45, 0.12)]):
            i = text.index(quote)
            ax.scatter(*P[i], s=90, facecolor="none", edgecolor=ORANGE, lw=2.2, zorder=5)
            ax.annotate(f"“{quote}”", P[i], xytext=spot, textcoords="axes fraction", fontsize=14,
                        color=INK, zorder=7, bbox=dict(boxstyle="round,pad=0.3", facecolor=PAPER,
                                                       edgecolor=BORDER),
                        arrowprops=dict(arrowstyle="-", color=ORANGE, lw=1.3, shrinkB=7))
        note(ax, f"{len(P):,} reviews: each dot is one review's two scores", size=18)
        return fig
    for k in order:
        m, fill, edge = CLUSTER_STYLE[k]
        ax.scatter(*P[lab == k].T, marker=m, s=16, color=fill, edgecolor=edge, lw=0.3,
                   alpha=0.8, zorder=3)
    centroids(ax, C, size=300)
    if step == 1:
        note(ax, "k-means, K = 3, on the two directions", size=18)
        return fig
    # label boxes go in empty corners (axes fractions), each tied to its centroid
    spots = {0: (0.62, 0.62), 1: (0.30, 0.86), 2: (0.45, 0.12)}
    by_size = sorted(range(3), key=lambda k: (lab == k).sum())  # smallest, middle, largest
    for k in range(3):
        sel = lab == k
        shares = "  ".join(f"{s[:3]} {np.mean(sent[sel] == s):.0%}" for s in SENTIMENTS)
        slot = 2 if k == by_size[-1] else (1 if C[k, 0] < 0 else 0)
        ax.annotate(f"{sel.sum():,} reviews\n{shares}", C[k], xytext=spots[slot],
                    textcoords="axes fraction", fontsize=13, color=INK, zorder=7,
                    bbox=dict(boxstyle="round,pad=0.3", facecolor=PAPER, edgecolor=BORDER),
                    arrowprops=dict(arrowstyle="-", color=STEEL, lw=1.1, shrinkB=12))
    note(ax, "Reveal the labels: two thin arms and one big blob", size=18)
    return fig


LEXICON_DIR = REPO_ROOT / "datasets" / "movie-reviews" / "opinion-lexicon"


def lexicon(name):
    """Hu and Liu's opinion lexicon: one word per line after a `;` comment header."""
    lines = (LEXICON_DIR / name).read_text(encoding="utf-8", errors="ignore").splitlines()
    return {w.strip() for w in lines if w.strip() and not w.startswith(";")}


@lru_cache(maxsize=None)
def review_word_counts():
    """Positive and negative lexicon words per review; K = 3 k-means on log(1 + count).

    The log keeps a few long reviews from setting the scale. Clusters are numbered by
    their share of positive reviews, highest first.
    """
    pos_words, neg_words = lexicon("positive-words.txt"), lexicon("negative-words.txt")
    df = pl.read_csv(REVIEWS_CSV)
    text = [html.unescape(t) for t in df["text"]]
    tokens = [re.findall(r"[a-z+\-']+", t.lower()) for t in text]
    counts = np.array([[sum(w in pos_words for w in t), sum(w in neg_words for w in t)]
                       for t in tokens])
    X = np.log1p(counts)
    km = KMeans(3, n_init=10, random_state=418).fit(X)
    sent = df["sentiment"].to_numpy()
    pos = [np.mean(sent[km.labels_ == c] == "positive") for c in range(3)]
    order = list(np.argsort(pos)[::-1])
    lab = np.array([order.index(c) for c in km.labels_])
    return counts, X, lab, km.cluster_centers_[order], sent, text


# real reviews, quoted as written (the third is an excerpt), with their counts in the corner
WORD_EXAMPLES = [("Great movie! Loved it!", (0.55, 0.30)),
                 ("Waste of time. Very boring", (0.06, 0.62)),
                 ("Great action, great effects, fantastic acting, funny humor.", (0.30, 0.90))]
COUNT_TICKS = [0, 1, 2, 5, 10, 20]


@steps("reviews-words", 3)
def reviews_words(step):
    counts, X, lab, C, sent, text = review_word_counts()
    fig, ax = fixed_fig(SPLIT, 90, 40, 120, 90)
    tidy(ax)
    ticks = np.log1p(COUNT_TICKS)
    lim = (-0.25, np.log1p(32))
    ax.set_xlim(lim)
    ax.set_ylim(lim)
    ax.set_xticks(ticks, COUNT_TICKS)
    ax.set_yticks(ticks, COUNT_TICKS)
    ax.set_xlabel("Positive words in the review (great, love, like, …)")
    ylabel_top(ax, "Negative words (bad, boring, waste, …)")
    # one dot per (positive, negative) pair; dot area grows with the number of reviews
    cells, inverse, n = np.unique(counts, axis=0, return_inverse=True, return_counts=True)
    inverse = inverse.ravel()
    P = np.log1p(cells)
    size = 10 + 1.3 * n
    cell_lab = np.array([lab[inverse == i][0] for i in range(len(cells))])
    if step == 0:
        ax.scatter(*P.T, s=size, color=STEEL, alpha=0.55, lw=0, zorder=3)
        for quote, spot in WORD_EXAMPLES:
            i = next(j for j, t in enumerate(text) if quote in t)
            p, q = counts[i]
            ax.scatter(*X[i], s=size[inverse[i]] + 60, facecolor="none", edgecolor=ORANGE,
                       lw=2.2, zorder=5)
            ax.annotate(f"“{quote}”\n{p} positive, {q} negative", X[i], xytext=spot,
                        textcoords="axes fraction", fontsize=13, color=INK, zorder=7,
                        bbox=dict(boxstyle="round,pad=0.3", facecolor=PAPER, edgecolor=BORDER),
                        arrowprops=dict(arrowstyle="-", color=ORANGE, lw=1.3, shrinkB=7))
        note(ax, f"{len(counts):,} reviews; dot area = how many share those two counts", size=18)
        return fig
    for k in range(3):
        m, fill, edge = CLUSTER_STYLE[k]
        sel = cell_lab == k
        ax.scatter(*P[sel].T, marker=m, s=size[sel] * (1.25 if m == "^" else 1.0), color=fill,
                   edgecolor=edge, lw=0.6, alpha=0.85, zorder=3)
    centroids(ax, C, size=300)
    if step == 1:
        note(ax, "k-means, K = 3, on the two counts (log scale)", size=18)
        return fig
    spots = {0: (0.62, 0.22), 1: (0.62, 0.88), 2: (0.06, 0.88)}
    for k in range(3):
        sel = lab == k
        shares = "  ".join(f"{s[:3]} {np.mean(sent[sel] == s):.0%}" for s in SENTIMENTS)
        ax.annotate(f"{sel.sum():,} reviews\n{shares}", C[k], xytext=spots[k],
                    textcoords="axes fraction", fontsize=13, color=INK, zorder=7,
                    bbox=dict(boxstyle="round,pad=0.3", facecolor=PAPER, edgecolor=BORDER),
                    arrowprops=dict(arrowstyle="-", color=STEEL, lw=1.1, shrinkB=12))
    note(ax, "Reveal the labels: word counts lean the right way, but only lean", size=18)
    return fig


# ---------------------------------------------- appendix: Zachary's karate club

@lru_cache(maxsize=None)
def karate():
    """Zachary (1977), as packaged by networkx: 34 members, 78 unweighted ties.

    Split in two by the sign of the Laplacian's second eigenvector (spectral clustering).
    """
    G = nx.karate_club_graph()
    nodes = list(G)
    pos = nx.spring_layout(G, seed=418)
    P = np.array([pos[n] for n in nodes])
    hi = np.array([G.nodes[n]["club"] == "Mr. Hi" for n in nodes])
    w, v = np.linalg.eigh(nx.laplacian_matrix(G, nodelist=nodes).toarray().astype(float))
    side = v[:, 1] > 0
    if (side == hi).sum() < (side != hi).sum():  # an eigenvector's sign is arbitrary
        side = ~side
    return G, nodes, P, hi, side


@steps("karate-club", 2)
def karate_club(step):
    G, nodes, P, hi, side = karate()
    fig, ax = fixed_fig(SPLIT, 30, 30, 110, 30)
    bare(ax)
    ax.set_aspect("equal")
    ax.margins(0.08)
    for a, b in G.edges():
        ax.plot(*P[[a, b]].T, color=BORDER, lw=1.2, zorder=1)
    if step == 0:
        ax.scatter(P[:, 0], P[:, 1], s=170, color=STEEL, edgecolor=PAPER, lw=1.2, zorder=3)
        note(ax, f"{len(nodes)} club members, {G.number_of_edges()} friendships:\n"
                 "who sits with whom?", size=17)
    else:
        for is_hi, m in ((True, "o"), (False, "s")):
            for is_side, fill, edge in ((True, STEEL, PAPER), (False, PAPER, INK)):
                sel = (hi == is_hi) & (side == is_side)
                ax.scatter(P[sel, 0], P[sel, 1], marker=m, s=190 if m == "o" else 160,
                           color=fill, edgecolor=edge, lw=1.4, zorder=3)
        miss = hi != side
        ax.scatter(P[miss, 0], P[miss, 1], s=620, facecolor="none", edgecolor=ORANGE, lw=3,
                   zorder=4)
        note(ax, f"Spectral split matches the real split for {(~miss).sum()} of {len(nodes)}",
             size=17)
        ax.text(0.03, 0.90, "Shape = the side each member joined (● Mr. Hi, ■ officer)\n"
                            "Fill = the spectral clustering (filled vs. hollow)",
                transform=fig.transFigure, fontsize=14, color=STEEL, va="top")
    for n, name, xy, ha, va in ((0, "Mr. Hi", (-40, -40), "right", "top"),
                                (33, "Officer", (100, -50), "left", "top")):
        ax.annotate(name, P[n], xytext=xy, textcoords="offset points", ha=ha,
                    va=va, fontsize=15, color=INK, zorder=5,
                    arrowprops=dict(arrowstyle="-", color=INK, lw=1.2, shrinkB=9),
                    bbox=dict(boxstyle="square,pad=0.1", facecolor=PAPER, edgecolor="none"))
    return fig


@steps("karate-embed", 2)
def karate_embed(step):
    """Each member placed at (2nd, 3rd) Laplacian eigenvector entries; split at 0 on the first."""
    G, nodes, P, hi, side = karate()
    w, v = np.linalg.eigh(nx.laplacian_matrix(G, nodelist=nodes).toarray().astype(float))
    E = v[:, 1:3] * (-1 if v[0, 1] > 0 else 1)  # Mr. Hi on the left
    fig, ax = fixed_fig(SPLIT, 90, 40, 120, 90)
    tidy(ax)
    ax.set_xlabel("Eigenvector 2 of the network (the 'Fiedler vector')")
    ylabel_top(ax, "Eigenvector 3")
    if step == 0:
        ax.scatter(*E.T, s=150, color=STEEL, edgecolor=PAPER, lw=1.2, zorder=3)
        note(ax, "The network, turned into coordinates", size=18)
    else:
        left = E[:, 0] < 0
        ax.axvline(0, color=ORANGE, lw=2.5, zorder=2)
        ax.scatter(*E[left].T, s=150, color=STEEL, edgecolor=PAPER, lw=1.2, zorder=3)
        ax.scatter(*E[~left].T, s=150, color=PAPER, edgecolor=INK, lw=1.4, zorder=3)
        note(ax, f"Split at 0: {left.sum()} members left, {(~left).sum()} right", size=18)
    for n, name, off in ((0, "Mr. Hi", (12, 10)), (33, "Officer", (-12, 10))):
        ax.annotate(name, E[n], xytext=off, textcoords="offset points", fontsize=15, color=INK,
                    ha="left" if off[0] > 0 else "right", va="bottom", zorder=5)
    return fig


# --------------------------------------------- appendix: color compression

PHOTOS = {"color-compression": OUT_DIR.parent / "orange-line-stops-better" / "stop11-ashland-a.jpg",
          "color-compression-skyline": OUT_DIR.parent / "orange-line-stops-better" / "stop11-ashland-b.jpg"}
PHOTO_KS = [None, 64, 32, 16, 8, 4, 2]
PHOTO_H = 950  # 60 headline + 720 photo + palette strip and its caption


@lru_cache(maxsize=None)
def photo_lab(path):
    from skimage.color import rgb2lab
    from PIL import Image
    im = Image.open(path).convert("RGB")
    im = im.resize((960, round(960 * im.height / im.width)), Image.LANCZOS)
    rgb = np.asarray(im) / 255.0
    return rgb, rgb2lab(rgb)


def quantize(k, path):
    """k-means in CIELAB (distance ~ perceived color difference), fit on 20,000 pixels."""
    from skimage.color import lab2rgb
    rgb, lab = photo_lab(path)
    flat = lab.reshape(-1, 3)
    rng = np.random.default_rng(418)
    km = KMeans(k, n_init=4, random_state=418).fit(flat[rng.choice(len(flat), 20000, replace=False)])
    lab_idx = km.predict(flat)
    pal = np.clip(lab2rgb(km.cluster_centers_[None])[0], 0, 1)
    return pal[lab_idx].reshape(rgb.shape), pal, np.bincount(lab_idx, minlength=k) / len(lab_idx)


def color_compression(step, path):
    k = PHOTO_KS[step]
    rgb, _ = photo_lab(path)
    fig = plt.figure(figsize=(1000 / DPI, PHOTO_H / DPI), dpi=DPI)
    fig.patch.set_facecolor(PAPER)
    fig.raster = "jpg" if k is None else "png"
    h, w = rgb.shape[:2]
    ax = fig.add_axes([20 / 1000, 160 / PHOTO_H, 960 / 1000, h / PHOTO_H])
    bare(ax)
    if k is None:
        ax.imshow(rgb)
        head = "Original: millions of possible colors, 24 bits per pixel"
    else:
        img, pal, share = quantize(k, path)
        ax.imshow(img)
        bits = int(np.log2(k))
        head = f"{k} colors: {bits} bit{'s' if bits > 1 else ''} per pixel ({24 / bits:.2g}× smaller)"
        strip = fig.add_axes([20 / 1000, 70 / PHOTO_H, 960 / 1000, 50 / PHOTO_H])
        bare(strip)
        x = 0.0
        for i in np.argsort(share)[::-1]:  # palette, widths = share of pixels
            strip.add_patch(plt.Rectangle((x, 0), share[i], 1, facecolor=pal[i], edgecolor="none"))
            x += share[i]
        strip.set_xlim(0, 1)
        strip.set_ylim(0, 1)
        fig.text(20 / 1000, 30 / PHOTO_H, "The palette k-means chose; each width = share of pixels",
                 fontsize=14, color=STEEL, va="center")
    fig.text(20 / 1000, 1 - 32 / PHOTO_H, head, fontsize=20, color=INK, va="center")
    return fig


for _name, _path in PHOTOS.items():
    steps(_name, len(PHOTO_KS))(lambda step, path=_path: color_compression(step, path))


# ---------------------------------------------------------------------- main

def main(argv: list[str]) -> None:
    if FONT_PATH.exists():
        font_manager.fontManager.addfont(str(FONT_PATH))
        family = font_manager.FontProperties(fname=str(FONT_PATH)).get_name()
        # DejaVu Sans (bundled with matplotlib) supplies the shape glyphs.
        plt.rcParams["font.family"] = [family, "DejaVu Sans"]
        plt.rcParams["mathtext.fontset"] = "custom"
        for slot in ("rm", "it", "bf"):
            plt.rcParams[f"mathtext.{slot}"] = family
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
