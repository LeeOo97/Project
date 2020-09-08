import networkx as nx


def networking (nodes,edges):
    #creates graph
    net = nx.Graph(edges)

    #adds nodes to graph
    for n in nodes:
        net.add_node(n)

    #prints number of nodes in net
    print(net.number_of_nodes())

    max_net(net)

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
                        top_k.append(n1_top_k[e1])

    #creates new network
    top_k_net = nx.Graph(top_k)

    #adds nodes to new network
    for n in nx.nodes(net):
        top_k_net.add_node(n)
    
    return top_k_net

def max_net (net):

    #determine the max size of a component (10)
    #check network for components larger
    #remove lowest cosines until component is compliant 

    max_size = 10
    new_component_total = []
    for node in nx.nodes(net):
        component = nx.node_connected_component(net, node)
        edges = sorted(net.edges(node, data=True), key = lambda t: t[2].get('weight', 1), reverse=True)

        if (len(component)>max_size):
            new_component = new_component(remove_last_edge(net, edges, node, max_size), max_size)
            new_component_total.extend(new_component)
        else: 
            new_component_total.extend(edges)

    max_size_component_net = nx.Graph(new_component_total)

    for n in nx.nodes(net):
        max_size_component_net.add_node(n)
    

    return max_size_component_net
             
def remove_last_edge(net, edges, node, max_size):
    
    remove = edges[-1]
    edges = edges[:-1]
    net.remove_edge(remove[0], remove[1])
    component = nx.node_connected_component(net, node)
    #recalls remove_edge until component has <=10 edges
    if (len(component)>max_size):
        remove_last_edge(net, edges, node, max_size)
    return edges 


def new_component (edges, max_size):
    new_component = []
    for i in range (0,max_size):
        new_component.append(edges[i])
    
    return new_component

def graphml (graph, name):
    #writes graphml file from any network passed in
    gml = nx.write_graphml(graph, name)
    return gml