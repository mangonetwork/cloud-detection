



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
import getUrls
from scipy.stats import spearmanr
import makePrediction

# def seefailures():
#     for row in getUrls.getURL():
#         res = makePrediction.makePrediction(row[0])
#         if res != row[1]:
#             print(res)
#             print(row)
# seefailures()

# with original crop (100:450, 100:550), bottom corner-ish
# [0.5207554886724045, 0.5142311153199162, 0.501646632251776, 0.5425676186838301, 0.5599164203046154, 0.5315147739932427, 0.5742475837304052, 0.5064896968472206, 0.5094727679045712, 0.5092323572012012, 0.5241249345270916, 0.5241249345270916, 0.5092323572012012, 0.5094727679045712, 0.5064896968472206, 0.5742475837304052, 0.5315147739932427, 0.5599164203046154, 0.5425676186838301, 0.501646632251776, 0.5142311153199162, 0.5207554886724045]
# [5399, 6299, 6749, 7199, 7649, 8099, 8549, 9899, 11251, 13049, 13051, 144899, 144901, 146699, 148051, 149401, 149851, 150301, 150751, 151201, 151651, 152551]
# [1, 449, 450, 900, 156600, 157050]
# [-0.6410236640016513, -0.6410236640016513, -0.6803932220646719, -0.5014695222668333, -0.5014695222668333, -0.6803932220646719]


# for wide crop arr[50:450, 100:600] (near full image)
# [0.5204157997783162, 0.5830829404667838, 0.5830829404667838, 0.5204157997783162]
# [502, 999, 199501, 199998]
# [1, 499, 500, 199500]
# [-0.7305291211438869, -0.7305291211438869, -0.7299151379328093, -0.7299151379328093]
#[0][1], [1][0], [1][499], [399][496]

#for pretty much just the image: a = arr[75:425, 125:575]
# []
# []
# [450, 157050]
# [-0.6252865173804327, -0.6252865173804327]

url = 'https://data.mangonetwork.org/data/transport/mango/archive/cvo/redline/raw/2024/272/09/mango-cvo-redline-20240928-093200.hdf5'
r = rqs.get(url, stream=True)
dump = r.raw
cwd = os.getcwd()
location = os.path.abspath(cwd)
with open('testfile.hdf5', 'wb') as location:
    sh.copyfileobj(dump, location)
file = h5.File('testfile.hdf5', 'r+')
arr = file['image'] #array of values
a = arr[50:450, 100:600] #crop the image
#a = arr[0:][0:]
a = arr
fig, axs = plt.subplots(1, 2)
axs[0].set_title("Sample Image with Class 'Clear'")
axs[0].imshow(arr, cmap='gray', vmax = 10000)
axs[0].axis("off")
url = 'https://data.mangonetwork.org/data/transport/mango/archive/blo/greenline/raw/2024/159/05/mango-blo-greenline-20240607-052600.hdf5'
r = rqs.get(url, stream=True)
dump = r.raw
cwd = os.getcwd()
location = os.path.abspath(cwd)
with open('testfile2.hdf5', 'wb') as location:
    sh.copyfileobj(dump, location)
file = h5.File('testfile2.hdf5', 'r+')
arr = file['image'] #array of values
a = arr[50:450, 100:600] #crop the image
a = arr
axs[1].set_title("Sample Image with Class 'Cloudy'")
axs[1].imshow(arr, cmap='gray', vmax = 10000)
axs[1].axis("off")
#axs[1, 1].imshow(a, cmap='gray', vmax = 10000)
plt.rcParams.update({'font.size': 15})
fig.tight_layout()
plt.show()


#[[0.9149854985497963, 1], [0.9159345934593225, 2], [0.9162829616294307, 3], [0.9164011401140323, 4], [0.9160176017602055, 5], [0.9152318565189645, 6]] with new crop of a = arr[50:450, 100:600] and ffs of d[0][1], d[1][0], d[1][499], d[399][496]
#seefailures()

#[[0.9136993699369363, 1], [0.9149754975497368, 2], [0.9156215621561566, 3], [0.9159380938094044, 4], [0.9157515751575441, 5], [0.9149608294162546, 6]]
#[[0.9147834783477782, 1], [0.9157465746574418, 2], [0.9160609394272143, 3], [0.9161948584575579, 4], [0.9158375187594073, 5], [0.9150348368169933, 6]]

#[[0.9148767153854234, 1], [0.9156739046639932, 2], [0.9161366943622752, 3], [0.9163098570797268, 4], [0.9159916267942717, 5], [0.9152254249815102, 6]] (no weighting, removing the splits with a distribtuion of samplesmore than half + 5 of the training dataset)

#precision: [[0.9001601744230814, 1], [0.9021257752304417, 2], [0.9016608195556393, 3], [0.9021686607121234, 4], [0.9024504058142806, 5], [0.901786753322591, 6]]

#cutting out sets with more than 60% one class in testing
# [[0.9147347347347354, 1], [0.9162162162162112, 2], [0.9153420086753339, 3], [0.9158658658658538, 4], [0.9159719719719728, 5], [0.9152218885552093, 6]]
# [[0.9001601744230814, 1], [0.9021257752304417, 2], [0.9016608195556393, 3], [0.9021686607121234, 4], [0.9024504058142806, 5], [0.901786753322591, 6]]
# 2 4
# 29 4
# 34 4 best at 0.91, 0.88
# 59 4 0.915 0.9191919191919192
# 68 4 0.925 0.956989247311828 (equal conf matrix)
# 97 4 0.91 0.8942307692307693
# 98 4 0.9 0.8571428571428571
# 120 4 0.89 0.875
# 124 4 0.935 0.9223300970873787 (better at clear, worse at cloudy than 68)
# 143 4 0.925 0.9047619047619048
# 155 40.91 0.9270833333333334