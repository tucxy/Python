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
G1.add_edges_from([ ('a',  'b'),  ('b',  'c')])

G2 = nx.Graph()
G2.add_edges_from([ ('c',  'd'),  ('d',  'e')])

# Merge the graphs
G_merged = nx.compose(G1,  G2)
'''
#how to merge multiple graphs
'''
# Create multiple graphs
G1 = nx.Graph()
G1.add_edges_from([ ('a',  'b'),  ('b',  'c')])

G2 = nx.Graph()
G2.add_edges_from([ ('c',  'd'),  ('d',  'e')])

G3 = nx.Graph()
G3.add_edges_from([ ('e',  'f'),  ('f',  'g')])

# Merge the graphs
G_merged = nx.compose_all([ G1,  G2,  G3])
'''

def inspect(G):
    nodes = list(G.nodes)
    edges = list(G.edges)
    
    Ginfo = {
        "Nodes": nodes,
        "Edges": edges
    }
    
    return Ginfo

def build(vertices,edges):
    """
    Create a graph using NetworkX from a list of vertices and edges.
    build([ u, v, w, ...],  [ (u,  v),  (w,  v),  ...])
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
        G.add_edge(C[ i],C[ i + 1])
    return G

def cycle(cycle):

    C = list(cycle)
    G = nx.Graph()
    G.add_nodes_from(C)
    for i in range(len(C)):
        G.add_edge(C[ i],C[ (i + 1) % len(C)])
    return G

def star(hub,neighbors):

    leaves = list(neighbors)
    G = nx.Graph()
    G.add_node(hub)
    for node in leaves:
        G.add_node(node)
        G.add_edge(hub,node)
    return G

def trees(n):
    def is_isomorphic_to_any(graph,graph_list):
        for g in graph_list:
            if nx.is_isomorphic(graph,g):
                return True
        return False

    all_trees = [ ]
    nodes = list(range(n + 1))  # A tree with n edges has n+1 nodes

    for edges in combinations(combinations(nodes,  2),n):
        G = nx.Graph()
        G.add_edges_from(edges)
        if nx.is_tree(G) and not is_isomorphic_to_any(G,all_trees):
            all_trees.append(G)

    return all_trees
#notebook
t = 2
inc = 14*(t-1)
#? 8 (mod 14)

#! (61)

#*(61)-1
G1  = merge(path([ 20, 11, 1, math.inf,  0,  9,  19]),  path([ 2, 10]))
G2 = merge(path([ 5, 13,( 2-inc)%(14*t+7), math.inf,  3,  11, ( 0-inc)%(14*t+7)]),  path([ 19,( 8-inc)%(14*t+7)]))
G3 = merge(path([ 3, 12, 4, math.inf,  5,  14, ( 1-inc)%(14*t+7)]),  path([ 20,( 8-inc)%(14*t+7)]))
G4 = merge(path([( 3+inc)%(14*t+7), (13+inc)%(14*t+7), 0, 10,  1,  9,  18]),  path([ math.inf, 6]))
G5 = merge(path([ 0, 6, 1, 5,  2,  9,  7]),  path([ 3, 4]))

F_61_1 = [ G1, G2, G3, G4, G5] #defines the decomposition 'object' a list of graph labelings
visualize(14*t+7, F_61_1,  '(61)-1',  'C:\\Users\\baneg\\OneDrive\\Desktop\\Git\\Python\\Research\\8 (mod 14)\\texgraph')


#*(61)-2
G1  = merge(path([ 9, 0, math.inf, 1, 11, 20]), path([ 1, (13+inc)%(14*t+7)]),  path([ 2, 12]))
G2  = merge(path([ (13+inc)%(14*t+7), 2, math.inf, 3, 11,( 0-inc)%(14*t+7)]), path([ 3, (16+inc)%(14*t+7)]),  path([ 12, 20]))
G3  = merge(path([ 3, 12, 4, math.inf, 5, 14]), path([ math.inf, 6]),  path([ 0, 8]))
G4  = merge(path([ (13+inc)%(14*t+7), 0, 10, 1, 9, 18]), path([ 1, (12+inc)%(14*t+7)]),  path([ 6, (17+inc)%(14*t+7)]))
G5  = merge(path([ 0, 6, 1, 5, 2, 9]), path([ 5, 3]),  path([ 7, 8]))

F_61_2 = [ G1, G2, G3, G4, G5]
#visualize(14*t+7, F_61_2,  '(61)-2',  'C:\\Users\\baneg\\OneDrive\\Desktop\\Git\\Python\\Research\\8 (mod 14)\\texgraph')

#*(61)-3
G1 = merge(path([ 11, 1, math.inf, 0, 9, 17]), path([ 9, 19]),  path([ 4, 13]))
G2  = merge(path([ 11, 3, math.inf, 2, (13+inc)%(14*t+7),( 5+inc)%(14*t+7)]), path([ 1, (13+inc)%(14*t+7)]),  path([ 7, (18+inc)%(14*t+7)]))
G3  = merge(path([ 14, 5, math.inf, 4, 12, 3]), path([( 1-inc)%(14*t+7), 12]),  path([ 7, 15]))
G4  = merge(path([ 9, 1, 10, 0, (13+inc)%(14*t+7),( 3+inc)%(14*t+7)]), path([ (13+inc)%(14*t+7), math.inf]),  path([ 2, 11]))
G5  = merge(path([ 0, 6, 1, 5, 2, 9]), path([ 2, 4]),  path([ 7, 8]))

F_61_3 = [ G1, G2, G3, G4, G5]
#visualize(14*t+7, F_61_3,  '(61)-3',  'C:\\Users\\baneg\\OneDrive\\Desktop\\Git\\Python\\Research\\8 (mod 14)\\texgraph')

#*(61)-4
G1 = merge(star(1, [ (14+inc)%(14*t+7), 11, (13+inc)%(14*t+7), math.inf]), path([ (20+inc)%(14*t+7), 7, math.inf]),  path([ 8, (19+inc)%(14*t+7)]))
G2 = merge(star(3, [ 13, math.inf, (14+inc)%(14*t+7), 11]), path([ 11,( 0-inc)%(14*t+7),( 9-inc)%(14*t+7)]),  path([ 6, (19+inc)%(14*t+7)]))
G3 = merge(star(math.inf, [ 2, 5, 6, 4]), path([ 3, 12, 4]),  path([ 7, (19+inc)%(14*t+7)]))
G4 = merge(star(9, [ (20+inc)%(14*t+7), 18, 19, 1]), path([ 2, 10, 1]),  path([ 4, 13]))
G5 = merge(star(1, [ 5, 6, 7, 4]), path([ 9, 2, 4]),  path([ 11, 10]))

F_61_4 = [ G1, G2, G3, G4, G5]
#visualize(14*t+7, F_61_4,  '(61)-4',  'C:\\Users\\baneg\\OneDrive\\Desktop\\Git\\Python\\Research\\8 (mod 14)\\texgraph')

#*(61)-5
G1 = merge(path([ 7, math.inf, 1, (13+inc)%(14*t+7), 0]), path([ (14+inc)%(14*t+7), 1, 11]),  path([ 8, (19+inc)%(14*t+7)]))
G2 = merge(path([( 0-inc)%(14*t+7), 11, 3, (16+inc)%(14*t+7), 5]), path([ 13, 3, math.inf]),  path([ 6, (19+inc)%(14*t+7)]))
G3 = merge(path([ 12, 4, math.inf, 5, (17+inc)%(14*t+7)]), path([ 2, math.inf, 6]),  path([ 7, (19+inc)%(14*t+7)]))
G4 = merge(path([ 10, 1, 9, 18,( 6-inc)%(14*t+7)]), path([ (20+inc)%(14*t+7), 9, 0]),  path([ 7, 17]))
G5 = merge(path([ 3, 8, 1, 4, 2]), path([ 5, 1, 7]),  path([ 9, 10]))

F_61_5 = [ G1, G2, G3, G4, G5]
#visualize(14*t+7, F_61_5,  '(61)-5',  'C:\\Users\\baneg\\OneDrive\\Desktop\\Git\\Python\\Research\\8 (mod 14)\\texgraph')

#*(61)-6
G1 = merge(star(7, [ (20+inc)%(14*t+7), 16, math.inf]), star(1, [ math.inf, (13+inc)%(14*t+7), 11]), path([ 8, (19+inc)%(14*t+7)]))
G2 = merge(star((0-inc)%(14*t+7), [( 8-inc)%(14*t+7), 12, 11]), star(3, [ 11, (16+inc)%(14*t+7), math.inf]), path([ 4, 13]))
G3 = merge(star(12, [ 20, 3, 4]), star(math.inf, [ 4, 6, 5]), path([ 2, (13+inc)%(14*t+7)]))
G4 = merge(star(10, [ 20, 0, 1]), star(9, [ 1, 19, 18]), path([ 2, math.inf]))
G5 = merge(star(8, [ 7, 4, 1]), star(6, [ 1, 0, 3]), path([ 9, 11]))

F_61_6 = [ G1, G2, G3, G4, G5]
#visualize(14*t+7, F_61_6,  '(61)-6',  'C:\\Users\\baneg\\OneDrive\\Desktop\\Git\\Python\\Research\\8 (mod 14)\\texgraph')

#*(61)-7
G1 = merge(star(1, [ math.inf, (14+inc)%(14*t+7), (13+inc)%(14*t+7), 11]), path([ 7, math.inf, 3]), path([ 0, 9]))
G2 = merge(star(3, [ 11, 13, (16+inc)%(14*t+7), (14+inc)%(14*t+7)]), path([( 0-inc)%(14*t+7), 11, 20]), path([ 4, 12]))
G3 = merge(star(math.inf, [ 2, 4, 6, 5]), path([ (17+inc)%(14*t+7), 5, 13]), path([ 7, (19+inc)%(14*t+7)]))
G4 = merge(star(9, [ 1, (20+inc)%(14*t+7), 18, 19]), path([ 10, 1, (12+inc)%(14*t+7)]), path([ 0, (13+inc)%(14*t+7)]))
G5 = merge(star(1, [ 8, 5, 6, 7]), path([ 3, 6, 4]), path([ 9, 10]))

F_61_7 = [ G1, G2, G3, G4, G5]
#visualize(14*t+7, F_61_7,  '(61)-7',  'C:\\Users\\baneg\\OneDrive\\Desktop\\Git\\Python\\Research\\8 (mod 14)\\texgraph')

#*(61)-8
G1 = merge(star(math.inf, [ 7, 2, 1, 6, 3]), path([ math.inf, 1, (13+inc)%(14*t+7)]), path([ 0, 9]))
G2 = merge(star(5, [ math.inf, 14, (17+inc)%(14*t+7), 13, (16+inc)%(14*t+7)]), path([ 4, math.inf, 5]), path([ 0, 10]))
G3 = merge(star(11, [( 0-inc)%(14*t+7), 2, 3, 19, 20]), path([ 11, 3, (16+inc)%(14*t+7)]), path([ 6, (17+inc)%(14*t+7)]))
G4 = merge(star(1, [ 10, (14+inc)%(14*t+7), 9, 11, (12+inc)%(14*t+7)]), path([ 1, 9, (20+inc)%(14*t+7)]), path([ 0, (13+inc)%(14*t+7)]))
G5 = merge(star(1, [ 5, 6, 7, 8, 4]), path([ 3, 5, 1]), path([ 9, 10]))

F_61_8 = [ G1, G2, G3, G4, G5]
#visualize(14*t+7, F_61_8,  '(61)-8',  'C:\\Users\\baneg\\OneDrive\\Desktop\\Git\\Python\\Research\\8 (mod 14)\\texgraph')

#*(61)-9
G1 = merge(path([ 7, math.inf, 1, (13+inc)%(14*t+7), 0]), path([ 1, (14+inc)%(14*t+7),( 5+inc)%(14*t+7)]), path([ 10, 20]))
G2 = merge(path([19, 11, 3, (16+inc)%(14*t+7),( 7+inc)%(14*t+7)]), path([ 3, math.inf, 2]), path([ 5,13]))
G3 = merge(path([ 14, 4, math.inf, 5, (17+inc)%(14*t+7)]), path([ math.inf, 6, 16]), path([ 1, 11]))
G4 = merge(path([ 10, 1, 9, 18,( 6-inc)%(14*t+7)]), path([ 9, 19,( 8-inc)%(14*t+7)]), path([ 7, 17]))
G5 = merge(path([ 5, 11, 9, 12, 7]), path([ 9, 10, 6]), path([ 1, 8]))

F_61_9 = [ G1, G2, G3, G4, G5]
#visualize(14*t+7, F_61_9,  '(61)-9',  'C:\\Users\\baneg\\OneDrive\\Desktop\\Git\\Python\\Research\\8 (mod 14)\\texgraph')

#*(61)-10
G1 = merge(star(1, [ math.inf, 11, (13+inc)%(14*t+7)]), path([ 3, math.inf, 7, 15]), path([ 0, 9]))
G2 = merge(star(3, [ 11, (16+inc)%(14*t+7), (14+inc)%(14*t+7)]), path([( 0-inc)%(14*t+7), 11, 20, 10]), path([ 2, math.inf]))
G3 = merge(star(5, [ math.inf, 13, (17+inc)%(14*t+7)]), path([ 4, math.inf, 6, 16]), path([ 7, (19+inc)%(14*t+7)]))
G4 = merge(star(1, [ 9, (12+inc)%(14*t+7), 10]), path([ 18, 9, 19, 11]), path([ 0, (13+inc)%(14*t+7)]))
G5 = merge(star(8, [ 1, 4, 5]),  path([ 3, 1, 6, 0]), path([ 9, 10]))

F_61_10 = [ G1, G2, G3, G4, G5]
#visualize(14*t+7, F_61_10,  '(61)-10',  'C:\\Users\\baneg\\OneDrive\\Desktop\\Git\\Python\\Research\\8 (mod 14)\\texgraph')

#! (52)

#*(52)-1
G1 = merge(path([ 20, 11, 1, math.inf, 0, 9]),  path([ 10, 2, 12]))
G2 = merge(path([ 5, 13,( 2-inc)%(14*t+7), math.inf, 3, 11]),  path([ 19,( 8-inc)%(14*t+7), 20]))
G3 = merge(path([ 3, 12, 4, math.inf, 5, 14]),  path([ 8, 0, (11+inc)%(14*t+7)]))
G4 = merge(path([ (13+inc)%(14*t+7), 0, 10, 1, 9, 18]),  path([ (17+inc)%(14*t+7), 6, math.inf]))
G5 = merge(path([ 0, 6, 1, 5, 2, 9]), path([ 12, 10, 11]))

F_52_1 = [ G1, G2, G3, G4, G5]
#visualize(14*t+7, F_52_1,  '(52)-1',  'C:\\Users\\baneg\\OneDrive\\Desktop\\Git\\Python\\Research\\8 (mod 14)\\texgraph')

#*(52)-2
G1 = merge(path([ 20, 11, 1, math.inf, 0]), path([ 2, 11]), path([ 17, 9, 19]))
G2 = merge(path([ 5, 13,( 2-inc)%(14*t+7), math.inf, 3]), path([( 1-inc)%(14*t+7), 13]), path([ (19+inc)%(14*t+7), 8, 16]))
G3 = merge(path([ 3, 12, 4, math.inf, 5]), path([( 0-inc)%(14*t+7), 12]), path([( 7-inc)%(14*t+7), 18, 10]))
G4 = merge(path([ (13+inc)%(14*t+7), 0, 10, 1, (14+inc)%(14*t+7)]), path([ 0, 9]), path([ (17+inc)%(14*t+7), 6, math.inf]))
G5 = merge(path([ 3, 6, 1, 8, 4]), path([ 0, 6]), path([ 10, 9, 11]))

F_52_2 = [ G1, G2, G3, G4, G5]
#visualize(14*t+7, F_52_2,  '(52)-2',  'C:\\Users\\baneg\\OneDrive\\Desktop\\Git\\Python\\Research\\8 (mod 14)\\texgraph')

#*(52)-3
G1 = merge(path([ 11, 1, math.inf, 0, 9]), path([ math.inf, 6]), path([ 5, 15, 7]))
G2 = merge(path([ (18+inc)%(14*t+7), 6, 16, math.inf, 3]), path([ 16,( 4-inc)%(14*t+7)]), path([ 12, 2, 10]))
G3 = merge(path([ 3, 12, 4, math.inf, 5]), path([ 4, (17+inc)%(14*t+7)]), path([ 6, (19+inc)%(14*t+7), 7]))
G4 = merge(path([ (11+inc)%(14*t+7), 0, 10, 1, 9]), path([ 10, 20]), path([ 15, 6, 14]))
G5 = merge(path([ 5, 11, 9, 12, 7]), path([ 9, 10]), path([ 1, 8, 4]))

F_52_3 = [ G1, G2, G3, G4, G5]
#visualize(14*t+7, F_52_3,  '(52)-3',  'C:\\Users\\baneg\\OneDrive\\Desktop\\Git\\Python\\Research\\8 (mod 14)\\texgraph')

#*(52)-4
G1 = merge(path([ 11, 1, math.inf, 0]), path([ (12+inc)%(14*t+7), 1, math.inf, 6]),  path([ 15, 7, 16]))
G2 = merge(path([ 6, 16, math.inf, 3]), path([( 4-inc)%(14*t+7), 16, math.inf, 5]),  path([ 12, 2, 10]))
G3 = merge(path([ 3, 12, 4, math.inf]), path([( 0-inc)%(14*t+7), 12, 4, (17+inc)%(14*t+7)]),  path([ 18,( 6-inc)%(14*t+7), 19]))
G4 = merge(path([ 0, 10, 1, 9]), path([ 20, 10, 1, (13+inc)%(14*t+7)]),  path([ 6, 14, 4]))
G5 = merge(path([ 3, 8, 1, 7]), path([ 4, 8, 1, 6]),  path([ 10, 9, 11]))

F_52_4 = [ G1, G2, G3, G4, G5]
#visualize(14*t+7, F_52_4,  '(52)-4',  'C:\\Users\\baneg\\OneDrive\\Desktop\\Git\\Python\\Research\\8 (mod 14)\\texgraph')

#*(52)-5
G1 = merge(star(1, [ 11, (14+inc)%(14*t+7), math.inf, (12+inc)%(14*t+7)]), path([ math.inf, 0]), path([ (19+inc)%(14*t+7), 7, 16]))
G2 = merge(star(math.inf, [ 3, 13, 16, 5]), path([ 16, 6]), path([ 20, 12, 2]))
G3 = merge(star(4, [ math.inf, (16+inc)%(14*t+7), 12, (17+inc)%(14*t+7)]), path([ 12, 3]), path([ (18+inc)%(14*t+7), 6, 15]))
G4 = merge(star(10, [ 0, 2, 1, 20]), path([ 1, 9]), path([ 6, 14, 4]))
G5 = merge(star(1, [ 8, 5, 4, 7]), path([ 8, 3]), path([ 10, 9, 11]))

F_52_5 = [ G1, G2, G3, G4, G5]
#visualize(14*t+7, F_52_5,  '(52)-5',  'C:\\Users\\baneg\\OneDrive\\Desktop\\Git\\Python\\Research\\8 (mod 14)\\texgraph')

#*(52)-6
G1 = merge(star(1, [ 11, (14+inc)%(14*t+7), math.inf, 9, (12+inc)%(14*t+7)]), path([ (19+inc)%(14*t+7), 7, 16]))
G2 = merge(star(math.inf, [ 13, 16, 0, 5, 3]), path([ 20, 12, 2]))
G3 = merge(star(4, [ math.inf, (16+inc)%(14*t+7), 12, 13, (17+inc)%(14*t+7)]), path([ 9, (20+inc)%(14*t+7), 8]))
G4 = merge(star(10, [ 0, 2, 1, 19, 20]), path([6, 14, 4]))
G5 = merge(star(1, [ 4, 5, 6, 7, 8]), path([ 10, 9, 11]))

F_52_6 = [ G1, G2, G3, G4, G5]
#visualize(14*t+7, F_52_6,  '(52)-6',  'C:\\Users\\baneg\\OneDrive\\Desktop\\Git\\Python\\Research\\8 (mod 14)\\texgraph')

#! (43)

#*(43)-1
G1 = merge(path([ 11, 1, math.inf, 0, 9]), path([ 10, 2, 12, 20]))
G2 = merge(path([ (13+inc)%(14*t+7), 2, math.inf, 3, 11]), path([ 5, 15, 6, (18+inc)%(14*t+7)]))
G3 = merge(path([ 12, 4, math.inf, 5, 14]), path([ 8, 0, (11+inc)%(14*t+7),( 2+inc)%(14*t+7)]))
G4 = merge(path([ (13+inc)%(14*t+7), 0, 10, 1, 9]), path([ 5, (17+inc)%(14*t+7), 6, math.inf]))
G5 = merge(path([ 0, 6, 1, 5, 2]), path([ 3, 10, 8, 9]))

F_43_1 = [ G1, G2, G3, G4, G5]
#visualize(14*t+7, F_43_1,  '(43)-1',  'C:\\Users\\baneg\\OneDrive\\Desktop\\Git\\Python\\Research\\8 (mod 14)\\texgraph')

#*(43)-2
G1 = merge(path([ 20, 12, 2, 10]), path([ 2, (13+inc)%(14*t+7)]), path([ 1, math.inf, 0, 9]))
G2 = merge(path([ (18+inc)%(14*t+7), 6, 15, 5]), path([ 15,( 4-inc)%(14*t+7)]), path([ 2, math.inf, 3, 11]))
G3 = merge(path([ 14, 5, math.inf, 4]), path([ math.inf, 6]), path([( 0-inc)%(14*t+7), 11, 2, (15+inc)%(14*t+7)]))
G4 = merge(path([ 1, 10, 0, (13+inc)%(14*t+7)]), path([ 0, 8]), path([ (18+inc)%(14*t+7), 5, (17+inc)%(14*t+7), 6]))
G5 = merge(path([ 5, 8, 1, 7]), path([ 1, 6]),  path([ 0, 4, 2, 3]))

F_43_2 = [ G1, G2, G3, G4, G5]
#visualize(14*t+7, F_43_2,  '(43)-2',  'C:\\Users\\baneg\\OneDrive\\Desktop\\Git\\Python\\Research\\8 (mod 14)\\texgraph')

#*(43)-3
G1 = merge(path([ 1, math.inf, 0, 9]), path([ 0, (12+inc)%(14*t+7)]), star((16+inc)%(14*t+7), [ 3, 5,( 6+inc)%(14*t+7)]))
G2 = merge(path([ 2, math.inf, 3, 11]), path([ 3, (15+inc)%(14*t+7)]), star(8, [ (20+inc)%(14*t+7), (19+inc)%(14*t+7), 18]))
G3 = merge(path([ (15+inc)%(14*t+7), 2, 11,( 0-inc)%(14*t+7)]), path([ 11, 20]), star(14, [ 6,( 3-inc)%(14*t+7),( 1-inc)%(14*t+7)]))
G4 = merge(path([ 6, (17+inc)%(14*t+7), 5, (18+inc)%(14*t+7)]), path([ 5, 13]), star(math.inf, [ 12, 4, 20]))
G5 = merge(path([ 4, 8, 1, 7]), path([ 1, 6]), star(9, [ 10, 12, 11]))

F_43_3 = [ G1, G2, G3, G4, G5]
#visualize(14*t+7, F_43_3,  '(43)-3',  'C:\\Users\\baneg\\OneDrive\\Desktop\\Git\\Python\\Research\\8 (mod 14)\\texgraph')

#*(43)-4
G1 = merge(star(16, [ 7, 6,( 5-inc)%(14*t+7),( 3-inc)%(14*t+7)]), path([ math.inf,( 0-inc)%(14*t+7), 12, 20]))
G2 = merge(star(8, [ (20+inc)%(14*t+7), (19+inc)%(14*t+7), 18, 17]), path([ 2, math.inf, 3, 11]))
G3 = merge(star(14, [ 6, 4,( 3-inc)%(14*t+7),( 1-inc)%(14*t+7)]), path([ 20, 11, 2, (15+inc)%(14*t+7)]))
G4 = merge(star(math.inf, [ 20, 12, 4, 1]), path([ 18,( 5-inc)%(14*t+7), 17,( 6-inc)%(14*t+7)]))
G5 = merge(star(0, [ 6, 5, 4, 3]), path([ 2, 9, 7, 8]))

F_43_4 = [ G1, G2, G3, G4, G5]
#visualize(14*t+7, F_43_4,  '(43)-4',  'C:\\Users\\baneg\\OneDrive\\Desktop\\Git\\Python\\Research\\8 (mod 14)\\texgraph')

#*(43)-5
G1 = merge(star(16, [ 7,( 5-inc)%(14*t+7),( 3-inc)%(14*t+7)]), path([ 1, math.inf,( 0-inc)%(14*t+7), 12, 20]))
G2 = merge(star(8, [ (20+inc)%(14*t+7), (19+inc)%(14*t+7), 17]), path([ 2, math.inf, 3, 11, 1]))
G3 = merge(star(14, [ 6, 4,( 3-inc)%(14*t+7)]), path([ 20, 11, 2, (15+inc)%(14*t+7),( 7+inc)%(14*t+7)]))
G4 = merge(star(math.inf, [ 20, 12, 4]), path([ (18+inc)%(14*t+7), 5, (17+inc)%(14*t+7), 6, 16]))
G5 = merge(star(9, [ 12, 11, 10]), path([ 4, 8, 1, 7, 2]))

F_43_5 = [ G1, G2, G3, G4, G5]
#visualize(14*t+7, F_43_5,  '(43)-5',  'C:\\Users\\baneg\\OneDrive\\Desktop\\Git\\Python\\Research\\8 (mod 14)\\texgraph')

#*(43)-6
G1 = merge(star(16, [ 8, 6,( 5-inc)%(14*t+7),( 3-inc)%(14*t+7)]), star((0-inc)%(14*t+7), [ math.inf, 12,( 9-inc)%(14*t+7)]))
G2 = merge(star(8, [ math.inf, (20+inc)%(14*t+7), (19+inc)%(14*t+7), 18]), star(14, [ 6,( 3-inc)%(14*t+7),( 1-inc)%(14*t+7)]))
G3 = merge(star(3, [ math.inf, (15+inc)%(14*t+7), 11, 13]), star(18, [ 9,( 7-inc)%(14*t+7),( 6-inc)%(14*t+7)]))
G4 = merge(star(math.inf, [ 20, 12, 4, 2]), star(5, [ (18+inc)%(14*t+7), (17+inc)%(14*t+7), 13]))
G5 = merge(star(0, [ 6, 5, 4, 3]), star(9, [ 8, 7, 2]))

F_43_6 = [ G1, G2, G3, G4, G5]
#visualize(14*t+7, F_43_6,  '(43)-6',  'C:\\Users\\baneg\\OneDrive\\Desktop\\Git\\Python\\Research\\8 (mod 14)\\texgraph')

#! (511)

#*(511)-1
G1 = merge(path([ 20, 11, 1, math.inf, 0, 9]), path([ 3, (16+inc)%(14*t+7)]), path([ 2, 12]))
G2 = merge(path([ 5, 13,( 2-inc)%(14*t+7), math.inf, 3, 11]), path([ 8, (19+inc)%(14*t+7)]), path([ 15, 6]))
G3 = merge(path([ 3, 12, 4, math.inf, 5, 14]), path([ 0, 8]), path([ 7, (18+inc)%(14*t+7)]))
G4 = merge(path([ (13+inc)%(14*t+7), 0, 10, 1, 9, 18]), path([ 6, (17+inc)%(14*t+7)]), path([ 20, math.inf]))
G5 = merge(path([ 0, 6, 1, 5, 2, 9]), path([ 8, 10]), path([ 3, 4]))

F_511_1 = [ G1, G2, G3, G4, G5]
#visualize(14*t+7, F_511_1,  '(511)-1',  'C:\\Users\\baneg\\OneDrive\\Desktop\\Git\\Python\\Research\\8 (mod 14)\\texgraph')


#*(511)-2
G1 = merge(path([ 0, math.inf, 1, 11, 20]), path([ 11, 2]), path([ 3, (16+inc)%(14*t+7)]), path([ 5, 15]))
G2 = merge(path([ 3, math.inf,( 2-inc)%(14*t+7), 13, 5]), path([ 13,( 1-inc)%(14*t+7)]), path([ 10, 18]), path([ 9, 19]))
G3 = merge(path([ 5, math.inf, 4, 12, 3]), path([ 12,( 0-inc)%(14*t+7)]), path([ 8, 16]), path([( 7-inc)%(14*t+7), 18]))
G4 = merge(path([ (14+inc)%(14*t+7), 1, 10, 0, (13+inc)%(14*t+7)]), path([ 0, 9]), path([ 6, (17+inc)%(14*t+7)]), path([ 20, math.inf]))
G5 = merge(path([ 4, 8, 1, 6, 3]), path([ 6, 0]), path([ 5, 7]), path([ 9, 10]))

F_511_2 = [ G1, G2, G3, G4, G5]
#visualize(14*t+7, F_511_2,  '(511)-2',  'C:\\Users\\baneg\\OneDrive\\Desktop\\Git\\Python\\Research\\8 (mod 14)\\texgraph')

#*(511)-3
G1 = merge(star(1, [ 11, (12+inc)%(14*t+7), math.inf, (14+inc)%(14*t+7)]), path([ math.inf, 0]), path([ 7, 16]), path([ 6, (19+inc)%(14*t+7)]))
G2 = merge(star(math.inf, [ 5, 3, 16, 13]), path([ 16, 6]), path([ 7, (19+inc)%(14*t+7)]), path([ 2, 12]))
G3 = merge(star(4, [ math.inf, (17+inc)%(14*t+7), 12, (16+inc)%(14*t+7)]), path([ 12, 3]), path([ 6, (18+inc)%(14*t+7)]), path([ 1, (13+inc)%(14*t+7)]))
G4 = merge(star(10, [ 0, 20, 1, 2]), path([ 1, 9]), path([ 7, (18+inc)%(14*t+7)]), path([ 6, 14]))
G5 = merge(star(1, [ 4, 5, 8, 7]), path([ 8, 3]), path([ 0, 2]), path([ 9, 10]))

F_511_3 = [ G1, G2, G3, G4, G5]
#visualize(14*t+7, F_511_3,  '(511)-3',  'C:\\Users\\baneg\\OneDrive\\Desktop\\Git\\Python\\Research\\8 (mod 14)\\texgraph')

#*(511)-4
G1 = merge(path([ 11, 1, math.inf, 0]), path([ (12+inc)%(14*t+7), 1, math.inf, 6]),  path([ 7, 15]), path([ 2, (14+inc)%(14*t+7)]))
G2 = merge(path([ 6, 16, math.inf, 3]), path([( 4-inc)%(14*t+7), 16, math.inf, 5]),  path([ 2, 12]), path([ 9, 17]))
G3 = merge(path([ 3, 12, 4, math.inf]), path([( 0-inc)%(14*t+7), 12, 4, (17+inc)%(14*t+7)]),  path([( 6-inc)%(14*t+7), 18]), path([ 5, 13]))
G4 = merge(path([ 0, 10, 1, 9]), path([ 20, 10, 1, (13+inc)%(14*t+7)]),  path([ 6, 14]), path([( 7-inc)%(14*t+7), 18]))
G5 = merge(path([ 5, 8, 1, 7]), path([ 4, 8, 1, 6]),  path([ 0, 2]), path([ 9, 10]))

F_511_4 = [ G1, G2, G3, G4, G5]
#visualize(14*t+7, F_511_4,  '(511)-4',  'C:\\Users\\baneg\\OneDrive\\Desktop\\Git\\Python\\Research\\8 (mod 14)\\texgraph')

#*(511)-5
G1 = merge(path([ 11, 1, math.inf, 0, 9]), path([ math.inf, 6]), path([ 7, (19+inc)%(14*t+7)]), path([ 5, 15]))
G2 = merge(path([ (18+inc)%(14*t+7), 6, 16, math.inf, 3]), path([ 16,( 4-inc)%(14*t+7)]), path([ 0, (13+inc)%(14*t+7)]), path([ 9, 19]))
G3 = merge(path([ 3, 12, 4, math.inf, 5]), path([ 4, (17+inc)%(14*t+7)]), path([ 6, (19+inc)%(14*t+7)]), path([ 0, 8]))
G4 = merge(path([ (11+inc)%(14*t+7), 0, 10, 1, 9]), path([ 10, 20]), path([ 6, 15]), path([ 3, (16+inc)%(14*t+7)]))
G5 = merge(path([ 5, 11, 9, 12, 7]), path([ 9, 10]), path([ 1, 8]), path([ 0, 4]))

F_511_5 = [ G1, G2, G3, G4, G5]
#visualize(14*t+7, F_511_5,  '(511)-5',  'C:\\Users\\baneg\\OneDrive\\Desktop\\Git\\Python\\Research\\8 (mod 14)\\texgraph')

#*(511)-6
G1 = merge(star(1, [ 11, (14+inc)%(14*t+7), math.inf, 9, (12+inc)%(14*t+7)]), path([ 7, (19+inc)%(14*t+7)]), path([ 5, 13]))
G2 = merge(star(math.inf, [ 13, 16, 0, 5, 3]), path([ 7, (20+inc)%(14*t+7)]), path([ 2, (14+inc)%(14*t+7)]))
G3 = merge(star(4, [ math.inf, (16+inc)%(14*t+7), 12, 13, (17+inc)%(14*t+7)]), path([ 6, 15]), path([ 9, (20+inc)%(14*t+7)]))
G4 = merge(star(10, [ 0, 2, 1, 19, 20]), path([ 4, 14]), path([ 5, (16+inc)%(14*t+7)]))
G5 = merge(star(1, [ 4, 5, 6, 7, 8]), path([ 2, 3]), path([ 9, 11]))

F_511_6 = [ G1, G2, G3, G4, G5]
#visualize(14*t+7, F_511_6,  '(511)-6',  'C:\\Users\\baneg\\OneDrive\\Desktop\\Git\\Python\\Research\\8 (mod 14)\\texgraph')

#! (421)

#*(421)-1
G1 = merge(path([ 11, 1, math.inf, 0, 9]), path([ 10, 2, 12]), path([ 5, 13]))
G2 = merge(path([ (13+inc)%(14*t+7), 2, math.inf, 3, 11]), path([ (18+inc)%(14*t+7), 6, 15]), path([ 1, (12+inc)%(14*t+7)]))
G3 = merge(path([ 12, 4, math.inf, 5, 14]), path([ 8, 0, (11+inc)%(14*t+7)]), path([ 9, 18]))
G4 = merge(path([ (13+inc)%(14*t+7), 0, 10, 1, 9]), path([ 5, (17+inc)%(14*t+7), 6]), path([ 20, math.inf]))
G5 = merge(path([ 0, 6, 1, 5, 2]), path([ 8, 10, 9]), path([ 4, 11]))

F_421_1 = [ G1, G2, G3, G4, G5]
#visualize(14*t+7, F_421_1,  '(421)-1',  'C:\\Users\\baneg\\OneDrive\\Desktop\\Git\\Python\\Research\\8 (mod 14)\\texgraph')

#*(421)-2
G1 = merge(path([ 20, 12, 2, 10]), path([ 2, (13+inc)%(14*t+7)]), path([ 1, math.inf, 0]), path([ 7, 16]))
G2 = merge(path([ (18+inc)%(14*t+7), 6, 15, 5]), path([ 15,( 4-inc)%(14*t+7)]), path([ 9, math.inf, 10]), path([ 3, 11]))
G3 = merge(path([ 14, 5, math.inf, 4]), path([ 6, math.inf]), path([( 0-inc)%(14*t+7), 11, 2]), path([ 1, 9]))
G4 = merge(path([ 1, 10, 0, (13+inc)%(14*t+7)]), path([ 0, 8]), path([ 5, (17+inc)%(14*t+7), 6]), path([ 4, 12]))
G5 = merge(path([ 5, 8, 1, 7]), path([ 1, 6]), path([ 10, 9, 11]), path([ 0, 4]))

F_421_2 = [ G1, G2, G3, G4, G5]
#visualize(14*t+7, F_421_2,  '(421)-2',  'C:\\Users\\baneg\\OneDrive\\Desktop\\Git\\Python\\Research\\8 (mod 14)\\texgraph')

#*(421)-3
G1 = merge(star(16, [( 3-inc)%(14*t+7), 6,( 5-inc)%(14*t+7), 7]), path([ 12,( 0-inc)%(14*t+7), math.inf]), path([ 10, 18]))
G2 = merge(star(8, [ 17, 18, (19+inc)%(14*t+7), (20+inc)%(14*t+7)]), path([ 2, math.inf, 3]), path([ 5, 13]))
G3 = merge(star(14, [ 6, 4,( 3-inc)%(14*t+7),( 1-inc)%(14*t+7)]), path([ 20, 11, 2]), path([ 8, 16]))
G4 = merge(star(math.inf, [ 20, 12, 4, 1]), path([ 17,( 5-inc)%(14*t+7), 18]), path([ 3, 13]))
G5 = merge(star(0, [ 6, 5, 4, 3]), path([ 1, 8, 7]), path([ 9, 11]))

F_421_3 = [ G1, G2, G3, G4, G5]
#visualize(14*t+7, F_421_3,  '(421)-3',  'C:\\Users\\baneg\\OneDrive\\Desktop\\Git\\Python\\Research\\8 (mod 14)\\texgraph')

#! (331)

#*(331)-1
G1 = merge(path([ 1, math.inf, 0, 9]), path([ 20, 12, 2, 10]), path([ 6, 16]))
G2 = merge(path([ (18+inc)%(14*t+7), 6, 15, 5]), path([ 2, math.inf, 3, 11]), path([ 0, 8]))
G3 = merge(path([ 14, 5, math.inf, 4]), path([( 0-inc)%(14*t+7), 11, 2, (15+inc)%(14*t+7)]), path([ 8, 18]))
G4 = merge(path([ 1, 10, 0, (13+inc)%(14*t+7)]), path([ (18+inc)%(14*t+7), 5, (17+inc)%(14*t+7), 6]), path([ math.inf, 20]))
G5 = merge(path([ 0, 6, 1, 5]), path([ 2, 9, 7, 10]), path([ 3, 4]))

F_331_1 = [ G1, G2, G3, G4, G5]
#visualize(14*t+7, F_331_1,  '(331)-1',  'C:\\Users\\baneg\\OneDrive\\Desktop\\Git\\Python\\Research\\8 (mod 14)\\texgraph')

#*(331)-2
G1 = merge(star(16, [( 3-inc)%(14*t+7),( 5-inc)%(14*t+7), 6]), path([ 1, math.inf, 0, 9]), path([( 7-inc)%(14*t+7), 19]))
G2 = merge(star(8, [ (20+inc)%(14*t+7), (19+inc)%(14*t+7), 18]), path([ 2, math.inf, 3, 11]), path([ 1, 10]))
G3 = merge(star(14, [( 1-inc)%(14*t+7),( 3-inc)%(14*t+7), 6]), path([ (15+inc)%(14*t+7), 2, 11,( 0-inc)%(14*t+7)]), path([ 4, 13]))
G4 = merge(star(math.inf, [ 4, 13, 19]), path([ 6, (17+inc)%(14*t+7), 5, (18+inc)%(14*t+7)]), path([ 12, 20]))
G5 = merge(star(0, [ 4, 5, 6]), path([ 11, 9, 10, 7]), path([ 1, 8]))

F_331_2 = [ G1, G2, G3, G4, G5]
#visualize(14*t+7, F_331_2,  '(331)-2',  'C:\\Users\\baneg\\OneDrive\\Desktop\\Git\\Python\\Research\\8 (mod 14)\\texgraph')

#*(331)-3
G1 = merge(star(math.inf, [ 11, 13, 19]), star(16, [( 3-inc)%(14*t+7),( 5-inc)%(14*t+7), 6]), path([( 2-inc)%(14*t+7), 15]))
G2 = merge(star(math.inf, [ 2, 3, 15]), star(8, [ (20+inc)%(14*t+7), (19+inc)%(14*t+7), 18]), path([ 1, 10]))
G3 = merge(star(11, [ 20, 2,( 0-inc)%(14*t+7)]), star(14, [ 6,( 3-inc)%(14*t+7),( 1-inc)%(14*t+7)]), path([( 5-inc)%(14*t+7), 18]))
G4 = merge(star(17, [( 6-inc)%(14*t+7),( 5-inc)%(14*t+7),( 4-inc)%(14*t+7)]), star(7, [ math.inf, (19+inc)%(14*t+7), 16]), path([ 12, 20]))
G5 = merge(star(0, [ 4, 5, 6]), star(9, [ 10, 11, 12]), path([ 1, 8]))

F_331_3 = [ G1, G2, G3, G4, G5]
#visualize(14*t+7, F_331_3,  '(331)-3',  'C:\\Users\\baneg\\OneDrive\\Desktop\\Git\\Python\\Research\\8 (mod 14)\\texgraph')

#! (322)

#*(322)-1
G1 = merge(path([ 1, math.inf, 0, 9]), path([( 6-inc)%(14*t+7), 18, 8]), path([ 10, 2, 12]))
G2 = merge(path([ 9, math.inf, 3, 11]), path([ 5, 13,( 2-inc)%(14*t+7)]), path([ 19,( 8-inc)%(14*t+7), 20]))
G3 = merge(path([ 18, math.inf, 5, 14]), path([ 3, 12, 4]), path([ 8, 0, (11+inc)%(14*t+7)]))
G4 = merge(path([ (13+inc)%(14*t+7), 0, 10, 1]), path([ 8, 16,( 4-inc)%(14*t+7)]), path([ (17+inc)%(14*t+7), 6, math.inf]))
G5 = merge(path([ 0, 6, 1, 5]), path([ 8, 10, 9]), path([ 11, 4, 7]))

F_322_1 = [ G1, G2, G3, G4, G5]
#visualize(14*t+7, F_322_1,  '(322)-1',  'C:\\Users\\baneg\\OneDrive\\Desktop\\Git\\Python\\Research\\8 (mod 14)\\texgraph')

#*(322)-2
G1 = merge(star((16+inc)%(14*t+7), [ 3, 5,( 6+inc)%(14*t+7)]), path([ 1, math.inf, 7]), path([ (12+inc)%(14*t+7), 0, 9]))
G2 = merge(star(8, [ (20+inc)%(14*t+7), (19+inc)%(14*t+7), 18]), path([ 2, math.inf, 10]), path([ (15+inc)%(14*t+7), 3, 11]))
G3 = merge(star(14, [( 1-inc)%(14*t+7),( 3-inc)%(14*t+7), 6]), path([( 0-inc)%(14*t+7), 11, 20]), path([ 8, 16,( 4-inc)%(14*t+7)]))
G4 = merge(star(math.inf, [ 20, 5, 4]), path([ 11, 19,( 6-inc)%(14*t+7)]), path([ 13, 3, 12]))
G5 = merge(star(0, [ 6, 5, 4]), path([ 1, 8, 7]), path([ 11, 9, 12]))

F_322_2 = [ G1, G2, G3, G4, G5]
#visualize(14*t+7, F_322_2,  '(322)-2',  'C:\\Users\\baneg\\OneDrive\\Desktop\\Git\\Python\\Research\\8 (mod 14)\\texgraph')

#! (3211)

#*(3211)-1
G1 = merge(path([ 1, math.inf, 0, 9]), path([ 12, 2, 10]), path([ 5, 13]), path([ 6, 16]))
G2 = merge(path([ 2, math.inf, 3, 11]), path([ (18+inc)%(14*t+7), 6, 15]), path([ 1, (12+inc)%(14*t+7)]), path([ 0, 8]))
G3 = merge(path([( 0-inc)%(14*t+7), 11, 2, (15+inc)%(14*t+7)]), path([ 5, math.inf, 4]), path([ 7, (19+inc)%(14*t+7)]), path([ 8, 18]))
G4 = merge(path([ (18+inc)%(14*t+7), 5, (17+inc)%(14*t+7), 6]), path([ 10, 0, (13+inc)%(14*t+7)]), path([ 3, (15+inc)%(14*t+7)]), path([ math.inf, 20]))
G5 = merge(path([ 0, 6, 1, 5]), path([ 8, 10, 7]), path([ 4, 11]), path([ 2, 3]))

F_3211_1 = [ G1, G2, G3, G4, G5]
#visualize(14*t+7, F_3211_1,  '(3211)-1',  'C:\\Users\\baneg\\OneDrive\\Desktop\\Git\\Python\\Research\\8 (mod 14)\\texgraph')

#*(3211)-2
G1 = merge(star(16, [( 3-inc)%(14*t+7),( 5-inc)%(14*t+7), 6]), path([ math.inf, 0, 9]), path([( 1-inc)%(14*t+7), 13]), path([( 2-inc)%(14*t+7), 15]))
G2 = merge(star(math.inf, [ 2, 3, 15]), path([ 18, 8, (19+inc)%(14*t+7)]), path([ 1, 10]), path([ 0, (12+inc)%(14*t+7)]))
G3 = merge(star(11, [( 0-inc)%(14*t+7), 2, 20]), path([ 6, 14,( 3-inc)%(14*t+7)]), path([( 5-inc)%(14*t+7), 18]), path([ 7, 15]))
G4 = merge(star(math.inf, [ 11, 13, 19]), path([ 6, (17+inc)%(14*t+7), 5]), path([ 10, 18]), path([ 12, 20]))
G5 = merge(star(0, [ 4, 5, 6]), path([ 11, 9, 12]), path([ 2, 3]), path([ 1, 8]))

F_3211_2 = [ G1, G2, G3, G4, G5]
#visualize(14*t+7, F_3211_2,  '(3211)-2',  'C:\\Users\\baneg\\OneDrive\\Desktop\\Git\\Python\\Research\\8 (mod 14)\\texgraph')

#! (4111)

#*(4111)-1
G1 = merge(path([ 11, 1, math.inf, 7, 16]), path([ 2, 10]), path([ 9, 19]), path([ 5, 13]))
G2 = merge(path([ 13,( 2-inc)%(14*t+7), math.inf, 3, 11]), path([( 6-inc)%(14*t+7), 18]), path([( 8-inc)%(14*t+7), 20]), path([( 1-inc)%(14*t+7), 12]))
G3 = merge(path([ 12, 4, math.inf, 5, 14]), path([ 0, 8]), path([( 7-inc)%(14*t+7), 18]), path([ 2, 11]))
G4 = merge(path([ (13+inc)%(14*t+7), 0, 10, 1, 9]), path([ 6, (17+inc)%(14*t+7)]), path([ 3, 12]), path([ 20, math.inf]))
G5 = merge(path([ 0, 6, 1, 5, 2]), path([ 3, 10]), path([ 7, 9]), path([ 11, 12]))

F_4111_1 = [ G1, G2, G3, G4, G5]
#visualize(14*t+7, F_4111_1,  '(4111)-1',  'C:\\Users\\baneg\\OneDrive\\Desktop\\Git\\Python\\Research\\8 (mod 14)\\texgraph')

#*(4111)-2
G1 = merge(path([ 11, 1, math.inf, 0]), path([ 1, 9]), path([ 3, (16+inc)%(14*t+7)]), path([ 5, 13]), path([ 2, 12]))
G2 = merge(path([ (13+inc)%(14*t+7), 2, math.inf, 3]), path([ 2, 11]), path([ 8, (20+inc)%(14*t+7)]), path([ 6, (18+inc)%(14*t+7)]), path([ 1, (12+inc)%(14*t+7)]))
G3 = merge(path([ 12, 4, math.inf, 19]), path([ 4, (17+inc)%(14*t+7)]), path([ 7, (18+inc)%(14*t+7)]), path([ 0, 8]), path([ 5, 14]))
G4 = merge(path([ (13+inc)%(14*t+7), 0, 10, 1]), path([ 0, 9]), path([ 6, (17+inc)%(14*t+7)]), path([ 3, 12]), path([ 20, math.inf]))
G5 = merge(path([ 4, 8, 1, 7]), path([ 1, 6]), path([ 3, 5]), path([ 9, 12]), path([ 10, 11]))

F_4111_2 = [ G1, G2, G3, G4, G5]
#visualize(14*t+7, F_4111_2,  '(4111)-2',  'C:\\Users\\baneg\\OneDrive\\Desktop\\Git\\Python\\Research\\8 (mod 14)\\texgraph')

#*(4111)-3
G1 = merge(star(16, [ 7, 6,( 5-inc)%(14*t+7),( 4-inc)%(14*t+7)]), path([ 10, 18]), path([( 0-inc)%(14*t+7), 12]), path([ 14, math.inf]))
G2 = merge(star(8, [ (20+inc)%(14*t+7), (19+inc)%(14*t+7), 18, 17]), path([ 5, 13]), path([ 2, math.inf]), path([ 1, 9]))
G3 = merge(star(14, [ 6, 4,( 3-inc)%(14*t+7),( 1-inc)%(14*t+7)]), path([ 10, math.inf]), path([ 9, 17]), path([ 11, 20]))
G4 = merge(star(math.inf, [ 20, 12, 4, 1]), path([ 3, 13]), path([ 5, (17+inc)%(14*t+7)]), path([ 11, 19]))
G5 = merge(star(0, [ 6, 5, 4, 3]), path([ 1, 8]), path([ 10, 11]), path([ 7, 9]))

F_4111_3 = [ G1, G2, G3, G4, G5]
#visualize(14*t+7, F_4111_3,  '(4111)-3',  'C:\\Users\\baneg\\OneDrive\\Desktop\\Git\\Python\\Research\\8 (mod 14)\\texgraph')

#! (2221)

#*(2221)-1
G1 = merge(path([ 1, math.inf, 0]), path([ 8, 18,( 6-inc)%(14*t+7)]), path([ 10, 2, 12]), path([ 7, 16]))
G2 = merge(path([ 9, math.inf, 3]), path([( 2-inc)%(14*t+7), 13, 5]), path([ 19,( 8-inc)%(14*t+7), 20]), path([ 10, 18]))
G3 = merge(path([ 18, math.inf, 5]), path([ 3, 12, 4]), path([ 8, 0, (11+inc)%(14*t+7)]), path([ 7, (19+inc)%(14*t+7)]))
G4 = merge(path([ 1, 10, 0]), path([ 8, 16,( 4-inc)%(14*t+7)]), path([ 17,( 6-inc)%(14*t+7), math.inf]), path([( 7-inc)%(14*t+7), 20]))
G5 = merge(path([ 0, 6, 1]), path([ 4, 8, 5]), path([ 2, 9, 7]), path([ 10, 11]))

F_2221_1 = [ G1, G2, G3, G4, G5]
#visualize(14*t+7, F_2221_1,  '(2221)-1',  'C:\\Users\\baneg\\OneDrive\\Desktop\\Git\\Python\\Research\\8 (mod 14)\\texgraph')


#! (31111)

#*(31111)-1
G1 = merge(path([ 8, math.inf, 0, 9]), path([ 1, 11]), path([( 6-inc)%(14*t+7), 18]), path([ 2, 10]), path([( 5-inc)%(14*t+7), 16]))
G2 = merge(path([ 9, math.inf, 3, 11]), path([ 6, 16]), path([ 5, 13]), path([( 1-inc)%(14*t+7), 12]), path([( 8-inc)%(14*t+7), 20]))
G3 = merge(path([ 11, math.inf, 5, 14]), path([ 10, 19]), path([( 7-inc)%(14*t+7), 18]), path([ 4, 12]), path([ 0, 8]))
G4 = merge(path([ 1, 10, 0, (13+inc)%(14*t+7)]), path([ 2, (15+inc)%(14*t+7)]), path([ 6, (17+inc)%(14*t+7)]), path([ 4, (16+inc)%(14*t+7)]), path([ 20, math.inf]))
G5 = merge(path([ 0, 6, 1, 5]), path([ 2, 9]), path([ 8, 10]), path([ 4, 7]), path([ 11, 12]))

F_31111_1 = [ G1, G2, G3, G4, G5]
#visualize(14*t+7, F_31111_1,  '(31111)-1',  'C:\\Users\\baneg\\OneDrive\\Desktop\\Git\\Python\\Research\\8 (mod 14)\\texgraph')

#*(31111)-2
G1 = merge(star(math.inf, [ 19, 13, 11]), path([ 1, 10]), path([ 8, (20+inc)%(14*t+7)]), path([ 5, (16+inc)%(14*t+7)]), path([ 2, (15+inc)%(14*t+7)]))
G2 = merge(star(math.inf, [ 3, 8, 16]), path([ 1, 11]), path([ 5, 15]), path([ 9, (20+inc)%(14*t+7)]), path([ 4, 12]))
G3 = merge(star(14, [ 6,( 3-inc)%(14*t+7),( 1-inc)%(14*t+7)]), path([( 0-inc)%(14*t+7), 11]), path([ 4, 13]), path([ 9, 18]), path([ 2, 10]))
G4 = merge(star(17, [( 6-inc)%(14*t+7),( 5-inc)%(14*t+7),( 4-inc)%(14*t+7)]), path([ 0, math.inf]), path([( 7-inc)%(14*t+7), 19]), path([( 2-inc)%(14*t+7), 14]), path([ 12, 20]))
G5 = merge(star(0, [ 6, 5, 4]), path([ 2, 3]), path([ 9, 11]), path([ 1, 8]), path([ 7, 10]))

F_31111_2 = [ G1, G2, G3, G4, G5]
#visualize(14*t+7, F_31111_2,  '(31111)-2',  'C:\\Users\\baneg\\OneDrive\\Desktop\\Git\\Python\\Research\\8 (mod 14)\\texgraph')


#! (22111)

#*(22111)-1
G1 = merge(path([ 11, math.inf, 13]), path([ 14, 6, (17+inc)%(14*t+7)]), path([ 1, 10]), path([ 5, (16+inc)%(14*t+7)]), path([ 8, (20+inc)%(14*t+7)]))
G2 = merge(path([ 16, math.inf, 3]), path([( 2-inc)%(14*t+7), 15, 5]), path([ 1, 11]), path([( 9-inc)%(14*t+7), 20]), path([ 4, 12]))
G3 = merge(path([( 1-inc)%(14*t+7), 14,( 3-inc)%(14*t+7)]), path([( 0-inc)%(14*t+7), 11, 20]), path([ 9, 18]), path([ 2, 10]), path([ 5, math.inf]))
G4 = merge(path([ 4, (17+inc)%(14*t+7), 5]), path([ 0, math.inf, 8]), path([ 2, (14+inc)%(14*t+7)]), path([ 7, (19+inc)%(14*t+7)]), path([ 12, 20]))
G5 = merge(path([ 0, 6, 1]), path([ 4, 8, 5]), path([ 3, 10]), path([ 7, 9]), path([ 11, 12]))

F_22111_1 = [ G1, G2, G3, G4, G5]
#visualize(14*t+7, F_22111_1,  '(22111)-1',  'C:\\Users\\baneg\\OneDrive\\Desktop\\Git\\Python\\Research\\8 (mod 14)\\texgraph')

#! (211111)

#*(211111)-1
G1 = merge(path([ 11, math.inf, 13]), path([ 4, 12]), path([( 6-inc)%(14*t+7), 17]), path([ 1, 10]), path([( 5-inc)%(14*t+7), 16]), path([( 8-inc)%(14*t+7), 20]))
G2 = merge(path([ 16, math.inf, 3]), path([ 1, 9]), path([ 5, 15]), path([ 8, 18]), path([( 2-inc)%(14*t+7), 13]), path([ 6, 14]))
G3 = merge(path([( 0-inc)%(14*t+7), 11, 20]), path([( 1-inc)%(14*t+7), 14]), path([ 7, 17]), path([ 9, 18]), path([ 2, 10]), path([ 5, math.inf]))
G4 = merge(path([ 0, math.inf, 8]), path([ 10, 18]), path([( 5-inc)%(14*t+7), 17]), path([( 2-inc)%(14*t+7), 14]), path([( 7-inc)%(14*t+7), 19]), path([ 12, 20]))
G5 = merge(path([ 0, 6, 1]), path([ 4, 8]), path([ 2, 5]), path([ 3, 10]), path([ 7, 9]), path([ 11, 12]))

F_211111_1 = [ G1, G2, G3, G4, G5]
#visualize(14*t+7, F_211111_1,  '(14*t+71111)-1',  'C:\\Users\\baneg\\OneDrive\\Desktop\\Git\\Python\\Research\\8 (mod 14)\\texgraph')
#& above here is generalized

#example:

G = merge(path([ ((7-inc)%(14*t+7))%(14*t+7), 18]), path([ 2, ((14+inc)%(14*t+7))%(14*t+7)]))
#visualize(14*t+7, [G],  '(14*t+71111)-1',  'C:\\Users\\baneg\\OneDrive\\Desktop\\Git\\Python\\Research\\8 (mod 14)\\texgraph')