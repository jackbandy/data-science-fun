from __future__ import annotations

import base64
import io
import math
from pathlib import Path

from PIL import Image, ImageDraw


PHI = (1 + math.sqrt(5)) / 2
WIDTH = 1600
HEIGHT = round(WIDTH / PHI)
UIC_RED = "#D50032"
OUTPUT_DIR = Path(__file__).resolve().parent


def triangle_points() -> list[tuple[float, float]]:
    side = HEIGHT * 0.88
    tri_height = side * math.sqrt(3) / 2
    x0 = (WIDTH - side) / 2
    y0 = (HEIGHT - tri_height) / 2 + tri_height
    return [
        (x0, y0),
        (x0 + side / 2, y0 - tri_height),
        (x0 + side, y0),
    ]


def rect_centered_on_segment(
    p0: tuple[float, float],
    p1: tuple[float, float],
    scale: float,
) -> tuple[int, int, int, int]:
    mid_x = (p0[0] + p1[0]) / 2
    mid_y = (p0[1] + p1[1]) / 2
    rect_w = WIDTH / scale
    rect_h = rect_w / PHI
    left = round(mid_x - rect_w / 2)
    top = round(mid_y - rect_h / 2)
    right = round(mid_x + rect_w / 2)
    bottom = round(mid_y + rect_h / 2)
    return (left, top, right, bottom)


def svg_markup(points: list[tuple[float, float]], *rects: tuple[int, int, int, int]) -> str:
    polygon = " ".join(f"{x:.2f},{y:.2f}" for x, y in points)
    rect_markup = "\n".join(
        f'  <rect x="{x0}" y="{y0}" width="{x1 - x0}" height="{y1 - y0}" '
        f'fill="none" stroke="{UIC_RED}" stroke-width="3" />'
        for x0, y0, x1, y1 in rects
    )
    return f"""<svg xmlns="http://www.w3.org/2000/svg" width="{WIDTH}" height="{HEIGHT}" viewBox="0 0 {WIDTH} {HEIGHT}">
  <rect width="100%" height="100%" fill="white" />
  <polygon points="{polygon}" fill="none" stroke="black" stroke-width="6" stroke-linejoin="round" />
{rect_markup}
</svg>
"""


def raster_svg_markup(image: Image.Image) -> str:
    buffer = io.BytesIO()
    image.save(buffer, format="PNG")
    encoded = base64.b64encode(buffer.getvalue()).decode("ascii")
    return f"""<svg xmlns="http://www.w3.org/2000/svg" width="{WIDTH}" height="{HEIGHT}" viewBox="0 0 {WIDTH} {HEIGHT}">
  <rect width="100%" height="100%" fill="white" />
  <image
    width="{WIDTH}"
    height="{HEIGHT}"
    href="data:image/png;base64,{encoded}"
    image-rendering="pixelated"
    preserveAspectRatio="none"
  />
</svg>
"""


def draw_triangle() -> Image.Image:
    image = Image.new("RGB", (WIDTH, HEIGHT), "white")
    draw = ImageDraw.Draw(image)
    draw.polygon(triangle_points(), outline="black", width=6)
    return image


def crop_and_resize(
    image: Image.Image,
    rect: tuple[int, int, int, int],
    resample: Image.Resampling,
) -> Image.Image:
    return image.crop(rect).resize((WIDTH, HEIGHT), resample=resample)


def draw_rect(image: Image.Image, rect: tuple[int, int, int, int]) -> None:
    ImageDraw.Draw(image).rectangle(rect, outline=UIC_RED, width=3)


def project_rect(
    outer_rect: tuple[int, int, int, int],
    inner_rect: tuple[int, int, int, int],
) -> tuple[int, int, int, int]:
    ox0, oy0, ox1, oy1 = outer_rect
    ix0, iy0, ix1, iy1 = inner_rect
    scale_x = WIDTH / (ox1 - ox0)
    scale_y = HEIGHT / (oy1 - oy0)
    return (
        round((ix0 - ox0) * scale_x),
        round((iy0 - oy0) * scale_y),
        round((ix1 - ox0) * scale_x),
        round((iy1 - oy0) * scale_y),
    )


def main() -> None:
    points = triangle_points()
    left_edge = (points[0], points[1])
    outer_rect = rect_centered_on_segment(*left_edge, scale=10)
    inner_rect = rect_centered_on_segment(*left_edge, scale=100)

    (OUTPUT_DIR / "00-triangle-best.svg").write_text(svg_markup(points), encoding="utf-8")
    (OUTPUT_DIR / "01-triangle-frame.svg").write_text(
        svg_markup(points, outer_rect), encoding="utf-8"
    )

    base_png = draw_triangle()
    edge_png = crop_and_resize(base_png, outer_rect, resample=Image.Resampling.LANCZOS)
    (OUTPUT_DIR / "02-triangle-edge.svg").write_text(
        raster_svg_markup(edge_png), encoding="utf-8"
    )

    edge_frame_png = edge_png.copy()
    nested_rect = project_rect(outer_rect, inner_rect)
    draw_rect(edge_frame_png, nested_rect)
    (OUTPUT_DIR / "03-triangle-edge-frame.svg").write_text(
        raster_svg_markup(edge_frame_png), encoding="utf-8"
    )

    zoom_source = base_png.crop(inner_rect)
    zoom_png = zoom_source.resize((WIDTH, HEIGHT), resample=Image.Resampling.NEAREST)
    (OUTPUT_DIR / "04-triangle-edge-zoom.svg").write_text(
        raster_svg_markup(zoom_png), encoding="utf-8"
    )


if __name__ == "__main__":
    main()
