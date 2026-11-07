#!/usr/bin/env python3
"""Fetch openly licensed headshots of Bulls players from Wikimedia Commons.

NOTICE: this file was substantially drafted by an LLM coding system and has not
yet been thoroughly reviewed.

For each player in the Bulls co-play network (bulls_data.py):
  1. Wikidata maps the player's ESPN ID (property P3685) to an item, and that
     item's image (P18) to a file on Wikimedia Commons.
  2. The Commons API gives a resized copy plus the file's license and author.
     Only public-domain, CC0, CC BY, and CC BY-SA files are used.
  3. The resized original is cached in .cache/originals/ (gitignored).
  4. OpenCV's YuNet face detector (downloaded once to .cache/, checksum
     verified) finds the face; the photo is cropped to a square around it, or
     to a hand-set box in OVERRIDES, or to the top-center square when no face
     is found, and saved as headshots/<espn id>.jpg, 256 x 256. Photos listed
     in SKIP (player not identifiable) are left out.
  5. headshots/credits.csv records, per file: player, Commons page, author,
     license, and how the crop was placed (face, manual, or fallback).

Players without an open Commons photo get no file; the figures draw their
initials instead.

Usage:  python3 fetch_headshots.py           (fetches only new players, re-crops all)
        python3 fetch_headshots.py --force   (refetch everything)
"""

from __future__ import annotations

import collections
import csv
import hashlib
import html
import json
import re
import sys
import time
import urllib.parse
import urllib.request
from io import BytesIO
from pathlib import Path

import cv2
import numpy as np
from PIL import Image

from bulls_data import build_graph, display_name, espn_id, load_games

OUT_DIR = Path(__file__).resolve().parent / "headshots"
CREDITS = OUT_DIR / "credits.csv"
USER_AGENT = "data-science-fun-course-figures/0.1 (https://github.com/jackbandy/data-science-fun)"
SIZE = 256
OPEN_LICENSES = re.compile(r"^(public domain|pd|cc0|cc[- ]by(-sa)?( \d\.\d)?)", re.I)


def get_json(url: str):
    req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    with urllib.request.urlopen(req, timeout=60) as resp:
        return json.load(resp)


def wikidata_images(ids):
    """{espn id: Commons file name} for players whose Wikidata item has an image."""
    values = " ".join(f'"{i}"' for i in ids)
    query = f"SELECT ?espn ?img WHERE {{ VALUES ?espn {{{values}}} ?item wdt:P3685 ?espn ; wdt:P18 ?img . }}"
    rows = get_json("https://query.wikidata.org/sparql?format=json&query="
                    + urllib.parse.quote(query))["results"]["bindings"]
    out = {}
    for r in rows:
        name = urllib.parse.unquote(r["img"]["value"].rsplit("/", 1)[1])
        out.setdefault(r["espn"]["value"], name)
    return out


def commons_info(filename: str):
    params = urllib.parse.urlencode({
        "action": "query", "format": "json", "prop": "imageinfo",
        "titles": f"File:{filename}", "iiprop": "url|extmetadata", "iiurlwidth": 800,
    })
    page = next(iter(get_json(f"https://commons.wikimedia.org/w/api.php?{params}")["query"]["pages"].values()))
    info = page["imageinfo"][0]
    meta = info.get("extmetadata", {})
    strip = lambda s: html.unescape(re.sub(r"<[^>]+>", "", s or "")).strip()
    return {
        "thumb": info.get("thumburl") or info["url"],
        "page": info["descriptionurl"],
        "license": strip(meta.get("LicenseShortName", {}).get("value")),
        "license_url": meta.get("LicenseUrl", {}).get("value", ""),
        "author": strip(meta.get("Artist", {}).get("value")),
    }


CACHE = Path(__file__).resolve().parent / ".cache"          # gitignored
ORIGINALS = CACHE / "originals"
YUNET = CACHE / "face_detection_yunet_2023mar.onnx"
YUNET_URL = ("https://github.com/opencv/opencv_zoo/raw/main/models/"
             "face_detection_yunet/face_detection_yunet_2023mar.onnx")
YUNET_SHA256 = "8f2383e4dd3cfbb4553ea8718107fc0423210dc964f9f4280604804ed2552fa4"

# Hand fixes after reviewing the contact sheet: espn id -> (center x, center y, side),
# as fractions of the original image's width, height, and shorter side.
OVERRIDES: dict[str, tuple[float, float, float]] = {
    "3207": (0.62, 0.40, 0.30),   # Aaron Gray: the detector picked a Wizards player behind him
    "3032": (0.65, 0.41, 0.45),    # Tyrus Thomas: a second face nearly as large
    "189": (0.66, 0.17, 0.50),     # Antonio Davis: no face detected (small photo)
    "285": (0.60, 0.25, 0.55),     # Adrian Griffin: photographed from behind
    "3229": (0.52, 0.17, 0.55),    # Chris Richard: full-length, small photo
}
# Photos that cannot be tied to the player with confidence: no headshot, initials instead.
SKIP = {
    "2221": "Linton Johnson: two players in the photo, unclear which is him",
}


def face_detector():
    if not YUNET.exists():
        CACHE.mkdir(exist_ok=True)
        req = urllib.request.Request(YUNET_URL, headers={"User-Agent": USER_AGENT})
        with urllib.request.urlopen(req, timeout=60) as resp:
            YUNET.write_bytes(resp.read())
    if hashlib.sha256(YUNET.read_bytes()).hexdigest() != YUNET_SHA256:
        raise SystemExit(f"Unexpected checksum for {YUNET}; delete it and rerun.")
    return cv2.FaceDetectorYN.create(str(YUNET), "", (320, 320), 0.7, 0.3, 5000)


def crop_headshot(img: Image.Image, detector, override=None):
    """Square crop around the most prominent face; top-center square otherwise.

    Returns the 256 x 256 crop and how it was placed: "face", "manual", or "fallback".
    """
    rgb = img.convert("RGB")
    w, h = rgb.size
    if override:
        fx, fy, fs = override
        side, cx, cy, how = fs * min(w, h), fx * w, fy * h, "manual"
    else:
        bgr = cv2.cvtColor(np.asarray(rgb), cv2.COLOR_RGB2BGR)
        detector.setInputSize((w, h))
        _, faces = detector.detect(bgr)
        if faces is not None and len(faces):
            # most prominent: confidence weighted by face size
            x, y, fw, fh = max(faces, key=lambda f: f[-1] * (f[2] * f[3]) ** 0.5)[:4]
            side, cx, cy, how = fw * 2.6, x + fw / 2, y + fh * 0.6, "face"
        else:
            side, cx, cy, how = min(w, h), w / 2, min(w, h) / 2, "fallback"
    side = min(side, w, h)
    left = min(max(cx - side / 2, 0), w - side)
    top = min(max(cy - side / 2, 0), h - side)
    crop = rgb.crop((round(left), round(top), round(left + side), round(top + side)))
    return crop.resize((SIZE, SIZE), Image.LANCZOS), how


def main(force: bool = False):
    OUT_DIR.mkdir(exist_ok=True)
    ORIGINALS.mkdir(parents=True, exist_ok=True)
    games, _ = load_games()
    players = sorted(build_graph(games))
    names = {espn_id(p): display_name(p) for p in players}
    rows = {}
    if CREDITS.exists() and not force:
        with open(CREDITS) as f:
            rows = {r["espn_id"]: r for r in csv.DictReader(f)}
    images = wikidata_images(sorted(names))
    print(f"{len(players)} players, {len(images)} with a Commons image on Wikidata")
    for pid in SKIP:
        rows.pop(pid, None)
        (OUT_DIR / f"{pid}.jpg").unlink(missing_ok=True)
    for pid, filename in sorted(images.items()):
        if pid in SKIP:
            continue
        original = ORIGINALS / f"{pid}.jpg"
        if pid in rows and original.exists() and not force:
            continue
        try:
            info = commons_info(filename)
        except Exception as e:  # network or API hiccup: skip, rerun later
            print(f"  skip {names[pid]}: {e}")
            continue
        if not OPEN_LICENSES.match(info["license"]):
            print(f"  skip {names[pid]}: license {info['license']!r}")
            continue
        req = urllib.request.Request(info["thumb"], headers={"User-Agent": USER_AGENT})
        with urllib.request.urlopen(req, timeout=60) as resp:
            Image.open(BytesIO(resp.read())).convert("RGB").save(original, quality=95)
        rows[pid] = {"espn_id": pid, "player": names[pid], "file": f"{pid}.jpg",
                     "commons_page": info["page"], "author": info["author"],
                     "license": info["license"], "license_url": info["license_url"]}
        print(f"  fetched {names[pid]}: {info['license']}")
        time.sleep(0.5)
    # Crop every headshot from the cached originals (no network needed).
    detector = face_detector()
    for pid, row in rows.items():
        head, how = crop_headshot(Image.open(ORIGINALS / f"{pid}.jpg"), detector, OVERRIDES.get(pid))
        head.save(OUT_DIR / row["file"], quality=88)
        row["crop"] = how
    with open(CREDITS, "w", newline="") as f:
        fields = ["espn_id", "player", "file", "commons_page", "author", "license", "license_url", "crop"]
        w = csv.DictWriter(f, fieldnames=fields, extrasaction="ignore")
        w.writeheader()
        for pid in sorted(rows, key=lambda k: rows[k]["player"]):
            w.writerow(rows[pid])
    crops = collections.Counter(r["crop"] for r in rows.values())
    print(f"wrote {CREDITS.relative_to(OUT_DIR.parent)} ({len(rows)} headshots; {dict(crops)})")


if __name__ == "__main__":
    main(force="--force" in sys.argv)
