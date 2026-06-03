from __future__ import annotations

from dataclasses import dataclass
from hashlib import sha256
from pathlib import Path


@dataclass(frozen=True)
class UdlSource:
    source_id: str
    filename: str
    url: str
    sha256: str

    @property
    def local_path(self) -> Path:
        return Path("raw/udl/source") / self.filename


TEXTBOOK = UdlSource(
    source_id="udlbook-v5.0.3-textbook",
    filename="UnderstandingDeepLearning_02_09_26_C.pdf",
    url="https://github.com/udlbook/udlbook/releases/download/v5.0.3/UnderstandingDeepLearning_02_09_26_C.pdf",
    sha256="f8237d393163900fa8e43210e680a3f987b45ccac7750b372e156fae3df0bf32",
)

ANSWER_BOOKLET = UdlSource(
    source_id="udlbook-answer-booklet-students",
    filename="UDL_Answer_Booklet_Students.pdf",
    url="https://raw.githubusercontent.com/udlbook/udlbook/main/UDL_Answer_Booklet_Students.pdf",
    sha256="ec58fde8a42da57979808b284e52a26e0b67142817d47a657772b09144d1dcf3",
)


def file_sha256(path: Path) -> str:
    digest = sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def verify_sha256(path: Path, expected: str) -> bool:
    return file_sha256(path) == expected
