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
# Provisional-turnout model: sd of the remaining-vote estimate, as a fraction of it (chosen by the instructor; no published error rate was found).
REMAINING_SD = 0.25
ACTUAL_Y = 0.65  # y position of the range row, below the swarm band (the y-axis is inverted)


def turnout_range(n_draws=1_000_000):
    """Provisional 2026 Illinois VEP turnout from results.csv: (counted + remaining governor votes) x ballots-per-governor-vote ratio / VEP.
    Remaining ~ Normal(estimate, REMAINING_SD * estimate) clipped at 0; ratio ~ Uniform between the 2022 and 2018 values. Extremes are counted votes only (low) and twice the remaining estimate at the larger ratio (high)."""
    r = pd.read_csv(HERE / "results.csv").set_index(["year", "measure"])["value"]
    vep = r[2026, "il_voting_eligible_population"]
    counted = r[2026, "il_governor_votes_counted"]
    remaining = r[2026, "il_governor_votes_remaining_est"]
    ratios = sorted([r[2022, "il_total_ballots_counted"] / r[2022, "il_governor_votes_total"], r[2018, "il_total_ballots_counted"] / r[2018, "il_vote_for_highest_office"]])
    rng = np.random.default_rng(2026)  # own generator, so the swarm jitter in the other PNGs is unchanged
    draws = np.clip(rng.normal(remaining, REMAINING_SD * remaining, n_draws), 0, None)
    turnout = 100 * (counted + draws) * rng.uniform(*ratios, n_draws) / vep
    return {
        "extremes": (100 * counted / vep, 100 * (counted + 2 * remaining) * ratios[1] / vep),
        "p95": tuple(np.percentile(turnout, [2.5, 97.5])),
        "p50": tuple(np.percentile(turnout, [25, 75])),
        "center": np.median(turnout),
    }


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


def plot(csv_name, xlabel, unit, n_drop, actual=None, out_name=None):
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
    ax.set_ylim(0.42 if actual is None else ACTUAL_Y + 0.2, -0.42)
    for coll in ax.collections:
        coll.set_clip_on(False)

    if actual is None:
        ax.axvline(median, color=INK_2, linewidth=1, zorder=0)
        ax.annotate(f"median {short_number(median, unit)}", xy=(median, 1), xycoords=("data", "axes fraction"),
                    xytext=(0, 4), textcoords="offset points", ha="center", va="bottom", color=INK_2, fontsize=10)
    else:
        ax.plot([median, median], [-0.42, 0.35], color=INK_2, linewidth=1, zorder=0)  # a Line2D, since the jitter pass below treats every collection as dots
        ax.annotate(f"class median {short_number(median, unit)} (n = {len(all_values)})", xy=(median, 1), xycoords=("data", "axes fraction"),
                    xytext=(0, 4), textcoords="offset points", ha="center", va="bottom", color=INK_2, fontsize=10)
        if "value" in actual:
            ax.plot([actual["value"]], [ACTUAL_Y], marker="D", markersize=7, color=INK, clip_on=False)
            ax.annotate(actual["label"], xy=(actual["value"], ACTUAL_Y), xytext=(0, 9),
                        textcoords="offset points", ha="center", va="bottom", color=INK, fontsize=10)
        else:
            for (x0, x1), lw in ((actual["extremes"], 1), (actual["p95"], 4), (actual["p50"], 9)):
                ax.plot([x0, x1], [ACTUAL_Y, ACTUAL_Y], color=INK, linewidth=lw, solid_capstyle="butt", clip_on=False)
            ax.annotate(f"actual turnout, provisional: {actual['center']:.1f}%", xy=(actual["center"], ACTUAL_Y), xytext=(0, 9),
                        textcoords="offset points", ha="center", va="bottom", color=INK, fontsize=10)
            ax.annotate(f"full range {actual['extremes'][0]:.1f}–{actual['extremes'][1]:.1f}%, thick 95% interval, thickest 50%",
                        xy=(actual["center"], ACTUAL_Y), xytext=(0, -9), textcoords="offset points", ha="center", va="top", color=INK_2, fontsize=8.5)

    ax.set_xlim(lo, hi)
    ax.set_xticks(np.arange(lo, hi + step / 2, step))
    ax.xaxis.set_major_formatter(FuncFormatter(lambda x, _: short_number(x, unit)))
    ax.set_xlabel(xlabel if actual else f"{xlabel} (n = {len(all_values)})", color=INK, fontsize=11)

    ax.grid(axis="x", color=GRID, linewidth=1)
    ax.set_axisbelow(True)
    ax.tick_params(colors=MUTED, labelcolor=INK_2, left=False)
    for side in ("top", "right", "left"):
        ax.spines[side].set_visible(False)
    ax.spines["bottom"].set_color(MUTED)

    out = HERE / (out_name or csv_name.replace(".csv", ".png"))
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
    actual = turnout_range()
    print("provisional turnout:", {k: np.round(v, 2) for k, v in actual.items()})
    plot(*PLOTS[0], actual=actual, out_name="illinois-voter-turnout-estimates-and-actual-2026.png")
    rides = pd.read_csv(HERE / "results.csv").set_index(["year", "measure"])["value"][2026, "uic_halsted_rides_2026_08_25"]
    plot(*PLOTS[1], actual={"value": rides, "label": f"actual: {rides:,.0f} rides"}, out_name="uic-halsted-boardings-estimates-and-actual-2026.png")
