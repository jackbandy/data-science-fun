#!/usr/bin/env bash
set -euo pipefail

# build_all_quarto.sh — compile all Quarto revealjs slide decks to HTML (and optionally PDF)
# Usage: ./build_all_quarto.sh [output-dir]
# If CHROME is set, it will be used as the Chrome/Chromium executable for PDF export.
# Set BUILD_PDFS=true to also generate PDF files.
# Set SKIP_HTML=true to skip HTML rendering and export PDFs from existing HTML.
# Set RENDER_SLIDES="week1.md week5.qmd" to render only specific decks.

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
OUTPUT_DIR="${1:-$SCRIPT_DIR}"
SERVER_ROOT="${QUARTO_SERVER_ROOT:-$(cd "$SCRIPT_DIR/.." && pwd)}"
QUARTO_CMD="${QUARTO_CMD:-quarto}"
PORT="${QUARTO_PORT:-}"
# BUILD_PDFS: env var wins; otherwise prompt when running interactively.
if [[ -z "${BUILD_PDFS:-}" ]]; then
  if [[ -t 0 && -t 1 ]]; then
    printf 'Generate PDFs? [y/N] (auto-no in 2s): '
    if IFS= read -r -t 2 _pdf_reply 2>/dev/null; then
      echo
      if [[ "$_pdf_reply" =~ ^[Yy]$ ]]; then BUILD_PDFS=true; else BUILD_PDFS=false; fi
    else
      echo
      BUILD_PDFS=false
    fi
  else
    BUILD_PDFS=false
  fi
fi
HAD_GITIGNORE=0
if [[ -e "$SCRIPT_DIR/.gitignore" ]]; then
  HAD_GITIGNORE=1
fi

if ! command -v "$QUARTO_CMD" >/dev/null 2>&1; then
  echo "Error: quarto command not found. Set QUARTO_CMD or install Quarto." >&2
  exit 1
fi

# Set up Python environment via uv if available
if command -v uv >/dev/null 2>&1; then
  VENV="$SCRIPT_DIR/.venv"
  if [[ -f "$SCRIPT_DIR/requirements.txt" ]]; then
    echo "[quarto] Installing Python dependencies with uv..."
    [[ -d "$VENV" ]] || uv venv --quiet "$VENV"
    uv pip install --quiet --python "$VENV" -r "$SCRIPT_DIR/requirements.txt"
  fi
  export VIRTUAL_ENV="$VENV"
  export PATH="$VENV/bin:$PATH"
  export QUARTO_PYTHON="$VENV/bin/python3"
  python3() { uv run --no-project python3 "$@"; }
  export -f python3
else
  echo "[quarto] Warning: uv not found. Install uv for reproducible Python environments." >&2
fi

find_chrome() {
  if [[ -n "${CHROME:-}" && -x "$CHROME" ]]; then
    printf '%s\n' "$CHROME"
    return
  fi

  local candidates=(
    "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
    "/Applications/Chromium.app/Contents/MacOS/Chromium"
    "/Applications/Microsoft Edge.app/Contents/MacOS/Microsoft Edge"
  )

  local candidate
  for candidate in "${candidates[@]}"; do
    if [[ -x "$candidate" ]]; then
      printf '%s\n' "$candidate"
      return
    fi
  done

  for candidate in google-chrome chromium chromium-browser chrome; do
    if command -v "$candidate" >/dev/null 2>&1; then
      command -v "$candidate"
      return
    fi
  done
}

mkdir -p "$OUTPUT_DIR"

if [[ "$BUILD_PDFS" != "true" ]]; then
  echo "[quarto] Building HTML only. Set BUILD_PDFS=true or answer 'y' at the prompt to include PDFs."
fi

SLIDE_FILES=()
if [[ -n "${RENDER_SLIDES:-}" ]]; then
  # Selective build: RENDER_SLIDES is a space-separated list of filenames (e.g. "week1.md week5.qmd")
  for name in $RENDER_SLIDES; do
    candidate="$SCRIPT_DIR/$name"
    if [[ -f "$candidate" ]]; then
      SLIDE_FILES+=("$candidate")
    else
      echo "[quarto] Warning: specified slide '$name' not found, skipping" >&2
    fi
  done
  echo "[quarto] Selective build: ${SLIDE_FILES[*]:-none}"
else
  while IFS= read -r candidate; do
    if [[ "$candidate" == *.qmd ]] || grep -Eq '^[[:space:]]*revealjs:' "$candidate"; then
      SLIDE_FILES+=("$candidate")
    fi
  done < <(find "$SCRIPT_DIR" -maxdepth 1 -type f \( -name "*.qmd" -o -name "*.md" \) | sort)
fi
if [[ "${#SLIDE_FILES[@]}" -eq 0 ]]; then
  echo "[quarto] No Quarto slide files found in $SCRIPT_DIR"
  exit 0
fi

SERVER_PID=""
TMP_DIR=""
cleanup() {
  # Restore any deck source left stamped if a render was interrupted.
  for backup in "$SCRIPT_DIR"/*.stampbak; do
    [[ -e "$backup" ]] || continue
    mv -f "$backup" "${backup%.stampbak}"
  done
  if [[ -n "$SERVER_PID" ]]; then
    kill "$SERVER_PID" >/dev/null 2>&1 || true
    wait "$SERVER_PID" 2>/dev/null || true
  fi
  if [[ -n "$TMP_DIR" && -d "$TMP_DIR" ]]; then
    rm -rf "$TMP_DIR"
  fi
  if [[ "$HAD_GITIGNORE" -eq 0 && -f "$SCRIPT_DIR/.gitignore" ]]; then
    local_gitignore_content="$(cat "$SCRIPT_DIR/.gitignore")"
    if [[ "$local_gitignore_content" == $'/.quarto/\n**/*.quarto_ipynb' ]]; then
      rm -f "$SCRIPT_DIR/.gitignore"
    fi
  fi
}
trap cleanup EXIT

if [[ "${SKIP_HTML:-false}" == "true" ]]; then
  echo "[quarto] SKIP_HTML=true: reusing existing HTML in $OUTPUT_DIR for PDF-only export"
else
echo "[quarto] Rendering HTML with $QUARTO_CMD"
for slide in "${SLIDE_FILES[@]}"; do
  base="$(basename "${slide%.*}")"
  html_out="$OUTPUT_DIR/$base.html"
  echo "[quarto] Generating HTML: $html_out from $slide"
  # Stamp the compile time into the Sources slide of a throwaway copy, render,
  # then restore the pristine source so the timestamp never gets committed.
  src_file="$SCRIPT_DIR/$(basename "$slide")"
  cp "$src_file" "$src_file.stampbak"
  python3 "$SCRIPT_DIR/postprocess_slides.py" "$src_file" \
    || { mv -f "$src_file.stampbak" "$src_file"; exit 1; }
  # For Python slides, ensure keep-ipynb: true is set so the notebook is preserved
  if grep -q '```{python}' "$src_file"; then
    python3 - "$src_file" <<'INJECT_PY'
import sys, re
path = sys.argv[1]
with open(path) as f:
    content = f.read()
if 'keep-ipynb' not in content:
    if re.search(r'^execute:', content, re.MULTILINE):
        content = re.sub(r'^(execute:[ \t]*\n)', r'\1  keep-ipynb: true\n', content, count=1, flags=re.MULTILINE)
    else:
        content = re.sub(r'^(---\n)', r'---\nexecute:\n  keep-ipynb: true\n', content, count=1, flags=re.MULTILINE)
    with open(path, 'w') as f:
        f.write(content)
INJECT_PY
    if [[ $? -ne 0 ]]; then mv -f "$src_file.stampbak" "$src_file"; exit 1; fi
  fi
  (
    cd "$SCRIPT_DIR"
    "$QUARTO_CMD" render "$(basename "$slide")" --to revealjs --output "$base.html"
  ) || { mv -f "$src_file.stampbak" "$src_file"; exit 1; }
  mv -f "$src_file.stampbak" "$src_file"
  if [[ "$OUTPUT_DIR" != "$SCRIPT_DIR" ]]; then
    mv "$SCRIPT_DIR/$base.html" "$html_out"
    if [[ -d "$SCRIPT_DIR/${base}_files" ]]; then
      rm -rf "$OUTPUT_DIR/${base}_files"
      mv "$SCRIPT_DIR/${base}_files" "$OUTPUT_DIR/${base}_files"
    fi
  fi
  ipynb_src="$SCRIPT_DIR/$base.quarto_ipynb"
  if [[ -f "$ipynb_src" ]]; then
    mv -f "$ipynb_src" "$SCRIPT_DIR/$base.ipynb"
    echo "[quarto] Saved notebook: $SCRIPT_DIR/$base.ipynb"
  fi
done
fi

if [[ "$BUILD_PDFS" != "true" ]]; then
  echo "[quarto] Skipping PDF generation."
  exit 0
fi

if ! command -v node >/dev/null 2>&1; then
  echo "Error: node command not found. Node is required for Chrome PDF export." >&2
  exit 1
fi


CHROME_CMD="$(find_chrome || true)"
if [[ -z "$CHROME_CMD" ]]; then
  echo "Error: Chrome/Chromium not found. Set CHROME to a browser executable." >&2
  exit 1
fi

if [[ -z "$PORT" ]]; then
  PORT="$(python3 - <<'PY'
import socket
with socket.socket() as s:
    s.bind(("127.0.0.1", 0))
    print(s.getsockname()[1])
PY
)"
fi

echo "[quarto] Starting local server on http://127.0.0.1:$PORT from $SERVER_ROOT"
python3 -m http.server "$PORT" --bind 127.0.0.1 --directory "$SERVER_ROOT" >/tmp/quarto-slides-server.log 2>&1 &
SERVER_PID="$!"

python3 - <<PY
import socket
import sys
import time

port = int("$PORT")
deadline = time.time() + 10
while time.time() < deadline:
    try:
        with socket.create_connection(("127.0.0.1", port), timeout=0.25):
            sys.exit(0)
    except OSError:
        time.sleep(0.1)
sys.exit("Timed out waiting for local preview server")
PY

echo "[quarto] Generating vector PDFs with $CHROME_CMD"
for slide in "${SLIDE_FILES[@]}"; do
  base="$(basename "${slide%.*}")"
  html_out="$OUTPUT_DIR/$base.html"
  html_export="$OUTPUT_DIR/.$base-pdf-export.html"
  pdf_out="$OUTPUT_DIR/$base.pdf"
  slide_count="$(python3 - <<PY
from pathlib import Path
import re

html = Path("$html_out").read_text(encoding="utf-8")
print(len(re.findall(r'<section\\b[^>]*class="[^"]*(?:\\bslide\\b|quarto-title-block)', html)))
PY
)"
  if [[ "$slide_count" -eq 0 ]]; then
    echo "Error: no revealjs slides found in $html_out" >&2
    exit 1
  fi

  python3 - <<PY
from pathlib import Path

html_path = Path("$html_out")
export_path = Path("$html_export")
html = html_path.read_text(encoding="utf-8")
css = """
<style>
.reveal .slide-menu-button,
.reveal .controls,
.reveal .progress,
.reveal .slide-chalkboard-buttons {
  display: none !important;
}
</style>
"""
export_path.write_text(html.replace("</head>", css + "</head>", 1), encoding="utf-8")
PY

  url_path="$(python3 - <<PY
import os
import urllib.parse

server_root = os.path.abspath("$SERVER_ROOT")
html_path = os.path.abspath("$html_export")
rel_path = os.path.relpath(html_path, server_root)
if rel_path.startswith(".."):
    raise SystemExit(f"Output file is outside server root: {html_path}")
print(urllib.parse.quote(rel_path.replace(os.sep, "/")))
PY
)"
  echo "[quarto] Generating PDF ($slide_count slides): $pdf_out"
  export CHROME_CMD QUARTO_PDF_PORT="$PORT" QUARTO_PDF_URL_PATH="$url_path" QUARTO_PDF_OUT="$pdf_out"
  node <<'NODE'
const { spawn } = require("node:child_process");
const fs = require("node:fs/promises");
const path = require("node:path");

const chrome = process.env.CHROME_CMD;
const port = Number(process.env.QUARTO_PDF_PORT);
const urlPath = process.env.QUARTO_PDF_URL_PATH;
const pdfOut = process.env.QUARTO_PDF_OUT;
const remotePort = 40000 + Math.floor(Math.random() * 20000);
const userData = path.join(process.env.TMPDIR || "/tmp", `quarto-chrome-${Date.now()}`);
// ?print-pdf activates reveal.js's print layout: all slides are rendered at once
// with page-break-after between them, so a single printToPDF call produces the full deck.
const printUrl = `http://127.0.0.1:${port}/${urlPath}?print-pdf&controls=false&progress=false`;
let chromeStderr = "";
let chromeExit = null;

const browser = spawn(chrome, [
  "--headless=new",
  "--disable-gpu",
  "--disable-dev-shm-usage",
  "--hide-scrollbars",
  "--no-sandbox",
  "--no-first-run",
  "--no-default-browser-check",
  "--force-color-profile=srgb",
  `--user-data-dir=${userData}`,
  "--remote-debugging-address=127.0.0.1",
  `--remote-debugging-port=${remotePort}`,
  "--window-size=1280,720",
  printUrl,
], { stdio: ["ignore", "ignore", "pipe"] });

browser.stderr.on("data", (chunk) => {
  chromeStderr += chunk.toString();
  if (chromeStderr.length > 8000) chromeStderr = chromeStderr.slice(-8000);
});

browser.on("exit", (code, signal) => {
  chromeExit = { code, signal };
});

function sleep(ms) {
  return new Promise((resolve) => setTimeout(resolve, ms));
}

async function getJson(resource) {
  const response = await fetch(`http://127.0.0.1:${remotePort}${resource}`);
  if (!response.ok) throw new Error(`${resource}: ${response.status}`);
  return response.json();
}

async function waitForDebugger() {
  for (let attempt = 0; attempt < 300; attempt += 1) {
    if (chromeExit) {
      throw new Error(`Chrome exited before debugger was ready: ${JSON.stringify(chromeExit)}\n${chromeStderr}`);
    }
    try {
      await getJson("/json/version");
      return;
    } catch {
      await sleep(100);
    }
  }
  throw new Error(`Timed out waiting for Chrome remote debugger\n${chromeStderr}`);
}

function createClient(webSocketUrl) {
  const WebSocketClass = (typeof WebSocket !== "undefined") ? WebSocket : (() => {
    try {
      return require('ws');
    } catch (err) {
      throw new Error('WebSocket is not defined and the "ws" package could not be required. Install "ws" or run in an environment with a global WebSocket.');
    }
  })();

  const socket = new WebSocketClass(webSocketUrl);
  let id = 0;
  const pending = new Map();

  let ready;
  if (typeof socket.on === 'function') {
    socket.on('message', (data) => {
      const message = JSON.parse(typeof data === 'string' ? data : data.toString());
      if (message.id && pending.has(message.id)) {
        const { resolve, reject } = pending.get(message.id);
        pending.delete(message.id);
        if (message.error) reject(new Error(JSON.stringify(message.error)));
        else resolve(message.result);
      }
    });
    ready = new Promise((resolve) => socket.on('open', resolve));
  } else {
    socket.onmessage = (event) => {
      const message = JSON.parse(event.data);
      if (message.id && pending.has(message.id)) {
        const { resolve, reject } = pending.get(message.id);
        pending.delete(message.id);
        if (message.error) reject(new Error(JSON.stringify(message.error)));
        else resolve(message.result);
      }
    };
    ready = new Promise((resolve) => { socket.onopen = resolve; });
  }

  function send(method, params = {}, timeoutMs = 30000) {
    const messageId = ++id;
    socket.send(JSON.stringify({ id: messageId, method, params }));
    return new Promise((resolve, reject) => {
      const timer = setTimeout(() => {
        pending.delete(messageId);
        reject(new Error(`CDP timeout (${timeoutMs}ms) waiting for: ${method}`));
      }, timeoutMs);
      pending.set(messageId, {
        resolve: (r) => { clearTimeout(timer); resolve(r); },
        reject: (e) => { clearTimeout(timer); reject(e); },
      });
    });
  }

  return { socket, ready, send };
}

async function main() {
  try {
    await waitForDebugger();
    const tabs = await getJson("/json/list");
    const tab = tabs.find((entry) => entry.type === "page" && entry.url.includes(urlPath))
      || tabs.find((entry) => entry.type === "page")
      || tabs[0];
    const client = createClient(tab.webSocketDebuggerUrl);
    await Promise.race([
      client.ready,
      new Promise((_, reject) => setTimeout(() => reject(new Error("Timed out connecting to Chrome WebSocket")), 10000)),
    ]);
    await client.send("Page.enable");
    await client.send("Runtime.enable");
    await client.send("Emulation.setEmulatedMedia", { media: "screen" });

    // Navigate to print-pdf view and poll until reveal.js finishes rendering all slides.
    await client.send("Page.navigate", { url: printUrl });
    let isReady = false;
    for (let i = 0; i < 60; i += 1) {
      await sleep(500);
      try {
        const result = await client.send("Runtime.evaluate", {
          expression: "document.readyState === 'complete' && window.Reveal && Reveal.isReady()",
          returnByValue: true,
        });
        if (result.result?.value === true) { isReady = true; break; }
      } catch { /* keep polling */ }
    }
    if (!isReady) throw new Error("Timed out waiting for reveal.js print layout");
    await client.send("Runtime.evaluate", { expression: "document.fonts.ready", awaitPromise: true });
    await sleep(500); // buffer for late-loading images

    const pdf = await client.send("Page.printToPDF", {
      landscape: false,
      printBackground: true,
      preferCSSPageSize: false,
      marginTop: 0.25,
      marginBottom: 0.25,
      marginLeft: 0.25,
      marginRight: 0.25,
      paperWidth: 13.333333,
      paperHeight: 7.5,
      displayHeaderFooter: false,
      generateDocumentOutline: true,
    }, 120000);
    await fs.writeFile(pdfOut, Buffer.from(pdf.data, "base64"));
    client.socket.close();
  } finally {
    browser.kill();
    await fs.rm(userData, { recursive: true, force: true }).catch(() => undefined);
  }
}

main().catch((error) => {
  browser.kill();
  console.error(error);
  process.exit(1);
});
NODE
  rm -f "$html_export"
done

echo "[quarto] Done."
