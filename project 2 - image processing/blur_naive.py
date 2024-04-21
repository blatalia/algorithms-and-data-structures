from greyscale import greyscale
import numpy as np
from PIL import Image
import time

start_time = time.time()

#*************************************************** faster naive approach
def naive_fast(array):
    blurred = np.zeros_like(array)
    for i in range(35, array.shape[0]-35):
        for j in range(35, array.shape[1]-35):
            mask = array[i-35:i+35, j-35:j+35]
            blurred[i, j] = (np.sum(mask) / (71*71))
    return blurred

Image.fromarray(naive_fast(greyscale("road.jpg"))).show()
print("%s seconds (naive approach)" % (time.time() - start_time))

# #************************************************** slower naive approach
# def naive_slow(array):
#     blurred_array = np.zeros_like(array)
#     rows = array.shape[0]
#     cols = array.shape[1]
#     for x in range(rows):
#       for y in range(cols): 
#         avg = 0
#         div = 0
#         for i in range(-35,36):
#            for j in range(-35,36):
#               if (i != 0 or j != 0) and (x+i >= 0 and x + i < array.shape[0]) and (y+j >= 0 and y + j < array.shape[1]):
#                 avg += array[x+i,y+j]
#                 div += 1
#         blurred_array[x,y] = avg/div
#     return blurred_array
# Image.fromarray(naive_slow(greyscale("road.jpg"))).show()
# print("%s seconds (naive approach)" % (time.time() - start_time))