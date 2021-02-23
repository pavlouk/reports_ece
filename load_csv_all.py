# -*- coding: utf-8 -*-
"""
Created on Mon Feb 22 14:48:13 2021

@author: plouk
"""
# -*- coding: utf-8 -*-
from glob import glob 
import pandas as pd
import numpy as np
import os 
# df = pd.read_csv(filepath_or_buffer='~/Adiposer/dataset/BAT/CSV_2509.csv', 
#                  sep=',', engine='python', 
#                  skip_blank_lines=True, skipinitialspace=True, skiprows=[0, 1])
# data = pd.concat((pd.read_csv(file).assign(filename=file) for file in csv_files), 
#                  ignore_index=True)
# data = [_data_fixer(file) for file in csv_files]

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
    

def load_csv_all(hours, name='BAT'):
    """ 
=======
load_csv_all
=======

Definition: load_csv_all(hours, name='BAT')

Image loader from the dataset directory 

Obtain all FLIR image metadata

Parameters
----------
hours : list[string] 
     Sampled Hours data

name : string {'WAT' or 'BAT'} (default 'BAT')
    Obtain appropriate data.

Returns
-------
sensor_data : dictionary {'Mouse Name' : {hour_sample : np.array}}
    Loaded sensor data.    
        
    """
    data_dictionary = dict.fromkeys(hours)
    CWD = os.getcwd()
    sensor_data = dict.fromkeys(['Mouse1', 'Mouse2', 'Mouse3', 'Mouse4', 'Mouse5'])
    
    if name == 'WAT':
        csv_files = sorted(glob(CWD + '/dataset/WAT/Mouse1/CSV_*.csv'))
        for sampleHour, file in zip(hours, csv_files):
            data_dictionary[sampleHour] = _data_fixer(file)
        sensor_data['Mouse1'] = data_dictionary
        
        csv_files = sorted(glob(CWD + '/dataset/WAT/Mouse2/CSV_*.csv'))
        for sampleHour, file in zip(hours, csv_files):
            data_dictionary[sampleHour] = _data_fixer(file)
        sensor_data['Mouse2'] = data_dictionary
        
        csv_files = sorted(glob(CWD + '/dataset/WAT/Mouse3/CSV_*.csv'))
        for sampleHour, file in zip(hours, csv_files):
            data_dictionary[sampleHour] = _data_fixer(file)
        sensor_data['Mouse3'] = data_dictionary
        
        csv_files = sorted(glob(CWD + '/dataset/WAT/Mouse4/CSV_*.csv'))
        for sampleHour, file in zip(hours, csv_files):
            data_dictionary[sampleHour] = _data_fixer(file)
        sensor_data['Mouse4'] = data_dictionary
        
        csv_files = sorted(glob(CWD + '/dataset/WAT/Mouse5/CSV_*.csv'))    
        for sampleHour, file in zip(hours, csv_files):
            data_dictionary[sampleHour] = _data_fixer(file)
        sensor_data['Mouse5'] = data_dictionary  
        # return pd.DataFrame(data_dictionary)
        return sensor_data
    
    
    csv_files = sorted(glob(CWD + '/dataset/BAT/Mouse1/CSV_*.csv'))
    for sampleHour, file in zip(hours, csv_files):
        data_dictionary[sampleHour] = _data_fixer(file)
    sensor_data['Mouse1'] = data_dictionary
    
    csv_files = sorted(glob(CWD + '/dataset/BAT/Mouse2/CSV_*.csv'))
    for sampleHour, file in zip(hours, csv_files):
        data_dictionary[sampleHour] = _data_fixer(file)
    sensor_data['Mouse2'] = data_dictionary
    
    csv_files = sorted(glob(CWD + '/dataset/BAT/Mouse3/CSV_*.csv'))
    for sampleHour, file in zip(hours, csv_files):
        data_dictionary[sampleHour] = _data_fixer(file)
    sensor_data['Mouse3'] = data_dictionary
       
    csv_files = sorted(glob(CWD + '/dataset/BAT/Mouse4/CSV_*.csv'))
    for sampleHour, file in zip(hours, csv_files):
        data_dictionary[sampleHour] = _data_fixer(file)
    sensor_data['Mouse4'] = data_dictionary
    
    csv_files = sorted(glob(CWD + '/dataset/BAT/Mouse5/CSV_*.csv'))    
    for sampleHour, file in zip(hours, csv_files):
        data_dictionary[sampleHour] = _data_fixer(file)
    sensor_data['Mouse5'] = data_dictionary     
    # return pd.DataFrame(data_dictionary)
    return sensor_data