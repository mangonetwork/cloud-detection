# check_cloudy.py
import datetime as dt
import h5py
from .makePrediction import makePrediction

def rawfile(filename):
    """
    Determine if image is cloudy or not from a single raw MANGO file.

    Input
    -----
    filname : str
        Path to a local raw MANGO datafile.
    
    Output
    ------
    cloudy : bool
        True = image is cloudy; False = image is clear
        
    """

    with h5py.File(filename, 'r') as h5:
        instrument = h5['image'].attrs['instrument']

    res = makePrediction(instrument, filename=filename)

    if res == 'Y':
        return False
    else:
        return True



def processedfile(filename, raw_mango_dir=None):
    """Check if each image is cloudy or not"""

    with h5py.File(filename) as h5:
        station = h5["ImageData"].attrs["station"]
        instrument = h5["ImageData"].attrs["instrument"]
        utime = h5["UnixTime"][0,:]

    cloudy = list()
    for ut in utime:
        time = dt.datetime.utcfromtimestamp(ut)
        raw_filename = f'{station}/{instrument}/raw/{time:%Y/%j/%H}/mango-{station}-{instrument}-{time:%Y%m%d-%H%M%S}.hdf5'
        if raw_mango_dir:
            raw_filepath = os.path.join(raw_mango_dir, raw_filename)
            res = makePrediction(instrument, filename=raw_filepath)
        else:
            base_url = 'https://data.mangonetwork.org/data/transport/mango/archive/'
            url = base_url+raw_filename
            res = makePrediction(instrument, url=url)
        if res == 'Y':
            cloudy.append(False)
        else:
            cloudy.append(True)

    return cloudy
