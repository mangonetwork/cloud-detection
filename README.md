This project is designed to classify images from the [MANGO ASI Network](https://data.mangonetwork.org/data/transport/mango/archive/) as either cloudy or clear.

Input data is processed through a 2D Fourier Transform to extract its most significantly-correlated features, and the data is then fed to the model for classification.

Presently the algorithm is only trained on raw images.  Categorizing processed data files is done by identifying the corresponding raw image.

# Installation

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

# Usage

Simple identification of clouds for a single file is done with the `check_cloudy` module.  For this module, returned values of `True` indicate clouds have been detected and `False` indicates clouds are not detected and the image in probably clear.

## Raw File
```
from mangonetwork.clouddetect import check_cloudy
cloudy = check_cloudy.rawfile(filename)
```

## Processed File
```
from mangonetwork.clouddetect import check_cloudy
cloudy = check_cloudy.processedfile(filename)
```
Note that the `processedfile` function works by identifing the coresponding raw files and running them through the regression algorithm.  If the optional argument `raw_mango_dir` it provided, it will look for these files locally. Otherwise, it will stream the raw files from the [MANGO database website](https://data.mangonetwork.org/data/transport/mango/archive/).  This is VERY slow.

## makePrediction Module
More flexible functionality is available directly from the `makePrediction` module.  It can take as input either the name of a file, the url to an image, or a 2D array of pixel brightnes.  Examples of each are shown.

### filename Input
```
from mangonetwork.clouddetect.makePrediction import makePrediction

res = makePrediction(filename='mango-mro-greenline-20230821-032000.hdf5')
```

### URL Input
```
from mangonetwork.clouddetect.makePrediction import makePrediction

res = makePrediction(url='https://data.mangonetwork.org/data/transport/mango/archive/mro/greenline/raw/2023/233/03/mango-mro-greenline-20230821-032000.hdf5')
```

### Array Input
```
from mangonetwork.clouddetect.makePrediction import makePrediction
import h5py

with h5py.File('mango-mro-greenline-20230821-032000.hdf5', 'r') as f:
    arr = f['image'][:]
res = makePrediction(dataArray=arr)
```


