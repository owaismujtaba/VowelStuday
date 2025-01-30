import os
import pandas as pd
from pathlib import Path
from mne_bids import BIDSPath

import config as config
from src.utils.graphics import styled_print
from src.dataset.utils import eeg_markers_setup

import pdb

class BIDSDataset:
    def __init__(self, xdf_reader):
        styled_print("🚀", "Initializing BIDSDataset Class", "yellow", panel=True)
        self.xdf_reader = xdf_reader
        self.sub_id = xdf_reader.sub_id
        self.ses_id = xdf_reader.ses_id
        self.eeg = xdf_reader.eeg
        self.filename = f'sub-{self.sub_id}_ses-{self.ses_id}_VowelStudy_run-01'
        self.markers = None
        self._ensure_directories()
        self.__eeg_markers_setup()
        self._save_markers_info()

    def __eeg_markers_setup(self):
        annotations = self.eeg.annotations
        onset, descriptions = [], []

        for event in annotations:
            onset.append(event['onset'])
            descriptions.append(event['description'])
        markers  = {'onset':onset, 'description':descriptions}
        markers = pd.DataFrame(markers)
        self.markers = eeg_markers_setup(markers)

    def _save_markers_info(self):
        destination = Path(config.CURR_DIR, 'MetaData')
        filename = self.filename + 'markers_meata_data.csv'
        filepath = Path(destination, filename)
        try:
            self.markers.to_csv(filepath)
        except :
            print('Error saving markers meta data')
    
    def _ensure_directories(self):
        self.root = config.BIDS_DIR
        self.bids_path = BIDSPath(
            subject=self.sub_id, session=self.ses_id,
            task='VowelStudy', run='01', datatype='eeg',
            root=self.root
        )

        destination_dir = Path(
            self.root, f'sub-{self.sub_id}',
            f'ses-{self.ses_id}'
        )
        os.makedirs(destination_dir, exist_ok=True)

