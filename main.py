

from src.dataset.data_reader import XDFDataReader

filepath = r'C:\DeepRESTORE\VowelStuday\Data\sub-01\ses-S001\eeg\sub-1PilotoDan_ses-S001_task-Default_run-001_eeg.xdf'
sub = '01'
ses = '01'
xdf_reader = XDFDataReader(
    filepath=filepath,
    sub_id=sub,
    ses_id=ses
)