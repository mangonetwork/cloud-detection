import matplotlib.pyplot as plt
import os
import requests as rqs
import h5py as h5
import shutil as sh
import getUrls
urlNums = [x for x in range(40, 120) if x % 2 == 0]
urls = getUrls.getURL()
def ViewIncorrect(urls):

    for url in urls:
        # fig, ax = plt.subplots(len(urls), len(urls))
        r = rqs.get(url, stream=True)
        print(url)
        dump = r.raw
        cwd = os.getcwd()
        location = os.path.abspath(cwd)
        with open('testfile5.hdf5', 'wb') as location:
            sh.copyfileobj(dump, location)
        file = h5.File('testfile5.hdf5', 'r+')
        a = file['image']
        plt.imshow(a)
        plt.show()
        file.close()

# for url, cloudy in urls:
#     _, ax = plt.subplots()
#     r = rqs.get(url, stream=True)
#     dump = r.raw
#     cwd = os.getcwd()
#     location = os.path.abspath(cwd)
#     with open('testfile.hdf5', 'wb') as location:
#         sh.copyfileobj(dump, location)
#     file = h5.File('testfile.hdf5', 'r+')
#     a = file['image']
#     plt.imshow(a)
    

# plt.show()