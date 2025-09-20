import pandas as pd
#import numpy as np
#import seaborn as sns
#import matplotlib.pyplot as plt
#from sklearn.model_selection import train_test_split
#from sklearn import metrics
from sklearn.linear_model import LogisticRegression
from sklearn.exceptions import ConvergenceWarning
#from sklearn.neighbors import KNeighborsClassifier
#import .getUrls
from .GetVals import func
#import csv
#from sklearn.inspection import DecisionBoundaryDisplay
#from sklearn import neighbors, datasets
#from matplotlib.colors import ListedColormap
#import math
#from sklearn.linear_model import LogisticRegression
#from sklearn import preprocessing
#from sklearn import svm
#from ast import literal_eval
#from sklearn.metrics import ConfusionMatrixDisplay
#from sklearn.metrics import confusion_matrix
#import heapq
#from sklearn.metrics import RocCurveDisplay
#from sklearn.preprocessing import LabelBinarizer
import warnings
import sys
if sys.version_info < (3, 9):
    import importlib_resources as resources
else:
    from importlib import resources



def makePrediction(filename=None, url=None, dataArray=None):
    # Something in here spits out a bunch of warnings - silence them?
    name = "Brightness_Data_Copy.csv"
    csv_filename = resources.files("mangonetwork.clouddetect.data").joinpath(name)
    data = pd.read_csv(csv_filename) #load the existing csv into a data variable

    x = data.drop(['ClearSky'], axis=1) #drop the classification column from the dataset 
    urlCol = x['URL'] 
    x = x.drop(['URL'], axis = 1) #drop the url column from the dataset
    y = data['ClearSky'] #save the classification column as a variable
    cw = {'Y': 0.9, 'N': 1.5} #Create the classification weights and fit

    logr = LogisticRegression(class_weight=cw)

    # Supress ConvergenceWarning - may need to be rechecked
    with warnings.catch_warnings():
        warnings.simplefilter("ignore", category=ConvergenceWarning)
        logr.fit(x, y)

    vals = func(filename, url, arr = dataArray) #get the features for the desired url/array

    # Supress UserWarning - may need to be rechecked
    with warnings.catch_warnings():
        warnings.simplefilter("ignore", category=UserWarning)
        res = logr.predict([vals]) #predict cloudy or clear
    
    if res[0] == 'Y':
        return True
    else:
        return False

#makePrediction(url = 'https://data.mangonetwork.org/data/transport/mango/archive/mro/greenline/raw/2023/233/03/mango-mro-greenline-20230821-032000.hdf5')
