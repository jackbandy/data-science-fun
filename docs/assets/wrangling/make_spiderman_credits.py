"""Generate spiderman-data-credits.svg from the data in spiderman-data-credits.md.

Golden-rectangle (portrait) poster: title at top, then a two-column table of
name (left) / role (right), with the repo fonts embedded as base64 data URIs.
"""

import base64
import re
from pathlib import Path

HERE = Path(__file__).parent
FONTS = Path(__file__).parent.parent / "fonts"
DATA_MD = HERE / "spiderman-data-credits.md"
OUT_SVG = HERE / "spiderman-data-credits.svg"

W, H = 800, 1294  # golden rectangle, portrait (800 * phi)


def font_data_uri(path: Path) -> str:
    return "data:font/woff2;base64," + base64.b64encode(path.read_bytes()).decode()


def load_rows():
    rows = []
    for line in DATA_MD.read_text().splitlines():
        m = re.fullmatch(r"\|\s*([^|]+?)\s*\|\s*([^|]+?)\s*\|", line)
        if m and m.group(1) not in ("Name", "---"):
            rows.append((m.group(1), m.group(2)))
    return rows


rows = load_rows()

big_shoulders = font_data_uri(FONTS / "big-shoulders/BigShoulders.woff2")
libre_franklin = font_data_uri(FONTS / "libre-franklin/LibreFranklin.woff2")

svg = [
    f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">',
    f"""<style>
@font-face {{ font-family: 'Big Shoulders'; src: url({big_shoulders}) format('woff2'); font-weight: 100 900; }}
@font-face {{ font-family: 'Libre Franklin'; src: url({libre_franklin}) format('woff2'); font-weight: 100 900; }}
text {{ font-family: 'Libre Franklin', sans-serif; fill: #000; }}
</style>""",
    f'<rect width="{W}" height="{H}" fill="#fff"/>',
    f'<rect x="40" y="40" width="{W - 80}" height="{H - 80}" fill="none" stroke="#000" stroke-width="2"/>',
    f'<rect x="52" y="52" width="{W - 104}" height="{H - 104}" fill="none" stroke="#000" stroke-width="1"/>',
    f'<text x="{W / 2}" y="200" text-anchor="middle" style="font-family: \'Big Shoulders\', sans-serif; font-size: 96px; font-weight: 900; text-transform: uppercase; letter-spacing: 2px;">Spider-Man</text>',
    f'<text x="{W / 2}" y="280" text-anchor="middle" style="font-family: \'Big Shoulders\', sans-serif; font-size: 54px; font-weight: 900; text-transform: uppercase; letter-spacing: 6px;">Brand New Day</text>',
    f'<line x1="140" y1="330" x2="{W - 140}" y2="330" stroke="#000" stroke-width="2"/>',
]

y = 410
line_h = 105
left_x, right_x = 110, W - 110
font_size = 24  # largest size where the widest row (name + role) fits between left_x and right_x, per Libre Franklin metrics
for i, (name, role) in enumerate(rows):
    yc = y + i * line_h
    svg.append(f'<text x="{left_x}" y="{yc}" font-size="{font_size}px">{name}</text>')
    svg.append(f'<text x="{right_x}" y="{yc}" font-size="{font_size}px" font-weight="700" text-anchor="end">{role}</text>')
    if i < len(rows) - 1:
        svg.append(f'<line x1="{left_x}" y1="{yc + 40}" x2="{right_x}" y2="{yc + 40}" stroke="#bbb" stroke-width="1" stroke-dasharray="3 4"/>')

svg.append(f'<text x="{W / 2}" y="{H - 90}" text-anchor="middle" font-size="18px">Cast &amp; crew credits via IMDb; roles containing &#8220;data&#8221;</text>')
svg.append("</svg>")

OUT_SVG.write_text("\n".join(svg))
print(f"Wrote {OUT_SVG} ({len(rows)} rows)")
