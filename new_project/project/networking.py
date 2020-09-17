import networkx as nx
import matplotlib.pyplot as plt
import igraph
import operator

def networking (nodes,edges):
    #creates graph
    net = nx.Graph()


    #adds nodes to graph
    for n in nodes:
        net.add_node(str(n.id1))
  
    
    for s1 in edges.keys():
        for s2 in edges[s1].keys():
            #net.add_edge(int(s1.id1),int(s2.id1), length=edges[s1][s2]["cosine"])
            net.add_edge(str(s1.id1),str(s2.id1), weight=edges[s1][s2]["cosine"])
  


    #prints number of nodes in net
    print(net.number_of_nodes())

    #exports .graphml and exports .svg to browser
    nx.write_graphml(net, "graph.graphml")
    nx.write_gml(net, "graph.gml")
    graph = igraph.load("graph.gml")
    layout = graph.layout("fr")
    igraph.Graph.write_svg(graph,fname="static/graph_image.svg", layout = layout, width = 4000, height = 4000)
 

    return net

def top_k (net, k):
    print('method called')
    #initilialises list to hold edges for filtered network
    top_k = []

    top_k_net = nx.Graph()


  
    #creates a list of the top 1000 edges for node 1
    for n1 in range (0, (len(net)-1)):
        print ('loop started')
        n1_edges = sorted(net.edges(n1, data=True), key=lambda t: t[2].get('cosine', 1), reverse=True)
        n1_top_k = []


        for i in range (0, k):
            if i < len(n1_edges):
                n1_top_k.append(n1_edges[i])
                print(n1_top_k[0])

        #creates a list of the top 1000 edges for node 2
        for n2 in range ((n1+1), len(net)):
            n2_edges = sorted(net.edges(n2,data=True), key=lambda t: t[2].get('cosine', 1), reverse=True)
            n2_top_k = []

            for j in range (0, k):
                if j<len(n2_edges):
                    n2_top_k.append(n2_edges[j])
                    print (n2_top_k[0])

            #if an edge is present in the top 1000 edges for both nodes, it is added to top_k for generation of new network
            for e1 in n1_top_k:
                for e2 in n2_top_k:
                    if e1 == e2:
                        top_k_net.add_edge(e1)

    
    #creates new network

    
    print('new graph made')
    #adds nodes to new network



    
    return top_k_net

def max_net (net, max_size):


    #creates new list of edges to form filtered network
    new_component_total = []


    #identifies component and sorts edges by weight
    for node in nx.nodes(net):
          
        component = nx.node_connected_component(net, node)
        
        #list of all edges in a component
        component_edges = []

        #adds to list of component edges
        for n in component:
            edges = sorted(net.edges(n, data=True), key = lambda t: t[2].get('weight', 1), reverse=True)
            component_edges.extend(edges)


        #if component size is > max_size, edges are removed until it is <= max_size and a new component is generated
        if (len(component)>max_size):
            new_component = make_new_component(remove_last_edge(net, component_edges, node, max_size), max_size)
            new_component_total.extend(new_component)

        #if a component is small enough, new_component total is automatically extended
        else: 
            new_component_total.extend(edges)

            

    #removes duplicates from edge list
    component_final = []
    for edge in new_component_total:
        if edge not in component_final:
            component_final.append(edge)
            
    #creates a new network with filtered components
    max_size_component_net = nx.Graph(component_final)

    for n in nx.nodes(net):
        max_size_component_net.add_node(n)
    
    nx.write_graphml(max_size_component_net, "graph.graphml")
    nx.write_gml(max_size_component_net, "graph.gml")
    graph = igraph.load("graph.gml")
    layout = graph.layout("fr")
    igraph.Graph.write_svg(graph,fname="static/graph_image.svg", layout = layout, width = 4000, height = 4000)
    

    return max_size_component_net
             
def remove_last_edge(net, edges, node, max_size):

    component = nx.node_connected_component(net, node)
    #sets edge to be removed
    remove = edges[-1]
    edges = edges[:-1]
    #removes edge
    if net.has_edge(0, 1):
        net.remove_edge(remove[0], remove[1])
    print("edge removed")
   
    component = nx.node_connected_component(net, node)
    #recalls remove_edge until component has <= max  edges
    if (len(component)>max_size):
        remove_last_edge(net, edges, node, max_size)
    return edges 


def make_new_component (edges, max_size):
    #list to hold new component edges
    new_component = []
    #adds edges to new_component
    for i in range (0,max_size):
        new_component.append(edges[i])
    
    return new_component

def new_top_k(net, k):
    
    print('method called')

    top_k_net = nx.Graph()

    top_k = []
        
    #loops through edges in network
    for e in net.edges:
        #defines end points for edges
        source, target = e

        #sorts edges for both end points
        sorted_source = sorted(net.edges(source, data=True), key=lambda t: t[2].get('cosine', 1), reverse=True)
        sorted_target = sorted(net.edges(target, data=True), key=lambda t: t[2].get('cosine', 1), reverse=True)

        #checks if number of edges is within K already
        if k < (len(sorted_source)):
            top_source = sorted_source[:k]
        else:
            top_source = sorted_target
        if k < (len(sorted_target)):
            top_target = sorted_target[:k]
        else: 
            top_target = sorted_target

        #adds edge to top_k_net 
        for s in top_source:
            s_source, s_target, s_cos = s
            for t in top_target:
                t_source, t_target, t_cos = t
                if t_source==s_target and s_source==t_target:
                    top_k_net.add_edge(str(s_source),str(s_target), weight = s_cos)

    #adds nodes
    for n in nx.nodes(net):
        top_k_net.add_node(n)

    #export
    nx.write_graphml(top_k_net, "graph.graphml")
    nx.write_gml(top_k_net, "graph.gml")
    graph = igraph.load("graph.gml")
    layout = graph.layout("fr")
    igraph.Graph.write_svg(graph,fname="static/graph_image.svg", layout = layout, width = 4000, height = 4000)
    
    
    return top_k_net



 






#def graphml (graph, name):
    #writes graphml file from any network passed in
    
   