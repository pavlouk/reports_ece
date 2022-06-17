from typing import List, Tuple

import numpy as np
from scipy import ndimage as ndi
from skimage.draw import rectangle_perimeter
from skimage.filters import sobel
from skimage.segmentation import watershed
from skimage.util import img_as_ubyte

Images = List[np.ndarray]


def mouse_detection(
    mouse_images: Images, marker_back=70, marker_body=120, formatted=False
) -> Tuple[Images, Images, Images, Images, Images, Images]:
    """mouse_images: used to be (240, 320) now are (240, 160)"""
    object_images, object_masks, initial_masks, mouse_locations = [], [], [], []
    for original in mouse_images:
        bordered = original
        # We create markers indicating the segmentation through histogram values
        marker_image = np.zeros_like(bordered)
        # We find markers of the background and the mouse body based on the extreme
        # parts of the histogram of gray values.

        marker_image[img_as_ubyte(bordered) < marker_back] = 1  # type: ignore
        marker_image[img_as_ubyte(bordered) > marker_body] = 2  # type: ignore
        elevation_map = sobel(bordered)

        initial_mask_temp = watershed(elevation_map, marker_image)
        # This method segments and labels the mouse individually
        initial_mask = ndi.binary_fill_holes(initial_mask_temp - 1)
        initial_masks.append(initial_mask)
        labeled_mouse, _ = ndi.label(initial_mask)
        mouse_location = ndi.find_objects(labeled_mouse)[0]
        r_o, c_o = rectangle_perimeter(
            start=(mouse_location[0].start, mouse_location[1].start),
            end=(mouse_location[0].stop, mouse_location[1].stop),
            shape=bordered.shape,
        )
        initial_mask[r_o, c_o] = True  # type: ignore
        mouse_locations.append(mouse_location)
        mouse_mask = initial_mask[mouse_location]  # type: ignore
        mouse_image = bordered[mouse_location]
        clean_mouse = mouse_image * mouse_mask
        object_masks.append(mouse_mask)
        object_images.append(clean_mouse)

    if formatted:
        n_object_images = [
            [
                object_images[i],
                object_images[i + 1],
                object_images[i + 2],
                object_images[i + 3],
            ]
            for i in range(0, len(mouse_images), 4)
        ]
        n_object_masks = [
            [
                object_masks[i],
                object_masks[i + 1],
                object_masks[i + 2],
                object_masks[i + 3],
            ]
            for i in range(0, len(mouse_images), 4)
        ]
        n_initial_masks = [
            [
                initial_masks[i],
                initial_masks[i + 1],
                initial_masks[i + 2],
                initial_masks[i + 3],
            ]
            for i in range(0, len(mouse_images), 4)
        ]
        n_mouse_images = [
            [
                mouse_images[i],
                mouse_images[i + 1],
                mouse_images[i + 2],
                mouse_images[i + 3],
            ]
            for i in range(0, len(mouse_images), 4)
        ]
        n_mouse_locations = [
            [
                mouse_locations[i],
                mouse_locations[i + 1],
                mouse_locations[i + 2],
                mouse_locations[i + 3],
            ]
            for i in range(0, len(mouse_images), 4)
        ]

        return (
            n_object_images,
            n_object_masks,
            n_initial_masks,
            n_mouse_images,
            n_mouse_locations,
        )  # type: ignore

    return (
        object_images,
        object_masks,
        initial_masks,
        mouse_images,
        mouse_locations,
    )  # type: ignore
