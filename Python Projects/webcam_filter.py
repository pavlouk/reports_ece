import cv2
cap = cv2.VideoCapture(0)

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


while True:
    ret, frame = cap.read()
    source = rgb_to_lab(frame)[1]
    binary = global_threshold(source)
    binary = cv2.resize(binary, (0, 0), fx=2, fy=2, interpolation=cv2.INTER_NEAREST)
    cv2.imshow('frame', binary)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()