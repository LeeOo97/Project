from mS2peak import MS2peak
from spectra import Spectra
from pimport import import_pimp
from networking import networking
from collections import defaultdict as ddict
from networkx.algorithms import matching
import networkx as nx
import math 
import numpy as numpy





   
def compare(spectra_list):
    print("running...")

    matches = {}


    #for i in range(0, (len(spectra_list)-1)/test value -1):
    for i in range (0, 50):
        s1= spectra_list[i]
        #for n in range (i+1, len(spectra_list)/test value):
        for n in range (i+1, 50):
            s2 = spectra_list[n]
            #prints in console the position of similarity calculator
            print (i , n)
                        
            #checks to see if spectras are the same spectra before calling
            if s1!=s2:
                #calls modified similarity method to find cosine score and number of peaks
                cosine_score, count = modified_similarity(s1, s2)
                #if the returned cosine value and number of peaks matched are both 0, the next set of peaks are selected 
                if (cosine_score!=0 and count!=0):
                #adds to matches if not already in matches as a dictionary
                    if s1 not in matches:
                        matches[s1]={}
                    matches[s1][s2]={'cosine':cosine_score}

                    if s2 not in matches:
                        matches[s2]={}
                    matches[s2][s1]={'cosine':cosine_score}



    print(len(matches))
    
 
    return spectra_list, matches
 
def modified_similarity (s1,s2, fragment_tolerance=0.3, precursor_tolerance=1.0):
    #calculate modification

    modification=(s1.mass)-(s2.mass)
    #returns 0,0 if modification is greater than the precursor tolerance
    if (abs(modification))>precursor_tolerance:
        return 0,0

    #initialises list of pairs and G (for maximum weight calculation)
    pairs = []
    G = nx.Graph()

    #creates pairs of peaks with a match score
    for i in s1.peaks:
        for j in s2.peaks:
            #checks if peaks are eligible matches
             if (abs((i.ms2mz)-(j.ms2mz)) <= fragment_tolerance) or (abs((i.ms2mz)+ modification - (j.ms2mz)) <= fragment_tolerance):
                #sum of cosines scaled for euclidean norm 1
                match_score = i.scaled * j.scaled
                #adds edges to G for max_weight_matching
                G.add_edge(i, j, weight= (match_score))
                #adds matched pair to pairs for counting of peaks
                pair = (i, j, match_score)
                pairs.append(pair)
    


    #finds maximum weight match between peaks in spectra
    max_score = nx.algorithms.max_weight_matching(G)

    #number of peaks between spectra found to be similar
    count = len(max_score)

    #max match represents the total cosine value of similarity between spectra
    max_match = 0

    #calculates max match
    for i in max_score:
        for j in pairs:
            if (i[0]==j[0] and i[1]==j[1]) or (i[0]==j[1] or j[0]==i[1]):
                max_match += j[2]


    return max_match, count

def similarity(spectra_list, s1, s2, round_precision=1):

    
    vector1 = ddict(int) 
    vector2 = ddict(int)
    mzs = set()

    #populatees vector lists with MS2 peaks
    for MS2peak in s1.peaks:
        vector1[round((MS2peak.ms2mz), round_precision)]
        mzs.add(round((MS2peak.ms2mz), round_precision))
    for MS2peak in s2.peaks:
        vector1[round((MS2peak.ms2mz), round_precision)]
        mzs.add(round((MS2peak.ms2mz), round_precision))

    z=0
    n_v1 = 0
    n_v2 = 0

    #calculates similarity between peaks and calculates spectra similarity
    for ms2mz in mzs:
        peak_sim_1 = vector1[ms2mz]
        peak_sim_2 = vector2[ms2mz]
        z += peak_sim_1*peak_sim_2
        n_v1 += peak_sim_1 * peak_sim_1
        n_v2 += peak_sim_2 * peak_sim_2
    try:
        cosine = z/(math.sqrt(n_v1)* math.sqrt(n_v2))
    #if cosine is 0.0, no cosine is returned
    except:
        cosine = 0.0
    return cosine 







