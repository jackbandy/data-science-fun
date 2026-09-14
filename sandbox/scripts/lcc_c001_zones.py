"""Draft: overlay seating zones on the LCC C001 floor plan.

The rows are concentric arcs. Center and radii were fitted from the plan image
(see geom notes); PNG pixel coords + 100 = SVG user units, since the plan image
is placed at (100, 100) at its native size.
"""
import math, re, sys, colorsys

CX, CY = 986.0, -180.0          # fan center, SVG units
ROWS = {                        # row -> radius of the desk front edge
    1: 668, 2: 788, 3: 908, 4: 1027, 5: 1147, 6: 1266, 7: 1386, 8: 1505, 9: 1625,
}
PAD_IN, PAD_OUT = 12, 104       # band runs from just in front of the desk to behind the chairs

# (row, theta_start, theta_end) in degrees, front to back. Angles were read off the
# chair glyphs detected in the plan: every split falls in a gap between two seats,
# and the left/middle/right splits line up across rows 4-7 at +/- 6.9 degrees.
ZONES = [
    (1, -19.0, 20.5),
    (2, -23.0, -0.8), (2, 0.8, 23.0),
    (3, -24.5, -0.8), (3, 0.8, 24.5),
    (4, -25.2, -7.7), (4, -6.1, 6.1), (4, 7.7, 25.2),
    (5, -25.5, -7.7), (5, -6.1, 6.1), (5, 7.7, 25.5),
    (6, -25.5, -7.7), (6, -6.1, 6.1), (6, 7.7, 25.5),
    (7, -19.5, -7.7), (7, -6.1, 6.1), (7, 7.7, 19.5),
    (8, -14.5, -0.8), (8, 0.8, 14.5),
]
BACK = (-9.0, 9.0)              # the last two rows together: row 9 plus the two rear tables
BACK_IN, BACK_OUT = ROWS[9] - 12, 1905

def pt(theta, r):
    t = math.radians(theta)
    return CX + r * math.sin(t), CY + r * math.cos(t)

def band(t0, t1, r0, r1):
    ax, ay = pt(t0, r0); bx, by = pt(t1, r0)
    cx, cy = pt(t1, r1); dx, dy = pt(t0, r1)
    return (f"M {ax:.1f} {ay:.1f} A {r0:.1f} {r0:.1f} 0 0 0 {bx:.1f} {by:.1f} "
            f"L {cx:.1f} {cy:.1f} A {r1:.1f} {r1:.1f} 0 0 1 {dx:.1f} {dy:.1f} Z")

def color(i):
    h = (i * 0.381966) % 1.0                     # golden angle: neighbors get far-apart hues
    fill = colorsys.hls_to_rgb(h, 0.62, 0.78)
    edge = colorsys.hls_to_rgb(h, 0.34, 0.85)
    hexit = lambda c: "#%02x%02x%02x" % tuple(round(v * 255) for v in c)
    return hexit(fill), hexit(edge)

out = ['<g id="zones">']
specs = [(row, t0, t1, ROWS[row] - PAD_IN, ROWS[row] + PAD_OUT) for row, t0, t1 in ZONES]
specs.append((9, BACK[0], BACK[1], BACK_IN, BACK_OUT))
for i, (row, t0, t1, r0, r1) in enumerate(specs):
    fill, edge = color(i)
    out.append(f'  <path d="{band(t0, t1, r0, r1)}" fill="{fill}" fill-opacity="0.42" stroke="{edge}" stroke-width="4" stroke-linejoin="round"/>')
    lx, ly = pt((t0 + t1) / 2, (r0 + r1) / 2)
    out.append(f'  <text x="{lx:.1f}" y="{ly:.1f}" text-anchor="middle" dominant-baseline="central" font-family="Helvetica, Arial, sans-serif" font-size="52" font-weight="bold" fill="{edge}" fill-opacity="0.85">{i + 1}</text>')
out.append('</g>')

src = open(sys.argv[1]).read()
assert src.rstrip().endswith('</svg>')
dst = src.rstrip()[: -len('</svg>')] + "\n".join(out) + "\n</svg>\n"
open(sys.argv[2], 'w').write(dst)
print("zones:", len(specs))
