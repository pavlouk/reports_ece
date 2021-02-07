# -*- coding: utf-8 -*-
from glob import glob 
import pandas as pd
import numpy as np

# df = pd.read_csv(filepath_or_buffer='~/Adiposer/dataset/BAT/CSV_2509.csv', 
#                  sep=',', engine='python', 
#                  skip_blank_lines=True, skipinitialspace=True, skiprows=[0, 1])
# data = pd.concat((pd.read_csv(file).assign(filename=file) for file in csvFiles), 
#                  ignore_index=True)
# data = [_data_fixer(file) for file in csvFiles]

def _data_fixer(fname):
    
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
    

def load_csv(hours, name='BAT'):
    """
    ας επιστρέψω για αρχή λεξικό γιατί έχω καθυστερήσει
    μετά να το κάνω να επιστρέφει λίστα από λεξικά 
    
    
    """
    data_dictionary = dict.fromkeys(hours)
    if name == 'WAT':
        csvFiles = sorted(glob('C:/Users/plouk/Adiposer/dataset/WAT/CSV_*.csv'))
        
        for sampleHour, file in zip(hours, csvFiles):
            data_dictionary[sampleHour] = _data_fixer(file)
            
        return pd.DataFrame(data_dictionary)
    
    csvFiles = sorted(glob('C:/Users/plouk/Adiposer/dataset/BAT/CSV_*.csv'))

    for sampleHour, file in zip(hours, csvFiles):
        data_dictionary[sampleHour] = _data_fixer(file)
        
    return pd.DataFrame(data_dictionary)
