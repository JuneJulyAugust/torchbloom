from __future__ import annotations

import argparse
from pathlib import Path
import re
from typing import Any

import yaml


FRONTMATTER_BOUNDARY = "---"
LOCAL_LINK_RE = re.compile(r"(?<!!)\[[^\]]+\]\(([^)]+)\)")


def required_frontmatter_keys() -> set[str]:
    return {
        "id",
        "type",
        "title",
        "chapter_scope",
        "source_anchors",
        "confidence",
        "prerequisites",
        "related",
        "learning_objectives",
    }


def validate_wiki_tree(wiki_root: Path, repo_root: Path | None = None) -> list[str]:
    wiki_root = Path(wiki_root)
    repo_root = Path(".") if repo_root is None else Path(repo_root)
    errors: list[str] = []

    for page in sorted(wiki_root.rglob("*.md")):
        rel_page = _relative_for_message(page, repo_root)
        text = page.read_text(encoding="utf-8")
        frontmatter, body, parse_error = _parse_frontmatter(text)
        if parse_error:
            errors.append(f"{rel_page}: {parse_error}")
            continue

        errors.extend(_validate_required_keys(rel_page, frontmatter))
        errors.extend(_validate_source_anchors(rel_page, frontmatter, repo_root))
        errors.extend(_validate_markdown_links(rel_page, page, body))

    return errors


def _parse_frontmatter(text: str) -> tuple[dict[str, Any], str, str | None]:
    lines = text.splitlines()
    if not lines or lines[0].strip() != FRONTMATTER_BOUNDARY:
        return {}, text, "missing YAML frontmatter"

    for index, line in enumerate(lines[1:], start=1):
        if line.strip() == FRONTMATTER_BOUNDARY:
            raw_yaml = "\n".join(lines[1:index])
            data = yaml.safe_load(raw_yaml) or {}
            if not isinstance(data, dict):
                return {}, "\n".join(lines[index + 1 :]), "frontmatter must be a mapping"
            return data, "\n".join(lines[index + 1 :]), None

    return {}, text, "unterminated YAML frontmatter"


def _validate_required_keys(rel_page: str, frontmatter: dict[str, Any]) -> list[str]:
    errors: list[str] = []
    for key in sorted(required_frontmatter_keys()):
        if key not in frontmatter:
            errors.append(f"{rel_page}: missing frontmatter key: {key}")
    return errors


def _validate_source_anchors(rel_page: str, frontmatter: dict[str, Any], repo_root: Path) -> list[str]:
    errors: list[str] = []
    anchors = frontmatter.get("source_anchors", [])
    if not isinstance(anchors, list):
        return [f"{rel_page}: source_anchors must be a list"]

    for index, anchor in enumerate(anchors, start=1):
        if not isinstance(anchor, dict):
            errors.append(f"{rel_page}: source_anchors[{index}] must be a mapping")
            continue
        locator = str(anchor.get("locator", "")).strip()
        if _looks_like_local_locator(locator):
            local = repo_root / _strip_anchor(locator)
            if not local.exists():
                errors.append(f"{rel_page}: missing source anchor: {locator}")

    return errors


def _validate_markdown_links(rel_page: str, page: Path, body: str) -> list[str]:
    errors: list[str] = []
    for match in LOCAL_LINK_RE.finditer(body):
        raw_target = match.group(1).strip()
        target = raw_target.split()[0].strip("<>")
        if _is_external_or_anchor(target):
            continue
        if not target.endswith(".md"):
            continue
        target_path = page.parent / _strip_anchor(target)
        if not target_path.exists():
            errors.append(f"{rel_page}: broken markdown link: {raw_target}")
    return errors


def _looks_like_local_locator(locator: str) -> bool:
    if not locator or _is_external_or_anchor(locator):
        return False
    return (
        locator.startswith("raw/")
        or locator.startswith("docs/")
        or locator.startswith("wiki/")
        or locator.endswith(".md")
        or locator.endswith(".json")
    )


def _is_external_or_anchor(target: str) -> bool:
    return target.startswith(("http://", "https://", "mailto:", "#"))


def _strip_anchor(target: str) -> str:
    return target.split("#", 1)[0]


def _relative_for_message(path: Path, repo_root: Path) -> str:
    try:
        return str(path.relative_to(repo_root))
    except ValueError:
        return str(path)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Validate TorchBloom wiki Markdown metadata and links.")
    parser.add_argument("--wiki-root", default="wiki/udl")
    parser.add_argument("--repo-root", default=".")
    args = parser.parse_args(argv)

    errors = validate_wiki_tree(Path(args.wiki_root), repo_root=Path(args.repo_root))
    if errors:
        for error in errors:
            print(error)
        return 1

    print(f"{args.wiki_root}: ok")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
