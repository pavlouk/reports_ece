import os
from email.mime import image
from pathlib import Path
from tkinter import Image
from typing import List, Tuple

import numpy as np
import pandas as pd
import yaml

# from skimage.feature import downscale_local_mean
from skimage.filters import unsharp_mask
from skimage.io import imread

HERE = Path(__file__)  # ~/Adiposer/src/data/data_utils.py
SRC_DIR = HERE.parent.parent
PROJECT_DIR = SRC_DIR.parent
RAW_DIR = PROJECT_DIR / "data" / "raw"
INTERIM_DIR = PROJECT_DIR / "data" / "interim"
PROCESSED_DIR = PROJECT_DIR / "data" / "processed"


class FLIRImage:
    def __init__(self) -> None:
        self.id = ""
        self.ir_path = ""
        self.dc_path = ""
        self.csv_path = ""
        self.ir_image = np.ndarray(shape=(320, 240))
        self.dc_image = np.ndarray(shape=(320, 240))
        self.csv_image = np.ndarray(shape=(320, 240))

    def set_ir(self, fpath: str, as_gray=True) -> None:
        """fpath: σετάρει το path της IR και σετάρει την θερμική"""
        self.ir_path = fpath
        ir_image = imread(fpath, as_gray=as_gray)
        self.ir_image = ir_image[:, 100:260]

    def set_dc(self, fpath: str) -> None:
        """fpath: σετάρει το path της DC και σετάρει την οπτική"""
        self.dc_path = fpath
        dc_image = imread(fpath, as_gray=True)
        self.dc_image = dc_image[:, 100:260]

    def set_csv(self, fpath: str) -> None:
        self.csv_path = fpath
        """fpath: σετάρει το path του csv και σετάρει τις θερμοκρασίες"""
        # με sep = ' ,' τότε παράγει δίστηλο frame
        df = pd.read_csv(filepath_or_buffer=fpath, sep=" ,", engine="python")
        column_names = df.columns
        # data_column με το 'Frame 1,' έχει τα ℃ ως pd.Series
        data_column = df[column_names[0]]
        first_line = data_column[0]  # string
        # 320 είναι τα ',' και στα υπόλοιπα
        raw_data = np.fromstring(first_line[8:], dtype=float, sep=",")
        # τα επόμενα ξεκινάνε με ',', οπότε το ίδιο για τα επόμενα 239
        for i in range(1, df.shape[0]):
            data_string_line = data_column[i]
            raw_data = np.vstack(
                (raw_data, np.fromstring(data_string_line[1:], dtype=float, sep=","))
            )
        self.csv_image = raw_data[:, 100:260]  # type: ignore

    def img_to_vectors(self, img) -> Tuple[np.ndarray, np.ndarray]:
        """return the coordinates of the non-zero pixels"""
        elements = np.argwhere(img)
        x_ordinates, y_ordinates = np.vsplit(elements.transpose(), 2)
        return x_ordinates.ravel(), y_ordinates.ravel()

    def downscale(self) -> None:
        """
        downscale + unsharp mask when using a graph-based method due to memory complexity
        η ανάλυση γίνεται η μισή (120, 77)
        preprocessing // αλλαγές: αποκλιμάκωση εικόνας και αφαίρεση θορύβου
        """
        # self.ir_image = downscale_local_mean(self.ir_image, (2, 2))
        # or denoise_wavelet
        self.ir_image = unsharp_mask(self.ir_image)


class ImageCollection:
    flir_images: List[FLIRImage] = []

    @classmethod
    def make_images(cls) -> None:
        """Create global paths of the tags in the yaml file"""
        # yaml file
        module_path = os.path.abspath(PROJECT_DIR)
        with open(os.path.abspath(PROJECT_DIR / "data/multiple_views.yml")) as file:
            experiment = yaml.load(file, Loader=yaml.FullLoader)

        for i, hour in enumerate(experiment["samples"]):
            for mouse_name in experiment["mouse_id"]:
                for mouse_angle in experiment["mouse_angle"]:
                    fi = FLIRImage()
                    jpg_id = experiment[mouse_name][mouse_angle]["jpg"][i]
                    csv_id = experiment[mouse_name][mouse_angle]["csv"][i]
                    dc_id = experiment[mouse_name][mouse_angle]["dc"][i]
                    fi.id = jpg_id
                    fi.set_ir(f"{module_path}/data/raw/{hour}/{mouse_name}/{jpg_id}")
                    fi.set_csv(f"{module_path}/data/raw/{hour}/{mouse_name}/{csv_id}")
                    fi.set_dc(f"{module_path}/data/raw/{hour}/{mouse_name}/{dc_id}")
                    cls.flir_images.append(fi)

    @classmethod
    def get_by_id(cls, id) -> FLIRImage:
        return cls.flir_images[id]

    @classmethod
    def get_by_mouse_id(cls, mouse_id) -> List[FLIRImage]:
        return cls.flir_images[0:mouse_id]

    @classmethod
    def get_by_sample(cls, sample) -> List[FLIRImage]:
        return cls.flir_images[0:sample]

    @classmethod
    def get_by_angle(cls, angle) -> List[FLIRImage]:
        return cls.flir_images[0:angle]


image_collection = ImageCollection()
image_collection.make_images()

for image in image_collection.flir_images:
    image.csv_image
    image.csv_path
