import h5py
import datetime
filename = "FPI_LOW_for_matthew_2021-08-15_2023-01-02.h5"
import xarray as xr
data = xr.open_dataset('FPI_LOW_for_matthew_2021-08-15_2023-01-02.h5')
i = 0
print(data['time'][15].to_numpy())

#using to_numpy fixes the error
# with h5py.File(filename, "r") as f:
#     i += 1
#     print("Keys: %s" % f.keys())
#     h5Data = list(f["time"])
#     print(h5Data[15])
    #print(f.get('image'))

#ask about the max issue with image brightness, replicate?




#moon-
#use local time
#maximum value is really high, maybe use 90th percentile, use plenty of different percentile




#print(len(data['time']))
#for i in data['time']:
    #print(i.time)


