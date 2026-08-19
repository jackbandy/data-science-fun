# PrairieLearn branding

Official PrairieLearn logo mark (the coneflower glyph), taken from the PrairieLearn repository at `docs/assets/`.

- `PL-logo-black.svg` — black fill, for a light background
- `PL-logo-white.svg` — white fill, for dark backgrounds

Source: <https://github.com/PrairieLearn/PrairieLearn/tree/master/docs/assets>. The same mark is used on <https://www.prairielearn.com/>. Used here to identify the platform students submit work on.

The repo's `docs/assets/PL-logo-adaptive.svg` variant was deliberately not kept: it swaps fill based on the *viewer's* `prefers-color-scheme`, which can render white-on-white when the slides are projected.

`PL-logo-white-on-blue.svg` is a local derivative, not an upstream file: the white mark, at natural scale and centered, on a `#052c65` panel. That blue is the header background on <https://www.prairielearn.com/> (`Header-module-scss-module__t7BEda__header { background-color: #052c65 }`), read from the site's stylesheet.

The panel is `viewBox="0 0 89 144"` — a portrait golden rectangle. 89 and 144 are consecutive Fibonacci numbers, so the frame is golden to four decimals (144/89 = 1.61798) while every coordinate stays an integer. It is used on the Homework 1 slide in `docs/slides/week1.qmd`, where the deck's golden ratio shows up again in the figure sizing.
