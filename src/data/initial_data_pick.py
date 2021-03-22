import os
from pathlib import Path
import pandas as pd
import numpy as np
from skimage.io import imread
from PIL import Image
from PIL.ExifTags import TAGS
# =============================================================================
# αυτός ο κώδικας μεταφέρει όλα τα δεδομένα data/raw στο φάκελο data/interim
# με τις επεξεργασίες τους να είναι:
#     IR_*.jpg    --> IR_ = cut IR_*[:, 100:260]
#     CSV_*.csv   --> fix --> cut [:, 100:260]
#     DC_*.jpg    --> cut centered[IR_]

# Στάδια που δουλεύει:
# 1. Αρχικοποίηση: 
#     iteration  0
#     Root: C:\Users\plouk\Adiposer\data\raw
#     DIRs: ['0h', '120h', '144h', '192h', '240h', '24h', '48h', '72h', '96h']
#     
#     Action: πήγαινε στο INTERIM_DIR και os.mkdir(DIRs)
#     
# 2. Ορισμός Ποντικίων για εκείνη την ώρα
#     iteration  1
#     Root: C:\Users\plouk\Adiposer\data\raw\0h
#     DIRs: ['Mouse1', 'Mouse2', 'Mouse3', 'Mouse4', 'Mouse5']
#     
# 3. Πέντε Ποντίκια
#     iteration  2
#     Root: C:\Users\plouk\Adiposer\data\raw\0h\Mouse1
#     DIRs: []
#     iteration  3
#     Root: C:\Users\plouk\Adiposer\data\raw\0h\Mouse2
#     DIRs: []
#     iteration  4
#     Root: C:\Users\plouk\Adiposer\data\raw\0h\Mouse3
#     DIRs: []
#     iteration  5
#     Root: C:\Users\plouk\Adiposer\data\raw\0h\Mouse4
#     DIRs: []
#     iteration  6
#     Root: C:\Users\plouk\Adiposer\data\raw\0h\Mouse5
#     DIRs: []
# =============================================================================


def _readable_EXIF(exifdata):
    exifList = []
    try:
        # iterating over all EXIF data fields
        for tag_id in exifdata:
            # get the tag name, instead of human unreadable tag id
            tag = TAGS.get(tag_id, tag_id)
            data = exifdata.get(tag_id)
            # decode bytes 
            if isinstance(data, bytes):
                data = data.decode()
            exifList.append(f"{tag:25}: {data}")
    except UnicodeDecodeError:
        return exifList
    return exifList

def _IR_fixer(fpath, fname):
# =============================================================================
#     fname: δέχεται το path του csv 
#     επιστρέφει τα δεδομένα σειριακά
# =============================================================================
    print(f'IR fixer ---------- accessing {fname} -------------')
    image = imread(fpath, as_gray=True)
    exif = _readable_EXIF(Image.open(fpath).getexif())
    return image[:, 100:260].flatten(), exif
    
def _DC_fixer(fpath, fname):
# =============================================================================
#     fname: δέχεται το path της jpeg εικόνας DC
#     επιστρέφει τα δεδομένα σειριακά σε συμφωνία με την infrared 
# =============================================================================
    print(f'DC fixer ---------- accessing {fname} -------------')
    image = imread(fpath, as_gray=True)
    image.shape
    # Image.open(imagePath).getexif())
    
def _CSV_fixer(fpath, fname):
# =============================================================================
#     fname: δέχεται το path του csv με τις θερμοκρασίες 
#     επιστρέφει στήλη «actual» με μέγεθος 
# =============================================================================
    print(f'CSV fixer ---------- accessing {fname} -------------')
#     άμα sep = 'κενό,' τότε φτιάνει δίστηλο frame
#     άμα sep = 'κενό' τότε φτιάνει τετράστηλο  frame
    dataF = pd.read_csv(filepath_or_buffer=fpath, sep=' ,', engine='python')
    columnNames = dataF.columns
#     μόνο η πρώτη στήλη με το περίεργο όνομα έχει τις θερμοκρασίες
#     firstColumn type: pandas Series
    dataColumn = dataF[columnNames[0]] # ας δούμε το πρώτο που έχει τη λέξη Frame 1 στην αρχή 
    firstLine = dataColumn[0]          # ειναι string, κάτι θα κάνουμε οπότε 
    # 320 ειναι τα κόμματα κάτι που ισχύει και για τα υπόλοιπα 
    rawData = np.fromstring(firstLine[8:], dtype=float, sep=',') # εδώ υπάρχει η λέξη 'Frame 1,' την διώχνουμε
    # τα επόμενα ξεκινάνε με κόμμα, οπότε για τα επόμενα 239 θα κάνουμε το ίδιο
    for i in range(1, dataF.shape[0]):
        dataStringLine = dataColumn[i]
        rawData = np.vstack((rawData, np.fromstring(dataStringLine[1:], dtype=float, sep=',')))
    """ sensor_data = dict.fromkeys(['Mouse1', 'Mouse2', 'Mouse3', 'Mouse4', 'Mouse5'])
        csv_files = sorted(glob(CWD + '/dataset/WAT/Mouse1/CSV_*.csv'))
        for sampleHour, file in zip(hours, csv_files):
            data_dictionary[sampleHour] = _data_fixer(file)
        sensor_data['Mouse1'] = data_dictionary """
    return rawData[:, 100:260].flatten() 
    

def process_targets(target_file_list, raw_files):
    # τελικό σχήμα (240, 160) = 38.400 flattened δείγματα 
    # δημιουργία τρίστηλου CSV: infrared, optical και actual

    count = 0
    print('******** Processing Targets **************')
    for (file, path) in zip(raw_files, target_file_list):
        if file.startswith('IR_'):
            if os.path.isfile(path):
                print('Processing ' + file)
                result = _IR_fixer(path, file)
                count += 1
        if file.startswith('DC_'):
            if os.path.isfile(path):
                print('Processing ' + file)
                result = _DC_fixer(path, file)
                count += 1
        if file.startswith('CSV_'):
            if os.path.isfile(path):
                print('Processing ' + file)
                result = _CSV_fixer(path, file)

                count += 1
    print(f'***** Finished Processing {count} Targets **********')

HERE = Path(__file__)
SRC_DIR = HERE.parent.parent
PROJECT_DIR = SRC_DIR.parent
RAW_DIR = PROJECT_DIR / "data" / "raw"
INTERIM_DIR = PROJECT_DIR / "data" / "interim"
mode = 0o755

if os.path.exists(RAW_DIR):
    # raw_root : string of a POSIX-style directory
    # raw_dirs : list of subdirectories 
    # raw_files: list of filenames in the directory
    processed_files = 0

    for i, (raw_root, raw_dirs, raw_files) in enumerate(os.walk(RAW_DIR)):
        print('iteration #', i)
        print('Root: ' + raw_root)
        print('DIRs: ' + str(raw_dirs))
        
        # 1. Αρχικοποίηση:
        if i == 0:
            print('******** Initialized data/interim directory **************')
            [os.mkdir(INTERIM_DIR / directory, mode) for directory in raw_dirs]
        elif len(raw_dirs) == 0: # 3. Πέντε Ποντίκια
            print('========> {} Files Found at {} '.format(str(len(raw_files)), raw_root))
            full_path_target = [raw_root + '/' + raw_file for raw_file in raw_files]
            process_targets(full_path_target, raw_files)
            
        raw_root_path = Path(raw_root)
        data_path = raw_root_path.parent
        # if str(data_path).endswith('raw'):
        #   os.mkdir(path, mode)
            
        # print('making dir at interim ' + str(raw_root_path.parent))
        # dirs_path = Path(dirs)
else:
    ValueError("Raw dataset doesn't exist")
        
