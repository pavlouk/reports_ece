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

def _edit_dc_image(image): 
    
    return image



def load_images_all(name='BAT'):
    """ 
=======
load_images_all
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
loaded_IR : list (np.array) -> 45 images = 9 images / mouse * 5 mice 
    Loaded image sequence. 
    
EXIF_data : list (strings) -> 45 metadata = 9 metadata / mouse * 5 mice 
    Image metadata: list of 22 strings 
        
    """
    
    loaded_IR = []
    loaded_DC = []
    EXIF_bytes = []
    EXIF_data = []
    CWD = os.getcwd()
    if name == 'WAT':        
        IRFiles = sorted(glob(CWD + '/dataset/WAT/Mouse1/IR_*.jpg'))
        [loaded_IR.append(imread(imagePath, as_gray=True)) for imagePath in IRFiles]
        [EXIF_bytes.append(Image.open(imagePath).getexif()) for imagePath in IRFiles]
        
        DCFiles = sorted(glob(CWD + '/dataset/WAT/Mouse1/DC_*.jpg'))
        [loaded_DC.append(imread(imagePath, as_gray=True)) for imagePath in DCFiles]
        
        
        IRFiles = sorted(glob(CWD + '/dataset/WAT/Mouse2/IR_*.jpg'))
        [loaded_IR.append(imread(imagePath, as_gray=True)) for imagePath in IRFiles]
        [EXIF_bytes.append(Image.open(imagePath).getexif()) for imagePath in IRFiles]
        
        DCFiles = sorted(glob(CWD + '/dataset/WAT/Mouse2/DC_*.jpg'))
        [loaded_DC.append(imread(imagePath, as_gray=True)) for imagePath in DCFiles]
        
        
        IRFiles = sorted(glob(CWD + '/dataset/WAT/Mouse3/IR_*.jpg'))
        [loaded_IR.append(imread(imagePath, as_gray=True)) for imagePath in IRFiles]
        [EXIF_bytes.append(Image.open(imagePath).getexif()) for imagePath in IRFiles]
        
        DCFiles = sorted(glob(CWD + '/dataset/WAT/Mouse3/DC_*.jpg'))
        [loaded_DC.append(imread(imagePath, as_gray=True)) for imagePath in DCFiles]
        
        
        IRFiles = sorted(glob(CWD + '/dataset/WAT/Mouse4/IR_*.jpg'))
        [loaded_IR.append(imread(imagePath, as_gray=True)) for imagePath in IRFiles]
        [EXIF_bytes.append(Image.open(imagePath).getexif()) for imagePath in IRFiles]
        
        DCFiles = sorted(glob(CWD + '/dataset/WAT/Mouse4/DC_*.jpg'))
        [loaded_DC.append(imread(imagePath, as_gray=True)) for imagePath in DCFiles]
        
        
        IRFiles = sorted(glob(CWD + '/dataset/WAT/Mouse5/IR_*.jpg'))
        [loaded_IR.append(imread(imagePath, as_gray=True)) for imagePath in IRFiles]
        [EXIF_bytes.append(Image.open(imagePath).getexif()) for imagePath in IRFiles]
        
        DCFiles = sorted(glob(CWD + '/dataset/WAT/Mouse5/DC_*.jpg'))
        [loaded_DC.append(imread(imagePath, as_gray=True)) for imagePath in DCFiles]
        
        EXIF_data = [_readable_EXIF(rawdata) for rawdata in EXIF_bytes]
        DC_loaded = [_edit_dc_image(rawDC) for rawDC in loaded_DC]
        return loaded_IR, DC_loaded, EXIF_bytes
    
    
    
    IRFiles = sorted(glob(CWD + '/dataset/BAT/Mouse1/IR_*.jpg'))
    [loaded_IR.append(imread(imagePath, as_gray=True)) for imagePath in IRFiles]
    [loaded_DC.append(imread(imagePath, as_gray=True)) for imagePath in IRFiles]
    [EXIF_bytes.append(Image.open(imagePath).getexif()) for imagePath in IRFiles]
    
    IRFiles = sorted(glob(CWD + '/dataset/BAT/Mouse2/IR_*.jpg'))
    [loaded_IR.append(imread(imagePath, as_gray=True)) for imagePath in IRFiles]
    [loaded_DC.append(imread(imagePath, as_gray=True)) for imagePath in IRFiles]
    [EXIF_bytes.append(Image.open(imagePath).getexif()) for imagePath in IRFiles]
    
    IRFiles = sorted(glob(CWD + 'dataset/BAT/Mouse3/IR_*.jpg'))
    [loaded_IR.append(imread(imagePath, as_gray=True)) for imagePath in IRFiles]
    [loaded_DC.append(imread(imagePath, as_gray=True)) for imagePath in IRFiles]
    [EXIF_bytes.append(Image.open(imagePath).getexif()) for imagePath in IRFiles]
    
    IRFiles = sorted(glob(CWD + '/dataset/BAT/Mouse4/IR_*.jpg'))
    [loaded_IR.append(imread(imagePath, as_gray=True)) for imagePath in IRFiles]
    [loaded_DC.append(imread(imagePath, as_gray=True)) for imagePath in IRFiles]
    [EXIF_bytes.append(Image.open(imagePath).getexif()) for imagePath in IRFiles]
    
    IRFiles = sorted(glob(CWD + '/dataset/BAT/Mouse5/IR_*.jpg'))
    [loaded_IR.append(imread(imagePath, as_gray=True)) for imagePath in IRFiles]
    [loaded_DC.append(imread(imagePath, as_gray=True)) for imagePath in IRFiles]
    [EXIF_bytes.append(Image.open(imagePath).getexif()) for imagePath in IRFiles]

    EXIF_data = [_readable_EXIF(rawdata) for rawdata in EXIF_bytes]
    return loaded_IR, EXIF_data
    