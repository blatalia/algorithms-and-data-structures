from greyscale import greyscale
import numpy as np
from PIL import Image
import copy
import matplotlib.pyplot as plt

def pmf(greyscalearray):
    pmf_values_array = np.zeros(256)
    greyscale_pmf = copy.deepcopy(greyscalearray)
    for x in range(greyscale_pmf.shape[0]):
        for y in range(greyscale_pmf.shape[1]):
            z = greyscale_pmf[x][y]
            pmf_values_array[z] += 1
    return pmf_values_array / (greyscale_pmf.shape[1]*greyscale_pmf.shape[0])

def cdf(pmfarray):
    pmf_table = copy.deepcopy(pmfarray)
    cdf_values_array = copy.deepcopy(pmf_table)
    cdf_values_array[0] = pmf_table[0]
    for i in range(1,256):
        cdf_values_array[i] = pmf_table[i] + cdf_values_array[i-1]
    return cdf_values_array

def contrast(addcontrast):
    pmf_greyscale = pmf(addcontrast)
    cdf_values = cdf(pmf_greyscale)
    contrast = copy.deepcopy(addcontrast)
    for x in range(contrast.shape[0]):
        for y in range(contrast.shape[1]):
            contrast[x][y] = np.ceil(cdf_values[contrast[x][y]]*(len(cdf_values)-1))
    return contrast
Image.fromarray(contrast(greyscale("yoda.jpeg"))).show()

def histogram(cdfarray, title):
    x = np.arange(0,256,1)
    y = cdfarray
    plt.title(title)
    plt.scatter(x,y)
    plt.show()
histogram(cdf(pmf(greyscale("yoda.jpeg"))), "cdf before histogram equalization")
histogram(cdf(pmf(contrast(greyscale("yoda.jpeg")))), "cdf after histogram equalization")