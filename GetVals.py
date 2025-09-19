# -*- coding: utf-8 -*-
"""
Created on Wed Mar  8 16:35:03 2023

@author: ndfon & MBurnes
"""
import requests as rqs #urls from website
import matplotlib as mp
import matplotlib.pyplot as plt
import pandas as pd
import math
import numpy as np
import h5py as h5 # hdf5 files - large files compact
import shutil as sh
import os as os
from PIL import Image, ImageDraw
import math
import scipy
from scipy.stats import spearmanr


def func(bigDF=None, filename=None, url=None, arr=None):

    if filename:
        file = h5.File(filename, 'r')
        arr = file['image'] #array of values

    elif url:   #if the input is a URL, retrieve the image data and label it as arr
        r = rqs.get(url, stream=True)
        dump = r.raw
        cwd = os.getcwd()   # Messy, especially if you're not deleting the file afterwards
        location = os.path.abspath(cwd)
        with open('testfile.hdf5', 'wb') as location:
            sh.copyfileobj(dump, location)

        file = h5.File('testfile.hdf5', 'r+')
        arr = file['image'] #array of values
    else:
        arr = np.array(arr)

    a = arr[50:450, 100:600]  #crop the image

   
    # h = len(a[0])
    # k = len(a[:, 0])
    # count = 0
    # dataPoints = [] #dataPoints stores the values inside of a circular crop which are used to get a mean
    # #radius to use for equation of a circle: 
    # rad = 200 #change to increase radius of measurement
    
    # for x in range(k): #This loop retrieves the data points that are inside the camera lens to make a complete mean measurement
        
    #     for y in range(h):
    #         circleCalc = (x - (k/2))**2 + (y - (h/2))**2 
    #         if circleCalc <= rad**2:
    #             dataPoints.append(a[x, y])
    #             count += 1
                
    norm = np.linalg.norm(a) #the data in the image is normalized before the Fourier transformation
    pre_norm_a = a
    a = a/norm 
    d = scipy.fft.fft2(a) #The Fourier features are calculated through the fourier transform and then abs is used to combine the real and imaginary components
    # for i in range(len(d)):
    #     for j in range(len(d[i])):
    #         d[i][j] = abs(d[i][j])
    # #print(d.shape)   
    d = d.real #we use d.real to dispose of the 0j value still present after using abs
    # bigDF[url] = np.ndarray.flatten(d) 
    #print(len(d[0]))
    a = a * norm
    #updated: 1, 450, 453, 7199 are the flattened fourier features I chose. Space for one more (8549 should be used if desired)
    return [np.mean(pre_norm_a), d[0][1], d[1][0], d[1][499], d[399][496]] # replaced d[0][1], d[1][0], d[19][0] d[15][449] #mean of datapoints and the most significant fourier features are returned, greenline
    #after redline integration, 1, 449, 450, 157040, 7649, 8549, 149401, 150301
    #return [np.mean(dataPoints), d[0][5], d[63][425], d[39][128], d[311][322]] #redline #
    #no signiciant difference for circle crop vs rectangle crop (no var)
    #


#453
#896
#897
#157053
#157054
#157497
# 450
# 157050
