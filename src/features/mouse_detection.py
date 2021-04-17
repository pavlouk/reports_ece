import numpy as np
from skimage.util import img_as_ubyte
from skimage.segmentation import watershed
from skimage.filters import sobel
from skimage.draw import rectangle_perimeter
from skimage.io import imread

from scipy import ndimage as ndi

def mouse_detection(mouse_images, markerBack=70, markerBody=120):
    object_images = []
    for original in mouse_images:
        bordered = original[:, 100:260]
        # We create markers indicating the segmentation through histogram values
        markerImage = np.zeros_like(bordered)
        # We find markers of the background and the mouse body based on the extreme
        # parts of the histogram of gray values.  μαρκάρω == marker, πινακιδιάζω == label
        
        markerImage[img_as_ubyte(bordered) < markerBack] = 1
        markerImage[img_as_ubyte(bordered) > markerBody] = 2
        elevationMap = sobel(bordered)
        
        initialMaskTemp = watershed(elevationMap, markerImage)
        # This method segments and labels the mouse individually
        initialMask = ndi.binary_fill_holes(initialMaskTemp - 1)
        labeledMouse, _ = ndi.label(initialMask)
        mouseLocation = ndi.find_objects(labeledMouse)[0]
        ro, co = rectangle_perimeter(start=(mouseLocation[0].start, mouseLocation[1].start), 
                             end=(mouseLocation[0].stop, mouseLocation[1].stop),
                             shape=bordered.shape)
        initialMask[ro, co] = True
        mouseMask = initialMask[mouseLocation]
        mouseImage = bordered[mouseLocation]
        cleanMouse = mouseImage * mouseMask
        object_images.append(cleanMouse)
    return object_images

# image = imread('C:\\Users\\plouk\\Adiposer/data/raw/0h/Mouse1\\IR_2066.jpg')
# uuu = [image]
# new = mouse_detection(uuu)

# from IPython.display import HTML 