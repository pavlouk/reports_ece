def rect_roi(image, ratios=(0.35, 0.65, 0.70, 0.78)):
    xmin = int(ratios[0]*image.shape[1])
    xmax = int(ratios[1]*image.shape[1])
    ymin = int(ratios[2]*image.shape[0])
    ymax = int(ratios[3]*image.shape[0])
    return xmin, xmax, ymin, ymax