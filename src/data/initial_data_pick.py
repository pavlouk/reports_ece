import os

from pathlib import Path

from .utils import get_project_root
def initial_data_pick():
    """ 
    αυτός ο κώδικας μεταφέρει όλα τα δεδομένα στο φάκελο data/interim
    τα δεδομένα είναι:
        DC_*.jpg
        IR_*.jpg
        CSV_*.csv

         """
    root_directory = get_project_root()
    if os.path.exists(os.path.join(root_directory, 'data/raw')):
        