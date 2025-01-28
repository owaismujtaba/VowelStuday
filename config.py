import os
import shutil
from pathlib import Path


TERMINAL_WIDTH = shutil.get_terminal_size().columns

CURR_DIR = os.getcwd()
RAW_DATA_DIR = Path(CURR_DIR, 'Data')

