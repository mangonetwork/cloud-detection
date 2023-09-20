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
import GetVals
import csv

def storeFourier(fourier):
    for i in range(len(fourier)):
        fourier[i] = abs(fourier[i])
        fourier[i] = np.real(fourier[i])
        
    with open('FourierData.csv', 'w', newline='') as myfile:
        wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
        wr.writerow(fourier)


def readFourier():
    with open("./FourierData.csv", 'r') as file:
        csvreader = csv.reader(file)
        for row in csvreader:
            print(row)









