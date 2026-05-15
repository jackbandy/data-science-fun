#!/usr/bin/env python3
"""
save_data8_pdfs.py

Written with copilot

Download all PDFs linked from https://data8.org/sp26/resources/ into a destination directory.
Features:
- Finds links ending with .pdf on the resources page
- Skips already-downloaded files
- Per-file retries with exponential backoff and jitter
- CLI options for destination, attempts and timeout
"""

import argparse
import os
import sys
import time
import random
import urllib.request
import urllib.parse
import urllib.error
from html.parser import HTMLParser

BASE_URL = 'https://data8.org/sp26/resources/'

class LinkParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.links = []
    def handle_starttag(self, tag, attrs):
        if tag.lower() == 'a':
            for k, v in attrs:
                if k.lower() == 'href' and v:
                    self.links.append(v)


def fetch_pdf_links(base=BASE_URL, timeout=20):
    parser = LinkParser()
    req = urllib.request.Request(base, headers={'User-Agent':'python-urllib/3'})
    with urllib.request.urlopen(req, timeout=timeout) as r:
        html = r.read().decode('utf-8', errors='ignore')
    parser.feed(html)
    pdfs = []
    import re
    for href in parser.links:
        if re.search(r'\.pdf($|\?)', href, re.I):
            full = urllib.parse.urljoin(base, href)
            pdfs.append(full)
    # unique preserving order
    seen = set(); out = []
    for u in pdfs:
        if u not in seen:
            seen.add(u); out.append(u)
    return out


def safe_filename_from_url(url):
    p = urllib.parse.urlparse(url)
    fn = os.path.basename(p.path)
    if not fn:
        fn = urllib.parse.quote_plus(url)
    return fn


def download(url, dest_path, max_attempts=5, timeout=30, backoff_base=1.0):
    attempt = 0
    last_exc = None
    while attempt < max_attempts:
        attempt += 1
        try:
            req = urllib.request.Request(url, headers={'User-Agent':'curl/7.68.0'})
            with urllib.request.urlopen(req, timeout=timeout) as r, open(dest_path, 'wb') as f:
                f.write(r.read())
            return True
        except Exception as e:
            last_exc = e
            wait = backoff_base * (2 ** (attempt-1))
            # jitter
            wait = wait * (0.5 + random.random())
            print(f"Attempt {attempt}/{max_attempts} failed for {url}: {e}; sleeping {wait:.1f}s")
            time.sleep(wait)
    print(f"Giving up on {url} after {max_attempts} attempts. Last error: {last_exc}")
    return False


def main():
    ap = argparse.ArgumentParser(description='Download all PDFs linked from the Data8 SP26 resources page')
    ap.add_argument('--dest', '-d', default='.', help='Destination directory (default: current dir)')
    ap.add_argument('--max-attempts', type=int, default=5, help='Max attempts per file')
    ap.add_argument('--timeout', type=int, default=30, help='HTTP timeout in seconds')
    ap.add_argument('--backoff-base', type=float, default=1.0, help='Base seconds for exponential backoff')
    ap.add_argument('--list-only', action='store_true', help='Only list discovered PDF URLs')
    args = ap.parse_args()

    dest = os.path.abspath(args.dest)
    os.makedirs(dest, exist_ok=True)

    try:
        pdf_urls = fetch_pdf_links(timeout=args.timeout)
    except Exception as e:
        print('Failed to fetch resource page:', e, file=sys.stderr)
        sys.exit(2)

    if not pdf_urls:
        print('No PDF links found on the page.', file=sys.stderr)
        sys.exit(1)

    if args.list_only:
        for u in pdf_urls:
            print(u)
        return

    failures = []
    for url in pdf_urls:
        fn = safe_filename_from_url(url)
        dst = os.path.join(dest, fn)
        if os.path.exists(dst):
            print('Skipping (exists):', fn)
            continue
        print('Downloading:', url, '->', dst)
        ok = download(url, dst, max_attempts=args.max_attempts, timeout=args.timeout, backoff_base=args.backoff_base)
        if not ok:
            failures.append((url, dst))

    if failures:
        print('\nThe following files failed to download:')
        for u, d in failures:
            print(u)
        print('\nYou can re-run this script (it will skip already-downloaded files).')
        sys.exit(3)
    else:
        print('\nAll done. Downloaded PDFs to', dest)

if __name__ == '__main__':
    main()
