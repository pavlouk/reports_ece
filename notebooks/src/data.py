import os
from pathlib import Path
from typing import List

import cv2 as cv
import numpy as np
import pandas as pd
import yaml

HERE = Path(__file__)
ADIPOSER_DIR = HERE.parent.parent.parent
RAW_DIR = ADIPOSER_DIR / "data" / "raw"
INTERIM_DIR = ADIPOSER_DIR / "data" / "interim"
PROCESSED_DIR = ADIPOSER_DIR / "data" / "processed"
project_dir = os.path.abspath(ADIPOSER_DIR)


class FLIRImage:
    def __init__(self) -> None:
        self.mouse = ""
        self.angle = ""
        self.sample = ""
        self.ir_id = ""
        self.dc_id = ""
        self.csv_id = ""
        self.ir_image = cv.Mat(shape=(320, 240))
        self.dc_image = cv.Mat(shape=(2048, 1536))
        self.csv_image = cv.Mat(shape=(320, 240))

    def set_ir(self) -> None:
        ir_path = f"{project_dir}/data/raw/{self.sample}/{self.mouse}/{self.ir_id}"
        if not os.path.exists(ir_path):
            self.ir_id = "NOT FOUND"
            return
        ir_image = cv.imread(ir_path, flags=cv.IMREAD_GRAYSCALE)
        self.ir_image = ir_image[:, 100:260]

    def set_dc(self) -> None:
        dc_path = f"{project_dir}/data/raw/{self.sample}/{self.mouse}/{self.dc_id}"
        if not os.path.exists(dc_path):
            self.dc_id = "NOT FOUND"
            return
        self.dc_image = cv.imread(dc_path, flags=cv.IMREAD_GRAYSCALE)

    def set_csv(self) -> None:
        csv_path = f"{project_dir}/data/raw/{self.sample}/{self.mouse}/{self.csv_id}"
        if not os.path.exists(csv_path):
            self.csv_id = "NOT FOUND"
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
    def __init__(self, *args) -> None:
        self.image_collection: List[FLIRImage] = []
        if args[0] == "all":
            return
        if args[0] == "IR_2060.jpg":
            fi = FLIRImage()
            fi.mouse = "mouse_1"
            fi.angle = "posterior"
            fi.sample = "0h"
            fi.ir_id = "IR_2060.jpg"
            fi.csv_id = "CSV_2060.jpg"
            fi.dc_id = "DC_2061.jpg"
            fi.set_ir()
            fi.set_csv()
            fi.set_dc()
            self.image_collection.append(fi)
        # load csv sample file and let pandas do filtering
        # with open(os.path.abspath(PROJECT_DIR / "data/multiple_views.yml")) as file:
        #     experiment = yaml.load(file, Loader=yaml.FullLoader)
        # # for i, sample in enumerate(experiment["samples"]):
        #     for mouse_id in experiment["ids"]:
        #         for angle in experiment["angles"]:

    def get_single_image(self, id) -> FLIRImage:
        default_image = FLIRImage()
        for flir_image in self.image_collection:
            if (
                flir_image.ir_id == id
                or flir_image.dc_id == id
                or flir_image.csv_id == id
            ):
                return flir_image
        return default_image

    def get_by_mouse_name(self, mouse) -> List[FLIRImage]:
        flir_images = []
        for flir_image in self.image_collection:
            if mouse == flir_image.mouse:
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
