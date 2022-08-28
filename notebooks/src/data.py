import os
from pathlib import Path
from typing import List, Tuple

import numpy as np
import pandas as pd
import yaml
# from skimage.feature import downscale_local_mean
from skimage.filters import unsharp_mask
from skimage.io import imread

HERE = Path(__file__)  # ~/Adiposer/src/data/data_utils.py
SRC_DIR = HERE.parent
PROJECT_DIR = SRC_DIR.parent
RAW_DIR = PROJECT_DIR / "data" / "raw"
INTERIM_DIR = PROJECT_DIR / "data" / "interim"
PROCESSED_DIR = PROJECT_DIR / "data" / "processed"
project_dir = os.path.abspath(PROJECT_DIR)


class FLIRImage:
    def __init__(self) -> None:
        self.mouse_id = ""
        self.angle = ""
        self.sample = ""
        self.ir_id = ""
        self.dc_id = ""
        self.csv_id = ""
        self.ir_image = np.ndarray(shape=(320, 240))
        self.dc_image = np.ndarray(shape=(320, 240))
        self.csv_image = np.ndarray(shape=(320, 240))

    def set_ir(self) -> None:
        """fpath: το path της IR και η θερμική εικόνα"""
        ir_path = f"{project_dir}/data/raw/{self.sample}/{self.mouse_id}/{self.ir_id}"
        if not os.path.exists(ir_path):
            self.ir_image = np.zeros(shape=(320, 240))
            return
        ir_image = imread(ir_path, as_gray=True)
        self.ir_image = ir_image[:, 100:260]

    def set_dc(self) -> None:
        """fpath: το path της DC και η οπτική"""
        dc_path = f"{project_dir}/data/raw/{self.sample}/{self.mouse_id}/{self.dc_id}"
        if not os.path.exists(dc_path):
            self.dc_image = np.empty(shape=(320, 240))
            return
        dc_image = imread(dc_path, as_gray=True)
        self.dc_image = dc_image

    def set_csv(self) -> None:
        """fpath: το path του CSV και οι θερμοκρασίες"""
        csv_path = f"{project_dir}/data/raw/{self.sample}/{self.mouse_id}/{self.csv_id}"
        if not os.path.exists(csv_path):
            self.csv_image = np.zeros(shape=(320, 240))
            return
        # με sep = ' ,' τότε παράγει δίστηλο frame
        df = pd.read_csv(filepath_or_buffer=csv_path, sep=" ,", engine="python")
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


class ImageCollection:

    def __init__(self, *args, **kwargs) -> None:
        self.image_collection: List[FLIRImage] = []
        if args == "all":
            return 
        # load csv sample file and let pandas do filtering 
        with open(os.path.abspath(PROJECT_DIR / "data/multiple_views.yml")) as file:
            experiment = yaml.load(file, Loader=yaml.FullLoader)
        df = pd.DataFrame()
        for i, sample in enumerate(experiment["samples"]):
            for mouse_id in experiment["ids"]:
                for angle in experiment["angles"]:
                    fi = FLIRImage()
                    fi.mouse_id = mouse_id
                    fi.angle = angle
                    fi.sample = sample
                    fi.ir_id = experiment[mouse_id][angle]["ir"][i]
                    fi.csv_id = experiment[mouse_id][angle]["csv"][i]
                    fi.dc_id = experiment[mouse_id][angle]["dc"][i]
                    fi.set_ir()
                    fi.set_csv()
                    fi.set_dc()
                    self.image_collection.append(fi)

    def get_by_id(self, id) -> FLIRImage:
        empty_image = FLIRImage()
        for flir_image in self.image_collection:
            if flir_image.ir_id == id or flir_image.dc_id == id or flir_image.csv_id == id:
                return flir_image
        return empty_image

    def get_by_mouse_name(self, mouse_id) -> List[FLIRImage]:
        flir_images = []
        for flir_image in self.image_collection:
            if mouse_id == flir_image.mouse_id:
                flir_images.append(flir_image)
        return flir_images

    def get_by_sample(self, sample) -> List[FLIRImage]:
        flir_images = []
        for flir_image in self.image_collection:
            if sample == flir_image.sample:
                flir_images.append(flir_image)
        return flir_images

    def get_by_angle(self, angle) -> List[FLIRImage]:
        flir_images = []
        for flir_image in self.image_collection:
            if angle == flir_image.angle:
                flir_images.append(flir_image)
        return flir_images
