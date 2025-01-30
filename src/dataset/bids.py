import os
import pandas as pd
from pathlib import Path
from mne.annotations import Annotations
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
        
        self.preprocess_eeg()

        self._ensure_directories()
        self.__eeg_markers_setup()
        self._save_markers_info()
        self._annotations_eeg_setup()


    def _annotations_eeg_setup(self):
        annotations = self.markers
        annotations = annotations[annotations['Start/End']=='Start']
        onsets = annotations['onset'].values
        descriptions = annotations['markers'].values
        self.annotations = Annotations(
            onset=onsets, 
            duration=[0] * len(onsets), 
            description=descriptions
        )



    def __bids_info_setup(self):
        self.ch_names = self.eeg.ch_names

    def preprocess_eeg(self):
        self.eeg = self.eeg.resample(config.EEG_SR)
        self.eeg.notch_filter(config.NOTCH_FREQ, fir_design='firwin')
        self.eeg.filter(
            l_freq=config.LOW_FREQ, h_freq=config.HIGH_FREQ,
            fir_design='firwin'
        )
        

    def create_bids_file(self):
        eeg_data = self.eeg.get_dat()

    def __eeg_markers_setup(self):
        styled_print("🧠", "Extracting EEG Markers...", "blue")
        
        annotations = self.eeg.annotations
        onset, descriptions = [], []

        for event in annotations:
            onset.append(event['onset'])
            descriptions.append(event['description'])
        
        markers = pd.DataFrame({'onset': onset, 'description': descriptions})
        
        markers = eeg_markers_setup(markers)
        markers = markers.dropna(axis=0)
        markers = markers[~markers.apply(lambda row: any(cell == '' for cell in row), axis=1)]
        markers['markers'] = markers.iloc[:, 2:].astype(str).agg('_'.join, axis=1)
        
        self.markers = markers
        
        styled_print("✅", "EEG Markers Setup Complete!", "green")

    def _save_markers_info(self):
        styled_print("💾", "Saving Markers Metadata...", "magenta")

        destination = Path(config.CURR_DIR, 'MetaData')
        os.makedirs(destination, exist_ok=True)
        filename = self.filename + '_markers_meta_data.csv'
        filepath = Path(destination, filename)
        try:
            self.markers.to_csv(str(filepath))
            styled_print("✅", f"Markers Metadata Saved: {filename}", "green")
        except Exception as e:
            styled_print("⚠️", f"Error saving markers metadata: {str(e)}", "red", panel=True)

    def _ensure_directories(self):
        styled_print("📂", "Ensuring BIDS Directory Structure...", "cyan")

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
        styled_print("✅", f"Directories Created: {destination_dir}", "green")
