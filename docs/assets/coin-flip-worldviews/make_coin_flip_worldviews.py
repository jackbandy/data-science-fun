#!/usr/bin/env python3
"""Bayesian vs. frequentist estimates of a coin's bias, flip by flip.

Recreates the setup from Panos Ipeirotis, "Are you a Bayesian or a Frequentist?
(Or Bayesian Statistics 101)" (2008):
https://www.behind-the-enemy-lines.com/2008/01/are-you-bayesian-or-frequentist-or.html

14 flips come up 10 heads / 4 tails, and the question is whether to bet on the
*next two* flips both coming up heads. The two worldviews land in different
places:

  frequentist (maximum likelihood)  p = h / n           = 10/14 = 71.4%
  Bayesian (Beta(1,1) prior)        p = (h+1) / (n+2)   = 11/16 = 68.75%

...and that gap is enough to flip the bet: 0.714^2 = 51% (take it) versus the
posterior-predictive 48.5% (pass). The figure plots both estimates after every
flip, so the shape of the disagreement is visible: the frequentist estimate
lurches (100% heads after one heads), the Bayesian estimate is dragged toward
the uniform prior and settles in more slowly. Ticks 15 and 16 stay empty --
those are the two flips being bet on.

Emits a build sequence for the slides (see VARIANTS): an empty chart, the prior
alone, the first three flips one at a time, then all 14. The axes, the coin
tokens, and the two series labels sit in the same place in every frame, so
nothing jumps between slides -- only the data fills in.

The post does not give a flip order, only the 10/4 total; the order below is
chosen to open with heads, which is where the two lines differ most.

This script was substantially drafted by an LLM coding system.
"""

from __future__ import annotations

from pathlib import Path

import matplotlib

matplotlib.use("Agg")

import matplotlib.patheffects as path_effects
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import font_manager
from matplotlib.transforms import blended_transform_factory

OUT_DIR = Path(__file__).resolve().parent
REPO_ROOT = OUT_DIR.parents[2]
STEM = "coin-flip-worldviews"
FONT_PATH = OUT_DIR.parent / "fonts" / "libre-franklin" / "LibreFranklin-Regular.ttf"

# STYLE.md palette
INK = "#1A1A1A"
STEEL = "#565A5C"
QUIET = "#AAAAAA"
BORDER = "#DDDDDD"
NEUTRAL_FILL = "#EEEEEE"
SOFT_GRAY = "#F4F4F2"
PAPER = "#FFFFFF"

# The two series read as one dark / one light gray, and are told apart three
# ways over (dark vs. light, solid vs. dashed, circle vs. square) so the figure
# survives grayscale printing and the projector in the back of the room.
BAYES_GRAY = INK
FREQ_GRAY = "#9BA0A2"  # steel, lightened

PHI = (1 + 5**0.5) / 2
WIDTH_PX = 1000
HEIGHT_PX = round(WIDTH_PX / PHI)
DPI = 100

# 10 heads, 4 tails, in the order they land.
FLIPS = "HHTHHHHTHHTHHT"
N_BLANK = 2  # the two flips being bet on: x = 15, 16

# Beta(1,1) = uniform prior, i.e. "the coin could be anything".
PRIOR_ALPHA = 1.0
PRIOR_BETA = 1.0

# Build sequence: (filename suffix, flips revealed). -1 = nothing at all,
# 0 = the prior and nothing else.
VARIANTS = (
    ("blank", -1),
    ("flip0", 0),
    ("flip1", 1),
    ("flip2", 2),
    ("flip3", 3),
    (f"flip{len(FLIPS)}", len(FLIPS)),
)

# The frequentist has nothing to say until a flip has landed, so its label waits
# for one.
FREQ_LABEL_FROM = 1


def _use_repo_font() -> str | None:
    """Register the vendored Libre Franklin; return its family name, else None.

    Reads the .ttf rather than the .woff2 beside it: the woff2 is for the web
    slides, and matplotlib cannot decode woff2 without brotli.
    """
    if not FONT_PATH.exists():
        return None
    font_manager.fontManager.addfont(str(FONT_PATH))
    return font_manager.FontProperties(fname=str(FONT_PATH)).get_name()


def estimates(flips: str) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    """Per-flip estimates, with index 0 = before any data.

    Returns (x, frequentist, bayesian). The frequentist entry at x=0 is NaN:
    h/n is undefined with no flips, which is the whole point of the contrast.
    """
    heads = np.cumsum([f == "H" for f in flips])
    n = np.arange(1, len(flips) + 1)

    x = np.arange(len(flips) + 1)
    freq = np.concatenate([[np.nan], heads / n])
    bayes = np.concatenate(
        [
            [PRIOR_ALPHA / (PRIOR_ALPHA + PRIOR_BETA)],
            (heads + PRIOR_ALPHA) / (n + PRIOR_ALPHA + PRIOR_BETA),
        ]
    )
    return x, freq, bayes


def two_heads_bayes(flips: str) -> float:
    """Posterior-predictive P(next two flips are both heads).

    Not the posterior mean squared: p is a random variable, so the answer is
    E[p^2] under the Beta posterior, which is a/(a+b) * (a+1)/(a+b+1) -- the
    second flip updates on the first. With Beta(11,5): 11/16 * 12/17 = 48.5%,
    against the frequentist's 0.714^2 = 51%, which is what flips the bet.
    """
    a = PRIOR_ALPHA + flips.count("H")
    b = PRIOR_BETA + flips.count("T")
    return (a / (a + b)) * ((a + 1) / (a + b + 1))


def _draw_flip_tokens(ax, x_max: int, n_shown: int) -> None:
    """Draw the flip outcomes as circled H/T tokens under their ticks.

    Coins are round, so the tokens are too: STYLE.md's diagram primitives give
    heads the highlight fill (dark, white text) and tails the neutral fill.
    Every flip not yet revealed is an empty hairline circle with a "?", so the
    row keeps its full width across the whole build.
    """
    tf = blended_transform_factory(ax.transData, ax.transAxes)
    y = -0.105  # axes fraction: below the numeric tick labels

    if n_shown >= 0:
        ax.text(
            0, y, "prior", transform=tf, ha="center", va="center",
            fontsize=11, color=QUIET, clip_on=False,
        )
    for i in range(1, x_max + 1):
        if i <= n_shown:
            heads = FLIPS[i - 1] == "H"
            ax.text(
                i, y, FLIPS[i - 1], transform=tf, ha="center", va="center",
                fontsize=12, color=PAPER if heads else INK, clip_on=False,
                bbox=dict(
                    boxstyle="circle,pad=0.34",
                    facecolor="#222222" if heads else NEUTRAL_FILL,
                    edgecolor="#222222" if heads else BORDER,
                    linewidth=1.4,
                ),
            )
        else:
            ax.text(
                i, y, "?", transform=tf, ha="center", va="center",
                fontsize=12, color=QUIET, clip_on=False,
                bbox=dict(
                    boxstyle="circle,pad=0.34",
                    facecolor=PAPER,
                    edgecolor=QUIET,
                    linewidth=0.6,  # hairline: present, but not a result yet
                ),
            )


def build_figure(n_shown: int):
    """One frame of the build: the prior plus `n_shown` flips (-1 = empty)."""
    x, freq, bayes = estimates(FLIPS)
    x_max = len(FLIPS) + N_BLANK

    fig, ax = plt.subplots(figsize=(WIDTH_PX / DPI, HEIGHT_PX / DPI), dpi=DPI)
    fig.patch.set_facecolor(PAPER)
    ax.set_facecolor(PAPER)

    ax.set_xlim(-0.6, x_max + 0.6)
    ax.set_ylim(0, 1.05)

    # The two flips being bet on: no data there, ever.
    ax.axvspan(
        len(FLIPS) + 0.5, x_max + 0.6, color=SOFT_GRAY, zorder=0, linewidth=0
    )
    ax.text(
        len(FLIPS) + 1.5, 0.06, "the bet",
        ha="center", va="bottom", fontsize=12, color=QUIET,
    )

    # 50% reference: a fair coin, and where the uniform prior starts.
    ax.axhline(0.5, color=BORDER, linewidth=1.0, zorder=1)

    # `n_shown + 1` covers index 0 (the prior) plus the flips revealed so far.
    if n_shown >= 0:
        cut = n_shown + 1
        ax.plot(
            x[:cut], freq[:cut],
            color=FREQ_GRAY, linewidth=2.5, linestyle=(0, (4, 2.5)),
            marker="s", markersize=6, zorder=3,
        )
        ax.plot(
            x[:cut], bayes[:cut],
            color=BAYES_GRAY, linewidth=2.5, marker="o", markersize=6, zorder=4,
        )

    # Direct labels instead of a legend, fixed in place across the build: both
    # tucked against the y-axis, left-aligned at the same x so the two labels
    # read as a stack. Two lines rather than one keeps the frequentist label
    # clear of its own line, which crosses that band between flips 2 and 3.
    if n_shown >= FREQ_LABEL_FROM:
        ax.text(
            -0.4, 0.875, "Frequentist\n(h / n)",
            ha="left", va="center", fontsize=14, color=STEEL, linespacing=1.3,
        )
    if n_shown >= 0:
        # Only the regular weight of Libre Franklin is vendored, so `fontweight`
        # would silently do nothing; a thin stroke in the text color is the
        # faux-bold that actually renders.
        ax.text(
            -0.4, 0.40, "Bayesian\n((h + 1) / (n + 2))",
            ha="left", va="top", fontsize=15, color=BAYES_GRAY,
            path_effects=[path_effects.withStroke(linewidth=0.9, foreground=BAYES_GRAY)],
        )

    # The punchline pair, saved for the frame that has all the data. Drawn a
    # shade darker than the lighter line, which reads as too faint as text.
    if n_shown == len(FLIPS):
        for series, color, va in ((freq, STEEL, "bottom"), (bayes, BAYES_GRAY, "top")):
            ax.annotate(
                f"{series[-1]:.1%}",
                xy=(x[-1], series[-1]),
                xytext=(8, 6 if va == "bottom" else -6),
                textcoords="offset points",
                ha="left", va=va, fontsize=14, color=color,
            )

    ax.set_xticks(np.arange(x_max + 1))
    ax.set_xticklabels([str(i) for i in range(x_max + 1)], fontsize=12, color=STEEL)
    ax.set_xlabel("Flips observed", fontsize=14, color=STEEL, labelpad=44)
    _draw_flip_tokens(ax, x_max, n_shown)

    ax.set_yticks(np.arange(0, 1.01, 0.25))
    ax.set_yticklabels([f"{v:.0%}" for v in np.arange(0, 1.01, 0.25)])
    ax.set_ylabel(
        "Estimated chance of heads on a single flip",
        rotation=0, ha="left", va="bottom", fontsize=14, color=STEEL,
    )
    ax.yaxis.set_label_coords(0, 1.015)
    ax.tick_params(axis="y", colors=STEEL, labelsize=12)
    ax.tick_params(axis="x", length=0, colors=STEEL)
    for side in ("top", "right"):
        ax.spines[side].set_visible(False)
    ax.spines["left"].set_color(BORDER)
    ax.spines["bottom"].set_color(BORDER)
    ax.grid(axis="y", color=BORDER, linewidth=0.8, alpha=0.7)
    ax.set_axisbelow(True)

    ax.set_title(
        "Frequentist and Bayesian estimates of the same coin",
        fontsize=19,
        color=INK,
        pad=42,  # clears the horizontal y-axis label sitting above the axis
        loc="left",
    )

    fig.tight_layout()
    # tight_layout can't see the flip tokens (they hang outside the axes), so
    # the bottom margin is set by hand to leave room for them.
    fig.subplots_adjust(bottom=0.24)
    return fig


def main() -> None:
    family = _use_repo_font()
    if family:
        plt.rcParams["font.family"] = family
    # Text as paths: the SVG stays self-contained, per STYLE.md.
    plt.rcParams["svg.fonttype"] = "path"

    for suffix, n_shown in VARIANTS:
        out_path = OUT_DIR / f"{STEM}-{suffix}.svg"
        fig = build_figure(n_shown)
        fig.savefig(out_path, format="svg", facecolor=PAPER)
        plt.close(fig)
        print(f"wrote {out_path.relative_to(REPO_ROOT)}  ({n_shown} flips shown)")

    _, freq, bayes = estimates(FLIPS)
    heads = FLIPS.count("H")
    print(f"  {heads} heads / {len(FLIPS) - heads} tails")
    print(f"  frequentist {freq[-1]:.4f} -> two heads {freq[-1] ** 2:.4f}")
    print(f"  Bayesian    {bayes[-1]:.4f} -> two heads {two_heads_bayes(FLIPS):.4f}")


if __name__ == "__main__":
    main()
