from pals.pimp_tools import *
from .spectra import Spectra
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

    spectra_list = []
    #spectra_list = np.array([], dtype = np.object)
    #spectra_list = np.array([], dtype=object)
    #spectra_list = np.vstack(spectra_list[:]).astype(np.float)

    #creates spectra objects
    for index, rows in frags_df.iterrows(): 
        id_temp = frags_df.loc[(index), 'ms1_id']
        i = 0
 
        if index == 0:
            mass = df.loc[(i), 'mass']
            spectra = Spectra(id_temp, mass)
            id = frags_df.loc[(index), 'ms2_id']
            ms2mz = frags_df.loc[(index), 'ms2_mz']
            ms2rt = frags_df.loc[(index), 'ms2_intensity']
            Spectra.add_peak(spectra, id, ms2mz, ms2rt)
        elif id_temp == frags_df.loc[(index-1), 'ms1_id']:
            #adds to list
            id = frags_df.loc[(index), 'ms2_id']
            ms2mz = frags_df.loc[(index), 'ms2_mz']
            ms2rt = frags_df.loc[(index), 'ms2_intensity']
            Spectra.add_peak(spectra, id, ms2mz, ms2rt)
        else:
            #create new spectra and add to list
            i += 1
            mass = df.loc[(i), 'mass']
            spectra = Spectra(id_temp, mass)
            id = frags_df.loc[(index), 'ms2_id']
            ms2mz = frags_df.loc[(index), 'ms2_mz']
            ms2rt = frags_df.loc[(index), 'ms2_intensity']
            Spectra.add_peak(spectra, id, ms2mz, ms2rt)

        spectra.scale_intensity()
        spectra_list.append(spectra)


    print(spectra_list[2].id1)

    return spectra_list





