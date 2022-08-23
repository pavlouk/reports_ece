# -*- coding: utf-8 -*-
from typing import Tuple

import numpy as np


def img_to_vectors(img: np.ndarray) -> Tuple[np.ndarray, np.ndarray]:
    """return the coordinates of the non-zero pixels"""
    elements = np.argwhere(img)
    x_ordinates, y_ordinates = np.vsplit(elements.transpose(), 2)
    return x_ordinates.ravel(), y_ordinates.ravel()
