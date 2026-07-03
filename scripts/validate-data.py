#!/usr/bin/env python3
"""Lint data/frameworks.json and verify README.md is generated from it."""
from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
import unicodedata
from collections import Counter
from pathlib import Path
from typing import Any


ENTRY_RE = re.compile(r"^[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+$")
ALLOWED_TOP_LEVEL_KEYS = {"categories", "frameworks", "related_lists"}
ALLOWED_CATEGORY_KEYS = {"name", "description"}
ALLOWED_FRAMEWORK_KEYS = {"name", "category", "url", "repo", "description"}
ALLOWED_RELATED_KEYS = {"name", "url", "description"}
FORBIDDEN_DESCRIPTION_TERMS = (
    "awesome",
    "best",
    "game-changing",
    "revolutionary",
    "ultimate",
)


class LintError(Exception):
    """Raised when validation finds one or more lint errors."""


def ascii_text(value: str) -> str:
    value = unicodedata.normalize("NFKD", value)
    return value.encode("ascii", "ignore").decode("ascii")


def clean_spaces(value: str) -> str:
    return re.sub(r"\s+", " ", value).strip()


def sort_key(value: str) -> str:
    value = ascii_text(value).lower()
    value = re.sub(r"[^a-z0-9]+", " ", value)
    return clean_spaces(value)


def duplicate_key_guard(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
    seen: set[str] = set()
    result: dict[str, Any] = {}
    for key, value in pairs:
        if key in seen:
            raise ValueError(f"duplicate JSON object key {key!r}")
        seen.add(key)
        result[key] = value
    return result


def load_json(path: Path) -> dict[str, Any]:
    try:
        return json.loads(path.read_text(encoding="utf-8"), object_pairs_hook=duplicate_key_guard)
    except json.JSONDecodeError as exc:
        raise LintError(f"{path}: invalid JSON: {exc}") from exc
    except ValueError as exc:
        raise LintError(f"{path}: {exc}") from exc


def require_string(item: dict[str, Any], key: str, context: str, errors: list[str]) -> str:
    value = item.get(key)
    if not isinstance(value, str) or not value.strip():
        errors.append(f"{context}: missing non-empty string field {key!r}")
        return ""
    if value != value.strip():
        errors.append(f"{context}.{key}: must not have leading or trailing whitespace")
    if "\n" in value or "\r" in value:
        errors.append(f"{context}.{key}: must be a single line")
    if value != ascii_text(value):
        errors.append(f"{context}.{key}: must use ASCII text")
    return value.strip()


def validate_keys(item: dict[str, Any], allowed: set[str], context: str, errors: list[str]) -> None:
    extra = set(item) - allowed
    missing = allowed - set(item)
    for key in sorted(missing):
        errors.append(f"{context}: missing required key {key!r}")
    for key in sorted(extra):
        errors.append(f"{context}: unknown key {key!r}")


def validate_sentence(value: str, context: str, errors: list[str]) -> None:
    if not value:
        return
    if not re.match(r"^[A-Z0-9`]", value):
        errors.append(f"{context}: must start with a capital letter, number, or code literal")
    if not value.endswith("."):
        errors.append(f"{context}: must end with a period")
    if len(value) > 220:
        errors.append(f"{context}: must be 220 characters or fewer")
    if "[" in value or "]" in value or "http://" in value or "https://" in value:
        errors.append(f"{context}: must not contain markdown links or URLs")
    if "  " in value:
        errors.append(f"{context}: must not contain repeated spaces")
    lowered = value.lower()
    for term in FORBIDDEN_DESCRIPTION_TERMS:
        if re.search(rf"\b{re.escape(term)}\b", lowered):
            errors.append(f"{context}: avoid subjective or hype term {term!r}")


def validate_data(data: dict[str, Any]) -> tuple[list[dict[str, str]], list[dict[str, str]], list[dict[str, str]]]:
    errors: list[str] = []
    validate_keys(data, ALLOWED_TOP_LEVEL_KEYS, "root", errors)

    raw_categories = data.get("categories")
    raw_frameworks = data.get("frameworks")
    raw_related = data.get("related_lists")
    if not isinstance(raw_categories, list) or not raw_categories:
        errors.append("root.categories: must be a non-empty list")
        raw_categories = []
    if not isinstance(raw_frameworks, list) or not raw_frameworks:
        errors.append("root.frameworks: must be a non-empty list")
        raw_frameworks = []
    if not isinstance(raw_related, list):
        errors.append("root.related_lists: must be a list")
        raw_related = []

    categories: list[dict[str, str]] = []
    category_names: set[str] = set()
    for index, raw in enumerate(raw_categories):
        context = f"categories[{index}]"
        if not isinstance(raw, dict):
            errors.append(f"{context}: must be an object")
            continue
        validate_keys(raw, ALLOWED_CATEGORY_KEYS, context, errors)
        name = require_string(raw, "name", context, errors)
        description = require_string(raw, "description", context, errors)
        validate_sentence(description, f"{context}.description", errors)
        if name in category_names:
            errors.append(f"{context}.name: duplicate category {name!r}")
        category_names.add(name)
        categories.append({"name": name, "description": description})

    frameworks: list[dict[str, str]] = []
    repo_counts: Counter[str] = Counter()
    name_counts: Counter[str] = Counter()
    url_counts: Counter[str] = Counter()
    for index, raw in enumerate(raw_frameworks):
        context = f"frameworks[{index}]"
        if not isinstance(raw, dict):
            errors.append(f"{context}: must be an object")
            continue
        validate_keys(raw, ALLOWED_FRAMEWORK_KEYS, context, errors)
        name = require_string(raw, "name", context, errors)
        category = require_string(raw, "category", context, errors)
        url = require_string(raw, "url", context, errors)
        repo = require_string(raw, "repo", context, errors)
        description = require_string(raw, "description", context, errors)
        validate_sentence(description, f"{context}.description", errors)
        if category and category not in category_names:
            errors.append(f"{context}.category: unknown category {category!r}")
        if repo and not ENTRY_RE.match(repo):
            errors.append(f"{context}.repo: must be owner/repo")
        if url and not url.startswith("https://github.com/"):
            errors.append(f"{context}.url: must be a GitHub URL")
        if url and repo and url.rstrip("/").lower() != f"https://github.com/{repo}".lower():
            errors.append(f"{context}.url: must match repo field")
        if name:
            name_counts[sort_key(name)] += 1
        if repo:
            repo_counts[repo.lower()] += 1
        if url:
            url_counts[url.rstrip("/").lower()] += 1
        frameworks.append(
            {
                "name": name,
                "category": category,
                "url": url,
                "repo": repo,
                "description": description,
            }
        )

    for label, counts in (("name", name_counts), ("repo", repo_counts), ("url", url_counts)):
        for value, count in counts.items():
            if count > 1:
                errors.append(f"frameworks: duplicate {label} {value!r}")

    category_order = {category["name"]: index for index, category in enumerate(categories)}
    expected_frameworks = sorted(
        frameworks,
        key=lambda item: (category_order.get(item["category"], 999), sort_key(item["name"])),
    )
    actual_order = [(item["category"], sort_key(item["name"]), item["repo"].lower()) for item in frameworks]
    expected_order = [(item["category"], sort_key(item["name"]), item["repo"].lower()) for item in expected_frameworks]
    if actual_order != expected_order:
        for index, (actual, expected) in enumerate(zip(frameworks, expected_frameworks)):
            if actual != expected:
                errors.append(
                    "frameworks: entries must be sorted by category order and name; "
                    f"first mismatch at index {index}: {actual['name']!r} should be {expected['name']!r}"
                )
                break

    related_lists: list[dict[str, str]] = []
    for index, raw in enumerate(raw_related):
        context = f"related_lists[{index}]"
        if not isinstance(raw, dict):
            errors.append(f"{context}: must be an object")
            continue
        validate_keys(raw, ALLOWED_RELATED_KEYS, context, errors)
        name = require_string(raw, "name", context, errors)
        url = require_string(raw, "url", context, errors)
        description = require_string(raw, "description", context, errors)
        validate_sentence(description, f"{context}.description", errors)
        related_lists.append({"name": name, "url": url, "description": description})

    expected_related = sorted(related_lists, key=lambda item: sort_key(item["name"]))
    if related_lists != expected_related:
        errors.append("related_lists: entries must be sorted by name")

    if errors:
        for error in errors:
            print(f"error: {error}", file=sys.stderr)
        raise LintError(f"{len(errors)} lint error(s)")
    return categories, frameworks, related_lists


def check_readme(repo_root: Path) -> None:
    result = subprocess.run(
        [sys.executable, str(repo_root / "scripts" / "generate-readme.py"), "--check"],
        cwd=repo_root,
        text=True,
        capture_output=True,
    )
    if result.returncode:
        if result.stdout:
            print(result.stdout, end="")
        if result.stderr:
            print(result.stderr, end="", file=sys.stderr)
        raise LintError("README.md is not current")


def check_github_repos(frameworks: list[dict[str, str]]) -> None:
    errors: list[str] = []
    repos = [item["repo"] for item in frameworks]
    for offset in range(0, len(repos), 50):
        batch = repos[offset : offset + 50]
        fields: list[str] = []
        for index, repo in enumerate(batch):
            owner, name = repo.split("/", 1)
            fields.append(
                "r{index}: repository(owner:{owner}, name:{name}) "
                "{{ nameWithOwner isPrivate isDisabled }}".format(
                    index=index,
                    owner=json.dumps(owner),
                    name=json.dumps(name),
                )
            )
        query = "query { " + " ".join(fields) + " }"
        result = subprocess.run(
            ["gh", "api", "graphql", "-f", f"query={query}"],
            text=True,
            capture_output=True,
        )
        if result.returncode:
            errors.append("gh api graphql failed while validating repositories")
            continue
        payload = json.loads(result.stdout)
        if payload.get("errors"):
            errors.extend(f"GitHub API error: {error.get('message', error)}" for error in payload["errors"])
        data = payload.get("data") or {}
        for index, repo in enumerate(batch):
            item = data.get(f"r{index}")
            if item is None:
                errors.append(f"{repo}: repository not found")
                continue
            actual = item["nameWithOwner"]
            if actual.lower() != repo.lower():
                errors.append(f"{repo}: repository has canonical name {actual}")
            if item.get("isPrivate"):
                errors.append(f"{repo}: repository is private")
            if item.get("isDisabled"):
                errors.append(f"{repo}: repository is disabled")
    if errors:
        for error in errors:
            print(f"error: {error}", file=sys.stderr)
        raise LintError(f"{len(errors)} GitHub validation error(s)")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo-root", type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument("--no-readme", action="store_true", help="Skip README freshness validation")
    parser.add_argument("--check-github", action="store_true", help="Validate GitHub repositories with gh")
    args = parser.parse_args()

    repo_root = args.repo_root.resolve()
    data_path = repo_root / "data" / "frameworks.json"
    try:
        data = load_json(data_path)
        categories, frameworks, related_lists = validate_data(data)
        if not args.no_readme:
            check_readme(repo_root)
        if args.check_github:
            check_github_repos(frameworks)
    except LintError as exc:
        print(f"data validation failed: {exc}", file=sys.stderr)
        return 1

    print(
        "data ok: {frameworks} frameworks, {categories} categories, {related} related lists".format(
            frameworks=len(frameworks),
            categories=len(categories),
            related=len(related_lists),
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
