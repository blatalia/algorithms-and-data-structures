import numpy as np
from PIL import Image
import copy

def open_image(image):
    og = Image.open(image)
    og_array = np.asarray(og)
    return og_array

def greyscale(image):
    colorarray = copy.deepcopy(open_image(image))
    greyscalearray = np.rint(np.mean(colorarray, axis = 2))
    greyscalearray = greyscalearray.astype('int32')
    return greyscalearray

def opengreyscale(image):
    return Image.fromarray(greyscale(image)).show()
opengreyscale("yoda.jpeg")
