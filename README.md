This project is designed to classify images from the [MANGO ASI Network](https://data.mangonetwork.org/data/transport/mango/archive/) as either cloudy or clear.

If you wish to use this project to classify a set of images, the function that explicitly classifies is makePrediction.makePrediction. It can either output `True` for a clear image, or `False` for a cloudy one.

Input data is processed through a 2D Fourier Transform to extract its most significantly-correlated features, and the data is then fed to the model for classification.

Presently this function ONLY works on raw images.

Installation
============

This package can be installed with pip, but is not currently available on PyPI.

To install directly from GitHub:
```
pip install git+https://github.com/mangonetwork/cloud-detection.git
```

To clone a copy of the repository and then install:
```
git clone https://github.com/mangonetwork/cloud-detection.git
cd cloud-detection
pip install .
```

Usage
=====

The prediction function `makePrediction` is used to determine if an image is cloudy or not.  It can take as input either the name of a file, the url to an image, or a 2D array of pixel pbrightnes.  Examples of each are shown.

filename Input
--------------
```
from mangonetwork.clouddetect.makePrediction import makePrediction

res = makePrediction(filename='mango-mro-greenline-20230821-032000.hdf5')
```

URL Input
---------
```
from mangonetwork.clouddetect.makePrediction import makePrediction

res = makePrediction(url='https://data.mangonetwork.org/data/transport/mango/archive/mro/greenline/raw/2023/233/03/mango-mro-greenline-20230821-032000.hdf5')
```

Array Input
-----------
```
from mangonetwork.clouddetect.makePrediction import makePrediction
import h5py

with h5py.File('mango-mro-greenline-20230821-032000.hdf5', 'r') as f:
    arr = f['image'][:]
res = makePrediction(dataArray=arr)
```


