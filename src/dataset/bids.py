import os
from pathlib import Path
from mne_bids import BIDSPath

import config as config
from src.utils.graphics import print_section_header

class BIDSDataset:
    def __init__(self, eeg, sub_id='01', ses_id='01'):
        print_section_header("Initializing BIDSDataset Class")
        self.sub_id = sub_id
        self.ses_id = ses_id
        self.eeg = eeg
        self.filename = f'sub-{self.sub_id}_ses-{self.ses_id}_VowelStudy_run-01'
        self._ensure_directories()

    
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

        