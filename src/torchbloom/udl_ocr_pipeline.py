"""Render UDL PDF pages, run DeepSeek-OCR-2, and write raw OCR artifacts."""

from __future__ import annotations

import argparse
import json
import sys
import time
from pathlib import Path

from torchbloom.udl_chapter_map import ChapterRange, load_chapter_map
from torchbloom.udl_ocr_parse import (
    build_frontmatter,
    parse_figure_title,
    parse_grounding_to_crops,
)

ERROR_MARKER = "[ERROR]"
GROUNDING_PROMPT = "<|grounding|>Convert the document to markdown."


def raw_ocr_path(output_dir: Path, page: int) -> Path:
    return Path(output_dir) / "raw_ocr" / f"page_{page:04d}.txt"


def is_page_done(output_dir: Path, page: int) -> bool:
    path = raw_ocr_path(output_dir, page)
    if not path.exists():
        return False
    head = path.read_text(encoding="utf-8")[: len(ERROR_MARKER)]
    return head != ERROR_MARKER


def _is_page_error(output_dir: Path, page: int) -> bool:
    path = raw_ocr_path(output_dir, page)
    if not path.exists():
        return False
    return path.read_text(encoding="utf-8")[: len(ERROR_MARKER)] == ERROR_MARKER


def _chapter_for_page(pdf_page: int, ranges: list[ChapterRange]) -> ChapterRange | None:
    for chapter in ranges:
        if chapter.pdf_start <= pdf_page <= chapter.pdf_end:
            return chapter
    return None


def page_md_dest(output_dir: Path, page: int, slug: str) -> Path:
    return Path(output_dir) / "pages" / slug / f"page_{page:04d}.md"


def _crop_and_save(page_image, img_w: int, img_h: int, box: list[int], out_path: Path, pad: int = 5) -> None:
    x1, y1, x2, y2 = box
    x1, x2 = sorted((x1, x2))
    y1, y2 = sorted((y1, y2))
    px1 = max(0, int(x1 / 1000.0 * img_w) - pad)
    py1 = max(0, int(y1 / 1000.0 * img_h) - pad)
    px2 = min(img_w, int(x2 / 1000.0 * img_w) + pad)
    py2 = min(img_h, int(y2 / 1000.0 * img_h) + pad)
    px2 = max(px2, px1 + 1)
    py2 = max(py2, py1 + 1)
    page_image.crop((px1, py1, px2, py2)).save(str(out_path), "PNG")


def write_page_from_raw(
    output_dir: Path,
    pdf_page: int,
    ranges: list[ChapterRange],
    page_image_path: Path,
    source_name: str,
    title_banner: str | None,
) -> Path:
    from PIL import Image

    output_dir = Path(output_dir)
    raw_text = raw_ocr_path(output_dir, pdf_page).read_text(encoding="utf-8")
    clean_md, crops, meta = parse_grounding_to_crops(raw_text, pdf_page)

    figures_dir = output_dir / "figures"
    figures_dir.mkdir(parents=True, exist_ok=True)
    figure_names: list[str] = []
    with Image.open(page_image_path) as image:
        img_w, img_h = image.size
        for fig_idx, box in crops:
            name = f"page_{pdf_page:04d}_fig_{fig_idx}.png"
            _crop_and_save(image, img_w, img_h, box, figures_dir / name)
            figure_names.append(name)

    if title_banner:
        clean_md = f"# {title_banner}\n\n{clean_md}"

    chapter_range = _chapter_for_page(pdf_page, ranges)
    chapter = f"{chapter_range.number} — {chapter_range.title}" if chapter_range else None
    slug = chapter_range.slug if chapter_range else "frontmatter"
    chapter_slug = chapter_range.slug if chapter_range else None
    title = title_banner or (meta["headings"][0] if meta["headings"] else f"Page {pdf_page}")
    frontmatter = build_frontmatter(
        source=source_name,
        page_key=pdf_page,
        pdf_page=pdf_page,
        title=title,
        chapter=chapter,
        chapter_slug=chapter_slug,
        figures=figure_names,
        headings=meta["headings"],
    )

    dest = page_md_dest(output_dir, pdf_page, slug)
    dest.parent.mkdir(parents=True, exist_ok=True)
    dest.write_text(f"{frontmatter}\n\n{clean_md}".strip() + "\n", encoding="utf-8")
    return dest


def status_report(output_dir: Path, ranges: list[ChapterRange], chapters: list[int]) -> dict:
    by_num = {chapter.number: chapter for chapter in ranges}
    per_chapter: dict[int, dict] = {}
    error_pages: list[int] = []
    total = 0
    done = 0

    for number in chapters:
        chapter = by_num[number]
        pages = range(chapter.pdf_start, chapter.pdf_end + 1)
        chapter_done = sum(1 for page in pages if is_page_done(output_dir, page))
        chapter_errors = [page for page in pages if _is_page_error(output_dir, page)]
        error_pages.extend(chapter_errors)
        chapter_total = chapter.pdf_end - chapter.pdf_start + 1
        per_chapter[number] = {"done": chapter_done, "total": chapter_total}
        total += chapter_total
        done += chapter_done

    return {
        "done": done,
        "total": total,
        "complete": done >= total,
        "per_chapter": per_chapter,
        "error_pages": error_pages,
    }


def _render_page_image(doc, pdf_page: int, dpi: int, dest: Path) -> Path:
    import fitz

    page = doc.load_page(pdf_page - 1)
    matrix = fitz.Matrix(dpi / 72.0, dpi / 72.0)
    pix = page.get_pixmap(matrix=matrix)
    dest.parent.mkdir(parents=True, exist_ok=True)
    pix.save(str(dest))
    return dest


def _ocr_page(model, processor, image_path: Path, args) -> str:
    from mlx_vlm import generate
    from mlx_vlm.prompt_utils import apply_chat_template

    prompt = apply_chat_template(processor, model.config, GROUNDING_PROMPT, num_images=1)
    result = generate(
        model,
        processor,
        prompt,
        [str(image_path)],
        max_tokens=args.max_tokens,
        temperature=0.0,
        repetition_penalty=1.2,
        repetition_context_size=20,
        verbose=False,
        min_patches=args.min_patches,
        max_patches=args.max_patches,
    )
    return result.text if hasattr(result, "text") else str(result)


def _ocr_title_strip(model, processor, image_path: Path) -> str:
    from PIL import Image
    from mlx_vlm import generate
    from mlx_vlm.prompt_utils import apply_chat_template

    strip_path = image_path.with_name(f"{image_path.stem}_titlestrip.png")
    with Image.open(image_path) as image:
        width, height = image.size
        image.crop((0, 0, width, int(height * 0.085))).save(strip_path)
    try:
        prompt = apply_chat_template(processor, model.config, "Free OCR.", num_images=1)
        result = generate(
            model,
            processor,
            prompt,
            [str(strip_path)],
            max_tokens=128,
            temperature=0.0,
            repetition_penalty=1.2,
            repetition_context_size=20,
            verbose=False,
            cropping=False,
        )
        return result.text if hasattr(result, "text") else str(result)
    finally:
        strip_path.unlink(missing_ok=True)


def _write_scaffold(output_dir: Path, source_name: str, ranges: list[ChapterRange], pages: list[int]) -> None:
    output_dir = Path(output_dir)
    (output_dir / "chapter_map.json").write_text(
        json.dumps([chapter.__dict__ for chapter in ranges], indent=2) + "\n",
        encoding="utf-8",
    )
    done = sum(1 for page in pages if is_page_done(output_dir, page))
    index = [
        "# Index - Understanding Deep Learning raw OCR layer",
        "",
        f"Source: `{source_name}`. {done}/{len(pages)} requested pages transcribed.",
        "",
        "See `chapter_map.json` for chapter ranges and `pages/<slug>/` for transcriptions.",
        "",
    ]
    (output_dir / "index.md").write_text("\n".join(index), encoding="utf-8")

    log = output_dir / "log.md"
    if not log.exists():
        log.write_text("# Log - UDL OCR\n\n", encoding="utf-8")
    span = f"{pages[0]}-{pages[-1]}" if pages else "-"
    with log.open("a", encoding="utf-8") as handle:
        handle.write(f"## [{time.strftime('%Y-%m-%d %H:%M')}] run | pages {span} | {done} done\n\n")


def _resolve_pages(ranges: list[ChapterRange], chapter_numbers: list[int]) -> list[int]:
    by_num = {chapter.number: chapter for chapter in ranges}
    pages: list[int] = []
    for number in chapter_numbers:
        if number not in by_num:
            raise ValueError(f"chapter {number} not found in chapter map")
        chapter = by_num[number]
        pages.extend(range(chapter.pdf_start, chapter.pdf_end + 1))
    return pages


def _select_pages(args, ranges: list[ChapterRange]) -> list[int]:
    if args.all:
        return _resolve_pages(ranges, sorted(chapter.number for chapter in ranges))
    if args.chapters:
        numbers = [int(value) for value in args.chapters.split(",") if value.strip()]
        return _resolve_pages(ranges, numbers)
    if args.pages:
        start_text, _, end_text = args.pages.partition("-")
        start = int(start_text)
        end = int(end_text) if end_text else start
        return list(range(start, end + 1))
    raise SystemExit("specify exactly one of --chapters, --pages, --all")


def run(args) -> int:
    output_dir = Path(args.output_dir)
    (output_dir / "raw_ocr").mkdir(parents=True, exist_ok=True)
    ranges = load_chapter_map(Path(args.pdf_path))
    pages = _select_pages(args, ranges)
    source_name = Path(args.pdf_path).name

    if args.status:
        chapters = sorted(
            {
                chapter.number
                for page in pages
                if (chapter := _chapter_for_page(page, ranges)) is not None
            }
        )
        report = status_report(output_dir, ranges, chapters)
        print(
            f"{report['done']}/{report['total']} pages done | "
            f"complete={report['complete']} | error_pages={report['error_pages']}"
        )
        for number, chapter_status in report["per_chapter"].items():
            print(f"  ch{number:02d}: {chapter_status['done']}/{chapter_status['total']}")
        return 0

    import fitz

    model = processor = None
    if not args.reparse:
        from mlx_vlm import load

        print(f"Loading model {args.model} ...")
        model, processor = load(args.model, trust_remote_code=True)

    with fitz.open(args.pdf_path) as doc:
        images_dir = output_dir / "images"
        for pdf_page in pages:
            if args.resume and not args.force and not args.reparse and is_page_done(output_dir, pdf_page):
                print(f"page {pdf_page}: skip (done)")
                continue

            page_png = images_dir / f"page_{pdf_page:04d}.png"
            try:
                _render_page_image(doc, pdf_page, args.dpi, page_png)

                if not args.reparse:
                    raw_text = _ocr_page(model, processor, page_png, args)
                    raw_ocr_path(output_dir, pdf_page).write_text(raw_text, encoding="utf-8")

                clean_preview, _, _ = parse_grounding_to_crops(
                    raw_ocr_path(output_dir, pdf_page).read_text(encoding="utf-8"),
                    pdf_page,
                )
                banner = None
                if not args.reparse:
                    banner = parse_figure_title(_ocr_title_strip(model, processor, page_png), clean_preview)
                write_page_from_raw(
                    output_dir=output_dir,
                    pdf_page=pdf_page,
                    ranges=ranges,
                    page_image_path=page_png,
                    source_name=source_name,
                    title_banner=banner,
                )
                print(f"page {pdf_page}: done")
            except Exception as exc:
                raw_ocr_path(output_dir, pdf_page).write_text(
                    f"{ERROR_MARKER} page {pdf_page}: {exc}",
                    encoding="utf-8",
                )
                print(f"page {pdf_page}: ERROR {exc}", file=sys.stderr)
            finally:
                if not args.keep_page_images:
                    page_png.unlink(missing_ok=True)
                if model is not None:
                    import mlx.core as mx

                    clear = getattr(mx, "clear_cache", None) or mx.metal.clear_cache
                    clear()

    _write_scaffold(output_dir, source_name, ranges, pages)
    return 0


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="OCR Understanding Deep Learning PDF to per-page Markdown.")
    parser.add_argument("--pdf-path", default="raw/udl/source/UnderstandingDeepLearning_02_09_26_C.pdf")
    parser.add_argument("--output-dir", default="raw/udl/textbook")
    selectors = parser.add_mutually_exclusive_group()
    selectors.add_argument("--chapters", help="comma-separated chapter numbers, e.g. 1,2,3")
    selectors.add_argument("--pages", help="PDF page range, e.g. 15-30")
    selectors.add_argument("--all", action="store_true", help="entire book")
    parser.add_argument("--model", default="mlx-community/DeepSeek-OCR-2-bf16")
    parser.add_argument("--dpi", type=int, default=300)
    parser.add_argument("--max-tokens", type=int, default=8192)
    parser.add_argument("--min-patches", type=int, default=2)
    parser.add_argument("--max-patches", type=int, default=12)
    parser.add_argument("--keep-page-images", action="store_true")
    parser.add_argument("--resume", action="store_true", default=True)
    parser.add_argument("--force", action="store_true")
    parser.add_argument("--reparse", action="store_true", help="rebuild md/figures from saved raw OCR; no model")
    parser.add_argument("--status", action="store_true", help="print progress and exit")
    args = parser.parse_args(argv)
    return run(args)


if __name__ == "__main__":
    raise SystemExit(main())
