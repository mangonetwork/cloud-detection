# check_cloudy.py
# Note that this module retuns True for cloudy images adn False for clear images
# This is the inverse of makePrediction, which returns Y for clear images and N for cloudy imagges
import os
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

    res = makePrediction(filename=filename)

    if res == 'Y':
        return False
    else:
        return True


def stationtime(station, instrument, time):
    """
    Determine if image is cloudy or not based on a particular camera and time.

    Input
    -----
    station : str
        Three-letter station code
    instrument: str
        Instrument (either 'greenline' or 'redline')
    time : datetime.datetime
        Time
    
    Output
    ------
    cloudy : bool
        True = image is cloudy; False = image is clear
        
    """

    raw_filename = f'{station}/{instrument}/raw/{time:%Y/%j/%H}/mango-{station}-{instrument}-{time:%Y%m%d-%H%M%S}.hdf5'
    base_url = 'https://data.mangonetwork.org/data/transport/mango/archive/'
    url = base_url+raw_filename

    res = makePrediction(url=url)

    if res == 'Y':
        return False
    else:
        return True


def processedfile(filename, raw_mango_dir=None):
    """Check if each image is cloudy or not"""

    print(filename)

    with h5py.File(filename) as h5:
        print(h5["ImageData"])
        station = h5["ImageData"].attrs["Station"]
        instrument = h5["ImageData"].attrs["Instrument"]
        utime = h5["UnixTime"][:,0]

    cloudy = list()
    for ut in utime:
        time = dt.datetime.utcfromtimestamp(ut)
        raw_filename = f'{station}/{instrument}/raw/{time:%Y/%j/%H}/mango-{station}-{instrument}-{time:%Y%m%d-%H%M%S}.hdf5'
        if raw_mango_dir:
            raw_filepath = os.path.join(raw_mango_dir, raw_filename)
            res = makePrediction(filename=raw_filepath)
        else:
            base_url = 'https://data.mangonetwork.org/data/transport/mango/archive/'
            url = base_url+raw_filename
            res = makePrediction(url=url)
        if res == 'Y':
            cloudy.append(False)
        else:
            cloudy.append(True)

    return cloudy
