#!/usr/bin/env python3
"""Figures for the Week 8, Day 1 "intro to modeling" slides.

NOTICE: this file was substantially drafted by an LLM coding system and has not
yet been reviewed. Check every figure against the slide it illustrates.

Follows docs/assets/STYLE.md and mirrors viz-basics/make_viz_basics_figures.py:
golden-ratio canvases, grayscale neutrals with orange reserved for the focal
element, vendored Libre Franklin drawn as paths so each SVG is self-contained.

Data:
  * Cook County home sales 2025 come from datasets/ in this repo, filtered the
    same way as the Week 5 slides (see the dataset README for provenance).
  * The bias-variance bullseyes are synthetic, redrawn after Scott
    Fortmann-Roe, "Understanding the Bias-Variance Tradeoff" (2012). See
    SOURCES.md in this folder.
  * The loss-function curves are plain math, no data.
  * The Day 2 classification figures (cls-*) read datasets/classification-examples/
    and need scikit-learn, which the slide venv does not include.

Usage:  python3 make_week8_figures.py [name ...]
        uv run --with scikit-learn --with polars --with matplotlib python3 make_week8_figures.py cls-...
"""

from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

import matplotlib

matplotlib.use("Agg")

import matplotlib.pyplot as plt
import numpy as np
import polars as pl
from matplotlib import font_manager
from matplotlib.patches import Circle

OUT_DIR = Path(__file__).resolve().parent
REPO_ROOT = OUT_DIR.parents[2]
DATASETS = REPO_ROOT / "datasets"
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

PHI = (1 + 5**0.5) / 2
WIDTH_PX = 1000
DPI = 100

FIGURES: dict[str, callable] = {}


def figure(name: str):
    """Register a builder under the filename stem it writes."""
    def wrap(fn):
        FIGURES[name] = fn
        return fn
    return wrap


def new_fig(width=WIDTH_PX, height=None, **kw):
    height = height or round(width / PHI)
    fig, ax = plt.subplots(figsize=(width / DPI, height / DPI), dpi=DPI, **kw)
    fig.patch.set_facecolor(PAPER)
    for a in np.atleast_1d(ax).ravel():
        a.set_facecolor(PAPER)
    return fig, ax


def tidy(ax, *, grid="y", spines=("left", "bottom")):
    """The deck's default axis furniture: two hairline spines, one grid."""
    for side in ("top", "right", "left", "bottom"):
        ax.spines[side].set_visible(side in spines)
        ax.spines[side].set_color(BORDER)
    if grid:
        ax.grid(axis=grid, color=BORDER, linewidth=0.8, alpha=0.7)
    ax.set_axisbelow(True)
    ax.tick_params(colors=STEEL, labelsize=11, length=0)
    for lbl in (ax.xaxis.label, ax.yaxis.label):
        lbl.set_color(STEEL)
        lbl.set_fontsize(13)
    return ax


def save(fig, name):
    out = OUT_DIR / f"{name}.svg"
    if isinstance(fig, str):  # already-rendered SVG markup
        out.write_text(fig, encoding="utf-8")
        print(f"  wrote {out.relative_to(REPO_ROOT)}")
        return
    fig.savefig(out, format="svg", facecolor=PAPER, bbox_inches="tight",
                pad_inches=0.12)
    plt.close(fig)
    print(f"  wrote {out.relative_to(REPO_ROOT)}")


def dollars(v, _=None):
    return f"${v / 1e6:g}M" if abs(v) >= 1e6 else f"${v / 1e3:,.0f}k"


_cache: dict[str, object] = {}


def barocas():
    """The Week 5 Barocas figure script, loaded for its 3D surface renderer."""
    if "barocas" not in _cache:
        path = OUT_DIR.parent / "barocas-inscrutability" / "make_inscrutability_figures.py"
        spec = importlib.util.spec_from_file_location("make_inscrutability_figures", path)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        _cache["barocas"] = module
    return _cache["barocas"]


def homes() -> pl.DataFrame:
    """Cook County single-family sales, filtered the way the Week 5 slides filter them."""
    if "homes" not in _cache:
        df = pl.read_csv(
            DATASETS / "cook-county-home-sales-2025" / "cook-county-home-sales-2025.csv",
            ignore_errors=True,
        )
        _cache["homes"] = df.filter(
            (pl.col("property_group") == "Single-Family")
            & (~pl.col("is_multisale"))
            & (pl.col("sale_price") > 10_000)
            & pl.col("building_sqft").is_not_null()
        )
    return _cache["homes"]


# --------------------------------------------------------------------------
# Loss
# --------------------------------------------------------------------------

@figure("loss-functions")
def loss_functions():
    """Squared vs. absolute loss for one point, as a function of the error."""
    err = np.linspace(-3, 3, 400)
    fig, ax = new_fig(width=820)
    ax.plot(err, err**2, color=ORANGE, linewidth=3, zorder=3)
    ax.plot(err, np.abs(err), color=STEEL, linewidth=3, zorder=3)
    ax.text(0, 8.2, "squared  $(y - \\theta)^2$", color=ORANGE, fontsize=15, ha="center")
    ax.text(0, 7.3, "absolute  $|y - \\theta|$", color=STEEL, fontsize=15, ha="center")
    ax.set(xlim=(-3, 3), ylim=(0, 9), xlabel="Error, $y - \\theta$", ylabel="Loss")
    tidy(ax)
    return fig


@figure("house-average-loss")
def house_average_loss():
    """Average loss over all home sales for every candidate constant theta.

    Squared loss bottoms out at the mean, absolute loss at the median. Each
    curve is rescaled to its own minimum so the two shapes share one axis.
    """
    y = homes()["sale_price"].to_numpy().astype(float)
    thetas = np.linspace(100_000, 900_000, 161)
    mse = np.array([np.mean((y - t) ** 2) for t in thetas])
    mae = np.array([np.mean(np.abs(y - t)) for t in thetas])
    mean, median = y.mean(), np.median(y)

    fig, axes = new_fig(width=1000, height=420, ncols=2)
    for ax, curve, best, color, name, est in [
        (axes[0], mse, mean, ORANGE, "Average squared loss", "mean"),
        (axes[1], mae, median, STEEL, "Average absolute loss", "median"),
    ]:
        scaled = curve / curve.min()
        ax.plot(thetas, scaled, color=color, linewidth=3, zorder=3)
        ax.axvline(best, color=INK, linewidth=1, linestyle=(0, (4, 4)), zorder=2)
        ax.text(best + 15_000, scaled.max(), f"{est} = {dollars(best)}",
                color=INK, fontsize=13, va="top")
        ax.set_title(name, fontsize=16, color=INK, loc="left", pad=10)
        ax.set_xlabel("$\\theta$ (one predicted price for every home)")
        ax.xaxis.set_major_formatter(dollars)
        ax.set_yticks([])
        tidy(ax, grid=None, spines=("bottom",))
    fig.subplots_adjust(wspace=0.12)
    return fig


# --------------------------------------------------------------------------
# Bias and variance
# --------------------------------------------------------------------------

@figure("bias-variance-bullseye")
def bias_variance_bullseye():
    """Four targets: rows are bias, columns are variance.

    Each dot is one fitted model (one re-run of the whole data-collection and
    fitting process). Redrawn after Fortmann-Roe (2012).
    """
    rng = np.random.default_rng(418)
    fig, axes = new_fig(width=760, height=760, nrows=2, ncols=2)
    for i, (bias_name, offset) in enumerate([("Low bias", 0.0), ("High bias", 0.48)]):
        for j, (var_name, spread) in enumerate([("Low variance", 0.07), ("High variance", 0.24)]):
            ax = axes[i][j]
            for k, r in enumerate([1.0, 0.75, 0.5, 0.25]):
                ax.add_patch(Circle((0, 0), r, facecolor=PAPER if k % 2 == 0 else SOFT_GRAY,
                                    edgecolor=QUIET, linewidth=1.2, zorder=1))
            ax.add_patch(Circle((0, 0), 0.1, facecolor=ORANGE, edgecolor="none", zorder=2))
            pts = rng.normal(0, spread, size=(12, 2)) + np.array([offset * 0.7, offset * 0.7])
            ax.scatter(pts[:, 0], pts[:, 1], s=46, color=INK, zorder=3,
                       edgecolor=PAPER, linewidth=0.8)
            ax.set(xlim=(-1.08, 1.08), ylim=(-1.08, 1.08), aspect="equal")
            ax.axis("off")
            if i == 0:
                ax.set_title(var_name, fontsize=16, color=INK, pad=8)
            if j == 0:
                ax.text(-1.25, 0, bias_name, fontsize=16, color=INK, rotation=90,
                        ha="center", va="center")
    fig.subplots_adjust(wspace=0.05, hspace=0.08)
    return fig


# --------------------------------------------------------------------------
# Overfitting
# --------------------------------------------------------------------------

def _overfit_sample() -> tuple[np.ndarray, np.ndarray]:
    df = (homes().filter((pl.col("sale_price") < 1_200_000)
                         & (pl.col("building_sqft") < 4_000))
          .sample(14, seed=418))
    return (df["building_sqft"].to_numpy().astype(float),
            df["sale_price"].to_numpy().astype(float))


def _overfit(labeled: bool, models: int = 3):
    """Three panels of the same sales; only the first `models` panels get their fitted curve."""
    x, y = _overfit_sample()
    # Polynomials on standardized x, so the degree-10 fit stays numerically sane.
    mu, sd = x.mean(), x.std()
    grid = np.linspace(x.min() - 50, x.max() + 50, 600)
    fits = [
        ("A", 0, "Underfit", "one number for every home"),
        ("B", 1, "Just right", "a line follows the trend"),
        ("C", 10, "Overfit", "chases the noise in 14 sales"),
    ]
    fig, axes = new_fig(width=1100, height=400, ncols=3, sharey=True)
    for i, (ax, (letter, deg, name, note)) in enumerate(zip(axes, fits)):
        shown = i < models
        if shown:
            coef = np.polyfit((x - mu) / sd, y, deg)
            ax.plot(grid, np.polyval(coef, (grid - mu) / sd), color=ORANGE,
                    linewidth=2.6, zorder=2)
        ax.scatter(x, y, s=40, color=INK, zorder=3, edgecolor=PAPER, linewidth=0.8)
        ax.set(ylim=(0, 1_300_000))
        ax.yaxis.set_major_formatter(dollars)
        ax.set_xticks([1000, 1500, 2000])
        ax.set_xlabel("Building sqft")
        heading = f"{letter}. {name}" if labeled else letter
        # Same title pad in both versions, so the plain and labeled SVGs line
        # up when one replaces the other on the slide.
        # A panel without its curve keeps a transparent title, so every build step crops to the same bbox.
        ax.set_title(heading, fontsize=18, color=INK, loc="left", pad=30,
                     alpha=1 if shown else 0)
        if labeled:
            ax.text(0, 1.03, note, transform=ax.transAxes, fontsize=12,
                    color=STEEL, va="bottom")
        tidy(ax)
    fig.subplots_adjust(wspace=0.08)
    return fig


@figure("overfit-data")
def overfit_data():
    return _overfit(labeled=False, models=0)


@figure("overfit-a")
def overfit_a():
    return _overfit(labeled=False, models=1)


@figure("overfit-ab")
def overfit_ab():
    return _overfit(labeled=False, models=2)


@figure("overfit-abc")
def overfit_abc():
    return _overfit(labeled=False)


@figure("overfit-abc-labeled")
def overfit_abc_labeled():
    return _overfit(labeled=True)


# --------------------------------------------------------------------------
# Multiple linear regression
# --------------------------------------------------------------------------

@figure("house-plane-3d")
def house_plane_3d():
    """Plane of best fit for sale price on building sqft and bedrooms.

    Drawn with the Week 5 Barocas renderer so it matches that deck's 3D boxes.
    The plane is fit on every sale, matching the slide's printed coefficients;
    only a sample of sales is drawn, so the cloud stays readable.
    """
    df = homes()
    X = np.column_stack([np.ones(df.height), df["building_sqft"].to_numpy(),
                         df["bedrooms"].to_numpy()]).astype(float)
    theta = np.linalg.lstsq(X, df["sale_price"].to_numpy().astype(float), rcond=None)[0]

    sqft_lo, sqft_hi, beds_lo, beds_hi = 500, 4000, 1, 6
    shown = (df.filter(pl.col("building_sqft").is_between(sqft_lo, sqft_hi)
                       & pl.col("bedrooms").is_between(beds_lo, beds_hi)
                       & (pl.col("sale_price") < 1_500_000))
             .sample(300, seed=418))
    rng = np.random.default_rng(418)
    # Jitter bedrooms so the points don't stack in six flat rows.
    beds = shown["bedrooms"].to_numpy() + rng.uniform(-0.2, 0.2, shown.height)
    # The renderer's near corner is the top of each floor axis; sqft runs the other way so it reads left to right and the plane's top faces the camera.
    points = np.column_stack([
        (sqft_hi - shown["building_sqft"].to_numpy()) / (sqft_hi - sqft_lo),
        (np.clip(beds, beds_lo, beds_hi) - beds_lo) / (beds_hi - beds_lo),
        shown["sale_price"].to_numpy(),
    ])

    def plane(beds_unit, sqft_unit):
        return (theta[0] + theta[1] * (sqft_hi - sqft_unit * (sqft_hi - sqft_lo))
                + theta[2] * (beds_lo + beds_unit * (beds_hi - beds_lo)))

    return barocas().surface_figure(
        plane, grid=10, z_fill=0.9, camera=(40.0, 20.0),
        labels=("Bedrooms", "Building sqft", "Sale price"),
        points=points, surface_opacity=0.8,
    )


# --------------------------------------------------------------------------
# Classification (Day 2): five two-feature, yes/no examples
# --------------------------------------------------------------------------
# Each example is fit and drawn in "plot space": skewed features are logged
# first, so a boundary drawn on the figure is the boundary the model learned.

CLASS_DATA = DATASETS / "classification-examples"
CLASS_EXAMPLES = ("universities", "spam", "penguins", "tumors", "cook-county")
YES_FILL = "#FDD5CA"   # light tint of ORANGE: region predicted "yes"
NO_FILL = "#E9E9E7"    # light neutral: region predicted "no"


def _log_ticks(values, fmt, offset=0.0):
    return [np.log10(v + offset) for v in values], [fmt(v) for v in values]


def _count(v):
    return f"{v / 1e3:g}k" if v >= 1e3 else f"{v:g}"


def cls_example(name: str) -> dict:
    """Features X (n x 2, plot space), labels y (True = the orange class), axis text."""
    key = f"cls-{name}"
    if key in _cache:
        return _cache[key]
    if name == "universities":
        df = pl.read_csv(CLASS_DATA / "college-scorecard.csv",
                         null_values=["NA", "NULL", "PrivacySuppressed"], infer_schema_length=None).filter(
            (pl.col("PREDDEG") == 3) & pl.col("CONTROL").is_in([1, 2])
            & (pl.col("UGDS") > 0) & (pl.col("TUITIONFEE_IN") > 0))
        X = np.column_stack([np.log10(df["UGDS"].to_numpy()), np.log10(df["TUITIONFEE_IN"].to_numpy())])
        uic = int(np.flatnonzero(df["UNITID"].to_numpy() == 145600)[0])
        ex = dict(X=X, y=(df["CONTROL"] == 1).to_numpy(), yes="Public", no="Private nonprofit",
                  xlabel="Undergraduate enrollment (log scale)", ylabel="In-state tuition and fees (log scale)",
                  xticks=_log_ticks([10, 100, 1_000, 10_000, 100_000], _count),
                  yticks=_log_ticks([1_000, 3_000, 10_000, 30_000, 60_000], lambda v: f"${_count(v)}"),
                  highlight=(X[uic], "UIC"), legend_loc="lower right")
    elif name == "spam":
        df = pl.read_csv(CLASS_DATA / "spambase.csv", infer_schema_length=None).sample(1200, seed=418)
        # Half the emails have no "!", so offset by 0.01 before logging.
        X = np.column_stack([np.log10(df["char_freq_!"].to_numpy() + 0.01),
                             np.log10(df["capital_run_length_average"].to_numpy())])
        ex = dict(X=X, y=(df["spam"] == 1).to_numpy(), yes="Spam", no="Not spam",
                  xlabel='"!" as a % of characters (log scale)',
                  ylabel="Average run of CAPITALS (log scale)",
                  xticks=_log_ticks([0, 0.1, 1, 10], lambda v: f"{v:g}%", offset=0.01),
                  yticks=_log_ticks([1, 3, 10, 30, 100], lambda v: f"{v:g}"))
    elif name == "penguins":
        df = pl.read_csv(CLASS_DATA / "penguins.csv", null_values="NA").filter(
            pl.col("species").is_in(["Adelie", "Gentoo"])
            & pl.col("bill_length_mm").is_not_null() & pl.col("bill_depth_mm").is_not_null())
        ex = dict(X=df.select("bill_length_mm", "bill_depth_mm").to_numpy(),
                  y=(df["species"] == "Gentoo").to_numpy(), yes="Gentoo", no="Adélie",
                  xlabel="Bill length (mm)", ylabel="Bill depth (mm)")
    elif name == "tumors":
        df = pl.read_csv(CLASS_DATA / "wdbc.csv")
        ex = dict(X=df.select("radius_mean", "texture_mean").to_numpy(),
                  y=(df["diagnosis"] == "M").to_numpy(), yes="Malignant", no="Benign",
                  xlabel="Mean radius of cell nuclei", ylabel="Mean texture of cell nuclei")
    elif name == "cook-county":
        df = pl.read_csv(CLASS_DATA / "cook-county-sales-density.csv", infer_schema_length=None).filter(
            (pl.col("property_group") == "Single-Family") & (~pl.col("is_multisale"))
            & (pl.col("sale_price") > 10_000) & pl.col("building_sqft").is_not_null()
            & (pl.col("land_sqft") > 0) & pl.col("housing_units_per_sq_mi").is_not_null()).sample(1000, seed=418)
        ex = dict(X=np.column_stack([np.log10(df["land_sqft"].to_numpy()),
                                     np.log10(df["housing_units_per_sq_mi"].to_numpy())]),
                  y=df["in_chicago"].to_numpy(), yes="Chicago", no="Suburban Cook County",
                  xlabel="Lot size, square feet (log scale)",
                  ylabel="Housing units per sq. mile in the tract (log scale)",
                  xticks=_log_ticks([1_000, 3_000, 10_000, 30_000, 100_000], _count),
                  yticks=_log_ticks([300, 1_000, 3_000, 10_000, 30_000], _count))
    else:
        raise KeyError(name)
    _cache[key] = ex
    return ex


def _cls_axes(ax, ex, *, labels=True):
    tidy(ax, grid="both")
    if "xticks" in ex:
        ax.set_xticks(*ex["xticks"])
    if "yticks" in ex:
        ax.set_yticks(*ex["yticks"])
    if labels:
        ax.set(xlabel=ex["xlabel"], ylabel=ex["ylabel"])


def _cls_points(ax, ex, size=22, legend=True, plain=False, highlight=True):
    X, y = ex["X"], ex["y"]
    if plain:  # the "before" frame: same points and axes, no labels revealed
        ax.scatter(*X.T, s=size, marker="o", color=MUTED, alpha=0.55, linewidths=0, zorder=3)
    else:
        # Shape doubles the color cue: circles for "no", triangles for "yes".
        ax.scatter(*X[~y].T, s=size, marker="o", color=MUTED, alpha=0.55, linewidths=0, label=ex["no"], zorder=3)
        ax.scatter(*X[y].T, s=size * 1.2, marker="^", color=ORANGE, alpha=0.7, linewidths=0, label=ex["yes"], zorder=3)
    if legend and not plain:
        ax.legend(loc=ex.get("legend_loc", "upper right"), frameon=True, facecolor=PAPER, edgecolor=BORDER, fontsize=12,
                  labelcolor=INK, markerscale=1.6)
    if highlight and "highlight" in ex:
        (hx, hy), text = ex["highlight"]
        ax.scatter([hx], [hy], s=size * 4, marker="o" if plain else "^", facecolor=MUTED if plain else ORANGE,
                   edgecolor=INK, linewidth=1.5, zorder=4)
        ax.annotate(text, (hx, hy), xytext=(10, -14), textcoords="offset points", color=INK, fontsize=13, zorder=4)


def _cls_regions(ax, model, ex, n=600):
    """Shade each region by the class the fitted model predicts there."""
    X = ex["X"]
    pad = 0.04 * (X.max(axis=0) - X.min(axis=0))
    (x0, y0), (x1, y1) = X.min(axis=0) - pad, X.max(axis=0) + pad
    gx, gy = np.meshgrid(np.linspace(x0, x1, n), np.linspace(y0, y1, n))
    z = model.predict(np.column_stack([gx.ravel(), gy.ravel()])).reshape(gx.shape).astype(float)
    ax.contourf(gx, gy, z, levels=[-0.5, 0.5, 1.5], colors=[NO_FILL, YES_FILL], zorder=1)
    ax.contour(gx, gy, z, levels=[0.5], colors=[INK], linewidths=1.2, zorder=2)
    ax.set(xlim=(x0, x1), ylim=(y0, y1))


def _cls_models():
    # scikit-learn is not in the slide venv; run with `uv run --with scikit-learn ...`.
    from sklearn.naive_bayes import GaussianNB
    from sklearn.neighbors import KNeighborsClassifier
    from sklearn.pipeline import make_pipeline
    from sklearn.preprocessing import StandardScaler
    from sklearn.svm import SVC
    from sklearn.tree import DecisionTreeClassifier
    # kNN and the SVM measure distance, so both get standardized features.
    return [
        ("Decision tree (depth 3)", DecisionTreeClassifier(max_depth=3, random_state=418)),
        ("Naive Bayes", GaussianNB()),
        ("k-nearest neighbors (k = 15)", make_pipeline(StandardScaler(), KNeighborsClassifier(n_neighbors=15))),
        ("Linear SVM", make_pipeline(StandardScaler(), SVC(kernel="linear", C=1.0))),
    ]


def _cls_scatter(name, plain=False, highlight=True):
    def build():
        ex = cls_example(name)
        fig, ax = new_fig(width=900)
        _cls_points(ax, ex, plain=plain, highlight=highlight)
        _cls_axes(ax, ex)
        return fig
    return build


def _cls_four(name):
    def build():
        ex = cls_example(name)
        fig, axes = new_fig(width=1400, height=400, ncols=4, sharex=True, sharey=True)
        for i, (ax, (title, model)) in enumerate(zip(axes, _cls_models())):
            model.fit(ex["X"], ex["y"])
            _cls_regions(ax, model, ex)
            _cls_points(ax, ex, size=8, legend=False)
            _cls_axes(ax, ex, labels=False)
            ax.set_title(title, color=INK, fontsize=14, loc="left")
            if i:
                ax.tick_params(labelleft=False)
        fig.supxlabel(ex["xlabel"], color=STEEL, fontsize=13)
        fig.supylabel(ex["ylabel"], color=STEEL, fontsize=13)
        fig.tight_layout()
        return fig
    return build


for _name in CLASS_EXAMPLES:
    figure(f"cls-{_name}-scatter")(_cls_scatter(_name))
    figure(f"cls-{_name}-scatter-plain")(_cls_scatter(_name, plain=True))
    figure(f"cls-{_name}-four-boundaries")(_cls_four(_name))
figure("cls-universities-scatter-plain-no-uic")(_cls_scatter("universities", plain=True, highlight=False))


@figure("cls-universities-line")
def cls_universities_line():
    """Least squares on a 0/1 response: the line runs past both 0 and 1."""
    ex = cls_example("universities")
    x, y = ex["X"][:, 0], ex["y"].astype(float)
    slope, intercept = np.polyfit(x, y, 1)
    rng = np.random.default_rng(418)
    fig, ax = new_fig(width=900)
    for value, color, marker in [(0, MUTED, "o"), (1, ORANGE, "^")]:
        m = y == value
        ax.scatter(x[m], y[m] + rng.uniform(-0.04, 0.04, m.sum()), s=18, marker=marker,
                   color=color, alpha=0.5, linewidths=0, zorder=3)
    xs = np.linspace(x.min(), x.max(), 200)
    ax.plot(xs, intercept + slope * xs, color=INK, linewidth=2.5, zorder=4)
    for level in (0, 1):
        ax.axhline(level, color=QUIET, linewidth=1, linestyle=(0, (4, 4)), zorder=2)
    lo, hi = intercept + slope * xs[0], intercept + slope * xs[-1]
    ax.annotate(f"predicts {lo:.2f}", (xs[0], lo), xytext=(4, 14), textcoords="offset points", color=INK, fontsize=14)
    ax.annotate(f"predicts {hi:.2f}", (xs[-1], hi), xytext=(-4, 14), textcoords="offset points",
                color=INK, fontsize=14, ha="right")
    tidy(ax, grid="both")
    ax.set_xticks(*ex["xticks"])
    ax.set_yticks([-0.5, 0, 0.5, 1], ["-0.5", "0 (private)", "0.5", "1 (public)"])
    ax.set(ylim=(-0.95, 1.35), xlabel=ex["xlabel"], ylabel="Public? (least squares fit)")
    return fig


@figure("cls-universities-boundary")
def cls_universities_boundary():
    ex = cls_example("universities")
    title, model = _cls_models()[3]
    model.fit(ex["X"], ex["y"])
    fig, ax = new_fig(width=900)
    _cls_regions(ax, model, ex)
    _cls_points(ax, ex)
    _cls_axes(ax, ex)
    return fig


# Penguin walk-through of training, validation, and test sets: 70/10/20,
# stratified by species so each set keeps the Adélie-to-Gentoo ratio.
PENGUIN_KS = (1, 15, 191)
PENGUIN_K = 15


def penguin_split() -> dict[str, dict]:
    if "penguin-split" not in _cache:
        from sklearn.model_selection import train_test_split
        ex = cls_example("penguins")
        X_rest, X_test, y_rest, y_test = train_test_split(ex["X"], ex["y"], test_size=0.2, random_state=418, stratify=ex["y"])
        X_train, X_val, y_train, y_val = train_test_split(X_rest, y_rest, test_size=0.125, random_state=418, stratify=y_rest)
        _cache["penguin-split"] = {name: {**ex, "X": X, "y": y} for name, X, y in [
            ("train", X_train, y_train), ("val", X_val, y_val), ("test", X_test, y_test)]}
    return _cache["penguin-split"]


def _knn(k):
    from sklearn.neighbors import KNeighborsClassifier
    from sklearn.pipeline import make_pipeline
    from sklearn.preprocessing import StandardScaler
    return make_pipeline(StandardScaler(), KNeighborsClassifier(n_neighbors=k))


def _hidden_points(ax, ex, size=22):
    """Held-out penguins whose species the model is not shown."""
    ax.scatter(*ex["X"].T, s=size, marker="o", facecolors="none", edgecolors=STEEL, linewidths=1, zorder=3)


def _same_limits(axes):
    X = cls_example("penguins")["X"]
    pad = 0.04 * (X.max(axis=0) - X.min(axis=0))
    for ax in axes:
        ax.set(xlim=(X[:, 0].min() - pad[0], X[:, 0].max() + pad[0]), ylim=(X[:, 1].min() - pad[1], X[:, 1].max() + pad[1]))


@figure("cls-penguins-split")
def cls_penguins_split():
    sets = penguin_split()
    fig, axes = new_fig(width=1200, height=420, ncols=3, sharex=True, sharey=True)
    titles = {"train": "Training set", "val": "Validation set", "test": "Test set"}
    for i, (ax, (name, ex)) in enumerate(zip(axes, sets.items())):
        if name == "train":
            _cls_points(ax, ex, size=14, legend=False)
            ax.legend(loc="lower left", frameon=True, facecolor=PAPER, edgecolor=BORDER, fontsize=11, labelcolor=INK, markerscale=1.4)
        else:
            _hidden_points(ax, ex, size=18)
        _cls_axes(ax, ex, labels=False)
        ax.set_title(f"{titles[name]}: {len(ex['y'])} penguins", color=INK, fontsize=14, loc="left")
        if i:
            ax.tick_params(labelleft=False)
    _same_limits(axes)
    ex = sets["train"]
    fig.supxlabel(ex["xlabel"], color=STEEL, fontsize=13)
    fig.supylabel(ex["ylabel"], color=STEEL, fontsize=13)
    fig.tight_layout()
    return fig


@figure("cls-penguins-validation")
def cls_penguins_validation():
    """kNN fit on the training set for three values of k, scored on the validation set."""
    sets = penguin_split()
    train, val = sets["train"], sets["val"]
    fig, axes = new_fig(width=1200, height=420, ncols=3, sharex=True, sharey=True)
    for i, (ax, k) in enumerate(zip(axes, PENGUIN_KS)):
        model = _knn(k).fit(train["X"], train["y"])
        correct = int((model.predict(val["X"]) == val["y"]).sum())
        _cls_regions(ax, model, cls_example("penguins"))
        _cls_points(ax, val, size=26, legend=False)
        _cls_axes(ax, val, labels=False)
        ax.set_title(f"k = {k}: {correct} of {len(val['y'])} correct", color=INK, fontsize=14, loc="left")
        print(f"    k = {k}: {correct} of {len(val['y'])} validation penguins correct")
        if i:
            ax.tick_params(labelleft=False)
    ex = train
    fig.supxlabel(ex["xlabel"], color=STEEL, fontsize=13)
    fig.supylabel(ex["ylabel"], color=STEEL, fontsize=13)
    fig.tight_layout()
    return fig


@figure("cls-penguins-test")
def cls_penguins_test():
    """The chosen k refit on training + validation, then scored once on the test set."""
    sets = penguin_split()
    train, val, test = sets["train"], sets["val"], sets["test"]
    model = _knn(PENGUIN_K).fit(np.vstack([train["X"], val["X"]]), np.concatenate([train["y"], val["y"]]))
    wrong = model.predict(test["X"]) != test["y"]
    fig, ax = new_fig(width=900)
    _cls_regions(ax, model, cls_example("penguins"))
    _cls_points(ax, test, size=30)
    if wrong.any():
        ax.scatter(*test["X"][wrong].T, s=260, facecolors="none", edgecolors=INK, linewidths=1.5, zorder=4)
    _cls_axes(ax, test)
    ax.set_title(f"k = {PENGUIN_K}: {int((~wrong).sum())} of {len(wrong)} test penguins correct", color=INK, fontsize=15, loc="left")
    print(f"    test: {int((~wrong).sum())} of {len(wrong)} correct")
    return fig


# Two new penguins, one easy vote and one close vote, for the kNN intuition slide.
KNN_QUERIES = ((45.0, 15.0), (45.0, 17.0))
KNN_INTUITION_K = 5


@figure("cls-penguins-knn-intuition")
def cls_penguins_knn_intuition():
    """Each new penguin's 5 nearest training penguins, measured on standardized features."""
    from matplotlib.patches import Ellipse
    train = penguin_split()["train"]
    X, y = train["X"], train["y"]
    sd = X.std(axis=0)
    fig, ax = new_fig(width=760, height=760)
    _cls_points(ax, train, size=46)
    for i, q in enumerate(np.array(KNN_QUERIES), start=1):
        dist = np.linalg.norm((X - q) / sd, axis=1)
        near = np.argsort(dist)[:KNN_INTUITION_K]
        for j in near:
            ax.plot([q[0], X[j, 0]], [q[1], X[j, 1]], color=INK, linewidth=1.2, zorder=2)
        r = dist[near].max() * 1.15
        # A circle in standardized units, which the axes' aspect makes look round.
        ax.add_patch(Ellipse(q, 2 * r * sd[0], 2 * r * sd[1], facecolor="none", edgecolor=INK, linewidth=1.2, linestyle=(0, (4, 3)), zorder=2))
        ax.scatter(*q, s=170, marker="o", facecolor=PAPER, edgecolor=INK, linewidth=2, zorder=5)
        ax.text(*q, str(i), color=INK, fontsize=11, ha="center", va="center", zorder=6)
        gentoo = int(y[near].sum())
        ax.annotate(f"{gentoo} of {KNN_INTUITION_K} Gentoo", q, xytext=(q[0] + r * sd[0] + 0.3, q[1]), color=INK, fontsize=14, va="center", bbox=dict(facecolor=PAPER, edgecolor="none", alpha=0.85, pad=2), zorder=6)
        print(f"    penguin {i} {tuple(q)}: {gentoo} of {KNN_INTUITION_K} nearest are Gentoo")
    _cls_axes(ax, train)
    # Equal standardized units on both axes, so distance on the page is the distance kNN uses.
    ax.set(xlim=(37, 53), ylim=(13.6, 19.4), aspect=sd[0] / sd[1])
    return fig


@figure("supervised-two-kinds")
def supervised_two_kinds():
    """Synthetic data: a line through numeric responses above, a boundary between two classes below."""
    rng = np.random.default_rng(418)
    fig, (top, bottom) = new_fig(width=480, height=640, nrows=2)

    x = rng.uniform(0, 10, 30)
    y = 2 + 0.8 * x + rng.normal(0, 1.2, x.size)
    slope, intercept = np.polyfit(x, y, 1)
    xs = np.array([0, 10])
    top.plot(xs, intercept + slope * xs, color=ORANGE, linewidth=2.6, zorder=2)
    top.scatter(x, y, s=34, color=INK, zorder=3, edgecolor=PAPER, linewidth=0.8)
    top.set_title("Regression: predict a number", color=INK, fontsize=15, loc="left")
    top.set(xlabel="Feature $x$", ylabel="Response $y$")

    n = 30
    yes = rng.normal([6.5, 3.5], 1.1, size=(n, 2))
    no = rng.normal([3.5, 6.5], 1.1, size=(n, 2))
    ex = dict(X=np.vstack([no, yes]), y=np.r_[np.zeros(n, bool), np.ones(n, bool)], yes="Class B", no="Class A")
    _title, model = _cls_models()[3]
    model.fit(ex["X"], ex["y"])
    _cls_regions(bottom, model, ex)
    _cls_points(bottom, ex, size=34, legend=False)
    bottom.set_title("Classification: predict a class", color=INK, fontsize=15, loc="left")
    bottom.set(xlabel="Feature $x_1$", ylabel="Feature $x_2$")

    for ax in (top, bottom):
        tidy(ax, grid=None)
        ax.set(xticks=[], yticks=[])
    fig.tight_layout(h_pad=1.6)
    return fig


# --------------------------------------------------------------------------

def main(argv: list[str]) -> None:
    if FONT_PATH.exists():
        font_manager.fontManager.addfont(str(FONT_PATH))
        plt.rcParams["font.family"] = font_manager.FontProperties(
            fname=str(FONT_PATH)).get_name()
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
