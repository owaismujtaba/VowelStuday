import os
import shutil
from pathlib import Path


# Directories 
CURR_DIR = os.getcwd()
RAW_DATA_DIR = Path(CURR_DIR, 'Data')
BIDS_DIR = Path(CURR_DIR, 'BIDS')

# Raw XDF Parameters
EEG_SR = 1000
AUDIO_SR = 48000

# Preprocessing Parameters
NOTCH_FREQ = [50, 100]
LOW_FREQ = 0.5
HIGH_FREQ = 170
