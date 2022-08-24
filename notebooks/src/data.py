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
        self.mouse_name = ""
        self.angle = ""
        self.sample = ""
        self.ir_path = ""
        self.dc_path = ""
        self.csv_path = ""
        self.ir_image = np.ndarray(shape=(320, 240))
        self.dc_image = np.ndarray(shape=(320, 240))
        self.csv_image = np.ndarray(shape=(320, 240))

    def set_ir(self, fpath: str, as_gray=True) -> None:
        """fpath: το path της IR και η θερμική εικόνα"""
        self.ir_path = fpath
        ir_image = imread(fpath, as_gray=as_gray)
        self.ir_image = ir_image[:, 100:260]

    def set_dc(self, fpath: str) -> None:
        """fpath: το path της DC και η οπτική"""
        self.dc_path = fpath
        dc_image = imread(fpath, as_gray=True)
        self.dc_image = dc_image[:, 100:260]

    def set_csv(self, fpath: str) -> None:
        """fpath: το path του CSV και οι θερμοκρασίες"""
        self.csv_path = fpath
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
        """στο downscale_local_mean η ανάλυση γίνεται η μισή (120, 77)"""
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
                for angle in experiment["mouse_angle"]:
                    fi = FLIRImage()
                    jpg_id = experiment[mouse_name][angle]["jpg"][i]
                    csv_id = experiment[mouse_name][angle]["csv"][i]
                    dc_id = experiment[mouse_name][angle]["dc"][i]
                    fi.id = jpg_id
                    fi.mouse_name = mouse_name
                    fi.angle = angle
                    fi.sample = hour
                    fi.set_ir(
                        fpath=f"{module_path}/data/raw/{hour}/{mouse_name}/{jpg_id}"
                    )
                    fi.set_csv(f"{module_path}/data/raw/{hour}/{mouse_name}/{csv_id}")
                    fi.set_dc(f"{module_path}/data/raw/{hour}/{mouse_name}/{dc_id}")
                    cls.flir_images.append(fi)

    @classmethod
    def get_by_id(cls, id) -> FLIRImage:
        for flir_image in cls.flir_images:
            if flir_image.id == id:
                return flir_image

    @classmethod
    def get_by_mouse_name(cls, mouse_id) -> List[FLIRImage]:
        flir_images = []
        for flir_image in cls.flir_images:
            if mouse_id == flir_image.mouse_name:
                flir_images.append(flir_image)
        return flir_images

    @classmethod
    def get_by_sample(cls, sample) -> List[FLIRImage]:
        flir_images = []
        for flir_image in cls.flir_images:
            if sample == flir_image.sample:
                flir_images.append(flir_image)
        return flir_images

    @classmethod
    def get_by_angle(cls, angle) -> List[FLIRImage]:
        flir_images = []
        for flir_image in cls.flir_images:
            if angle == flir_image.angle:
                flir_images.append(flir_image)


image_collection = ImageCollection()
image_collection.make_images()

for image in image_collection.flir_images:
    image.csv_image
    image.csv_path
