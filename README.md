This project is designed to classify greenline images of the type seen on https://data.mangonetwork.org/data/transport/mango/archive/

If you wish to use this project to classify a set of images, the function that explicitly classifies is makePrediction.makePrediction. It can either out 'Y' for a clear image, or 'N' for a cloudy one.

Data can be passed into makePrediction as either a url leading to an hdf5 file or a 2D array of pixel brightnesses
