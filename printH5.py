import h5py
import requests
import numpy
import shutil
import xarray

# r = 'https://data.mangonetwork.org/data/transport/mango/archive/low/greenline/raw/2022/063/03/mango-low-greenline-20220304-030000.hdf5'
# myData = requests.get(r)
# myFile = open('demofile3.txt', 'w')
# myFile.write(myData)

#what is the line for moon elevation
#what is up with the maximum issue
#literally just waiting for manual work?
#currently have moon elevation, time, max bright, median bright, and the manual cloud estimate. Max bright not working, where should I count the moon as being up or down


filename = "FPI_LOW_for_matthew_2021-08-15_2022-01-26.h5"
with h5py.File(filename, "r") as f:
    print("Keys: %s" % f.keys())
    data = list(f["time"])
    #print(data)
    #print(list(f["string6"]))
    #print(data)
    moonData = list(f["ze"])
    print(data)
    moonFile = open("moonData.txt", 'w')
    for moonItem in moonData:
        moonFile.write(str(moonItem) + '\n')
    moonFile.close()
    file = open("cloudData.txt", 'w')
    for item in data:
        file.write(str(item) + "\n")
    file.close()

    #we said -32 is the breaking point?
