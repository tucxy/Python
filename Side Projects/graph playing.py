import networkx as nx
from Gvis import *

def build(vertices, edges):
    """
    Create a graph using NetworkX from a list of vertices and edges.
    build([u,v,w,...], [(u, v), (w, v), ...])
    """
    G = nx.Graph()
    G.add_nodes_from(vertices)
    G.add_edges_from(edges)
    return G

G = build([1,2,3,4],[(1,2),(1,3),(1,4)])

visualize(G,"TEST")

