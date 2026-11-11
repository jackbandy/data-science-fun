"""Looping "move toward the front" GIFs drawn over the LCC C001 floor plan (LCC_C001_crop.svg).

NOTICE: this file was drafted by an LLM coding system and has not yet been reviewed. Check every GIF against the slide it illustrates.

Ten options, one GIF each. v10 is the one chosen for the slides.

v1 to v5 are faded streams. Every mark travels along a radius of the seating arcs (the rows in LCC_C001_groups_rectangle.svg are circles around CENTER), so it crosses each row at a right angle, heads for the top center of the room, and fades out inside the front row. Marks are the STYLE.md orange at FADE opacity, multiplied under the plan's linework so the drawing stays crisp. Each loop advances the pattern by exactly one spacing, so the last frame hands off to the first.

v6 to v9 put one full-strength orange dot on every seat (chairs and wheelchair spaces, found in the plan's linework) except the very back row. Each loop every dot moves up one row to the seat nearest its own angle, the front row's dots stay put, and new dots fade in from behind wherever a seat has nobody arriving. The timing is the Datasaurus loop's (orange-line/sandbox/make_datasaurus_gif_og.py): a 0.64 s hold, then 12 smoothstepped frames at 25 fps.

v10 is v6 with three changes. The front row's dots sit on one arc (the row's median radius) instead of following its two offset seats. The front FULL_ROWS rows are full strength and the rows behind fade steadily to BACK_OPACITY. No two dots ever head for the same seat behind the front row: rows narrow toward the front, so each row keeps only as many dots as the second row has seats, and the empty seats are a seeded random draw (the same every run).

Needs rsvg-convert on PATH (brew install librsvg).

Usage:  docs/slides/.venv/bin/python3 make_lcc_c001_front_gifs.py
"""

import functools
import io
import math
import random
import subprocess
from pathlib import Path

import numpy as np
from PIL import Image, ImageChops
from scipy import ndimage

HERE = Path(__file__).resolve().parent
PLAN = HERE / "LCC_C001_crop.svg"
VIEW_W, VIEW_H = 1975, 2115
OUT_W = 900
FRAME_MS = 50

ORANGE = "#f9461c"
FADE = 0.45

CENTER = (986.0, -180.0)  # shared center of the seating arcs
ROW_PITCH = 120.0  # radial distance between rows
R_END = 705.0  # inside the front row (radii 656 to 772)
R_BACK = 1560.0  # just behind the last full row
FADE_IN, FADE_OUT = 170.0, 120.0


def pt(r, deg):
    th = math.radians(deg)
    return CENTER[0] + r * math.sin(th), CENTER[1] + r * math.cos(th)


def smooth(x):
    x = min(1.0, max(0.0, x))
    return x * x * (3 - 2 * x)


def envelope(r):
    return smooth((R_BACK - r) / FADE_IN) * smooth((r - R_END) / FADE_OUT)


def poly(points):
    return " ".join(f"{x:.1f},{y:.1f}" for x, y in points)


def head(r_tip, deg, length=36.0, half=17.0):
    bx, by = pt(r_tip + length, deg)
    th = math.radians(deg)
    px, py = math.cos(th) * half, -math.sin(th) * half
    return [pt(r_tip, deg), (bx + px, by + py), (bx - px, by - py)]


def chevrons(t):
    out = []
    for deg in range(-15, 16, 5):
        for k in range(8):
            r = R_END + (k + 1 - t) * ROW_PITCH
            a = envelope(r)
            if a > 0.01:
                tip, left, right = head(r, deg, length=18.0, half=26.0)
                out.append(f'<polyline points="{poly([left, tip, right])}" fill="none" stroke="{ORANGE}" stroke-width="9" stroke-linecap="round" stroke-linejoin="round" opacity="{a:.3f}"/>')
    return out


def dots(t):
    out = []
    spacing = ROW_PITCH / 2
    for i, deg in enumerate([-18, -13.5, -9, -4.5, 0, 4.5, 9, 13.5, 18]):
        for k in range(-1, 16):  # -1 covers the half-step lanes at the front
            r = R_END + (k + 1 - t + 0.5 * (i % 2)) * spacing
            a = envelope(r)
            if a > 0.01:
                x, y = pt(r, deg)
                out.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="10" fill="{ORANGE}" opacity="{a:.3f}"/>')
    return out


def dashed_arrows(t):
    dash, gap = 27.0, 24.0  # STYLE.md "9 8" at stroke-width 3, scaled to stroke-width 9
    out = []
    for i, deg in enumerate([-16, -8, 0, 8, 16]):
        x1, y1 = pt(R_BACK, deg)
        x2, y2 = pt(R_END + 40, deg)
        gx, gy = pt(R_BACK - 260, deg)
        out.append(f'<linearGradient id="g{i}" gradientUnits="userSpaceOnUse" x1="{x1:.1f}" y1="{y1:.1f}" x2="{gx:.1f}" y2="{gy:.1f}"><stop offset="0" stop-color="{ORANGE}" stop-opacity="0"/><stop offset="1" stop-color="{ORANGE}" stop-opacity="1"/></linearGradient>')
        out.append(f'<line x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}" stroke="url(#g{i})" stroke-width="9" stroke-dasharray="{dash} {gap}" stroke-dashoffset="{-t * (dash + gap):.2f}"/>')
        out.append(f'<polygon points="{poly(head(R_END, deg, length=45.0, half=22.5))}" fill="{ORANGE}"/>')
    return out


def arcs(t):
    out = []
    span = 18.0
    for k in range(8):
        r = R_END + (k + 1 - t) * ROW_PITCH
        a = envelope(r)
        if a > 0.01:
            (x1, y1), (x2, y2) = pt(r, -span), pt(r, span)
            out.append(f'<path d="M {x1:.1f} {y1:.1f} A {r:.1f} {r:.1f} 0 0 0 {x2:.1f} {y2:.1f}" fill="none" stroke="{ORANGE}" stroke-width="10" stroke-linecap="round" opacity="{a:.3f}"/>')
    return out


def tapered_arrows(t):
    spacing = 2 * ROW_PITCH
    tail = 190.0
    out = []
    n = 0
    for i, deg in enumerate(range(-15, 16, 5)):
        phase = (i * 0.382) % 1  # golden-ratio stagger so neighboring lanes are out of step
        for k in range(-1, 5):  # -1 covers the phase-shifted lanes at the front
            r = R_END + (k + 1 - t + phase) * spacing
            a = envelope(r)
            if a > 0.01:
                tip, left, right = head(r, deg)
                bx, by = (left[0] + right[0]) / 2, (left[1] + right[1]) / 2
                th = math.radians(deg)
                px, py = math.cos(th) * 6, -math.sin(th) * 6
                ex, ey = pt(r + tail, deg)
                out.append(f'<linearGradient id="t{n}" gradientUnits="userSpaceOnUse" x1="{ex:.1f}" y1="{ey:.1f}" x2="{bx:.1f}" y2="{by:.1f}"><stop offset="0" stop-color="{ORANGE}" stop-opacity="0"/><stop offset="1" stop-color="{ORANGE}" stop-opacity="1"/></linearGradient>')
                out.append(f'<g opacity="{a:.3f}"><polygon points="{poly([(ex, ey), (bx + px, by + py), (bx - px, by - py)])}" fill="url(#t{n})"/><polygon points="{poly([tip, left, right])}" fill="{ORANGE}"/></g>')
                n += 1
    return out


def rasterize(svg_bytes, width=OUT_W):
    png = subprocess.run(["rsvg-convert", "-w", str(width), "-f", "png"], input=svg_bytes, check=True, capture_output=True).stdout
    return Image.open(io.BytesIO(png)).convert("RGB")


@functools.cache
def seat_rows():
    """Seats as (radius, angle, x, y), grouped into rows from front to back."""
    gray = np.asarray(rasterize(PLAN.read_bytes(), VIEW_W).convert("L"))
    labels, _ = ndimage.label(gray > 200)
    seats = []
    for i, box in enumerate(ndimage.find_objects(labels), start=1):
        h, w = (s.stop - s.start for s in box)
        if 30 < h < 60 and 30 < w < 60:
            mask = labels[box] == i
            if 1300 < mask.sum() < 1750:  # the enclosed seat of a chair (about 1410 px) or wheelchair (about 1655 px)
                cy, cx = ndimage.center_of_mass(mask)
                dx, dy = cx + box[1].start + 0.5 - CENTER[0], cy + box[0].start + 0.5 - CENTER[1]
                seats.append((math.hypot(dx, dy), math.degrees(math.atan2(dx, dy)), dx + CENTER[0], dy + CENTER[1]))
    seats.sort()
    rows = [[seats[0]]]
    for seat in seats[1:]:
        if seat[0] - rows[-1][-1][0] > 40:
            rows.append([])
        rows[-1].append(seat)
    return rows


@functools.cache
def seat_moves():
    """Each move is (start xy, end xy, fades in)."""
    rows = seat_rows()
    moves = []
    for k in range(1, len(rows)):
        ahead, taken = rows[k - 1], set()
        for _, deg, x, y in rows[k]:
            target = min(ahead, key=lambda seat: abs(seat[1] - deg))
            taken.add(target)
            moves.append(((x, y), target[2:], k == len(rows) - 1))
        if k > 1:  # the front row keeps its own dots
            moves += [(pt(seat[0] + ROW_PITCH, seat[1]), seat[2:], True) for seat in ahead if seat not in taken]
    return moves


DOT_R = 15.0


def seat_dots(t, trails=False, front_rings=False, seat_rings=False):
    rows = seat_rows()
    out, dots_out = [], []
    if seat_rings:
        out += [f'<circle cx="{x:.1f}" cy="{y:.1f}" r="20" fill="none" stroke="{ORANGE}" stroke-width="3"/>' for row in rows for _, _, x, y in row]
    for _, _, x, y in rows[0]:
        if front_rings:
            out.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="24" fill="none" stroke="{ORANGE}" stroke-width="4"/>')
        dots_out.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{DOT_R}" fill="{ORANGE}" opacity="1.000"/>')
    for n, ((x0, y0), (x1, y1), fades_in) in enumerate(seat_moves()):
        x, y = x0 + (x1 - x0) * t, y0 + (y1 - y0) * t
        a = t if fades_in else 1.0
        if trails and 0 < t < 1:
            out.append(f'<linearGradient id="s{n}" gradientUnits="userSpaceOnUse" x1="{x0:.1f}" y1="{y0:.1f}" x2="{x:.1f}" y2="{y:.1f}"><stop offset="0" stop-color="{ORANGE}" stop-opacity="0"/><stop offset="1" stop-color="{ORANGE}" stop-opacity="1"/></linearGradient>')
            out.append(f'<line x1="{x0:.1f}" y1="{y0:.1f}" x2="{x:.1f}" y2="{y:.1f}" stroke="url(#s{n})" stroke-width="{DOT_R * 1.3:.1f}" opacity="{0.6 * a * math.sin(math.pi * t):.3f}"/>')
        if a > 0:
            dots_out.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{DOT_R}" fill="{ORANGE}" opacity="{a:.3f}"/>')
    return out + list(dict.fromkeys(dots_out))  # dots that have merged on one seat are drawn once, so the end of the move matches the first frame


FULL_ROWS = 3  # rows from the front drawn at full strength
BACK_OPACITY = 0.3  # opacity of the last row that holds dots at rest


def row_opacity(k):
    last = len(seat_rows()) - 2
    if k > last:
        return 0.0
    return 1.0 - (1.0 - BACK_OPACITY) * max(0, k - (FULL_ROWS - 1)) / (last - (FULL_ROWS - 1))


@functools.cache
def fading_moves():
    """(front-row dots, moves); each move is (start xy, end xy, start opacity, end opacity) and no two moves end on one seat behind the front row."""
    rows = [sorted(row, key=lambda seat: seat[1]) for row in seat_rows()]
    front_r = sorted(seat[0] for seat in rows[0])[len(rows[0]) // 2]
    front = [(deg, pt(front_r, deg)) for _, deg, _, _ in rows[0]]
    cap = len(rows[1])  # a row can only send forward as many dots as the row ahead has seats, so every row keeps at most this many
    rng = random.Random(418)
    best = None
    for _ in range(4000):  # random gaps, keeping the draw whose dots drift sideways the least
        kept = [row if len(row) <= cap else [row[i] for i in sorted(rng.sample(range(len(row)), cap))] for row in rows]
        drift = max(abs(a[1] - b[1]) for k in range(2, len(rows) - 2) for a, b in zip(kept[k], kept[k - 1]))
        if best is None or drift < best[0]:
            best = (drift, kept)
    kept = best[1]
    moves = [((x, y), min(front, key=lambda f: abs(f[0] - deg))[1], 1.0, 1.0) for _, deg, x, y in kept[1]]
    for k in range(2, len(rows)):
        ahead, behind = kept[k - 1], kept[k]
        if len(behind) == len(ahead):
            pairs = list(zip(behind, ahead))
        else:  # the short rows at the back: each dot takes the nearest seat ahead
            pairs = [(seat, min(ahead, key=lambda a: abs(a[1] - seat[1]))) for seat in behind]
        taken = {target for _, target in pairs}
        moves += [(seat[2:], target[2:], row_opacity(k), row_opacity(k - 1)) for seat, target in pairs]
        moves += [(pt(seat[0] + ROW_PITCH, seat[1]), seat[2:], 0.0, row_opacity(k - 1)) for seat in ahead if seat not in taken]
    return [xy for _, xy in front], moves


def seat_dots_fading(t):
    front, moves = fading_moves()
    out = [f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{DOT_R}" fill="{ORANGE}" opacity="1.000"/>' for x, y in front]
    for (x0, y0), (x1, y1), a0, a1 in moves:
        a = a0 + (a1 - a0) * t
        if a > 0:
            out.append(f'<circle cx="{x0 + (x1 - x0) * t:.1f}" cy="{y0 + (y1 - y0) * t:.1f}" r="{DOT_R}" fill="{ORANGE}" opacity="{a:.3f}"/>')
    return list(dict.fromkeys(out))  # a dot arriving in the front row lands on the dot already there


def steady(n):
    return [i / n for i in range(n)], [FRAME_MS] * n


MORPH = [0.0] + [smooth(step / 13) for step in range(1, 13)], [640] + [40] * 12  # the Datasaurus loop's hold and morph

# name -> (draw function, (loop positions, frame durations in ms), orange opacity)
OPTIONS = {
    "v1-chevrons": (chevrons, steady(40), FADE),
    "v2-dots": (dots, steady(20), FADE),
    "v3-dashed-arrows": (dashed_arrows, steady(17), FADE),
    "v4-arcs": (arcs, steady(40), FADE),
    "v5-tapered-arrows": (tapered_arrows, steady(60), FADE),
    "v6-seat-dots": (seat_dots, MORPH, 1.0),
    "v7-seat-dots-trails": (functools.partial(seat_dots, trails=True), MORPH, 1.0),
    "v8-seat-dots-front-rings": (functools.partial(seat_dots, front_rings=True), MORPH, 1.0),
    "v9-seat-dots-seat-rings": (functools.partial(seat_dots, seat_rings=True), MORPH, 1.0),
    "v10-seat-dots-fading": (seat_dots_fading, MORPH, 1.0),
}


def overlay(elements, fade=FADE):
    body = "\n".join(elements)
    svg = f'<svg xmlns="http://www.w3.org/2000/svg" width="{VIEW_W}" height="{VIEW_H}" viewBox="0 0 {VIEW_W} {VIEW_H}"><rect width="{VIEW_W}" height="{VIEW_H}" fill="#ffffff"/><g opacity="{fade}">{body}</g></svg>'
    return rasterize(svg.encode())


def palette_image(fade):
    o = [int(ORANGE[i : i + 2], 16) / 255 for i in (1, 3, 5)]
    pal = []
    for j in range(12):  # orange strength, 0 to fade
        a = fade * j / 11
        for i in range(16):  # plan linework, black to white
            g = i / 15
            pal += [round(255 * g * (1 - a + a * c)) for c in o]
    img = Image.new("P", (1, 1))
    img.putpalette(pal + [0] * (768 - len(pal)))
    return img


def main():
    plan = rasterize(PLAN.read_bytes())
    for name, (draw, (times, durations), fade) in OPTIONS.items():
        pal = palette_image(fade)
        frames = [ImageChops.multiply(plan, overlay(draw(t), fade)).quantize(palette=pal, dither=Image.Dither.NONE) for t in times]
        path = HERE / f"LCC_C001_front-{name}.gif"
        frames[0].save(path, save_all=True, append_images=frames[1:], duration=durations, loop=0, optimize=False)
        print(f"{path.name}: {len(frames)} frames, {sum(durations) / 1000:.2f} s loop, {path.stat().st_size / 1e6:.2f} MB")


if __name__ == "__main__":
    main()
