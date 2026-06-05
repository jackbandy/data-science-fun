#!/usr/bin/env python3
# NOTICE: This file was created and modified by an LLM coding system.
"""Audit the Ethics in Data Science bibliography and write a report card.

The checker performs local BibTeX validation, tests cited URLs and DOI
resolvers, collects candidate records from OpenAlex and Semantic Scholar, and
then separately verifies whether those records agree with the local citation.
It uses only the Python standard library.
"""

from __future__ import annotations

import argparse
import concurrent.futures
import dataclasses
import datetime as dt
import difflib
import html
import json
import os
import re
import sqlite3
import sys
import time
import unicodedata
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path
from typing import Any


SCRIPT_DIR = Path(__file__).resolve().parent
REPO_ROOT = SCRIPT_DIR.parents[1]
DOCS_DIR = REPO_ROOT / "docs"
DEFAULT_BIB = DOCS_DIR / "ethics-in-data-science" / "references.bib"
DEFAULT_REPORT = SCRIPT_DIR / "references-report.md"
DEFAULT_JSON = SCRIPT_DIR / "references-report.json"
DEFAULT_ZOTERO_DB = Path("/Users/jackb/Zotero/zotero.sqlite")
DEFAULT_CACHE = SCRIPT_DIR / "ethics-reference-check-cache.json"

OPENALEX_API = "https://api.openalex.org"
SEMANTIC_SCHOLAR_API = "https://api.semanticscholar.org/graph/v1"
DOI_RE = re.compile(r"^10\.\d{4,9}/\S+$", re.IGNORECASE)
ISBN_RE = re.compile(r"^[0-9Xx -]{10,20}$")
YEAR_RE = re.compile(r"^\d{4}$")
LATEX_COMMAND_RE = re.compile(r"\\['\"`^~=.uvHckbdrt]\s*\{?([A-Za-z])\}?")
NON_WORD_RE = re.compile(r"[^a-z0-9]+")
MULTISPACE_RE = re.compile(r"\s+")

REQUIRED_FIELDS = {
    "article": (("author",), ("title",), ("year",), ("journal",)),
    "book": (("author", "editor"), ("title",), ("year",), ("publisher",)),
    "incollection": (("author",), ("title",), ("year",), ("booktitle",)),
    "inproceedings": (("author",), ("title",), ("year",), ("booktitle",)),
    "online": (("author", "editor"), ("title",), ("year",), ("url",)),
    "movie": (("title",), ("year",)),
}

SCHOLARLY_TYPES = {
    "article",
    "book",
    "incollection",
    "inproceedings",
    "conference",
    "proceedings",
    "phdthesis",
    "mastersthesis",
    "techreport",
}


@dataclasses.dataclass
class BibEntry:
    entry_type: str
    key: str
    fields: dict[str, str]
    line: int


@dataclasses.dataclass
class LinkResult:
    url: str
    reachable: bool
    status: int | None
    final_url: str | None
    error: str | None
    elapsed_ms: int | None


@dataclasses.dataclass
class ProviderResult:
    provider: str
    status: str
    matched_by: str | None = None
    record_id: str | None = None
    record_url: str | None = None
    title: str | None = None
    year: int | None = None
    authors: list[str] = dataclasses.field(default_factory=list)
    doi: str | None = None
    title_similarity: float | None = None
    author_overlap: float | None = None
    year_match: bool | None = None
    verified: bool = False
    error: str | None = None


@dataclasses.dataclass
class EntryAudit:
    entry: BibEntry
    issues: list[str] = dataclasses.field(default_factory=list)
    warnings: list[str] = dataclasses.field(default_factory=list)
    url_result: LinkResult | None = None
    doi_result: LinkResult | None = None
    zotero: ProviderResult | None = None
    openalex: ProviderResult | None = None
    semantic_scholar: ProviderResult | None = None
    score: int = 0
    grade: str = "F"


@dataclasses.dataclass
class ZoteroRecord:
    item_id: int
    key: str
    item_type: str
    title: str | None
    year: int | None
    authors: list[str]
    doi: str | None
    url: str | None
    isbn: str | None


class Cache:
    def __init__(self, path: Path, max_age_days: int, refresh: bool) -> None:
        self.path = path
        self.max_age = dt.timedelta(days=max_age_days)
        self.refresh = refresh
        self.data: dict[str, dict[str, Any]] = {}
        if path.exists() and not refresh:
            try:
                raw = json.loads(path.read_text(encoding="utf-8"))
                if isinstance(raw, dict):
                    self.data = raw
            except (OSError, json.JSONDecodeError):
                pass

    def get(self, key: str) -> Any | None:
        item = self.data.get(key)
        if not item:
            return None
        try:
            checked = dt.datetime.fromisoformat(item["checked_at"])
        except (KeyError, TypeError, ValueError):
            return None
        now = dt.datetime.now(dt.timezone.utc)
        if checked.tzinfo is None:
            checked = checked.replace(tzinfo=dt.timezone.utc)
        if now - checked > self.max_age:
            return None
        return item.get("value")

    def set(self, key: str, value: Any) -> None:
        self.data[key] = {
            "checked_at": dt.datetime.now(dt.timezone.utc).isoformat(),
            "value": value,
        }

    def save(self) -> None:
        self.path.parent.mkdir(parents=True, exist_ok=True)
        self.path.write_text(
            json.dumps(self.data, indent=2, sort_keys=True, ensure_ascii=False) + "\n",
            encoding="utf-8",
        )


class HttpClient:
    def __init__(
        self,
        *,
        timeout: float,
        user_agent: str,
        cache: Cache,
        semantic_scholar_key: str | None,
    ) -> None:
        self.timeout = timeout
        self.user_agent = user_agent
        self.cache = cache
        self.semantic_scholar_key = semantic_scholar_key

    def request_json(
        self,
        url: str,
        *,
        cache_key: str,
        headers: dict[str, str] | None = None,
        retries: int = 2,
    ) -> tuple[int, dict[str, Any] | list[Any] | None, str | None]:
        cached = self.cache.get(cache_key)
        if cached is not None:
            return cached["status"], cached.get("data"), cached.get("error")

        request_headers = {"User-Agent": self.user_agent, "Accept": "application/json"}
        if headers:
            request_headers.update(headers)
        if self.semantic_scholar_key and "api.semanticscholar.org" in url:
            request_headers["x-api-key"] = self.semantic_scholar_key

        result: dict[str, Any] = {"status": 0, "data": None, "error": None}
        for attempt in range(retries + 1):
            try:
                request = urllib.request.Request(url, headers=request_headers)
                with urllib.request.urlopen(request, timeout=self.timeout) as response:
                    payload = response.read()
                    result = {
                        "status": response.status,
                        "data": json.loads(payload.decode("utf-8")),
                        "error": None,
                    }
                    break
            except urllib.error.HTTPError as exc:
                result = {"status": exc.code, "data": None, "error": str(exc)}
                if exc.code not in {429, 500, 502, 503, 504}:
                    break
            except (urllib.error.URLError, TimeoutError, json.JSONDecodeError) as exc:
                result = {"status": 0, "data": None, "error": str(exc)}
            if attempt < retries:
                time.sleep(1.0 * (2**attempt))

        if result["status"] in {200, 404}:
            self.cache.set(cache_key, result)
        return result["status"], result.get("data"), result.get("error")

    def check_link(self, url: str, *, cache_key: str) -> LinkResult:
        cached = self.cache.get(cache_key)
        if cached is not None:
            return LinkResult(**cached)

        start = time.monotonic()
        status: int | None = None
        final_url: str | None = None
        error: str | None = None
        headers = {"User-Agent": self.user_agent, "Accept": "*/*"}

        for method in ("HEAD", "GET"):
            try:
                request_headers = dict(headers)
                if method == "GET":
                    request_headers["Range"] = "bytes=0-1023"
                request = urllib.request.Request(url, headers=request_headers, method=method)
                with urllib.request.urlopen(request, timeout=self.timeout) as response:
                    status = response.status
                    final_url = response.geturl()
                    if method == "GET":
                        response.read(1024)
                    break
            except urllib.error.HTTPError as exc:
                status = exc.code
                final_url = exc.geturl()
                error = str(exc)
                if method == "HEAD" and exc.code in {400, 403, 405, 406, 429, 501}:
                    continue
                break
            except (urllib.error.URLError, TimeoutError, ValueError) as exc:
                error = str(exc)
                if method == "HEAD":
                    continue
                break

        elapsed_ms = round((time.monotonic() - start) * 1000)
        reachable = status is not None and 200 <= status < 400
        result = LinkResult(url, reachable, status, final_url, error, elapsed_ms)
        self.cache.set(cache_key, dataclasses.asdict(result))
        return result


def strip_outer(value: str) -> str:
    value = value.strip()
    while len(value) >= 2 and (
        (value[0] == "{" and value[-1] == "}")
        or (value[0] == '"' and value[-1] == '"')
    ):
        value = value[1:-1].strip()
    return value


def split_top_level(text: str, separator: str = ",") -> list[str]:
    parts: list[str] = []
    start = 0
    brace_depth = 0
    in_quote = False
    escaped = False
    for index, char in enumerate(text):
        if escaped:
            escaped = False
            continue
        if char == "\\":
            escaped = True
            continue
        if char == '"' and brace_depth == 0:
            in_quote = not in_quote
        elif not in_quote:
            if char == "{":
                brace_depth += 1
            elif char == "}":
                brace_depth = max(0, brace_depth - 1)
            elif char == separator and brace_depth == 0:
                parts.append(text[start:index])
                start = index + 1
    parts.append(text[start:])
    return parts


def parse_bibtex(path: Path) -> tuple[list[BibEntry], list[str]]:
    text = path.read_text(encoding="utf-8")
    entries: list[BibEntry] = []
    errors: list[str] = []
    index = 0

    while True:
        match = re.search(r"@([A-Za-z]+)\s*\{", text[index:])
        if not match:
            break
        entry_start = index + match.start()
        body_start = index + match.end()
        entry_type = match.group(1).lower()
        line = text.count("\n", 0, entry_start) + 1
        depth = 1
        in_quote = False
        escaped = False
        cursor = body_start
        while cursor < len(text) and depth:
            char = text[cursor]
            if escaped:
                escaped = False
            elif char == "\\":
                escaped = True
            elif char == '"':
                in_quote = not in_quote
            elif not in_quote:
                if char == "{":
                    depth += 1
                elif char == "}":
                    depth -= 1
            cursor += 1
        if depth:
            errors.append(f"Line {line}: unclosed @{entry_type} entry")
            break

        body = text[body_start : cursor - 1]
        parts = split_top_level(body)
        key = parts[0].strip()
        if not key:
            errors.append(f"Line {line}: entry has no citation key")
            index = cursor
            continue

        fields: dict[str, str] = {}
        for raw_field in parts[1:]:
            raw_field = raw_field.strip()
            if not raw_field:
                continue
            if "=" not in raw_field:
                errors.append(f"Line {line}: malformed field in {key}: {raw_field[:60]}")
                continue
            name, value = raw_field.split("=", 1)
            name = name.strip().lower()
            if not re.fullmatch(r"[A-Za-z][A-Za-z0-9_-]*", name):
                errors.append(f"Line {line}: invalid field name in {key}: {name}")
                continue
            if name in fields:
                errors.append(f"Line {line}: duplicate field {name} in {key}")
            fields[name] = strip_outer(value)

        entries.append(BibEntry(entry_type, key, fields, line))
        index = cursor

    return entries, errors


def latex_to_text(value: str) -> str:
    value = value.replace("``", '"').replace("''", '"')
    value = LATEX_COMMAND_RE.sub(r"\1", value)
    value = re.sub(r"\\[A-Za-z]+\s*\{([^{}]*)\}", r"\1", value)
    value = value.replace(r"\&", "&").replace(r"\%", "%").replace(r"\_", "_")
    value = value.replace("{", "").replace("}", "").replace("\\", "")
    return html.unescape(MULTISPACE_RE.sub(" ", value).strip())


def normalize_text(value: str) -> str:
    value = latex_to_text(value)
    value = unicodedata.normalize("NFKD", value)
    value = "".join(char for char in value if not unicodedata.combining(char))
    return MULTISPACE_RE.sub(" ", NON_WORD_RE.sub(" ", value.lower())).strip()


def normalize_doi(value: str) -> str:
    value = strip_outer(value).strip()
    value = re.sub(r"^https?://(?:dx\.)?doi\.org/", "", value, flags=re.IGNORECASE)
    value = re.sub(r"^doi:\s*", "", value, flags=re.IGNORECASE)
    return value.rstrip(" .").lower()


def normalize_isbn(value: str) -> str:
    return re.sub(r"[^0-9Xx]", "", value).upper()


def valid_isbn(value: str) -> bool:
    isbn = normalize_isbn(value)
    if len(isbn) == 10:
        if not re.fullmatch(r"\d{9}[\dX]", isbn):
            return False
        total = sum((10 - index) * (10 if char == "X" else int(char)) for index, char in enumerate(isbn))
        return total % 11 == 0
    if len(isbn) == 13:
        if not isbn.isdigit():
            return False
        total = sum(int(char) * (1 if index % 2 == 0 else 3) for index, char in enumerate(isbn))
        return total % 10 == 0
    return False


def author_names(entry: BibEntry) -> list[str]:
    raw = entry.fields.get("author") or entry.fields.get("editor") or ""
    return [latex_to_text(name).strip() for name in re.split(r"\s+and\s+", raw) if name.strip()]


def author_surnames(names: list[str]) -> set[str]:
    surnames: set[str] = set()
    for name in names:
        if "," in name:
            surname = name.split(",", 1)[0]
        else:
            words = name.split()
            surname = words[-1] if words else ""
        normalized = normalize_text(surname)
        if normalized:
            surnames.add(normalized)
    return surnames


def title_similarity(left: str, right: str) -> float:
    return difflib.SequenceMatcher(None, normalize_text(left), normalize_text(right)).ratio()


def overlap_score(expected: list[str], actual: list[str]) -> float:
    expected_set = author_surnames(expected)
    actual_set = author_surnames(actual)
    if not expected_set:
        return 1.0
    return len(expected_set & actual_set) / len(expected_set)


def local_audit(entry: BibEntry) -> EntryAudit:
    audit = EntryAudit(entry)
    fields = entry.fields
    required_groups = REQUIRED_FIELDS.get(entry.entry_type, (("title",), ("year",)))

    for alternatives in required_groups:
        if not any(fields.get(field, "").strip() for field in alternatives):
            audit.issues.append(f"Missing required field: {' or '.join(alternatives)}")

    if "year" in fields and not YEAR_RE.fullmatch(strip_outer(fields["year"])):
        audit.issues.append(f"Invalid year: {fields['year']}")

    doi = normalize_doi(fields.get("doi", ""))
    if fields.get("doi") and not DOI_RE.fullmatch(doi):
        audit.issues.append(f"Invalid DOI syntax: {fields['doi']}")

    url = fields.get("url", "").strip()
    if url:
        parsed = urllib.parse.urlsplit(url)
        if parsed.scheme not in {"http", "https"} or not parsed.netloc:
            audit.issues.append(f"Invalid URL: {url}")
        if doi and "doi.org" in parsed.netloc.lower():
            url_doi = normalize_doi(url)
            if url_doi != doi:
                audit.issues.append(f"DOI field and doi.org URL disagree: {doi} vs {url_doi}")
    elif doi:
        audit.warnings.append("Has DOI but no URL")

    if not doi and entry.entry_type in SCHOLARLY_TYPES:
        audit.warnings.append("No DOI")

    if "isbn" in fields:
        candidates = re.findall(
            r"(?:97[89](?:[- ]?\d){10}|\d(?:[- ]?\d){8}[- ]?[\dXx])",
            fields["isbn"],
        )
        if not candidates or not all(valid_isbn(candidate) for candidate in candidates):
            audit.issues.append(f"Invalid ISBN syntax: {fields['isbn']}")

    if "title" in fields and not normalize_text(fields["title"]):
        audit.issues.append("Title is empty after normalization")
    if "author" in fields and not author_names(entry):
        audit.issues.append("Author field could not be parsed")
    return audit


def duplicate_checks(audits: list[EntryAudit]) -> None:
    indexes: dict[str, dict[str, list[EntryAudit]]] = {
        "citation key": {},
        "DOI": {},
        "normalized title": {},
        "URL": {},
    }
    for audit in audits:
        entry = audit.entry
        values = {
            "citation key": entry.key.lower(),
            "DOI": normalize_doi(entry.fields.get("doi", "")),
            "normalized title": normalize_text(entry.fields.get("title", "")),
            "URL": entry.fields.get("url", "").strip(),
        }
        for label, value in values.items():
            if value:
                indexes[label].setdefault(value, []).append(audit)

    for label, values in indexes.items():
        for duplicates in values.values():
            if len(duplicates) > 1:
                keys = ", ".join(item.entry.key for item in duplicates)
                for audit in duplicates:
                    audit.issues.append(f"Duplicate {label}: {keys}")


def openalex_lookup(entry: BibEntry, client: HttpClient, mailto: str | None) -> ProviderResult:
    doi = normalize_doi(entry.fields.get("doi", ""))
    title = latex_to_text(entry.fields.get("title", ""))
    params = {"mailto": mailto} if mailto else {}
    matched_by = "doi" if doi else "title"
    if doi:
        encoded_doi = urllib.parse.quote(doi, safe="/")
        url = f"{OPENALEX_API}/works/https://doi.org/{encoded_doi}"
    else:
        params.update({"search": title, "per-page": "5"})
        url = f"{OPENALEX_API}/works?{urllib.parse.urlencode(params)}"
    if doi and params:
        url += "?" + urllib.parse.urlencode(params)

    status, data, error = client.request_json(
        url, cache_key=f"openalex:{matched_by}:{doi or normalize_text(title)}"
    )
    if status == 404:
        return ProviderResult("OpenAlex", "not_found", matched_by=matched_by)
    if status != 200 or not isinstance(data, dict):
        return ProviderResult("OpenAlex", "error", matched_by=matched_by, error=error or f"HTTP {status}")

    candidates = [data] if doi else data.get("results", [])
    if not candidates:
        return ProviderResult("OpenAlex", "not_found", matched_by=matched_by)
    record = max(
        candidates,
        key=lambda item: title_similarity(title, item.get("display_name", "")),
    )
    authors = [
        authorship.get("author", {}).get("display_name", "")
        for authorship in record.get("authorships", [])
        if authorship.get("author", {}).get("display_name")
    ]
    record_doi = normalize_doi(record.get("doi") or "")
    result = provider_comparison(
        provider="OpenAlex",
        entry=entry,
        matched_by=matched_by,
        record_id=record.get("id"),
        record_url=record.get("id"),
        title=record.get("display_name"),
        year=record.get("publication_year"),
        authors=authors,
        doi=record_doi or None,
    )
    return result


def semantic_scholar_lookup(entry: BibEntry, client: HttpClient) -> ProviderResult:
    doi = normalize_doi(entry.fields.get("doi", ""))
    title = latex_to_text(entry.fields.get("title", ""))
    fields = "title,year,authors,externalIds,url,venue,publicationTypes"
    matched_by = "doi" if doi else "title"
    if doi:
        paper_id = urllib.parse.quote(f"DOI:{doi}", safe="")
        url = f"{SEMANTIC_SCHOLAR_API}/paper/{paper_id}?fields={urllib.parse.quote(fields)}"
    else:
        params = urllib.parse.urlencode({"query": title, "fields": fields})
        url = f"{SEMANTIC_SCHOLAR_API}/paper/search/match?{params}"

    status, data, error = client.request_json(
        url, cache_key=f"semantic-scholar:{matched_by}:{doi or normalize_text(title)}"
    )
    if status == 404:
        return ProviderResult("Semantic Scholar", "not_found", matched_by=matched_by)
    if status != 200 or not isinstance(data, dict):
        return ProviderResult(
            "Semantic Scholar", "error", matched_by=matched_by, error=error or f"HTTP {status}"
        )

    if not doi and isinstance(data.get("data"), list):
        matches = data["data"]
        if not matches:
            return ProviderResult("Semantic Scholar", "not_found", matched_by=matched_by)
        data = max(
            matches,
            key=lambda item: title_similarity(title, item.get("title", "")),
        )

    authors = [
        author.get("name", "")
        for author in data.get("authors", [])
        if author.get("name")
    ]
    external_ids = data.get("externalIds") or {}
    record_doi = normalize_doi(external_ids.get("DOI") or "")
    return provider_comparison(
        provider="Semantic Scholar",
        entry=entry,
        matched_by=matched_by,
        record_id=data.get("paperId"),
        record_url=data.get("url"),
        title=data.get("title"),
        year=data.get("year"),
        authors=authors,
        doi=record_doi or None,
    )


def provider_comparison(
    *,
    provider: str,
    entry: BibEntry,
    matched_by: str,
    record_id: str | None,
    record_url: str | None,
    title: str | None,
    year: int | None,
    authors: list[str],
    doi: str | None,
) -> ProviderResult:
    expected_title = entry.fields.get("title", "")
    expected_year_text = strip_outer(entry.fields.get("year", ""))
    expected_year = int(expected_year_text) if YEAR_RE.fullmatch(expected_year_text) else None
    similarity = title_similarity(expected_title, title or "")
    overlap = overlap_score(author_names(entry), authors)
    year_match = expected_year is None or year is None or expected_year == year
    exact_doi = bool(
        normalize_doi(entry.fields.get("doi", ""))
        and normalize_doi(entry.fields.get("doi", "")) == normalize_doi(doi or "")
    )
    verified = exact_doi or (similarity >= 0.88 and overlap >= 0.5 and year_match)
    return ProviderResult(
        provider=provider,
        status="found",
        matched_by=matched_by,
        record_id=record_id,
        record_url=record_url,
        title=title,
        year=year,
        authors=authors,
        doi=doi,
        title_similarity=round(similarity, 3),
        author_overlap=round(overlap, 3),
        year_match=year_match,
        verified=verified,
    )


def parse_year_text(value: str | None) -> int | None:
    if not value:
        return None
    match = re.search(r"\b(\d{4})\b", value)
    if not match:
        return None
    return int(match.group(1))


def load_zotero_records(db_path: Path) -> list[ZoteroRecord]:
    query = """
    WITH item_fields AS (
        SELECT
            i.itemID AS item_id,
            i.key AS item_key,
            it.typeName AS item_type,
            f.fieldName AS field_name,
            v.value AS field_value
        FROM items i
        JOIN itemTypes it ON it.itemTypeID = i.itemTypeID
        LEFT JOIN itemData d ON d.itemID = i.itemID
        LEFT JOIN fieldsCombined f ON f.fieldID = d.fieldID
        LEFT JOIN itemDataValues v ON v.valueID = d.valueID
    ),
    author_fields AS (
        SELECT
            ic.itemID AS item_id,
            ic.orderIndex AS order_index,
            CASE
                WHEN c.fieldMode = 1 THEN c.lastName
                WHEN c.firstName IS NOT NULL AND c.firstName != ''
                    THEN c.lastName || ', ' || c.firstName
                ELSE c.lastName
            END AS author_name
        FROM itemCreators ic
        JOIN creators c ON c.creatorID = ic.creatorID
    )
    SELECT
        f.item_id,
        f.item_key,
        f.item_type,
        MAX(CASE WHEN f.field_name = 'title' THEN f.field_value END) AS title,
        MAX(CASE WHEN f.field_name = 'date' THEN f.field_value END) AS date_value,
        MAX(CASE WHEN f.field_name = 'DOI' THEN f.field_value END) AS doi,
        MAX(CASE WHEN f.field_name = 'url' THEN f.field_value END) AS url,
        MAX(CASE WHEN f.field_name = 'ISBN' THEN f.field_value END) AS isbn,
        GROUP_CONCAT(a.author_name, ' || ') AS authors
    FROM item_fields f
    LEFT JOIN author_fields a ON a.item_id = f.item_id
    GROUP BY f.item_id, f.item_key, f.item_type
    """
    with sqlite3.connect(f"file:{db_path}?mode=ro", uri=True) as conn:
        rows = conn.execute(query).fetchall()

    records: list[ZoteroRecord] = []
    for item_id, key, item_type, title, date_value, doi, url, isbn, authors in rows:
        author_list = [name.strip() for name in (authors or "").split(" || ") if name.strip()]
        records.append(
            ZoteroRecord(
                item_id=item_id,
                key=key,
                item_type=item_type,
                title=title,
                year=parse_year_text(date_value),
                authors=author_list,
                doi=normalize_doi(doi) if doi else None,
                url=url,
                isbn=normalize_isbn(isbn) if isbn else None,
            )
        )
    return records


def zotero_lookup(entry: BibEntry, records: list[ZoteroRecord]) -> ProviderResult:
    doi = normalize_doi(entry.fields.get("doi", ""))
    title = latex_to_text(entry.fields.get("title", ""))
    matched_by = "doi" if doi else "title"

    candidates = [
        record for record in records if record.doi and doi and record.doi == doi
    ] if doi else []
    if not candidates:
        normalized_title = normalize_text(title)
        candidates = [
            record
            for record in records
            if record.title and normalize_text(record.title) == normalized_title
        ]
    if not candidates:
        candidates = [
            record
            for record in records
            if record.title and title_similarity(title, record.title) >= 0.88
        ]
    if not candidates:
        return ProviderResult("Zotero", "not_found", matched_by=matched_by)

    record = max(
        candidates,
        key=lambda item: (
            1 if doi and item.doi == doi else 0,
            title_similarity(title, item.title or ""),
            overlap_score(author_names(entry), item.authors),
        ),
    )
    return provider_comparison(
        provider="Zotero",
        entry=entry,
        matched_by="doi" if doi and record.doi == doi else "title",
        record_id=str(record.item_id),
        record_url=f"zotero://select/library/items/{record.key}",
        title=record.title,
        year=record.year,
        authors=record.authors,
        doi=record.doi,
    )


def calculate_score(audit: EntryAudit, offline: bool) -> None:
    score = 100
    score -= 20 * len(audit.issues)
    score -= 5 * len(audit.warnings)

    if audit.entry.entry_type in SCHOLARLY_TYPES:
        if not (audit.zotero and audit.zotero.verified):
            score -= 10

    if not offline:
        if audit.url_result and not audit.url_result.reachable:
            score -= 15
        if audit.doi_result and not audit.doi_result.reachable:
            score -= 20
        providers = [audit.zotero, audit.openalex, audit.semantic_scholar]
        found = [result for result in providers if result and result.status == "found"]
        verified = [result for result in found if result.verified]
        if audit.entry.entry_type in SCHOLARLY_TYPES and len(verified) >= 2:
            score += 5

    audit.score = max(0, min(100, score))
    if audit.score >= 90:
        audit.grade = "A"
    elif audit.score >= 80:
        audit.grade = "B"
    elif audit.score >= 70:
        audit.grade = "C"
    elif audit.score >= 60:
        audit.grade = "D"
    else:
        audit.grade = "F"


def pct(numerator: int, denominator: int) -> str:
    return f"{(100 * numerator / denominator):.1f}%" if denominator else "n/a"


def mark(value: bool | None) -> str:
    if value is True:
        return "Yes"
    if value is False:
        return "No"
    return "n/a"


def provider_label(result: ProviderResult | None) -> str:
    if result is None:
        return "Not checked"
    if result.status == "error":
        return f"Error: {result.error}"
    if result.status == "not_found":
        return "No record collected"
    verdict = "Collected and verified" if result.verified else "Collected, not verified"
    return (
        f"{verdict}; title {result.title_similarity:.0%}, "
        f"authors {result.author_overlap:.0%}, year {mark(result.year_match)}"
    )


def report_summary(audits: list[EntryAudit], parse_errors: list[str], offline: bool) -> dict[str, Any]:
    total = len(audits)
    scholarly = [audit for audit in audits if audit.entry.entry_type in SCHOLARLY_TYPES]
    with_doi = [audit for audit in audits if audit.entry.fields.get("doi")]
    with_url = [audit for audit in audits if audit.entry.fields.get("url")]
    reachable_urls = [
        audit for audit in with_url if audit.url_result and audit.url_result.reachable
    ]
    reachable_dois = [
        audit for audit in with_doi if audit.doi_result and audit.doi_result.reachable
    ]
    openalex_collected = [
        audit for audit in audits if audit.openalex and audit.openalex.status == "found"
    ]
    zotero_collected = [
        audit for audit in audits if audit.zotero and audit.zotero.status == "found"
    ]
    s2_collected = [
        audit
        for audit in audits
        if audit.semantic_scholar and audit.semantic_scholar.status == "found"
    ]
    zotero_verified = [
        audit for audit in audits if audit.zotero and audit.zotero.verified
    ]
    openalex_verified = [
        audit for audit in audits if audit.openalex and audit.openalex.verified
    ]
    s2_verified = [
        audit for audit in audits if audit.semantic_scholar and audit.semantic_scholar.verified
    ]
    either_verified = [
        audit
        for audit in audits
        if (audit.zotero and audit.zotero.verified)
        or (audit.openalex and audit.openalex.verified)
        or (audit.semantic_scholar and audit.semantic_scholar.verified)
    ]
    both_verified = [
        audit
        for audit in audits
        if sum(
            1
            for result in (audit.zotero, audit.openalex, audit.semantic_scholar)
            if result and result.verified
        ) >= 2
    ]
    return {
        "total": total,
        "scholarly": len(scholarly),
        "with_doi": len(with_doi),
        "with_url": len(with_url),
        "reachable_urls": len(reachable_urls),
        "reachable_dois": len(reachable_dois),
        "zotero_collected": len(zotero_collected),
        "zotero_verified": len(zotero_verified),
        "openalex_collected": len(openalex_collected),
        "semantic_scholar_collected": len(s2_collected),
        "openalex_verified": len(openalex_verified),
        "semantic_scholar_verified": len(s2_verified),
        "either_verified": len(either_verified),
        "both_verified": len(both_verified),
        "entries_with_issues": sum(bool(audit.issues) for audit in audits),
        "entries_with_warnings": sum(bool(audit.warnings) for audit in audits),
        "parse_errors": len(parse_errors),
        "average_score": round(sum(audit.score for audit in audits) / total, 1) if total else 0,
        "offline": offline,
    }


def render_markdown(
    bib_path: Path,
    audits: list[EntryAudit],
    parse_errors: list[str],
    offline: bool,
) -> str:
    summary = report_summary(audits, parse_errors, offline)
    generated = dt.datetime.now().astimezone().isoformat(timespec="seconds")
    lines = [
        "# Ethics References Report Card",
        "",
        f"Generated: `{generated}`",
        f"Bibliography: `{bib_path}`",
        f"Mode: `{'offline' if offline else 'live network verification'}`",
        "",
        "## Overall",
        "",
        f"**Average score: {summary['average_score']}/100** across {summary['total']} references.",
        "",
        "| Measure | Count | Coverage |",
        "|---|---:|---:|",
        f"| References | {summary['total']} | 100% |",
        f"| Scholarly-type references | {summary['scholarly']} | {pct(summary['scholarly'], summary['total'])} |",
        f"| References with a DOI | {summary['with_doi']} | {pct(summary['with_doi'], summary['total'])} |",
        f"| References with a URL | {summary['with_url']} | {pct(summary['with_url'], summary['total'])} |",
    ]
    if not offline:
        lines.extend(
            [
                f"| Reachable cited URLs | {summary['reachable_urls']} | {pct(summary['reachable_urls'], summary['with_url'])} of URLs |",
                f"| Reachable DOI resolvers | {summary['reachable_dois']} | {pct(summary['reachable_dois'], summary['with_doi'])} of DOIs |",
                f"| Zotero records collected | {summary['zotero_collected']} | {pct(summary['zotero_collected'], summary['total'])} |",
                f"| Zotero metadata verified | {summary['zotero_verified']} | {pct(summary['zotero_verified'], summary['total'])} |",
                f"| OpenAlex records collected | {summary['openalex_collected']} | {pct(summary['openalex_collected'], summary['total'])} |",
                f"| OpenAlex metadata verified | {summary['openalex_verified']} | {pct(summary['openalex_verified'], summary['total'])} |",
                f"| Semantic Scholar records collected | {summary['semantic_scholar_collected']} | {pct(summary['semantic_scholar_collected'], summary['total'])} |",
                f"| Semantic Scholar metadata verified | {summary['semantic_scholar_verified']} | {pct(summary['semantic_scholar_verified'], summary['total'])} |",
                f"| Metadata verified by at least one source | {summary['either_verified']} | {pct(summary['either_verified'], summary['total'])} |",
                f"| Metadata verified by at least two sources | {summary['both_verified']} | {pct(summary['both_verified'], summary['total'])} |",
            ]
        )
    lines.extend(
        [
            f"| Entries with local errors | {summary['entries_with_issues']} | {pct(summary['entries_with_issues'], summary['total'])} |",
            f"| Entries with warnings | {summary['entries_with_warnings']} | {pct(summary['entries_with_warnings'], summary['total'])} |",
            "",
            "## Interpretation",
            "",
            "- `Collected` means the provider returned a candidate record. Collection alone does not validate the citation.",
            "- `Verified` means the collected record had an exact DOI match, or strong title and author similarity with a compatible year.",
            "- `Collected, not verified` means a candidate record was retrieved but its metadata did not meet the verification threshold.",
            "- `Zotero` checks compare the citation against your local Zotero library in `/Users/jackb/Zotero`.",
            "- `No record collected` is not necessarily an error for web pages, films, archival documents, and other non-scholarly sources.",
            "- Network/API errors are reported separately and do not mean that a citation is invalid.",
            "- Scores emphasize local citation correctness, reachable identifiers, and independent metadata agreement. They are diagnostics, not scholarly-quality judgments.",
            "",
        ]
    )

    if parse_errors:
        lines.extend(["## BibTeX Parse Errors", ""])
        lines.extend(f"- {error}" for error in parse_errors)
        lines.append("")

    problem_audits = [
        audit
        for audit in audits
        if audit.issues
        or audit.warnings
        or (audit.url_result and not audit.url_result.reachable)
        or (audit.doi_result and not audit.doi_result.reachable)
        or (
            audit.entry.entry_type in SCHOLARLY_TYPES
            and not (
                (audit.zotero and audit.zotero.verified)
                or
                (audit.openalex and audit.openalex.verified)
                or (audit.semantic_scholar and audit.semantic_scholar.verified)
            )
        )
    ]
    lines.extend(["## Action Items", ""])
    if not problem_audits:
        lines.append("No action items.")
    else:
        for audit in sorted(problem_audits, key=lambda item: (item.score, item.entry.key)):
            details = list(audit.issues) + list(audit.warnings)
            if audit.url_result and not audit.url_result.reachable:
                details.append(
                    f"URL unreachable ({audit.url_result.status or audit.url_result.error})"
                )
            if audit.doi_result and not audit.doi_result.reachable:
                details.append(
                    f"DOI resolver unreachable ({audit.doi_result.status or audit.doi_result.error})"
                )
            if (
                audit.entry.entry_type in SCHOLARLY_TYPES
                and not (
                    (audit.zotero and audit.zotero.verified)
                    or
                    (audit.openalex and audit.openalex.verified)
                    or (audit.semantic_scholar and audit.semantic_scholar.verified)
                )
            ):
                details.append(
                    "Not verified by Zotero"
                    if offline
                    else "Not verified by Zotero, OpenAlex, or Semantic Scholar"
                )
            lines.append(
                f"- **{audit.entry.key}** ({audit.grade}, {audit.score}/100): "
                + "; ".join(details)
            )
    lines.append("")

    lines.extend(
        [
            "## Reference Details",
            "",
            "| Key | Type | Grade | DOI | URL | Zotero | OpenAlex | Semantic Scholar |",
            "|---|---|---:|---|---|---|---|---|",
        ]
    )
    for audit in sorted(audits, key=lambda item: item.entry.key.lower()):
        doi_status = "Missing"
        if audit.entry.fields.get("doi"):
            doi_status = (
                mark(audit.doi_result.reachable)
                if audit.doi_result
                else "Present"
            )
        url_status = "Missing"
        if audit.entry.fields.get("url"):
            url_status = (
                mark(audit.url_result.reachable)
                if audit.url_result
                else "Present"
            )
        cells = [
            audit.entry.key,
            audit.entry.entry_type,
            f"{audit.grade} ({audit.score})",
            doi_status,
            url_status,
            provider_label(audit.zotero),
            provider_label(audit.openalex),
            provider_label(audit.semantic_scholar),
        ]
        lines.append("| " + " | ".join(cell.replace("|", r"\|") for cell in cells) + " |")
    lines.append("")

    lines.extend(["## Per-Reference Notes", ""])
    for audit in sorted(audits, key=lambda item: item.entry.key.lower()):
        entry = audit.entry
        lines.extend(
            [
                f"### `{entry.key}`",
                "",
                f"- Citation: {latex_to_text(entry.fields.get('title', '(no title)'))}",
                f"- Type/year: `{entry.entry_type}` / `{entry.fields.get('year', 'missing')}`",
                f"- Local checks: {'Pass' if not audit.issues else '; '.join(audit.issues)}",
                f"- Warnings: {'None' if not audit.warnings else '; '.join(audit.warnings)}",
            ]
        )
        if audit.url_result:
            lines.append(
                f"- URL: {mark(audit.url_result.reachable)}"
                f" (HTTP {audit.url_result.status or 'n/a'}, {audit.url_result.elapsed_ms} ms)"
            )
        if audit.doi_result:
            lines.append(
                f"- DOI resolver: {mark(audit.doi_result.reachable)}"
                f" (HTTP {audit.doi_result.status or 'n/a'}, {audit.doi_result.elapsed_ms} ms)"
            )
        lines.append(f"- Zotero: {provider_label(audit.zotero)}")
        if not offline:
            lines.append(f"- OpenAlex: {provider_label(audit.openalex)}")
            lines.append(f"- Semantic Scholar: {provider_label(audit.semantic_scholar)}")
        lines.extend([f"- Score: **{audit.grade} ({audit.score}/100)**", ""])
    return "\n".join(lines)


def json_payload(
    bib_path: Path,
    audits: list[EntryAudit],
    parse_errors: list[str],
    offline: bool,
) -> dict[str, Any]:
    return {
        "generated_at": dt.datetime.now(dt.timezone.utc).isoformat(),
        "bibliography": str(bib_path),
        "summary": report_summary(audits, parse_errors, offline),
        "parse_errors": parse_errors,
        "references": [
            {
                "key": audit.entry.key,
                "type": audit.entry.entry_type,
                "line": audit.entry.line,
                "fields": audit.entry.fields,
                "issues": audit.issues,
                "warnings": audit.warnings,
                "url_check": dataclasses.asdict(audit.url_result) if audit.url_result else None,
                "doi_check": dataclasses.asdict(audit.doi_result) if audit.doi_result else None,
                "zotero": dataclasses.asdict(audit.zotero) if audit.zotero else None,
                "openalex": dataclasses.asdict(audit.openalex) if audit.openalex else None,
                "semantic_scholar": (
                    dataclasses.asdict(audit.semantic_scholar)
                    if audit.semantic_scholar
                    else None
                ),
                "score": audit.score,
                "grade": audit.grade,
            }
            for audit in audits
        ],
    }


def run_network_checks(
    audits: list[EntryAudit],
    client: HttpClient,
    mailto: str | None,
    workers: int,
) -> None:
    link_jobs: list[tuple[EntryAudit, str, str]] = []
    for audit in audits:
        url = audit.entry.fields.get("url", "").strip()
        doi = normalize_doi(audit.entry.fields.get("doi", ""))
        if url:
            link_jobs.append((audit, "url", url))
        if doi:
            link_jobs.append((audit, "doi", f"https://doi.org/{doi}"))

    def check_link(job: tuple[EntryAudit, str, str]) -> tuple[EntryAudit, str, LinkResult]:
        audit, kind, url = job
        result = client.check_link(url, cache_key=f"link:{url}")
        return audit, kind, result

    print(
        f"Reachability: checking {len(link_jobs)} cited URL/DOI targets "
        f"with {workers} workers.",
        file=sys.stderr,
    )
    with concurrent.futures.ThreadPoolExecutor(max_workers=workers) as executor:
        futures = [executor.submit(check_link, job) for job in link_jobs]
        for completed, future in enumerate(
            concurrent.futures.as_completed(futures), start=1
        ):
            audit, kind, result = future.result()
            if kind == "url":
                audit.url_result = result
            else:
                audit.doi_result = result
            outcome = (
                f"reachable (HTTP {result.status})"
                if result.reachable
                else f"not reachable ({result.status or result.error})"
            )
            print(
                f"Reachability [{completed}/{len(link_jobs)}]: "
                f"{audit.entry.key} {kind.upper()} is {outcome}.",
                file=sys.stderr,
            )

    print(
        "Metadata: collecting candidate records, then verifying each candidate "
        "against the BibTeX title, authors, year, and DOI.",
        file=sys.stderr,
    )
    for index, audit in enumerate(audits, start=1):
        print(
            f"Metadata [{index}/{len(audits)}]: {audit.entry.key}",
            file=sys.stderr,
        )
        audit.openalex = openalex_lookup(audit.entry, client, mailto)
        print(
            f"  OpenAlex collection: {provider_collection_label(audit.openalex)}",
            file=sys.stderr,
        )
        print(
            f"  OpenAlex verification: {provider_verification_label(audit.openalex)}",
            file=sys.stderr,
        )
        audit.semantic_scholar = semantic_scholar_lookup(audit.entry, client)
        print(
            "  Semantic Scholar collection: "
            f"{provider_collection_label(audit.semantic_scholar)}",
            file=sys.stderr,
        )
        print(
            "  Semantic Scholar verification: "
            f"{provider_verification_label(audit.semantic_scholar)}",
            file=sys.stderr,
        )
        time.sleep(0.1)


def provider_collection_label(result: ProviderResult) -> str:
    if result.status == "found":
        return f"candidate record collected via {result.matched_by}"
    if result.status == "not_found":
        return "no candidate record collected"
    return f"collection error ({result.error})"


def provider_verification_label(result: ProviderResult) -> str:
    if result.status != "found":
        return "not attempted because no candidate record was available"
    if result.verified:
        return "verified against local citation metadata"
    return (
        "not verified "
        f"(title {result.title_similarity:.0%}, authors {result.author_overlap:.0%}, "
        f"year {mark(result.year_match)})"
    )


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Audit references.bib and write Markdown and JSON report cards."
    )
    parser.add_argument("--bib", type=Path, default=DEFAULT_BIB, help="BibTeX file to audit")
    parser.add_argument(
        "--output", type=Path, default=DEFAULT_REPORT, help="Markdown report path"
    )
    parser.add_argument(
        "--json-output", type=Path, default=DEFAULT_JSON, help="JSON report path"
    )
    parser.add_argument("--offline", action="store_true", help="skip URL and metadata APIs")
    parser.add_argument(
        "--zotero-db",
        type=Path,
        default=DEFAULT_ZOTERO_DB,
        help="path to the Zotero sqlite library used for local metadata verification",
    )
    parser.add_argument("--limit", type=int, help="audit only the first N references")
    parser.add_argument("--timeout", type=float, default=15.0, help="HTTP timeout in seconds")
    parser.add_argument("--workers", type=int, default=6, help="concurrent URL checks")
    parser.add_argument("--cache", type=Path, default=DEFAULT_CACHE, help="HTTP cache path")
    parser.add_argument("--cache-days", type=int, default=7, help="cache lifetime")
    parser.add_argument("--refresh-cache", action="store_true", help="ignore cached results")
    parser.add_argument(
        "--mailto",
        default=os.environ.get("OPENALEX_MAILTO"),
        help="contact email sent to OpenAlex (or set OPENALEX_MAILTO)",
    )
    parser.add_argument(
        "--semantic-scholar-key",
        default=os.environ.get("SEMANTIC_SCHOLAR_API_KEY"),
        help="Semantic Scholar API key (or set SEMANTIC_SCHOLAR_API_KEY)",
    )
    parser.add_argument(
        "--fail-under",
        type=float,
        help="exit 2 if the average score is below this threshold",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    bib_path = args.bib.resolve()
    zotero_db_path = args.zotero_db.resolve()
    if not bib_path.exists():
        print(f"Error: bibliography not found: {bib_path}", file=sys.stderr)
        return 1
    if not zotero_db_path.exists():
        print(f"Error: Zotero database not found: {zotero_db_path}", file=sys.stderr)
        return 1
    if args.limit is not None and args.limit < 1:
        print("Error: --limit must be at least 1", file=sys.stderr)
        return 1
    if args.workers < 1:
        print("Error: --workers must be at least 1", file=sys.stderr)
        return 1

    print(f"Input: reading bibliography from {bib_path}", file=sys.stderr)
    entries, parse_errors = parse_bibtex(bib_path)
    if args.limit:
        entries = entries[: args.limit]
        print(f"Input: limiting this run to {len(entries)} references.", file=sys.stderr)
    else:
        print(f"Input: parsed {len(entries)} references.", file=sys.stderr)
    if parse_errors:
        print(f"Input: found {len(parse_errors)} BibTeX parse errors.", file=sys.stderr)

    print("Local checks: validating fields, identifiers, and duplicates.", file=sys.stderr)
    audits = [local_audit(entry) for entry in entries]
    duplicate_checks(audits)
    local_errors = sum(len(audit.issues) for audit in audits)
    local_warnings = sum(len(audit.warnings) for audit in audits)
    print(
        f"Local checks: complete with {local_errors} errors and "
        f"{local_warnings} warnings.",
        file=sys.stderr,
    )

    print(f"Zotero: reading library data from {zotero_db_path}", file=sys.stderr)
    try:
        zotero_records = load_zotero_records(zotero_db_path)
    except sqlite3.Error as exc:
        print(f"Error: could not read Zotero database: {exc}", file=sys.stderr)
        return 1
    print(f"Zotero: loaded {len(zotero_records)} library items.", file=sys.stderr)

    print("Zotero: matching local references against the library.", file=sys.stderr)
    for index, audit in enumerate(audits, start=1):
        audit.zotero = zotero_lookup(audit.entry, zotero_records)
        print(
            f"Zotero [{index}/{len(audits)}]: {audit.entry.key} "
            f"{provider_verification_label(audit.zotero)}",
            file=sys.stderr,
        )

    cache = Cache(args.cache.resolve(), args.cache_days, args.refresh_cache)
    if not args.offline:
        contact = args.mailto or "bibliography-checker"
        user_agent = f"data-adventures-reference-checker/1.0 ({contact})"
        client = HttpClient(
            timeout=args.timeout,
            user_agent=user_agent,
            cache=cache,
            semantic_scholar_key=args.semantic_scholar_key,
        )
        run_network_checks(audits, client, args.mailto, args.workers)
        print(f"Cache: writing reusable API results to {cache.path}", file=sys.stderr)
        cache.save()
    else:
        print(
            "Network checks: skipped in offline mode; no reachability or "
            "provider metadata claims will be made.",
            file=sys.stderr,
        )

    print("Scoring: calculating per-reference grades.", file=sys.stderr)
    for audit in audits:
        calculate_score(audit, args.offline)

    print("Reports: rendering Markdown and JSON report cards.", file=sys.stderr)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.json_output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(
        render_markdown(bib_path, audits, parse_errors, args.offline) + "\n",
        encoding="utf-8",
    )
    args.json_output.write_text(
        json.dumps(
            json_payload(bib_path, audits, parse_errors, args.offline),
            indent=2,
            ensure_ascii=False,
        )
        + "\n",
        encoding="utf-8",
    )

    summary = report_summary(audits, parse_errors, args.offline)
    print(f"Wrote {args.output}")
    print(f"Wrote {args.json_output}")
    print(
        f"References: {summary['total']}; DOI: {summary['with_doi']}; "
        f"URL: {summary['with_url']}; average score: {summary['average_score']}"
    )
    print(
        "Zotero records: "
        f"{summary['zotero_collected']} collected, "
        f"{summary['zotero_verified']} metadata-verified"
    )
    if not args.offline:
        print(
            "OpenAlex records: "
            f"{summary['openalex_collected']} collected, "
            f"{summary['openalex_verified']} metadata-verified"
        )
        print(
            "Semantic Scholar records: "
            f"{summary['semantic_scholar_collected']} collected, "
            f"{summary['semantic_scholar_verified']} metadata-verified"
        )
    if parse_errors:
        return 1
    if args.fail_under is not None and summary["average_score"] < args.fail_under:
        return 2
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
