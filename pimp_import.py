from pals.pimp_tools import *
import os
import sys
import pathlib
import pickle 


sys.path.append('..')

import pandas as pd


#def import_from_pimp():
    #Token generation
username = '2143815O' #username
password = 'XPNfM4nfYQ' #password
host = PIMP_HOST #server address and port
token = get_authentication_token(host, username, password)

#id for pimp project
analysis_id = 1321 # beer analysis

#fetches ms1 intensities
int_df, annotation_df, experimental_design = download_from_pimp(token, PIMP_HOST, analysis_id, 'ms1')

#loads all information associated with MS1 peaks
df = get_ms1_peaks(token, PIMP_HOST, analysis_id)

#sets pid column as index
df.set_index('pid')

#loads MS2 fragmentation data 
frags = get_ms2_peaks(token, PIMP_HOST, analysis_id, as_dataframe=False)