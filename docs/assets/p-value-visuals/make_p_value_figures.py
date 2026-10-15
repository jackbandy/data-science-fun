#!/usr/bin/env python3
"""p-value figures for the Week 7, Day 1 hypothesis testing slides.

NOTICE: this file was substantially drafted by an LLM coding system and has not yet been reviewed. Check every figure against the slide it illustrates.

Follows docs/assets/STYLE.md and mirrors week8/make_week8_figures.py: golden-ratio canvases, grayscale neutrals with orange reserved for the focal element, horizontal y-axis labels, vendored Libre Franklin drawn as paths so each SVG is self-contained.

Data (see SOURCES.md in this folder):
  * resume-permutation reads datasets/resume-audit-bertrand-mullainathan/.
  * Everything else is simulated with a fixed seed or is plain math.

Usage:  python3 make_p_value_figures.py [name ...]
        (docs/slides/.venv has every dependency: numpy, scipy, polars, matplotlib)
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
from scipy import stats

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
ORANGE_DARK = "#C83214"

PHI = (1 + 5**0.5) / 2
WIDTH_PX = 1000
DPI = 100
SEED = 418

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
    ax.tick_params(colors=STEEL, labelsize=12, length=0)
    for lbl in (ax.xaxis.label, ax.yaxis.label):
        lbl.set_color(STEEL)
        lbl.set_fontsize(14)
    return ax


def horizontal_ylabels(fig):
    """STYLE.md: y-axis labels run horizontally across the top of the axis, and any title moves up to clear them."""
    for ax in fig.axes:
        label = ax.yaxis.label
        # A label the figure already turned horizontal (e.g. row labels in a small-multiples grid) keeps its own placement.
        if not label.get_text().strip() or label.get_rotation() == 0 or ax.name != "rectilinear" or ax.get_label() == "<colorbar>":
            continue
        right = ax.yaxis.get_label_position() == "right"
        label.set(rotation=0, ha="right" if right else "left", va="bottom")
        ax.yaxis.set_label_coords(1 if right else 0, 1.025)
        pad = max(30, ax.titleOffsetTrans.get_matrix()[1, 2] * 72 / fig.dpi)
        for loc, title in (("left", ax._left_title), ("center", ax.title), ("right", ax._right_title)):
            if title.get_text():
                ax.set_title(title.get_text(), loc=loc, pad=pad, fontsize=title.get_fontsize(), color=title.get_color(), fontweight=title.get_fontweight())


def save(fig, name):
    out = OUT_DIR / f"{name}.svg"
    horizontal_ylabels(fig)
    fig.savefig(out, format="svg", facecolor=PAPER, bbox_inches="tight", pad_inches=0.12)
    plt.close(fig)
    print(f"  wrote {out.relative_to(REPO_ROOT)}")


def welch(a, b):
    """Difference in means, its 95% CI, and the two-sided Welch p-value."""
    diff = a.mean() - b.mean()
    va, vb = a.var(ddof=1) / len(a), b.var(ddof=1) / len(b)
    se = np.sqrt(va + vb)
    df = (va + vb) ** 2 / (va**2 / (len(a) - 1) + vb**2 / (len(b) - 1))
    half = stats.t.ppf(0.975, df) * se
    p = 2 * stats.t.sf(abs(diff) / se, df)
    return diff, diff - half, diff + half, p


# Shared setup for the dance: two groups of 32, true difference 10, SD 20 (a "medium" effect of d = 0.5).
DANCE_N, DANCE_DIFF, DANCE_SD = 32, 10, 20


def dance_replications(reps, rng):
    out = []
    for _ in range(reps):
        a = rng.normal(50 + DANCE_DIFF, DANCE_SD, DANCE_N)
        b = rng.normal(50, DANCE_SD, DANCE_N)
        out.append(welch(a, b))
    return np.array(out)


@figure("z-test-tail")
def z_test_tail():
    """The battery-life z-test: the left tail beyond z = -0.555 is the p-value; the alpha = .05 cutoff sits much further out."""
    z_obs, z_crit = -0.555, stats.norm.ppf(0.05)
    x = np.linspace(-3.5, 3.5, 500)
    fig, ax = new_fig()
    ax.plot(x, stats.norm.pdf(x), color=INK, linewidth=2, zorder=3)
    left = x <= z_obs
    ax.fill_between(x[left], stats.norm.pdf(x[left]), color=ORANGE, alpha=0.85, zorder=2)
    ax.axvline(z_crit, color=STEEL, linewidth=1.2, linestyle=(0, (4, 4)))
    ax.text(z_crit - 0.08, 0.36, "$\\alpha$ = .05 cutoff\nz = −1.645", color=STEEL, fontsize=13, ha="right", va="top")
    ax.annotate(f"p = P(Z ≤ {z_obs}) ≈ {stats.norm.cdf(z_obs):.3f}", xy=(-1.0, 0.1), xytext=(-3.4, 0.24), color=ORANGE_DARK, fontsize=15, arrowprops={"arrowstyle": "-", "color": ORANGE_DARK, "lw": 1})
    ax.text(z_obs + 0.1, 0.355, f"observed\nz = {z_obs}", color=INK, fontsize=13, va="top")
    ax.axvline(z_obs, color=INK, linewidth=1)
    ax.set(ylim=(0, 0.42), yticks=[], xlabel="z, if the true mean battery life is 7.8 hours")
    tidy(ax, grid=None, spines=("bottom",))
    return fig


@figure("resume-permutation")
def resume_permutation():
    """Shuffle the race labels 10,000 times; the observed callback gap sits far outside every shuffled gap."""
    df = pl.read_csv(DATASETS / "resume-audit-bertrand-mullainathan" / "resume.csv")
    y = df["received_callback"].to_numpy().astype(float)
    white = (df["race"] == "white").to_numpy()
    observed = y[white].mean() - y[~white].mean()
    rng = np.random.default_rng(SEED)
    null = np.empty(10_000)
    for i in range(len(null)):
        s = rng.permutation(white)
        null[i] = y[s].mean() - y[~s].mean()
    fig, ax = new_fig()
    # The gap moves in steps of 2/2435 points, so bins span whole steps to avoid aliasing spikes.
    step = 100 * 2 / white.sum()
    ax.hist(null * 100, bins=np.arange(-40.5, 41.5, 3) * step, color=QUIET, zorder=3)
    ax.axvline(observed * 100, color=ORANGE, linewidth=3, zorder=4)
    ax.text(observed * 100 - 0.1, ax.get_ylim()[1] * 0.95, f"observed gap\n{observed * 100:.1f} points", color=ORANGE_DARK, fontsize=15, ha="right", va="top")
    ax.text(-2.3, ax.get_ylim()[1] * 0.95, "gaps from 10,000\nshuffles of the\nname labels", color=STEEL, fontsize=13, va="top")
    ax.set(xlabel="Callback rate, white-sounding minus Black-sounding names (percentage points)", ylabel="Shuffles", xlim=(-2.5, 3.8))
    tidy(ax)
    return fig


@figure("significance-vs-size")
def significance_vs_size():
    """Two hypothetical studies: a tiny effect measured precisely, and a large effect measured noisily."""
    studies = [
        ("Study A: 200,000 people", 0.5, 0.2),
        ("Study B: 30 people", 12.0, 8.0),
    ]
    fig, ax = new_fig(height=420)
    for i, (label, est, se) in enumerate(studies):
        lo, hi = est - 1.96 * se, est + 1.96 * se
        p = 2 * stats.norm.sf(est / se)
        color = ORANGE if p < 0.05 else STEEL
        ax.plot([lo, hi], [i, i], color=color, linewidth=3, zorder=3)
        ax.scatter([est], [i], color=color, s=80, zorder=4)
        ax.text(-9.5, i + 0.22, label, color=INK, fontsize=15)
        ax.text(hi + 0.6, i, f"p {'< .001' if p < 0.001 else f'= {p:.2f}'}", color=color, fontsize=15, va="center")
    ax.axvline(0, color=INK, linewidth=1, linestyle=(0, (4, 4)))
    ax.text(0.3, 1.55, "no effect", color=STEEL, fontsize=13)
    ax.set(ylim=(-0.6, 1.8), yticks=[], xlim=(-10, 33), xlabel="Estimated effect with 95% confidence interval (hypothetical units)")
    tidy(ax, grid="x", spines=("bottom",))
    return fig


@figure("dance-of-p-values")
def dance_of_p_values():
    """25 replications of the same two-group experiment, after Geoff Cumming's 'dance of the p values'."""
    rng = np.random.default_rng(SEED)
    reps = dance_replications(25, rng)
    fig, ax = new_fig(height=700)
    for i, (diff, lo, hi, p) in enumerate(reps):
        y = len(reps) - i
        color = ORANGE if p < 0.05 else STEEL
        ax.plot([lo, hi], [y, y], color=color, linewidth=2, zorder=3)
        ax.scatter([diff], [y], color=color, s=30, zorder=4)
        label = "< .001" if p < 0.001 else f"{p:.3f}".lstrip("0")
        ax.text(34, y, label, color=color, fontsize=12, va="center", ha="right")
    ax.axvline(0, color=INK, linewidth=1)
    ax.axvline(DANCE_DIFF, color=STEEL, linewidth=1, linestyle=(0, (4, 4)))
    ax.text(DANCE_DIFF, len(reps) + 1.2, "true difference", color=STEEL, fontsize=13, ha="center")
    ax.text(0, len(reps) + 1.2, "$H_0$", color=INK, fontsize=13, ha="center")
    ax.text(34, len(reps) + 1.2, "p", color=INK, fontsize=13, ha="right")
    ax.set(ylim=(0.2, len(reps) + 2), yticks=[], xlim=(-15, 35), xlabel="Difference in means with 95% CI (n = 32 per group)")
    tidy(ax, grid="x", spines=("bottom",))
    return fig


@figure("p-value-distributions")
def p_value_distributions():
    """Where p-values land over 10,000 replications, with no effect and with the dance's medium effect."""
    rng = np.random.default_rng(SEED)
    null_p = [stats.ttest_ind(rng.normal(50, DANCE_SD, DANCE_N), rng.normal(50, DANCE_SD, DANCE_N), equal_var=False).pvalue for _ in range(10_000)]
    real_p = dance_replications(10_000, rng)[:, 3]
    bins = np.linspace(0, 1, 21)
    fig, axes = new_fig(height=440, ncols=2, sharey=True)
    for ax, ps, title in [(axes[0], null_p, "No effect ($H_0$ true)"), (axes[1], real_p, "Medium effect (d = 0.5)")]:
        counts, _, patches = ax.hist(ps, bins=bins, color=QUIET, zorder=3)
        patches[0].set_facecolor(ORANGE)
        share = np.mean(np.array(ps) < 0.05)
        ax.text(0.1, counts.max() * 0.9 if ax is axes[1] else 4200, f"{share:.0%} of p-values < .05", color=ORANGE_DARK, fontsize=14)
        ax.set_title(title, fontsize=16, color=INK, loc="left", pad=10)
        ax.set_xlabel("p-value")
        tidy(ax)
    axes[0].set_ylabel("Replications (of 10,000)")
    fig.subplots_adjust(wspace=0.08)
    return fig


@figure("two-replications")
def two_replications():
    """Two hypothetical studies of the same effect: one 'significant', one not, with heavily overlapping intervals."""
    studies = [("Study 1", 8.0, 3.6), ("Study 2", 5.0, 4.8)]
    fig, ax = new_fig(height=420)
    for i, (label, est, se) in enumerate(studies):
        lo, hi = est - 1.96 * se, est + 1.96 * se
        p = 2 * stats.norm.sf(est / se)
        color = ORANGE if p < 0.05 else STEEL
        y = 1 - i
        ax.plot([lo, hi], [y, y], color=color, linewidth=3, zorder=3)
        ax.scatter([est], [y], color=color, s=80, zorder=4)
        ax.text(-12.5, y, label, color=INK, fontsize=15, va="center")
        ax.text(hi + 0.8, y, f"p = {p:.2f}", color=color, fontsize=15, va="center")
    ax.axvline(0, color=INK, linewidth=1, linestyle=(0, (4, 4)))
    ax.text(0.3, 1.5, "no effect", color=STEEL, fontsize=13)
    ax.set(ylim=(-0.6, 1.8), yticks=[], xlim=(-13, 24), xlabel="Estimated effect with 95% confidence interval (hypothetical units)")
    tidy(ax, grid="x", spines=("bottom",))
    return fig


@figure("many-tests")
def many_tests():
    """Chance of at least one p < .05 across k independent tests when every null hypothesis is true."""
    k = np.arange(1, 41)
    risk = 1 - 0.95**k
    fig, ax = new_fig()
    ax.plot(k, risk, color=ORANGE, linewidth=3, zorder=3)
    ax.scatter([1, 20], [risk[0], risk[19]], color=INK, s=50, zorder=4)
    ax.annotate("1 test: 5%", xy=(1, risk[0]), xytext=(4, 0.03), color=INK, fontsize=14)
    ax.annotate(f"20 tests: {risk[19]:.0%}", xy=(20, risk[19]), xytext=(22, 0.5), color=INK, fontsize=14, arrowprops={"arrowstyle": "-", "color": STEEL, "lw": 1})
    ax.set(ylim=(0, 1), xlim=(0, 41), xlabel="Number of independent tests (no real effects anywhere)", ylabel="P(at least one p < .05)")
    ax.yaxis.set_major_formatter(lambda v, _: f"{v:.0%}")
    tidy(ax)
    return fig


def main(argv: list[str]) -> None:
    if FONT_PATH.exists():
        font_manager.fontManager.addfont(str(FONT_PATH))
        plt.rcParams["font.family"] = font_manager.FontProperties(fname=str(FONT_PATH)).get_name()
    # Text as paths, per STYLE.md: the SVG stays self-contained.
    plt.rcParams["svg.fonttype"] = "path"

    wanted = argv or list(FIGURES)
    unknown = [name for name in wanted if name not in FIGURES]
    if unknown:
        raise SystemExit(f"unknown figure(s): {', '.join(unknown)}\navailable: {', '.join(FIGURES)}")
    print(f"writing {len(wanted)} figure(s) to {OUT_DIR.relative_to(REPO_ROOT)}")
    for name in wanted:
        save(FIGURES[name](), name)


if __name__ == "__main__":
    main(sys.argv[1:])
