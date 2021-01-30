# -*- coding: utf-8 -*-
from glob import glob 
from skimage.io import imread
from PIL import Image
def load_images(name='BAT'):
    """ 
=======
load_images
=======

Definition: load_images(name='BAT')

Image loader from the dataset directory 

Obtain all FLIR image metadata

Parameters
----------
name : string {'WAT' or 'BAT'} (default 'BAT')
    Obtain appropriate data.

Returns
-------
loaded_images : list (np.array)
    Loaded image sequence. 
    
EXIF_data : list (bytes)
    image metadata     
        
    """
    
    loaded_images = []
    EXIF_data = []
    
    if name == 'WAT':        
        imageFiles = sorted(glob('C:/Users/plouk/Adiposer/dataset/WAT/IR_*.jpg'))
        [loaded_images.append(imread(imagePath, as_gray=True)) for imagePath in imageFiles]
        [EXIF_data.append(Image.open(imagePath).getexif()) for imagePath in imageFiles]
        
        return loaded_images, EXIF_data
    imageFiles = sorted(glob('C:/Users/plouk/Adiposer/dataset/BAT/IR_*.jpg'))
    [loaded_images.append(imread(imagePath, as_gray=True)) for imagePath in imageFiles]
    [EXIF_data.append(Image.open(imagePath).getexif()) for imagePath in imageFiles]

    return loaded_images, EXIF_data
    
