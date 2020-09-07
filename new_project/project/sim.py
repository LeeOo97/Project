from .mS2peak import MS2peak
from .spectra import Spectra
from .pimport import import_pimp
from .networking import networking
from collections import defaultdict as ddict
from networkx.algorithms import matching
import networkx as nx
import math 
import numpy as numpy





   
def compare(spectra_list):
    print("running...")

    matches = {}


    #for i in range(0, (len(spectra_list)-1)):
    for i in range (0, 20):
        s1= spectra_list[i]
        #for n in range (i+1, len(spectra_list)):
        for n in range (i+1, 20):
            s2 = spectra_list[n]
            print (i , n)
            
            #calls modified similarity method to find cosine score and number of peaks
            cosine_score, count = modified_similarity(spectra_list, s1, s2)

            if (cosine_score==0 and count==0):
                continue
            #adds to matches if not already in matches
            if s1 not in matches:
                matches[s1]={}
            matches[s1][s2]={'cosine':cosine_score, 'peaks': count}

            if s2 not in matches:
                matches[s2]={}
            matches[s2][s1]={'cosine':cosine_score, 'peaks': count}



    print(len(matches))
    
    #generates network by passing spectra_list(nodes) and matches(edges)
    networking(spectra_list, matches)

    return matches
 
def modified_similarity (spectra_list, s1,s2, fragment_tolerance=0.3, precursor_tolerance=1.0):
    #calculate modification
    modification = (s2.mass)-(s1.mass)
    #returns 0,0 if modification is greater than the precursor tolerance
    if (abs(modification))>precursor_tolerance:
        return 0,0

    pairs = []
    #creates pairs of peaks with a match score
    for i in s1.peaks:
        for j in s2.peaks:
            if (abs(i.ms2mz)-(j.ms2mz) <= fragment_tolerance) or (abs(i.ms2mz)+ modification - (j.ms2mz) <= fragment_tolerance):
                match_score = i.scaled * j.scaled
                pair = (i, j, match_score)
                pairs.append(pair)
    
    #tests pairs for maximum weight matching
    G = nx.Graph()
    for i in pairs:
        G.add_edge(i[0], i[1], weight=i[2])

    max_score = nx.algorithms.max_weight_matching(G)

    count = len(max_score)

    max_match = 0

    for i in max_score:
        for j in pairs:
            if (i[0]==j[0] and i[1]==j[1]) or (i[0]==j[1] or j[0]==i[1]):
                max_match += j[2]

    return max_match, count




def similarity(spectra_list, s1, s2, round_precision=1):

    
    vector1 = ddict(int) 
    vector2 = ddict(int)
    mzs = set()

    for MS2peak in s1.peaks:
        vector1[round((MS2peak.ms2mz), round_precision)]
        mzs.add(round((MS2peak.ms2mz), round_precision))
    for MS2peak in s2.peaks:
        vector1[round((MS2peak.ms2mz), round_precision)]
        mzs.add(round((MS2peak.ms2mz), round_precision))

    z=0
    n_v1 = 0
    n_v2 = 0

    for ms2mz in mzs:
        int1 = vector1[ms2mz]
        int2 = vector2[ms2mz]
        z += int1*int2
        n_v1 += int1*int1
        n_v2 += int2*int2
    try:
        cosine = z/(math.sqrt(n_v1)* math.sqrt(n_v2))
    except:
        cosine = 0.0
    return cosine 







