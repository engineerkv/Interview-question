#!/usr/bin/env python3
"""Find relative Markdown links that do not resolve on disk."""

from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1] / "docs"
LINK_RE = re.compile(r"\[[^\]]*\]\(([^)]+)\)")


def is_local(url: str) -> bool:
    if not url or url.startswith(("#", "http://", "https://", "mailto:", "pathname://")):
        return False
    return True


def target_exists(source: Path, url: str) -> bool:
    path_part = url.split("#", 1)[0].split("?", 1)[0]
    if not path_part:
        return True
    resolved = (source.parent / path_part).resolve()
    if resolved.is_file():
        return True
    if resolved.suffix == "" and resolved.with_suffix(".md").is_file():
        return True
    if resolved.is_dir() and (resolved / "index.md").is_file():
        return True
    return False


def main() -> int:
    broken: list[str] = []
    for md in ROOT.rglob("*.md"):
        text = md.read_text(encoding="utf-8")
        for match in LINK_RE.finditer(text):
            url = match.group(1).strip()
            if not is_local(url):
                continue
            if not target_exists(md, url):
                rel = md.relative_to(ROOT)
                broken.append(f"{rel}: {url}")
    for item in broken:
        print(item)
    print(f"\nBroken local Markdown links: {len(broken)}")
    return 1 if broken else 0


if __name__ == "__main__":
    raise SystemExit(main())
