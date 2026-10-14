#!/usr/bin/env python3
"""Background-free dance loops for the experimental Week 8 "penguin parade" title slide.

NOTICE: this file was substantially drafted by an LLM coding system and has not yet been reviewed. Check every GIF against its source clip.

For each dance GIF in ../characters/ this script:
  1. lifts the penguin(s) off the background with Apple Vision's foreground instance mask (vision_mask.swift, macOS 14+, compiled on first run),
  2. finds the most seamless loop inside the clip (the start frame that best matches the frame after the loop's last frame) and never loops across a scene cut,
  3. crops to the dancer and caps the height at MAX_HEIGHT,
  4. retimes the loop to a whole number of beats at 125 BPM, picking the beat count closest to the clip's own tempo so each repeated move lands on a beat.

125 BPM is the tempo of Lane 8 & Robby East, "Penguin Parade" (../characters/lane8/). Measured with librosa over both MP3s: a robust line fit through the tracked beats gives 124.997 and the one-bar onset autocorrelation 124.99. One beat is 0.48 s, exactly 48 GIF centiseconds, so beat-aligned loops need no rounding.

Writes <character>-dance-<n>.gif and manifest.js, which slides/shared/includes/penguin-parade-after-body.html loads.

Usage:  uv run --with numpy --with pillow --with scipy python3 make_parade_gifs.py [clip ...]
"""

from __future__ import annotations

import json
import math
import subprocess
import sys
import tempfile
from dataclasses import dataclass
from pathlib import Path

import numpy as np
from PIL import Image
from scipy import ndimage

HERE = Path(__file__).resolve().parent
CHARACTERS = HERE.parent / "characters"
BPM = 125
BEAT_CS = 6000 // BPM  # 48 centiseconds
MAX_HEIGHT = 400
MIN_LOOP_S = 0.9
# A seam that jumps further than this (in typical frame steps) plays as a visible hitch, so the clip boomerangs instead.
MAX_SEAM = 0.6


@dataclass
class Clip:
    src: str
    # "all" keeps every subject Vision finds; "bluest" keeps the one Pablo-blue instance per frame.
    pick: str = "all"
    # Keep only the largest connected blob (drops props and background characters that Vision lifts too).
    largest: bool = False
    # The clip walks across the frame: cancel the drift so it struts in place, and report its pace.
    walk: bool = False
    # Loop the whole clip even when a shorter loop has a cleaner seam (keeps one-off moments like a blink).
    whole: bool = False
    # Drop frames from here on (an uploader's crossfade back to the start).
    last: int | None = None
    dither: bool = True


# Skipped on purpose: chilly-willy/dance-2 (axe and dog, no dance), pingu/dance-2 (Vision lifts the toy box with Pingu), pablo/dance-2 (cuts to a close-up; the wide shot lasts under a second), and the duplicate cuts mumble/dance-1, madagascar/dance-2 (captioned), madagascar/dance-3 (220 px copy), gunter/dance-1 and wheezy/dance-2 (smaller framings of the same scenes).
CLIPS = {
    "chilly-willy-dance-1": Clip("chilly-willy/dance-1.gif", whole=True, dither=False),
    "feathers-mcgraw-dance-1": Clip("feathers-mcgraw/dance-1.gif", dither=False),
    "feathers-mcgraw-dance-2": Clip("feathers-mcgraw/dance-2.gif", walk=True, dither=False),
    "gunter-dance-2": Clip("gunter/dance-2.gif", dither=False),
    "madagascar-dance-1": Clip("madagascar/dance-1.gif"),
    "madagascar-dance-2": Clip("madagascar/dance-2-nocaption.gif", last=41),
    "madagascar-dance-4": Clip("madagascar/dance-4.gif"),
    "madagascar-dance-5": Clip("madagascar/dance-5.gif"),
    "mumble-dance-2": Clip("mumble/dance-2.gif"),
    "pablo-dance-1": Clip("pablo/dance-1.gif", pick="bluest"),
    "pingu-dance-1": Clip("pingu/dance-1.gif"),
    "pororo-dance-1": Clip("pororo/dance-1.gif"),
    "pororo-dance-2": Clip("pororo/dance-2.gif"),
    "tux-dance-1": Clip("tux/dance-1.gif"),
    "tux-dance-2": Clip("tux/dance-2.gif"),
    "wheezy-dance-1": Clip("wheezy/dance-1.gif", largest=True),
}


def vision_tool() -> Path:
    src = HERE / "vision_mask.swift"
    exe = Path(tempfile.gettempdir()) / "penguin-parade-vision-mask"
    if not exe.exists() or exe.stat().st_mtime < src.stat().st_mtime:
        subprocess.run(["swiftc", "-O", str(src), "-o", str(exe)], check=True)
    return exe


def load_frames(path: Path) -> tuple[list[np.ndarray], list[int]]:
    im = Image.open(path)
    frames, delays = [], []
    for k in range(im.n_frames):
        im.seek(k)
        frames.append(np.asarray(im.convert("RGB")))
        # Browsers play a 0 or 1 cs delay at 10 cs.
        cs = round(im.info.get("duration", 100) / 10)
        delays.append(cs if cs >= 2 else 10)
    return frames, delays


def vision_masks(frames: list[np.ndarray], pick: str) -> list[np.ndarray]:
    """Soft foreground masks in [0, 1], one per frame."""
    with tempfile.TemporaryDirectory() as tmp:
        tmp = Path(tmp)
        paths = []
        for k, f in enumerate(frames):
            p = tmp / f"f{k:04d}.png"
            Image.fromarray(f).save(p)
            paths.append(str(p))
        subprocess.run([str(vision_tool()), str(tmp), *paths], check=True, capture_output=True)
        masks = []
        for k, f in enumerate(frames):
            if pick == "all":
                p = tmp / f"f{k:04d}_all.png"
                masks.append(np.asarray(Image.open(p), dtype=np.float32) / 255 if p.exists() else np.zeros(f.shape[:2], np.float32))
                continue
            best, best_score = np.zeros(f.shape[:2], np.float32), -np.inf
            for p in sorted(tmp.glob(f"f{k:04d}_i*.png")):
                m = np.asarray(Image.open(p), dtype=np.float32) / 255
                inside = m > 0.5
                if inside.sum() < 50:
                    continue
                rgb = f[inside].astype(np.float32)
                score = (rgb[:, 2] - rgb[:, 0]).mean()
                if score > best_score:
                    best, best_score = m, score
            masks.append(best)
    return masks


def clean(mask: np.ndarray, largest: bool) -> np.ndarray:
    """Drop specks (and with largest=True, every blob but the biggest) from a soft mask."""
    labels, n = ndimage.label(mask > 0.5)
    if n == 0:
        return mask
    areas = ndimage.sum(np.ones_like(mask), labels, range(1, n + 1))
    keep = [i + 1 for i, a in enumerate(areas) if (a == areas.max() if largest else a >= 0.12 * areas.max())]
    # Grow the kept blobs by a pixel so the soft edge survives the cut.
    region = ndimage.binary_dilation(np.isin(labels, keep), iterations=2)
    return mask * region


def stabilize(frames, masks, delays):
    """Cancel a steady walk across the frame. Returns shifted frames/masks, usable flags, and pace in px/s."""
    h, w = masks[0].shape
    xs, ts, usable = [], [], []
    t = 0.0
    for m, d in zip(masks, delays):
        on = m > 0.5
        cols = np.flatnonzero(on.any(axis=0))
        # The dancer must be wholly inside the frame for its position to mean anything.
        ok = cols.size > 0 and cols[0] > 1 and cols[-1] < w - 2
        usable.append(ok)
        xs.append(np.average(np.arange(w), weights=on.sum(axis=0)) if ok else np.nan)
        ts.append(t)
        t += d / 100
    xs, ts = np.array(xs), np.array(ts)
    ok = np.array(usable)
    pace, x0 = np.polyfit(ts[ok], xs[ok], 1)
    pad = int(abs(pace) * np.abs(ts - ts[ok].mean()).max()) + 4
    out_f, out_m = [], []
    for f, m, tt in zip(frames, masks, ts):
        dx = int(round(pace * tt + x0 - (pace * ts[ok].mean() + x0)))
        cf = np.zeros((h, w + 2 * pad, 3), f.dtype)
        cm = np.zeros((h, w + 2 * pad), m.dtype)
        cf[:, pad - dx:pad - dx + w] = f
        cm[:, pad - dx:pad - dx + w] = m
        out_f.append(cf)
        out_m.append(cm)
    return out_f, out_m, usable, abs(pace)


def features(frames, masks) -> np.ndarray:
    on = np.any([m > 0.5 for m in masks], axis=0)
    rows, cols = np.flatnonzero(on.any(axis=1)), np.flatnonzero(on.any(axis=0))
    y0, y1, x0, x1 = rows[0], rows[-1] + 1, cols[0], cols[-1] + 1
    scale = 64 / max(y1 - y0, x1 - x0)
    size = (max(1, round((x1 - x0) * scale)), max(1, round((y1 - y0) * scale)))
    out = []
    for f, m in zip(frames, masks):
        a = m[y0:y1, x0:x1, None]
        comp = f[y0:y1, x0:x1].astype(np.float32) * a + 128 * (1 - a)
        small = np.asarray(Image.fromarray(comp.astype(np.uint8)).resize(size, Image.BILINEAR), np.float32) / 255
        out.append(small.ravel())
    return np.array(out)


def distances(feat: np.ndarray) -> np.ndarray:
    sq = (feat ** 2).sum(axis=1)
    d2 = np.maximum(sq[:, None] + sq[None, :] - 2 * feat @ feat.T, 0)
    return np.sqrt(d2 / feat.shape[1])


def best_loop(D: np.ndarray, delays: list[int], usable: list[bool]) -> tuple[int, int, float]:
    """Pick frames [i, j) whose wrap-around jump looks like an ordinary step. Returns (i, j, seam cost in steps)."""
    n = len(delays)
    step = np.array([D[k, k + 1] for k in range(n - 1)])
    # Held (duplicated) frames would drag the typical step toward zero.
    med = np.median(step[step > 0.3 * np.median(step)])
    # A scene cut or a lighting flash is a step several times the typical one.
    breaks = {k + 1 for k in range(n - 1) if step[k] > 4 * med or not (usable[k] and usable[k + 1])}
    runs, start = [], 0
    for k in range(1, n + 1):
        if k == n or k in breaks:
            runs.append((start, k))
            start = k
    runs = [(a, b) for a, b in runs if usable[a]]
    min_s = min(MIN_LOOP_S, 0.7 * sum(delays) / 100)
    best = None
    for a, b in runs:
        for i in range(a, b):
            t = 0
            for j in range(i + 1, b + 1):
                t += delays[j - 1]
                if t / 100 < min_s:
                    continue
                if j < b:
                    seam = D[j, i] + (0.5 * D[j + 1, i + 1] if j + 1 < b else 0.5 * D[j, i])
                    seam /= 1.5
                elif i == a == 0 and b == n:
                    # The clip's own wrap: frame n-1 back to frame 0 may be no bigger than the steps on either side of it.
                    seam = max(0.0, D[n - 1, 0] - max(step[0], step[-1]))
                else:
                    continue
                cost = seam / med - 0.25 * min(t / 100, 6) / 6
                if best is None or cost < best[0]:
                    best = (cost, i, j, seam / med)
    _, i, j, seam = best
    return i, j, seam


def dance_beat(D: np.ndarray, delays: list[int], order: list[int]) -> tuple[float, float]:
    """The clip's own beat period (s) and its strength, from the periodicity of motion speed around the loop."""
    L = len(order)
    speed = []
    for k, f in enumerate(order):
        nxt = order[(k + 1) % L]
        speed += [D[f, nxt] / delays[f]] * delays[f]
    sig = np.array(speed) - np.mean(speed)
    ac = np.fft.irfft(np.abs(np.fft.rfft(sig)) ** 2, n=len(sig))
    ac /= ac[0]
    # Dance beats between 50 and 200 BPM, as long as the loop holds at least two of them.
    lo, hi = 30, min(120, len(sig) // 2)
    if hi <= lo:
        return 0.0, 0.0
    peaks = [k for k in range(lo, hi) if ac[k] >= ac[k - 1] and ac[k] > ac[k + 1]]
    if not peaks:
        return 0.0, 0.0
    lag = max(peaks, key=lambda k: ac[k])
    return lag / 100, float(ac[lag])


def beats_for(seconds: float, beat: float, strength: float) -> int:
    """Whole beats at BPM for the loop: map the clip's own beat onto the track's when the motion has a clear pulse."""
    best = None
    if strength >= 0.3:
        for per in (0.5, 1, 2):
            exact = per * seconds / beat
            B = max(1, round(exact))
            # Past this the dance stops looking like itself; fall back to the nearest whole-beat loop below.
            if not 0.8 <= seconds / (B * BEAT_CS / 100) <= 1.35:
                continue
            cost = abs(math.log(B * BEAT_CS / 100 / seconds)) + 2 * abs(B - exact) / max(exact, 1)
            if best is None or cost < best[0]:
                best = (cost, B)
        if best:
            return best[1]
    for B in range(1, 65):
        cost = abs(math.log(B * BEAT_CS / 100 / seconds)) + (0 if B % 4 == 0 or B < 3 else 0.04 if B % 2 == 0 else 0.1)
        if best is None or cost < best[0]:
            best = (cost, B)
    return best[1]


def retime(delays: list[int], beats: int) -> tuple[list[int], list[int]]:
    """Frame indices to keep and their new delays (cs), summing exactly to beats * BEAT_CS."""
    total = beats * BEAT_CS
    keep = list(range(len(delays)))
    d = [x * total / sum(delays) for x in delays]
    # Browsers clamp delays under 2 cs; also no point carrying more than ~33 fps.
    while sum(d) / len(d) < 3 and len(keep) > 2:
        keep = keep[::2]
        d = [sum(d[k:k + 2]) for k in range(0, len(d), 2)]
    cum = np.round(np.cumsum(d)).astype(int)
    cum[-1] = total
    out = np.diff(np.concatenate([[0], cum])).tolist()
    for k, x in enumerate(out):
        if x < 2:
            nb = (k + 1) % len(out)
            out[nb] -= 2 - x
            out[k] = 2
    return keep, out


def write_gif(path: Path, rgbs: list[np.ndarray], alphas: list[np.ndarray], delays: list[int], dither: bool) -> None:
    sample = np.concatenate([rgb[a] for rgb, a in zip(rgbs, alphas)])
    sample = sample[:: max(1, len(sample) // 200_000)]
    pal_img = Image.fromarray(sample[None, :, :]).quantize(255, method=Image.Quantize.MEDIANCUT)
    # Pad to a full 256 entries so index 255 (transparent) exists even when the clip needs fewer colors.
    palette = pal_img.getpalette()[: 255 * 3]
    palette += [0, 0, 0] * (256 - len(palette) // 3)
    pal_img.putpalette(palette)
    frames = []
    for rgb, a in zip(rgbs, alphas):
        q = Image.fromarray(rgb).quantize(palette=pal_img, dither=Image.Dither.FLOYDSTEINBERG if dither else Image.Dither.NONE)
        idx = np.asarray(q).copy()
        idx[~a] = 255
        fr = Image.fromarray(idx, "P")
        fr.putpalette(palette)
        frames.append(fr)
    frames[0].save(path, save_all=True, append_images=frames[1:], duration=[d * 10 for d in delays], loop=0, transparency=255, disposal=2, optimize=False)


def make(name: str, clip: Clip) -> dict:
    frames, delays = load_frames(CHARACTERS / clip.src)
    frames, delays = frames[:clip.last], delays[:clip.last]
    masks = [clean(m, clip.largest) for m in vision_masks(frames, clip.pick)]
    usable = [bool((m > 0.5).sum() > 100) for m in masks]
    pace = None
    if clip.walk:
        frames, masks, walk_ok, pace = stabilize(frames, masks, delays)
        usable = [u and w for u, w in zip(usable, walk_ok)]
    D = distances(features(frames, masks))
    i, j, seam = (0, len(delays), 0.0) if clip.whole else best_loop(D, delays, usable)
    order = list(range(i, j))
    if seam > MAX_SEAM:
        # Forward then back: seamless by construction, at the cost of the moves reversing.
        order += list(range(j - 2, i, -1))
    seconds = sum(delays[f] for f in order) / 100
    beat, strength = dance_beat(D, delays, order)
    beats = beats_for(seconds, beat, strength)

    on = np.any([m > 0.5 for m in masks[i:j]], axis=0)
    rows, cols = np.flatnonzero(on.any(axis=1)), np.flatnonzero(on.any(axis=0))
    h, w = on.shape
    # Subjects cut off by the bottom of the source frame are busts; the slide raises them from below the footer.
    bust = bool(rows[-1] >= h - 3)
    y0, y1 = max(rows[0] - 2, 0), min(rows[-1] + 3, h)
    x0, x1 = max(cols[0] - 2, 0), min(cols[-1] + 3, w)
    scale = min(1.0, MAX_HEIGHT / (y1 - y0))
    size = (round((x1 - x0) * scale), round((y1 - y0) * scale))

    keep, new_delays = retime([delays[f] for f in order], beats)
    rgbs, alphas = [], []
    for k in keep:
        f, m = frames[order[k]][y0:y1, x0:x1], masks[order[k]][y0:y1, x0:x1]
        rgbs.append(np.asarray(Image.fromarray(f).resize(size, Image.LANCZOS)))
        alphas.append(np.asarray(Image.fromarray((m * 255).astype(np.uint8)).resize(size, Image.BILINEAR)) >= 128)
    out = HERE / f"{name}.gif"
    write_gif(out, rgbs, alphas, new_delays, clip.dither)

    rate = seconds / (beats * BEAT_CS / 100)
    # Where the feet meet the floor, as a fraction of the height from the top: the median lowest opaque row, so jumps and stray pixels don't move it.
    foot = (np.median([np.flatnonzero(a.any(axis=1))[-1] for a in alphas if a.any()]) + 1) / size[1]
    entry = {"src": f"{name}.gif", "width": size[0], "height": size[1], "beats": beats, "bust": bust, "foot": round(float(foot), 4)}
    if pace is not None:
        # Body heights per second at the retimed speed, so the slide can move it without the feet sliding.
        entry["walk"] = round(pace * rate / (y1 - y0), 3)
    print(f"{name:26s} frames {i}-{j - 1} of {len(delays)}{' boomerang' if len(order) > j - i else ''} ({seconds:.2f}s, seam {seam:.2f} steps, own beat {beat:.2f}s @ {strength:.2f}) -> {beats} beats, x{rate:.2f} speed, {len(keep)} frames, {size[0]}x{size[1]}{' bust' if bust else ''}, {out.stat().st_size // 1024} KB")
    return entry


def main(names: list[str]) -> None:
    manifest_path = HERE / "manifest.js"
    entries = {}
    if manifest_path.exists() and names:
        text = manifest_path.read_text()
        old = json.loads(text[text.index("{"): text.rindex("}") + 1])
        entries = {Path(e["src"]).stem: e for e in old["clips"]}
    for name in names or CLIPS:
        entries[name] = make(name, CLIPS[name])
    clips = [entries[n] for n in CLIPS if n in entries]
    body = json.dumps({"bpm": BPM, "clips": clips}, indent=2)
    manifest_path.write_text(f"// Generated by make_parade_gifs.py; rerun it rather than editing by hand.\nwindow.PENGUIN_PARADE = {body};\n")


if __name__ == "__main__":
    main(sys.argv[1:])
