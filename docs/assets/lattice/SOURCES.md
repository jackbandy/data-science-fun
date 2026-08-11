# Sources — Lattice QCD slide (Spider-Man: Brand New Day)

The purpose of this folder is to recreate a lecture slide visible behind Bruce Banner (Mark Ruffalo) in the *Spider-Man: Brand New Day* (2026) classroom scene at Empire State University.

Lattice quantum chromodynamics (lattice QCD) is a computational version of quantum chromodynamics — the theory of the strong nuclear force — that represents spacetime as a discrete grid ("lattice") so physicists can calculate how quarks and gluons behave.

- [Get Your Comic On — Breaking Down the First SPIDER-MAN: BRAND NEW DAY Trailer](https://getyourcomicon.co.uk/blog/2026/03/18/breaking-down-the-first-spider-man-brand-new-day-trailer/)
- [Reddit r/Marvel — Banner in Brand New Day](https://www.reddit.com/r/Marvel/comments/1rx2l3f/banner_in_brand_new_day/)
- [Wikipedia — Spider-Man: Brand New Day](https://en.wikipedia.org/wiki/Spider-Man:_Brand_New_Day)
- [Instagram — Bruce Banner teaching with "Lattice Quantum Chromodynamics" on screen](https://www.instagram.com/p/DWF5HKwj42Y/)

- Banner teaches a physics lecture in front of a display reading **"Lattice Quantum Chromodynamics (QCD)"**, showing **a series of cubes forming a larger cube**, with **"quark"** and **"gluon"** pointed out.
  - [Comic Book Club — 'Spider-Man: Brand New Day' Trailer Burning Questions](https://comicbookclublive.com/2026/03/18/spider-man-brand-new-day-trailer-burning-questions-from-sadie-sink-to-the-other/)
- Banner wears a Hulk-inhibitor device (as seen in *She-Hulk*) during the scene.
  - [Bleeding Cool — Trailer: Punisher, Banner, The Hand & More](https://bleedingcool.com/movies/spider-man-brand-new-day-trailer-punisher-banner-the-hand-more/)
- The lecture is at Empire State University and concerns time/space ("chrono-dynamics"), tying to Banner's post-*Endgame* expertise.
  - [ScreenRant — Easter Eggs, References & Cameos Explained](https://screenrant.com/spiderman-brand-new-day-movie-easter-eggs-references/)
  - [Medium — Every Detail, Layer by Layer](https://medium.com/@DID911/spider-man-brand-new-day-every-detail-layer-by-layer-personality-03-3db1a1c2925a)

## Details from the frames (reference images in this folder)

- Mint-teal gradient background, lighter at top; bold white sans-serif title across the top.
- Thick white wireframe cube subdivided into smaller cells.
- Quarks: glossy purple-blue spheres on lattice sites; **QUARK** callout with filled arrowhead points at one on the far-right edge.
- Gluons: orange arrows along the links between sites; **GLUON** callout points at one (matches real lattice QCD: quarks on sites, gluons on links — [Wikipedia](https://en.wikipedia.org/wiki/Lattice_QCD)).
- **TIME** on the vertical axis, **SPACE** on a double-headed arrow under the bottom edge.
- Gray bar across the bottom with **"Slide 9 of 22"** at right; three dark circular buttons (replay, prev, next) in the bottom-right of the green area (`buttons.avif`).


## Files

- `generate_lattice_slide.py` — generates the slide; PNG via `rsvg-convert`.
- `lattice-qcd-slide-v2.svg` / `lattice-qcd-slide-v2.png` — current slide, 1920×1080.
- `lattice-qcd-slide.svg` / `.png` — first draft (before the close-up reference frames).
