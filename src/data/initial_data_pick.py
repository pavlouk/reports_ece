import os
from pathlib import Path
import pandas as pd
import numpy as np
from skimage.io import imread
from PIL import Image
from PIL.ExifTags import TAGS
import re 
# =============================================================================
# αυτός ο κώδικας μεταφέρει όλα τα δεδομένα data/raw στο φάκελο data/interim
# με τις επεξεργασίες τους να είναι: (240, 160)
#     IR_*.jpg    --> IR_ = cut IR_*[:, 100:260]
#     CSV_*.csv   --> fix --> cut [:, 100:260]
#     DC_*.jpg    --> cut centered[IR_]

# Στάδια: τι συμβαίνει μέσα σε ένα os.walk
# 1. Αρχικοποίηση: 
#     iteration  0
#     Root: C:\Users\plouk\Adiposer\data\raw
#     DIRs: ['0h', '120h', '144h', '192h', '240h', '24h', '48h', '72h', '96h'] => len = 9
#     
#     Action: πήγαινε στο INTERIM_DIR και os.mkdir(DIRs)
#     
# 2. Ορισμός directories για εκείνη την ώρα:
#     iteration  1
#     Root: C:\Users\plouk\Adiposer\data\raw\0h                                 parent = raw, os.dirname(root) = '0h'
#     DIRs: ['Mouse1', 'Mouse2', 'Mouse3', 'Mouse4', 'Mouse5']                 => len = 5 
#     
#     Action: πήγαινε στο INTERIM_DIR / "0h" και os.mkdir(DIRs)

# 3. Πέντε Ποντίκια
#     iteration  2, 3, 4, 5 
#     Root: C:\Users\plouk\Adiposer\data\raw\0h\Mouse1, 2, 3, 4, 5
#     DIRs: []                                                                 => len = 0
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
#     fname: δέχεται το path της jpeg εικόνας ΙR
#     επιστρέφει τα δεδομένα σειριακά δεδομένα εικόνας (240, 160) = 38.400
# =============================================================================
    # print(f'IR fixer ---------- accessing {fname} -------------')
    image = imread(fpath, as_gray=True)
    exif = _readable_EXIF(Image.open(fpath).getexif())
    return image[:, 100:260].flatten(), exif
    
def _DC_fixer(fpath, fname):
# =============================================================================
#     fname: δέχεται το path της jpeg εικόνας DC
#     επιστρέφει τα δεδομένα σειριακά σε συμφωνία με την infrared (240, 160) = 38.400
# =============================================================================
    # print(f'DC fixer ---------- accessing {fname} -------------')
    image = imread(fpath, as_gray=True)
    image.shape
    
def _CSV_fixer(fpath, fname):
# =============================================================================
#     fname: δέχεται το path του csv με τις θερμοκρασίες 
#     επιστρέφει σειριακά δεδομένα θερμοκρασιών μεγέθους (240, 160) = 38.400
# =============================================================================
    # print(f'CSV fixer ---------- accessing {fname} -------------')
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
        
    return rawData[:, 100:260].flatten() 
    

def process_targets(target_file_list, raw_files):
    # τελικό σχήμα (240, 160) = 38.400 flattened δείγματα 
    # δημιουργία τρίστηλου CSV: infrared, optical και actual
    # βγάζω τα unique ids από τη λίστα raw_files
    pattern = re.compile("[0-9][0-9][0-9][0-9]")
    ids = [pattern.findall(content) for content in raw_files]
    
    count = 0
    print(f'******** Processing {len(raw_files)} Targets **************')
    # τα targets έχουν τις μορφές: 
    # IR_{id}.jpg, CSV_{id}.csv και DC_{id + 1}.jpg
    # φτιάχνουμε αρχεία της μορφής sample_{id}.csv
    for (file, path) in zip(raw_files, target_file_list):
        if file.startswith('IR_'):
            # print('Processing ' + file)
            result = _IR_fixer(path, file)
            count += 1
        if file.startswith('DC_'):
            # print('Processing ' + file)
            result = _DC_fixer(path, file)
            count += 1
        if file.startswith('CSV_'):
            # print('Processing ' + file)
            result = _CSV_fixer(path, file)
            count += 1
    print(f'***** Finished Processing {count} Targets **********')
    return count 

HERE = Path(__file__)           # /src/data/file.py
SRC_DIR = HERE.parent.parent
PROJECT_DIR = SRC_DIR.parent
RAW_DIR = PROJECT_DIR / "data" / "raw"
INTERIM_DIR = PROJECT_DIR / "data" / "interim"
mode = 0o755
import re 
pattern = re.compile("[0-9][0-9][0-9][0-9]")
ids = [int(pattern.findall(content).pop()) for content in raw_files]
unique_ids = list(set(ids))
unique_ids.sort()
for u_id in unique_ids
if os.path.exists(RAW_DIR):
    # raw_root : string of a POSIX-style directory
    # raw_dirs : list of subdirectories 
    # raw_files: list of filenames in the directory
    processed_files = 0
    
    for i, (raw_root, raw_dirs, raw_files) in enumerate(os.walk(RAW_DIR)):
        print(f'iteration #{i}')
        print(f'             Root dir: {os.path.basename(raw_root)}')
        print(f'             DIR list: {str(raw_dirs)}')
        
        if len(raw_dirs) == 9: # 1. Αρχικοποίηση:
            print('******** Initialized /data/interim/[sample_hours] directories **************')
            [os.mkdir(INTERIM_DIR / directory, mode) for directory in raw_dirs]  # raw_dirs = ['0h', '120h', '144h', '192h', '240h', '24h', '48h', '72h', '96h']
        elif len(raw_dirs) == 5: # 2. Ορισμός 5 directories για εκείνη την ώρα:
            print('******** Creating /data/interim/[sample_hours]/[mouse_ids] directories **************')
            sample_name = os.path.basename(raw_root)
            [os.mkdir(INTERIM_DIR / sample_name / mouse_name) for mouse_name in ['mouse_1', 'mouse_2', 'mouse_3', 'mouse_4', 'mouse_5']]
        elif len(raw_dirs) == 0: # 3. Δεδομένα εικόνων 
            print(f'========> {len(raw_files)} Files Found at {raw_root}')
            full_path_target = [raw_root + '/' + raw_file for raw_file in raw_files]
            processed_files += process_targets(full_path_target, raw_files)
            
        print(f'------------ Total Processed Files {processed_files} ------------------')
else:
    ValueError("No dataset exists!!!")
        
