import h5py as h5
import requests
import urllib.request

url = 'https://data.mangonetwork.org/data/transport/mango/archive/low/greenline/raw/2022/001/07/mango-low-greenline-20220101-070000.hdf5'

r = requests.get(url)
hfw = h5.File('temp.hdf5', 'w')
data = r.keys()
print(data)
hfw.write(data)
hfw.close()
f = h5.File("temp.hdf5", "r")
