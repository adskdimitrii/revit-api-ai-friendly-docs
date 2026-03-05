#!/usr/bin/env python3

from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import time
from dataclasses import dataclass
from pathlib import Path
from typing import Optional
from urllib.parse import urljoin, urlparse
import xml.etree.ElementTree as ET

import requests
from bs4 import BeautifulSoup
from html_to_markdown import convert_to_markdown


DEFAULT_SITEMAP_URL = "https://www.revitapidocs.com/2026/sitemap.xml"
BASE_DOCS_URL = "https://www.revitapidocs.com/2026/"
USER_AGENT = "agent-project-template-revit-crawler/1.0"


@dataclass
class PageRecord:
    url: str
    html: str
    title: str
    namespace: Optional[str]
    output_path: Path


def slugify(text: str) -> str:
    cleaned = re.sub(r"\s+", " ", text).strip()
    slug = re.sub(r"[^a-zA-Z0-9._-]+", "-", cleaned)
    slug = re.sub(r"-+", "-", slug).strip("-._")
    return slug or "untitled"


def ensure_dir(path: Path) -> None:
    path.mkdir(parents=True, exist_ok=True)


def clean_previous_markdown(output_dir: Path) -> None:
    for md_file in output_dir.rglob("*.md"):
        md_file.unlink()

    for json_file in output_dir.rglob("_crawl_errors.json"):
        json_file.unlink()

    removable_dirs = sorted(
        [d for d in output_dir.rglob("*") if d.is_dir() and d.name != ".cache"],
        key=lambda path: len(path.parts),
        reverse=True,
    )
    for directory in removable_dirs:
        if directory == output_dir:
            continue
        try:
            directory.rmdir()
        except OSError:
            pass


def parse_sitemap_urls(xml_text: str) -> list[str]:
    root = ET.fromstring(xml_text)
    namespace = {"sm": "http://www.sitemaps.org/schemas/sitemap/0.9"}
    urls = [node.text.strip() for node in root.findall("sm:url/sm:loc", namespace) if node.text]
    return urls


def normalize_revit_url(url: str) -> str:
    parsed = urlparse(url)
    path = parsed.path or "/"
    if path != "/" and path.endswith("/"):
        path = path.rstrip("/")
    return f"https://www.revitapidocs.com{path}"


def is_revit_2026_url(url: str) -> bool:
    parsed = urlparse(url)
    return parsed.netloc == "www.revitapidocs.com" and parsed.path.startswith("/2026")


def collect_internal_links(html: str, source_url: str) -> set[str]:
    soup = BeautifulSoup(html, "html.parser")
    found: set[str] = set()
    for link in soup.find_all("a", href=True):
        href = (link.get("href") or "").strip()
        if not href:
            continue
        absolute = urljoin(source_url, href)
        if is_revit_2026_url(absolute):
            found.add(normalize_revit_url(absolute))
    return found


def extract_title(soup: BeautifulSoup, url: str) -> str:
    for selector in ["main h1", "main h2", "main h3", "main h4", "h1", "h2", "h3", "h4"]:
        node = soup.select_one(selector)
        if node:
            text = node.get_text(" ", strip=True)
            if text:
                return text

    if soup.title and soup.title.get_text(strip=True):
        return soup.title.get_text(" ", strip=True)

    path = urlparse(url).path.rstrip("/")
    return path.split("/")[-1] or "Revit API 2026"


def maybe_namespace_from_title(title: str) -> Optional[str]:
    match = re.match(r"^([A-Za-z0-9_.]+)\s+Namespace$", title)
    if match:
        return match.group(1)
    return None


def clean_namespace_name(namespace: str) -> str:
    cleaned = re.sub(r"\s+", " ", namespace).strip()
    cleaned = re.sub(r"\s+Namespace$", "", cleaned, flags=re.IGNORECASE)
    return cleaned


def extract_namespace(soup: BeautifulSoup, title: str) -> Optional[str]:
    from_title = maybe_namespace_from_title(title)
    if from_title:
        return from_title

    text_nodes = soup.find_all(string=re.compile(r"\bNamespace\s*:\s*", re.IGNORECASE))
    for text_node in text_nodes:
        parent = text_node.parent
        if not parent:
            continue

        link = parent.find("a")
        if link:
            candidate = link.get_text(" ", strip=True)
            if candidate and "." in candidate:
                return clean_namespace_name(candidate)

        next_link = parent.find_next("a")
        if next_link:
            candidate = next_link.get_text(" ", strip=True)
            if candidate and "." in candidate:
                return clean_namespace_name(candidate)

    ref_heading = soup.find(["h1", "h2", "h3", "h4"], string=re.compile(r"^\s*Reference\s*$", re.IGNORECASE))
    if ref_heading:
        for link in ref_heading.find_all_next("a", limit=8):
            candidate = link.get_text(" ", strip=True)
            if candidate and "." in candidate and not candidate.endswith("Class"):
                return clean_namespace_name(candidate)

    return None


def relative_doc_path(url: str, namespace: Optional[str], title: str, used_paths: set[Path]) -> Path:
    parsed = urlparse(url)
    raw_path = parsed.path.strip("/")

    if raw_path in {"2026", "2026/"}:
        candidate = Path("index.md")
    elif raw_path in {"2026/news", "2026/news/"}:
        candidate = Path("api-changes-2026.md")
    else:
        filename = f"{slugify(title)}.md"
        if namespace:
            candidate = Path(namespace) / filename
        else:
            candidate = Path("ungrouped") / filename

    if candidate not in used_paths:
        used_paths.add(candidate)
        return candidate

    stem = candidate.stem
    suffix = candidate.suffix
    parent = candidate.parent
    index = 2
    while True:
        deduped = parent / f"{stem}-{index}{suffix}"
        if deduped not in used_paths:
            used_paths.add(deduped)
            return deduped
        index += 1


def strip_unwanted_sections(container: BeautifulSoup) -> None:
    selectors = [
        "script",
        "style",
        "noscript",
        "header",
        "footer",
        "nav",
        ".navbar",
        ".site-footer",
        ".footer",
        ".copyright",
    ]
    for selector in selectors:
        for node in container.select(selector):
            node.decompose()


def to_markdown(html: str, source_url: str, title: str) -> str:
    soup = BeautifulSoup(html, "html.parser")
    container = soup.select_one("main") or soup.select_one("article") or soup.body or soup
    strip_unwanted_sections(container)

    body = convert_to_markdown(
        str(container),
        heading_style="atx",
        remove_navigation=True,
        preprocess_html=False,
    )
    body = re.sub(r"\n{3,}", "\n\n", body).strip()
    return f"# {title}\n\nSource: {source_url}\n\n---\n\n{body}\n"


def localize_markdown_links(
    markdown_text: str,
    source_url: str,
    current_output_path: Path,
    url_to_output_path: dict[str, Path],
) -> str:
    link_pattern = re.compile(r"\[([^\]]+)\]\(([^)]+)\)")

    def replace_link(match: re.Match[str]) -> str:
        label = match.group(1)
        target = match.group(2).strip()

        if target.startswith("mailto:") or target.startswith("tel:"):
            return match.group(0)

        if target.startswith("#"):
            return match.group(0)

        absolute = urljoin(source_url, target)

        parsed = urlparse(absolute)
        if parsed.scheme in {"http", "https"} and parsed.netloc == "www.revitapidocs.com" and parsed.path.startswith("/2026"):
            normalized = normalize_revit_url(absolute)
            anchor = f"#{parsed.fragment}" if parsed.fragment else ""
            output_path = url_to_output_path.get(normalized)
            if output_path:
                current_parent = current_output_path.parent
                relative_str = os.path.relpath(output_path.as_posix(), start=current_parent.as_posix())
                return f"[{label}]({relative_str}{anchor})"

        return match.group(0)

    return link_pattern.sub(replace_link, markdown_text)


def fetch_with_cache(session: requests.Session, url: str, cache_dir: Path, timeout: int, delay: float) -> str:
    key = hashlib.sha256(url.encode("utf-8")).hexdigest()
    cache_file = cache_dir / f"{key}.html"

    if cache_file.exists():
        print(f"[CACHE] {url}")
        return cache_file.read_text(encoding="utf-8")

    response = session.get(url, timeout=timeout)
    response.raise_for_status()
    html = response.text
    cache_file.write_text(html, encoding="utf-8")

    if delay > 0:
        time.sleep(delay)

    return html


def build_records(
    session: requests.Session,
    urls: list[str],
    output_dir: Path,
    cache_dir: Path,
    timeout: int,
    delay: float,
    max_pages: Optional[int],
) -> tuple[list[PageRecord], dict[str, Path], list[str]]:
    records: list[PageRecord] = []
    url_to_output_path: dict[str, Path] = {}
    errors: list[str] = []
    used_paths: set[Path] = set()

    seed_targets = urls[:max_pages] if max_pages and max_pages > 0 else urls
    queue: list[str] = [normalize_revit_url(url) for url in seed_targets]
    queued: set[str] = set(queue)
    processed: set[str] = set()
    index = 0

    while queue:
        url = queue.pop(0)
        if url in processed:
            continue
        index += 1
        try:
            html = fetch_with_cache(session, url, cache_dir, timeout, delay)
            soup = BeautifulSoup(html, "html.parser")
            title = extract_title(soup, url)
            namespace = extract_namespace(soup, title)
            rel_output = relative_doc_path(url, namespace, title, used_paths)

            record = PageRecord(
                url=url,
                html=html,
                title=title,
                namespace=namespace,
                output_path=output_dir / rel_output,
            )
            records.append(record)
            url_to_output_path[normalize_revit_url(url)] = rel_output
            processed.add(url)

            if not max_pages:
                for discovered in collect_internal_links(html, url):
                    if discovered not in processed and discovered not in queued:
                        queue.append(discovered)
                        queued.add(discovered)

            print(f"[OK] ({index}) {url} -> {rel_output}")
        except Exception as exc:
            processed.add(url)
            errors.append(f"{url} :: {exc}")
            print(f"[WARN] ({index}) {url} :: {exc}")

    return records, url_to_output_path, errors


def write_markdown(records: list[PageRecord], url_to_output_path: dict[str, Path], output_dir: Path) -> None:
    for record in records:
        markdown = to_markdown(record.html, record.url, record.title)
        localized = localize_markdown_links(
            markdown,
            record.url,
            record.output_path.relative_to(output_dir),
            url_to_output_path,
        )

        ensure_dir(record.output_path.parent)
        record.output_path.write_text(localized, encoding="utf-8")


def write_url_index(url_to_output_path: dict[str, Path], output_dir: Path) -> None:
    lines = [
        "# Revit 2026 URL Index",
        "",
        "Auto-generated mapping from source URLs to local markdown files.",
        "",
    ]
    for url in sorted(url_to_output_path):
        lines.append(f"- {url} -> {url_to_output_path[url].as_posix()}")

    (output_dir / "_url_index.md").write_text("\n".join(lines) + "\n", encoding="utf-8")


def write_readme(output_dir: Path, total: int) -> None:
    content = f"""# Revit API Docs 2026

This folder contains a local markdown crawl of Revit API Docs 2026.

- Source sitemap: {DEFAULT_SITEMAP_URL}
- Total pages processed: {total}
- Organization: namespace-based subfolders (for API pages), plus root-level index/change pages

## Generated Files

- `_url_index.md`: URL to local file mapping.
- Namespace folders such as `Autodesk.Revit.DB`, `Autodesk.Revit.DB.Structure`, etc.

## Regenerate

Run:

```bash
python docs/revit/2026/crawl_docs.py
```
"""
    (output_dir / "README.md").write_text(content, encoding="utf-8")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Crawl Revit API Docs 2026 sitemap into local markdown files.")
    parser.add_argument("--sitemap-url", default=DEFAULT_SITEMAP_URL)
    parser.add_argument("--output-dir", default="docs/revit/2026")
    parser.add_argument("--timeout", type=int, default=30)
    parser.add_argument("--delay", type=float, default=0.5)
    parser.add_argument("--max-pages", type=int, default=0, help="Optional limit for test runs.")
    parser.add_argument("--test", action="store_true", help="Run in test mode (first 50 URLs only).")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    output_dir = Path(args.output_dir)
    cache_dir = output_dir / ".cache"
    ensure_dir(output_dir)
    ensure_dir(cache_dir)
    clean_previous_markdown(output_dir)

    session = requests.Session()
    session.headers.update({"User-Agent": USER_AGENT})

    print(f"[INFO] Fetching sitemap: {args.sitemap_url}")
    sitemap_resp = session.get(args.sitemap_url, timeout=args.timeout)
    sitemap_resp.raise_for_status()
    urls = parse_sitemap_urls(sitemap_resp.text)

    if not urls:
        raise RuntimeError("No URLs found in sitemap.")

    max_pages = args.max_pages if args.max_pages and args.max_pages > 0 else None
    if args.test:
        max_pages = 50
    print(f"[INFO] URLs discovered: {len(urls)}")
    if max_pages:
        print(f"[INFO] Limiting run to first {max_pages} pages")

    records, url_to_output_path, errors = build_records(
        session=session,
        urls=urls,
        output_dir=output_dir,
        cache_dir=cache_dir,
        timeout=args.timeout,
        delay=args.delay,
        max_pages=max_pages,
    )

    print(f"[INFO] Writing markdown for {len(records)} pages")
    write_markdown(records, url_to_output_path, output_dir)
    write_url_index(url_to_output_path, output_dir)
    write_readme(output_dir, len(records))

    if errors:
        error_file = output_dir / "_crawl_errors.json"
        error_file.write_text(json.dumps(errors, indent=2), encoding="utf-8")
        print(f"[WARN] Completed with {len(errors)} errors. See {error_file}")
    else:
        print("[INFO] Completed with no fetch errors")

    print("[INFO] Done")


if __name__ == "__main__":
    main()
