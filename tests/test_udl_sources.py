from pathlib import Path

from torchbloom.udl_sources import (
    ANSWER_BOOKLET,
    TEXTBOOK,
    verify_sha256,
)


def test_udl_source_metadata_is_pinned():
    assert TEXTBOOK.filename == "UnderstandingDeepLearning_02_09_26_C.pdf"
    assert TEXTBOOK.sha256 == "f8237d393163900fa8e43210e680a3f987b45ccac7750b372e156fae3df0bf32"
    assert ANSWER_BOOKLET.filename == "UDL_Answer_Booklet_Students.pdf"
    assert ANSWER_BOOKLET.sha256 == "ec58fde8a42da57979808b284e52a26e0b67142817d47a657772b09144d1dcf3"


def test_verify_sha256_rejects_mismatch(tmp_path: Path):
    sample = tmp_path / "sample.txt"
    sample.write_text("TorchBloom", encoding="utf-8")

    assert verify_sha256(sample, "7daa00e2b5305f2e8a8052e40944b1a885c6baec87e08dcad1d85cca86b67711")
    assert not verify_sha256(sample, "0" * 64)
