from flask import Flask
import os
from flask import render_template, request, send_file
import networkx as nx
import pimport
import sim 
import networking
import igraph

app = Flask(__name__)

UPLOAD_DIRECTORY = "/uploads" 

@app.route('/')
def index():
    return render_template("index.html")


@app.route('/uploads/<path:filename>', methods = ["GET"])
def file_downloads(filename):
    return send_file("uploads/" + filename)

@app.route('/result', methods=["POST"])
def result():
    print(request.form)
    username=request.form.get("username")
    password=request.form.get("password")
    analysis_id=int(request.form.get("analysis_id"))
    top_k=request.form.get("top_k")
    max_component_size=request.form.get("max_component_size")
    filter = request.form.get("filters") 
    print (filter)

    spectra_list, matches = sim.compare(pimport.import_pimp(username, password, analysis_id))
    #generates network by passing spectra_list(nodes) and matches(edges)
    network = networking.networking(spectra_list, matches)

    if filter is not None:
        if top_k != "":
            network = networking.top_k(network, int(top_k))
            
        if max_component_size != "":
            network = networking.max_net(network, int(max_component_size))
    #networking.graphml(network, "graph.graphml")
    


    nx.write_graphml(network, "uploads/graph.graphml")
    nx.write_gml(network, "graph.gml")
    graph = igraph.load("graph.gml")
    layout = graph.layout("kk")
    igraph.Graph.write_svg(graph,fname="static/graph_image.svg", layout = layout, width = 4000, height = 4000)


    graph_file = "graph_image.svg"

    return render_template("result.html", graph_image = graph_file)


    