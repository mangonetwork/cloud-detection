# -*- coding: utf-8 -*-
"""
Created on Wed Mar  8 16:35:03 2023

@author: ndfon
"""
import requests as rqs #urls from website
import matplotlib as mp
import matplotlib.pyplot as plt
import pandas as pd

import numpy as np
import h5py as h5 # hdf5 files - large files compact
import shutil as sh
import os as os

def func():
    url = 'https://data.mangonetwork.org/data/transport/mango/archive/low/greenline/raw/2022/237/05/mango-low-greenline-20220825-052400.hdf5'
    r = rqs.get(url, stream=True)
    dump = r.raw
    cwd = os.getcwd()
    location = os.path.abspath(cwd)
    with open('testfile.hdf5', 'wb') as location:
        sh.copyfileobj(dump, location)
    file = h5.File('testfile.hdf5', 'r')
    
    a = file['image'] #array of values

    a = a[100:450, 100:550]
    #print(a.shape)
    #print(a[1])
    #print(list(file.keys())) # don't need units, only images
    #imgplot = plt.imshow(a)
    #plt.show()
    #plt.imshow(a, cmap = 'hot')
    #plt.show()
    #b=[]
    #for i in a:
        #b += [x for x in i if x < 60000]
    print(np.percentile(a, 90))
    print(np.percentile(a, 10))
    print(np.median(a))
func()

#def func1():
