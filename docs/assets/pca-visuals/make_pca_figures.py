#!/usr/bin/env python3
"""Principal component analysis figures, on the Palmer Penguins.

NOTICE: this file was substantially drafted by an LLM coding system and has not
yet been reviewed. Check every figure against the slide it illustrates.

Follows docs/assets/STYLE.md and the clustering-visuals generator: grayscale
neutrals, vendored Libre Franklin drawn as paths, numbered step sets.

Orange marks the first principal component, the direction PCA is looking for;
the second component is ink. Species, when shown, use the Week 9 / clustering
convention: Chinstrap orange triangle, Adélie steel circle, Gentoo ink square.

Canvases: SPLIT (900 x 700) for the right column of a `.golden-figure` split
slide. Step sets are saved uncropped so frames line up.

Data: `datasets/classification-examples/penguins.csv`, the 342 penguins with
all four measurements, each standardized (mean 0, SD 1) before PCA.
The `pca-cf-*` figures use `datasets/mlb-center-fielders-2026/center-fielders.csv`
instead: 40 MLB center fielders, 11 stats each, standardized; Pete Crow-Armstrong
is the orange point. See SOURCES.md in this folder.

Usage:  python3 make_pca_figures.py [name ...]
"""

from __future__ import annotations

import sys
from pathlib import Path

import matplotlib

matplotlib.use("Agg")

import matplotlib.pyplot as plt
import numpy as np
import polars as pl
from matplotlib import font_manager
from sklearn.decomposition import PCA

OUT_DIR = Path(__file__).resolve().parent
REPO_ROOT = OUT_DIR.parents[2]
FONT_PATH = OUT_DIR.parent / "fonts" / "libre-franklin" / "LibreFranklin-Regular.ttf"
PENGUIN_CSV = REPO_ROOT / "datasets" / "classification-examples" / "penguins.csv"

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

SPECIES_STYLE = {"Adelie": ("o", STEEL, "Adélie"),
                 "Chinstrap": ("^", ORANGE, "Chinstrap"),
                 "Gentoo": ("s", INK, "Gentoo")}
SPECIES_ORDER = ["Adelie", "Chinstrap", "Gentoo"]
FEATURES = ["bill_length_mm", "bill_depth_mm", "flipper_length_mm", "body_mass_g"]
FEATURE_NAMES = ["Bill length", "Bill depth", "Flipper length", "Body mass"]

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


def fixed_fig(size, left, right, top, bottom):
    width, height = size
    fig = plt.figure(figsize=(width / DPI, height / DPI), dpi=DPI)
    fig.patch.set_facecolor(PAPER)
    ax = fig.add_axes([left / width, bottom / height,
                       (width - left - right) / width, (height - top - bottom) / height])
    ax.set_facecolor(PAPER)
    return fig, ax


def tidy(ax, *, grid="both", spines=("left", "bottom")):
    for side in ("top", "right", "left", "bottom"):
        ax.spines[side].set_visible(side in spines)
        ax.spines[side].set_color(BORDER)
    if grid:
        ax.grid(axis=grid, color=BORDER, linewidth=0.8, alpha=0.7)
    ax.set_axisbelow(True)
    ax.tick_params(colors=STEEL, labelsize=13, length=0)
    ax.xaxis.label.set_color(STEEL)
    ax.xaxis.label.set_fontsize(15)
    return ax


def ylabel_top(ax, text):
    """STYLE.md: horizontal y-label, left-aligned above the axis."""
    ax.set_ylabel(text, rotation=0, ha="left", va="bottom", color=STEEL, fontsize=15)
    ax.yaxis.set_label_coords(0, 1.02)


def note(ax, text, *, size=18):
    ax.text(0.03, 0.985, text, transform=ax.figure.transFigure, fontsize=size, color=INK,
            ha="left", va="top")


def save(fig, name):
    out = OUT_DIR / f"{name}.svg"
    fig.savefig(out, format="svg", facecolor=PAPER)
    plt.close(fig)
    print(f"  wrote {out.relative_to(REPO_ROOT)}")


def penguins(cols):
    df = pl.read_csv(PENGUIN_CSV, null_values="NA").drop_nulls(FEATURES)
    X = df.select(cols).to_numpy().astype(float)
    mu, sd = X.mean(axis=0), X.std(axis=0)
    return (X - mu) / sd, df["species"].to_numpy(), mu, sd


def species_points(ax, X, species, *, size=60):
    for sp in SPECIES_ORDER:
        m, fill, _ = SPECIES_STYLE[sp]
        pts = X[species == sp]
        ax.scatter(pts[:, 0], pts[:, 1], marker=m, s=size * (1.25 if m == "^" else 1.0),
                   color=fill, edgecolor=PAPER, linewidth=0.7, zorder=3)


def species_legend(ax, *, x=0.03, y=0.985, size=17):
    glyph = {"o": "●", "^": "▲", "s": "■"}
    for sp in SPECIES_ORDER:
        m, fill, name = SPECIES_STYLE[sp]
        ax.text(x, y, glyph[m], transform=ax.figure.transFigure, color=fill, fontsize=size,
                ha="left", va="top")
        ax.text(x + 0.035, y, name, transform=ax.figure.transFigure, color=INK, fontsize=size,
                ha="left", va="top")
        x += 0.06 + 0.014 * len(name)


# ------------------------------------------------------------- 2-D intuition

LIM = (-3.0, 3.0)


@steps("pca-penguins", 3)
def pca_penguins(step):
    """Two standardized measurements; PC1 and PC2; projecting onto PC1."""
    Z, species, mu, sd = penguins(["bill_length_mm", "flipper_length_mm"])
    pca = PCA().fit(Z)
    fig, ax = fixed_fig(SPLIT, 175, 175, 110, 70)
    ax.set_xlim(*LIM)
    ax.set_ylim(*LIM)
    ax.set_aspect("equal")
    tidy(ax, grid=None)
    xt, yt = np.arange(35, 61, 5), np.arange(180, 231, 10)
    ax.set_xticks((xt - mu[0]) / sd[0], [str(v) for v in xt])
    ax.set_yticks((yt - mu[1]) / sd[1], [str(v) for v in yt])
    ax.set_xlabel("Bill length (mm)")
    ylabel_top(ax, "Flipper length (mm)")
    pc1, pc2 = pca.components_
    ev = pca.explained_variance_ratio_
    if step < 2:
        ax.scatter(Z[:, 0], Z[:, 1], s=55, color=STEEL, edgecolor=PAPER, lw=0.6, zorder=3)
    if step == 0:
        note(ax, "Two measurements per penguin (standardized)")
        return fig
    for v, col, lam, name in ((pc1, ORANGE, pca.explained_variance_[0], "PC1"),
                              (pc2, INK, pca.explained_variance_[1], "PC2")):
        L = 2 * np.sqrt(lam)
        ax.annotate("", xy=v * L, xytext=(0, 0), zorder=6,
                    arrowprops=dict(arrowstyle="-|>,head_length=0.8,head_width=0.4",
                                    color=col, lw=3.5, shrinkA=0, shrinkB=0))
    ax.text(*(pc1 * 2 * np.sqrt(pca.explained_variance_[0]) + [0.1, -0.1]),
            f"PC1: {ev[0]:.0%} of the variance", color=INK, fontsize=16, va="top", zorder=7)
    ax.text(*(pc2 * 2 * np.sqrt(pca.explained_variance_[1]) + [0.15, 0]),
            f"PC2: {ev[1]:.0%}", color=INK, fontsize=16, va="center", zorder=7)
    if step == 1:
        note(ax, "PC1 points along the most spread; PC2 is perpendicular")
    else:
        t = Z @ pc1
        P = np.outer(t, pc1)
        ax.plot([-3.4 * pc1[0], 3.4 * pc1[0]], [-3.4 * pc1[1], 3.4 * pc1[1]], color=ORANGE,
                lw=1.5, zorder=2)
        for a, b in zip(Z, P):
            ax.plot(*zip(a, b), color=QUIET, lw=0.6, zorder=1)
        ax.scatter(Z[:, 0], Z[:, 1], s=40, color=QUIET, edgecolor=PAPER, lw=0.5, zorder=3)
        ax.scatter(P[:, 0], P[:, 1], s=40, color=ORANGE, edgecolor=PAPER, lw=0.5, zorder=4)
        note(ax, f"Keep only PC1: one number per penguin,\n{ev[0]:.0%} of the variance kept")
    return fig


# ------------------------------------------------------------ four features

def four():
    Z, species, *_ = penguins(FEATURES)
    return Z, species, PCA().fit(Z)


@figure("pca-scree")
def pca_scree():
    Z, species, pca = four()
    ev = pca.explained_variance_ratio_
    ks = np.arange(1, len(ev) + 1)
    fig, ax = fixed_fig(SPLIT, 110, 60, 110, 80)
    tidy(ax, grid="y", spines=("bottom",))
    ax.bar(ks, ev, width=0.6, color=[ORANGE if k <= 2 else STEEL for k in ks])
    ax.plot(ks, np.cumsum(ev), color=INK, lw=2.5, marker="o", ms=9, mec=PAPER, zorder=4)
    for k, (e, c) in enumerate(zip(ev, np.cumsum(ev)), start=1):
        ax.text(k, e + 0.02, f"{e:.0%}", ha="center", va="bottom", fontsize=15, color=STEEL)
        if k > 1:  # PC1's running total is its own bar
            ax.text(k + 0.08, c + 0.035, f"{c:.0%}", ha="left", va="bottom", fontsize=15, color=INK)
    ax.set_xticks(ks, [f"PC{k}" for k in ks], fontsize=15)
    ax.set_ylim(0, 1.12)
    ax.set_yticks([0, 0.25, 0.5, 0.75, 1.0], ["0%", "25%", "50%", "75%", "100%"])
    ylabel_top(ax, "Share of variance: bars = each PC, line = running total")
    note(ax, f"Four measurements → PC1 and PC2 keep {np.cumsum(ev)[1]:.0%}")
    return fig


@figure("pca-loadings")
def pca_loadings():
    Z, species, pca = four()
    W = pca.components_[:2]
    fig = plt.figure(figsize=(SPLIT[0] / DPI, SPLIT[1] / DPI), dpi=DPI)
    fig.patch.set_facecolor(PAPER)
    for r, (w, name) in enumerate(zip(W, ["PC1", "PC2"])):
        ax = fig.add_axes([0.27, 0.55 - 0.43 * r, 0.65, 0.3])
        tidy(ax, grid="x", spines=())
        y = np.arange(len(w))[::-1]
        ax.barh(y, w, height=0.6, color=[ORANGE if r == 0 else INK] * len(w))
        ax.axvline(0, color=STEEL, lw=1.2)
        ax.set_yticks(y, FEATURE_NAMES, fontsize=15, color=INK)
        ax.set_xlim(-1, 1)
        for yy, v in zip(y, w):
            ax.text(v + (0.03 if v >= 0 else -0.03), yy, f"{v:+.2f}", va="center",
                    ha="left" if v >= 0 else "right", fontsize=14, color=STEEL)
        ax.text(-0.36, 1.08, f"{name} = weighted sum of all four", transform=ax.transAxes,
                fontsize=17, color=INK, ha="left", va="bottom")
    note(ax, "What do the components mean?")
    return fig


@figure("pca-species")
def pca_species():
    Z, species, pca = four()
    T = pca.transform(Z)[:, :2]
    ev = pca.explained_variance_ratio_
    fig, ax = fixed_fig(SPLIT, 110, 60, 110, 80)
    tidy(ax, grid="both")
    species_points(ax, T, species)
    ax.set_aspect("equal")
    ax.set_xlim(-3.6, 4.2)
    ax.set_ylim(-2.6, 3.4)
    ax.set_xlabel(f"PC1 ({ev[0]:.0%} of variance)")
    ylabel_top(ax, f"PC2 ({ev[1]:.0%})")
    species_legend(ax)
    return fig


# ------------------------------------------------------ PCA with PCA (MLB CF)

CF_CSV = REPO_ROOT / "datasets" / "mlb-center-fielders-2026" / "center-fielders.csv"
# grouped plate discipline / power / legs / glove, so the loadings read in blocks
CF_FEATURES = ["k_pct", "whiff_pct", "chase_pct", "bb_pct", "iso", "barrel_pct",
               "hard_hit_pct", "sprint_speed", "sb", "oaa", "arm_mph"]
CF_NAMES = ["Strikeout %", "Whiff %", "Chase %", "Walk %", "Isolated power", "Barrel %",
            "Hard-hit %", "Sprint speed", "Stolen bases", "Outs above average", "Arm strength"]
PETE = "Crow-Armstrong, Pete"
CF_LABELED = ["Kwan, Steven", "Cruz, Oneil", "Trout, Mike", "Rafaela, Ceddanne"]


def center_fielders():
    df = pl.read_csv(CF_CSV)
    X = df.select(CF_FEATURES).to_numpy().astype(float)
    Z = (X - X.mean(axis=0)) / X.std(axis=0)
    pca = PCA().fit(Z)
    # a component's sign is arbitrary; point PC1 toward power and PC2 toward chasing
    for k, feat in ((0, "iso"), (1, "chase_pct")):
        if pca.components_[k, CF_FEATURES.index(feat)] < 0:
            pca.components_[k] *= -1
    return df["player"].to_list(), pca.transform(Z), pca


def first_last(name):
    last, first = name.split(", ")
    return f"{first} {last}"


@figure("pca-cf-scree")
def pca_cf_scree():
    names, T, pca = center_fielders()
    ev = pca.explained_variance_ratio_
    ks = np.arange(1, len(ev) + 1)
    fig, ax = fixed_fig(SPLIT, 110, 60, 110, 80)
    tidy(ax, grid="y", spines=("bottom",))
    ax.bar(ks, ev, width=0.6, color=[ORANGE if k <= 2 else STEEL for k in ks])
    ax.plot(ks, np.cumsum(ev), color=INK, lw=2.5, marker="o", ms=8, mec=PAPER, zorder=4)
    for k, e in enumerate(ev[:3], start=1):  # beside the bar, clear of the line
        ax.text(k + 0.34, e, f"{e:.0%}", ha="left", va="center", fontsize=14, color=STEEL)
    c2 = np.cumsum(ev)[1]
    ax.text(1.85, c2 + 0.01, f"{c2:.0%}", ha="right", va="bottom", fontsize=15, color=INK)
    ax.set_xticks(ks, [f"{k}" for k in ks], fontsize=14)
    ax.set_xlabel("Principal component")
    ax.set_ylim(0, 1.12)
    ax.set_yticks([0, 0.25, 0.5, 0.75, 1.0], ["0%", "25%", "50%", "75%", "100%"])
    ylabel_top(ax, "Share of variance: bars = each PC, line = running total")
    note(ax, f"Eleven stats → PC1 and PC2 keep {c2:.0%}")
    return fig


@figure("pca-cf-loadings")
def pca_cf_loadings():
    names, T, pca = center_fielders()
    W = pca.components_[:2]
    fig = plt.figure(figsize=(SPLIT[0] / DPI, SPLIT[1] / DPI), dpi=DPI)
    fig.patch.set_facecolor(PAPER)
    titles = ["PC1: swing big", "PC2: chase and run, don't walk"]
    for r, (w, title) in enumerate(zip(W, titles)):
        ax = fig.add_axes([0.3, 0.5 - 0.44 * r, 0.62, 0.36])
        tidy(ax, grid="x", spines=())
        y = np.arange(len(w))[::-1]
        ax.barh(y, w, height=0.65, color=ORANGE if r == 0 else INK)
        ax.axvline(0, color=STEEL, lw=1.2)
        ax.set_yticks(y, CF_NAMES, fontsize=13, color=INK)
        ax.set_xlim(-0.8, 0.8)
        ax.set_xticks([-0.5, 0, 0.5])
        for yy, v in zip(y, w):
            v = 0.0 if abs(v) < 0.005 else v  # no "-0.00"
            ax.text(v + (0.02 if v >= 0 else -0.02), yy, f"{v:+.2f}", va="center",
                    ha="left" if v >= 0 else "right", fontsize=11, color=STEEL)
        ax.text(-0.42, 1.03, title, transform=ax.transAxes, fontsize=17, color=INK,
                ha="left", va="bottom")
    return fig


@steps("pca-cf-map", 3)
def pca_cf_map(step):
    """The 40 center fielders on PC1/PC2; then names for the corners; then PCA."""
    names, T, pca = center_fielders()
    ev = pca.explained_variance_ratio_
    fig, ax = fixed_fig(SPLIT, 90, 50, 110, 110)
    tidy(ax, grid="both")
    ax.set_aspect("equal")
    ax.set_xlim(-6, 6)
    ax.set_ylim(-4, 4)
    ax.set_xlabel(f"PC1 ({ev[0]:.0%} of variance)")
    ylabel_top(ax, f"PC2 ({ev[1]:.0%})")
    pete = names.index(PETE)
    others = [i for i in range(len(names)) if not (step == 2 and i == pete)]
    ax.scatter(T[others, 0], T[others, 1], s=80, color=STEEL, edgecolor=PAPER, lw=0.8, zorder=3)
    if step == 0:
        note(ax, f"{len(names)} center fielders, 11 stats each → 2 numbers each")
        return fig
    for name in CF_LABELED:
        i = names.index(name)
        ax.annotate(first_last(name), T[i, :2], xytext=(0, -14 if T[i, 1] < 0 else 10),
                    textcoords="offset points", ha="center",
                    va="top" if T[i, 1] < 0 else "bottom", fontsize=14, color=STEEL)
    for x, text, ha in ((0, "← more contact", "left"), (1, "more power, more K →", "right")):
        ax.text(x, -0.115, text, transform=ax.transAxes, ha=ha, va="top", fontsize=14,
                color=INK)
    ax.text(-5.9, 3.9, "↑ chases, runs\n↓ walks", ha="left", va="top", fontsize=14,
            color=INK, linespacing=1.3)
    if step == 1:
        note(ax, "Name the directions using the loadings")
        return fig
    ax.scatter(*T[pete, :2], s=200, color=ORANGE, edgecolor=PAPER, lw=1.2, zorder=5)
    ax.annotate("Pete Crow-Armstrong", T[pete, :2], xytext=(0, 14),
                textcoords="offset points", ha="center", va="bottom", fontsize=16, color=INK,
                zorder=6)
    note(ax, f"PCA on PCA: #{int((T[:, 0] > T[pete, 0]).sum()) + 1} of {len(names)} on PC1")
    return fig


def main(argv: list[str]) -> None:
    if FONT_PATH.exists():
        font_manager.fontManager.addfont(str(FONT_PATH))
        family = font_manager.FontProperties(fname=str(FONT_PATH)).get_name()
        plt.rcParams["font.family"] = [family, "DejaVu Sans"]
    plt.rcParams["svg.fonttype"] = "path"
    wanted = argv or list(FIGURES)
    unknown = [name for name in wanted if name not in FIGURES]
    if unknown:
        raise SystemExit(f"unknown figure(s): {', '.join(unknown)}")
    print(f"writing {len(wanted)} figure(s) to {OUT_DIR.relative_to(REPO_ROOT)}")
    for name in wanted:
        save(FIGURES[name](), name)


if __name__ == "__main__":
    main(sys.argv[1:])
