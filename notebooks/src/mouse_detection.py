import math
import os
from pathlib import Path
from typing import List, Tuple

import numpy as np
from PIL.Image import fromarray
from PIL.Image import open as pil_open
from scipy import ndimage as ndi
from skimage.draw import rectangle_perimeter
from skimage.filters import sobel
from skimage.segmentation import watershed
from skimage.util import img_as_ubyte

from data import FLIRImage as FLIRImage

HERE = Path(__file__)  # ~/Adiposer/src/data/data_utils.py
SRC_DIR = HERE.parent.parent
PROJECT_DIR = SRC_DIR.parent
RAW_DIR = PROJECT_DIR / "data" / "raw"
INTERIM_DIR = PROJECT_DIR / "data" / "interim"
PROCESSED_DIR = PROJECT_DIR / "data" / "processed"


class Detection:
    def __init__(self) -> None:
        self.object_image = np.ndarray(shape=(320, 240))
        self.object_mask = np.ndarray(shape=(320, 240))
        self.initial_mask = np.ndarray(shape=(320, 240))
        self.marker_back = 70
        self.marker_body = 120

    def extract_region(self, flir_image: FLIRImage) -> None:
        """mouse_images: used to be (240, 320) now are (240, 160)"""
        bordered = flir_image.ir_image
        # We create markers indicating the segmentation through histogram values
        marker_image = np.zeros_like(bordered)
        # Markers image for background and  mouse body
        # based on the extreme parts of the histogram.
        marker_image[img_as_ubyte(bordered) < marker_back] = 1  # type: ignore
        marker_image[img_as_ubyte(bordered) > marker_body] = 2  # type: ignore

        elevation_map = sobel(bordered)
        initial_mask_temp = watershed(elevation_map, marker_image)
        # This method segments and labels the mouse individually
        self.initial_mask = ndi.binary_fill_holes(initial_mask_temp - 1)
        labeled_mouse, _ = ndi.label(self.initial_mask)
        self.mouse_location = ndi.find_objects(labeled_mouse)[0]
        r_o, c_o = rectangle_perimeter(
            start=(self.mouse_location[0].start, self.mouse_location[1].start),
            end=(self.mouse_location[0].stop, self.mouse_location[1].stop),
            shape=bordered.shape,
        )
        self.initial_mask[r_o, c_o] = True  # type: ignore
        self.mouse_mask = initial_mask[mouse_location]  # type: ignore
        mouse_image = bordered[self.mouse_location]
        self.object_image = mouse_image * self.mouse_mask

    def bounding_box(self, image, ratios=(0.35, 0.65, 0.70, 0.78)):
        xmin = int(ratios[0] * image.shape[1])
        xmax = int(ratios[1] * image.shape[1])
        ymin = int(ratios[2] * image.shape[0])
        ymax = int(ratios[3] * image.shape[0])
        return xmin, xmax, ymin, ymax

    def mask_orientation(self, props):
        y0, x0 = props.centroid
        orientation = props.orientation
        x1 = x0 + math.cos(orientation) * 0.5 * props.minor_axis_length
        y1 = y0 - math.sin(orientation) * 0.5 * props.minor_axis_length
        x2 = x0 - math.sin(orientation) * 0.5 * props.major_axis_length
        y2 = y0 - math.cos(orientation) * 0.5 * props.major_axis_length
        minr, minc, maxr, maxc = props.bbox
        bx = (minc, maxc, maxc, minc, minc)
        by = (minr, minr, maxr, maxr, minr)
        return x0, x1, x2, y0, y1, y2, bx, by

    def save_data_processed(
        self, object_images, object_masks, initial_masks, marker_back, marker_body
    ) -> None:
        """save on ~/data/processed"""
        batch_dir = os.path.abspath(
            PROCESSED_DIR / f"version{marker_back}_{marker_body}"
        )

        os.mkdir(batch_dir)
        # Convert to losless PIL Image and save to ~/data/processed
        for i, file in enumerate(object_images):
            fromarray(file).save(f"{batch_dir}/{i}_obj_image.tif")
        for i, file in enumerate(object_masks):
            fromarray(file).save(f"{batch_dir}/{i}_obj_mask.tif")
        for i, file in enumerate(initial_masks):
            fromarray(file).save(f"{batch_dir}/{i}_initial_mask.tif")

    def load_data_processed(self, marker_back: int, marker_body: int) -> None:
        """load images from ~/data/processed"""
        batch_id = f"version{marker_back}_{marker_body}"
        batch_dir = os.path.abspath(PROCESSED_DIR / batch_id)
        if os.path.exists(batch_dir) or os.listdir(batch_dir) == []:
            # Read back from disk and convert to Numpy format {id}_obj_image.tif
            for i in sorted(os.listdir(batch_dir)):
                if i.endswith("obj_image.tif"):
                    self.object_image = np.array(pil_open(f"{batch_dir}/{i}"))
                if i.endswith("obj_mask.tif"):
                    self.object_mask = np.array(pil_open(f"{batch_dir}/{i}"))
                if i.endswith("initial_mask.tif"):
                    self.initial_mask = np.array(pil_open(f"{batch_dir}/{i}"))
