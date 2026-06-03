from pathlib import Path

from torchbloom.wiki_validation import (
    required_frontmatter_keys,
    validate_wiki_tree,
)


def _valid_page(path: Path, locator: str = "raw/source.md") -> None:
    path.write_text(
        "\n".join(
            [
                "---",
                "id: sample-page",
                "type: concept",
                "title: Sample Page",
                "chapter_scope: [ch02]",
                "source_anchors:",
                "  - source: sample-source",
                f"    locator: {locator}",
                "confidence: directional",
                "prerequisites: []",
                "related: []",
                "learning_objectives:",
                "  - Explain the sample idea.",
                "---",
                "",
                "# Sample Page",
                "",
            ]
        ),
        encoding="utf-8",
    )


def test_required_frontmatter_keys_include_source_anchors():
    keys = required_frontmatter_keys()
    assert "id" in keys
    assert "type" in keys
    assert "source_anchors" in keys
    assert "confidence" in keys


def test_validate_wiki_tree_accepts_valid_page(tmp_path):
    repo = tmp_path
    wiki = repo / "wiki" / "udl"
    wiki.mkdir(parents=True)
    source = repo / "raw" / "source.md"
    source.parent.mkdir()
    source.write_text("source", encoding="utf-8")
    _valid_page(wiki / "sample-page.md")

    errors = validate_wiki_tree(wiki, repo_root=repo)

    assert errors == []


def test_validate_wiki_tree_reports_missing_frontmatter_key(tmp_path):
    repo = tmp_path
    wiki = repo / "wiki" / "udl"
    wiki.mkdir(parents=True)
    page = wiki / "bad.md"
    page.write_text("---\nid: bad\n---\n\n# Bad\n", encoding="utf-8")

    errors = validate_wiki_tree(wiki, repo_root=repo)

    assert any("missing frontmatter key: source_anchors" in error for error in errors)


def test_validate_wiki_tree_reports_missing_local_source_anchor(tmp_path):
    repo = tmp_path
    wiki = repo / "wiki" / "udl"
    wiki.mkdir(parents=True)
    _valid_page(wiki / "sample-page.md", locator="raw/missing.md")

    errors = validate_wiki_tree(wiki, repo_root=repo)

    assert any("missing source anchor" in error for error in errors)


def test_validate_wiki_tree_reports_missing_local_markdown_link(tmp_path):
    repo = tmp_path
    wiki = repo / "wiki" / "udl"
    wiki.mkdir(parents=True)
    source = repo / "raw" / "source.md"
    source.parent.mkdir()
    source.write_text("source", encoding="utf-8")
    page = wiki / "sample-page.md"
    _valid_page(page)
    page.write_text(page.read_text(encoding="utf-8") + "[Missing](missing.md)\n", encoding="utf-8")

    errors = validate_wiki_tree(wiki, repo_root=repo)

    assert any("broken markdown link" in error for error in errors)
