#!/usr/bin/env python3
"""Newspaper ad revenue vs. Google and Meta ad revenue, for the Week 6 slides.

U.S. newspaper advertising revenue (Pew Research Center, from News Media
Alliance data through 2012 and Pew estimates after) against Google's and
Meta's worldwide advertising revenue (their SEC filings). Everything is
converted to 2022 dollars with the CPI-U annual average, since the newspaper
series spans 66 years.

Writes three SVGs with identical geometry, so the slides can build up in steps:
  newspaper-ad-revenue-blank.svg       axes, ticks, and labels only (the "frame")
  newspaper-ad-revenue-newspapers.svg  the same frame with the newspaper line only
  newspaper-ad-revenue-complete.svg    the same frame with all three lines

NOTICE: This script was substantially drafted by an LLM coding system.
"""

from __future__ import annotations

from pathlib import Path

import matplotlib

matplotlib.use("Agg")

import matplotlib.pyplot as plt
import polars as pl
from matplotlib import font_manager

OUT_DIR = Path(__file__).resolve().parent
DATA_DIR = OUT_DIR / "data"
REPO_ROOT = OUT_DIR.parents[2]
STEM = "newspaper-ad-revenue"
FONT_PATH = OUT_DIR.parent / "fonts" / "libre-franklin" / "LibreFranklin-Regular.ttf"

# STYLE.md palette
ORANGE = "#F9461C"
INK = "#1A1A1A"
STEEL = "#565A5C"
BORDER = "#DDDDDD"
PAPER = "#FFFFFF"

PHI = (1 + 5**0.5) / 2
WIDTH_PX = 1000
HEIGHT_PX = round(WIDTH_PX / PHI)
DPI = 100

START_YEAR = 1956  # first year of the Pew series
END_YEAR = 2022  # last year of the Pew series
DOLLAR_YEAR = 2022

# Newspapers are the orange focal line: the collapse is the story. The two
# platforms are neutral inks, told apart by lightness and by direct labels.
SERIES = {
    "newspapers": ("U.S. newspapers", ORANGE),
    "Google": ("Google (worldwide)", INK),
    "Meta": ("Meta (worldwide)", STEEL),
}


def _use_repo_font() -> str | None:
    if not FONT_PATH.exists():
        return None
    font_manager.fontManager.addfont(str(FONT_PATH))
    return font_manager.FontProperties(fname=str(FONT_PATH)).get_name()


def load_real_billions() -> dict[str, pl.DataFrame]:
    """Each series as (year, billions of DOLLAR_YEAR dollars[, estimated])."""
    cpi = (
        pl.read_csv(DATA_DIR / "fred-CPIAUCSL.csv", try_parse_dates=True)
        .group_by(pl.col("observation_date").dt.year().alias("year"))
        .agg(pl.col("CPIAUCSL").mean().alias("cpi"))
    )
    cpi_target = cpi.filter(pl.col("year") == DOLLAR_YEAR)["cpi"].item()

    def to_real(df: pl.DataFrame, nominal_usd: pl.Expr) -> pl.DataFrame:
        return (
            df.join(cpi, on="year")
            .with_columns((nominal_usd * cpi_target / pl.col("cpi") / 1e9).alias("billions"))
            .filter(pl.col("year").is_between(START_YEAR, END_YEAR))
            .sort("year")
        )

    out = {
        "newspapers": to_real(
            pl.read_csv(DATA_DIR / "pew-newspaper-ad-revenue.csv"),
            pl.col("advertising_usd_nominal"),
        )
    }
    tech = pl.read_csv(DATA_DIR / "sec-tech-ad-revenue.csv")
    for company in ("Google", "Meta"):
        out[company] = to_real(
            tech.filter(pl.col("company") == company),
            pl.col("advertising_usd_millions_nominal") * 1e6,
        )
    return out


def draw(data: dict[str, pl.DataFrame], series: tuple[str, ...], out_path: Path) -> None:
    fig = plt.figure(figsize=(WIDTH_PX / DPI, HEIGHT_PX / DPI), dpi=DPI)
    fig.patch.set_facecolor(PAPER)
    # Fixed axes box (no tight_layout / bbox="tight") so all three files line up exactly.
    ax = fig.add_axes((0.09, 0.10, 0.68, 0.78))
    ax.set_facecolor(PAPER)

    ax.set_xlim(START_YEAR, END_YEAR)
    ax.set_ylim(0, 250)
    ax.set_xticks(range(1960, END_YEAR + 1, 10))
    ax.set_yticks(range(0, 251, 50))
    ax.set_yticklabels([f"${v}B" if v else "0" for v in range(0, 251, 50)])
    ax.tick_params(axis="both", colors=STEEL, labelsize=14)
    ax.set_ylabel(
        f"Advertising revenue (billions of {DOLLAR_YEAR} dollars)",
        rotation=0, ha="left", va="bottom", fontsize=15, color=STEEL,
    )
    ax.yaxis.set_label_coords(0, 1.02)
    for side in ("top", "right"):
        ax.spines[side].set_visible(False)
    ax.spines["left"].set_color(BORDER)
    ax.spines["bottom"].set_color(BORDER)
    ax.grid(axis="y", color=BORDER, linewidth=0.8)
    ax.set_axisbelow(True)

    if series:
        for key in series:
            label, color = SERIES[key]
            df = data[key]
            if key == "newspapers":
                # Pew's post-2012 numbers are estimates from public companies'
                # filings; dash them so the change of method stays visible.
                measured = df.filter(~pl.col("estimated"))
                estimated = df.filter(pl.col("year") >= measured["year"].max())
                ax.plot(measured["year"], measured["billions"], color=color, linewidth=3,
                        solid_capstyle="round", zorder=3)
                ax.plot(estimated["year"], estimated["billions"], color=color, linewidth=3,
                        linestyle=(0, (2, 1.5)), zorder=3)
            else:
                ax.plot(df["year"], df["billions"], color=color, linewidth=3,
                        solid_capstyle="round", zorder=3)
            ax.annotate(
                label, xy=(END_YEAR, df["billions"][-1]),
                xytext=(END_YEAR + 1.2, df["billions"][-1]),
                va="center", ha="left", fontsize=15, color=INK, annotation_clip=False,
            )
        peak = data["newspapers"].sort("billions")[-1]
        ax.annotate(
            f"Newspapers peak: ${peak['billions'].item():.0f}B ({peak['year'].item()})",
            xy=(peak["year"].item(), peak["billions"].item()),
            xytext=(1970, 112), fontsize=13, color=STEEL,
            arrowprops=dict(arrowstyle="-", color=STEEL, linewidth=1),
        )

    fig.savefig(out_path, format="svg", facecolor=PAPER)
    plt.close(fig)


def main() -> None:
    family = _use_repo_font()
    if family:
        plt.rcParams["font.family"] = family
    plt.rcParams["svg.fonttype"] = "path"
    plt.rcParams["svg.hashsalt"] = STEM  # stable ids, so re-runs make clean diffs

    data = load_real_billions()
    stages = {
        "blank": (),
        "newspapers": ("newspapers",),
        "complete": tuple(SERIES),
    }
    for suffix, series in stages.items():
        out = OUT_DIR / f"{STEM}-{suffix}.svg"
        draw(data, series, out)
        print(f"wrote {out.relative_to(REPO_ROOT)}")
    for key, df in data.items():
        peak = df.sort("billions")[-1]
        print(f"  {key}: peak ${peak['billions'].item():.1f}B in {peak['year'].item()}, "
              f"{END_YEAR} ${df['billions'][-1]:.1f}B")


if __name__ == "__main__":
    main()
