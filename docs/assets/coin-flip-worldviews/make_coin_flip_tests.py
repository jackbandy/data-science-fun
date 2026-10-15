#!/usr/bin/env python3
"""Coin-flip hypothesis-test and randomness figures for the Week 7 slides.

The Week 2 coin (10 heads in 14 flips, see make_coin_flip_worldviews.py) as a hypothesis test: its null distribution and the power of 14 flips, plus a streaks figure for "what does random look like?"

NOTICE: this file was substantially drafted by an LLM coding system and has not yet been reviewed. Check every figure against the slide it illustrates.

Follows docs/assets/STYLE.md: golden-ratio canvases, grayscale neutrals with orange reserved for the focal element, horizontal y-axis labels, vendored Libre Franklin drawn as paths so each SVG is self-contained. Everything is exact binomial math or simulated with a fixed seed.

Usage:  python3 make_coin_flip_tests.py [name ...]
        (docs/slides/.venv has every dependency: numpy, scipy, matplotlib)
"""

from __future__ import annotations

import sys
from pathlib import Path

import matplotlib

matplotlib.use("Agg")

import itertools

import matplotlib.pyplot as plt
import numpy as np
from matplotlib import font_manager
from scipy import stats

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


def _flip_grid(ax, flips, title, *, annotate, streak=4):
    """Draw 100 flips as a 5 x 20 grid; annotated, it outlines every flip in a run of `streak` or more and states the run counts."""
    run_len = []
    start = 0
    for i in range(1, len(flips) + 1):
        if i == len(flips) or flips[i] != flips[start]:
            run_len += [i - start] * (i - start)
            start = i
    switches = sum(a != b for a, b in itertools.pairwise(flips))
    long_runs = sum(1 for i, n in enumerate(run_len) if n >= streak and (i == 0 or flips[i] != flips[i - 1]))
    for i, f in enumerate(flips):
        r, c = divmod(i, 20)
        in_streak = annotate and run_len[i] >= streak
        ax.add_patch(plt.Rectangle((c, -r), 0.86, 0.86, facecolor=ORANGE if f else BORDER, edgecolor=INK if in_streak else "none", linewidth=2.5 if in_streak else 0))
    label = f"{title}: {switches} switches, longest streak {max(run_len)}, {long_runs} streaks of {streak}+ (outlined)" if annotate else title
    ax.set_title(label, fontsize=15, color=INK, loc="left", pad=6)
    ax.set(xlim=(-0.2, 20), ylim=(-4.2, 1))
    ax.set_aspect("equal")
    ax.axis("off")


@figure("coin-null-distribution")
def coin_null_distribution():
    """Heads in 14 flips of a fair coin; the bars at least as extreme as 10 heads make up the two-sided p-value."""
    k = np.arange(15)
    pmf = stats.binom.pmf(k, 14, 0.5)
    extreme = (k >= 10) | (k <= 4)
    p = pmf[extreme].sum()
    fig, ax = new_fig()
    ax.bar(k, pmf, color=np.where(extreme, ORANGE, QUIET), width=0.8, zorder=3)
    ax.annotate("observed:\n10 heads", xy=(10, pmf[10] + 0.004), xytext=(11.6, 0.15), color=INK, fontsize=14, ha="center", arrowprops={"arrowstyle": "-", "color": STEEL, "lw": 1})
    ax.text(0.02, 0.97, f"If $H_0$ (fair coin) is true,\nP(this extreme or more) = {p:.2f}", transform=ax.transAxes, color=ORANGE_DARK, fontsize=15, va="top")
    ax.set(xticks=k, xlabel="Number of heads in 14 flips", ylabel="Probability if the coin is fair")
    tidy(ax)
    return fig


@figure("power-coin")
def power_coin():
    """How often a two-sided binomial test at alpha = .05 rejects 'fair' for a coin that lands heads 70% of the time."""
    ns = np.arange(5, 151)
    power = []
    for n in ns:
        k = np.arange(n + 1)
        pvals = np.array([stats.binomtest(int(i), int(n), 0.5).pvalue for i in k])
        power.append(stats.binom.pmf(k, n, 0.7)[pvals < 0.05].sum())
    power = np.array(power)
    fig, ax = new_fig()
    ax.plot(ns, power, color=ORANGE, linewidth=3, zorder=3)
    p14 = power[ns == 14][0]
    ax.scatter([14], [p14], color=INK, s=50, zorder=4)
    ax.annotate(f"14 flips: rejects only {p14:.0%} of the time", xy=(14, p14), xytext=(30, 0.12), color=INK, fontsize=14, arrowprops={"arrowstyle": "-", "color": STEEL, "lw": 1})
    ax.axhline(0.8, color=STEEL, linewidth=1, linestyle=(0, (4, 4)))
    ax.text(150, 0.82, "80% power", color=STEEL, fontsize=13, ha="right")
    ax.set(ylim=(0, 1.02), xlim=(0, 152), xlabel="Number of flips", ylabel="Power: P(reject $H_0$)")
    ax.yaxis.set_major_formatter(lambda v, _: f"{v:.0%}")
    ax.set_title("A coin that lands heads 70% of the time", fontsize=16, color=INK, loc="left", pad=10)
    tidy(ax)
    return fig


def _streaks(annotate):
    """100 fair coin flips beside 100 made-up 'flips' written the way people tend to: switching too often and never repeating more than three times."""
    rng = np.random.default_rng(SEED)
    fair = rng.integers(0, 2, 100)
    switchy = [int(rng.integers(0, 2))]
    for _ in range(99):
        too_long = len(switchy) >= 3 and switchy[-1] == switchy[-2] == switchy[-3]
        switchy.append(1 - switchy[-1] if too_long or rng.random() < 0.7 else switchy[-1])
    fig, axes = new_fig(height=560, nrows=2)
    _flip_grid(axes[0], list(switchy), "Sequence A", annotate=annotate)
    _flip_grid(axes[1], list(fair), "Sequence B", annotate=annotate)
    fig.subplots_adjust(hspace=0.25)
    return fig


@figure("streaks-plain")
def streaks_plain():
    """The two sequences with no hints, for asking which one is random."""
    return _streaks(annotate=False)


@figure("streaks")
def streaks():
    """The same two sequences with switches and long streaks marked, for the answer."""
    return _streaks(annotate=True)


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
