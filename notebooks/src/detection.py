from pathlib import Path

from .data import FLIRImage as FLIRImage

HERE = Path(__file__)
SRC_DIR = HERE
PROJECT_DIR = SRC_DIR.parent.parent.parent
RAW_DIR = PROJECT_DIR / "data" / "raw"
INTERIM_DIR = PROJECT_DIR / "data" / "interim"
PROCESSED_DIR = PROJECT_DIR / "data" / "processed"


class Detection:
    def __init__(self) -> None:
        self.name = "Detection"
        self.HERE = HERE


class DetectionCollection:
    def __init__(self) -> None:
        self.name = "DetectionCollection"
        self.RAW_DIR = RAW_DIR
