# Terabyte Scale — Image Sources

Assets for the "how big is a terabyte" analogy slides in Week 1. Images are from Wikimedia Commons (public domain or CC-licensed) unless noted.

---

## `iphone-17-pro-max-cosmic-orange.jpg` / `-full.jpg`

Photo by Ahmad Ali Karim (Wikimedia user EmpAhmadK), 19 September 2025, taken at an Apple launch event at The Exchange TRX, Kuala Lumpur. **[CC0 1.0](https://creativecommons.org/publicdomain/zero/1.0/)** (public domain dedication).
[Wikimedia Commons](https://commons.wikimedia.org/wiki/File:Cosmic_Orange_iPhone_17_Pro_Max.jpg)

`-full.jpg` is the unmodified Commons original, byte-for-byte: 7,220,500 bytes, SHA-1 `4e26fe562b7babf35f2b1dfc251cac8ce03170d1`, matching the file's `imageinfo` from the Commons API. It stores 6240 × 4160 with EXIF orientation 8, so it *displays* 4160 × 6240 portrait — that is why Commons reports the portrait dimensions.

The file without the suffix is the one the slide uses: same image at 933 × 1400, EXIF rotation baked in rather than left as a tag, quality 85.


---

## `oppenheimer-format-guide.jpg` (Copyrighted — used under fair use)

The *Oppenheimer* format guide, comparing IMAX 70mm / 70mm / 35mm film against IMAX with Laser / IMAX Xenon / DCP digital projection. Studio marketing material by Universal Pictures and IMAX, published with Rasmus Larsen, ["Only 30 theaters will screen 'Oppenheimer' as intended by Christopher Nolan"](https://www.flatpanelshd.com/news.php?subaction=showfull&id=1685963488), *FlatpanelsHD*, 5 June 2023.

- License: Copyrighted (Universal Pictures / IMAX); used here under fair use for non-commercial educational commentary


---

## `terabyte-video-hours-log.svg` and `terabyte-video-hours-linear.svg`

Drawn for this deck by `make_terabyte_video_figure.py`, which writes both files from the same data and layout — they differ only in x scale. 


| Resolution | Bitrate range (Mbps) | Hours per TB |
|---|---|---|
| 480p | 2.5 – 4 | 556 – 889 |
| 720p | 5 – 9.5 | 234 – 444 |
| 1080p | 8 – 15 | 148 – 278 |
| 1440p | 16 – 30 | 74 – 139 |
| 4K UHD | 35 – 85 | 26 – 63 |
| 8K | 80 – 300 | 7 – 28 |

Source: YouTube Help, ["Recommended upload encoding settings"](https://support.google.com/youtube/answer/1722171). 480p lists no HDR tier, so its high end is SDR at high frame rate.

Hours are exact arithmetic: 1 TB = 8 x 10^12 bits, so `hours = 8e12 / (Mbps x 1e6 x 3600) = 2222.2 / Mbps`. Although these are mastering bitrates, not streaming bitrates. E.g. Netflix publishes a cap of about 7 GB/hour for Ultra HD ([Netflix Help](https://help.netflix.com/en/node/87))
