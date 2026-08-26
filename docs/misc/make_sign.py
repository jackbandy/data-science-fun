#!/usr/bin/env python3
"""Generate a landscape PDF sign using pandoc + LaTeX (Computer Modern font)."""

import subprocess
import tempfile
import os

LINE1 = "PLEASE DON'T SIT IN THIS ROW"
LINE2 = "(QUIZ DAY)"

OUTPUT_PDF = "sign.pdf"

def make_markdown():
    return f"""---
header-includes: |
  \\pagestyle{{empty}}
---

\\vspace*{{\\fill}}
\\begin{{center}}
{{\\fontsize{{60}}{{72}}\\selectfont\\bfseries {LINE1}\\par}}
{{\\fontsize{{60}}{{72}}\\selectfont {LINE2}\\par}}
\\end{{center}}
\\vspace*{{\\fill}}
"""

def main():
    with tempfile.NamedTemporaryFile("w", suffix=".md", delete=False) as f:
        f.write(make_markdown())
        md_path = f.name

    try:
        subprocess.run(
            [
                "pandoc",
                md_path,
                "-o", OUTPUT_PDF,
                "-V", "geometry:landscape",
                "-V", "geometry:margin=1in",
            ],
            check=True,
        )
        print(f"Wrote {OUTPUT_PDF}")
    finally:
        os.remove(md_path)

if __name__ == "__main__":
    main()
