import os
from pathlib import Path
from typing import List

import cv2 as cv
import numpy as np
import pandas as pd

HERE = Path(__file__)
ADIPOSER_DIR = HERE.parent.parent.parent
RAW_DIR = ADIPOSER_DIR / "data" / "raw"
INTERIM_DIR = ADIPOSER_DIR / "data" / "interim"
PROCESSED_DIR = ADIPOSER_DIR / "data" / "processed"
project_dir = os.path.abspath(ADIPOSER_DIR)
CSV_FILE = "selected.csv"


class FLIRImage:
    def __init__(self, mouse, angle, sample, ir_id, dc_id, csv_id) -> None:
        self.mouse = mouse
        self.angle = angle
        self.sample = sample
        self.ir_id = ir_id
        self.dc_id = dc_id
        self.csv_id = csv_id
        self.ir_image = np.zeros(shape=(320, 240))
        self.dc_image = np.zeros(shape=(2048, 1536))
        self.csv_image = np.zeros(shape=(320, 240))
        self.set_csv()
        self.set_dc()
        self.set_ir()

    def set_ir(self) -> None:
        ir_path = f"{project_dir}/data/raw/{self.sample}/{self.mouse}/{self.ir_id}"
        if not os.path.exists(ir_path):
            self.ir_id = "NOT FOUND"
            return
        self.ir_image = cv.imread(ir_path, flags=cv.IMREAD_GRAYSCALE)
        self.ir_image = self.ir_image[:, 100:260]

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
    def __init__(self, **kwargs) -> None:
        """
        constructs image collection based on keyword arguments
        if kwargs is None then construct the whole dataset
        mouse=["mouse_1", "mouse_2"]
        angle="left"
        """
        self.image_collection: List[FLIRImage] = []
        csv_path = f"{project_dir}/data/{CSV_FILE}"
        csv = pd.read_csv(csv_path)
        if kwargs is None:
            for index, data in csv.iterrows():
                self.image_collection.append(
                    FLIRImage(
                        mouse=data["mouse"],
                        angle=data["angle"],
                        sample=data["sample"],
                        ir_id=data["ir_id"],
                        dc_id=data["dc_id"],
                        csv_id=data["csv_id"],
                    )
                )
        else:
            mouse_angle_sample_ir_dc_csv_list = [
                kwargs.get("mouse"),
                kwargs.get("angle"),
                kwargs.get("sample"),
                kwargs.get("ir_id"),
                kwargs.get("dc_id"),
                kwargs.get("csv_id"),
            ]

            mouse_angle_sample_ir_dc_csv = list(
                map(
                    lambda x: "0" if x is None else "1",
                    mouse_angle_sample_ir_dc_csv_list,
                )
            )
            self.mouse_angle_sample_ir_dc_csv = "".join(mouse_angle_sample_ir_dc_csv)
            self.csv_results = {
                "100000": lambda: csv[(csv["mouse"] == kwargs["mouse"])],
                "110000": lambda: csv[
                    (csv["mouse"] == kwargs["mouse"])
                    & (csv["angle"] == kwargs["angle"])
                ],
                "111000": lambda: csv[
                    (csv["mouse"] == kwargs["mouse"])
                    & (csv["angle"] == kwargs["angle"])
                    & (csv["sample"] == kwargs["sample"])
                ],
                "101000": lambda: csv[
                    (csv["mouse"] == kwargs["mouse"])
                    & (csv["sample"] == kwargs["sample"])
                ],
                "000100": lambda: csv[(csv["ir_id"] == kwargs["ir_id"])],
            }.get(self.mouse_angle_sample_ir_dc_csv, lambda: "Not assigned case")
            self.csv_results = self.csv_results()
            for indx, data in self.csv_results.iterrows():  # type: ignore
                self.image_collection.append(
                    FLIRImage(
                        mouse=data["mouse"],
                        angle=data["angle"],
                        sample=data["sample"],
                        ir_id=data["ir_id"],
                        dc_id=data["dc_id"],
                        csv_id=data["csv_id"],
                    )
                )

    def get_single_image(self, id: str) -> FLIRImage:
        default_image = FLIRImage("", "", "", "", "", "")
        for flir_image in self.image_collection:
            if (
                flir_image.ir_id == id
                or flir_image.dc_id == id
                or flir_image.csv_id == id
            ):
                return flir_image
        return default_image

    def get_by_mouse_name(self, mouse: str) -> List[FLIRImage]:
        flir_images = []
        for flir_image in self.image_collection:
            if mouse == flir_image.mouse:
                flir_images.append(flir_image)
        return flir_images

    def get_by_sample(self, sample: str) -> List[FLIRImage]:
        flir_images = []
        for flir_image in self.image_collection:
            if sample == flir_image.sample:
                flir_images.append(flir_image)
        return flir_images

    def get_by_angle(self, angle: str) -> List[FLIRImage]:
        flir_images = []
        for flir_image in self.image_collection:
            if angle == flir_image.angle:
                flir_images.append(flir_image)
        return flir_images
