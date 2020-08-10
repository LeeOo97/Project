from pals.pimp_tools import *
from .mS2peak import MS2peak
import os
import sys
import pathlib
import pickle 


sys.path.append('..')

import pandas as pd
import numpy

#class pimport:
def import_pimp():
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
    frags_df = get_ms2_peaks(token, PIMP_HOST, analysis_id, as_dataframe=True)


    #initialises list for MS2peak objects
    spectra_list=[]
    rootintensity=[]
    #creates MS2peak for each ms2 peak
    for index, row in frags_df.iterrows():        
        id = frags_df.loc[(index), 'ms2_id']
        ms1mz = frags_df.loc[(index), 'ms1_mz']
        ms2mz = frags_df.loc[(index), 'ms2_mz']
        ms2rt = frags_df.loc[(index), 'ms2_intensity']

        #appends intensity peak for euclidian norm calculation
        rootintensity.append(ms2rt)

        #creates the new object
        peak = MS2peak(id, ms1mz, ms2mz, ms2rt)
        #adds to list
        spectra_list.append(peak)

    #prints specific value of list
    print(spectra_list[100].rootMS2)

    #calculates euclidian norm and scales
    norm = numpy.linalg.norm(rootintensity)
    for spectra in spectra_list:
        scalednorm = (rootintensity)/norm


    return spectra_list           

    
    
















