# Fonts

Self-hosted fonts used by the slide theme (`docs/slides/shared/theme/uic-orange-reveal.scss`),
the site CSS (`docs/css/`), and the figure generators under `docs/assets/`.

- **Big Shoulders** (`big-shoulders/BigShoulders.woff2`): downloaded from the upstream XO Type Co repository: https://github.com/xotypeco/big_shoulders. Additional non-Google references: https://bigshoulders.me/ and https://design.chicago.gov/typography/. Copyright 2019 The Big Shoulders Project Authors, licensed under the SIL Open Font License (`big-shoulders/OFL.txt`). Used as the slide/heading face.
- **Libre Franklin** (`libre-franklin/`): downloaded from the upstream Impallari Type repository: https://github.com/impallari/Libre-Franklin. Used as the self-hosted OFL fallback for the slide body's ITC Franklin Gothic stack because ITC Franklin Gothic itself is a commercial typeface and no permissive redistribution source was identified. Licensed under the SIL Open Font License 1.1 (`libre-franklin/OFL.txt`). Two formats:
	- `LibreFranklin.woff2` for the web slides and site CSS
	- `LibreFranklin-Regular.ttf` (static Regular, v3.000, from `fonts/TTF/` upstream) for figure generators that render with matplotlib — matplotlib cannot decode woff2 without brotli.
- **Nunito** (`Nunito-wght.ttf`): variable weight axis, v3.602. Copyright 2014 The Nunito Project Authors (https://github.com/googlefonts/nunito), Vernon Adams. Licensed under the SIL Open Font License 1.1. Used by `docs/css/index.css`.
- **VT323** (`VT323-Regular.ttf`): v2.000. Copyright 2011 The VT323 Project Authors, Peter Hull. Licensed under the SIL Open Font License 1.1. Used by `docs/assets/pyramid/generate-pyramid-variants.py` for the "info" layer label.
- **BPdots** (`BPdots-Regular.otf`): v1.000. Copyright 2007 George Triantafyllakos, distributed as a free font by his foundry backpacker.gr (https://backpacker.gr/fonts/). **No formal license instrument exists for this font.** The only permission is the foundry's own terms, which offer the free collection "as in beer" for personal or commercial projects, asking that users act with "a sense of responsibility and respect" and "refer to backpacker.gr whenever possible." Hopefully the use in `docs/assets/pyramid/generate-pyramid-variants.py` for the "data" layer label is considered responsible and respectful.
