import matplotlib.pyplot as plt
import getUrls
import os
import requests as rqs
import h5py as h5
import random
import shutil as sh
fig, axs = plt.subplots(5, 5)
urls = getUrls.getURL()

for ax in axs.flat:
    url = random.choice(urls)[0]
    r = rqs.get(url, stream=True)
    dump = r.raw
    cwd = os.getcwd()
    location = os.path.abspath(cwd)
    with open('testfile2.hdf5', 'wb') as location:
        sh.copyfileobj(dump, location)
    file = h5.File('testfile2.hdf5', 'r+')
    
    a = file['image'] #array of values
    ax.plot(a)
plt.show()