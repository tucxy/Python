import networkx as nx
import sys
sys.path.append('C:\\Users\\baneg\\OneDrive\\Desktop\\Git\\Python\\Research\\Graph Theory') # here is the path with GVIS
from graph_visualization import visualize
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

def edgeless(n):
    V = range(0,n)
    G = nx.Graph()
    G.add_nodes_from(V)
    return G


K21 = nx.complete_graph(21,create_using=None)
K22 = nx.complete_graph(22,create_using=None)
K35 = nx.complete_graph(35,create_using=None)
K36 = nx.complete_graph(36,create_using=None)
K49 = nx.complete_graph(49,create_using=None)

t=3
inc = 14*(t-1)

visualize(14*t+7,[K21], '(61)-1', 'C:\\Users\\baneg\\OneDrive\\Desktop\\Git\\Python\\Research\\7 (mod 14)\\texgraph')

#? 7 (mod 14)

#! (61)

#*(61)-1
G1  = merge(path([10,0,9,1,14+inc,5+inc,15+inc]), path([3,13]))
G2  = merge(path([14,4,13,5,18+inc,8+inc,17+inc]), path([3,12]))
G3  = merge(path([12,2,11,3,16+inc,6+inc,15+inc]), path([0-inc,13]))
G4 = merge(path([0,6,1,5, 2, 9, 7]), path([3,4]))

F_61_1 = [G1,G2,G3,G4] #defines the decomposition 'object' a list of graph labelings
#visualize(14*t+7,F_61_1, '(61)-1', 'C:\\Users\\baneg\\OneDrive\\Desktop\\Git\\Python\\Research\\7 (mod 14)\\texgraph')

#*(61)-8
G1 = merge(star(15,[2,3,5,6,7]),path([2,13]),path([12,20]))
G2 = merge(star(14,[2,3,4,5,6]),path([2,10]),path([9,19]))
G3 = merge(star(4,[12,13,15,16,17]),path([17,6]),path([10,19]))
G4 = merge(star(1,[5,6,7,8,4]),path([3,5,1]),path([9,10]))

F_61_8 = [G1]
#visualize(21,F_61_8, '(61)-8', 'C:\\Users\\baneg\\OneDrive\\Desktop\\Git\\Python\\Research\\8 (mod 14)\\texgraph')

#*(511)-4
G1 = merge(path([16+14,5,15,7]),path([17+14,5,15,2-14]),path([0,9]),path([1,10]))
G2 = merge(path([4,14,6,15]),path([3-14,14,6,19+14]), path([2,10]),path([8,17]))
G3 = merge(path([3,13,4,16+14]),path([2-14,13,4,17+14]), path([5-14,18]),path([1,11]))
G4 = merge(path([5,8,1,7]),path([4,8,1,6]), path([0,2]),path([9,10]))

F_511_4 = [G1,G2,G3,G4]
#visualize(14*t+7,F_511_4, '(511)-4', 'C:\\Users\\baneg\\OneDrive\\Desktop\\Git\\Python\\Research\\8 (mod 14)\\texgraph')

#*(511)-5
G1 = merge(path([1-14,14,5,15,2-14]),path([5,17+14]),path([9,19]),path([12,20]))
G2 = merge(path([6,14,4,16+14,3]),path([4,13]),path([1,10]),path([8,18]))
G3 = merge(path([12,4,17+14,6,15]),path([7+14,17+14]),path([0,9]),path([2-14,13]))
G4 = merge(path([5,11,9,12,7]),path([9,10]),path([1,8]),path([0,4]))

F_511_5 = [G1,G2,G3,G4]
#visualize(14*t+7,F_511_5, '(511)-5', 'C:\\Users\\baneg\\OneDrive\\Desktop\\Git\\Python\\Research\\8 (mod 14)\\texgraph')

#*(511)-6
G1 = merge(star(0,[8,9,10,12+14,13+14]),path([6,17+14]),path([5,15]))
G2 = merge(star(2,[10,11,12,13+14,15+14]),path([6,19+14]),path([8,17]))
G3 = merge(star(4,[12,13,14,15+14,17+14]),path([10,19]),path([8,20+14]))
G4 = merge(star(1,[4,5,6,7,8]),path([2,3]),path([9,11]))

F_511_6 = [G1,G2,G3,G4]
#visualize(14*t+7,F_511_6, '(511)-6', 'C:\\Users\\baneg\\OneDrive\\Desktop\\Git\\Python\\Research\\8 (mod 14)\\texgraph')

#*(31111)-1

G1 = merge(path([15,5,14,6]),path([0,10]),path([1,9]),path([7,16]),path([3,13]))
G2 = merge(path([4,13,5,17+14*(t-1)]),path([1,10]),path([8,18]),path([3,16+14*(t-1)]),path([0-14*(t-1),11]))
G3 = merge(path([4,12,2,11]),path([9,20+14*(t-1)]),path([1,14+14*(t-1)]),path([6,15]),path([10,18]))
G4 = merge(path([0,6,1,5]),path([2,9]),path([8,10]),path([4,7]),path([11,12]))

F_31111_1 = [G1,G2,G3,G4]
#visualize(14*t+7,F_31111_1, '(31111)-1', 'C:\\Users\\baneg\\OneDrive\\Desktop\\Git\\Python\\Research\\8 (mod 14)\\texgraph')

#? 8 (mod 14)

#*(211111)-1
t = 2
G1 = merge(path([11,math.inf,13]),path([4,12]),path([6-14*(t-1),17]),path([1,10]),path([5-14*(t-1),16]),path([8-14*(t-1),20]))
G2 = merge(path([16,math.inf,3]),path([1,9]),path([5,15]),path([8,18]),path([2-14*(t-1),13]),path([6,14]))
G3 = merge(path([0-14*(t-1),11,20]),path([1-14*(t-1),14]),path([7,17]),path([9,18]),path([2,10]),path([5,math.inf]))
G4 = merge(path([0,math.inf,8]),path([10,18]),path([5-14*(t-1),17]),path([2-14*(t-1),14]),path([7-14*(t-1),19]),path([12,20]))
G5 = merge(path([0,6,1]),path([4,8]),path([2,5]),path([3,10]),path([7,9]),path([11,12]))

F_211111_1 = [G1,G2,G3,G4,G5]
visualize(14*t+7,F_211111_1, '(211111)-1', 'C:\\Users\\baneg\\OneDrive\\Desktop\\Git\\Python\\Research\\8 (mod 14)\\texgraph')

#*(43)-4
G1 = merge(star(16,[7-14(t-1),6,5,3-14*(t-1)]),path([math.inf,0-14*(t-1),12,20]))
G2 = merge(star(8,[20+14*(t-1),19+14*(t-1),18,17]),path([2,math.inf,3,11]))
G3 = merge(star(14,[6,4,3-14*(t-1),1-14*(t-1)]),path([20,11,2,15+14*(t-1)]))
G4 = merge(star(math.inf,[20,12,4,1]),path([18,5-14*(t-1),17,6-14*(t-1)]))
G5 = merge(star(0,[6,5,4,3]),path([2,9,7,8]))

F_43_4 = [G1,G2,G3,G4,G5]
#visualize(14*t+7,F_43_4, '(43)-4', 'C:\\Users\\baneg\\OneDrive\\Desktop\\Git\\Python\\Research\\8 (mod 14)\\texgraph')

