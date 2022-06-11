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

class Segmentation1(object):
    def __init__(self, filename, path, procedure):
        self.filename = filename
        self.path = path
        self.procedure = procedure

    def start_pipline(self):
        # Read image
        image = cv2.imread(self.path + self.filename)

        # Do segmentation procedure depending on procedure
        if self.procedure == 'test01':
            source = rgb_to_hsv(image)[1]
            binary = treshold_otsu(source)
        elif self.procedure == 'test02':
            source = rgb_to_lab(image)[1]
            binary = global_threshold(source)

        # Save image
        cv2.imwrite(self.path + self.filename.split('.')[0] + '_' + self.procedure + '.png', binary)


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
    #images = [img[2:] for img in args.images]

    # Start segmentation for each image
    for img in images:
        os.chdir(img_dir)
        print('SEGMENTING ' + img)
        segmenter = Segmentation1(img, img_dir, procedure)
        obj = segmenter.start_pipline()
        del obj
    
if __name__ == '__main__':
    main()