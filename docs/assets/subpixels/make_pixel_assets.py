# NOTICE: subpixel-crop section added by an LLM coding agent; unreviewed.
from __future__ import annotations

import math
from pathlib import Path

from PIL import Image


PHI = (1 + math.sqrt(5)) / 2
ASSET_DIR = Path(__file__).resolve().parent
SOURCE = ASSET_DIR / "lcd-pixel-macro-2023.jpg"
CROP_OUTPUT = ASSET_DIR / "lcd-pixel-macro-2023-golden.jpg"
ZOOM_OUTPUT = ASSET_DIR / "lcd-pixel-macro-2023-golden-zoom-10x.jpg"
SUBPIXEL_OUTPUT = ASSET_DIR / "lcd-pixel-macro-2023-golden-subpixel.jpg"
# Crop box in full-resolution source coordinates, found by hand: it isolates
# the pure-color core of a single red subpixel, avoiding the black grid lines
# around it, sized to a landscape golden-ratio rectangle.
SUBPIXEL_BOX = (2935, 1949, 2953, 1960)
SUBPIXEL_SCALE = 45


def centered_golden_crop_box(width: int, height: int) -> tuple[int, int, int, int]:
    target_height = round(width / PHI)
    if target_height > height:
        target_width = round(height * PHI)
        left = (width - target_width) // 2
        return (left, 0, left + target_width, height)

    top = (height - target_height) // 2
    return (0, top, width, top + target_height)


def centered_zoom_box(width: int, height: int, factor: int) -> tuple[int, int, int, int]:
    zoom_width = width // factor
    zoom_height = height // factor
    left = (width - zoom_width) // 2
    top = (height - zoom_height) // 2
    return (left, top, left + zoom_width, top + zoom_height)


def save_jpeg(image: Image.Image, path: Path) -> None:
    image.save(path, format="JPEG", quality=95, subsampling=0, optimize=True)


def main() -> None:
    source = Image.open(SOURCE)
    crop_box = centered_golden_crop_box(*source.size)
    cropped = source.crop(crop_box)
    save_jpeg(cropped, CROP_OUTPUT)

    zoom_box = centered_zoom_box(*cropped.size, factor=10)
    zoomed = cropped.crop(zoom_box).resize(cropped.size, resample=Image.Resampling.LANCZOS)
    save_jpeg(zoomed, ZOOM_OUTPUT)

    subpixel = source.crop(SUBPIXEL_BOX)
    subpixel = subpixel.resize(
        (subpixel.width * SUBPIXEL_SCALE, subpixel.height * SUBPIXEL_SCALE),
        resample=Image.Resampling.LANCZOS,
    )
    save_jpeg(subpixel, SUBPIXEL_OUTPUT)


if __name__ == "__main__":
    main()
