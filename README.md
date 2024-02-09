This project is designed to classify greenline images of the type seen on https://data.mangonetwork.org/data/transport/mango/archive/

If you wish to use this project to classify a set of images, the function that explicitly classifies is makePrediction.makePrediction. It can either output 'Y' for a clear image, or 'N' for a cloudy one.

Data can be passed into makePrediction as either a url leading to an hdf5 file or a 2D array of pixel brightnesses

The makePrediction file reference data from the urls in getURLs.py whcih have been used to train a logistic regression machine learning model.

Input data is processed through a 2D Fourier Transform in GetVals.py to extract its most significantly-correlated features, and the data is then fed to the model for classification.