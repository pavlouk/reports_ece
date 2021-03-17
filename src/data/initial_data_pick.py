import os
from pathlib import Path
from src.utils import get_project_root
import pandas as pd
import numpy as np
# =============================================================================
# αυτός ο κώδικας μεταφέρει όλα τα δεδομένα data/raw στο φάκελο data/interim
# με τις επεξεργασίες τους να είναι:
#     IR_*.jpg    --> IR_ = cut IR_*[:, 100:260]
#     CSV_*.csv   --> fix --> cut [:, 100:260]
#     DC_*.jpg    --> cut centered[IR_]
#     
# Paths:
#     print('here is ' + str(HERE))
#     print('src is ' + str(SRC_DIR))
#     print('root is ' + str(ROOT_DIR))
#     print('raw is ' + str(RAW_DIR))
#     
# Walking the RAW directory:
#     print('ROOT: \n' + str(root), 
#           '\n DIR: \n' + str(dirs), 
#           '\n FILE: ' + str(files))
#     
#     print('ROOT: \n' + str(root), 
#           '\n DIR: \n' + str(dirs))
#     
#     print('DIR: ' + str(dirs))
#     
#     print('Root: ' + str(root))
#     
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

def _csv_fixer(fname):
    
    # έχω θέμα με τα separators και τη διάσταση του frame 
    # άμα sep = 'κενό,' τότε φτιάνει δίστηλο 
    # άμα sep = 'κενό' τότε φτιάνει τετράστηλο  
    # όπως και να έχει είναι σκουπίδια και θέλουν επεξεργασία, οπότε θα πάρουμε το δίστηλο 
    dataF = pd.read_csv(filepath_or_buffer=fname, sep=' ,', engine='python')
    columnNames = dataF.columns
    # μόνο η πρώτη στήλη με το περίεργο όνομα έχει τις θερμοκρασίες
    # firstColumn type: pandas Series
    dataColumn = dataF[columnNames[0]] # ας δούμε το πρώτο που έχει τη λέξη Frame 1 στην αρχή 
    firstLine = dataColumn[0] # ειναι string, κάτι θα κάνουμε οπότε 
    # firstLine.count(',') # 320 ειναι τα κόμματα κάτι που ισχύει και για τα υπόλοιπα 
    rawData = np.fromstring(firstLine[8:], dtype=float, sep=',') # εδώ υπάρχει η λέξη 'Frame 1,' την διώχνουμε
    # np.hstack(rawData)
    # τα επόμενα ξεκινάνε με κόμμα, οπότε για τα επόμενα 239 θα κάνουμε το ίδιο
    for i in range(1, dataF.shape[0]):
        dataStringLine = dataColumn[i]
        rawData = np.vstack((rawData, np.fromstring(dataStringLine[1:], dtype=float, sep=',')))
        
    return rawData

def process_targets(target_file_list, raw_files):
    count = 0
    print('******** Processing Targets **************')
    for (file, path) in zip(raw_files, target_file_list):
        if file.startswith('IR_'):
            if os.path.isfile(path):
                print('Processing ' + file)
                _csv_fixer(path)
                count += 1
        if file.startswith('DC_'):
            if os.path.isfile(path):
                print('Processing ' + file)
                count += 1
        if file.startswith('CSV_'):
            if os.path.isfile(path):
                print('Processing ' + file)
                
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
        #     # os.mkdir(path, mode)
            
        # print('making dir at interim ' + str(raw_root_path.parent))
        # dirs_path = Path(dirs)
else:
    ValueError("Raw dataset doesn't exist")
        
