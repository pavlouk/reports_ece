from skimage.feature import downscale_local_mean
from skimage.filter import unsharp_mask

def downscale(imagesBefore):
    """
    downscale + unsharp mask when using a graph-based method due to memory complexity
    εδώ προφανώς θα πέσουμε στα (120, 77)
    preprocessing // αλλαγές: αποκλιμάκωση εικόνας και αφαίρεση θορύβου
    """
    mouseImages = [downscale_local_mean(mouseImage, (2, 2)) for mouseImage in imagesBefore]
    # or denoise_wavelet
    mouseImages = [unsharp_mask(mouseImage) for mouseImage in mouseImages]
    
    return mouseImages
