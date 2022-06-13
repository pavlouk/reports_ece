from typing import List

import numpy as np
from skimage.feature import downscale_local_mean
from skimage.filter import unsharp_mask


def downscale(images_before: List[np.ndarray]) -> List[np.ndarray]:
    """
    downscale + unsharp mask when using a graph-based method due to memory complexity
    εδώ προφανώς θα πέσουμε στα (120, 77)
    preprocessing // αλλαγές: αποκλιμάκωση εικόνας και αφαίρεση θορύβου
    """
    mouse_images = [
        downscale_local_mean(mouse_image, (2, 2)) for mouse_image in images_before
    ]
    # or denoise_wavelet
    mouse_images = [unsharp_mask(mouse_image) for mouse_image in mouse_images]
    return mouse_images
