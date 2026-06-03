# LLM Wiki Raw Intake

This folder is the intake area for sources used by `wiki/llm-wiki/`.

## Layout

- `manifests/` - source records, licenses, retrieval notes, and trust status.
- `sources/` - committed source files only when license and size make that appropriate.
- `extracts/` - OCR, Markdown, snippets, tables, or other derived working files.
- `private/` - local-only full text or restricted assets. Ignored by git.

## Intake Checklist

1. Create a manifest in `manifests/`.
2. Record title, authors, URL or local source, license, retrieval date, and intended use.
3. Decide whether source files can be committed.
4. If extracting content, preserve source locators such as chapter, section, page, timestamp, or commit SHA.
5. Reference the manifest id from wiki page `source_anchors`.
