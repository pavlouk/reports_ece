import os
import shutil
from pathlib import Path
from typing import List, Tuple

import numpy as np
import pandas as pd
import yaml
from PIL import Image
from skimage.io import imread

Images = List[np.ndarray]


def ir_fixer(fpath: str, as_gray=True) -> np.ndarray:
    """fpath: το path της jpeg εικόνας ΙR"""
    image = imread(fpath, as_gray=as_gray)
    return image[:, 100:260]


def dc_fixer(fpath: str) -> np.ndarray:
    """fname: το path της jpeg εικόνας DC"""
    image = imread(fpath, as_gray=True)
    return image.shape


def csv_fixer(fpath: str) -> np.ndarray:
    """fpath: δέχεται το path του csv με τις θερμοκρασίες"""
    # με sep = 'κενό,' τότε δίστηλο frame, με sep = 'κενό' τότε τετράστηλο frame
    data_frame = pd.read_csv(filepath_or_buffer=fpath, sep=" ,", engine="python")
    column_names = data_frame.columns
    # μόνο η πρώτη στήλη με το Frame 1 έχει τις θερμοκρασίες
    # data_column type: pandas Series
    # ας δούμε το πρώτο που έχει τη λέξη Frame 1 στην αρχή
    data_column = data_frame[column_names[0]]
    first_line = data_column[0]  # string
    # 320 ειναι τα κόμματα κάτι που ισχύει και για τα υπόλοιπα
    # εδώ υπάρχει η λέξη 'Frame 1,' την διώχνουμε
    raw_data = np.fromstring(first_line[8:], dtype=float, sep=",")
    # τα επόμενα ξεκινάνε με κόμμα, οπότε για τα επόμενα 239 θα κάνουμε το ίδιο
    for i in range(1, data_frame.shape[0]):
        data_string_line = data_column[i]
        raw_data = np.vstack(
            (raw_data, np.fromstring(data_string_line[1:], dtype=float, sep=","))
        )
    # return raw_data[:, 100:260] causes linting warning
    return raw_data[:, 100:260]  # type: ignore


def make_items() -> Tuple[List[str], List[str]]:
    """Εισαγωγή του αρχείου yaml"""
    module_path = os.path.abspath(PROJECT_DIR)
    with open(os.path.abspath(PROJECT_DIR / "data/multiple_views.yml")) as file:
        experiment = yaml.load(file, Loader=yaml.FullLoader)
    infrared_items, csv_items = [], []
    for i, hour in enumerate(experiment["samples"]):
        for mouse_name in experiment["mouse_id"]:
            for mouse_angle in experiment["mouse_angle"]:
                jpg_file = experiment[mouse_name][mouse_angle]["jpg"][i]
                infrared_items.append(
                    f"{module_path}/data/raw/{hour}/{mouse_name}/{jpg_file}"
                )
                # identifiers.append((mouse_angle, mouse_name, hour))
                csv_file = experiment[mouse_name][mouse_angle]["csv"][i]
                csv_items.append(
                    f"{module_path}/data/raw/{hour}/{mouse_name}/{csv_file}"
                )
    return infrared_items, csv_items


def save_interim(infrared_items, csv_items) -> None:
    """
    create the drawn data from the selected list of the yaml file
    this file contains the unique file names for the utilized data
    data consist of:
    """
    mult_views_dir = os.path.abspath(INTERIM_DIR / "multiple_views")
    if os.path.exists(mult_views_dir):
        os.mkdir(INTERIM_DIR / "multiple_views")
    else:
        for infrared_item, csv_item in zip(infrared_items, csv_items):
            shutil.copy2(src=infrared_item, dst=mult_views_dir)
            shutil.copy2(src=csv_item, dst=mult_views_dir)


def save_processed(
    object_images: Images,
    object_masks: Images,
    initial_masks: Images,
    marker_back: int,
    marker_body: int,
) -> str:
    """save on the data / processed folder"""
    obj_size = [obj.nbytes for obj in object_images]
    mask_size = [obj.nbytes for obj in object_masks]
    init_mask_size = [obj.nbytes for obj in initial_masks]
    print(f"Total dir size: {sum(obj_size) + sum(mask_size) + sum(init_mask_size)}")
    location_dir = os.path.abspath(
        PROCESSED_DIR / f"version{marker_back}_{marker_body}"
    )
    os.mkdir(location_dir)
    # Convert to PIL Image and save
    for i, file in enumerate(object_images):
        Image.fromarray(file).save(f"{location_dir}/{i}_obj_image.tif")
    for i, file in enumerate(object_masks):
        Image.fromarray(file).save(f"{location_dir}/{i}_obj_mask.tif")
    for i, file in enumerate(initial_masks):
        Image.fromarray(file).save(f"{location_dir}/{i}_initial_mask.tif")

    return location_dir


def load_processed(marker_back: int, marker_body: int):
    """load the processed data from the data / processed folder"""
    object_images, object_masks, initia_masks = [], [], []
    location = f"version{marker_back}_{marker_body}"
    location_dir = os.path.abspath(PROCESSED_DIR / location)
    if os.path.exists(location_dir) or os.listdir(location_dir) == []:
        # Read back from disk and convert to Numpy format {id}_obj_image.tif
        for i in sorted(os.listdir(location_dir)):
            if i.endswith("obj_image.tif"):
                object_images.append(np.array(Image.open(f"{location_dir}/{i}")))
            if i.endswith("obj_mask.tif"):
                object_masks.append(np.array(Image.open(f"{location_dir}/{i}")))
            if i.endswith("initial_mask.tif"):
                initia_masks.append(np.array(Image.open(f"{location_dir}/{i}")))
        return object_images, object_masks, initia_masks


HERE = Path(__file__)  # ~/Adiposer/src/data/data_utils.py
SRC_DIR = HERE.parent.parent
PROJECT_DIR = SRC_DIR.parent
RAW_DIR = PROJECT_DIR / "data" / "raw"
INTERIM_DIR = PROJECT_DIR / "data" / "interim"
PROCESSED_DIR = PROJECT_DIR / "data" / "processed"
