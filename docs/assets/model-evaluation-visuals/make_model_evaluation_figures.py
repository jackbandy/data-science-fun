#!/usr/bin/env python3
"""Model evaluation figures: held-out data, imbalance, confusion matrices,
precision and recall, F-score, and multiclass strategies.

NOTICE: this file was substantially drafted by an LLM coding system and has not
yet been reviewed. Check every figure against the slide it illustrates.

Follows docs/assets/STYLE.md and the clustering-visuals generator: grayscale
neutrals, vendored Libre Franklin drawn as paths, numbered step sets.

The running example is Week 9's "Chinstrap vs. the rest": Chinstrap is the
positive class, drawn as the orange triangle (the class the classifier is
looking for gets the accent color); Adélie and Gentoo are the negative class,
steel circles. 68 of 342 penguins are Chinstraps, so the classes are
imbalanced (20% / 80%) without any made-up data. In the three-species figures,
Adélie is a steel circle and Gentoo an ink square, as in clustering-visuals.

In the train/test and cross-validation figures, orange marks the part being
evaluated (the held-out fold); the locked test set is ink.

Canvases: SPLIT (900 x 700) for the right column of a `.golden-figure` split
slide; GOLDEN (1000 x 618) for full-width `.image-frame-slide` figures.

Data: `datasets/classification-examples/penguins.csv`, the 342 penguins with
all four measurements; features are bill length and flipper length,
standardized, as in clustering-visuals. Predictions are 5-fold
cross-validated (stratified, seed 418), so every penguin is predicted by a
model that never saw it. See SOURCES.md in this folder.

Usage:  python3 make_model_evaluation_figures.py [name ...]
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
from matplotlib.patches import FancyBboxPatch, Rectangle
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import StratifiedKFold, cross_val_predict
from sklearn.svm import SVC

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
ORANGE_TINT = "#FDE3DA"

PHI = (1 + 5**0.5) / 2
DPI = 100
SPLIT = (900, 700)
GOLDEN = (1000, round(1000 / PHI))

POS, NEG = "▲", "●"  # ▲ Chinstrap, ● not Chinstrap
SPECIES_STYLE = {"Adelie": ("o", STEEL, "Adélie"),
                 "Chinstrap": ("^", ORANGE, "Chinstrap"),
                 "Gentoo": ("s", INK, "Gentoo")}
SPECIES_ORDER = ["Adelie", "Chinstrap", "Gentoo"]
GLYPH = {"o": "●", "^": "▲", "s": "■"}
CUTOFFS = [0.8, 0.5, 0.2]

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


def canvas(size=SPLIT):
    fig = plt.figure(figsize=(size[0] / DPI, size[1] / DPI), dpi=DPI)
    fig.patch.set_facecolor(PAPER)
    return fig


def fixed_fig(size, left, right, top, bottom):
    width, height = size
    fig = canvas(size)
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


def bare(ax):
    ax.set_xticks([])
    ax.set_yticks([])
    for s in ax.spines.values():
        s.set_visible(False)


def note(fig, text, *, size=18, y=0.985):
    fig.text(0.03, y, text, fontsize=size, color=INK, ha="left", va="top")


def save(fig, name):
    out = OUT_DIR / f"{name}.svg"
    fig.savefig(out, format="svg", facecolor=PAPER)
    plt.close(fig)
    print(f"  wrote {out.relative_to(REPO_ROOT)}")


# ---------------------------------------------------------------------- data

def penguins():
    df = pl.read_csv(PENGUIN_CSV, null_values="NA").drop_nulls(
        ["bill_length_mm", "bill_depth_mm", "flipper_length_mm", "body_mass_g"])
    X = df.select("bill_length_mm", "flipper_length_mm").to_numpy().astype(float)
    return (X - X.mean(0)) / X.std(0), df["species"].to_numpy()


CV = StratifiedKFold(5, shuffle=True, random_state=418)


def chinstrap_scores():
    """Cross-validated P(Chinstrap) from a logistic regression, and the true labels."""
    Z, species = penguins()
    y = (species == "Chinstrap").astype(int)
    p = cross_val_predict(LogisticRegression(), Z, y, cv=CV, method="predict_proba")[:, 1]
    return p, y


def counts(y, yhat):
    tp = int(np.sum((y == 1) & (yhat == 1)))
    fn = int(np.sum((y == 1) & (yhat == 0)))
    fp = int(np.sum((y == 0) & (yhat == 1)))
    tn = int(np.sum((y == 0) & (yhat == 0)))
    return tp, fn, fp, tn


# --------------------------------------------------------- held-out evaluation

def block(ax, x, y, w, h, *, fill, text="", color=INK, edge=PAPER, size=15):
    ax.add_patch(FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0,rounding_size=0.08",
                                facecolor=fill, edgecolor=edge, lw=2.5))
    if text:
        ax.text(x + w / 2, y + h / 2, text, ha="center", va="center", fontsize=size, color=color)


@steps("holdout", 6)
def holdout(step):
    """v0: train/test split. v1-v5: five-fold cross-validation inside the train set."""
    n, n_test = 342, 68
    fig, ax = fixed_fig(SPLIT, 30, 30, 120, 30)
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 7.2)
    bare(ax)
    W = 10 * (n - n_test) / n  # train width
    top = 6.0
    block(ax, 0, top, W, 0.9, fill=SOFT_GRAY, text=f"Train: {n - n_test} penguins", edge=BORDER)
    block(ax, W, top, 10 - W, 0.9, fill=INK, text=f"Test: {n_test}", color=PAPER)
    if step == 0:
        note(fig, "Set the test set aside first (20% here),\nand do not touch it until the end")
        return fig
    fw = W / 5
    for r in range(step):
        y = top - 1.15 * (r + 1)
        for f in range(5):
            held = f == r
            block(ax, f * fw, y, fw, 0.85, fill=ORANGE if held else SOFT_GRAY,
                  text="validate" if held else "fit", color=PAPER if held else STEEL,
                  edge=PAPER, size=13)
        ax.text(W + 0.25, y + 0.42, f"round {r + 1}", fontsize=14, color=STEEL, va="center")
    note(fig, f"5-fold cross-validation, round {step}: fit on 4 folds,\n"
              f"score on the 5th. The test set stays locked.")
    return fig


# ---------------------------------------------------------------- imbalance

@figure("chinstrap-waffle")
def chinstrap_waffle():
    Z, species = penguins()
    y = species == "Chinstrap"
    order = np.r_[np.flatnonzero(y), np.flatnonzero(~y)]
    cols = 19
    fig, ax = fixed_fig(SPLIT, 40, 40, 150, 40)
    bare(ax)
    for k, i in enumerate(order):
        r, c = divmod(k, cols)
        if y[i]:
            ax.scatter(c, -r, marker="^", s=150, color=ORANGE, edgecolor=PAPER, lw=0.6)
        else:
            ax.scatter(c, -r, marker="o", s=120, color=STEEL, edgecolor=PAPER, lw=0.6)
    ax.set_xlim(-0.8, cols - 0.2)
    ax.set_ylim(-(len(order) // cols) - 0.8, 0.8)
    ax.set_aspect("equal")
    note(fig, f"{POS} {y.sum()} Chinstraps ({y.mean():.0%})   {NEG} {(~y).sum()} others ({(~y).mean():.0%})\n"
              f"Always guessing “not Chinstrap”: {(~y).mean():.0%} accurate,\n"
              f"and it finds zero Chinstraps")
    return fig


@steps("resample", 3)
def resample(step):
    n_pos, n_neg = 68, 274
    bars = {0: (n_pos, n_neg, "Original training data"),
            1: (n_pos, n_pos, "Undersample the majority: keep 68 of 274 at random"),
            2: (n_neg, n_neg, "Oversample the minority: repeat Chinstraps up to 274")}
    p, q, title = bars[step]
    fig, ax = fixed_fig(SPLIT, 230, 80, 140, 80)
    tidy(ax, grid="x", spines=())
    ax.barh([1, 0], [p, q], height=0.55, color=[ORANGE, STEEL])
    if step == 2:
        ax.barh([1], [p - n_pos], left=[n_pos], height=0.55, color=ORANGE_TINT,
                edgecolor=ORANGE, hatch="//", lw=1.2)
        ax.text(n_pos + (p - n_pos) / 2, 1, "copies", ha="center", va="center", fontsize=15, color=INK)
    if step == 1:
        ax.barh([0], [n_neg - n_pos], left=[n_pos], height=0.55, color=PAPER,
                edgecolor=QUIET, ls="--", lw=1.5)
        ax.text(n_pos + (n_neg - n_pos) / 2, 0, "set aside", ha="center", va="center",
                fontsize=15, color=STEEL)
    for yy, v in ((1, p), (0, q)):
        ax.text(v + 6, yy, str(v), va="center", fontsize=16, color=INK)
    ax.set_yticks([1, 0], [f"{POS} Chinstrap", f"{NEG} Not Chinstrap"], fontsize=17, color=INK)
    ax.set_xlim(0, 300)
    ax.set_ylim(-0.6, 1.6)
    ax.set_xlabel("Training examples")
    note(fig, title)
    return fig


# --------------------------------------------------------- confusion matrices

def matrix(ax, M, rows, cols, *, diag=True, big=26):
    n, m = M.shape
    ax.set_xlim(0, m)
    ax.set_ylim(n, 0)
    bare(ax)
    for i in range(n):
        for j in range(m):
            good = (i == j) if diag else False
            ax.add_patch(Rectangle((j, i), 1, 1, facecolor=ORANGE_TINT if good else SOFT_GRAY,
                                   edgecolor=PAPER, lw=4))
            ax.text(j + 0.5, i + 0.5, M[i, j] if isinstance(M[i, j], str) else str(M[i, j]),
                    ha="center", va="center", fontsize=big, color=INK if good else STEEL)
    for i, r in enumerate(rows):
        ax.text(-0.08, i + 0.5, r, ha="right", va="center", fontsize=17, color=INK)
    for j, c in enumerate(cols):
        ax.text(j + 0.5, -0.1, c, ha="center", va="bottom", fontsize=17, color=INK)


@steps("confusion-chinstrap", 2)
def confusion_chinstrap(step):
    p, y = chinstrap_scores()
    yhat = np.zeros_like(y) if step == 0 else (p >= 0.5).astype(int)
    tp, fn, fp, tn = counts(y, yhat)
    M = np.array([[f"TP\n{tp}", f"FN\n{fn}"], [f"FP\n{fp}", f"TN\n{tn}"]], dtype=object)
    fig, ax = fixed_fig(SPLIT, 280, 50, 190, 150)
    matrix(ax, M, [f"True {POS} Chinstrap", f"True {NEG} other"],
           [f"Predicted {POS}", f"Predicted {NEG}"], big=24)
    acc = (tp + tn) / len(y)
    prec = tp / (tp + fp) if tp + fp else float("nan")
    rec = tp / (tp + fn)
    who = {0: "Always guess “not Chinstrap”",
           1: "Logistic regression, cutoff 0.5"}[step]
    note(fig, who)
    prec_s = "undefined (0 / 0)" if np.isnan(prec) else f"{prec:.0%}"
    fig.text(0.03, 0.08, f"Accuracy {acc:.0%}     Precision {prec_s}     Recall {rec:.0%}",
             fontsize=18, color=INK, ha="left", va="bottom")
    return fig


@figure("confusion-penguins")
def confusion_penguins():
    """Three species, an RBF SVM (Week 9), cross-validated."""
    Z, species = penguins()
    yhat = cross_val_predict(SVC(kernel="rbf"), Z, species, cv=CV)
    M = np.array([[int(np.sum((species == a) & (yhat == b))) for b in SPECIES_ORDER]
                  for a in SPECIES_ORDER])
    names = [f"{SPECIES_STYLE[s][2]} {GLYPH[SPECIES_STYLE[s][0]]}" for s in SPECIES_ORDER]
    fig, ax = fixed_fig(SPLIT, 230, 40, 190, 100)
    matrix(ax, M, names, [f"Pred.\n{n}" for n in names], big=26)
    ax.text(-0.08, -0.1, "True ↓\nPredicted →", ha="right", va="bottom", fontsize=14, color=STEEL)
    note(fig, f"SVM (RBF kernel), 5-fold cross-validated: {np.trace(M) / M.sum():.0%} accurate")
    return fig


# ------------------------------------------------------ precision and recall

@steps("pr-cutoff", 3)
def pr_cutoff(step):
    p, y = chinstrap_scores()
    rng = np.random.default_rng(418)
    jit = rng.uniform(-0.38, 0.38, len(p))
    fig, ax = fixed_fig(SPLIT, 170, 40, 170, 90)
    tidy(ax, grid=None, spines=("bottom",))
    t = CUTOFFS[step]
    ax.axvspan(t, 1.02, color=ORANGE_TINT, zorder=0)
    ax.axvline(t, color=ORANGE, lw=3, zorder=1)
    neg, pos = y == 0, y == 1
    ax.scatter(p[neg], 0 + jit[neg], marker="o", s=55, color=STEEL, edgecolor=PAPER, lw=0.5, zorder=3)
    ax.scatter(p[pos], 1 + jit[pos], marker="^", s=75, color=ORANGE, edgecolor=INK, lw=0.6, zorder=3)
    ax.set_yticks([1, 0], [f"{POS} Chinstrap", f"{NEG} other"], fontsize=15, color=INK)
    ax.set_xlim(-0.02, 1.02)
    ax.set_ylim(-0.55, 1.55)
    ax.set_xlabel("Model's score: estimated chance of Chinstrap")
    ax.text(t + 0.01, 1.52, "predicted Chinstrap →", fontsize=14, color=INK, va="top")
    tp, fn, fp, tn = counts(y, (p >= t).astype(int))
    note(fig, f"Cutoff {t}: {tp + fp} predicted Chinstrap, {tp} of them correct\n"
              f"Precision {tp}/{tp + fp} = {tp / (tp + fp):.0%}     "
              f"Recall {tp}/{tp + fn} = {tp / (tp + fn):.0%}")
    return fig


@figure("pr-curve")
def pr_curve():
    p, y = chinstrap_scores()
    ts = np.unique(p)[::-1]
    P, R = [], []
    for t in ts:
        tp, fn, fp, tn = counts(y, (p >= t).astype(int))
        P.append(tp / (tp + fp))
        R.append(tp / (tp + fn))
    fig, ax = fixed_fig(SPLIT, 110, 60, 110, 80)
    tidy(ax, grid="both")
    ax.plot(R, P, color=STEEL, lw=2.5)
    for t in CUTOFFS:
        tp, fn, fp, tn = counts(y, (p >= t).astype(int))
        r, pr = tp / (tp + fn), tp / (tp + fp)
        ax.scatter([r], [pr], s=180, color=ORANGE, edgecolor=INK, lw=1.2, zorder=4)
        ax.annotate(f"cutoff {t}", xy=(r, pr), xytext=(r - 0.2, pr - 0.12), fontsize=15,
                    color=INK, arrowprops=dict(arrowstyle="-", color=INK, lw=1.2))
    ax.set_xlim(0, 1.02)
    ax.set_ylim(0, 1.05)
    ax.set_xlabel("Recall: share of Chinstraps found")
    ylabel_top(ax, "Precision: share of “Chinstrap” guesses that are right")
    note(fig, "Lower the cutoff: recall rises, precision falls")
    return fig


@figure("f1-mean")
def f1_mean():
    r = 0.9
    pr = np.linspace(0.001, 1, 400)
    fig, ax = fixed_fig(SPLIT, 110, 60, 110, 80)
    tidy(ax, grid="both")
    ax.plot(pr, (pr + r) / 2, color=QUIET, lw=2.5, ls="--")
    ax.plot(pr, 2 * pr * r / (pr + r), color=ORANGE, lw=3.5)
    ax.text(0.05, 0.53, "Arithmetic mean", fontsize=16, color=STEEL)
    ax.text(0.2, 0.2, "F₁ (harmonic mean)", fontsize=16, color=INK)
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.set_xlabel("Precision")
    ylabel_top(ax, f"Combined score, with recall fixed at {r}")
    note(fig, "F₁ stays low unless both precision and recall are high")
    return fig


# --------------------------------------------------------------- multiclass

PAIRS_OVR = [("Adelie", None), ("Chinstrap", None), ("Gentoo", None)]
PAIRS_OVO = [("Adelie", "Chinstrap"), ("Adelie", "Gentoo"), ("Chinstrap", "Gentoo")]


@steps("ovr-ovo", 2)
def ovr_ovo(step):
    Z, species = penguins()
    pairs = PAIRS_OVR if step == 0 else PAIRS_OVO
    fig = canvas(GOLDEN)
    for c, (a, b) in enumerate(pairs):
        ax = fig.add_axes([0.03 + c * 0.325, 0.06, 0.3, 0.68])
        bare(ax)
        ax.set_facecolor(SOFT_GRAY)
        ax.set_xlim(-2.5, 3.2)
        ax.set_ylim(-2.4, 2.5)
        pos = species == a
        neg = (~pos) if b is None else (species == b)
        out = ~(pos | neg)
        if out.any():
            ax.scatter(Z[out, 0], Z[out, 1], s=14, facecolor="none", edgecolor=QUIET, lw=0.8)
        ax.scatter(Z[neg, 0], Z[neg, 1], s=22, marker="o", color=STEEL, edgecolor=PAPER, lw=0.4)
        ax.scatter(Z[pos, 0], Z[pos, 1], s=30, marker="^", color=ORANGE, edgecolor=PAPER, lw=0.4)
        label = (f"{SPECIES_STYLE[a][2]} vs. rest" if b is None
                 else f"{SPECIES_STYLE[a][2]} vs. {SPECIES_STYLE[b][2]}")
        ax.text(0.0, 1.03, f"{c + 1}. {label}", transform=ax.transAxes,
                fontsize=16, color=INK, ha="left", va="bottom")
    title = {0: "One vs. rest: one binary classifier per species (orange = “yes”)",
             1: "One vs. one: one binary classifier per pair (hollow = not used)"}[step]
    note(fig, title, size=19)
    return fig


@figure("classifier-count")
def classifier_count():
    ks = np.arange(2, 11)
    fig, ax = fixed_fig(SPLIT, 110, 60, 110, 80)
    tidy(ax, grid="both")
    ax.plot(ks, ks, color=STEEL, lw=2.5, marker="o", ms=8, mec=PAPER)
    ax.plot(ks, ks * (ks - 1) / 2, color=ORANGE, lw=3, marker="o", ms=8, mec=PAPER)
    ax.text(10.1, 10, "One vs. rest: K", fontsize=15, color=STEEL, va="center")
    ax.text(10.1, 45, "One vs. one:\nK(K − 1)/2", fontsize=15, color=INK, va="center")
    ax.scatter([3], [3], s=380, facecolor="none", edgecolor=INK, lw=2.2, zorder=5)
    ax.annotate("penguins: K = 3,\n3 classifiers either way", xy=(3, 3), xytext=(3.4, 22),
                fontsize=15, color=INK, arrowprops=dict(arrowstyle="-", color=INK, lw=1.2))
    ax.set_xticks(ks)
    ax.set_xlim(1.5, 12.8)
    ax.set_ylim(0, 48)
    ax.set_xlabel("Number of classes, K")
    ylabel_top(ax, "Binary classifiers to train")
    return fig


def main(argv: list[str]) -> None:
    if FONT_PATH.exists():
        font_manager.fontManager.addfont(str(FONT_PATH))
        family = font_manager.FontProperties(fname=str(FONT_PATH)).get_name()
        # DejaVu Sans (bundled with matplotlib) supplies the class glyphs.
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
