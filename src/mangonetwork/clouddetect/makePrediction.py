import pandas as pd
import requests as rqs #urls from website
import h5py as h5 # hdf5 files - large files compact
import shutil as sh
from sklearn.linear_model import LogisticRegression
from sklearn.exceptions import ConvergenceWarning
from .GetVals import feature_vector
import warnings
import sys
import os
if sys.version_info < (3, 9):
    import importlib_resources as resources
else:
    from importlib import resources

# NOTE: Block notations may not be accurate - LL 2025-09-22

def makePrediction(instrument, filename=None, url=None, dataArray=None):

    # Load Training Data
    if instrument == 'greenline':
        name = "Brightness_Data_Copy.csv"   # Dependent on red or green
    else:
        name = "Brightness_Data_Copy_Red.csv"   # Dependent on red or green
    csv_filename = resources.files("mangonetwork.clouddetect.data").joinpath(name)
    data = pd.read_csv(csv_filename) #load the existing csv into a data variable

    # Organize Training Data
    x = data.drop(['ClearSky'], axis=1) #drop the classification column from the dataset 
    urlCol = x['URL'] 
    x = x.drop(['URL'], axis = 1) #drop the url column from the dataset
    y = data['ClearSky'] #save the classification column as a variable
    cw = {'Y': 0.9, 'N': 1.5} #Create the classification weights and fit

    # Initialize Regression Class
    logr = LogisticRegression(class_weight=cw)

    # Training
    # Supress ConvergenceWarning - may need to be rechecked
    with warnings.catch_warnings():
        warnings.simplefilter("ignore", category=ConvergenceWarning)
        logr.fit(x, y)      # Does this retrain the ML every time??
        # This may actually prevent the output from being fully deterministic.

    # Load Image for Prediction
    if filename:    #if the input is a filename, load teh image and lable it as arr
        file = h5.File(filename, 'r')
        arr = file['image'] #array of values
    elif url:   #if the input is a URL, retrieve the image data and label it as arr
        r = rqs.get(url, stream=True)
        dump = r.raw
        cwd = os.getcwd()   # Messy, especially if you're not deleting the file afterwards
        location = os.path.abspath(cwd)
        with open('tempfile.hdf5', 'wb') as location:
            sh.copyfileobj(dump, location)
        file = h5.File('tempfile.hdf5', 'r+')
        arr = file['image'] #array of values
    else:
        arr = np.array(arr)


    # Find Feature Vector
    vals = feature_vector(arr) #get the features for the desired url/array

    # Prediction
    # Supress UserWarning - may need to be rechecked
    with warnings.catch_warnings():
        warnings.simplefilter("ignore", category=UserWarning)
        res = logr.predict([vals]) #predict cloudy or clear
    
    return res
#    if res[0] == 'Y':
#        return True     # clear
#    else:
#        return False    # cloudy

#makePrediction(url = 'https://data.mangonetwork.org/data/transport/mango/archive/mro/greenline/raw/2023/233/03/mango-mro-greenline-20230821-032000.hdf5')
