#!/usr/bin/env python3
"""Chart Chicago's six citywide ballot questions from the Nov 3, 2026 general election: Yes share per question, sorted by support, with the range of possible final shares once ballots not yet counted are in.

Data comes from the Chicago Board of Election Commissioners (CBOE) "Summary Report - Unofficial Results" PDF. Run with --fetch to download the current version; otherwise the copy in data/ is used.

Uncertainty: the outer limits are the worst cases, the final Yes share if every uncounted ballot voted No (lower) or Yes (upper). Between them, a Beta prior on the uncounted ballots' Yes share, peaked at the counted share, says which final shares are likelier. Uncounted = CBOE's outstanding mail ballots + an estimate for unreported precincts (that question's average votes per reported precinct x unreported precincts).

Writes:
  data/referenda.csv                        parsed counts, shares, worst-case bounds, and the middle 50% interval
  chicago-ballot-questions-nested.svg/png   middle 50% thick, hairline out to the worst cases
  chicago-ballot-questions-gradient.svg/png gradient band, darker = more likely

Needs Poppler's pdftotext/pdfinfo on PATH.

NOTICE: This script was substantially drafted by an LLM coding system.
"""

from __future__ import annotations

import argparse
import re
import subprocess
import urllib.request
from pathlib import Path

import matplotlib

matplotlib.use("Agg")

import matplotlib.pyplot as plt
import numpy as np
import polars as pl
from matplotlib import font_manager
from matplotlib.colors import to_rgb
from scipy.stats import beta

OUT_DIR = Path(__file__).resolve().parent
DATA_DIR = OUT_DIR / "data"
PDF_PATH = DATA_DIR / "cboe-summary-report.pdf"
CSV_PATH = DATA_DIR / "referenda.csv"
STEM = "chicago-ballot-questions"
PDF_URL = "https://results.chicagoelections.gov/results/Summary%20Report%20%282%20Column%29.pdf"
TITLE_FONT = OUT_DIR.parent / "fonts" / "big-shoulders" / "BigShoulders-Bold.ttf"

# https://chicagoelections.gov/outstanding-ballot-count, "Vote By Mail – Sent, Not Returned Back to Board (Outstanding)", read 2026-11-04; the page carries no timestamp, so re-read it before re-running.
OUTSTANDING_MAIL_BALLOTS = 30_987

# Beta(1 + k*s, 1 + k*(1 - s)) prior on the uncounted ballots' Yes share, with its mode at the counted share s; k = 10 gives an SD of about 11 points at s = 0.85. TODO: calibrate k, e.g. from how late mail ballots split against the Election Day count in past Chicago elections.
UNCOUNTED_CONCENTRATION = 10
GRADIENT_HALF_HEIGHT = 0.1
GRADIENT_SLICES = 60

# CBOE contest title (whitespace-normalized) -> chart label. Wording per Block Club Chicago's Oct 14, 2026 explainer.
QUESTIONS = {
    "Chicago Cost Recovery from Midway Blitz": "Seek federal repayment for Midway Blitz",
    "ADVISORY QUESTION REGARDING MILLIONAIRES SURCHARGE": "Millionaires' tax to fund public schools",
    "The Cook County Millionaire Amendment for Property Tax Relief": "Millionaires' tax for tax relief and schools",
    "ADVISORY QUESTION REGARDING CHICAGO LAND OWNERS": "Vacant-land penalty to fund schools",
    "Restart Chicago Gunshot Detection": "Bring back gunshot detection",
    "Permanent Chicago Festival Space": "Create permanent festival grounds",
}

# Chicago flag light blue, from the Wikimedia Commons flag SVG
FLAG_BLUE = "#41B6E6"
INK = "#1A1A1A"
STEEL = "#565A5C"
BORDER = "#DDDDDD"
PAPER = "#FFFFFF"

PHI = (1 + 5**0.5) / 2
WIDTH_PX = 1000
HEIGHT_PX = round(WIDTH_PX / PHI)
DPI = 100
PNG_DPI = 300
HAIRLINE = 0.3

CONTEST = re.compile(r"\(\s*(\d+) of (\d+) precincts reported\s*\)\s*Yes\s+([\d,]+)\s+[\d.]+%\s*No\s+([\d,]+)\s+[\d.]+%\s*Total\s+([\d,]+)")


def fetch() -> None:
    DATA_DIR.mkdir(exist_ok=True)
    req = urllib.request.Request(PDF_URL, headers={"User-Agent": "Mozilla/5.0"})
    with urllib.request.urlopen(req) as resp:
        PDF_PATH.write_bytes(resp.read())


def pdf_columns(path: Path) -> str:
    """The report is two columns per page; crop each half so contests read top to bottom."""
    info = subprocess.run(["pdfinfo", str(path)], capture_output=True, text=True, check=True).stdout
    pages = int(re.search(r"Pages:\s+(\d+)", info).group(1))
    width, height = (float(v) for v in re.search(r"Page size:\s+([\d.]+) x ([\d.]+)", info).groups())
    half = width / 2
    chunks = []
    for page in range(1, pages + 1):
        for x in (0, half):
            args = ["pdftotext", "-layout", "-r", "72", "-f", str(page), "-l", str(page), "-x", str(int(x)), "-y", "0", "-W", str(int(half)), "-H", str(int(height)), str(path), "-"]
            chunks.append(subprocess.run(args, capture_output=True, text=True, check=True).stdout)
    return "\n".join(chunks)


def report_version(path: Path) -> str:
    """Version and refresh time from page 1, uncropped, since the centered header straddles both columns."""
    page1 = subprocess.run(["pdftotext", "-f", "1", "-l", "1", str(path), "-"], capture_output=True, text=True, check=True).stdout
    flat = re.sub(r"\s+", " ", page1)
    version = re.search(r"CHI \d+ Ver \w+", flat).group(0)
    refreshed = re.search(r"Data Refreshed: \w+, (.+? [AP]M)", flat).group(1)
    return f"{version}, data refreshed {refreshed}"


def parse(text: str) -> pl.DataFrame:
    flat = re.sub(r"\s+", " ", text)
    rows = []
    for title, label in QUESTIONS.items():
        m = re.search(re.escape(title) + r"\s*" + CONTEST.pattern, flat)
        if m is None:
            raise ValueError(f"contest not found in report: {title!r}")
        reported, precincts, yes, no, total = (int(g.replace(",", "")) for g in m.groups())
        assert yes + no == total, f"{title}: Yes + No != Total"
        rows.append({"question": label, "cboe_title": title, "precincts_reported": reported, "precincts_total": precincts, "yes": yes, "no": no})
    return pl.DataFrame(rows)


def with_bounds(df: pl.DataFrame, outstanding_mail: int) -> pl.DataFrame:
    counted = pl.col("yes") + pl.col("no")
    unreported = (counted / pl.col("precincts_reported") * (pl.col("precincts_total") - pl.col("precincts_reported"))).round().cast(pl.Int64)
    df = df.with_columns(counted=counted, uncounted_est=unreported + outstanding_mail)
    final = pl.col("counted") + pl.col("uncounted_est")
    return df.with_columns(
        yes_share=pl.col("yes") / pl.col("counted"),
        yes_share_low=pl.col("yes") / final,
        yes_share_high=(pl.col("yes") + pl.col("uncounted_est")) / final,
    ).sort("yes_share", descending=True)


def outcomes(r: dict, k: float = UNCOUNTED_CONCENTRATION):
    """The prior on the uncounted ballots' Yes share p, and the map from p to the final Yes share (0-1)."""
    s = r["yes"] / r["counted"]
    prior = beta(1 + k * s, 1 + k * (1 - s))
    return prior, lambda p: (r["yes"] + p * r["uncounted_est"]) / (r["counted"] + r["uncounted_est"])


def with_intervals(df: pl.DataFrame) -> pl.DataFrame:
    cols = {}
    for q in (0.25, 0.75):
        vals = []
        for r in df.iter_rows(named=True):
            prior, to_final = outcomes(r)
            vals.append(float(to_final(prior.ppf(q))))
        cols[f"yes_share_q{q * 100:g}".replace(".", "_")] = vals
    return df.with_columns(**{name: pl.Series(v) for name, v in cols.items()})


def draw_nested(ax, i: int, r: dict) -> None:
    ax.hlines(i, 100 * r["yes_share_low"], 100 * r["yes_share_high"], color=INK, linewidth=HAIRLINE, zorder=3)
    ax.hlines(i, 100 * r["yes_share_q25"], 100 * r["yes_share_q75"], color=INK, linewidth=7, zorder=3)


def draw_gradient(ax, i: int, r: dict) -> None:
    """Abutting vector slices, each as opaque as the prior's density there, so the SVG stays raster-free."""
    prior, to_final = outcomes(r)
    edges = np.linspace(0, 1, GRADIENT_SLICES + 1)
    density = prior.pdf((edges[:-1] + edges[1:]) / 2)
    alpha = density / density.max()
    x = 100 * to_final(edges)
    colors = [(*to_rgb(INK), a) for a in alpha]
    ax.broken_barh(list(zip(x[:-1], np.diff(x))), (i - GRADIENT_HALF_HEIGHT, 2 * GRADIENT_HALF_HEIGHT), facecolors=colors, linewidth=0, zorder=3)


STYLES = {
    "nested": (draw_nested, "Line ends: every uncounted ballot votes No, or every one votes Yes. (Thick line: middle 50% of likely final shares)"),
    "gradient": (draw_gradient, "Dark band: where the final share is likely to land once uncounted ballots are in, fading toward all-No and all-Yes"),
}


def draw(df: pl.DataFrame, source_note: str, outstanding_mail: int, style: str) -> None:
    mark, legend = STYLES[style]
    font_manager.fontManager.addfont(str(TITLE_FONT))
    title_family = font_manager.FontProperties(fname=str(TITLE_FONT)).get_name()
    plt.rcParams["font.family"] = "Arial"

    fig = plt.figure(figsize=(WIDTH_PX / DPI, HEIGHT_PX / DPI), dpi=DPI)
    fig.patch.set_facecolor(PAPER)
    ax = fig.add_axes((0.43, 0.18, 0.53, 0.59))
    ax.set_facecolor(PAPER)

    for i, r in enumerate(df.iter_rows(named=True)):
        share, hi = 100 * r["yes_share"], 100 * r["yes_share_high"]
        ax.barh(i, share, height=0.62, color=FLAG_BLUE, zorder=2)
        mark(ax, i, r)
        ax.text(hi + 1.5, i, f"{share:.1f}%", va="center", ha="left", fontsize=15, color=INK, zorder=4)

    ax.set_yticks(range(df.height), df["question"].to_list(), fontsize=15, color=INK)
    ax.invert_yaxis()
    ax.set_xlim(0, 100)
    ax.set_xticks(range(0, 101, 25), [f"{t}%" for t in range(0, 101, 25)])
    ax.tick_params(axis="x", colors=STEEL, labelsize=13)
    ax.tick_params(axis="y", length=0, pad=10)
    ax.grid(axis="x", color=BORDER, linewidth=0.8, zorder=0)
    for side in ("top", "right", "left"):
        ax.spines[side].set_visible(False)
    ax.spines["bottom"].set_color(BORDER)

    reported, total = df["precincts_reported"].min(), df["precincts_total"].max()
    fig.text(0.03, 0.91, "Unofficial Results for Chicago Citywide Ballot Questions", family=title_family, fontsize=34, color=INK)
    fig.text(0.03, 0.82, f"Share voting Yes, Nov 3, 2026 ({reported:,} of {total:,} precincts reported)\n{legend}", fontsize=12, color=STEEL, linespacing=1.5)
    fig.text(0.03, 0.02, f"Chicago Board of Election Commissioners, Summary Report {source_note}\nData source: {PDF_URL}\nUncounted: {outstanding_mail:,} outstanding mail ballots + an estimate for unreported precincts", fontsize=10, color=STEEL, linespacing=1.5, url=PDF_URL)

    for ext in ("svg", "png"):
        fig.savefig(OUT_DIR / f"{STEM}-{style}.{ext}", facecolor=PAPER, dpi=PNG_DPI if ext == "png" else DPI)
        print(f"  wrote {STEM}-{style}.{ext}")
    plt.close(fig)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--fetch", action="store_true", help="download the current CBOE summary report before charting")
    args = parser.parse_args()
    if args.fetch or not PDF_PATH.exists():
        fetch()
    df = with_intervals(with_bounds(parse(pdf_columns(PDF_PATH)), OUTSTANDING_MAIL_BALLOTS))
    source_note = report_version(PDF_PATH)
    df.write_csv(CSV_PATH)
    print(df.select("question", "yes_share", "yes_share_low", "yes_share_q25", "yes_share_q75", "yes_share_high"))
    for style in STYLES:
        draw(df, source_note, OUTSTANDING_MAIL_BALLOTS, style)


if __name__ == "__main__":
    main()
