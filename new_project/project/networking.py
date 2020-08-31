import networkx as nx

def networking (nodes,edges):
    net = nx.Graph(edges)

    for N in nodes:
        net.add_node(N)

    return net
