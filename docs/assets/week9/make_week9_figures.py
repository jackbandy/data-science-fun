#!/usr/bin/env python3
"""Figures for the Week 9, Day 1 slides: k-nearest neighbors and decision trees.

NOTICE: this file was substantially drafted by an LLM coding system and has not
yet been reviewed. Check every figure against the slide it illustrates.

Follows docs/assets/STYLE.md and mirrors week8/make_week8_figures.py:
golden-ratio canvases, grayscale neutrals with orange reserved for the focal
element, vendored Libre Franklin drawn as paths so each SVG is self-contained.

Most figures are step sets: `name-v0.svg`, `name-v1.svg`, ... each adding one
thing (a data point, a distance, a split) to the one before, for the deck's
r-stack fragments.

Color and shape carry the class everywhere in this deck:
  * positive class (+, "yes", "like", pass): orange triangle. It is the class
    the classifier is looking for, so it gets the accent color.
  * negative class (-, "no", "hate", fail): steel-gray circle with a
    white minus inside, keeping the - of the CIML and Lecture 13 notation.
  * a point still waiting for a label: white square with "?".
  Shapes repeat the color so the slides survive grayscale printing. Figure text
  names the classes with the same shapes (U+25B2, U+25CF, from the DejaVu Sans
  fallback font).

Step sets whose data must not move between slides (knn-steps, knn-lazy,
choose-k) are drawn on a fixed 1000 x 618 canvas with a golden-ratio plot area
and saved without tight cropping, so every frame lines up exactly.

Data:
  * Exercise 12.4 / 13.1 numbers, the tax-cheating tree, and the 18/20 and
    400/1200 split counts are copied from the cited lecture slides and CIML.
  * The study-hours students (Week 8's, plus a random day of month born) and
    the two-class point clouds are synthetic.
  * The class survey (`survey-*` figures, the deck's running example) is
    synthetic, from `make_survey`, the same generator as the code demo.
  See SOURCES.md in this folder.

Usage:  python3 make_week9_figures.py [name ...]
"""

from __future__ import annotations

import sys
from pathlib import Path

import matplotlib

matplotlib.use("Agg")

import matplotlib.pyplot as plt
import numpy as np
from matplotlib import font_manager
from matplotlib.patches import Circle, FancyBboxPatch
from matplotlib.path import Path as MPath
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier

OUT_DIR = Path(__file__).resolve().parent
REPO_ROOT = OUT_DIR.parents[2]
FONT_PATH = OUT_DIR.parent / "fonts" / "libre-franklin" / "LibreFranklin-Regular.ttf"

# STYLE.md palette
INK = "#1A1A1A"
STEEL = "#565A5C"
MUTED = "#777777"
QUIET = "#AAAAAA"
BORDER = "#DDDDDD"
SOFT_GRAY = "#F4F4F2"
PAPER = "#FFFFFF"
ORANGE = "#F9461C"
NODE_FILL = "#EEEEEE"
HIGHLIGHT = "#222222"

# Region tints for decision boundaries: a light wash of each class color.
POS_TINT = "#FDE3DA"
NEG_TINT = "#ECECEC"

PHI = (1 + 5**0.5) / 2
WIDTH_PX = 1000
DPI = 100

# Class glyphs for figure text, matching the point markers.
POS_GLYPH = "\u25B2"  # ▲
NEG_GLYPH = "\u25CF"  # ●

# A filled bar, so the negative class reads as a "minus" next to the "plus".
MINUS = MPath([(-1, -0.3), (1, -0.3), (1, 0.3), (-1, 0.3), (-1, -0.3)],
              [MPath.MOVETO, MPath.LINETO, MPath.LINETO, MPath.LINETO, MPath.CLOSEPOLY])

FIGURES: dict[str, callable] = {}


def figure(name: str):
    """Register a builder under the filename stem it writes."""
    def wrap(fn):
        FIGURES[name] = fn
        return fn
    return wrap


def steps(name: str, n: int):
    """Register `name-v0` ... `name-v{n-1}`, each built by fn(step)."""
    def wrap(fn):
        for i in range(n):
            FIGURES[f"{name}-v{i}"] = (lambda i=i: fn(i))
        return fn
    return wrap


def new_fig(width=WIDTH_PX, height=None, **kw):
    height = height or round(width / PHI)
    fig, ax = plt.subplots(figsize=(width / DPI, height / DPI), dpi=DPI, **kw)
    fig.patch.set_facecolor(PAPER)
    for a in np.atleast_1d(ax).ravel():
        a.set_facecolor(PAPER)
    return fig, ax


def tidy(ax, *, grid="both", spines=("left", "bottom")):
    """The deck's default axis furniture: two hairline spines, one grid."""
    for side in ("top", "right", "left", "bottom"):
        ax.spines[side].set_visible(side in spines)
        ax.spines[side].set_color(BORDER)
    if grid:
        ax.grid(axis=grid, color=BORDER, linewidth=0.8, alpha=0.7)
    ax.set_axisbelow(True)
    ax.tick_params(colors=STEEL, labelsize=12, length=0)
    for lbl in (ax.xaxis.label, ax.yaxis.label):
        lbl.set_color(STEEL)
        lbl.set_fontsize(15)
    return ax


def fixed_fig(left, right, top, bottom):
    """A fixed 1000 x 618 canvas with one axes inset by the given pixel margins.

    Saved uncropped (see `save`), so frames of a step set stack pixel for pixel.
    """
    width, height = WIDTH_PX, round(WIDTH_PX / PHI)
    fig = plt.figure(figsize=(width / DPI, height / DPI), dpi=DPI)
    fig.patch.set_facecolor(PAPER)
    ax = fig.add_axes([left / width, bottom / height,
                       (width - left - right) / width, (height - top - bottom) / height])
    ax.set_facecolor(PAPER)
    fig.fixed_layout = True
    return fig, ax


def golden_fig():
    """`fixed_fig` with a golden-ratio plot area, for 0..10*PHI by 0..10."""
    height = round(WIDTH_PX / PHI)
    top, bottom = 50, 34
    side = (WIDTH_PX - (height - top - bottom) * PHI) / 2
    return fixed_fig(side, side, top, bottom)


GOLDEN_LIM = ((0, 10 * PHI), (0, 10))


def save(fig, name):
    out = OUT_DIR / f"{name}.svg"
    if getattr(fig, "fixed_layout", False):
        fig.savefig(out, format="svg", facecolor=PAPER)
    else:
        fig.savefig(out, format="svg", facecolor=PAPER, bbox_inches="tight",
                    pad_inches=0.12)
    plt.close(fig)
    print(f"  wrote {out.relative_to(REPO_ROOT)}")


# ---------------------------------------------------------------- shared marks

def neg_marks(ax, X, *, size, edgecolor=PAPER, linewidth=0.8, alpha=1.0, zorder=4):
    """Steel circles with a white minus inside."""
    X = np.atleast_2d(X)
    ax.scatter(X[:, 0], X[:, 1], marker="o", s=size * 1.2, color=STEEL,
               edgecolor=edgecolor, linewidth=linewidth, alpha=alpha, zorder=zorder)
    ax.scatter(X[:, 0], X[:, 1], marker=MINUS, s=size * 0.5, color=PAPER,
               linewidth=0, alpha=alpha, zorder=zorder + 0.1)


def pos_marks(ax, X, *, size, edgecolor=PAPER, linewidth=0.8, alpha=1.0, zorder=4):
    """Orange triangles, drawn a little larger so they weigh the same as circles."""
    X = np.atleast_2d(X)
    ax.scatter(X[:, 0], X[:, 1], marker="^", s=size * 1.3, color=ORANGE,
               edgecolor=edgecolor, linewidth=linewidth, alpha=alpha, zorder=zorder)


def points(ax, X, y, *, size=170, alpha=1.0, zorder=4):
    """Plot +1 as orange triangles and -1 (or 0) as steel circles with a minus."""
    X, y = np.asarray(X, float), np.asarray(y)
    pos = y == 1
    pos_marks(ax, X[pos], size=size, alpha=alpha, zorder=zorder)
    neg_marks(ax, X[~pos], size=size, alpha=alpha, zorder=zorder)


def query(ax, xy, label=None, *, size=420, text="?"):
    """The point we are asked to classify: a square with '?' until it has a label,
    then the class's own shape, outlined in ink."""
    if label is None:
        ax.scatter([xy[0]], [xy[1]], marker="s", s=size * 0.85, color=PAPER,
                   edgecolor=INK, linewidth=2.2, zorder=6)
        ax.text(xy[0], xy[1], text, ha="center", va="center_baseline",
                fontsize=17, color=INK, zorder=7)
    elif label == 1:
        pos_marks(ax, xy, size=size, edgecolor=INK, linewidth=2.2, zorder=6)
    else:
        neg_marks(ax, xy, size=size, edgecolor=INK, linewidth=2.2, zorder=6)


def ring(ax, xy, r, *, color=INK, lw=2.2, ls="-"):
    ax.add_patch(Circle(xy, r, fill=False, edgecolor=color, linewidth=lw,
                        linestyle=ls, zorder=5))


def halo(ax, XY, *, size=520):
    """Thin ring around the chosen neighbors."""
    XY = np.atleast_2d(XY)
    ax.scatter(XY[:, 0], XY[:, 1], s=size, facecolor="none", edgecolor=INK,
               linewidth=1.6, zorder=3)


def shade(ax, model_predict, xlim, ylim, *, n=400, boundary=True):
    """Tint each region by the class the model predicts there."""
    xx, yy = np.meshgrid(np.linspace(*xlim, n), np.linspace(*ylim, n))
    Z = model_predict(np.c_[xx.ravel(), yy.ravel()]).reshape(xx.shape)
    Z = (Z == 1).astype(float)
    ax.contourf(xx, yy, Z, levels=[-0.5, 0.5, 1.5], colors=[NEG_TINT, POS_TINT],
                zorder=0)
    if boundary and 0 < Z.mean() < 1:
        ax.contour(xx, yy, Z, levels=[0.5], colors=[INK], linewidths=1.6, zorder=1)


def plain_axes(ax, xlim, ylim, xlabel="$x_1$", ylabel="$x_2$", *, ticks=False):
    ax.set_xlim(*xlim)
    ax.set_ylim(*ylim)
    ax.set_aspect("equal")
    tidy(ax, grid="both" if ticks else None)
    if not ticks:
        ax.set_xticks([])
        ax.set_yticks([])
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel, rotation=0, labelpad=14)


def note(ax, text, *, x=0.0, y=1.02, color=INK, size=17, ha="left", va="bottom"):
    ax.text(x, y, text, transform=ax.transAxes, fontsize=size, color=color,
            ha=ha, va=va)


# ------------------------------------------------------------- k-NN, by hand

# Hand-placed so the single nearest neighbor of Q is a noisy minus sitting
# inside the plus cluster (CIML Fig. 3.4's setup), while 2 of the 3 nearest
# are plusses. Placed on a 10 x 10 square, then stretched by PHI along x to
# fill the golden-ratio plot area; the neighbor order survives the stretch.
KNN_POS = np.array([(7.1, 6.9), (6.9, 5.6), (5.7, 7.3), (8.2, 7.6), (7.9, 5.0),
                    (8.6, 8.7), (6.6, 8.5), (9.0, 6.3)])
KNN_NEG = np.array([(5.85, 5.95), (2.0, 3.0), (3.1, 2.2), (2.6, 4.3), (1.4, 5.0),
                    (3.8, 3.6), (4.2, 1.4), (1.6, 1.6), (3.3, 5.2)])
KNN_X = np.vstack([KNN_POS, KNN_NEG]) * (PHI, 1)
KNN_Y = np.r_[np.ones(len(KNN_POS)), -np.ones(len(KNN_NEG))]
KNN_Q = np.array([6.4, 6.4]) * (PHI, 1)
KNN_LIM = GOLDEN_LIM


def radius_for(k, dists):
    """A ring radius halfway between the k-th and (k+1)-th nearest distance."""
    d = np.sort(dists)
    return (d[k - 1] + d[k]) / 2


@steps("knn-steps", 5)
def knn_steps(step):
    fig, ax = golden_fig()
    plain_axes(ax, *KNN_LIM)
    d = np.linalg.norm(KNN_X - KNN_Q, axis=1)
    order = np.argsort(d)
    assert KNN_Y[order[0]] == -1 and KNN_Y[order[:3]].sum() > 0
    captions = [
        "1. Training data: each example is a point with a label",
        "2. A new example arrives. What is its label?",
        "3. Compute its distance to every training example",
        f"4. k = 1: the single nearest neighbor is {NEG_GLYPH} … so predict {NEG_GLYPH}",
        f"5. k = 3: two {POS_GLYPH} and one {NEG_GLYPH} vote, so predict {POS_GLYPH}",
    ]
    points(ax, KNN_X, KNN_Y)
    if step >= 1:
        label = {3: -1, 4: 1}.get(step)
        query(ax, KNN_Q, label)
    if step == 2:
        for p in KNN_X:
            ax.plot([KNN_Q[0], p[0]], [KNN_Q[1], p[1]], color=QUIET, lw=1.1,
                    ls=(0, (4, 3)), zorder=2)
    if step >= 3:
        k = 1 if step == 3 else 3
        ring(ax, KNN_Q, radius_for(k, d))
        halo(ax, KNN_X[order[:k]])
    note(ax, captions[step])
    return fig


# Exercise 13.1 (Bello, Lecture 13): five labeled points and z = (3, 2).
EX131_X = np.array([(2.5, 3.5), (1.5, 4.0), (5.0, 1.5), (4.0, 2.5), (2.0, 1.0)])
EX131_Y = np.array([1, 1, -1, -1, 1])
EX131_Z = np.array([3.0, 2.0])


@steps("ex13-1", 5)
def ex13_1(step):
    fig, ax = new_fig(height=640)
    plain_axes(ax, (0, 6), (0, 5), "A", "B", ticks=True)
    points(ax, EX131_X, EX131_Y, size=200)
    d = np.linalg.norm(EX131_X - EX131_Z, axis=1)
    order = np.argsort(d)
    for i, (x, yv) in enumerate(EX131_X):
        lbl = f"$x_{i + 1}$"
        if step >= 2:
            lbl += f"  d = {d[i]:.2f}"
        ax.text(x + 0.3, yv + 0.12, lbl, fontsize=15, color=INK, zorder=8)
    if step >= 1:
        label = {2: -1, 4: 1}.get(step)
        query(ax, EX131_Z, label, text="z")
    # Inside mathtext, the glyphs only reach the STIX fallback in math mode.
    P, N = f"${POS_GLYPH}$", f"${NEG_GLYPH}$"
    captions = [
        "Training data",
        "Classify z = (3.0, 2.0)",
        f"k = 1: nearest is $x_4$ ({N}), so predict {N}",
        f"k = 2: $x_4$ ({N}) and $x_5$ ({P}) tie 1 to 1, so choose randomly",
        f"k = 3: $x_4$ ({N}), $x_5$ ({P}), $x_1$ ({P}): predict {P}",
    ]
    if step >= 2:
        k = step - 1
        ring(ax, EX131_Z, radius_for(k, d))
        halo(ax, EX131_X[order[:k]], size=600)
    note(ax, captions[step])
    return fig


@steps("distance", 3)
def distance(step):
    """Euclidean vs. Manhattan between a = (3, 4) and b = (2, 2), Lecture 13."""
    fig, ax = new_fig(width=620, height=620)
    a, b = (3, 4), (2, 2)
    plain_axes(ax, (0, 5), (0, 5), "", "", ticks=True)
    ax.set_xticks(range(6))
    ax.set_yticks(range(6))
    if step >= 2:
        ax.plot([b[0], a[0], a[0]], [b[1], b[1], a[1]], color=STEEL, lw=3.5,
                ls=(0, (5, 3)), solid_capstyle="round", zorder=3)
        ax.text(2.5, 1.72, "1", ha="center", fontsize=18, color=STEEL)
        ax.text(3.18, 3.0, "2", va="center", fontsize=18, color=STEEL)
        ax.text(3.35, 2.35, "Manhattan\n1 + 2 = 3", fontsize=17, color=STEEL,
                va="center")
    if step >= 1:
        ax.plot([b[0], a[0]], [b[1], a[1]], color=ORANGE, lw=3.5, zorder=4,
                solid_capstyle="round")
        ax.text(1.2, 3.35, "Euclidean\n√(1² + 2²) = √5 ≈ 2.24",
                fontsize=17, color=ORANGE, ha="center", va="center")
    for (x, yv), name, dx, dy, ha in ((a, "a = (3, 4)", 0.15, 0.18, "left"),
                                      (b, "b = (2, 2)", -0.15, -0.35, "right")):
        ax.scatter([x], [yv], s=150, color=INK, zorder=6)
        ax.text(x + dx, yv + dy, name, fontsize=17, color=INK, ha=ha)
    return fig


@steps("knn-lazy", 4)
def knn_lazy(step):
    """The 1-NN boundary redraws itself as each training point arrives."""
    fig, ax = golden_fig()
    plain_axes(ax, *KNN_LIM)
    # Arrival order: alternate classes so every frame has both.
    order = [0, 10, 3, 13, 1, 11, 7, 15, 2, 12, 4, 14, 5, 16, 6, 9, 8]
    n = [2, 4, 8, len(order)][step]
    idx = order[:n]
    X, y = KNN_X[idx], KNN_Y[idx]
    model = KNeighborsClassifier(n_neighbors=1).fit(X, y)
    shade(ax, model.predict, *KNN_LIM)
    points(ax, X, y)
    note(ax, f"1-nearest neighbor with {n} training examples")
    return fig


# --------------------------------------------- a noisy two-class point cloud

def two_class(n, rng, *, flip=0.0):
    """Two overlapping blobs; `flip` is the fraction of labels swapped (noise)."""
    n_pos = n * 7 // 15
    pos = rng.normal((6.4, 6.0), (1.35, 1.2), size=(n_pos, 2))
    neg = rng.normal((3.6, 4.0), (1.35, 1.25), size=(n - n_pos, 2))
    X = np.vstack([pos, neg])
    y = np.r_[np.ones(n_pos), -np.ones(n - n_pos)]
    if flip:
        swap = rng.random(n) < flip
        y[swap] *= -1
    return X, y


def cloud():
    """60 points (27 +, 33 -) including three deliberately mislabeled examples."""
    rng = np.random.default_rng(418)
    X, y = two_class(60, rng)
    X = np.clip(X, 0.4, 9.6)
    # Label noise: flip the plus nearest each of two spots inside the plus
    # cluster and the minus nearest one spot inside the minus cluster, so each
    # mislabeled point sits well inside the other class.
    noisy = [int(np.argmin(np.where(y == cls, np.linalg.norm(X - spot, axis=1), np.inf)))
             for cls, spot in ((1, (7.3, 7.0)), (1, (5.6, 7.4)), (-1, (3.0, 3.2)))]
    y[noisy] *= -1
    return X, y, noisy


CLOUD_LIM = ((0, 10), (0, 10))


@steps("choose-k", 4)
def choose_k(step):
    # The same cloud, stretched by PHI along x to fill the golden plot area.
    X, y, noisy = cloud()
    X = X * (PHI, 1)
    fig, ax = golden_fig()
    plain_axes(ax, *GOLDEN_LIM)
    if step == 0:
        halo(ax, X[noisy], size=650)
        note(ax, f"{len(y)} training examples ({int((y == 1).sum())} {POS_GLYPH}, "
                 f"{int((y == -1).sum())} {NEG_GLYPH}); ringed labels are noise")
    else:
        k = [None, 1, 7, len(y)][step]
        model = KNeighborsClassifier(n_neighbors=k).fit(X, y)
        shade(ax, model.predict, *GOLDEN_LIM)
        msg = {1: "k = 1: an island around every noisy label (overfit)",
               2: "k = 7: a smoother boundary",
               3: f"k = N = {len(y)}: always the majority class, {NEG_GLYPH} (underfit)"}
        note(ax, msg[step])
    points(ax, X, y)
    return fig


@steps("k-accuracy", 3)
def k_accuracy(step):
    """Train vs. held-out accuracy as k grows, averaged over 40 draws; `depth_accuracy`'s data."""
    ks = np.array([1, 3, 5, 7, 9, 11, 15, 21, 31, 41, 51, 75, 101, 125, 149])  # odd, so votes never tie
    train, test = np.zeros(len(ks)), np.zeros(len(ks))
    reps = 40
    for r in range(reps):
        rng = np.random.default_rng(1000 + r)
        Xtr, ytr = two_class(150, rng, flip=0.1)
        Xte, yte = two_class(1500, rng, flip=0.1)
        for i, k in enumerate(ks):
            m = KNeighborsClassifier(n_neighbors=int(k)).fit(Xtr, ytr)
            train[i] += m.score(Xtr, ytr)
            test[i] += m.score(Xte, yte)
    train /= reps
    test /= reps
    fig, ax = new_fig(height=560)
    tidy(ax, grid="y")
    ax.plot(ks, train, color=STEEL, lw=3, marker="o", ms=6)
    ax.text(ks[-1] * 1.12, train[-1], "training", color=STEEL, fontsize=16, va="bottom")
    if step >= 1:
        ax.plot(ks, test, color=ORANGE, lw=3, marker="o", ms=6)
        ax.text(ks[-1] * 1.12, test[-1], "held-out", color=ORANGE, fontsize=16, va="top")
    if step >= 2:
        b = int(np.argmax(test))
        ax.scatter([ks[b]], [test[b]], s=260, facecolor="none", edgecolor=INK, lw=2.2, zorder=5)
        ax.annotate(f"best held-out: k = {ks[b]}", (ks[b], test[b]), xytext=(6, 0.94),
                    fontsize=16, color=INK, arrowprops=dict(arrowstyle="-", color=INK, lw=1.2))
        ax.text(1, 0.56, "overfit\n(k = 1)", fontsize=14, color=STEEL)
        ax.text(105, 0.6, "underfit\n(k ≈ N)", fontsize=14, color=STEEL, ha="right")
    ax.set_xscale("log")
    ax.set_xlim(0.8, 330)
    ax.set_ylim(0.5, 1.02)
    ax.set_xticks([1, 3, 10, 30, 100])
    ax.set_xticklabels(["1", "3", "10", "30", "100"])
    ax.set_xlabel("k (number of neighbors, log scale)")
    ax.set_ylabel("accuracy")
    ax.yaxis.set_major_formatter(lambda v, _: f"{v:.0%}")
    return fig


# ------------------------------------------------------ k-NN pitfalls

# Week 8's study-hours students (`supervised-two-kinds` in week8/make_week8_figures.py), same seed and draws, so the points match last week's slide. Pass (score of 70 or more) is the positive class.
# Day of month born is pure noise. Seed 182 is picked from 300 so that "born on or before the 15th?" gains exactly nothing and k-NN visibly follows birthdays; across the 300 seeds the median share of the plane whose prediction flips is 28% (38% here).
HOURS_K = 5
HOURS_Q = (1.0, 17)  # a new student: studied 1 hour, born on the 17th


def study_hours():
    """(hours studied, Week 8's jitter for the pass/fail rows, day of month born, passed)."""
    rng = np.random.default_rng(418)
    hours = rng.uniform(0, 10, 30)
    score = np.clip(45 + 5 * hours + rng.normal(0, 7, hours.size), 0, 100)
    jitter = rng.uniform(-0.12, 0.12, hours.size)
    day = np.random.default_rng(182).integers(1, 32, hours.size)
    return hours, jitter, day, (score >= 70).astype(int)


HOURS_XLIM = (-0.4, 10.4)


def pass_fail_rows(ax, *, ylim=(-0.7, 1.7)):
    """Week 8's layout: hours along x, a fail row and a pass row."""
    ax.set_xlim(*HOURS_XLIM)
    ax.set_ylim(*ylim)
    tidy(ax, grid=None)
    ax.set_xticks([0, 2, 4, 6, 8, 10])
    ax.set_yticks([0, 1], ["fail", "pass"])
    ax.tick_params(axis="y", labelsize=15)
    ax.set_xlabel("hours studied")


@steps("hours-knn", 2)
def hours_knn(step):
    """k-NN on hours studied alone (Week 8's layout), then with day of month born added in raw units.

    The second frame is drawn at equal scale, one day as long as one hour, so the ringed neighbors are visibly the nearest points. That only fits a slide with days along x, so hours move to the y-axis.
    """
    hours, jitter, day, y = study_hours()
    if step == 0:
        fig, ax = fixed_fig(left=130, right=30, top=56, bottom=72)
        X, q = np.c_[hours, y + jitter], (HOURS_Q[0], 0.5)
        d = np.abs(hours - q[0])
        pass_fail_rows(ax)
        lead = "Hours studied only"
    else:
        # Same 1000 x 618 canvas as frame 0, so the r-stack frames cover each other; the margins leave an equal-scale 32 x 11.2 plot area.
        fig, ax = fixed_fig(left=130, right=30, top=160, bottom=164)
        X, q = np.c_[day, hours], HOURS_Q[::-1]
        d = np.linalg.norm(X - q, axis=1)
        ax.set_xlim(0, 32)
        ax.set_ylim(-0.6, 10.6)
        ax.set_aspect("equal")
        tidy(ax, grid=None)
        ax.set_xticks([1, 5, 10, 15, 20, 25, 31])
        ax.set_yticks([0, 5, 10])
        ax.set_xlabel("day of month born")
        ax.set_ylabel("hours\nstudied", rotation=0, labelpad=30, va="center")
        lead = "Add day of month born"
    near = np.argsort(d)[:HOURS_K]
    pred = int(y[near].sum() * 2 > HOURS_K)
    for j in near:
        ax.plot([q[0], X[j, 0]], [q[1], X[j, 1]], color=INK, lw=1.4, ls=(0, (4, 3)), zorder=2)
    points(ax, X, y, size=120)
    halo(ax, X[near], size=330)
    query(ax, q, pred, size=330)
    n_pos = int(y[near].sum())
    note(ax, f"{lead}: the {HOURS_K} nearest are {n_pos} {POS_GLYPH} and {HOURS_K - n_pos} {NEG_GLYPH}, "
             f"so predict {'pass' if pred else 'fail'}", size=17)
    # Below the axis on the equal-scale frame, where points fill the lower-right corner.
    ax.text(0.99, 0.02 if step == 0 else -0.2, f"{POS_GLYPH} pass   {NEG_GLYPH} fail", transform=ax.transAxes, fontsize=14,
            color=STEEL, ha="right", va="bottom" if step == 0 else "top", bbox=dict(facecolor=PAPER, edgecolor="none", pad=2), zorder=8)
    return fig


# Irrelevant feature: one feature separates the classes on its own.
REL_POS = np.array([6.3, 6.9, 7.4, 8.1, 8.8, 9.4])
REL_NEG = np.array([0.8, 1.6, 2.3, 3.1, 3.9, 4.6])
IRR_POS = np.array([9.5, 1.0, 8.8, 0.5, 9.0, 1.5])
IRR_NEG = np.array([8.5, 2.5, 6.0, 9.6, 4.2, 5.5])
REL_Q = np.array([5.8, 5.0])


@steps("irrelevant", 2)
def irrelevant(step):
    fig, ax = new_fig(height=640)
    x = np.r_[REL_POS, REL_NEG]
    yl = np.r_[np.ones(6), -np.ones(6)]
    if step == 0:
        X, q = np.c_[x, np.full(12, 5.0)], REL_Q
        ylabel = ""
        caption = (f"One relevant feature: the 3 nearest are {POS_GLYPH}, {POS_GLYPH}, "
                   f"{NEG_GLYPH}, so predict {POS_GLYPH} (correct)")
    else:
        X, q = np.c_[x, np.r_[IRR_POS, IRR_NEG]], REL_Q
        ylabel = "random\nnoise"
        caption = f"Add one irrelevant feature: the 3 nearest are all {NEG_GLYPH} (wrong)"
    d = np.linalg.norm(X - q, axis=1)
    order = np.argsort(d)
    pred = 1 if yl[order[:3]].sum() > 0 else -1
    plain_axes(ax, (0, 10), (0, 10), "relevant feature", ylabel)
    if step == 0:
        ax.axhline(5.0, color=BORDER, lw=1, zorder=1)
    points(ax, X, yl)
    ring(ax, q, radius_for(3, d))
    halo(ax, X[order[:3]])
    query(ax, q, pred)
    note(ax, caption, size=16)
    return fig


@figure("knn-vs-tree")
def knn_vs_tree():
    X, y, _ = cloud()
    fig, axes = new_fig(height=520, ncols=2, gridspec_kw={"wspace": 0.12})
    knn = KNeighborsClassifier(n_neighbors=7).fit(X, y)
    tree = DecisionTreeClassifier(criterion="entropy", max_depth=3,
                                  random_state=0).fit(X, y)
    for ax, model, title in ((axes[0], knn, "k-NN, k = 7: any shape"),
                             (axes[1], tree, "Decision tree, depth 3: axis-aligned boxes")):
        plain_axes(ax, *CLOUD_LIM)
        shade(ax, model.predict, *CLOUD_LIM)
        points(ax, X, y, size=110)
        note(ax, title, size=16)
    return fig


# ------------------------------------------------------- tree diagrams

def node_box(ax, xy, text, *, leaf=False, fill=NODE_FILL, edge=INK, color=INK,
             lw=3, w=None, h=0.62, size=16):
    """Rounded-rect internal node, or a pill-shaped leaf (STYLE.md nodes)."""
    w = w or max(1.3, 0.2 * len(text) + 0.5)
    pad = h / 2 if leaf else 0.12
    box = FancyBboxPatch((xy[0] - w / 2 + pad, xy[1] - h / 2 + pad), w - 2 * pad,
                         h - 2 * pad, boxstyle=f"round,pad={pad}",
                         facecolor=fill, edgecolor=edge, linewidth=lw, zorder=3)
    ax.add_patch(box)
    ax.text(xy[0], xy[1], text, ha="center", va="center_baseline", fontsize=size,
            color=color, zorder=4)


def edge(ax, a, b, label=None, *, color=INK, lw=3, size=14, side="left",
         gap=0.36):
    ax.plot([a[0], b[0]], [a[1] - gap, b[1] + gap], color=color, lw=lw,
            solid_capstyle="round", zorder=2)
    if label:
        mx, my = (a[0] + b[0]) / 2, (a[1] + b[1]) / 2
        off = -0.12 if side == "left" else 0.12
        ax.text(mx + off, my, label, fontsize=size, color=color if color != INK else STEEL,
                ha="right" if side == "left" else "left", va="center",
                bbox=dict(facecolor=PAPER, edgecolor="none", pad=1.5), zorder=4)


# Tax-cheating tree from Bello, Lecture 12, slide 8.
TAX_NODES = {
    "refund": ((5.0, 5.3), "Refund", False),
    "no1": ((2.6, 3.9), "NO", True),
    "marital": ((7.2, 3.9), "Marital Status", False),
    "income": ((5.0, 2.5), "Taxable Income", False),
    "no2": ((9.2, 2.5), "NO", True),
    "no3": ((3.3, 1.1), "NO", True),
    "yes": ((6.7, 1.1), "YES", True),
}
TAX_EDGES = [("refund", "no1", "Yes", "left"), ("refund", "marital", "No", "right"),
             ("marital", "income", "Single, Divorced", "left"),
             ("marital", "no2", "Married", "right"),
             ("income", "no3", "< 80K", "left"), ("income", "yes", "> 80K", "right")]
TAX_PATHS = {
    "single-no-refund-100k": ["refund", "marital", "income", "yes"],
    "married-no-refund-40k": ["refund", "marital", "no2"],
}


def tax_tree(highlight=None, path=None, caption=None):
    fig, ax = new_fig(height=600)
    ax.set_xlim(0.6, 10.6)
    ax.set_ylim(0.5, 5.9)
    ax.axis("off")
    path = path or []
    on_path = set(zip(path, path[1:]))
    groups = {"root": {"refund"}, "internal": {"marital", "income"},
              "leaf": {"no1", "no2", "no3", "yes"}}
    for a, b, lbl, side in TAX_EDGES:
        hot = (a, b) in on_path or highlight == "branch"
        edge(ax, TAX_NODES[a][0], TAX_NODES[b][0], lbl, side=side,
             color=ORANGE if hot else INK, lw=5 if hot else 3)
    for key, (xy, text, leaf) in TAX_NODES.items():
        hot = key in groups.get(highlight, ())
        on = key in path
        node_box(ax, xy, text, leaf=leaf,
                 fill=HIGHLIGHT if hot else NODE_FILL,
                 color=PAPER if hot else INK,
                 edge=ORANGE if on else INK, lw=5 if on else 3,
                 w=1.4 if leaf else None)
    labels = {"root": ((5.0, 5.82), "root node"),
              "internal": ((9.35, 3.9), "internal nodes:\neach splits on\na predictor"),
              "leaf": ((9.3, 1.1), "leaf nodes:\neach holds a\nclass label"),
              "branch": ((0.75, 2.4), "branches:\nconnections\nbetween nodes")}
    if highlight in labels:
        (lx, ly), txt = labels[highlight]
        ax.text(lx, ly, txt, fontsize=16, color=ORANGE, ha="center" if highlight == "root" else "left",
                va="center")
    if caption:
        ax.text(0.6, 0.45, caption, fontsize=16, color=INK, va="top")
    return fig


@steps("tax-tree", 5)
def tax_tree_steps(step):
    return tax_tree([None, "root", "internal", "leaf", "branch"][step])


@figure("tax-path-a")
def tax_path_a():
    return tax_tree(path=TAX_PATHS["single-no-refund-100k"],
                    caption="Single, no refund, income 100K: Refund = No, then Single, then > 80K, so YES")


@figure("tax-path-b")
def tax_path_b():
    return tax_tree(path=TAX_PATHS["married-no-refund-40k"],
                    caption="Married, no refund, income 40K: Refund = No, then Married, so NO (income never asked)")


@figure("tax-path-ex")
def tax_path_ex():
    return tax_tree(path=TAX_PATHS["single-no-refund-100k"],
                    caption="D. Single, no refund, income 85K: > 80K, so YES")


# ------------------------------------------------- split scoring diagrams

def count_bar(ax, center, counts, *, width=2.2, height=0.42, names=("+", "−"),
              above=True):
    """A node drawn as a stacked bar: orange share = class 1, gray = class 0."""
    pos, neg = counts
    total = pos + neg
    x0 = center[0] - width / 2
    y0 = center[1] - height / 2
    wp = width * pos / total
    ax.add_patch(plt.Rectangle((x0, y0), wp, height, facecolor=ORANGE,
                               edgecolor=PAPER, lw=1.5, zorder=3))
    ax.add_patch(plt.Rectangle((x0 + wp, y0), width - wp, height,
                               facecolor=QUIET, edgecolor=PAPER, lw=1.5, zorder=3))
    ax.add_patch(plt.Rectangle((x0, y0), width, height,
                               fill=False, edgecolor=INK, lw=1.5, zorder=4))
    ax.text(center[0], y0 + height + 0.1 if above else y0 - 0.1,
            f"{pos} {names[0]} / {neg} {names[1]}" if names else f"{pos} / {neg}",
            ha="center",
            va="bottom" if above else "top", fontsize=15, color=INK)


def class_key(ax, pos_name, neg_name, *, x=0.0, y=3.6):
    """One-line key for count bars drawn without class names."""
    ax.text(x, y, f"orange = {pos_name},  gray = {neg_name}", ha="center",
            va="bottom", fontsize=14, color=STEEL)


def split_diagram(ax, root, children, edge_labels, question, notes=None,
                  *, names=("+", "−"), show_children=True, cx=0.0, span=3.4):
    """Root bar, a question, and two child bars underneath.

    Bars have equal widths; the orange share inside each bar is the class mix.
    """
    rx, ry = cx, 3.0
    count_bar(ax, (rx, ry), root, names=names)
    ax.text(rx, ry - 0.35, question, ha="center", va="top", fontsize=16,
            color=INK, fontweight="bold")
    if not show_children:
        return
    for i, (counts, lbl) in enumerate(zip(children, edge_labels)):
        x = cx + (-span / 2 if i == 0 else span / 2)
        ax.plot([rx, x], [ry - 0.8, 1.38], color=INK, lw=2.5, zorder=2)
        ax.text((rx + x) / 2 + (-0.15 if i == 0 else 0.15), 1.85, lbl,
                ha="right" if i == 0 else "left", fontsize=14, color=STEEL)
        count_bar(ax, (x, 1.15), counts, names=names, above=False)
        if notes:
            ax.text(x, 0.5, notes[i], ha="center", va="top", fontsize=15,
                    color=INK, linespacing=1.4)


@steps("majority-vote", 3)
def majority_vote(step):
    """CIML Section 1.3's scoring rule on 20 invented Chicago baseball fans
    (9 Cubs / 11 Sox, split into 7/3 and 2/8, scoring 15/20).

    Cubs take the orange accent; the White Sox take gray, after their black and
    silver.
    """
    fig, ax = new_fig(height=560)
    ax.set_xlim(-4, 4)
    ax.set_ylim(-1.0, 3.7)
    ax.axis("off")
    notes = None
    if step == 2:
        notes = ["guess Cubs:\n7 of 10 correct", "guess Sox:\n8 of 10 correct"]
    split_diagram(ax, (9, 11), [(7, 3), (2, 8)], ["no", "yes"],
                  "Lives south of Madison Street?", notes, names=("Cubs", "Sox"),
                  show_children=step >= 1)
    if step == 2:
        ax.text(0, -0.85, "score = 7 + 8 = 15 / 20", ha="center", fontsize=19,
                color=ORANGE, fontweight="bold")
    return fig


@steps("split-entropy", 4)
def split_entropy(step):
    """The Cubs / Sox split from `majority_vote`, scored with entropy instead:
    parent H, then each child's H, then the information gain. Same canvas and
    limits as `majority_vote`, so the tree sits in the same place.
    """
    fig, ax = new_fig(height=560)
    ax.set_xlim(-4, 4)
    ax.set_ylim(-1.0, 3.7)
    ax.axis("off")
    root, kids = (9, 11), [(7, 3), (2, 8)]
    h_root = H(root[0] / sum(root))
    h_kids = [H(c / (c + s)) for c, s in kids]
    weights = [sum(k) / sum(root) for k in kids]
    gain = h_root - sum(w * h for w, h in zip(weights, h_kids))
    notes = [f"H = {h:.3f}" for h in h_kids] if step >= 2 else None
    split_diagram(ax, root, kids, ["no", "yes"], "Lives south of Madison Street?",
                  notes, names=("Cubs", "Sox"))
    if step >= 1:
        ax.text(1.3, 3.0, f"H = {h_root:.3f}", ha="left", va="center", fontsize=15,
                color=INK)
    if step >= 3:
        ax.text(0, -0.85, f"IG = {h_root:.3f} − ½({h_kids[0]:.3f}) − ½({h_kids[1]:.3f})"
                          f" = {gain:.3f}", ha="center", fontsize=19, color=ORANGE,
                fontweight="bold")
    return fig


@steps("majority-tie", 2)
def majority_tie(step):
    """Zheleva (after Carpuat): two splits, same 400/1200 error, different entropy."""
    fig, ax = new_fig(height=520)
    ax.set_xlim(-8.2, 8.2)
    ax.set_ylim(-1.0, 4.0)
    ax.axis("off")
    class_key(ax, "yes", "no")
    for cx, kids, name, ent in ((-4.1, [(400, 200), (400, 200)], "Feature 1", 0.92),
                                (4.1, [(250, 240), (550, 160)], "Feature 2", 0.86)):
        split_diagram(ax, (800, 400), kids, ["", ""], f"split on {name}",
                      names=None, cx=cx, span=3.6)
        ax.text(cx, 0.15, "error: 400 / 1200", ha="center", fontsize=16, color=INK)
        if step >= 1:
            ax.text(cx, -0.4, f"weighted entropy: {ent:.2f}", ha="center",
                    fontsize=16, color=ORANGE if ent < 0.9 else INK,
                    fontweight="bold" if ent < 0.9 else "normal")
    return fig


def split_quiz_kids(key):
    """(question, [no child, yes child] as (pass, fail), good?) for the 30 study-hours students.

    Hours and birthday split the real synthetic data; the seat and practice-exam counts are invented to sum to the same 20 pass / 10 fail.
    Information gain: hours 0.581, birthday 0.000, seat 0.002, practice exam 0.479.
    """
    hours, _, day, y = study_hours()
    if key == "hours":
        m = hours > 6
        return "Studied more than 6 hours?", [(int(y[~m].sum()), int((1 - y[~m]).sum())), (int(y[m].sum()), int((1 - y[m]).sum()))], True
    if key == "birthday":
        m = day <= 15
        return "Born on or before the 15th?", [(int(y[~m].sum()), int((1 - y[~m]).sum())), (int(y[m].sum()), int((1 - y[m]).sum()))], False
    if key == "seat":
        return "Sits on the left side of the room?", [(11, 5), (9, 5)], False
    return "Took the practice exam?", [(2, 9), (18, 1)], True


def split_quiz(key, step):
    """Is this a good split? The question and children first, then the class mix of each child and a verdict, before any scoring rule."""
    question, kids, good = split_quiz_kids(key)
    fig, ax = new_fig(height=560)
    ax.set_xlim(-4, 4)
    ax.set_ylim(-1.0, 3.7)
    ax.axis("off")
    notes = None
    if step == 1:
        notes = [f"{max(p, f) / (p + f):.0%} {'pass' if p >= f else 'fail'}" for p, f in kids]
    split_diagram(ax, (20, 10), kids, ["no", "yes"], question, notes, names=("pass", "fail"))
    if step == 1:
        verdict = "Good split: each side is mostly one class" if good else "Bad split: each side looks like the whole class (67% pass)"
        ax.text(0, -0.85, verdict, ha="center", fontsize=19, color=ORANGE if good else INK, fontweight="bold")
    return fig


for _key in ("hours", "birthday", "seat", "practice"):
    steps(f"split-quiz-{_key}", 2)(lambda step, key=_key: split_quiz(key, step))


def H(p):
    p = np.asarray(p, float)
    with np.errstate(divide="ignore", invalid="ignore"):
        h = -(p * np.log2(p) + (1 - p) * np.log2(1 - p))
    return np.nan_to_num(h)


@steps("ex12-4", 3)
def ex12_4(step):
    """Bello, Lecture 12, Exercise 12.4: split on X_a or X_b?"""
    fig, ax = new_fig(height=520)
    ax.set_xlim(-8.2, 8.2)
    ax.set_ylim(-1.3, 4.0)
    ax.axis("off")
    class_key(ax, "class 1", "class 0")
    for cx, kids, name, ig in ((-4.1, [(2, 3), (3, 2)], "a", 0.029),
                               (4.1, [(1, 4), (4, 1)], "b", 0.278)):
        notes = None
        if step >= 1:
            notes = [f"H = {H(k[0] / 5):.3f}" for k in kids]
        split_diagram(ax, (5, 5), kids, [f"$X_{name}$ = 0", f"$X_{name}$ = 1"],
                      f"split on $X_{name}$", notes, names=None,
                      cx=cx, span=3.6)
        if step >= 2:
            hot = ig > 0.1
            ax.text(cx, -0.25, f"IG = 1 − ½({H(kids[0][0] / 5):.3f}) "
                    f"− ½({H(kids[1][0] / 5):.3f})\n= {ig:.3f}",
                    ha="center", va="top", fontsize=16, color=ORANGE if hot else INK,
                    fontweight="bold" if hot else "normal", linespacing=1.4)
    return fig


@steps("entropy-curve", 4)
def entropy_curve(step):
    """Information gain read off the entropy curve, after Raschka's FAQ figure:
    the size-weighted average of two children falls on the straight line
    between them, below the curve, and the drop from the parent is the gain.
    Nodes are Bello's Exercise 12.4 (parent 5/5; X_a gives 2/3 and 3/2, X_b
    gives 1/4 and 4/1), so the drops match the Worked Example slide.
    """
    fig, ax = fixed_fig(left=95, right=25, top=20, bottom=70)
    p = np.linspace(0, 1, 401)
    ax.plot(p, H(p), color=INK, lw=3, zorder=2)
    tidy(ax, grid="y")
    ax.set_xlim(-0.02, 1.02)
    ax.set_ylim(0, 1.12)
    ax.set_xlabel("share of the node in class 1")
    ax.set_ylabel("entropy H")
    ax.text(0.02, 0.06, "pure: H = 0", fontsize=15, color=STEEL)
    ax.text(0.98, 0.06, "pure: H = 0", fontsize=15, color=STEEL, ha="right")
    if step == 0:
        ax.text(0.5, 1.04, "50/50: H = 1", fontsize=15, color=STEEL, ha="center")
    else:
        ax.scatter([0.5], [1.0], s=170, color=INK, zorder=6)
        ax.text(0.5, 1.04, "parent: 5 / 5, H = 1", fontsize=15, color=INK, ha="center")
    # (name, child shares, color, bracket x, gap-label xy, text-block y).
    # X_a's gap is too thin to label beside, so its number sits out to the left.
    splits = [("a", (0.4, 0.6), STEEL, 0.47, (0.22, 1.05), 0.50),
              ("b", (0.2, 0.8), ORANGE, 0.53, (0.545, 0.861), 0.30)]
    for name, (lo, hi), col, bx, (gx, gy), ty in splits[:max(step - 1, 0)]:
        avg = (H(lo) + H(hi)) / 2  # equal-size children: weights 5/10 each
        gain = 1 - avg
        ax.plot([lo, hi], [H(lo), H(hi)], color=col, lw=2, ls=(0, (5, 3)), zorder=3)
        ax.scatter([lo, hi], [H(lo), H(hi)], s=130, color=col, zorder=5)
        ax.scatter([0.5], [avg], s=130, facecolor=PAPER, edgecolor=col, lw=2.5, zorder=5)
        ax.text(lo + 0.015, H(lo) - 0.025, f"$X_{name}$", ha="left", va="top",
                fontsize=16, color=col)
        ax.plot([bx, bx], [avg, 1.0], color=col, lw=2.5, zorder=4)
        for yv in (avg, 1.0):
            ax.plot([bx - 0.01, bx + 0.01], [yv, yv], color=col, lw=2.5, zorder=4)
        ax.annotate(f"{gain:.3f}", (bx - 0.012, (avg + 1) / 2), xytext=(gx, gy),
                    ha="left", va="center", fontsize=15, color=col, fontweight="bold",
                    arrowprops=dict(arrowstyle="-", color=col, lw=1.2)
                    if gx < bx else None)
        ax.text(0.5, ty, f"$X_{name}$: children average H = {avg:.3f}\n"
                         f"drop from parent = 1 − {avg:.3f} = {gain:.3f}",
                ha="center", va="center", fontsize=16, color=col, linespacing=1.5)
    return fig


# ------------------------------------------- continuous features: thresholds

@steps("hours-threshold", 3)
def hours_threshold(step):
    """A one-question tree on hours studied: the points, every candidate threshold, then the one scikit-learn's tree picks."""
    hours, jitter, _, y = study_hours()
    fig, (ax, tx) = new_fig(height=560, ncols=2, gridspec_kw={"width_ratios": [2.3, 1], "wspace": 0.08})
    stump = DecisionTreeClassifier(criterion="entropy", max_depth=1).fit(hours[:, None], y)
    cut = stump.tree_.threshold[0]
    below, above = hours <= cut, hours > cut
    pass_fail_rows(ax)
    tx.axis("off")
    tx.set_xlim(0, 4)
    tx.set_ylim(0, 4)
    if step == 0:
        note(ax, f"30 students: passed ({POS_GLYPH}) or failed ({NEG_GLYPH})", size=16)
    if step == 1:
        s = np.sort(hours)
        for m in (s[1:] + s[:-1]) / 2:
            ax.axvline(m, color=QUIET, lw=1, ls=(0, (3, 3)), zorder=1)
        note(ax, "Candidate thresholds: midpoints between sorted hours", size=16)
    if step == 2:
        ax.axvspan(HOURS_XLIM[0], cut, color=NEG_TINT, zorder=0)
        ax.axvspan(cut, HOURS_XLIM[1], color=POS_TINT, zorder=0)
        ax.axvline(cut, color=INK, lw=2, zorder=1)
        note(ax, f"Split at {cut:.2f} hours: all {above.sum()} students above it passed", size=16)
        node_box(tx, (2, 3.1), f"hours ≤ {cut:.2f}", w=2.6, size=15)
        node_box(tx, (1, 1.2), f"fail {NEG_GLYPH}", leaf=True, w=1.5, size=15)
        node_box(tx, (3, 1.2), f"pass {POS_GLYPH}", leaf=True, w=1.5, size=15)
        edge(tx, (2, 3.1), (1, 1.2), "yes", side="left", size=14)
        edge(tx, (2, 3.1), (3, 1.2), "no", side="right", size=14)
        for x, m in ((1, below), (3, above)):
            tx.text(x, 0.55, f"{y[m].sum()} {POS_GLYPH}  {(1 - y[m]).sum()} {NEG_GLYPH}", ha="center", va="top",
                    fontsize=14, color=STEEL)
    points(ax, np.c_[hours, y + jitter], y, size=120)
    return fig


# ----------------------------------------------------- growing a tree

def fit_tree(X, y, depth):
    return DecisionTreeClassifier(criterion="entropy", max_depth=depth,
                                  random_state=0).fit(X, y)


def split_segments(tree, lim):
    """(depth, feature, threshold, bounds) for every internal node of a fitted tree."""
    t = tree.tree_
    out = []

    def walk(node, depth, box):
        f = t.feature[node]
        if f < 0:
            return
        thr = t.threshold[node]
        out.append((depth, f, thr, [list(b) for b in box]))
        left = [list(b) for b in box]
        right = [list(b) for b in box]
        left[f][1] = thr
        right[f][0] = thr
        walk(t.children_left[node], depth + 1, left)
        walk(t.children_right[node], depth + 1, right)

    walk(0, 0, [list(lim[0]), list(lim[1])])
    return out


def draw_tree(ax, tree, newest_depth):
    """Lay out a fitted sklearn tree: leaves evenly spaced, parents centered."""
    t = tree.tree_
    classes = tree.classes_
    pos, leaves = {}, []

    def collect(node, depth):
        if t.feature[node] < 0:
            leaves.append(node)
            pos[node] = (len(leaves) - 1, depth)
            return pos[node][0]
        xs = [collect(t.children_left[node], depth + 1),
              collect(t.children_right[node], depth + 1)]
        pos[node] = (sum(xs) / 2, depth)
        return pos[node][0]

    collect(0, 0)
    n_leaves = max(len(leaves), 1)
    max_d = max(d for _, d in pos.values())
    W = max(n_leaves - 1, 1)
    sx = lambda x: 0.5 if n_leaves == 1 else 0.06 + 0.88 * x / W
    sy = lambda d: 0.9 - 0.75 * d / max(max_d, 3)
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis("off")
    small = n_leaves > 4
    for node, (x, d) in pos.items():
        if t.feature[node] >= 0:
            for child in (t.children_left[node], t.children_right[node]):
                cx, cd = pos[child]
                ax.plot([sx(x), sx(cx)], [sy(d) - 0.04, sy(cd) + 0.04], color=INK,
                        lw=2.5 if cd == newest_depth else 1.5, zorder=1)
    for node, (x, d) in pos.items():
        new = d == newest_depth or (t.feature[node] >= 0 and d == newest_depth - 1)
        counts = t.value[node][0] * t.n_node_samples[node]
        if t.feature[node] >= 0:
            sub = "1" if t.feature[node] == 0 else "2"
            text = f"$x_{sub}$ ≤ {t.threshold[node]:.1f}"
            fill, col = NODE_FILL, INK
        else:
            label = classes[np.argmax(counts)]
            n_pos = int(round(counts[list(classes).index(1)]))
            n_neg = int(round(counts[list(classes).index(-1)]))
            text = f"{POS_GLYPH if label == 1 else NEG_GLYPH}  {n_pos}/{n_neg}"
            fill = POS_TINT if label == 1 else NEG_TINT
            col = INK
        ax.text(sx(x), sy(d), text, ha="center", va="center",
                fontsize=11 if small else 14, color=col, zorder=3,
                bbox=dict(boxstyle="round,pad=0.35", facecolor=fill,
                          edgecolor=INK, linewidth=2.2 if new and d > 0 else 1.2))
    ax.text(0.5, 0.0, f"leaf: predicted class, then # {POS_GLYPH} / # {NEG_GLYPH} training examples",
            ha="center", fontsize=12, color=STEEL)


@steps("tree-grow", 5)
def tree_grow(step):
    X, y, _ = cloud()
    depth = [0, 1, 2, 3, None][step]
    fig, (ax, tx) = new_fig(height=600, ncols=2,
                            gridspec_kw={"width_ratios": [1, 1.15], "wspace": 0.05})
    plain_axes(ax, *CLOUD_LIM)
    if depth == 0:
        majority = 1 if (y == 1).sum() > (y == -1).sum() else -1
        shade(ax, lambda P: np.full(len(P), majority), *CLOUD_LIM)
        points(ax, X, y, size=110)
        acc = (y == majority).mean()
        note(ax, f"Depth 0, the empty tree: predict {NEG_GLYPH} for everything "
                 f"(training accuracy {acc:.0%})", size=15)
        tx.axis("off")
        tx.text(0.5, 0.6, f"{NEG_GLYPH}  {int((y == 1).sum())}/{int((y == -1).sum())}",
                ha="center", va="center", fontsize=18,
                bbox=dict(boxstyle="round,pad=0.5", facecolor=NEG_TINT,
                          edgecolor=INK, linewidth=2))
        tx.text(0.5, 0.42, f"one leaf ({POS_GLYPH} / {NEG_GLYPH} counts)", ha="center",
                fontsize=14, color=STEEL)
        return fig
    tree = fit_tree(X, y, depth)
    shade(ax, tree.predict, *CLOUD_LIM, boundary=False)
    newest = tree.get_depth() - 1
    for d, f, thr, box in split_segments(tree, CLOUD_LIM):
        hot = d == newest and depth is not None
        kw = dict(color=INK, lw=2.6 if hot else 1.3, zorder=2)
        if f == 0:
            ax.plot([thr, thr], box[1], **kw)
        else:
            ax.plot(box[0], [thr, thr], **kw)
    points(ax, X, y, size=110)
    acc = tree.score(X, y)
    if depth is None:
        note(ax, f"Full tree: depth {tree.get_depth()}, {tree.get_n_leaves()} leaves, "
                 f"training accuracy {acc:.0%}", size=15)
        tx.axis("off")
        tx.text(0.5, 0.55, f"{tree.get_n_leaves()} leaves,\none per pocket of\n"
                           "training points\n(too big to draw here)",
                ha="center", va="center", fontsize=17, color=STEEL, linespacing=1.5)
    else:
        note(ax, f"Depth {depth}: training accuracy {acc:.0%}", size=15)
        draw_tree(tx, tree, newest_depth=tree.get_depth())
    return fig


@steps("depth-accuracy", 3)
def depth_accuracy(step):
    """Train vs. held-out accuracy as max_depth grows, averaged over 40 draws."""
    depths = np.arange(0, 16)
    train, test = np.zeros(len(depths)), np.zeros(len(depths))
    reps = 40
    for r in range(reps):
        rng = np.random.default_rng(1000 + r)
        Xtr, ytr = two_class(150, rng, flip=0.1)
        Xte, yte = two_class(1500, rng, flip=0.1)
        for i, d in enumerate(depths):
            if d == 0:
                maj = 1 if (ytr == 1).sum() > (ytr == -1).sum() else -1
                train[i] += (ytr == maj).mean()
                test[i] += (yte == maj).mean()
            else:
                m = fit_tree(Xtr, ytr, int(d))
                train[i] += m.score(Xtr, ytr)
                test[i] += m.score(Xte, yte)
    train /= reps
    test /= reps
    fig, ax = new_fig(height=560)
    tidy(ax, grid="y")
    ax.plot(depths, train, color=STEEL, lw=3, marker="o", ms=6)
    ax.text(depths[-1] + 0.3, train[-1], "training", color=STEEL, fontsize=16,
            va="center")
    if step >= 1:
        ax.plot(depths, test, color=ORANGE, lw=3, marker="o", ms=6)
        ax.text(depths[-1] + 0.3, test[-1], "held-out", color=ORANGE, fontsize=16,
                va="center")
    if step >= 2:
        best = int(depths[np.argmax(test)])
        ax.scatter([best], [test.max()], s=260, facecolor="none", edgecolor=INK,
                   lw=2.2, zorder=5)
        ax.annotate(f"best held-out: depth {best}", (best, test.max()),
                    xytext=(best + 2.2, test.max() + 0.07), fontsize=16, color=INK,
                    arrowprops=dict(arrowstyle="-", color=INK, lw=1.2))
        ax.text(0.4, 0.56, "underfit\n(empty tree)", fontsize=14, color=STEEL)
        ax.text(15, 0.62, "overfit\n(near-full tree)", fontsize=14, color=STEEL,
                ha="right")
    ax.set_xlim(-0.5, 17.8)
    ax.set_ylim(0.5, 1.02)
    ax.set_xticks(depths[::2])
    ax.set_xlabel("max_depth")
    ax.set_ylabel("accuracy")
    ax.yaxis.set_major_formatter(lambda v, _: f"{v:.0%}")
    return fig


# ------------------------------------------- the class survey (running example)

# The worksheet's 12 courses: CS 412 is the label, the other 11 are features.
SURVEY_COURSES = ["CS 100", "CS 251", "CS 301", "CS 361", "CS 401", "CS 411",
                  "CS 424", "CS 426", "CS 427", "CS 480", "CS 488"]
SURVEY_LABEL = "CS 412"


def make_survey(n, seed=418):
    """Synthetic course survey: 1 = took the course. Same draws as `make_survey` in week9.qmd's code demo; keep the two copies in sync."""
    rng = np.random.default_rng(seed)
    senior = rng.random(n) < 0.5   # hidden: further along in the major
    ai_fan = rng.random(n) < 0.45  # hidden: into AI and data
    gamer = rng.random(n) < 0.25   # hidden: into games and art

    def took(p):  # 1 with probability p, else 0
        return (rng.random(n) < p).astype(int)

    survey = {
        "CS 100": took(0.08),
        "CS 251": np.ones(n, int),  # the prerequisite for CS 418
        "CS 301": took(np.where(senior, 0.85, 0.35)),
        "CS 361": took(np.where(senior, 0.8, 0.3)),
        "CS 401": took(np.where(senior, 0.75, 0.15)),
        "CS 411": took(np.where(ai_fan, 0.85, 0.05) * np.where(senior, 1, 0.7)),
        "CS 424": took(np.where(ai_fan, 0.6, 0.1)),
        "CS 426": took(np.where(gamer, 0.6, 0.05)),
        "CS 427": took(np.where(gamer, 0.5, 0.05)),
        "CS 480": took(np.where(senior, 0.5, 0.2)),
        "CS 488": took(0.12),
    }
    survey["CS 412"] = took(np.where(ai_fan, 0.9, 0.03) * np.where(senior, 1, 0.5))
    return survey


def class_survey():
    """20 classmates and Alice: rows 0-19 and row 33 of make_survey(60, seed=18981).

    Seed and row were found by search so every teaching point shows up in the data (see SOURCES.md).
    """
    s = make_survey(60, seed=18981)
    X = np.column_stack([s[c] for c in SURVEY_COURSES])
    y = s[SURVEY_LABEL]
    return X[:20], y[:20], X[33], int(y[33])


def big_survey():
    """The demo's 1,000 students, split 600 / 200 / 200 exactly as in week9.qmd."""
    s = make_survey(1000, seed=418)
    X = np.column_stack([s[c] for c in SURVEY_COURSES]).astype(bool)
    y = s[SURVEY_LABEL]
    X_tr, _, y_tr, _ = train_test_split(X, y, test_size=0.2, random_state=0)  # the test set stays untouched
    X_tr, X_va, y_tr, y_va = train_test_split(X_tr, y_tr, test_size=0.25, random_state=0)
    return X_tr, y_tr, X_va, y_va


ALICE_MONTH_SEED = 0  # birth months for the irrelevant-feature slide


def birth_months():
    months = np.random.default_rng(ALICE_MONTH_SEED).integers(1, 13, 21)
    return months[:20], int(months[20])


def pair_counts(Xc, a):
    """N11, N10, N01, N00 between Alice (a) and each classmate, as in Bello's notation."""
    n11 = ((a == 1) & (Xc == 1)).sum(1)
    n10 = ((a == 1) & (Xc == 0)).sum(1)
    n01 = ((a == 0) & (Xc == 1)).sum(1)
    n00 = ((a == 0) & (Xc == 0)).sum(1)
    return n11, n10, n01, n00


def jaccard_smc(Xc, a):
    n11, n10, n01, n00 = pair_counts(Xc, a)
    return n11 / (n11 + n10 + n01), (n11 + n00) / Xc.shape[1]


def top_ylabel(ax, text):
    """STYLE.md: horizontal y-axis label, left-aligned above the axis."""
    ax.set_ylabel(text, rotation=0, ha="left", va="bottom", color=STEEL, fontsize=15)
    ax.yaxis.set_label_coords(0, 1.025)


def cell(ax, xy, on, *, size=0.8, on_color=STEEL, edge=BORDER, lw=1.0, zorder=3):
    """One survey answer: a filled square for 1, an empty one for 0."""
    ax.add_patch(plt.Rectangle((xy[0] - size / 2, xy[1] - size / 2), size, size,
                               facecolor=on_color if on else PAPER,
                               edgecolor=on_color if on else edge, lw=lw, zorder=zorder))


@steps("survey-grid", 3)
def survey_grid(step):
    """The whole class survey, laid out like worksheet checkpoint 1: courses as rows, students as columns."""
    Xc, yc, a, _ = class_survey()
    fig, ax = new_fig(height=600)
    ax.set_xlim(-3.4, 22.8)
    ax.set_ylim(-13.0, 2.0)
    ax.set_aspect("equal")
    ax.axis("off")
    label_y = -11.9
    for i, course in enumerate(SURVEY_COURSES + [SURVEY_LABEL]):
        y = -i if i < len(SURVEY_COURSES) else label_y
        hot = course == SURVEY_LABEL and step >= 1
        ax.text(-0.7, y, course, ha="right", va="center", fontsize=13,
                color=ORANGE if hot else INK, fontweight="bold" if hot else "normal")
    if step >= 1:
        ax.text(-0.7, label_y - 0.85, "(label)", ha="right", va="center", fontsize=12, color=ORANGE)
        ax.plot([-3.2, 22.6], [(label_y - 10) / 2] * 2, color=QUIET, lw=1, ls=(0, (4, 3)))
    for j in range(20):
        ax.text(j, 1.0, str(j + 1), ha="center", va="center", fontsize=11, color=STEEL)
        for i in range(len(SURVEY_COURSES)):
            cell(ax, (j, -i), Xc[j, i])
        if step == 0:
            cell(ax, (j, label_y), yc[j])
        else:
            points(ax, [(j, label_y)], [yc[j]], size=110)
    ax.text(9.5, 1.85, "classmate", ha="center", va="center", fontsize=12, color=STEEL)
    if step >= 2:
        ax.text(21.2, 1.0, "Alice", ha="center", va="center", fontsize=13, color=INK, fontweight="bold")
        ax.add_patch(plt.Rectangle((20.5, label_y - 0.65), 1.4, -label_y + 0.65 + 0.55, fill=False, edgecolor=INK, lw=2, zorder=5))
        for i in range(len(SURVEY_COURSES)):
            cell(ax, (21.2, -i), a[i])
        query(ax, (21.2, label_y), size=300)
    return fig


ALICE_PAIR = 4  # classmate #5: Alice's nearest neighbor by Jaccard


@steps("survey-pair", 3)
def survey_pair(step):
    """Alice next to classmate #5, one column per course: disagreements, then the four N counts."""
    Xc, _, a, _ = class_survey()
    b = Xc[ALICE_PAIR]
    fig, ax = new_fig(height=380)
    ax.set_xlim(-2.6, 11.0)
    ax.set_ylim(-3.3, 2.1)
    ax.set_aspect("equal")
    ax.axis("off")
    for i, course in enumerate(SURVEY_COURSES):
        ax.text(i, 1.65, course.split()[1], ha="center", va="center", fontsize=13, color=STEEL)
    ax.text(-0.75, 1.65, "CS", ha="right", va="center", fontsize=13, color=STEEL)
    for row, (name, v) in enumerate((("Alice", a), (f"#{ALICE_PAIR + 1}", b))):
        ax.text(-0.75, 0.7 - row, name, ha="right", va="center", fontsize=15, color=INK)
        for i in range(len(SURVEY_COURSES)):
            cell(ax, (i, 0.7 - row), v[i])
    diff = a != b
    if step == 1:
        for i in np.flatnonzero(diff):
            ax.add_patch(plt.Rectangle((i - 0.5, -0.8), 1.0, 2.0, fill=False, edgecolor=ORANGE, lw=3, zorder=5))
        d = int(diff.sum())
        ax.text(5, -1.45, f"{d} courses differ", ha="center", va="center", fontsize=17, color=ORANGE, fontweight="bold")
        ax.text(5, -2.35, f"Manhattan = {d}      Euclidean = √{d} ≈ {d ** 0.5:.2f}", ha="center", va="center", fontsize=17, color=INK)
    if step == 2:
        kinds = {(1, 1): "$N_{11}$", (1, 0): "$N_{10}$", (0, 1): "$N_{01}$", (0, 0): "$N_{00}$"}
        for i in range(len(SURVEY_COURSES)):
            k = (int(a[i]), int(b[i]))
            ax.text(i, -1.2, kinds[k], ha="center", va="center", fontsize=13,
                    color=ORANGE if k == (1, 1) else (QUIET if k == (0, 0) else INK))
        n11, n10, n01, n00 = (int(v[ALICE_PAIR]) for v in pair_counts(Xc, a))
        ax.text(5, -2.0, f"$N_{{11}}$ = {n11}    $N_{{10}}$ = {n10}    $N_{{01}}$ = {n01}    $N_{{00}}$ = {n00}",
                ha="center", va="center", fontsize=16, color=INK)
        ax.text(5, -2.85, f"Jaccard = {n11}/{n11 + n10 + n01} ≈ {n11 / (n11 + n10 + n01):.3f}      "
                          f"SMC = {n11 + n00}/11 ≈ {(n11 + n00) / 11:.3f}",
                ha="center", va="center", fontsize=16, color=ORANGE, fontweight="bold")
    return fig


def ranked_bars(ax, values, title, *, top_color=ORANGE, fmt="{:.3f}", xmax=1.0):
    """Every classmate as a bar, sorted high to low; ties keep classmate order."""
    order = np.argsort(-values, kind="stable")
    best = values[order[0]]
    for r, j in enumerate(order):
        hot = values[j] == best
        ax.barh(-r, values[j], height=0.72, color=top_color if hot else QUIET, zorder=2)
        ax.text(-0.01 * xmax, -r, f"#{j + 1}", ha="right", va="center", fontsize=11,
                color=INK if hot else STEEL, fontweight="bold" if hot else "normal")
        ax.text(values[j] + 0.01 * xmax, -r, fmt.format(values[j]), ha="left", va="center",
                fontsize=10, color=INK if hot else STEEL)
    ax.set_xlim(0, xmax * 1.12)
    ax.set_ylim(-len(values) + 0.4, 0.8)
    ax.axis("off")
    ax.text(0, 1.3, title, ha="left", va="bottom", fontsize=15, color=INK)
    return order


@steps("survey-neighbors", 2)
def survey_neighbors(step):
    """All 20 classmates ranked by Jaccard, then by SMC: the nearest neighbor changes."""
    Xc, _, a, _ = class_survey()
    jac, smc = jaccard_smc(Xc, a)
    fig, (lx, rx) = new_fig(height=600, ncols=2, gridspec_kw={"wspace": 0.25})
    ranked_bars(lx, jac, "Jaccard: only shared 1s count")
    if step >= 1:
        ranked_bars(rx, smc, "SMC: shared 0s count too")
    else:
        rx.axis("off")
    return fig


KNN_SHOW = 7  # the 7 most similar classmates (5th through 7th tie)


@steps("survey-knn", 4)
def survey_knn(step):
    """k-NN for Alice: classmates ranked by Jaccard similarity, each with their CS 412 answer."""
    Xc, yc, a, ya = class_survey()
    jac, _ = jaccard_smc(Xc, a)
    order = np.argsort(-jac, kind="stable")[:KNN_SHOW]
    fig, (ax, tx) = new_fig(height=520, ncols=2, gridspec_kw={"width_ratios": [1.25, 1], "wspace": 0.05})
    for r, j in enumerate(order):
        ax.barh(-r, jac[j], height=0.66, color=QUIET, zorder=2)
        ax.text(-0.02, -r, f"#{j + 1}", ha="right", va="center", fontsize=14, color=INK)
        ax.text(jac[j] + 0.015, -r, f"{jac[j]:.3f}", ha="left", va="center", fontsize=12, color=STEEL)
        points(ax, [(0.78, -r)], [yc[j]], size=150)
    ax.text(0, 0.9, "Jaccard similarity", ha="left", va="bottom", fontsize=14, color=STEEL)
    ax.text(0.78, 0.9, "took 412?", ha="center", va="bottom", fontsize=14, color=STEEL)
    ax.set_xlim(-0.12, 1.05)
    ax.set_ylim(-KNN_SHOW + 0.3, 1.6)
    ax.axis("off")
    tx.axis("off")
    tx.set_xlim(0, 1)
    tx.set_ylim(0, 1)
    rows = [(1, 0.78), (3, 0.5)]
    for k, ty in rows[:min(step, 2)]:
        votes = yc[order[:k]]
        n_pos, n_neg = int(votes.sum()), int(k - votes.sum())
        pred = 1 if n_pos > n_neg else 0
        ax.add_patch(plt.Rectangle((-0.11, -k + 0.5), 0.99, k, fill=False, edgecolor=INK, lw=2,
                                   ls="-" if k == 1 else (0, (5, 3)), zorder=5))
        ax.text(0.9, -k + 0.55, f"k = {k}", ha="left", va="bottom", fontsize=14, color=INK)
        tx.text(0.02, ty, f"k = {k}:  {n_pos} {POS_GLYPH}  vs.  {n_neg} {NEG_GLYPH}", fontsize=18, color=INK, va="center")
        tx.text(0.02, ty - 0.09, f"predict {POS_GLYPH if pred else NEG_GLYPH}", fontsize=18,
                color=ORANGE if pred else STEEL, va="center", fontweight="bold")
        if step >= 3:
            ok = pred == ya
            tx.text(0.62, ty - 0.09, "right" if ok else "wrong", fontsize=17, va="center",
                    color=INK if ok else ORANGE)
    if step >= 3:
        tx.text(0.02, 0.2, f"Alice's real answer: {POS_GLYPH if ya else NEG_GLYPH}\n"
                           f"(she did not take CS 412)", fontsize=16, color=INK, va="center", linespacing=1.5)
    return fig


@steps("survey-month", 2)
def survey_month(step):
    """Add an irrelevant, large-scale feature (birth month) and Manhattan distance picks a new nearest neighbor."""
    Xc, _, a, _ = class_survey()
    months, alice_month = birth_months()
    courses = (Xc != a).sum(1)
    gap = np.abs(months - alice_month)
    total = courses + (gap if step >= 1 else 0)
    order = np.argsort(courses, kind="stable")
    best = total.min()
    fig, ax = new_fig(height=600)
    for r, j in enumerate(order):
        hot = total[j] == best
        ax.barh(-r, courses[j], height=0.72, color=INK if hot else QUIET, zorder=2)
        if step >= 1:
            ax.barh(-r, gap[j], left=courses[j], height=0.72, color=ORANGE, alpha=1.0 if hot else 0.45, zorder=2)
        ax.text(-0.15, -r, f"#{j + 1}", ha="right", va="center", fontsize=11,
                color=INK if hot else STEEL, fontweight="bold" if hot else "normal")
        label = f"{courses[j]}" if step == 0 else f"{courses[j]} + {gap[j]} = {total[j]}   (month {months[j]})"
        ax.text(total[j] + 0.15, -r, label, ha="left", va="center", fontsize=10, color=INK if hot else STEEL)
    ax.set_xlim(0, 17)
    ax.set_ylim(-19.6, 1.6)
    ax.axis("off")
    if step == 0:
        ax.text(0, 1.0, "Manhattan distance to Alice = number of courses that differ", fontsize=15, color=INK)
    else:
        ax.text(0, 1.0, f"Add birth month (Alice: {alice_month}): distance = courses that differ + |month gap|",
                fontsize=15, color=INK)
    return fig


@steps("survey-choose-k", 3)
def survey_choose_k(step):
    """Validation accuracy against k on the demo's 1,000 students (600 training, 200 validation)."""
    X_tr, y_tr, X_va, y_va = big_survey()
    ks = np.array([1, 3, 5, 7, 9, 11, 15, 21, 31, 41, 51, 75, 101, 151, 201, 301, 451, 599])
    acc = np.array([KNeighborsClassifier(n_neighbors=int(k), metric="jaccard").fit(X_tr, y_tr).score(X_va, y_va)
                    for k in ks])
    majority = max(y_va.mean(), 1 - y_va.mean())
    fig, ax = new_fig(height=540)
    tidy(ax, grid="y")
    ax.plot(ks, acc, color=ORANGE, lw=3, marker="o", ms=6, zorder=3)
    if step >= 1:
        ax.axhline(majority, color=STEEL, lw=1.5, ls=(0, (5, 3)), zorder=2)
        ax.text(ks[-1], majority - 0.008, f"always guess {NEG_GLYPH}: {majority:.0%}", ha="right", va="top",
                fontsize=14, color=STEEL)
    if step >= 2:
        b = int(np.argmax(acc))
        ax.scatter([ks[b]], [acc[b]], s=260, facecolor="none", edgecolor=INK, lw=2.2, zorder=5)
        ax.annotate(f"best: k = {ks[b]} ({acc[b]:.0%})", (ks[b], acc[b]), xytext=(ks[b] * 2.2, acc[b] + 0.03),
                    fontsize=15, color=INK, arrowprops=dict(arrowstyle="-", color=INK, lw=1.2))
        ax.text(1, acc[0] - 0.03, "small k:\noverfit", fontsize=14, color=STEEL, va="top")
        ax.text(599, acc[-1] + 0.03, "k ≈ N:\nunderfit", fontsize=14, color=STEEL, ha="right", va="bottom")
    ax.set_xscale("log")
    ax.set_xticks([1, 3, 10, 30, 100, 300, 599])
    ax.set_xticklabels(["1", "3", "10", "30", "100", "300", "599"])
    ax.set_ylim(0.6, 0.95)
    ax.set_xlabel("k (number of neighbors, log scale)")
    top_ylabel(ax, "validation accuracy")
    ax.yaxis.set_major_formatter(lambda v, _: f"{v:.0%}")
    return fig


def survey_splits():
    """(course, majority-vote score, information gain, children) for every course at the root."""
    Xc, yc, _, _ = class_survey()
    out = []
    for i, course in enumerate(SURVEY_COURSES):
        kids = [(int(yc[Xc[:, i] == v].sum()), int((1 - yc[Xc[:, i] == v]).sum())) for v in (0, 1)]
        if min(sum(k) for k in kids) == 0:
            out.append((course, None, None, kids))
            continue
        score = sum(max(k) for k in kids)
        h_root = H(yc.mean())
        ig = h_root - sum(sum(k) / len(yc) * H(k[0] / sum(k)) for k in kids)
        out.append((course, score, float(ig), kids))
    return out


@steps("survey-split-scores", 2)
def survey_split_scores(step):
    """Every course as a candidate root question: majority-vote score, then information gain."""
    rows = [r for r in survey_splits() if r[1] is not None]
    rows.sort(key=lambda r: -r[2])
    best_score = max(r[1] for r in rows)
    best_ig = rows[0][2]
    fig, (lx, rx) = new_fig(height=560, ncols=2, gridspec_kw={"wspace": 0.35})
    n = len(rows)
    for r, (course, score, ig, _) in enumerate(rows):
        tie = score == best_score
        lx.plot([12, score], [-r, -r], color=BORDER, lw=2, zorder=1)
        lx.scatter([score], [-r], s=150, color=INK if tie else QUIET, zorder=3)
        lx.text(11.6, -r, course, ha="right", va="center", fontsize=13, color=INK if tie else STEEL,
                fontweight="bold" if tie else "normal")
        lx.text(score + 0.3, -r, f"{score}/20", ha="left", va="center", fontsize=11, color=STEEL)
        if step >= 1:
            hot = ig == best_ig
            rx.barh(-r, ig, height=0.66, color=ORANGE if hot else QUIET, zorder=2)
            rx.text(-0.01, -r, course, ha="right", va="center", fontsize=13, color=INK if hot else STEEL,
                    fontweight="bold" if hot else "normal")
            rx.text(ig + 0.01, -r, f"{ig:.3f}", ha="left", va="center", fontsize=11, color=STEEL)
    lx.plot([14, 14], [-n + 0.4, 0.6], color=STEEL, lw=1.2, ls=(0, (5, 3)), zorder=0)
    lx.text(14, -n + 0.1, f"no question: guess {NEG_GLYPH} for all = 14/20", ha="center", va="top", fontsize=11, color=STEEL)
    lx.set_xlim(12, 20.5)
    lx.set_ylim(-n - 0.6, 1.9)
    lx.axis("off")
    lx.text(12, 1.6, "majority vote: correct out of 20", ha="left", va="bottom", fontsize=14, color=INK)
    rx.set_xlim(0, 0.68)
    rx.set_ylim(-n - 0.6, 1.9)
    rx.axis("off")
    if step >= 1:
        rx.text(0, 1.6, "information gain", ha="left", va="bottom", fontsize=14, color=INK)
    fig.text(0.5, 0.01, "CS 251 left out: all 20 classmates took it (the prerequisite), so it splits no one",
             ha="center", fontsize=12, color=STEEL)
    return fig


SURVEY_NAMES = (POS_GLYPH, NEG_GLYPH)


def survey_kids(course):
    return next(r[3] for r in survey_splits() if r[0] == course)


@steps("survey-majority", 3)
def survey_majority(step):
    """CIML §1.3's majority-vote score for the best survey question, "Took CS 424?"."""
    fig, ax = new_fig(height=560)
    ax.set_xlim(-4, 4)
    ax.set_ylim(-1.0, 3.7)
    ax.axis("off")
    kids = survey_kids("CS 424")
    notes = None
    if step == 2:
        notes = [f"guess {NEG_GLYPH}:\n{kids[0][1]} of {sum(kids[0])} correct",
                 f"guess {POS_GLYPH}:\n{kids[1][0]} of {sum(kids[1])} correct"]
    split_diagram(ax, (6, 14), kids, ["no", "yes"], "Took CS 424?", notes, names=SURVEY_NAMES,
                  show_children=step >= 1)
    if step == 2:
        ax.text(0, -0.85, f"score = {kids[0][1]} + {kids[1][0]} = {kids[0][1] + kids[1][0]} / 20", ha="center",
                fontsize=19, color=ORANGE, fontweight="bold")
    return fig


def weighted_entropy(kids):
    """Size-weighted child entropy from the 3-decimal child values the slides print, so the arithmetic checks by hand."""
    n = sum(sum(k) for k in kids)
    return sum(sum(k) / n * round(float(H(k[0] / sum(k))), 3) for k in kids)


@steps("survey-tie", 2)
def survey_tie(step):
    """CS 424 and CS 411 both score 18/20 by majority vote; weighted entropy separates them."""
    fig, ax = new_fig(height=520)
    ax.set_xlim(-8.2, 8.2)
    ax.set_ylim(-1.0, 4.0)
    ax.axis("off")
    pair = [(-4.1, "CS 424"), (4.1, "CS 411")]
    ents = {c: weighted_entropy(survey_kids(c)) for _, c in pair}
    for cx, course in pair:
        kids = survey_kids(course)
        split_diagram(ax, (6, 14), kids, ["no", "yes"], f"Took {course}?", names=SURVEY_NAMES, cx=cx, span=3.6)
        wrong = min(kids[0]) + min(kids[1])
        ax.text(cx, 0.15, f"wrong: {wrong} / 20", ha="center", fontsize=16, color=INK)
        if step >= 1:
            hot = ents[course] == min(ents.values())
            ax.text(cx, -0.4, f"weighted entropy: {ents[course]:.3f}", ha="center", fontsize=16,
                    color=ORANGE if hot else INK, fontweight="bold" if hot else "normal")
    return fig


@steps("survey-split-entropy", 4)
def survey_split_entropy(step):
    """The "Took CS 424?" split scored with entropy: parent H, each child's H, then the information gain."""
    fig, ax = new_fig(height=560)
    ax.set_xlim(-4, 4)
    ax.set_ylim(-1.0, 3.7)
    ax.axis("off")
    root, kids = (6, 14), survey_kids("CS 424")
    h_root = H(root[0] / sum(root))
    h_kids = [H(p / (p + q)) for p, q in kids]
    n = [p + q for p, q in kids]
    gain = h_root - sum(k / 20 * h for k, h in zip(n, h_kids))
    notes = [f"H = {h:.3f}" for h in h_kids] if step >= 2 else None
    split_diagram(ax, root, kids, ["no", "yes"], "Took CS 424?", notes, names=SURVEY_NAMES)
    if step >= 1:
        ax.text(1.3, 3.0, f"H = {h_root:.3f}", ha="left", va="center", fontsize=15, color=INK)
    if step >= 3:
        ax.text(0, -0.85, f"IG = {h_root:.3f} − ({n[0]}/20)({h_kids[0]:.3f}) − ({n[1]}/20)({h_kids[1]:.3f})"
                          f" = {gain:.3f}", ha="center", fontsize=19, color=ORANGE, fontweight="bold")
    return fig


@steps("survey-entropy-curve", 4)
def survey_entropy_curve(step):
    """Information gain read off the entropy curve (after Raschka's FAQ figure) for the two tied survey questions.

    The size-weighted average of the children's shares is the parent's share, so each split's average
    entropy sits on its chord directly below the parent; the drop is the gain.
    """
    fig, ax = fixed_fig(left=95, right=330, top=40, bottom=70)
    p = np.linspace(0, 1, 401)
    ax.plot(p, H(p), color=INK, lw=3, zorder=2)
    tidy(ax, grid="y")
    ax.set_xlim(-0.02, 1.02)
    ax.set_ylim(0, 1.12)
    ax.set_xlabel(f"share of the node that took CS 412 ({POS_GLYPH})")
    top_ylabel(ax, "entropy H")
    ax.text(0.02, 0.06, "pure: H = 0", fontsize=15, color=STEEL)
    ax.text(0.98, 0.06, "pure: H = 0", fontsize=15, color=STEEL, ha="right")
    root = 6 / 20
    if step == 0:
        ax.text(0.5, 1.04, "50/50: H = 1", fontsize=15, color=STEEL, ha="center")
        return fig
    ax.scatter([root], [H(root)], s=170, color=INK, zorder=6)
    ax.annotate(f"parent: 6 {POS_GLYPH} / 14 {NEG_GLYPH}\nH = {H(root):.3f}", (root, H(root)), xytext=(0.02, 1.0),
                fontsize=14, color=INK, ha="left", va="center", linespacing=1.4,
                arrowprops=dict(arrowstyle="-", color=INK, lw=1.2, shrinkB=8))
    # (course, color, bracket x, text-block xy)
    splits = [("CS 411", STEEL, 0.285, (1.05, 0.75)), ("CS 424", ORANGE, 0.315, (1.05, 0.45))]
    for course, col, bx, (tx, ty) in splits[:step - 1]:
        kids = survey_kids(course)
        shares = [k[0] / sum(k) for k in kids]
        avg = weighted_entropy(kids)
        gain = H(root) - avg
        ax.plot(shares, [H(s) for s in shares], color=col, lw=2, ls=(0, (5, 3)), zorder=3)
        ax.scatter(shares, [H(s) for s in shares], s=130, color=col, zorder=5)
        ax.scatter([root], [avg], s=130, facecolor=PAPER, edgecolor=col, lw=2.5, zorder=5)
        ax.plot([bx, bx], [avg, H(root)], color=col, lw=2.5, zorder=4)
        for yv in (avg, H(root)):
            ax.plot([bx - 0.01, bx + 0.01], [yv, yv], color=col, lw=2.5, zorder=4)
        ax.text(tx, ty, f"Took {course}?\nchildren average H = {avg:.3f}\n"
                        f"gain = {H(root):.3f} − {avg:.3f} = {gain:.3f}",
                ha="left", va="center", fontsize=14, color=col, linespacing=1.5, transform=ax.get_yaxis_transform(),
                clip_on=False)
    return fig


def survey_tree():
    Xc, yc, _, _ = class_survey()
    return DecisionTreeClassifier(criterion="entropy", random_state=0).fit(Xc, yc)


def draw_course_tree(ax, tree, *, max_depth=None, path=(), note_text=None):
    """Draw the survey tree with course questions. Node positions come from the full tree, so a
    depth-limited version keeps every node in place and only turns the deepest nodes into leaves."""
    Xc, yc, _, _ = class_survey()
    t = tree.tree_
    visits = tree.decision_path(Xc).toarray().astype(bool)
    n_pos = (visits & (yc[:, None] == 1)).sum(0)
    n_neg = (visits & (yc[:, None] == 0)).sum(0)
    pos, leaves = {}, []

    def walk(node, depth):
        if t.feature[node] < 0:
            pos[node] = (len(leaves), depth)
            leaves.append(node)
            return pos[node][0]
        xs = [walk(t.children_left[node], depth + 1), walk(t.children_right[node], depth + 1)]
        pos[node] = (sum(xs) / 2, depth)
        return pos[node][0]

    walk(0, 0)
    sx, sy = 2.9, 1.3
    xy = {n: (x * sx, -d * sy) for n, (x, d) in pos.items()}
    deep = max(d for _, d in pos.values())
    limit = deep if max_depth is None else max_depth
    shown = {n for n, (_, d) in pos.items() if d <= limit}
    internal = {n for n in shown if t.feature[n] >= 0 and pos[n][1] < limit}
    on_path = set(zip(path, path[1:]))
    for n in internal:
        for child, lbl, side in ((t.children_left[n], "no", "left"), (t.children_right[n], "yes", "right")):
            hot = (n, child) in on_path
            edge(ax, xy[n], xy[child], lbl, side=side, color=ORANGE if hot else INK, lw=5 if hot else 3)
    for n in shown:
        on = n in path
        if n in internal:
            node_box(ax, xy[n], f"Took {SURVEY_COURSES[t.feature[n]]}?", size=15,
                     edge=ORANGE if on else INK, lw=5 if on else 3)
        else:
            pred = 1 if n_pos[n] > n_neg[n] else 0
            node_box(ax, xy[n], f"{n_pos[n]} {POS_GLYPH} / {n_neg[n]} {NEG_GLYPH}", leaf=True, size=15,
                     fill=POS_TINT if pred else NEG_TINT, edge=ORANGE if on else INK, lw=5 if on else 3, w=2.5)
    ax.set_xlim(-1.6, (max(x for x, _ in pos.values())) * sx + 1.6)
    ax.set_ylim(-deep * sy - 0.9, 0.9)
    ax.axis("off")
    ax.text(ax.get_xlim()[0], -deep * sy - 0.75,
            f"leaf color = prediction: orange {POS_GLYPH} took CS 412, gray {NEG_GLYPH} did not (a tie goes to {NEG_GLYPH})",
            fontsize=13, color=STEEL, va="center")
    if note_text:
        ax.text(ax.get_xlim()[0], 0.75, note_text, fontsize=16, color=INK, va="center")


@steps("survey-tree-grow", 4)
def survey_tree_grow(step):
    """Greedy growth on the 20 classmates: depth 0, 1, 2, then the full tree."""
    Xc, yc, _, _ = class_survey()
    tree = survey_tree()
    depth = [0, 1, 2, None][step]
    if depth == 0:
        acc = max(yc.mean(), 1 - yc.mean())
    else:
        acc = DecisionTreeClassifier(criterion="entropy", max_depth=depth, random_state=0).fit(Xc, yc).score(Xc, yc)
    label = "full tree" if depth is None else f"depth {depth}"
    fig, ax = new_fig(height=600)
    draw_course_tree(ax, tree, max_depth=depth, note_text=f"{label}: training accuracy {acc:.0%}")
    return fig


@figure("survey-tree-path")
def survey_tree_path():
    """Alice walks the full tree from the root: one question, then a leaf."""
    _, _, a, _ = class_survey()
    tree = survey_tree()
    path = list(np.flatnonzero(tree.decision_path(a.reshape(1, -1)).toarray()[0]))
    pred = int(tree.predict(a.reshape(1, -1))[0])
    fig, ax = new_fig(height=600)
    draw_course_tree(ax, tree, path=path,
                     note_text=f"Alice: took CS 424? no  →  predict {POS_GLYPH if pred else NEG_GLYPH}")
    return fig


@steps("survey-depth-accuracy", 3)
def survey_depth_accuracy(step):
    """Training vs. validation accuracy against max_depth on the demo's 1,000 students."""
    X_tr, y_tr, X_va, y_va = big_survey()
    depths = np.arange(0, 11)
    train, val = [], []
    for d in depths:
        if d == 0:
            maj = int(y_tr.mean() > 0.5)
            train.append((y_tr == maj).mean())
            val.append((y_va == maj).mean())
        else:
            m = DecisionTreeClassifier(criterion="entropy", max_depth=int(d), random_state=0).fit(X_tr, y_tr)
            train.append(m.score(X_tr, y_tr))
            val.append(m.score(X_va, y_va))
    fig, ax = new_fig(height=540)
    tidy(ax, grid="y")
    ax.plot(depths, train, color=STEEL, lw=3, marker="o", ms=6)
    ax.text(depths[-1] + 0.25, train[-1], "training", color=STEEL, fontsize=16, va="center")
    if step >= 1:
        ax.plot(depths, val, color=ORANGE, lw=3, marker="o", ms=6)
        ax.text(depths[-1] + 0.25, val[-1], "validation", color=ORANGE, fontsize=16, va="center")
    if step >= 2:
        best = int(depths[int(np.argmax(val))])
        ax.scatter([best], [max(val)], s=260, facecolor="none", edgecolor=INK, lw=2.2, zorder=5)
        ax.annotate(f"best validation: depth {best}", (best, max(val)), xytext=(best + 1.5, max(val) + 0.05),
                    fontsize=16, color=INK, arrowprops=dict(arrowstyle="-", color=INK, lw=1.2))
        ax.text(0, 0.66, "underfit\n(empty tree)", fontsize=14, color=STEEL)
        ax.text(10, 0.66, "overfit\n(deep tree)", fontsize=14, color=STEEL, ha="right")
    ax.set_xlim(-0.4, 12.2)
    ax.set_ylim(0.65, 0.95)
    ax.set_xticks(depths)
    ax.set_xlabel("max_depth")
    top_ylabel(ax, "accuracy")
    ax.yaxis.set_major_formatter(lambda v, _: f"{v:.0%}")
    return fig


def main(argv: list[str]) -> None:
    if FONT_PATH.exists():
        font_manager.fontManager.addfont(str(FONT_PATH))
        family = font_manager.FontProperties(fname=str(FONT_PATH)).get_name()
        # DejaVu Sans (bundled with matplotlib) supplies the class glyphs.
        plt.rcParams["font.family"] = [family, "DejaVu Sans"]
        # Subscripts ($x_1$) come from mathtext; draw them in the same face.
        plt.rcParams["mathtext.fontset"] = "custom"
        for slot in ("rm", "it", "bf"):
            plt.rcParams[f"mathtext.{slot}"] = family
        # ...and fall back to STIX Sans for the class glyphs inside mathtext.
        plt.rcParams["mathtext.fallback"] = "stixsans"
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
