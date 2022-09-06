import math
from pathlib import Path
from typing import List, Tuple

import numpy as np

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

    @staticmethod
    def region_growing(an_image, a_seed_set: List[Tuple], an_in_value, tolerance=5):
        visited_matrix = np.full(shape=(240, 160), fill_value=False, dtype=bool)
        point_list = a_seed_set.copy()
        logger_list = []
        while len(point_list) > 0:
            this_point = point_list.pop()
            x, y = this_point[0], this_point[1]
            pixel_value = an_image[x, y]
            visited_matrix[x, y] = an_in_value
            logger_list.append(len(point_list))
            for j in range(y - 1, y + 2):
                if 0 <= j and j < an_image.shape[1]:
                    for i in range(x - 1, x + 2):
                        if 0 <= i and i < an_image.shape[0]:
                            neighbor_value = an_image[i, j]
                            neighbor_visited = visited_matrix[i, j]
                            if not neighbor_visited and math.fabs(
                                neighbor_value - pixel_value
                            ) <= (tolerance / 100.0 * 255):
                                point_list.append((i, j))
        return visited_matrix, logger_list


class DetectionCollection:
    def __init__(self) -> None:
        self.name = "DetectionCollection"
