---
layout: default
title: Privacy &amp; Security
description: Privacy and security policy for dodatascience.fun
---

<!-- NOTICE: The "Third-party requests", "What's in place", "Known gaps", and reporting sections were substantially revised by an LLM coding system (Claude Code) on 3 October 2026 to match the site after its CSP and third-party cleanup. Review before relying on them. -->

# Privacy &amp; Security

## Privacy

This site collects nothing. No analytics, no cookies, no accounts, no advertising, no profiling. GitHub pages and GitHub itself collects basic traffic data, although it seems pretty unreliable...

### No analytics, no cookies

There is no analytics script on this site — no GoatCounter, no Clicky, no Google Analytics, etc. The site sets no cookies and no local storage. There is nothing to opt out of and nothing to block.

There are also no accounts, no logins, no comment system, and no newsletter, so there is nothing for the site to store about you :-)

### Third-party requests

The core pages (home, syllabus, FAQ, worksheets, exercises) are self-contained: HTML, CSS, fonts, and a few small JavaScript files, all served from this domain. The **mini-book** (`/ethics-in-data-science/book/`) is now self-contained too: its font is self-hosted, and its math is rendered as MathML when the book is built, not loaded from a CDN.

Two areas do reach outside the domain, and you should know about them:

- **Slides** (`/slides/`) are Reveal.js decks built by [Quarto](https://quarto.org). Decks with Python output load two scripts, jQuery and RequireJS, from [jsDelivr](https://www.jsdelivr.com), pinned to exact versions with Subresource Integrity hashes. A few slides embed a page from another site: YouTube (via `youtube-nocookie.com`), Gapminder, UIC, Northwestern, and Tyler Vigen's *Spurious Correlations*. Those embeds are subject to the provider's own privacy practices, not mine. The radio button streams UIC Radio from `maindigitalstream.com` only after you press play, and the roll-call draws ask `random.org` for numbers only when the button is pressed.
- **The Python Yard** (`/yard/`) runs Python in your browser with JupyterLite. Starting it downloads the Pyodide runtime and its packages from jsDelivr, and the example notebooks read datasets from this site's repository on GitHub (`raw.githubusercontent.com`).

### Hosting

The site is static files served by GitHub Pages, which keeps its own request logs under [GitHub's privacy statement](https://docs.github.com/en/site-policy/privacy-policies/github-general-privacy-statement) (there is no access to per-visitor data from those logs).

---

## Security

*Reporting procedure adapted from the [GitHub official security policy template](https://github.com/github/.github/blob/master/SECURITY.md).*

This is a course website — static HTML on GitHub Pages, with no server-side code, no database, and no user accounts. The attack surface is small, but I still take reports seriously, so thanks for being here.

### What's in place

- **Static hosting**: no server-side code, no database, nothing to inject into.
- **HTTPS everywhere**, enforced by GitHub Pages.
- **Content Security Policy on every page** except the Python Yard, set in a `<meta>` tag. On the core pages it defaults to `'self'`, with no `'unsafe-inline'` for scripts, so injected inline JavaScript will not run. `base-uri 'none'` blocks `<base>`-tag hijacking, and `form-action 'none'` applies everywhere because the site has no forms. The slides and mini-book get their own policies, which name each outside host listed above and nothing else. The two jsDelivr scripts are allowlisted by their exact file paths, not the whole CDN.
- **Subresource Integrity** on both jsDelivr script tags in the slides, so a tampered copy fails to run rather than running silently.
- **Minimal scripts**, none of them inline on the core pages: a few pages use small local JavaScript files; the rest is HTML and CSS.
- **No third-party fonts**: every font is self-hosted.
- **Everything is public**: the full source of this site is in [the repository](https://github.com/jackbandy/data-science-fun), so anything you can find in the site, you can also find in the code.

### Known gaps

- GitHub Pages cannot send custom response headers, so there is no HTTP Strict Transport Security and no clickjacking protection (`frame-ancestors` only works as a header, not in a `<meta>` tag).
- The slides' and mini-book's policies still allow `'unsafe-inline'` scripts, because Quarto writes inline scripts into every page it generates.
- The Python Yard has no Content Security Policy yet. JupyterLite needs WebAssembly, web workers, and the outside hosts listed above, and a policy for it has not been tested.
- There is no CSP violation reporting, so I find out about problems when someone tells me.

### Reporting security issues

If you believe you have found a security or privacy issue, please report it! Through coordinated disclosure: Email [jxb@uic.edu](mailto:jxb@uic.edu) for anything sensitive. To encrypt it, use my [PGP key](https://jackbandy.com/pgp-key.txt), fingerprint `F37C FDA1 D0DD 0853 6C60 7D86 D9C9 11D1 1B09 9DD3`. For non-sensitive issues, you can submit a [GitHub issue](https://github.com/jackbandy/data-science-fun/issues).

Include as much of the following as you can:

- The type of issue
- Full paths of source file(s) related to the issue
- The location of the affected source code (i.e. direct URL)
- Any special configuration required to reproduce the issue
- Step-by-step instructions to reproduce the issue
- Proof-of-concept or exploit code (if possible)
- Impact of the issue, including how an attacker might exploit it
- Anything else you think I should know

### Policy

This site follows the principles of [GitHub's Safe Harbor Policy](https://docs.github.com/en/site-policy/security-policies/github-bug-bounty-program-legal-safe-harbor). Good-faith research consistent with that policy is welcome. There is no bug bounty — this is a very simple course site — but I'm glad to say thanks and/or credit you somewhere.

Machine-readable contact details: [security.txt](/.well-known/security.txt).

*Last reviewed: 3 October 2026.*
