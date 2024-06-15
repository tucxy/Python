import networkx as nx
import sys
sys.path.append('path/to/containing/directory')
from graph_visualization import multivisualize
from itertools import combinations
import math

# how to merge two graphs:
'''
# Create two graphs
G1 = nx.Graph()
G1.add_edges_from([('a', 'b'), ('b', 'c')])

G2 = nx.Graph()
G2.add_edges_from([('c', 'd'), ('d', 'e')])

# Merge the graphs
G_merged = nx.compose(G1, G2)
'''
#how to merge multiple graphs
'''
# Create multiple graphs
G1 = nx.Graph()
G1.add_edges_from([('a', 'b'), ('b', 'c')])

G2 = nx.Graph()
G2.add_edges_from([('c', 'd'), ('d', 'e')])

G3 = nx.Graph()
G3.add_edges_from([('e', 'f'), ('f', 'g')])

# Merge the graphs
G_merged = nx.compose_all([G1, G2, G3])
'''

def inspect(G):
    nodes = list(G.nodes)
    edges = list(G.edges)
    
    Ginfo = {
        "Nodes": nodes,
        "Edges": edges
    }
    
    return Ginfo

def build(vertices, edges):
    """
    Create a graph using NetworkX from a list of vertices and edges.
    build([u,v,w,...], [(u, v), (w, v), ...])
    """
    G = nx.Graph()
    G.add_nodes_from(vertices)
    G.add_edges_from(edges)
    return G

def merge(*graphs):
    """
    Merge multiple NetworkX graphs into a single graph.
    """
    G = nx.Graph()
    
    for graph in graphs:
        G.add_nodes_from(graph.nodes())
        G.add_edges_from(graph.edges())
    
    return G

def path(cycle):

    C = list(cycle)
    G = nx.Graph()
    G.add_nodes_from(C)
    for i in range(len(C) - 1):
        G.add_edge(C[i], C[i + 1])
    return G

def cycle(cycle):

    C = list(cycle)
    G = nx.Graph()
    G.add_nodes_from(C)
    for i in range(len(C)):
        G.add_edge(C[i], C[(i + 1) % len(C)])
    return G

def star(hub, neighbors):

    leaves = list(neighbors)
    G = nx.Graph()
    G.add_node(hub)
    for node in leaves:
        G.add_node(node)
        G.add_edge(hub, node)
    return G

def trees(n):
    def is_isomorphic_to_any(graph, graph_list):
        for g in graph_list:
            if nx.is_isomorphic(graph, g):
                return True
        return False

    all_trees = []
    nodes = list(range(n + 1))  # A tree with n edges has n+1 nodes

    for edges in combinations(combinations(nodes, 2), n):
        G = nx.Graph()
        G.add_edges_from(edges)
        if nx.is_tree(G) and not is_isomorphic_to_any(G, all_trees):
            all_trees.append(G)

    return all_trees
#notebook

'''
8 (mod 14) case example:

P1 = path([20,11,1,math.inf,0,9])
P2 = path([10,2,12])
G1 = merge(P1,P2)

P3 = path([5,13,2,math.inf,3,11])
P4 = path([19,8,20])
G2 = merge(P3,P4)

P5 = path([3,12,4,math.inf,5,14])
P6 = path([11,0,8])
G3 = merge(P5,P6)

P7 = path([13,0,10,1,9,18])
P8 = path([math.inf,6,17])
G4 = merge(P7,P8)

multivisualize([G1,G2,G3,G4],'multitest')
'''

#7 (mod 14) example: 
S1 = star(0,[8,9,10])
P11 = path([6,18,7])
P12 = path([1,13,5])
G1 = merge(S1,P11,P12)

S2 = star(1,[9,10,11])
P21 = path([12,0,13])
P22 = path([6,17,4])
G2 = merge(S2,P21,P22)

S3 = star(2,[10,11,13])
P31 = path([17,5,16])
P32 = path([1,12,4])
G3 = merge(S3,P31,P32)

S0 = star(0,[4,5,6])
P01 = path([1,8,7])
P02 = path([11,9,12])
G0 = merge(S0,P01,P02)
multivisualize([G1,G2,G3,G0],'test', location="default")


