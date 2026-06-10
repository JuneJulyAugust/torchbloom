"""Run PPStructureV3 over UDL page images and save fusion-ready evidence."""

from __future__ import annotations

import argparse
import json
import os
import shutil
import sys
from pathlib import Path
from typing import Any

from torchbloom.udl_fusion_pilot import (
    DEFAULT_PADDLE_PAGES_DIR,
    DEFAULT_RAW_ROOT,
    Chapter,
    PageSpec,
    load_chapters,
    select_pages,
)

ERROR_MARKER = "[ERROR]"
LAYOUT_CROP_LABELS = {"image", "chart", "table", "formula"}
LAYOUT_FINAL_VISUAL_LABELS = {"image", "chart", "table"}


def page_output_dir(output_dir: Path, spec: PageSpec) -> Path:
    return Path(output_dir) / "pages" / spec.source_key


def page_markdown_path(output_dir: Path, spec: PageSpec) -> Path:
    return page_output_dir(output_dir, spec) / f"{spec.source_key}.combined.md"


def page_error_path(output_dir: Path, spec: PageSpec) -> Path:
    return page_output_dir(output_dir, spec) / f"{spec.source_key}.error.txt"


def is_page_done(output_dir: Path, spec: PageSpec) -> bool:
    return page_markdown_path(output_dir, spec).exists() and not page_error_path(output_dir, spec).exists()


def _chapter_for_page(chapters: list[Chapter], page: int) -> Chapter:
    for chapter in chapters:
        if chapter.pdf_start <= page <= chapter.pdf_end:
            return chapter
    raise ValueError(f"PDF page {page} is not covered by chapter_map.json")


def _parse_page_range(page_text: str) -> tuple[int, int]:
    start_text, _, end_text = page_text.partition("-")
    start = int(start_text)
    end = int(end_text) if end_text else start
    if end < start:
        raise ValueError(f"invalid page range: {page_text}")
    return start, end


def resolve_specs(args: argparse.Namespace, chapters: list[Chapter]) -> list[PageSpec]:
    if args.all:
        chapter_text = ",".join(str(chapter.number) for chapter in chapters)
        return select_pages(chapters, chapter_text, args.book_page_offset)
    if args.chapters:
        return select_pages(chapters, args.chapters, args.book_page_offset)
    if args.pages:
        start, end = _parse_page_range(args.pages)
        return [
            PageSpec(
                chapter=_chapter_for_page(chapters, page),
                page=page,
                book_page_offset=args.book_page_offset,
            )
            for page in range(start, end + 1)
        ]
    raise SystemExit("specify exactly one of --chapters, --pages, --all")


def save_page_result(pipeline: Any, result: list[Any], output_dir: Path, spec: PageSpec) -> Path:
    page_dir = page_output_dir(output_dir, spec)
    json_dir = page_dir / "json"
    page_dir.mkdir(parents=True, exist_ok=True)
    json_dir.mkdir(parents=True, exist_ok=True)

    markdown_pages: list[str] = []
    for item in result:
        save_json = getattr(item, "save_to_json", None)
        if callable(save_json):
            save_json(save_path=str(json_dir))

        save_markdown = getattr(item, "save_to_markdown", None)
        if callable(save_markdown):
            save_markdown(save_path=str(page_dir))

        markdown = getattr(item, "markdown", None)
        if markdown:
            markdown_pages.append(str(markdown))

    if hasattr(pipeline, "concatenate_markdown_pages"):
        combined = pipeline.concatenate_markdown_pages(markdown_pages)
    else:
        combined = "\n\n".join(markdown_pages)

    dest = page_markdown_path(output_dir, spec)
    dest.write_text(combined.strip() + "\n", encoding="utf-8")
    page_error_path(output_dir, spec).unlink(missing_ok=True)
    return dest


def _box_to_ints(coordinate: list[Any]) -> list[int]:
    x1, y1, x2, y2 = [round(float(value)) for value in coordinate]
    left, right = sorted((x1, x2))
    top, bottom = sorted((y1, y2))
    return [left, top, right, bottom]


def _scale_box_to_layout(box: list[int], image_size: tuple[int, int], layout_width: int) -> list[int]:
    scale = layout_width / image_size[0]
    return [round(value * scale) for value in box]


def _clip_box(box: list[int], image_size: tuple[int, int]) -> tuple[int, int, int, int]:
    width, height = image_size
    left, top, right, bottom = box
    left = max(0, min(left, width - 1))
    top = max(0, min(top, height - 1))
    right = max(left + 1, min(right, width))
    bottom = max(top + 1, min(bottom, height))
    return left, top, right, bottom


def _union_bbox(boxes: list[list[int]]) -> list[int]:
    return [
        min(box[0] for box in boxes),
        min(box[1] for box in boxes),
        max(box[2] for box in boxes),
        max(box[3] for box in boxes),
    ]


def _box_center_y(box: list[int]) -> float:
    return (box[1] + box[3]) / 2


def _is_caption_anchor(entry: dict[str, Any]) -> bool:
    if entry["label"] != "figure_title":
        return False
    left, top, right, bottom = entry["layout_bbox"]
    return right - left >= 80 and bottom - top >= 25


def _visual_groups(entries: list[dict[str, Any]]) -> tuple[list[dict[str, Any]], set[int]]:
    visuals = [entry for entry in entries if entry["label"] in LAYOUT_FINAL_VISUAL_LABELS]
    anchors = sorted((entry for entry in entries if _is_caption_anchor(entry)), key=lambda entry: entry["layout_bbox"][1])
    groups: list[dict[str, Any]] = []
    assigned: set[int] = set()
    previous_anchor_bottom = 0

    for anchor in anchors:
        anchor_top = anchor["layout_bbox"][1]
        group_entries = [
            entry
            for entry in visuals
            if entry["index"] not in assigned
            and previous_anchor_bottom <= _box_center_y(entry["layout_bbox"]) < anchor_top
        ]
        if group_entries:
            for entry in group_entries:
                assigned.add(entry["index"])
            groups.append(
                {
                    "label": "image",
                    "source_box_indexes": [entry["index"] for entry in group_entries],
                    "pixel_bbox": _union_bbox([entry["pixel_bbox"] for entry in group_entries]),
                    "layout_bbox": _union_bbox([entry["layout_bbox"] for entry in group_entries]),
                    "anchor_index": anchor["index"],
                }
            )
        previous_anchor_bottom = anchor["layout_bbox"][3]

    return groups, assigned


def save_layout_result(
    result: list[dict[str, Any]],
    output_dir: Path,
    spec: PageSpec,
    image_path: Path,
    layout_width: int = 1000,
) -> Path:
    from PIL import Image

    page_dir = page_output_dir(output_dir, spec)
    json_dir = page_dir / "json"
    imgs_dir = page_dir / "imgs"
    if json_dir.exists():
        shutil.rmtree(json_dir)
    if imgs_dir.exists():
        shutil.rmtree(imgs_dir)
    json_dir.mkdir(parents=True, exist_ok=True)
    imgs_dir.mkdir(parents=True, exist_ok=True)

    boxes = result[0].get("boxes", []) if result else []
    normalized: list[dict[str, Any]] = []
    lines = [f"# Paddle LayoutDetection {spec.source_key}", "", "## Layout boxes", ""]

    with Image.open(image_path) as image:
        for index, box in enumerate(boxes, start=1):
            label = str(box["label"])
            pixel_bbox = _box_to_ints(box["coordinate"])
            layout_bbox = _scale_box_to_layout(pixel_bbox, image.size, layout_width)
            score = float(box.get("score", 0.0))
            entry = {
                "index": index,
                "label": label,
                "score": score,
                "pixel_bbox": pixel_bbox,
                "layout_bbox": layout_bbox,
            }
            normalized.append(entry)
            lines.append(f"{index}. {label} score={score:.3f} bbox={layout_bbox}")

        visual_groups, grouped_indexes = _visual_groups(normalized)
        for group in visual_groups:
            crop_name = f"img_in_image_box_{'_'.join(str(value) for value in group['layout_bbox'])}.jpg"
            crop = image.crop(_clip_box(group["pixel_bbox"], image.size))
            crop.save(imgs_dir / crop_name, quality=95, subsampling=0, optimize=True)
            group["crop_path"] = f"imgs/{crop_name}"

        for entry in normalized:
            label = entry["label"]
            if label in LAYOUT_FINAL_VISUAL_LABELS and entry["index"] in grouped_indexes:
                continue
            if label in LAYOUT_CROP_LABELS:
                crop_name = f"img_in_{label}_box_{'_'.join(str(value) for value in entry['layout_bbox'])}.jpg"
                crop = image.crop(_clip_box(entry["pixel_bbox"], image.size))
                crop.save(imgs_dir / crop_name, quality=95, subsampling=0, optimize=True)
                entry["crop_path"] = f"imgs/{crop_name}"

    (json_dir / f"{spec.source_key}.layout.json").write_text(
        json.dumps({"page": spec.source_key, "boxes": normalized, "visual_groups": visual_groups}, indent=2) + "\n",
        encoding="utf-8",
    )
    dest = page_markdown_path(output_dir, spec)
    dest.write_text("\n".join(lines).strip() + "\n", encoding="utf-8")
    page_error_path(output_dir, spec).unlink(missing_ok=True)
    return dest


def pipeline_kwargs(args: argparse.Namespace) -> dict[str, Any]:
    return {
        "lang": args.lang,
        "use_doc_orientation_classify": False,
        "use_doc_unwarping": False,
        "use_textline_orientation": False,
        "use_table_recognition": args.use_table_recognition,
        "use_formula_recognition": args.use_formula_recognition,
        "use_chart_recognition": args.use_chart_recognition,
        "use_region_detection": args.use_region_detection,
        "device": args.device,
        "engine": args.engine,
    }


def build_pipeline(args: argparse.Namespace) -> Any:
    if args.paddlex_cache:
        cache_path = Path(args.paddlex_cache)
        cache_path.mkdir(parents=True, exist_ok=True)
        os.environ["PADDLE_PDX_CACHE_HOME"] = str(cache_path)

    from paddleocr import PPStructureV3

    return PPStructureV3(**pipeline_kwargs(args))


def build_layout_detector(args: argparse.Namespace) -> Any:
    if args.paddlex_cache:
        cache_path = Path(args.paddlex_cache)
        cache_path.mkdir(parents=True, exist_ok=True)
        os.environ["PADDLE_PDX_CACHE_HOME"] = str(cache_path)

    from paddleocr import LayoutDetection

    return LayoutDetection(device=args.device, engine=args.engine)


def status_report(output_dir: Path, specs: list[PageSpec]) -> dict[str, Any]:
    per_chapter: dict[int, dict[str, int]] = {}
    error_pages: list[int] = []
    done = 0
    for spec in specs:
        chapter_status = per_chapter.setdefault(spec.chapter.number, {"done": 0, "total": 0})
        chapter_status["total"] += 1
        if is_page_done(output_dir, spec):
            done += 1
            chapter_status["done"] += 1
        if page_error_path(output_dir, spec).exists():
            error_pages.append(spec.pdf_page)
    return {
        "done": done,
        "total": len(specs),
        "complete": done >= len(specs),
        "per_chapter": per_chapter,
        "error_pages": error_pages,
    }


def print_status(report: dict[str, Any]) -> None:
    print(
        f"{report['done']}/{report['total']} pages done | "
        f"complete={report['complete']} | error_pages={report['error_pages']}"
    )
    for number, chapter_status in sorted(report["per_chapter"].items()):
        print(f"  ch{number:02d}: {chapter_status['done']}/{chapter_status['total']}")


def run(args: argparse.Namespace) -> int:
    raw_root = Path(args.raw_root)
    output_dir = Path(args.output_dir)
    image_root = Path(args.image_root)
    chapters = load_chapters(raw_root / "chapter_map.json")
    specs = resolve_specs(args, chapters)

    if args.status:
        print_status(status_report(output_dir, specs))
        return 0

    predictor = build_pipeline(args) if args.backend == "ppstructurev3" else build_layout_detector(args)
    errors = 0
    for spec in specs:
        if args.resume and not args.force and is_page_done(output_dir, spec):
            print(f"{spec.source_key}: skip (done)")
            continue

        image_path = image_root / f"{spec.source_key}.png"
        try:
            if not image_path.exists():
                raise FileNotFoundError(image_path)
            result = predictor.predict(str(image_path))
            if args.backend == "ppstructurev3":
                save_page_result(predictor, result, output_dir, spec)
            else:
                save_layout_result(result, output_dir, spec, image_path, layout_width=args.layout_width)
            print(f"{spec.source_key}: done")
        except Exception as exc:  # pragma: no cover - exercised by real OCR failures
            errors += 1
            err_path = page_error_path(output_dir, spec)
            err_path.parent.mkdir(parents=True, exist_ok=True)
            err_path.write_text(f"{ERROR_MARKER} {spec.source_key}: {exc}\n", encoding="utf-8")
            print(f"{spec.source_key}: ERROR {exc}", file=sys.stderr)

    print_status(status_report(output_dir, specs))
    return 1 if errors else 0


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Run PPStructureV3 for UDL page images.")
    parser.add_argument("--raw-root", default=str(DEFAULT_RAW_ROOT))
    parser.add_argument("--image-root", default=str(DEFAULT_RAW_ROOT / "images"))
    parser.add_argument("--output-dir", default=str(DEFAULT_PADDLE_PAGES_DIR.parent))
    selectors = parser.add_mutually_exclusive_group()
    selectors.add_argument("--chapters", help="comma-separated chapter numbers, e.g. 4,5,6")
    selectors.add_argument("--pages", help="PDF page range, e.g. 55-69")
    selectors.add_argument("--all", action="store_true", help="all mapped textbook chapters")
    parser.add_argument("--book-page-offset", type=int, default=14)
    parser.add_argument("--paddlex-cache", default="output/.paddlex-cache")
    parser.add_argument("--backend", choices=["layout-detection", "ppstructurev3"], default="layout-detection")
    parser.add_argument("--layout-width", type=int, default=1000)
    parser.add_argument("--lang", default="en")
    parser.add_argument("--device", default="cpu")
    parser.add_argument("--engine", default="paddle")
    parser.add_argument("--use-table-recognition", action="store_true")
    parser.add_argument("--use-formula-recognition", action="store_true")
    parser.add_argument("--use-chart-recognition", action="store_true")
    parser.add_argument("--use-region-detection", action="store_true")
    parser.add_argument("--resume", action="store_true", default=True)
    parser.add_argument("--force", action="store_true")
    parser.add_argument("--status", action="store_true")
    args = parser.parse_args(argv)
    return run(args)


if __name__ == "__main__":
    raise SystemExit(main())
