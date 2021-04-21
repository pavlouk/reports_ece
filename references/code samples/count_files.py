# -*- coding: utf-8 -*-
"""
Created on Wed Mar  3 21:46:04 2021

@author: plouk
"""
import os 


def count_py_files_in_repos(dirname):
    # --παιζει αναδρομικα--
    # δεχεται μορφή dirname 'C:/Users/plouk/Adiposer'
    # λουπα για το παρών dirname
    # αναδρομική κληση σε λουπα για 
    if os.path.exists(os.path.join(dirname, '.git')):
        count = 0
        for root, dirs, files in os.walk(dirname):
            count += len([f for f in files if f.endswith('.py')])
        print('{} has {} Python files'.format(dirname, count))
        
    for name in os.listdir(dirname):
        path = os.path.join(dirname, name)
        
        if os.path.isdir(path):
            count_py_files_in_repos(path)
            