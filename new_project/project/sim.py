from .mS2peak import MS2peak
from .pimport import import_pimp
from collections import defaultdict as ddict
import math 
import numpy as numpy

def compare(df, spectra_list):
    print("running...")
    for i in range(0, len(spectra_list)):
        s1= spectra_list[i]
        for n in range (i+1, len(spectra_list)):
            s2 = spectra_list[n]
            similarity(df, spectra_list, s1, s2, round_precision=0)

def similarity(df, spectra_list, s1, s2, round_precision=1):
    vector1 = ddict(int) 
    vector2 = ddict(int)
    mzs = set()


    vector1[round(s1.ms2mz, round_precision)]
    mzs.add(round(s2.ms2mz, round_precision))

    vector2[round(s1.ms2mz, round_precision)]
    mzs.add(round(s2.ms2mz, round_precision))

    z=0
    n_v1 = 0
    n_v2 = 0

    for ms2mz in mzs:
        int1 = vector1[ms2mz]
        int2 = vector2[ms2mz]
        z += int1*int2
        n_v1 += int1*int1
        n_v2 += int2 * int2
    try:
        cosine = z / (math.sqrt(n_v1)* math.sqrt(n_v2))
    except:
        cosine = 0.0
    return cosine 





