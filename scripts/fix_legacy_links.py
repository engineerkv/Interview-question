#!/usr/bin/env python3
"""Second migration pass: remove footer nav blocks and repair legacy-style links."""

import json
import os
import re
from pathlib import Path
from urllib.parse import unquote

ROOT = Path(__file__).resolve().parent.parent
DOCS = ROOT / "docs"
MAPPING = json.loads((ROOT / "scripts" / "migration-map.json").read_text())
REVERSE = {v: k for k, v in MAPPING.items()}

NAV_DIV = re.compile(r'<div align="center">\s*\n(.*?)\n\s*</div>\s*\n?', re.S)
NAV_WORDS = re.compile(r"Previous|Next|Home|Cheatsheet|Question", re.I)
LINK = re.compile(r"\[([^\]]*)\]\(([^)\s]+)\)")


def is_nav(inner: str) -> bool:
    lines = [line for line in inner.splitlines() if line.strip()]
    return bool(lines) and all("](" in line and NAV_WORDS.search(line) for line in lines)


def fix_file(path: Path, broken: list):
    new_rel = path.relative_to(DOCS).as_posix()
    old_rel = REVERSE.get(new_rel)
    text = path.read_text(encoding="utf-8")
    text = NAV_DIV.sub(lambda m: "" if is_nav(m.group(1)) else m.group(0), text)

    if old_rel:
        old_dir, new_dir = os.path.dirname(old_rel), os.path.dirname(new_rel)

        def repl(m):
            label, target = m.group(1), m.group(2)
            if re.match(r"^[a-z]+:", target) or target.startswith(("#", "./", "../")) and (DOCS / new_dir / target.split("#")[0]).exists():
                return m.group(0)
            path_part, _, anchor = target.partition("#")
            if not path_part.endswith(".md"):
                return m.group(0)
            resolved = os.path.normpath(os.path.join(old_dir, unquote(path_part)))
            if resolved not in MAPPING:
                sibling = os.path.join(old_dir, os.path.basename(unquote(path_part)))
                resolved = sibling if sibling in MAPPING else None
            if not resolved:
                if not (DOCS / new_dir / unquote(path_part)).exists():
                    broken.append(f"{new_rel}: {target}")
                    return label
                return m.group(0)
            rel = os.path.relpath(MAPPING[resolved], new_dir)
            rel = rel if rel.startswith(".") else f"./{rel}"
            return f"[{label}]({rel}{'#' + anchor if anchor else ''})"

        text = LINK.sub(repl, text)

    text = re.sub(r"(\n---\s*\n)(\s*---\s*\n)+", r"\1", text)
    path.write_text(re.sub(r"\n{3,}", "\n\n", text), encoding="utf-8")


def main():
    broken = []
    for path in DOCS.rglob("*.md"):
        fix_file(path, broken)
    if broken:
        print("Unlinked:\n" + "\n".join(broken))


if __name__ == "__main__":
    main()
