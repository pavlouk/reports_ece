import os
from pathlib import Path
import pandas as pd
import numpy as np
from skimage.io import imread
from PIL import Image
import shutil
import yaml


def IR_fixer(fpath, as_gray=True):
    # fpath: το path της jpeg εικόνας ΙR
    image = imread(fpath, as_gray=as_gray)
    return image[:, 100:260]

def DC_fixer(fpath):
    # fname: το path της jpeg εικόνας DC
    image = imread(fpath, as_gray=True)
    return image.shape

def CSV_fixer(fpath):
    # fpath: δέχεται το path του csv με τις θερμοκρασίες
    # με sep = 'κενό,' τότε δίστηλο frame, με sep = 'κενό' τότε τετράστηλο frame
    dataF = pd.read_csv(filepath_or_buffer=fpath, sep=' ,', engine='python')
    columnNames = dataF.columns
    # μόνο η πρώτη στήλη με το Frame 1 έχει τις θερμοκρασίες
    # dataColumn type: pandas Series
    # ας δούμε το πρώτο που έχει τη λέξη Frame 1 στην αρχή
    dataColumn = dataF[columnNames[0]]
    firstLine = dataColumn[0]          # string
    # 320 ειναι τα κόμματα κάτι που ισχύει και για τα υπόλοιπα
    # εδώ υπάρχει η λέξη 'Frame 1,' την διώχνουμε
    rawData = np.fromstring(firstLine[8:], dtype=float, sep=',')
    # τα επόμενα ξεκινάνε με κόμμα, οπότε για τα επόμενα 239 θα κάνουμε το ίδιο
    for i in range(1, dataF.shape[0]):
        dataStringLine = dataColumn[i]
        rawData = np.vstack((rawData, np.fromstring(
            dataStringLine[1:], dtype=float, sep=',')))

    return rawData[:, 100:260]

def make_items():
    # Εισαγωγή του αρχείου yaml
    module_path = os.path.abspath(PROJECT_DIR)
    with open(os.path.abspath(PROJECT_DIR / 'data/multiple_views.yml')) as file:
        experiment = yaml.load(file, Loader=yaml.FullLoader)
    # access: experiment['samples'], experiment['mouse_id']
    infrared_items, csv_items = [], []
    for i, hour in enumerate(experiment['samples']):
        for mouse_name in experiment['mouse_id']:
            for mouse_angle in experiment['mouse_angle']:
                jpg_file = experiment[mouse_name][mouse_angle]['jpg'][i]
                infrared_items.append(f'{module_path}/data/raw/{hour}/{mouse_name}/{jpg_file}')
                # identifiers.append((mouse_angle, mouse_name, hour))
                csv_file = experiment[mouse_name][mouse_angle]['csv'][i]
                csv_items.append(f'{module_path}/data/raw/{hour}/{mouse_name}/{csv_file}')
    return infrared_items, csv_items, experiment

def save_interim(infrared_items, csv_items):
    """
    in this utility function we create the drawn data from the 
    selected list of the yaml file 
    this file contains the unique file names for the utilized data
    data consist of:
    """
    mult_views_dir = os.path.abspath(INTERIM_DIR / 'multiple_views')
    if os.path.exists(mult_views_dir):
        os.mkdir(INTERIM_DIR / 'multiple_views')
    else:
        for infrared_item, csv_item in zip(infrared_items, csv_items):
            shutil.copy2(src=infrared_item, dst=mult_views_dir)
            shutil.copy2(src=csv_item, dst=mult_views_dir)

def save_processed(object_images, object_masks, initial_masks, markerBack, markerBody):
    obj_size = [obj.nbytes for obj in object_images]
    mask_size = [obj.nbytes for obj in object_masks]
    init_mask_size = [obj.nbytes for obj in initial_masks]
    print(f'Total dir size: {sum(obj_size) + sum(mask_size) + sum(init_mask_size)}')
    location_dir = os.path.abspath(PROCESSED_DIR / f'version{markerBack}_{markerBody}')
    os.mkdir(location_dir)
    # Convert to PIL Image and save
    for i, file in enumerate(object_images):
        Image.fromarray(file).save(f'{location_dir}/{i}_obj_image.tif')
    for i, file in enumerate(object_masks):
        Image.fromarray(file).save(f'{location_dir}/{i}_obj_mask.tif')
    for i, file in enumerate(initial_masks):
        Image.fromarray(file).save(f'{location_dir}/{i}_initial_mask.tif')

    return location_dir

def load_processed(markerBack, markerBody):
    object_images, object_masks, initia_masks = [], [], []
    location = f'version{markerBack}_{markerBody}'
    location_dir = os.path.abspath(PROCESSED_DIR / location)
    if os.path.exists(location_dir) or os.listdir(location_dir) == []:
        # Read back from disk and convert to Numpy format {id}_obj_image.tif
        for i in sorted(os.listdir(location_dir)):
            if i.endswith('obj_image.tif'):
                object_images.append(np.array(Image.open(f'{location_dir}/{i}')))
            if i.endswith('obj_mask.tif'):
                object_masks.append(np.array(Image.open(f'{location_dir}/{i}')))
            if i.endswith('initial_mask.tif'):
                initia_masks.append(np.array(Image.open(f'{location_dir}/{i}')))
        return object_images, object_masks, initia_masks

HERE = Path(__file__)       # ~/Adiposer/src/data/data_utils.py
SRC_DIR = HERE.parent.parent
PROJECT_DIR = SRC_DIR.parent
RAW_DIR = PROJECT_DIR / "data" / "raw"
INTERIM_DIR = PROJECT_DIR / "data" / "interim"
PROCESSED_DIR = PROJECT_DIR / "data" / "processed"
mode = 0o755
print(__name__)