import networkx as nx


def networking (nodes,edges):
    #creates graph
    net = nx.Graph(edges)

    #adds nodes to graph
    for n in nodes:
        net.add_node(n)

    #prints number of nodes in net
    print(net.number_of_nodes())

    return net

def top_k (net, nodes, edges):
    #initilialises list to hold edges for filtered network
    top_k = []

    #creates a list of the top 1000 edges for node 1
    for n1 in range (0, (net.number_of_nodes)-1):
        n1_edges = sorted(net.edges(n1, data=True), key=lambda t: t[2].get('weight', 1), reverse=True)
        n1_top_k = []
        for i in range (0, 1000):
            n1_top_k.append(n1_edges[i])

        #creates a list of the top 1000 edges for node 2
        for n2 in range ((n1+1), net.number_of_nodes):
            n2_edges = sorted(net.edges(n2,data=True), key=lambda t: t[2].get('weight', 1), reverse=True)
            n2_top_k = []
            for j in range (0, 1000):
                n2_top_k.append(n2_edges[j])

            #if an edge is present in the top 1000 edges for both nodes, it is added to top_k for generation of new network
            for e1 in n1_top_k:
                for e2 in n2_top_k:
                    if e1 == e2:
                        top_k.append(e1)

    #creates new network
    top_k_net = nx.Graph(top_k)

    #adds nodes to new network
    for n in nodes:
        net.add_node(n)
    
    return top_k_net

def max_net (net):
    print('blah blah')
    #determine the max size of a component
    #check network for components larger
    #remove lowest cosines until component is compliant 


def graphml (graph, name):
    #writes graphml file from any network passed in
    gml = nx.write_graphml(graph, name)
    return gml