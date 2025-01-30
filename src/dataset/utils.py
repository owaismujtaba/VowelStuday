


def eeg_markers_row_setup(row):
    # Start/End column
    if 'Start' in row['description']:
        row['Start/End'] = 'Start'
    elif 'End' in row['description']:
        row['Start/End'] = 'End'
    else:
        row['Start/End'] = ''
   
    # Covert/Overt column
    if 'Covert' in row['description']:
        row['Covert/Overt'] = 'Covert'
    else:
        row['Covert/Overt'] = 'Overt'
   
    # Fixation/Stimulus/ISI/ITI/Speech column
    if 'Fixation' in row['description']:
        row['Fixation/Stimulus/ISI/ITI/Speech'] = 'Fixation'
    elif 'Stimulus' in row['description']:
        row['Fixation/Stimulus/ISI/ITI/Speech'] = 'Stimulus'
    elif 'ISI' in row['description']:
        row['Fixation/Stimulus/ISI/ITI/Speech'] = 'ISI'
    elif 'ITI' in row['description']:
        row['Fixation/Stimulus/ISI/ITI/Speech'] = 'ITI'
    elif 'Speech' in row['description']:
        row['Fixation/Stimulus/ISI/ITI/Speech'] = 'Speech'
    else:
        row['Fixation/Stimulus/ISI/ITI/Speech'] = ''
   
    vowel_info = ''
    # Extract vowel info from the description if applicable
    if 'Vowel' in row['description'] and 'Fixation' in row['description']:
        vowel_info = row['description'].split('Vowel')[1]
        
    elif 'Vowel' in row['description'] and 'Target' in row['description']:
        vowel_info = row['description'].split('Vowel')[1]
    elif 'Vowel' in row['description'] and 'Speech' in row['description']:
        vowel_info = row['description'].split('Vowel')[1]
     

    else:
        pass
    if ':' in vowel_info:
        vowel_info = vowel_info.split(':')[1]
    row['Vowel'] = vowel_info
    
    return row


def eeg_markers_setup(markers):
    markers = markers.apply(eeg_markers_row_setup, axis=1)
    markers['Vowel'] = markers['Vowel'].where(markers['Vowel'] != '', other=None)
    markers['Vowel'] = markers['Vowel'].fillna(method='bfill')

    return markers