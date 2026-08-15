# The English baseline used by the "Unusual words" section

`build_data.py` ranks this repository's vocabulary against general English. This
file records where that baseline comes from and what it can and cannot support.

## Source

`count_1w.txt` — "the 1/3 million most frequent words, all lowercase, with
counts", 333,333 entries over 588,124,220,187 tokens.

- Downloaded from <https://norvig.com/ngrams/>
- Accompanies: Peter Norvig, "Natural Language Corpus Data", in *Beautiful
  Data*, ed. Toby Segaran and Jeff Hammerbacher (O'Reilly, 2009), ch. 14.
- Norvig's page states the files are "derived from the Google Web Trillion Word
  Corpus, as described by Thorsten Brants and Alex Franz, and distributed by the
  Linguistic Data Consortium."
- Underlying corpus: Thorsten Brants and Alex Franz, *Web 1T 5-gram Version 1*,
  LDC2006T13 (Linguistic Data Consortium, 2006).

## Why it is downloaded rather than committed

Norvig's page grants an MIT license over **the code** on that page. It states no
license for the data files, which are Google's and are distributed by the LDC.
Rather than assume redistribution rights we do not have, `build_data.py`
downloads the file to `meta_analytics_source/.cache/` (git-ignored) on first run
and reuses it afterward. Only the computed result — 40 rows of word, count, and
rate — is committed and published.

This follows the same reasoning as `datasets/musiclab-salganik-2006/`, whose raw
data is git-ignored and fetched rather than redistributed.

## Caveats, which the page states in plain language

The baseline is **2006 web text**, not a balanced corpus of written English.
Three consequences shape how the results should be read:

1. **It postdates nothing.** Words coined or popularized after 2006 — `llms`,
   `agentic`, `github` — are absent from it. `build_data.py` drops any word
   missing from the baseline rather than reporting an infinite ratio, so the
   over-used list is a list of *ordinary English words this site leans on*, not
   a list of neologisms.
2. **It is web pages, so it is full of navigation and commerce.** `home`,
   `contact`, `free`, `price`, `email`, `products` are far more common in it
   than in prose generally. This is why the under-used list reads as a
   catalogue of web boilerplate: what the site under-uses, relative to the web
   of 2006, is the web of 2006.
3. **It is uncased and unlemmatized**, matching how `build_data.py` tokenizes,
   so the two sides of the comparison are at least consistent with each other.

## The statistic

For each word appearing at least `MIN_COUNT` (10) times here and present in the
baseline:

    ratio = (occurrences here / total words here) / (occurrences in English / total English)

Above 1 is over-used, below 1 is under-used. The minimum count exists because
the ratio is unstable for rare words: a single stray occurrence of an otherwise
rare word already reads as a thousandfold excess.
