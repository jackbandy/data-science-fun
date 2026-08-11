#!/usr/bin/env python3
"""Generate lattice-qcd-slide.svg: a 1920x1080 slide with a subdivided lattice cube.

Emulates the lecture slide behind Bruce Banner in Spider-Man: Brand New Day
(reference frames + notes in SOURCES.md). Thin white wireframe cube of
3x3x3 cells on a sage-green gradient, glowing blue quark sphere on a site,
TIME up the left axis, QUARK/GLUON callouts, "Slide 9 of 22" footer.
Writes lattice-qcd-slide-v4.svg and lattice-qcd-slide-v4.png.
"""

import math
import shutil
import subprocess

W, H = 1920, 1080
N = 4  # sites per edge -> 3x3x3 lattice of cells

# Oblique projection: i -> right, j -> up (TIME), k -> depth (up-right).
CX, CY = 690, 800   # screen anchor for front-bottom-left site
A = 140             # lattice spacing on screen for x/y
DK = (78, -52)      # screen offset per unit depth


BAR_H = 70  # gray bar across the bottom of the screen


def project(i, j, k):
    return CX + i * A + k * DK[0], CY - j * A + k * DK[1]


def arrowhead(tipx, tipy, ang, size=30, spread=0.38):
    """Filled triangle with its tip at (tipx, tipy), pointing along ang."""
    p1 = (tipx - size * math.cos(ang - spread),
          tipy - size * math.sin(ang - spread))
    p2 = (tipx - size * math.cos(ang + spread),
          tipy - size * math.sin(ang + spread))
    return (
        f'<path d="M {tipx:.1f} {tipy:.1f} L {p1[0]:.1f} {p1[1]:.1f} '
        f'L {p2[0]:.1f} {p2[1]:.1f} Z" fill="#ffffff"/>'
    )


back_lines = []   # any line beyond the front slab of cubes (faded)
front_lines = []  # lines within the front layer of cubes (k <= 1)

for k in range(N):
    for j in range(N):
        for i in range(N):
            p = project(i, j, k)
            for di, dj, dk in ((1, 0, 0), (0, 1, 0), (0, 0, 1)):
                ii, jj, kk = i + di, j + dj, k + dk
                if ii >= N or jj >= N or kk >= N:
                    continue
                q = project(ii, jj, kk)
                (front_lines if k <= 1 and kk <= 1 else back_lines).append(
                    (p, q))

cube_cx = (project(0, 0, 0)[0] + project(N - 1, N - 1, N - 1)[0]) / 2
cube_cy = (project(0, 0, 0)[1] + project(N - 1, N - 1, N - 1)[1]) / 2

parts = [
    f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" '
    f'viewBox="0 0 {W} {H}" font-family="Helvetica, Arial, sans-serif">'
]

parts.append(f"""
<defs>
  <linearGradient id="bg" x1="0" y1="0" x2="0" y2="1">
    <stop offset="0%" stop-color="#2b5044"/>
    <stop offset="40%" stop-color="#4a7362"/>
    <stop offset="75%" stop-color="#7fa48c"/>
    <stop offset="100%" stop-color="#a9c2ab"/>
  </linearGradient>
  <radialGradient id="glow" cx="50%" cy="50%" r="50%">
    <stop offset="0%" stop-color="#ffffff" stop-opacity="0.28"/>
    <stop offset="60%" stop-color="#e8f2ea" stop-opacity="0.10"/>
    <stop offset="100%" stop-color="#e8f2ea" stop-opacity="0"/>
  </radialGradient>
  <radialGradient id="quark" cx="38%" cy="32%" r="70%">
    <stop offset="0%" stop-color="#ffffff"/>
    <stop offset="35%" stop-color="#b3a6f2"/>
    <stop offset="100%" stop-color="#6252c9"/>
  </radialGradient>
  <radialGradient id="quarkhalo" cx="50%" cy="50%" r="50%">
    <stop offset="0%" stop-color="#cfc4ff" stop-opacity="0.8"/>
    <stop offset="100%" stop-color="#cfc4ff" stop-opacity="0"/>
  </radialGradient>
</defs>
""")
parts.append(f'<rect width="{W}" height="{H-BAR_H}" fill="url(#bg)"/>')

# Soft glow behind the cube.
parts.append(
    f'<ellipse cx="{cube_cx:.0f}" cy="{cube_cy:.0f}" rx="620" ry="480" '
    'fill="url(#glow)"/>'
)

# Title: bold white, across the top.
parts.append(
    f'<text x="{W/2}" y="132" text-anchor="middle" font-size="72" '
    'font-weight="700" fill="#ffffff" letter-spacing="0.5">'
    'Lattice Quantum Chromodynamics (QCD)</text>'
)

# Lattice beams: uniform width; front layer of cubes full white,
# everything behind it faded.
for (x1, y1), (x2, y2) in back_lines:
    parts.append(
        f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="#ffffff" '
        'stroke-opacity="0.35" stroke-width="5" stroke-linecap="round"/>'
    )
for (x1, y1), (x2, y2) in front_lines:
    parts.append(
        f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="#ffffff" '
        'stroke-opacity="0.9" stroke-width="5" stroke-linecap="round"/>'
    )

# Gluons: orange arrows emitted from the quarks, running along links.
GLUON_SHAFT, GLUON_HEAD = '#f5a86b', '#ee8f52'
gluon_links = [  # (quark site, neighboring site the arrow points to)
    ((3, 2, 3), (3, 1, 3)),
    ((3, 2, 3), (2, 2, 3)),
    ((2, 2, 0), (1, 2, 0)),
    ((2, 2, 0), (2, 1, 0)),
]
for a, b in gluon_links:
    (x1, y1), (x2, y2) = project(*a), project(*b)
    ang = math.atan2(y2 - y1, x2 - x1)
    ax1, ay1_ = x1 + 22 * math.cos(ang), y1 + 22 * math.sin(ang)
    bx2, by2 = x2 - 26 * math.cos(ang), y2 - 26 * math.sin(ang)
    parts.append(
        f'<line x1="{ax1:.1f}" y1="{ay1_:.1f}" x2="{bx2:.1f}" y2="{by2:.1f}" '
        f'stroke="{GLUON_SHAFT}" stroke-width="10" stroke-linecap="round"/>'
    )
    p1 = (x2 - 34 * math.cos(ang - 0.5), y2 - 34 * math.sin(ang - 0.5))
    p2 = (x2 - 34 * math.cos(ang + 0.5), y2 - 34 * math.sin(ang + 0.5))
    parts.append(
        f'<path d="M {x2:.1f} {y2:.1f} L {p1[0]:.1f} {p1[1]:.1f} '
        f'L {p2[0]:.1f} {p2[1]:.1f} Z" fill="{GLUON_HEAD}"/>'
    )

# Quarks: glossy purple-blue spheres on a few lattice sites.
for site in ((3, 2, 3), (2, 2, 0)):
    sx, sy = project(*site)
    parts.append(f'<circle cx="{sx}" cy="{sy}" r="32" fill="url(#quarkhalo)"/>')
    parts.append(f'<circle cx="{sx}" cy="{sy}" r="16" fill="url(#quark)"/>')

# TIME axis: double-headed arrow alongside the cube's left edge, with
# straight witness lines from the cube corners out to the arrowhead tips.
ax = CX - 55
ay0, ay1 = CY, CY - (N - 1) * A
parts.append(
    f'<line x1="{ax}" y1="{ay0-30}" x2="{ax}" y2="{ay1+30}" '
    'stroke="#ffffff" stroke-width="5" stroke-linecap="round"/>'
)
parts.append(arrowhead(ax, ay1, -math.pi / 2))
parts.append(arrowhead(ax, ay0, math.pi / 2))
for ey in (ay0, ay1):
    parts.append(
        f'<line x1="{CX}" y1="{ey}" x2="{ax}" y2="{ey}" stroke="#ffffff" '
        'stroke-width="5" stroke-linecap="round"/>'
    )
mid_y = (ay0 + ay1) / 2
parts.append(
    f'<text x="{ax-30}" y="{mid_y}" text-anchor="middle" font-size="40" '
    f'font-weight="700" fill="#ffffff" letter-spacing="4" '
    f'transform="rotate(-90 {ax-30} {mid_y})">TIME</text>'
)

# QUARK: glowing blue sphere on the outer far-right edge of the lattice
# (back-right vertical edge, the rightmost silhouette edge), arrow + label.
qx, qy = project(N - 1, 2, N - 1)
parts.append(f'<circle cx="{qx}" cy="{qy}" r="34" fill="url(#quarkhalo)"/>')
parts.append(f'<circle cx="{qx}" cy="{qy}" r="15" fill="url(#quark)"/>')
tail = qx + 120
parts.append(
    f'<line x1="{qx+46}" y1="{qy}" x2="{tail}" y2="{qy}" stroke="#ffffff" '
    'stroke-width="5" stroke-linecap="round"/>'
)
parts.append(arrowhead(qx + 24, qy, math.pi))
parts.append(
    f'<text x="{tail+22}" y="{qy+15}" font-size="44" font-weight="700" '
    'fill="#ffffff" letter-spacing="2">QUARK</text>'
)

# GLUON: label at lower right pointing up-left at the gluon arrow emitted
# below the labeled quark.
g1, g2 = project(3, 2, 3), project(3, 1, 3)
gx, gy = (g1[0] + g2[0]) / 2 + 22, (g1[1] + g2[1]) / 2 + 26
tx, ty = gx + 60, gy + 160
ang = math.atan2(gy - ty, gx - tx)
sx2, sy2 = gx - 26 * math.cos(ang), gy - 26 * math.sin(ang)
parts.append(
    f'<line x1="{tx}" y1="{ty}" x2="{sx2:.1f}" y2="{sy2:.1f}" '
    'stroke="#ffffff" stroke-width="5" stroke-linecap="round"/>'
)
parts.append(arrowhead(gx, gy, ang))
parts.append(
    f'<text x="{tx+22}" y="{ty+16}" font-size="44" font-weight="700" '
    'fill="#ffffff" letter-spacing="2">GLUON</text>'
)

# SPACE: double-headed arrow under the cube's front-bottom edge, with
# straight witness lines from the cube corners down to the arrowhead tips.
s1, s2 = project(0, 0, 0), project(N - 1, 0, 0)
sy = s1[1] + 48
parts.append(
    f'<line x1="{s1[0]+30}" y1="{sy}" x2="{s2[0]-30}" y2="{sy}" '
    'stroke="#ffffff" stroke-width="5" stroke-linecap="round"/>'
)
parts.append(arrowhead(s1[0], sy, math.pi))
parts.append(arrowhead(s2[0], sy, 0))
for ex in (s1[0], s2[0]):
    parts.append(
        f'<line x1="{ex}" y1="{s1[1]}" x2="{ex}" y2="{sy}" '
        'stroke="#ffffff" stroke-width="5" stroke-linecap="round"/>'
    )
parts.append(
    f'<text x="{(s1[0]+s2[0])/2}" y="{sy+62}" text-anchor="middle" '
    'font-size="40" font-weight="700" fill="#ffffff" '
    'letter-spacing="4">SPACE</text>'
)

# Three circular presentation buttons (replay, prev, next) in the bottom
# right of the green area, above the gray bar.
by = H - BAR_H - 64
r = 28
for n, bx in enumerate((W - 234, W - 162, W - 90)):
    parts.append(
        f'<circle cx="{bx}" cy="{by}" r="{r}" fill="#141a22" '
        'fill-opacity="0.9"/>'
    )
    if n == 0:  # Material Design "refresh" glyph, flipped horizontally
        refresh_path = (
            'M17.65 6.35A7.958 7.958 0 0 0 12 4c-4.42 0-7.99 3.58-8 8'
            's3.57 8 8 8c3.73 0 6.84-2.55 7.73-6h-2.08A5.99 5.99 0 0 1 '
            '12 18c-3.31 0-6-2.69-6-6s2.69-6 6-6c1.66 0 3.14.69 4.22 '
            '1.78L13 11h7V4l-2.35 2.35z'
        )
        parts.append(
            f'<g transform="translate({bx} {by}) scale(-1.5 1.5) '
            'translate(-12 -12)">'
            f'<path d="{refresh_path}" fill="#ffffff"/></g>'
        )
    elif n == 1:  # previous: left-pointing triangle
        parts.append(
            f'<path d="M {bx-11} {by} L {bx+8} {by-12} L {bx+8} {by+12} Z" '
            'fill="#ffffff"/>'
        )
    else:  # next: right-pointing triangle
        parts.append(
            f'<path d="M {bx+11} {by} L {bx-8} {by-12} L {bx-8} {by+12} Z" '
            'fill="#ffffff"/>'
        )

# Gray bar across the bottom with the slide counter.
parts.append(
    f'<rect y="{H-BAR_H}" width="{W}" height="{BAR_H}" fill="#4b4b4b"/>'
)
parts.append(
    f'<text x="{W-64}" y="{H-BAR_H/2+8}" text-anchor="end" font-size="24" '
    'font-weight="700" fill="#e9e9e9">Slide 9 of 22</text>'
)

parts.append('</svg>')

with open('lattice-qcd-slide-v4.svg', 'w') as f:
    f.write('\n'.join(parts) + '\n')
print('wrote lattice-qcd-slide-v4.svg')

if shutil.which('rsvg-convert'):
    subprocess.run(
        ['rsvg-convert', '-w', str(W), '-h', str(H),
         '-o', 'lattice-qcd-slide-v4.png', 'lattice-qcd-slide-v4.svg'],
        check=True,
    )
    print('wrote lattice-qcd-slide-v4.png')
else:
    print('rsvg-convert not found; skipped PNG export')
