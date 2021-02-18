# -*- coding: utf-8 -*-
"""
Created on Wed Feb 17 14:22:00 2021

@author: plouk
"""
from glob import glob 
from skimage.io import imread
from PIL import Image
from PIL.ExifTags import TAGS
import os

def _readable_EXIF(exifdata):
    exifList = []
    try:
        # iterating over all EXIF data fields
        for tag_id in exifdata:
            # get the tag name, instead of human unreadable tag id
            tag = TAGS.get(tag_id, tag_id)
            data = exifdata.get(tag_id)
            # decode bytes 
            if isinstance(data, bytes):
                data = data.decode()
            exifList.append(f"{tag:25}: {data}")
    except UnicodeDecodeError:
        return exifList
    return exifList


def load_images_all(name='BAT'):
    """ 
=======
load_images
=======

Definition: load_images_all(name='BAT')

Image loader from the dataset directory 

Obtain all FLIR image metadata (bytes) and convert them to strings 

Parameters
----------
name : string {'WAT' or 'BAT'} (default 'BAT')
    Obtain appropriate data.

Returns
-------
loaded_images : list (np.array) -> 45 images = 9 images / mouse * 5 mice 
    Loaded image sequence. 
    
EXIF_data : list (strings) -> 45 metadata = 9 metadata / mouse * 5 mice 
    Image metadata     
        
    """
    
    loaded_images = []
    EXIF_bytes = []
    EXIF_data = []
    CWD = os.getcwd()
    if name == 'WAT':        
        imageFiles = sorted(glob(CWD + '/dataset/WAT/Mouse_1/IR_*.jpg'))
        [loaded_images.append(imread(imagePath, as_gray=True)) for imagePath in imageFiles]
        [EXIF_bytes.append(Image.open(imagePath).getexif()) for imagePath in imageFiles]
        
        imageFiles = sorted(glob(CWD + '/dataset/WAT/Mouse_2/IR_*.jpg'))
        [loaded_images.append(imread(imagePath, as_gray=True)) for imagePath in imageFiles]
        [EXIF_bytes.append(Image.open(imagePath).getexif()) for imagePath in imageFiles]
        
        imageFiles = sorted(glob(CWD + '/dataset/WAT/Mouse_3/IR_*.jpg'))
        [loaded_images.append(imread(imagePath, as_gray=True)) for imagePath in imageFiles]
        [EXIF_bytes.append(Image.open(imagePath).getexif()) for imagePath in imageFiles]
        
        imageFiles = sorted(glob(CWD + '/dataset/WAT/Mouse_3/IR_*.jpg'))
        [loaded_images.append(imread(imagePath, as_gray=True)) for imagePath in imageFiles]
        [EXIF_bytes.append(Image.open(imagePath).getexif()) for imagePath in imageFiles]
        
        imageFiles = sorted(glob(CWD + '/dataset/WAT/Mouse_5/IR_*.jpg'))
        [loaded_images.append(imread(imagePath, as_gray=True)) for imagePath in imageFiles]
        [EXIF_bytes.append(Image.open(imagePath).getexif()) for imagePath in imageFiles]
        
        EXIF_data = [_readable_EXIF(rawdata) for rawdata in EXIF_bytes]
        return loaded_images, EXIF_bytes
    imageFiles = sorted(glob(CWD + '/dataset/BAT/Mouse_1/IR_*.jpg'))
    [loaded_images.append(imread(imagePath, as_gray=True)) for imagePath in imageFiles]
    [EXIF_bytes.append(Image.open(imagePath).getexif()) for imagePath in imageFiles]
    
    imageFiles = sorted(glob(CWD + '/dataset/BAT/Mouse_2/IR_*.jpg'))
    [loaded_images.append(imread(imagePath, as_gray=True)) for imagePath in imageFiles]
    [EXIF_bytes.append(Image.open(imagePath).getexif()) for imagePath in imageFiles]
    
    imageFiles = sorted(glob(CWD + 'dataset/BAT/Mouse_3/IR_*.jpg'))
    [loaded_images.append(imread(imagePath, as_gray=True)) for imagePath in imageFiles]
    [EXIF_bytes.append(Image.open(imagePath).getexif()) for imagePath in imageFiles]
    
    imageFiles = sorted(glob(CWD + '/dataset/BAT/Mouse_4/IR_*.jpg'))
    [loaded_images.append(imread(imagePath, as_gray=True)) for imagePath in imageFiles]
    [EXIF_bytes.append(Image.open(imagePath).getexif()) for imagePath in imageFiles]
    
    imageFiles = sorted(glob(CWD + '/dataset/BAT/Mouse_5/IR_*.jpg'))
    [loaded_images.append(imread(imagePath, as_gray=True)) for imagePath in imageFiles]
    [EXIF_bytes.append(Image.open(imagePath).getexif()) for imagePath in imageFiles]

    EXIF_data = [_readable_EXIF(rawdata) for rawdata in EXIF_bytes]
    return loaded_images, EXIF_data
    