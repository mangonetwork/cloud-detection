import matplotlib.pyplot as plt
import os
import requests as rqs
import h5py as h5
import shutil as sh
url = 'https://data.mangonetwork.org/data/transport/mango/archive/blo/greenline/raw/2022/278/08/mango-blo-greenline-20221005-083400.hdf5'
r = rqs.get(url, stream=True)
dump = r.raw
cwd = os.getcwd()
location = os.path.abspath(cwd)
with open('testfile.hdf5', 'wb') as location:
    sh.copyfileobj(dump, location)
file = h5.File('testfile.hdf5', 'r+')
    
a = file['image'] #array of values
plt.imshow(a)
plt.show()