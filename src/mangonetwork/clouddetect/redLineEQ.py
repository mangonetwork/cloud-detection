import getUrls
import makePrediction
import requests as rqs #urls from website
import matplotlib as mp
import matplotlib.pyplot as plt
import pandas as pd
import math
import numpy as np
import csv
import h5py as h5 # hdf5 files - large files compact
import shutil as sh
import os as os
from PIL import Image, ImageDraw
import math
import scipy
from scipy.stats import spearmanr
import GetVals
import pandas as pd
bigDF = pd.DataFrame()
right = 0
wrong = 0
urls = [url for url in getUrls.getURL() if url[0][59:62] == 'cfs']
redLines = []
bidDf = pd.DataFrame()
counter = 0
urlList = []
for url in urls:
    res = url[1]
    url = url[0]
    url = url[0:63] + 'red' + url[68:]
    url = url[0:97] + 'red' + url[102:]
    r = rqs.get(url, stream=True)
    if r.status_code == 404:
        char = int(url[117])
        if char == 8:
            char -= 2
        else:
            char += 2
        url = url[:117] + str(char) + url[118:]
    urlList.append([url, res])
#print(urlList)
for lst in urlList:
    
    letter = lst[1]
    #print(lst[0])

        #vals is the function that analyses each image and calculates each relevant feature
   # print(lst[0])
    vals = GetVals.func(bigDF, lst[0])
    #print(vals)
    lst[1] = vals[0]
    lst.append(vals[1])
    lst.append(vals[2])
    lst.append(vals[3])
    lst.append(vals[4])
    lst.append(letter)
    #print(lst)
       # this block writes the results to the brightness data csv file where all relevant stats are kept
    with open('Brightness_Data_Copy_Reds.csv', 'w', newline='') as myfile:
        wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
        wr.writerow(lst)
    

df = pd.DataFrame(urlList, columns=['URL', 'Median', '90th Percentile', 'Mean', 'versions', 'version2', 'ClearSky'])
df.to_csv("./Brightness_Data_Copy_Reds.csv", sep = ',', index = False)
data = pd.read_csv("Brightness_Data_Copy_Reds.csv") #load the existing csv into a data variable

x = data.drop(['ClearSky'], axis=1) #drop the classification column from the dataset 
urlCol = x['URL'] 
x = x.drop(['URL'], axis = 1) #drop the url column from the dataset
y = data['ClearSky'] #save the classification column as a variable
newList = []
for q in range(len(y)):
    if y[q] == 'N':
        newList.append(0)
    else:
        newList.append(1)

res =[]
for d in range(len(bigDF.index)):
    b = bigDF.iloc[d].to_numpy()
    #print(b)
    #print(np.corrcoef(newList, b))
    if np.corrcoef(newList, b)[0][1] <= -0.60:
         print(d)
    res.append(np.corrcoef(newList, b)[0][1])
print(res.index(max(res)))

#atmospheric science motivated (all-sky images) red and green airglow, need for automated analysis, we sought to develpop a ml algo to classify clear and claud y, add results
#redline integration is 1.1
#have a maybe output (confidence interval)
#debug redline (priority)
#plot the greenline/redline pairs to check if they're the same


#add two minutes to each redline image
