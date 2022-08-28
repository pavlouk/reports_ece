from pathlib import Path

from .data import FLIRImage as FLIRImage

HERE = Path(__file__)
SRC_DIR = HERE.parent.parent
PROJECT_DIR = SRC_DIR.parent
RAW_DIR = PROJECT_DIR / "data" / "raw"
INTERIM_DIR = PROJECT_DIR / "data" / "interim"
PROCESSED_DIR = PROJECT_DIR / "data" / "processed"


class Detection:
    def __init__(self) -> None:
        pass


class DetectionCollection:
    def __init__(self) -> None:
        pass
