#!/usr/bin/env python3
"""Generate the Week 6 serif vs. sans-serif letter figures: "AaBbCc" in Superclarendon, the same with its serifs in red, and in Helvetica.

Letters are outlined paths, so no font is embedded. Run with: uvx --from fonttools python make_serif_figures.py
"""

from __future__ import annotations

from pathlib import Path

from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.transformPen import TransformPen
from fontTools.ttLib import TTCollection

TEXT = "AaBbCc"
WIDTH, HEIGHT = 1000, 260
MARGIN = 20
INK = "#111111"
MARK = "#E00000"
OUT_DIR = Path(__file__).resolve().parent

SERIF = ("/System/Library/Fonts/Supplemental/SuperClarendon.ttc", "Superclarendon Regular")
SANS = ("/System/Library/Fonts/Helvetica.ttc", "Helvetica")

# Boxes (font units, per glyph: x0, y0, x1, y1) around the parts of each serif or terminal that stick out past the main stroke.
# Read off Superclarendon Regular outlines; the red fill is the glyph clipped to these boxes.
SERIF_BOXES = {
    "A": [(37, 0, 122, 100), (180, 0, 312, 100), (470, 0, 585, 100), (760, 0, 842, 100)],
    "a": [(70, 310, 215, 440), (560, -20, 660, 160)],
    "B": [(37, 640, 122, 745), (37, 0, 122, 105)],
    "b": [(0, 640, 95, 775)],
    "C": [(660, 480, 750, 750)],
    "c": [(390, 310, 545, 430)],
}


def load(path: str, name: str):
    return next(f for f in TTCollection(path).fonts if f["name"].getDebugName(4) == name)


def layout(font):
    """Return (glyph_name, char, x_offset) per character and the scale/translate that fit the line in the canvas."""
    cmap, hmtx = font.getBestCmap(), font["hmtx"]
    placed, x = [], 0
    for ch in TEXT:
        name = cmap[ord(ch)]
        placed.append((name, ch, x))
        x += hmtx[name][0]
    ascent = font["OS/2"].sCapHeight or font["hhea"].ascent
    scale = min((WIDTH - 2 * MARGIN) / x, (HEIGHT - 2 * MARGIN) / (ascent * 1.1))
    tx = (WIDTH - x * scale) / 2
    ty = HEIGHT / 2 + ascent * scale / 2
    return placed, scale, tx, ty


def glyph_d(font, name: str, scale: float, x: float, ty: float) -> str:
    pen = SVGPathPen(font.getGlyphSet())
    font.getGlyphSet()[name].draw(TransformPen(pen, (scale, 0, 0, -scale, x, ty)))
    return pen.getCommands()


def render(font, label: str, marked: bool = False) -> str:
    placed, scale, tx, ty = layout(font)
    ink, marks, clips = [], [], []
    for i, (name, ch, dx) in enumerate(placed):
        d = glyph_d(font, name, scale, tx + dx * scale, ty)
        ink.append(d)
        if marked and SERIF_BOXES.get(ch):
            rects = "".join(
                f'<rect x="{tx + (dx + x0) * scale:.1f}" y="{ty - y1 * scale:.1f}" width="{(x1 - x0) * scale:.1f}" height="{(y1 - y0) * scale:.1f}"/>'
                for x0, y0, x1, y1 in SERIF_BOXES[ch]
            )
            clips.append(f'<clipPath id="serif-{i}">{rects}</clipPath>')
            marks.append(f'<path d="{d}" fill="{MARK}" clip-path="url(#serif-{i})"/>')
    return (
        f'<svg width="{WIDTH}" height="{HEIGHT}" viewBox="0 0 {WIDTH} {HEIGHT}" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="{label}">\n'
        f"<defs>{''.join(clips)}</defs>\n"
        f'<path d="{" ".join(ink)}" fill="{INK}"/>\n'
        + "".join(m + "\n" for m in marks)
        + "</svg>\n"
    )


def main() -> None:
    serif, sans = load(*SERIF), load(*SANS)
    (OUT_DIR / "serif-demo.svg").write_text(render(serif, "AaBbCc in Superclarendon, a serif typeface"))
    (OUT_DIR / "serif-demo-marked.svg").write_text(render(serif, "AaBbCc in Superclarendon with the serifs in red", marked=True))
    (OUT_DIR / "sans-demo.svg").write_text(render(sans, "AaBbCc in Helvetica, a sans-serif typeface"))
    print("wrote serif-demo.svg, serif-demo-marked.svg, sans-demo.svg")


if __name__ == "__main__":
    main()
