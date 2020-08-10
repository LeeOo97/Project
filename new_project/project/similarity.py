from .mS2peak import MS2peak
from .pimport import import_pimp

def compare (spectra_list):
    'list of spectrtum objects > calculate modified cosine for eavh spectrum matched with other spectrum'
    'return a dictionary of spectrum matches with cosine score and number of matches'

    dicti = {}

    for i in range(0, len(spectra_list)):
        s1 = spectra_list[i]
        for n in range (i+1, len(spectra_list)):
            s2 = spectra_list[n]

            



