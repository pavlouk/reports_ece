import cv2
import os
import argparse

def rgb_to_hsv(image):
    print ('hsv')
    hsv_image = cv2.cvtColor(image, cv2.COLOR_RGB2HSV)
    hue, sat, val = hsv_image[:, :, 0], hsv_image[:, :, 1], hsv_image[:, :, 2]
    return hsv_image, hue, sat, val

def rgb_to_lab(image):
    lab_image = cv2.cvtColor(image, cv2.COLOR_RGB2LAB)
    l_chan, a_chan, b_chan = lab_image[:, :, 0], lab_image[:, :, 1], lab_image[:, :, 2]
    return lab_image, l_chan, a_chan, b_chan

def treshold_otsu(gray_image):
    ret, thresholded_image = cv2.threshold(gray_image, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
    return thresholded_image

def global_threshold(gray_image):
    ret, thresholded_image = cv2.threshold(gray_image, 127, 255, cv2.THRESH_BINARY)
    return thresholded_image


class SegmentationType(object):
    DISPLAY_NAME = "invalid"

    def __init__(self, filename, path):
        self.filename = filename
        self.path = path
        self.input_data = None
        self.output_data = None

    def read_image(self):
        self.input_data =  cv2.imread(self.path + self.filename)[1]

    def write_image(self):
        cv2.imwrite(self.path + self.filename.split('.')[0] + '_' + self.DISPLAY_NAME + '.png', self.output_data)

    def process(self):
        # override in derived classes to perform an actual segmentation
        pass

    def start_pipeline(self):
        self.read_image()
        self.process()
        self.write_image()

class HSVSegmenter(SegmentationType):
    DISPLAY_NAME = 'HSV'

    def process(self):
        source = rgb_to_hsv(self.input_data)
        self.output_data = treshold_otsu(source)


class LABSegmenter(SegmentationType):
    DISPLAY_NAME = 'LAB'

    def process(self):
        source = rgb_to_lab(self.input_data)
        self.output_data = global_threshold(source)

def main() -> None:
    parser = argparse.ArgumentParser(description = 'Test.')
    parser.add_argument('-d', '--img_dir', required = True,
                        help = 'directory containing images to segment.')
    parser.add_argument('-p', '--procedure', required = True,
                        help = 'procedure to run.')

    args = parser.parse_args()
    print(args)
    img_dir = args.img_dir
    procedure = args.procedure
    images = os.listdir(img_dir)

    segmenter_class = {
        'hsv': HSVSegmenter,
        'lab': LABSegmenter
    }.get(procedure)

    if not segmenter_class:
        raise AttributeError("Invalid segmentation method '{}'".format(procedure))

    for img in images:
        os.chdir(img_dir)
        processor = segmenter_class(img, img_dir, procedure)
        processor.start_pipeline()