

from src.dataset.data_reader import XDFDataReader
import pdb

filepaths  = [
    '/home/owaismujtaba/projects/VowelStuday/Data/sub-1PilotoDan/ses-S002/eeg/sub-1PilotoDan_ses-S002_task-Default_run-001_eeg.xdf',
    '/home/owaismujtaba/projects/VowelStuday/Data/sub-2Piloto/ses-S001/eeg/sub-2Piloto_ses-S001_task-Default_run-001_eeg.xdf',
    '/home/owaismujtaba/projects/VowelStuday/Data/sub-2Piloto/ses-S002/eeg/sub-2Piloto_ses-S002_task-Default_run-001_eeg.xdf',
    '/home/owaismujtaba/projects/VowelStuday/Data/sub-P003/ses-S001/eeg/sub-P003_ses-S001_task-Default_run-001_eeg.xdf',
    '/home/owaismujtaba/projects/VowelStuday/Data/sub-P003/ses-S001/eeg/sub-P003_ses-S001_task-Default_run-001_eeg.xdf',
    '/home/owaismujtaba/projects/VowelStuday/Data/sub-P004/ses-S001/eeg/sub-P004_ses-S001_task-Default_run-001_eeg.xdf',
    '/home/owaismujtaba/projects/VowelStuday/Data/sub-P004/ses-S002/eeg/sub-P004_ses-S002_task-Default_run-001_eeg.xdf',
    '/home/owaismujtaba/projects/VowelStuday/Data/sub-P005/ses-S001/eeg/sub-P005_ses-S001_task-Default_run-001_eeg.xdf',
    '/home/owaismujtaba/projects/VowelStuday/Data/sub-P005/ses-S002/eeg/sub-P005_ses-S002_task-Default_run-001_eeg.xdf',
    '/home/owaismujtaba/projects/VowelStuday/Data/sub-P006/ses-S001/eeg/sub-P006_ses-S001_task-Default_run-001_eeg.xdf',
    '/home/owaismujtaba/projects/VowelStuday/Data/sub-P006/ses-S002/eeg/sub-P006_ses-S002_task-Default_run-001_eeg.xdf'
]

for filepath in filepaths:
    sub = '01'
    ses = '01'
    xdf_reader = XDFDataReader(
        filepath=filepath,
        sub_id=sub,
        ses_id=ses
    )
    pdb.set_trace()