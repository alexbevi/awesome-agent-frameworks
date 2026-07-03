#!/usr/bin/env python3
"""Generate README.md from data/frameworks.json and data/README.template.md."""
from __future__ import annotations

import argparse
import json
import re
import sys
import unicodedata
from collections import defaultdict
from pathlib import Path
from typing import Any


ENTRY_RE = re.compile(r"^[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+$")
PLACEHOLDERS = {
    "{{ contents }}",
    "{{ framework_sections }}",
    "{{ related_lists }}",
}


def ascii_text(value: str) -> str:
    value = unicodedata.normalize("NFKD", value)
    return value.encode("ascii", "ignore").decode("ascii")


def clean_spaces(value: str) -> str:
    return re.sub(r"\s+", " ", value).strip()


def sort_key(value: str) -> str:
    value = ascii_text(value).lower()
    value = re.sub(r"[^a-z0-9]+", " ", value)
    return clean_spaces(value)


def github_slug(heading: str) -> str:
    slug = ascii_text(heading).lower()
    slug = re.sub(r"[^\w\s-]", "", slug)
    slug = re.sub(r"\s+", "-", slug.strip())
    return slug


def markdown_label(value: str) -> str:
    return ascii_text(value).replace("[", r"\[").replace("]", r"\]")


def load_data(path: Path) -> dict[str, Any]:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        raise SystemExit(f"{path}: invalid JSON: {exc}") from exc


def require_string(item: dict[str, Any], key: str, context: str) -> str:
    value = item.get(key)
    if not isinstance(value, str) or not value.strip():
        raise ValueError(f"{context}: missing non-empty string field {key!r}")
    return value.strip()


def validate_data(data: dict[str, Any]) -> tuple[list[dict[str, str]], list[dict[str, str]], list[dict[str, str]]]:
    errors: list[str] = []
    categories_raw = data.get("categories")
    frameworks_raw = data.get("frameworks")
    related_raw = data.get("related_lists", [])

    if not isinstance(categories_raw, list) or not categories_raw:
        raise SystemExit("data/frameworks.json: expected non-empty categories list")
    if not isinstance(frameworks_raw, list) or not frameworks_raw:
        raise SystemExit("data/frameworks.json: expected non-empty frameworks list")
    if not isinstance(related_raw, list):
        raise SystemExit("data/frameworks.json: expected related_lists to be a list")

    categories: list[dict[str, str]] = []
    category_names: set[str] = set()
    for index, raw in enumerate(categories_raw):
        if not isinstance(raw, dict):
            errors.append(f"categories[{index}]: expected object")
            continue
        try:
            name = require_string(raw, "name", f"categories[{index}]")
            description = require_string(raw, "description", f"categories[{index}]")
        except ValueError as exc:
            errors.append(str(exc))
            continue
        if name in category_names:
            errors.append(f"categories[{index}]: duplicate category {name!r}")
        category_names.add(name)
        categories.append({"name": name, "description": description.rstrip(".") + "."})

    frameworks: list[dict[str, str]] = []
    seen_repos: set[str] = set()
    for index, raw in enumerate(frameworks_raw):
        if not isinstance(raw, dict):
            errors.append(f"frameworks[{index}]: expected object")
            continue
        context = f"frameworks[{index}]"
        try:
            name = require_string(raw, "name", context)
            category = require_string(raw, "category", context)
            url = require_string(raw, "url", context)
            repo = raw.get("repo", "")
            if repo is None:
                repo = ""
            if not isinstance(repo, str):
                errors.append(f"{context}: repo must be a string when present")
                repo = ""
            repo = repo.strip()
            description = require_string(raw, "description", context)
        except ValueError as exc:
            errors.append(str(exc))
            continue
        if category not in category_names:
            errors.append(f"{context}: unknown category {category!r}")
        if not url.startswith("https://"):
            errors.append(f"{context}: url must be an HTTPS URL")
        if repo:
            if not ENTRY_RE.match(repo):
                errors.append(f"{context}: repo must be owner/repo")
            if url.rstrip("/").lower() != f"https://github.com/{repo}".lower():
                errors.append(f"{context}: url must match repo")
            repo_key = repo.lower()
            if repo_key in seen_repos:
                errors.append(f"{context}: duplicate repo {repo!r}")
            seen_repos.add(repo_key)
        if not description.endswith("."):
            errors.append(f"{context}: description must end with a period")
        frameworks.append(
            {
                "name": name,
                "category": category,
                "url": url,
                "repo": repo,
                "description": description,
            }
        )

    related_lists: list[dict[str, str]] = []
    for index, raw in enumerate(related_raw):
        if not isinstance(raw, dict):
            errors.append(f"related_lists[{index}]: expected object")
            continue
        context = f"related_lists[{index}]"
        try:
            name = require_string(raw, "name", context)
            url = require_string(raw, "url", context)
            description = require_string(raw, "description", context)
        except ValueError as exc:
            errors.append(str(exc))
            continue
        related_lists.append({"name": name, "url": url, "description": description.rstrip(".") + "."})

    if errors:
        for error in errors:
            print(f"error: {error}", file=sys.stderr)
        raise SystemExit(1)
    return categories, frameworks, related_lists


def render_contents(categories: list[dict[str, str]]) -> str:
    lines = [f"- [{category['name']}](#{github_slug(category['name'])})" for category in categories]
    lines.extend(
        [
            "- [Related Awesome Lists](#related-awesome-lists)",
            "- [Contribute](#contribute)",
            "- [License](#license)",
        ]
    )
    return "\n".join(lines)


def render_sections(categories: list[dict[str, str]], frameworks: list[dict[str, str]]) -> str:
    by_category: dict[str, list[dict[str, str]]] = defaultdict(list)
    for framework in frameworks:
        by_category[framework["category"]].append(framework)

    sections: list[str] = []
    for category in categories:
        entries = sorted(by_category.get(category["name"], []), key=lambda item: sort_key(item["name"]))
        if not entries:
            continue
        lines = [
            f'<a id="{github_slug(category["name"])}"></a>',
            f'## {category["name"]}',
            "",
            category["description"],
            "",
        ]
        for entry in entries:
            badge = (
                f" ![GitHub Repo stars](https://img.shields.io/github/stars/{entry['repo']}?style=social)"
                if entry.get("repo")
                else ""
            )
            lines.append(
                f"- [{markdown_label(entry['name'])}]({entry['url']}){badge} - {entry['description']}"
            )
        sections.append("\n".join(lines))
    return "\n\n".join(sections)


def render_related(related_lists: list[dict[str, str]]) -> str:
    return "\n".join(
        f"- [{item['name']}]({item['url']}) - {item['description']}" for item in related_lists
    )


def render_readme(template: str, categories: list[dict[str, str]], frameworks: list[dict[str, str]], related_lists: list[dict[str, str]]) -> str:
    missing = [placeholder for placeholder in PLACEHOLDERS if placeholder not in template]
    if missing:
        raise SystemExit(f"template missing placeholders: {', '.join(sorted(missing))}")
    rendered = template
    rendered = rendered.replace("{{ contents }}", render_contents(categories))
    rendered = rendered.replace("{{ framework_sections }}", render_sections(categories, frameworks))
    rendered = rendered.replace("{{ related_lists }}", render_related(related_lists))
    return rendered.rstrip() + "\n"


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="Fail if README.md is out of date")
    parser.add_argument("--repo-root", type=Path, default=Path(__file__).resolve().parents[1])
    args = parser.parse_args()

    repo_root = args.repo_root.resolve()
    data = load_data(repo_root / "data" / "frameworks.json")
    categories, frameworks, related_lists = validate_data(data)
    template = (repo_root / "data" / "README.template.md").read_text(encoding="utf-8")
    rendered = render_readme(template, categories, frameworks, related_lists)

    readme_path = repo_root / "README.md"
    if args.check:
        existing = readme_path.read_text(encoding="utf-8") if readme_path.exists() else ""
        if existing != rendered:
            print("README.md is out of date. Run scripts/generate-readme.py", file=sys.stderr)
            return 1
    else:
        readme_path.write_text(rendered, encoding="utf-8")

    print(f"generated README.md from {len(frameworks)} entries across {len(categories)} categories")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
