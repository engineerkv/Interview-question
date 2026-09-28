#!/usr/bin/env python3
"""One-time migration of the legacy Markdown tree into Docusaurus `docs/`.

Moves files with `git mv` (history preserved), renames them to URL-safe slugs,
strips the legacy HTML navigation blocks, adds sidebar frontmatter, and
rewrites relative Markdown links to the new locations.
"""

import json
import os
import re
import subprocess
import sys
from pathlib import Path
from urllib.parse import unquote

ROOT = Path(__file__).resolve().parent.parent
DOCS = ROOT / "docs"

FOLDER_MAP = {
    "FE/Javascript": "fundamentals/javascript",
    "FE/Typescript": "fundamentals/typescript",
    "DSA": "fundamentals/dsa",
    "FE/HTML": "frontend/html",
    "FE/CSS": "frontend/css",
    "FE/React": "frontend/react",
    "FE/Next": "frontend/nextjs",
    "FE/React-Native": "frontend/react-native",
    "FE/FE-System-Design": "frontend/architecture",
    "BE/Node-Express": "backend/node-express",
    "BE/Sql": "backend/sql",
    "BE/No-Sql": "backend/mongodb",
    "BE/BE-System-Design": "backend/architecture",
    "Projects": "case-studies",
    "Puzzles": "puzzles",
}

FILE_OVERRIDES = {
    "FE/README.md": "frontend/index.md",
    "Code-Reviews/README.md": "leadership/code-reviews/manual-review-guide.md",
    "rule.md": "contributing/answer-playbook.md",
    "BE/BE-System-Design/06) AWS Cloud Architecture.md": "devops/cloud/01-aws-cloud-architecture.md",
    "BE/BE-System-Design/07) Observability.md": "devops/telemetry/01-cloudwatch-and-new-relic.md",
    "BE/BE-System-Design/10) Git, Docker, CI-CD, Tooling.md": "devops/ci-cd-and-releases/01-git-docker-ci-cd-tooling.md",
}

CATEGORY_LABELS = {
    "fundamentals": ("Programming Fundamentals", 1),
    "fundamentals/javascript": ("JavaScript", 1),
    "fundamentals/typescript": ("TypeScript", 2),
    "fundamentals/dsa": ("Data Structures & Algorithms", 3),
    "frontend": ("Frontend Engineering", 2),
    "frontend/html": ("HTML", 1),
    "frontend/css": ("CSS", 2),
    "frontend/react": ("React", 3),
    "frontend/nextjs": ("Next.js", 4),
    "frontend/react-native": ("React Native", 5),
    "frontend/architecture": ("Frontend Architecture (Deep Dives)", 6),
    "backend": ("Backend Engineering", 3),
    "backend/node-express": ("Node.js & Express", 1),
    "backend/sql": ("SQL", 3),
    "backend/mongodb": ("MongoDB (NoSQL)", 4),
    "backend/architecture": ("Backend Architecture", 9),
    "case-studies": ("System Design Case Studies", 5),
    "puzzles": ("Puzzles", 9),
    "leadership": ("Tech Lead & Leadership", 8),
    "leadership/code-reviews": ("Code Reviews", 1),
    "contributing": ("Contributing", 11),
}


def slugify(name: str) -> str:
    stem = name[:-3] if name.endswith(".md") else name
    m = re.match(r"^(\d+)\)\s*(.*)$", stem)
    prefix, rest = (m.group(1), m.group(2)) if m else (None, stem)
    rest = rest.replace("&", " and ").replace("+", " plus ")
    rest = re.sub(r"[^A-Za-z0-9]+", "-", rest).strip("-").lower()
    return f"{prefix}-{rest}.md" if prefix else f"{rest}.md"


def target_name(filename: str) -> str:
    if filename == "question.md":
        return "question-index.md"
    if filename == "README.md":
        return "index.md"
    if "Cheatsheet" in filename:
        return "cheatsheet.md"
    return slugify(filename)


def build_mapping() -> dict:
    mapping = {}
    for old_dir, new_dir in FOLDER_MAP.items():
        for path in sorted((ROOT / old_dir).glob("*.md")):
            rel = path.relative_to(ROOT).as_posix()
            mapping[rel] = f"{new_dir}/{target_name(path.name)}"
    mapping.update(FILE_OVERRIDES)
    return mapping


NAV_START = re.compile(r"^##\s*📍\s*Navigation\s*$")
FENCE = re.compile(r"^\s*(```|~~~)")
LINK = re.compile(r"(!?)\[([^\]]*)\]\(([^)\s]+)\)")


def strip_nav_blocks(text: str) -> str:
    out, in_code, skipping = [], False, False
    for line in text.split("\n"):
        if not skipping and FENCE.match(line):
            in_code = not in_code
        if skipping:
            if line.strip() == "</div>":
                skipping = False
            continue
        if not in_code and NAV_START.match(line):
            skipping = True
            continue
        out.append(line)
    text = "\n".join(out)
    text = re.sub(r"(\n---\s*\n)(\s*---\s*\n)+", r"\1", text)
    return re.sub(r"\n{3,}", "\n\n", text)


def rewrite_links(text: str, old_rel: str, new_rel: str, mapping: dict, broken: list) -> str:
    old_dir = os.path.dirname(old_rel)
    new_dir = os.path.dirname(new_rel)

    def repl(m):
        bang, label, target = m.group(1), m.group(2), m.group(3)
        if bang or re.match(r"^[a-z]+:", target) or target.startswith("#"):
            return m.group(0)
        path, _, anchor = target.partition("#")
        resolved = os.path.normpath(os.path.join(old_dir, unquote(path)))
        if resolved.endswith("/") or not resolved.endswith(".md"):
            candidate = os.path.join(resolved, "README.md")
            resolved = candidate if candidate in mapping else resolved
        if resolved not in mapping:
            broken.append(f"{old_rel}: {target}")
            return label
        new_target = os.path.relpath(mapping[resolved], new_dir)
        if not new_target.startswith("."):
            new_target = f"./{new_target}"
        return f"[{label}]({new_target}{'#' + anchor if anchor else ''})"

    out, in_code = [], False
    for line in text.split("\n"):
        if FENCE.match(line):
            in_code = not in_code
            out.append(line)
            continue
        out.append(line if in_code else LINK.sub(repl, line))
    return "\n".join(out)


def sidebar_label(new_rel: str, text: str) -> str:
    name = os.path.basename(new_rel)
    if name == "question-index.md":
        return "Question Index"
    if name == "cheatsheet.md":
        return "Cheatsheet"
    if name == "index.md":
        return "Overview"
    h1 = re.search(r"^#\s+(.+)$", text, re.M)
    label = h1.group(1) if h1 else name
    label = re.sub(r"^[^\w(]+", "", label)
    label = re.sub(r"^\d+\.\s*", "", label)
    label = re.sub(r"\s*\((Q|P)[^)]*\)\s*$", "", label)
    return label.strip() or name


def add_frontmatter(text: str, new_rel: str) -> str:
    if text.startswith("---\n"):
        return text
    name = os.path.basename(new_rel)
    fm = {"sidebar_label": sidebar_label(new_rel, text)}
    if name == "question-index.md":
        fm["sidebar_position"] = 0
    elif name == "cheatsheet.md":
        fm["sidebar_position"] = 100
    lines = ["---"] + [f"{k}: {json.dumps(v, ensure_ascii=False)}" for k, v in fm.items()] + ["---", ""]
    return "\n".join(lines) + text.lstrip("\n")


def write_categories():
    for rel, (label, pos) in CATEGORY_LABELS.items():
        folder = DOCS / rel
        folder.mkdir(parents=True, exist_ok=True)
        data = {"label": label, "position": pos}
        if not (folder / "index.md").exists():
            data["link"] = {"type": "generated-index", "description": f"{label} interview preparation."}
        (folder / "_category_.json").write_text(json.dumps(data, indent=2) + "\n")


def main():
    mapping = build_mapping()
    for old_rel, new_rel in mapping.items():
        dest = DOCS / new_rel
        dest.parent.mkdir(parents=True, exist_ok=True)
        subprocess.run(["git", "mv", old_rel, str(dest.relative_to(ROOT))], cwd=ROOT, check=True)

    broken = []
    for old_rel, new_rel in mapping.items():
        dest = DOCS / new_rel
        text = dest.read_text(encoding="utf-8")
        text = strip_nav_blocks(text)
        text = rewrite_links(text, old_rel, new_rel, mapping, broken)
        text = add_frontmatter(text, new_rel)
        dest.write_text(text, encoding="utf-8")

    write_categories()
    (ROOT / "scripts" / "migration-map.json").write_text(json.dumps(mapping, indent=2) + "\n")
    print(f"Moved {len(mapping)} files")
    if broken:
        print(f"{len(broken)} links pointed to missing files and were unlinked:")
        print("\n".join(sorted(set(broken))))


if __name__ == "__main__":
    sys.exit(main())
