from flask import Flask
from flask import render_template, request
import networkx as nx
import matplotlib.pyplot as plt
import pimport
import sim 
import networking

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/result', methods=["POST"])
def result():
    print(request.form)
    username=request.form.get("username")
    password=request.form.get("password")
    analysis_id=int(request.form.get("analysis_id"))
    top_k=int(request.form.get("top_k"))
    max_component_size=int(request.form.get("max_component_size"))

    spectra_list, matches = sim.compare(pimport.import_pimp(username, password, analysis_id))
    #generates network by passing spectra_list(nodes) and matches(edges)
    network = networking.networking(spectra_list, matches)

    #networking.graphml(network, "graph.graphml")
    #change into image, show image, add weighted edges
    return username


    