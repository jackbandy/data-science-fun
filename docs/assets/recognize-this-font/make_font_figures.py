#!/usr/bin/env python3
"""Generate the "Recognize this font?" SVGs for the Week 6 slides: each typeface once plain (black on white) and once themed.

Text is converted to outlined paths so no font file is redistributed; see SOURCES.md for where each font comes from.
Run with: uvx --from fonttools python make_font_figures.py
"""

from __future__ import annotations

from pathlib import Path

from fontTools.pens.boundsPen import BoundsPen
from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.transformPen import TransformPen
from fontTools.ttLib import TTCollection, TTFont

PHI = (1 + 5**0.5) / 2
WIDTH = 1000
HEIGHT = round(WIDTH / PHI)
TEXT = "Example Font"
TEXT_WIDTH = 0.8 * WIDTH

OUT_DIR = Path(__file__).resolve().parent
LOCAL_FONTS = OUT_DIR / ".fonts"  # git-ignored; see SOURCES.md

PLAIN = {"background": '<rect width="100%" height="100%" fill="#FFFFFF"/>', "fill": "#111111", "defs": "", "filter": ""}

THEMES = {
    "avatar": {
        "font": ("/System/Library/Fonts/Supplemental/Papyrus.ttc", "Papyrus"),
        "defs": (
            '<radialGradient id="bg" cx="50%" cy="50%" r="70%"><stop offset="0" stop-color="#0E2F55"/><stop offset="1" stop-color="#020C18"/></radialGradient>'
            '<filter id="glow" x="-20%" y="-50%" width="140%" height="200%"><feGaussianBlur stdDeviation="9" result="blur"/><feMerge><feMergeNode in="blur"/><feMergeNode in="SourceGraphic"/></feMerge></filter>'
        ),
        "background": '<rect width="100%" height="100%" fill="url(#bg)"/>',
        "fill": "#8FE8FF",
        "filter": ' filter="url(#glow)"',
    },
    "olivia-rodrigo": {
        "font": (str(LOCAL_FONTS / "JustLikeHeavenRegular.woff"), None),
        "defs": '<linearGradient id="bg" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#8DB6DE"/><stop offset="1" stop-color="#E4EEF8"/></linearGradient>',
        "background": '<rect width="100%" height="100%" fill="url(#bg)"/>',
        "fill": "#F0619F",
        "filter": "",
    },
    "kpop-demon-hunters": {
        "font": (str(LOCAL_FONTS / "Hunters K-Pop.otf"), None),
        "defs": '<linearGradient id="ink" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#FF3FA4"/><stop offset="0.5" stop-color="#B44BFF"/><stop offset="1" stop-color="#3FD4FF"/></linearGradient>',
        "background": '<rect width="100%" height="100%" fill="#120A1F"/>',
        "fill": "url(#ink)",
        "filter": "",
    },
    "ikea": {
        "font": ("/System/Library/Fonts/Supplemental/Verdana Bold.ttf", None),
        "defs": "",
        "background": '<rect width="100%" height="100%" fill="#0058A3"/>',
        "fill": "#FFDB00",
        "filter": "",
    },
    "brat": {
        "font": ("/System/Library/Fonts/Supplemental/Arial.ttf", None),
        # The cover sets its lowercase title neither large nor small, a little soft.
        "text": "example font",
        "width": 0.55 * WIDTH,
        "defs": '<filter id="soft"><feGaussianBlur stdDeviation="1.6"/></filter>',
        "background": '<rect width="100%" height="100%" fill="#8ACE00"/>',
        "fill": "#000000",
        "filter": ' filter="url(#soft)"',
    },
}


def load_font(path: str, name: str | None) -> TTFont:
    if path.endswith(".ttc"):
        return next(f for f in TTCollection(path).fonts if f["name"].getDebugName(4) == name)
    return TTFont(path)


def text_path(font: TTFont, text: str, width: float) -> str:
    """Lay out text on one line, then scale it to width and center it on the canvas."""
    glyphs = font.getGlyphSet()
    cmap = font.getBestCmap()
    hmtx = font["hmtx"]

    placed, x = [], 0
    for ch in text:
        name = cmap[ord(ch)]
        placed.append((name, x))
        x += hmtx[name][0]

    bounds = BoundsPen(glyphs)
    for name, dx in placed:
        glyphs[name].draw(TransformPen(bounds, (1, 0, 0, 1, dx, 0)))
    xmin, ymin, xmax, ymax = bounds.bounds

    scale = width / (xmax - xmin)
    # Flip y (font units point up) and center the ink box on the canvas.
    tx = WIDTH / 2 - scale * (xmin + xmax) / 2
    ty = HEIGHT / 2 + scale * (ymin + ymax) / 2

    pen = SVGPathPen(glyphs)
    for name, dx in placed:
        glyphs[name].draw(TransformPen(pen, (scale, 0, 0, -scale, tx + scale * dx, ty)))
    return pen.getCommands()


def render(d: str, style: dict, label: str) -> str:
    return (
        f'<svg width="{WIDTH}" height="{HEIGHT}" viewBox="0 0 {WIDTH} {HEIGHT}" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="{label}">\n'
        f'<defs>{style["defs"]}</defs>\n'
        f'{style["background"]}\n'
        f'<path d="{d}" fill="{style["fill"]}"{style["filter"]}/>\n'
        "</svg>\n"
    )


def main() -> None:
    for slug, theme in THEMES.items():
        text = theme.get("text", TEXT)
        d = text_path(load_font(*theme["font"]), text, theme.get("width", TEXT_WIDTH))
        (OUT_DIR / f"{slug}-plain.svg").write_text(render(d, PLAIN, f"The words {text} in black on white"))
        (OUT_DIR / f"{slug}-themed.svg").write_text(render(d, theme, f"The words {text} in a themed color scheme"))
        print(f"wrote {slug}-plain.svg, {slug}-themed.svg")


if __name__ == "__main__":
    main()
