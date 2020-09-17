#test sim
#test max network filter
#test top k filter
import networkx as nx
from pals.pimp_tools import *
from spectra import Spectra
from mS2peak import MS2peak
from networking import top_k, new_top_k, max_net
import sim


import random


def sim_test():
    spectra_list_test = []
    
    #generate 2 spectra wotj
    s1mass = 100
    s1 = Spectra(1, s1mass)
    Spectra.add_peak(s1, 1, 50, 100)
    Spectra.add_peak(s1, 2, 55, 107)
    Spectra.add_peak(s1, 3, 60, 112)
    Spectra.add_peak(s1, 4, 65, 90)
    s1.scale_intensity()
    spectra_list_test.append(s1)

    s2 = Spectra(2, s1mass)
    Spectra.add_peak(s2, 5, 50, 100)
    Spectra.add_peak(s2, 6, 55, 107)
    Spectra.add_peak(s2, 7, 60, 112)
    Spectra.add_peak(s2, 8, 65, 90)
    s2.scale_intensity()
    spectra_list_test.append(s2)
    
    print("sim_test")
    print(sim.modified_similarity(s1,s2, fragment_tolerance=0.3, precursor_tolerance=1.0))

def test_top_k():
    net = nx.Graph()

    for n in range (0, 5):
        net.add_node(n)
    
    edges = [(0, 1, {'cosine':0.9}), (0, 4, {'cosine':0.4}), (1,2,{'cosine':0.12}), (1,3,{'cosine':0.3}), (2, 4, {'cosine':0.8})]

    
    net.add_edges_from(edges)

    #top 1 edges (0,1), (0.2)
    test_net = new_top_k(net, 2, edges)


    #for n in nx.nodes(test_net):
        #print (test_net.degree[n])

def test_max():
    net = nx.Graph()

    for n in range (0, 5):
        net.add_node(n)
    
    edges = [(0, 1, {'cosine':0.9}), (0, 4, {'cosine':0.4}), (1,2,{'cosine':0.12}), (1,3,{'cosine':0.3}), (2, 4, {'cosine':0.8})]

    
    net.add_edges_from(edges)

    test_max = max_net(net, 3)

    for n in nx.nodes(net):
        component = nx.node_connected_component(net, n)
        print (component)

test_max()
#test_top_k()
#sim_test()