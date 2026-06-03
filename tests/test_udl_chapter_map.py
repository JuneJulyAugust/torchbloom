from torchbloom.udl_chapter_map import build_chapter_map, slugify_title


def test_slugify_title_is_stable():
    assert slugify_title("Shallow Neural Networks") == "shallow-neural-networks"
    assert slugify_title("Background Mathematics") == "background-mathematics"


def test_build_chapter_map_from_outline_entries():
    outline = [
        (1, "Preface", 1),
        (1, "1 Background Mathematics", 9),
        (1, "2 Supervised Learning", 31),
        (1, "3 Shallow Neural Networks", 47),
        (1, "References", 100),
    ]

    chapters = build_chapter_map(outline, page_count=120)

    assert [chapter.number for chapter in chapters] == [1, 2, 3]
    assert chapters[0].slug == "ch01-background-mathematics"
    assert chapters[0].pdf_start == 9
    assert chapters[0].pdf_end == 30
    assert chapters[1].slug == "ch02-supervised-learning"
    assert chapters[1].pdf_start == 31
    assert chapters[1].pdf_end == 46
    assert chapters[2].slug == "ch03-shallow-neural-networks"
    assert chapters[2].pdf_start == 47
    assert chapters[2].pdf_end == 99


def test_build_chapter_map_from_unnumbered_udl_outline():
    outline = [
        (1, "Preface", 5),
        (1, "Acknowledgements", 11),
        (1, "Introduction", 15),
        (1, "Supervised learning", 31),
        (1, "Shallow neural networks", 39),
        (1, "Notation", 451),
    ]

    chapters = build_chapter_map(outline, page_count=541)

    assert [chapter.number for chapter in chapters] == [1, 2, 3]
    assert chapters[0].slug == "ch01-introduction"
    assert chapters[0].pdf_start == 15
    assert chapters[0].pdf_end == 30
    assert chapters[2].slug == "ch03-shallow-neural-networks"
    assert chapters[2].pdf_start == 39
    assert chapters[2].pdf_end == 450
