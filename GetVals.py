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


def func(bigDF, url='', arr=[[]]):
    #url = 'https://data.mangonetwork.org/data/transport/mango/archive/low/greenline/raw/2022/237/05/mango-low-greenline-20220825-052400.hdf5'
    if (not url==''):
        r = rqs.get(url, stream=True)
        dump = r.raw
        cwd = os.getcwd()
        location = os.path.abspath(cwd)
        with open('testfile.hdf5', 'wb') as location:
            sh.copyfileobj(dump, location)
        file = h5.File('testfile.hdf5', 'r+')
        
        a = file['image'] #array of values
        #emptA = []

    
    a = a[100:450, 100:550]
    h = len(a[0])
    k = len(a[:, 0])
    count = 0
    dataPoints = []
    #radius to use for equation of a circle: 
    rad = 200 #change to increase radius of measurement
    #image has decimals, need to iterate with for all and then use .indepip install chardet
    # x Of for finding temporary dimensions for the circle calculation
    
    for x in range(k):
        
        for y in range(h):
            circleCalc = (x - (k/2))**2 + (y - (h/2))**2 
            # print('h' + str(h))
            # print(k)
            # print(rad**2)
            # print(circleCalc)
            if circleCalc <= rad**2:
                dataPoints.append(a[x, y])
                #print(a[x][y])
                count += 1
                


    # for i in range(w):
    #     for j in range(h):
    #         if (i)

    # lum_img = Image.new('L',[h,k] ,0)
    # draw = ImageDraw.Draw(lum_img)
    # draw.pieslice([(0,0),(h,k)],0,360,fill=255)
    # img_arr = np.array(a)
    # lum_img_arr = np.array(lum_img)


    # #make something to trim the rectangle into a central circle. get all arrays that are in positions index <= abs((length/2) + 
    # print(a.shape)
    # print(a[1])
    # print(list(file.keys())) # don't need units, only images
    # #correlation between 
    # final_img_arr = np.dstack((img_arr, lum_img_arr))
    # imgplot = plt.imshow(Image.fromarray(final_img_arr))
    # plt.imshow(a)
    # plt.show()
    # print(count)
    # print(k, h)
    # plt.imshow(a) #cmap = 'hot')
    # plt.show()
    # print(a)
    p = np.percentile(dataPoints, 10)
    b = np.percentile(dataPoints, 90)
    varArr = [i for i in dataPoints if i > p and i < b]
    #c = np.fft.fft(dataPoints, n=5)
    norm = np.linalg.norm(a)
    a = a/norm 
    d = scipy.fft.fft2(a)
    #FourierCorrelation.storeFourier(d)
    #corr = spearmanr(d, dataPoints, nan_policy='omit')
    #print(corr)
    for i in range(len(d)):
        for j in range(len(d[i])):
            d[i][j] = abs(d[i][j])
        
    d = d.real
    #print(d[0].shape)
    #print(d)
    bigDF[url] = np.ndarray.flatten(d)
    
    #print(varArr)
    #print([np.median(dataPoints), np.percentile(dataPoints, 90),  np.percentile(dataPoints, 10)])
    return [np.mean(dataPoints), d[1][3], d[349][0], d[28][449], d[349][3]]
#func(url = 'https://data.mangonetwork.org/data/transport/mango/archive/blo/greenline/raw/2022/291/04/mango-blo-greenline-20221018-043800.hdf5')
#def func1():




#correlation between current variables and labelled images, then compare with the 1s and 0s
#abs for each fourier frequency, try to get 3 features
#swap a feature with the best fourier feature
#numpy correlation function