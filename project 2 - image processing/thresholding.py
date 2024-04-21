from greyscale import greyscale
import numpy as np
from PIL import Image
import copy

def singlethresholding(greyscale_sth):
    threshold = 150
    greyscaleth1 = copy.deepcopy(greyscale_sth)
    greyscaleth1[greyscaleth1 >= threshold] = 255
    greyscaleth1[greyscaleth1 < threshold] = 0
    return Image.fromarray(greyscaleth1).show()

def doublethresholding(greyscale_dth):
    th1 = 100
    th2 = 190
    greyscaleth2 = copy.deepcopy(greyscale_dth)
    greyscaleth2[greyscaleth2 < th1] = 0
    greyscaleth2[greyscaleth2 > th2] = 0
    greyscaleth2[(greyscaleth2 >= th1) & (greyscaleth2 <= th2)] = 255
    return Image.fromarray(greyscaleth2).show()

greyscale = greyscale("yoda.jpeg")
singlethresholding(greyscale)
doublethresholding(greyscale)

