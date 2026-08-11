#!/usr/bin/env python3
"""Split the Macworld pie chart comparison into its two panels.

`misleading-macworld-3d-pie-chart.svg` (Cmglee, CC BY-SA 4.0 — see SOURCES.md)
stacks a 3D perspective pie over a flat 2D pie of the same data. Slides want the
panels side by side, so this writes each one as its own SVG, cropped to the
panel's own viewBox and carrying only the elements that belong to it.

Nothing is redrawn: the top panel keeps the original's embedded raster and the
bottom panel keeps its vector sectors. The results are derivative works, so they
stay CC BY-SA 4.0.
"""

from __future__ import annotations

import re
from pathlib import Path

HERE = Path(__file__).resolve().parent
SOURCE = HERE / "misleading-macworld-3d-pie-chart.svg"
TOP = HERE / "macworld-pie-3d.svg"
BOTTOM = HERE / "macworld-pie-2d.svg"

# The source viewBox is "-279 -728 558 992": the 3D raster spans y -720..-266,
# the 2D pie is a circle of r=256 centred on the origin. Both panels keep the
# original's ~8px vertical and ~23px horizontal margins.
TOP_VIEWBOX = "-279 -728 558 470"
BOTTOM_VIEWBOX = "-279 -264 558 536"

CREDIT = (
    "Panel from 'misleading macworld 3d pie chart' by Cmglee, Wikimedia Commons, "
    "CC BY-SA 4.0. Cropped, unaltered otherwise."
)


def part(source: str, pattern: str) -> str:
    match = re.search(pattern, source, re.S)
    if match is None:
        raise SystemExit(f"source SVG no longer matches: {pattern}")
    return match.group(0)


def document(viewbox: str, title: str, desc: str, body: str) -> str:
    return f"""<?xml version="1.0" encoding="utf-8"?>
<svg version="1.1" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" width="100%" height="100%" viewBox="{viewbox}">
 <title>{title}</title>
 <desc>{desc} {CREDIT}</desc>
 <style type="text/css">
svg {{ font-family:'Liberation Sans',Helvetica,Arial,sans-serif; font-size:24px; text-anchor:middle; fill:#000; stroke:none; }}
.vs {{ font-size:40px; font-weight:bold; }}
 </style>
 <circle cx="0" cy="0" r="99999" fill="#fff"/>
{body}
</svg>
"""


def main() -> None:
    source = SOURCE.read_text()

    image = part(source, r"<image\b[^>]*/>")
    sectors = part(source, r'<g fill="#9cf">.*?</g>')
    labels = part(source, r'<g id="label">.*?</g>')
    top_labels = part(source, r'<use xlink:href="#label"[^>]*/>')

    # Top: the raster panel, with the label group defined but drawn only through
    # the <use> that offsets it onto the 3D pie.
    TOP.write_text(
        document(
            TOP_VIEWBOX,
            "Macworld 2008 pie chart, 3D perspective",
            "US smartphone market share as a 3D perspective pie chart, as presented at Macworld 2008.",
            f" <defs>\n  {labels}\n </defs>\n {image}\n {top_labels}",
        )
    )

    # Bottom: the vector pie, labels drawn in place at the origin.
    BOTTOM.write_text(
        document(
            BOTTOM_VIEWBOX,
            "Macworld 2008 pie chart data, flat 2D",
            "The same US smartphone market share data as a flat 2D pie chart.",
            f' <circle cx="0" cy="0" r="256"/>\n {sectors}\n {labels}',
        )
    )

    for path in (TOP, BOTTOM):
        print(f"{path.name} ({path.stat().st_size:,} bytes)")


if __name__ == "__main__":
    main()
