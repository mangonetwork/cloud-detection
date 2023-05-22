# -*- coding: utf-8 -*-
"""
Created on Wed Mar  8 16:35:03 2023

@author: ndfon & MBurnes
"""
import requests as rqs #urls from website
#import matplotlib as mp
import matplotlib.pyplot as plt
import pandas as pd

import numpy as np
import h5py as h5 # hdf5 files - large files compact
import shutil as sh
import os as os
from PIL import Image, ImageDraw
import math
def func(url):
    #url = 'https://data.mangonetwork.org/data/transport/mango/archive/low/greenline/raw/2022/237/05/mango-low-greenline-20220825-052400.hdf5'
    r = rqs.get(url, stream=True)
    dump = r.raw
    cwd = os.getcwd()
    location = os.path.abspath(cwd)
    with open('testfile.hdf5', 'wb') as location:
        sh.copyfileobj(dump, location)
    file = h5.File('testfile.hdf5', 'r')
    
    a = file['image'] #array of values
    emptA = []

    #a = a[100:450, 100:550]
    h = len(a[0])
    k = len(a[:, 0])
    count = 0
    #radius to use for equation of a circle: 
    rad = 50
    #image has decimals, need to iterate with for all and then use .iO for finding temporary dimensions for the circle calculation
    for x in range(k):
        for y in range(h):
            circleCalc = (x - (k/2))**2 + (y - (h/2))**2 
            # print('h' + str(h))
            # print(k)
            # print(rad**2)
            # print(circleCalc)
            if circleCalc > rad**2:
                a[x][y] = 10000
                count += 1
                


    # for i in range(w):
    #     for j in range(h):
    #         if (i)

    # lum_img = Image.new('L',[h,w] ,0)
    # draw = ImageDraw.Draw(lum_img)
    # draw.pieslice([(0,0),(h,w)],0,360,fill=255)
    # img_arr = np.array(a)
    # lum_img_arr = np.array(lum_img)


    #make something to trim the rectangle into a central circle. get all arrays that are in positions index <= abs((length/2) + 
    #print(a.shape)
    #print(a[1])
    #print(list(file.keys())) # don't need units, only images
    
    # final_img_arr = np.dstack((img_arr, lum_img_arr))
    # imgplot = plt.imshow(Image.fromarray(final_img_arr))
    # plt.show()
    print(count)
    print(k, h)
    plt.imshow(a, cmap = 'hot')
    plt.show()
    print(a)
    
    
    #b=[]
    #for i in a:
        #b += [x for x in i if x < 60000]
    return [np.median(a), np.percentile(a, 90),  np.percentile(a, 10)]
#func()

#def func1():
