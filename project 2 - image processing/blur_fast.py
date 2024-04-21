from greyscale import greyscale
import numpy as np
from PIL import Image
import time

start_time = time.time()

def fast(array):
    integral = np.cumsum(np.cumsum(array, axis=1), axis=0)
    blurred = np.zeros_like(array)
    
    for i in range (35, blurred.shape[0]-36):
        for j in range (35, blurred.shape[1]-36):
            summed = integral[i+35,j+35] - integral[i+35,j-35] - integral[i-35,j+35] + integral[i-35,j-35]
            blurred[i,j] = summed/5041
    return blurred

Image.fromarray(fast(greyscale("road.jpg"))).show()
print("%s seconds (summed area table approach)" % (time.time() - start_time))
