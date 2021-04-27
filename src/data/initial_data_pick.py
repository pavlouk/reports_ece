import os
from pathlib import Path
import pandas as pd
import numpy as np
from skimage.io import imread
from PIL import Image
from PIL.ExifTags import TAGS
import re 
import shutil 
# =============================================================================
# αυτός ο κώδικας μεταφέρει όλα τα δεδομένα data/raw στο φάκελο data/interim
# με τις επεξεργασίες τους να είναι: (240, 160)
#     IR_*.jpg    --> IR_ = cut IR_*[:, 100:260]
#     CSV_*.csv   --> fix --> cut [:, 100:260]
#     DC_*.jpg    --> cut centered[IR_]
# 3. Πέντε Ποντίκια """return pd.DataFrame(rawData[:, 100:260].flatten()).to_csv(save_dir.as_posix() + '\/' + fname)"""
#     iteration  2, 3, 4, 5 
#     Root: C:\Users\plouk\Adiposer\data\raw\0h\Mouse1, 2, 3, 4, 5
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

def IR_fixer(fpath, fname):
# =============================================================================
#     fname: δέχεται το path της jpeg εικόνας ΙR
#     επιστρέφει τα δεδομένα σειριακά δεδομένα εικόνας (240, 160) = 38.400
# =============================================================================
    # print(f'IR fixer ---------- accessing {fname} -------------')
    image = imread(fpath, as_gray=True)
    exif = _readable_EXIF(Image.open(fpath).getexif())
    return image[:, 100:260], exif
    
def _DC_fixer(fpath, fname):
# =============================================================================
#     fname: δέχεται το path της jpeg εικόνας DC
#     επιστρέφει τα δεδομένα σειριακά σε συμφωνία με την infrared (240, 160) = 38.400
# =============================================================================
    # print(f'DC fixer ---------- accessing {fname} -------------')
    image = imread(fpath, as_gray=True)
    return image.shape
    
def CSV_fixer(fpath, fname, save_dir):
    # =============================================================================
    # fname: δέχεται το path του csv με τις θερμοκρασίες 
    # επιστρέφει σειριακά δεδομένα θερμοκρασιών μεγέθους (240, 160) = 38.400
    # =============================================================================
    # print(f'CSV fixer ---------- accessing {fname} -------------')
    # με sep = 'κενό,' τότε δίστηλο frame, με sep = 'κενό' τότε τετράστηλο frame
    dataF = pd.read_csv(filepath_or_buffer=fpath, sep=' ,', engine='python')
    columnNames = dataF.columns
    # μόνο η πρώτη στήλη με το Frame 1 έχει τις θερμοκρασίες
    # dataColumn type: pandas Series
    dataColumn = dataF[columnNames[0]] # ας δούμε το πρώτο που έχει τη λέξη Frame 1 στην αρχή 
    firstLine = dataColumn[0]          # string
    # 320 ειναι τα κόμματα κάτι που ισχύει και για τα υπόλοιπα 
    rawData = np.fromstring(firstLine[8:], dtype=float, sep=',') # εδώ υπάρχει η λέξη 'Frame 1,' την διώχνουμε
    # τα επόμενα ξεκινάνε με κόμμα, οπότε για τα επόμενα 239 θα κάνουμε το ίδιο
    for i in range(1, dataF.shape[0]):
        dataStringLine = dataColumn[i]
        rawData = np.vstack((rawData, np.fromstring(dataStringLine[1:], dtype=float, sep=',')))
        
    return rawData[:, 100:260]
    

def process_targets(target_file_list, raw_files, save_dir):
    # τελικό σχήμα (240, 160) = 38.400 flattened δείγματα 
    # δημιουργία τρίστηλου CSV: infrared, optical και actual
    # βγάζω τα unique ids από τη λίστα raw_files    
    count = 0
    print(f'******** Processing {len(raw_files)} Targets **************')
    # τα targets έχουν τις μορφές: 
    # IR_{id}.jpg, CSV_{id}.csv και DC_{id + 1}.jpg
    # φτιάχνουμε αρχεία της μορφής sample_{id}.csv
    # Πώς όμως; αρχικά πήρα τη λίστα raw_files και την επεξεργάζομαι 
    # η λίστα περιέχει strings της μορφής [IR_{id}.jpg, CSV_{id}.csv και DC_{id + 1}.jpg]
    # με τα regular expression κάνω εξάγωγή των αριθμών,
    #   έπειτα φτιάχνω ένα set, το οποίο αποθηκεύει τα μοναδικά id
    #   έπειτα φτιάχνουμε ζεύγη με τα γειτονικά, δηλαδή 
    for (file, path) in zip(raw_files, target_file_list):
        # if file.startswith('IR_'):
        #     # print('Processing ' + file)
        #     result = _IR_fixer(path, file)
        #     count += 1
        # if file.startswith('DC_'):
        #     # print('Processing ' + file)
        #     result = _DC_fixer(path, file)
        #     count += 1
        if file.startswith('CSV_'):
            # print('Processing ' + file)
            result = CSV_fixer(path, file, save_dir)
            count += 1
    print(f'***** Finished Processing {count} Targets **********')
    return count 

HERE = Path(__file__)           # ~/Adiposer/src/data/data_pick.py
SRC_DIR = HERE.parent.parent
PROJECT_DIR = SRC_DIR.parent
RAW_DIR = PROJECT_DIR / "data" / "raw"
INTERIM_DIR = PROJECT_DIR / "data" / "interim"
mode = 0o755
print(__name__)
if __name__ == '__main__':
    print('lathos meros')
    # import re 
    # pattern = re.compile("[0-9][0-9][0-9][0-9]")
    # ids = [int(pattern.findall(content).pop()) for content in raw_files] 
    # ids_unique = list(set(ids))
    # couple_list = []
    # unique_iter = iter(ids_unique)
    # couple = (next(unique_iter), next(unique_iter))
    # for i in range(len(ids_unique)):
    #     if couple[0] == couple[1] + 1:
    #         couple_list.append(couple)
    #     couple = (next(unique_iter), next(unique_iter))

    if os.path.exists(RAW_DIR):

        processed_files = 0
        # 1. Αρχικοποιηση 
        print('******* Initialized /data/interim/[sample_hours] directories **************')
        sample_hours = ['0h', '24h', '48h', '72h', '96h', '120h', '144h', '192h', '240h']
        [os.mkdir(INTERIM_DIR / sample_hour, mode) for sample_hour in sample_hours]
        # 2. Πέντε ποντίκια για κάθε ώρα δειγματοληψίας 
        print('******* Creating /data/interim/[sample_hours]/[mouse_ids] directories **************')
        mouse_ids = ['mouse_1', 'mouse_2', 'mouse_3', 'mouse_4', 'mouse_5']
        [os.mkdir(INTERIM_DIR / sample_hour / mouse_id, mode) for sample_hour in sample_hours for mouse_id in mouse_ids]
        
        for i, (raw_root, raw_dirs, raw_files) in enumerate(os.walk(RAW_DIR)):
            # raw_root : string of a POSIX-style directory
            # raw_dirs : list of subdirectories basenames
            # raw_files: list of filenames in the directory
            print(f'Iteration #{i}')
            print(f'        Basename Root dir: {os.path.basename(raw_root)}')
            print(f'        Found DIRs: {str(raw_dirs)}')
                
            if len(raw_dirs) == 0: # 3. Δεδομένα εικόνων 
                print(f'******* {len(raw_files)} Files Found at {raw_root}')
                
                paren_dir = os.path.abspath(os.path.join(raw_root, os.pardir))
                sample_h = os.path.basename(paren_dir)
                
                if raw_root.endswith('1'):
                    mouse_id = 'mouse_1'
                elif raw_root.endswith('2'):
                    mouse_id = 'mouse_2'
                elif raw_root.endswith('3'):
                    mouse_id = 'mouse_3'
                elif raw_root.endswith('4'):
                    mouse_id = 'mouse_4'
                elif raw_root.endswith('5'):
                    mouse_id = 'mouse_5'
                    
                SAVE_DIR = INTERIM_DIR / sample_h / mouse_id
                
                print(f'Base directory: {os.path.basename(raw_root)}')
                print(f'Saving at: {SAVE_DIR.as_posix}')
                full_path_target = [raw_root + '/' + raw_file for raw_file in raw_files]
                processed_files += process_targets(full_path_target, raw_files, SAVE_DIR)
                
                print(f'------------ Total Processed Files {processed_files} ------------------')
    else:
        ValueError("The dataset does not exist!")
        
