#!/usr/bin/env bash
set -euo pipefail

# build_all_quarto.sh — compile all Quarto revealjs slide decks to HTML and PDF
# Usage: ./build_all_quarto.sh [output-dir]
# If CHROME is set, it will be used as the Chrome/Chromium executable for PDF export.
# Set BUILD_PDFS=false to render HTML only.

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
OUTPUT_DIR="${1:-$SCRIPT_DIR}"
SERVER_ROOT="${QUARTO_SERVER_ROOT:-$(cd "$SCRIPT_DIR/.." && pwd)}"
QUARTO_CMD="${QUARTO_CMD:-quarto}"
PORT="${QUARTO_PORT:-}"
BUILD_PDFS="${BUILD_PDFS:-true}"
HAD_GITIGNORE=0
if [[ -e "$SCRIPT_DIR/.gitignore" ]]; then
  HAD_GITIGNORE=1
fi

if ! command -v "$QUARTO_CMD" >/dev/null 2>&1; then
  echo "Error: quarto command not found. Set QUARTO_CMD or install Quarto." >&2
  exit 1
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

SLIDE_FILES=()
while IFS= read -r candidate; do
  if [[ "$candidate" == *.qmd ]] || grep -Eq '^[[:space:]]*revealjs:' "$candidate"; then
    SLIDE_FILES+=("$candidate")
  fi
done < <(find "$SCRIPT_DIR" -maxdepth 1 -type f \( -name "*.qmd" -o -name "*.md" \) | sort)
if [[ "${#SLIDE_FILES[@]}" -eq 0 ]]; then
  echo "[quarto] No Quarto slide files found in $SCRIPT_DIR"
  exit 0
fi

SERVER_PID=""
TMP_DIR=""
cleanup() {
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

echo "[quarto] Rendering HTML with $QUARTO_CMD"
for slide in "${SLIDE_FILES[@]}"; do
  base="$(basename "${slide%.*}")"
  html_out="$OUTPUT_DIR/$base.html"
  echo "[quarto] Generating HTML: $html_out from $slide"
  (
    cd "$SCRIPT_DIR"
    "$QUARTO_CMD" render "$(basename "$slide")" --to revealjs --output "$base.html"
  )
  if [[ "$OUTPUT_DIR" != "$SCRIPT_DIR" ]]; then
    mv "$SCRIPT_DIR/$base.html" "$html_out"
    if [[ -d "$SCRIPT_DIR/${base}_files" ]]; then
      rm -rf "$OUTPUT_DIR/${base}_files"
      mv "$SCRIPT_DIR/${base}_files" "$OUTPUT_DIR/${base}_files"
    fi
  fi
done

if [[ "$BUILD_PDFS" == "false" ]]; then
  echo "[quarto] Skipping PDF generation."
  exit 0
fi

if ! command -v node >/dev/null 2>&1; then
  echo "Error: node command not found. Node is required for Chrome PDF export." >&2
  exit 1
fi

if ! python3 -c "import fitz" >/dev/null 2>&1; then
  echo "Error: Python package PyMuPDF is required for merging PDF pages (import fitz failed)." >&2
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

TMP_DIR="$(mktemp -d "${TMPDIR:-/tmp}/quarto-slides-pdf.XXXXXX")"

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
  echo "[quarto] Printing $slide_count slides for PDF: $pdf_out"
  slide_dir="$TMP_DIR/$base"
  mkdir -p "$slide_dir"
  export CHROME_CMD
  export QUARTO_PDF_PORT="$PORT"
  export QUARTO_PDF_URL_PATH="$url_path"
  export QUARTO_PDF_SLIDE_COUNT="$slide_count"
  export QUARTO_PDF_SLIDE_DIR="$slide_dir"
  node <<'NODE'
const { spawn } = require("node:child_process");
const fs = require("node:fs/promises");
const path = require("node:path");

const chrome = process.env.CHROME_CMD;
const port = Number(process.env.QUARTO_PDF_PORT);
const urlPath = process.env.QUARTO_PDF_URL_PATH;
const slideCount = Number(process.env.QUARTO_PDF_SLIDE_COUNT);
const slideDir = process.env.QUARTO_PDF_SLIDE_DIR;
const remotePort = 40000 + Math.floor(Math.random() * 20000);
const userData = path.join(process.env.TMPDIR || "/tmp", `quarto-chrome-${Date.now()}`);
const baseUrl = `http://127.0.0.1:${port}/${urlPath}?controls=false&progress=false`;
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
  `--user-data-dir=${userData}`,
  "--remote-debugging-address=127.0.0.1",
  `--remote-debugging-port=${remotePort}`,
  "--window-size=1280,720",
  `${baseUrl}#/0`
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
  // Ensure a WebSocket implementation exists in Node (use 'ws' package if available)
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

  // Support both browser-like and ws (Node) event APIs
  let ready;
  if (typeof socket.on === 'function') {
    // ws module (Node)
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
    // browser-like WebSocket
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

  function send(method, params = {}) {
    const messageId = ++id;
    socket.send(JSON.stringify({ id: messageId, method, params }));
    return new Promise((resolve, reject) => {
      pending.set(messageId, { resolve, reject });
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
    await client.ready;
    await client.send("Page.enable");
    await client.send("Runtime.enable");
    await client.send("Emulation.setEmulatedMedia", { media: "screen" });

    for (let index = 0; index < slideCount; index += 1) {
      await client.send("Page.navigate", { url: `${baseUrl}#/${index}` });
      await sleep(1200);
      await client.send("Runtime.evaluate", {
        expression: "window.Reveal && Reveal.isReady && Reveal.isReady()",
        returnByValue: true
      });
      const pdf = await client.send("Page.printToPDF", {
        landscape: false,
        printBackground: true,
        preferCSSPageSize: false,
        marginTop: 0,
        marginBottom: 0,
        marginLeft: 0,
        marginRight: 0,
        paperWidth: 13.333333,
        paperHeight: 7.5,
        displayHeaderFooter: false
      });
      const filename = path.join(slideDir, `${String(index).padStart(3, "0")}.pdf`);
      await fs.writeFile(filename, Buffer.from(pdf.data, "base64"));
    }

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

  python3 - <<PY
from pathlib import Path
import fitz

slide_dir = Path("$slide_dir")
pdf_out = Path("$pdf_out")
merged = fitz.open()
for pdf in sorted(slide_dir.glob("*.pdf")):
    page_pdf = fitz.open(pdf)
    merged.insert_pdf(page_pdf)
    page_pdf.close()
if merged.page_count == 0:
    raise SystemExit("No slide PDFs generated")
merged.save(pdf_out)
merged.close()
PY
  rm -f "$html_export"
done

echo "[quarto] Done."
