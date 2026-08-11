#!/usr/bin/env python3
"""Redraw the Barocas "Understanding Inscrutability" figures as native SVG.

The `fig-*.svg` files in this folder are extractions from the source deck (see
SOURCES.md): PowerPoint charts full of glyph outlines and rasterised shading.
This script re-draws the same eight ideas from scratch -- own 3D projection,
own painter's-algorithm surface renderer -- in the repo palette, on
golden-ratio canvases, writing `fig-*-remix.svg` alongside the originals.
"""

from __future__ import annotations

import base64
import math
from pathlib import Path
from xml.sax.saxutils import escape

import numpy as np


PHI = (1 + 5**0.5) / 2
WIDTH = 1000
HEIGHT = round(WIDTH / PHI)

OUT_DIR = Path(__file__).resolve().parent

ORANGE = "#f9461c"
INK = "#1a1a1a"
TEXT = "#444"
QUIET = "#aaa"
BORDER = "#ddd"
PAPER = "#fff"

# Ends of the shading ramp for lit surfaces; plain orange sits about midway.
SHADE_DARK = (0xA8, 0x2A, 0x0E)
SHADE_LIGHT = (0xFF, 0xA8, 0x76)

CURVE_WIDTH = 5
AXIS_WIDTH = 2
MESH_STROKE = "#3d3230"

FONT_FAMILY = "Libre Franklin"
FONT_SOURCE = OUT_DIR / ".." / "fonts" / "libre-franklin" / "LibreFranklin.woff2"

LABEL_SIZE = 22

# Cameras are (azimuth, elevation) in degrees, chosen per figure to match the
# viewpoint of the corresponding slide in the source deck. Any azimuth in
# (0, 90) puts the far corner of the unit square nearest the viewer, so the two
# front edges splay down-left (debts) and down-right (income); raising it
# swings the box to look more along the debts axis. World x = income,
# world y = outstanding debts.
DEFAULT_CAMERA = (45.0, 20.0)
LIGHT = (-0.42, 0.25, 0.87)


# --------------------------------------------------------------------------
# svg scaffolding


def font_data_url() -> str:
    encoded = base64.b64encode(FONT_SOURCE.resolve().read_bytes()).decode("ascii")
    return f"data:font/woff2;base64,{encoded}"


def svg_document(body: str) -> str:
    return f"""<svg width="{WIDTH}" height="{HEIGHT}" viewBox="0 0 {WIDTH} {HEIGHT}" xmlns="http://www.w3.org/2000/svg">
  <rect width="{WIDTH}" height="{HEIGHT}" fill="{PAPER}"/>
  <style>
    @font-face {{
      font-family: '{FONT_FAMILY}';
      src: url('{font_data_url()}') format('woff2');
      font-weight: 100 900;
      font-style: normal;
    }}
  </style>
{body}
</svg>
"""


def label(text: str, x: float, y: float, rotation: float = 0, anchor: str = "middle") -> str:
    transform = f' transform="rotate({rotation:.1f} {x:.1f} {y:.1f})"' if rotation else ""
    return (
        f'  <text x="{x:.1f}" y="{y:.1f}" text-anchor="{anchor}"{transform} '
        f'font-family="{FONT_FAMILY}" font-size="{LABEL_SIZE}" font-weight="400" '
        f'fill="{INK}">{escape(text)}</text>'
    )


# --------------------------------------------------------------------------
# two-dimensional relationships


def curve_figure(fn, samples: int = 400) -> str:
    left, right, top, bottom = 186, 56, 46, 92
    plot_w = WIDTH - left - right
    plot_h = HEIGHT - top - bottom
    base_y = top + plot_h

    xs = np.linspace(0.0, 1.0, samples)
    ys = np.asarray(fn(xs), dtype=float)
    ys = (ys - ys.min()) / (ys.max() - ys.min())

    points = " ".join(
        f"{left + x * plot_w:.2f},{base_y - y * plot_h:.2f}" for x, y in zip(xs, ys)
    )

    parts = [
        f'  <line x1="{left}" y1="{top - 6}" x2="{left}" y2="{base_y}" '
        f'stroke="{QUIET}" stroke-width="{AXIS_WIDTH}"/>',
        f'  <line x1="{left}" y1="{base_y}" x2="{WIDTH - right + 6}" y2="{base_y}" '
        f'stroke="{QUIET}" stroke-width="{AXIS_WIDTH}"/>',
        f'  <polyline points="{points}" fill="none" stroke="{ORANGE}" '
        f'stroke-width="{CURVE_WIDTH}" stroke-linecap="round" stroke-linejoin="round"/>',
        label("Length of Employment", left + plot_w / 2, HEIGHT - 34),
        label("Credit Score", left - 18, top + plot_h / 2 + LABEL_SIZE * 0.35, anchor="end"),
    ]
    return svg_document("\n".join(parts))


# --------------------------------------------------------------------------
# three-dimensional relationships


def project(point: tuple[float, float, float], camera) -> tuple[float, float, float]:
    """Orthographic projection -> (screen x, screen y, depth); larger depth is nearer."""
    x, y, z = point
    azimuth, elevation = (math.radians(angle) for angle in camera)
    ca, sa = math.cos(azimuth), math.sin(azimuth)
    ce, se = math.cos(elevation), math.sin(elevation)
    screen_x = -x * sa + y * ca
    screen_y = -((-x * ca - y * sa) * se + z * ce)
    depth = x * ca * ce + y * sa * ce + z * se
    return screen_x, screen_y, depth


def fit_transform(corners: list[tuple[float, float, float]], camera) -> tuple[float, float, float]:
    """Scale + offset that fits the box corners into the canvas with room for labels."""
    # The left margin carries the horizontal "Credit Score" label.
    margin_left, margin_right, margin_top, margin_bottom = 178, 56, 40, 76
    projected = [project(corner, camera) for corner in corners]
    min_x = min(p[0] for p in projected)
    max_x = max(p[0] for p in projected)
    min_y = min(p[1] for p in projected)
    max_y = max(p[1] for p in projected)
    scale = min(
        (WIDTH - margin_left - margin_right) / (max_x - min_x),
        (HEIGHT - margin_top - margin_bottom) / (max_y - min_y),
    )
    offset_x = (margin_left + WIDTH - margin_right) / 2 - scale * (min_x + max_x) / 2
    offset_y = (margin_top + HEIGHT - margin_bottom) / 2 - scale * (min_y + max_y) / 2
    return scale, offset_x, offset_y


def shade(normal: tuple[float, float, float]) -> str:
    length = math.sqrt(sum(component**2 for component in normal)) or 1.0
    light_length = math.sqrt(sum(component**2 for component in LIGHT))
    lambert = sum(n * l for n, l in zip(normal, LIGHT)) / (length * light_length)
    t = max(0.0, min(1.0, (lambert - 0.30) / 0.60))
    channels = (
        round(dark + (light - dark) * t) for dark, light in zip(SHADE_DARK, SHADE_LIGHT)
    )
    return "#" + "".join(f"{channel:02x}" for channel in channels)


def surface_figure(
    fn,
    grid: int = 16,
    z_extent: float = 0.60,
    z_fill: float = 1.0,
    mesh_width: float = 0.8,
    camera=DEFAULT_CAMERA,
) -> str:
    """Render credit score = fn(debts, income) over the unit square, inside a box.

    World axes follow the camera note above: x is income, y is outstanding debts.
    """
    axis = np.linspace(0.0, 1.0, grid + 1)
    gx, gy = np.meshgrid(axis, axis, indexing="ij")
    gz = np.asarray(fn(gy, gx), dtype=float)
    gz = (gz - gz.min()) / (gz.max() - gz.min())
    gz = 0.5 + (gz - 0.5) * z_fill  # gentler relationships need not fill the box

    # Centre the box on the origin so the projection stays balanced.
    def world(i: int, j: int) -> tuple[float, float, float]:
        return (gx[i, j] - 0.5, gy[i, j] - 0.5, (gz[i, j] - 0.5) * z_extent)

    corners = [
        (sx, sy, sz * z_extent)
        for sx in (-0.5, 0.5)
        for sy in (-0.5, 0.5)
        for sz in (-0.5, 0.5)
    ]
    scale, offset_x, offset_y = fit_transform(corners, camera)

    def to_screen(point: tuple[float, float, float]) -> tuple[float, float, float]:
        sx, sy, depth = project(point, camera)
        return scale * sx + offset_x, scale * sy + offset_y, depth

    # Every primitive goes into one depth-sorted list so the box wireframe
    # weaves in front of and behind the surface without special-casing.
    primitives: list[tuple[float, str]] = []

    step = 1.0 / grid
    for i in range(grid):
        for j in range(grid):
            quad = [world(i, j), world(i + 1, j), world(i + 1, j + 1), world(i, j + 1)]
            screen = [to_screen(point) for point in quad]
            dz_dx = (gz[i + 1, j] - gz[i, j] + gz[i + 1, j + 1] - gz[i, j + 1]) / 2
            dz_dy = (gz[i, j + 1] - gz[i, j] + gz[i + 1, j + 1] - gz[i + 1, j]) / 2
            normal = (-dz_dx * z_extent / step, -dz_dy * z_extent / step, 1.0)
            points = " ".join(f"{x:.2f},{y:.2f}" for x, y, _ in screen)
            primitives.append(
                (
                    sum(p[2] for p in screen) / 4,
                    f'  <polygon points="{points}" fill="{shade(normal)}" '
                    f'stroke="{MESH_STROKE}" stroke-width="{mesh_width}" '
                    'stroke-linejoin="round" stroke-opacity="0.55"/>',
                )
            )

    box_edges = [
        (a, b)
        for a in corners
        for b in corners
        if sum(1 for ca, cb in zip(a, b) if ca != cb) == 1 and a < b
    ]
    for a, b in box_edges:
        ax, ay, ad = to_screen(a)
        bx, by, bd = to_screen(b)
        primitives.append(
            (
                (ad + bd) / 2,
                f'  <line x1="{ax:.1f}" y1="{ay:.1f}" x2="{bx:.1f}" y2="{by:.1f}" '
                f'stroke="{BORDER}" stroke-width="{AXIS_WIDTH}"/>',
            )
        )

    primitives.sort(key=lambda item: item[0])
    body = [markup for _, markup in primitives]

    z_bottom = -0.5 * z_extent
    z_top = 0.5 * z_extent
    # The two edges meeting at the near corner, plus the leftmost vertical edge.
    body.append(edge_label("Outstanding Debts", (0.5, 0.5, z_bottom), (0.5, -0.5, z_bottom), to_screen, 30))
    body.append(edge_label("Income", (0.5, 0.5, z_bottom), (-0.5, 0.5, z_bottom), to_screen, 30))
    body.append(
        edge_label(
            "Credit Score", (0.5, -0.5, z_bottom), (0.5, -0.5, z_top), to_screen, 20, upright=True
        )
    )

    return svg_document("\n".join(body))


def edge_label(text: str, a, b, to_screen, gap: float, upright: bool = False) -> str:
    """Place a label alongside a box edge, rotated to run with it (or left upright)."""
    ax, ay, _ = to_screen(a)
    bx, by, _ = to_screen(b)
    cx, cy, _ = to_screen((0.0, 0.0, 0.0))
    mid_x, mid_y = (ax + bx) / 2, (ay + by) / 2

    dx, dy = bx - ax, by - ay
    length = math.hypot(dx, dy) or 1.0
    # Perpendicular, pointed away from the box centre.
    px, py = -dy / length, dx / length
    if px * (mid_x - cx) + py * (mid_y - cy) < 0:
        px, py = -px, -py

    if upright:
        # Horizontal text, set outside the edge and away from the box.
        anchor = "end" if px < 0 else "start"
        return label(
            text, mid_x + px * gap, mid_y + LABEL_SIZE * 0.35, anchor=anchor
        )

    angle = math.degrees(math.atan2(dy, dx))
    if angle > 90:
        angle -= 180
    elif angle < -90:
        angle += 180

    x = mid_x + px * gap
    y = mid_y + py * gap + LABEL_SIZE * 0.35
    return label(text, x, y, rotation=angle)


def relu_network(layers=(16, 16, 16), seed: int = 10, span: float = 6.0):
    """A real four-layer ReLU net with random weights -- the creases are genuine.

    Inputs are spread over a wide span and biases are loose so that plenty of
    unit boundaries fall inside the plotted square; that is what makes the
    surface fold rather than drift.
    """
    rng = np.random.default_rng(seed)
    weights = []
    sizes = (2,) + tuple(layers) + (1,)
    for fan_in, fan_out in zip(sizes[:-1], sizes[1:]):
        weights.append(
            (
                rng.normal(0, math.sqrt(2.0 / fan_in), size=(fan_in, fan_out)),
                rng.normal(0, 1.4, size=fan_out),
            )
        )

    def forward(debts, income):
        activation = np.stack(
            [
                (income.ravel() - 0.5) * span,
                (debts.ravel() - 0.5) * span,
            ],
            axis=1,
        )
        for index, (w, b) in enumerate(weights):
            activation = activation @ w + b
            if index < len(weights) - 1:
                activation = np.maximum(activation, 0.0)
        return activation.reshape(debts.shape)

    return forward


FIGURES = [
    (
        "fig-04-linear-remix.svg",
        lambda: curve_figure(lambda x: x),
    ),
    (
        "fig-05-nonlinear-remix.svg",
        lambda: curve_figure(lambda x: np.exp(3.2 * x)),
    ),
    (
        "fig-06-non-monotonic-remix.svg",
        lambda: curve_figure(lambda x: np.exp(-(((x - 0.45) / 0.17) ** 2))),
    ),
    (
        "fig-07-multidimensional-linear-remix.svg",
        lambda: surface_figure(
            lambda debts, income: 0.7 * income - 0.3 * debts,
            grid=14,
            z_fill=0.62,
            camera=(45.0, 22.0),
        ),
    ),
    (
        "fig-08-multidimensional-nonlinear-remix.svg",
        lambda: surface_figure(
            lambda debts, income: (debts - 0.5) ** 2 + (income - 0.5) ** 2,
            camera=(45.0, 20.0),
        ),
    ),
    (
        "fig-09-multidimensional-non-monotonic-a-remix.svg",
        lambda: surface_figure(
            lambda debts, income: 1.4 * (debts - 0.5) * (income - 0.5)
            + 0.40 * income
            - 0.40 * debts,
            z_fill=0.82,
            camera=(52.0, 16.0),
        ),
    ),
    (
        "fig-10-multidimensional-non-monotonic-b-remix.svg",
        lambda: surface_figure(
            lambda debts, income: np.sin(4.4 * income - 0.6) * np.cos(3.6 * debts + 0.4)
            + 0.55 * np.sin(6.5 * (income + debts)),
            grid=24,
            camera=(60.0, 18.0),
        ),
    ),
    (
        "fig-11-four-layer-neural-network-remix.svg",
        lambda: surface_figure(
            relu_network(), grid=30, mesh_width=0.6, camera=(20.0, 30.0)
        ),
    ),
]


def main() -> None:
    for name, build in FIGURES:
        path = OUT_DIR / name
        path.write_text(build(), encoding="utf-8")
        print(path.name)


if __name__ == "__main__":
    main()
