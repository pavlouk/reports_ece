# -*- coding: utf-8 -*-
import numpy as np

def img_to_vectors(img):
    
    """ 
=======
img_to_vectors
=======

Definition: img_to_vectors(image)

This function takes a sparse image and return the indices of 
its non-zero coordinates

Parameters
----------
image : 2-D array 
    Input image.


Returns
-------
xOrdinates, yOrdinates : array (int)
    Output Coordinates. 
    
    """
    elements = np.argwhere(img)
    xOrdinates, yOrdinates = np.vsplit(elements.transpose(), 2)
    return xOrdinates.ravel(), yOrdinates.ravel()