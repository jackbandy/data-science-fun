# NOTICE: This file was written by an LLM (Claude Opus 5.5) and has not yet been reviewed.
# Draws one swarm plot per estimates CSV in this folder and saves it as a PNG
# next to the CSV. The x-axis spans the full range of plotted estimates, padded
# out to round tick values. Where noted, the largest estimate(s) are left off
# the plot (and printed) so it doesn't flatten the rest; the median and n still
# include it. A vertical line marks the median, the statistic Galton
# used as the "vox populi" in 1907.

import math
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
from matplotlib.ticker import FuncFormatter

HERE = Path(__file__).parent

# (csv file, x-axis label, unit suffix for tick labels, how many of the largest estimates to leave off the plot)
PLOTS = [
    ("illinois-voter-turnout-estimates-2026.csv", "Estimated Illinois voter turnout, Nov 3, 2026", "%", 0),
    ("uic-halsted-boardings-estimates-2026.csv", "Estimated UIC-Halsted boardings, Aug 25, 2026", "", 1),
    ("cta-rail-boardings-estimates-2026.csv", "Estimated CTA rail boardings, Sep 7, 2026", "", 2),
]

GOLDEN = (1 + 5 ** 0.5) / 2
WIDTH = 8
SURFACE = "#fcfcfb"
SERIES = "#f9461c"  # UIC orange, $orange in docs/slides/shared/theme/uic-orange-reveal.scss
INK = "#0b0b0b"
INK_2 = "#52514e"
MUTED = "#898781"
GRID = "#e1e0d9"
# Vertical noise added to each dot after seaborn packs the swarm, in y data units
# (the swarm band spans +/-0.4). Seeded so the PNGs are reproducible.
JITTER_SD = 0.01
RNG = np.random.default_rng(1907)


def jitter_without_overlap(ax, coll):
    """Nudge each dot vertically by Gaussian noise, keeping a nudge only if the
    dot then clears every other dot. The swarm starts overlap-free and every
    accepted move keeps it so, so the result never overlaps."""
    xy = coll.get_offsets().copy()
    # Same collision radius seaborn's swarm uses: marker radius plus half the ring.
    radius = (np.sqrt(coll.get_sizes()[0]) / 2 + coll.get_linewidth()[0] / 2) * ax.figure.dpi / 72
    px = ax.transData.transform(xy)
    for i in RNG.permutation(len(xy)):
        y_new = np.clip(xy[i, 1] + RNG.normal(0, JITTER_SD), -0.4, 0.4)
        p_new = ax.transData.transform((xy[i, 0], y_new))
        others = np.delete(px, i, axis=0)
        if len(others) == 0 or np.min(np.hypot(*(others - p_new).T)) >= 2 * radius:
            xy[i, 1], px[i] = y_new, p_new
    coll.set_offsets(xy)


def nice_step(span, target_ticks=5):
    """Round span / target_ticks to 1, 2, 2.5, or 5 times a power of ten."""
    raw = span / target_ticks
    mag = 10 ** math.floor(math.log10(raw))
    for m in (1, 2, 2.5, 5, 10):
        if m * mag >= raw:
            return m * mag


def short_number(x, unit=""):
    """Format 1500 as 1.5k, 2000000 as 2M, etc."""
    for div, suffix in ((1e9, "B"), (1e6, "M"), (1e3, "k")):
        if abs(x) >= div:
            return f"{x / div:.3g}{suffix}{unit}"
    return f"{x:.3g}{unit}"


def plot(csv_name, xlabel, unit, n_drop):
    all_values = pd.read_csv(HERE / csv_name).iloc[:, 0].dropna()
    dropped = all_values.nlargest(n_drop)
    values = all_values.drop(dropped.index)
    if n_drop:
        print(f"{csv_name}: left off plot: {', '.join(f'{v:,.0f}' for v in dropped)}")
    step = nice_step(values.max() - values.min())
    lo = math.floor(values.min() / step) * step
    hi = math.ceil(values.max() / step) * step
    if unit == "%":
        lo, hi = max(lo, 0), min(hi, 100)
    median = all_values.median()

    fig, ax = plt.subplots(figsize=(WIDTH, WIDTH / GOLDEN), facecolor=SURFACE)
    ax.set_facecolor(SURFACE)
    sns.swarmplot(x=values, ax=ax, color=SERIES, size=5, linewidth=0.75, edgecolor=SURFACE)
    # Seaborn packs the swarm into +/-0.4 data units; trim the y-limits so that band
    # fills the plot height, and let dots at the axis ends draw past the edge.
    ax.set_ylim(0.42, -0.42)
    for coll in ax.collections:
        coll.set_clip_on(False)

    ax.axvline(median, color=INK_2, linewidth=1, zorder=0)
    ax.annotate(f"median {short_number(median, unit)}", xy=(median, 1), xycoords=("data", "axes fraction"),
                xytext=(0, 4), textcoords="offset points", ha="center", va="bottom", color=INK_2, fontsize=10)

    ax.set_xlim(lo, hi)
    ax.set_xticks(np.arange(lo, hi + step / 2, step))
    ax.xaxis.set_major_formatter(FuncFormatter(lambda x, _: short_number(x, unit)))
    ax.set_xlabel(f"{xlabel} (n = {len(all_values)})", color=INK, fontsize=11)

    ax.grid(axis="x", color=GRID, linewidth=1)
    ax.set_axisbelow(True)
    ax.tick_params(colors=MUTED, labelcolor=INK_2, left=False)
    for side in ("top", "right", "left"):
        ax.spines[side].set_visible(False)
    ax.spines["bottom"].set_color(MUTED)

    out = HERE / csv_name.replace(".csv", ".png")
    fig.tight_layout()
    # Seaborn lays out the swarm at draw time, so draw once, then swap its draw hook
    # back for matplotlib's and add noise to the settled y positions.
    fig.canvas.draw()
    for coll in ax.collections:
        del coll.draw
        jitter_without_overlap(ax, coll)
    fig.savefig(out, dpi=200, facecolor=SURFACE)
    plt.close(fig)
    print(f"wrote {out.name}")


if __name__ == "__main__":
    for args in PLOTS:
        plot(*args)
