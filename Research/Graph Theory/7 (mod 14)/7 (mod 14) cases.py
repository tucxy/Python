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

#notebook
t = 50
inc = 14*(t-1)

#? 7 (mod 14)

#! (61)

#*(61)-1
G1  = merge(path([10,0,9,1,14+inc,5+inc,15+inc]), path([3,13]))
G2  = merge(path([14,4,13,5,18+inc,8+inc,17+inc]), path([3,12]))
G3  = merge(path([12,2,11,3,16+inc,6+inc,15+inc]), path([0,13+inc]))
G4 = merge(path([0,6,1,5, 2, 9, 7]), path([3,4]))

F_61_1 = [G1,G2,G3,G4] #defines the decomposition 'object' a list of graph labelings
#visualize(14*t+7,F_61_1, '(61)-1', 'C:\\Users\\baneg\\OneDrive\\Desktop\\Git\\Python\\Research\\7 (mod 14)\\texgraph')

#*(61)-2
G1 = merge(path([15,5,14,1-inc,9-inc,0-inc]),path([1-inc,11-inc]), path([2,10]))
G2 = merge(path([14,4,13,5,18+inc,9+inc]),path([5,16+inc]), path([3,12]))
G3 = merge(path([7,20+inc,8,17,6-inc,16-inc]),path([4-inc,17]), path([0,10]))
G4 = merge(path([0,6,1,5,2,9]),path([5,3]), path([7,8]))

F_61_2 = [G1,G2,G3,G4]
#visualize(14*t+7,F_61_2, '(61)-2', 'C:\\Users\\baneg\\OneDrive\\Desktop\\Git\\Python\\Research\\7 (mod 14)\\texgraph')


#*(61)-3
G1  = merge(path([0-inc,9-inc,1-inc,14,5,17+inc]),path([5,15]), path([2,12]))
G2  = merge(path([8+inc,18+inc,5,13,4,14]),path([4,16+inc]), path([7,20+inc]))
G3  = merge(path([14,3-inc,16,6,17+inc,8+inc]),path([4,17+inc]), path([1,13+inc]))
G4  = merge(path([0,6,1,5,2,9]),path([2,4]), path([7,8]))

F_61_3 = [G1,G2,G3,G4]
#visualize(14*t+7,F_61_3, '(61)-3', 'C:\\Users\\baneg\\OneDrive\\Desktop\\Git\\Python\\Research\\7 (mod 14)\\texgraph')
#& above here is generalized
#*(61)-4

G1 = merge(star(5,[16,15,17,14]),path([14,1,9]), path([0,13]))
G2 = merge(star(4,[14,15,16,13]),path([13,5,18]), path([7,17]))
G3 = merge(star(17,[4,9,8,6]),path([6,16,7]), path([1,13]))
G4 = merge(star(1,[5,6,7,4]),path([9,2,4]), path([11,10]))

F_61_4 = [G1,G2,G3,G4]
#visualize(14*t+7,F_61_4, '(61)-4', 'C:\\Users\\baneg\\OneDrive\\Desktop\\Git\\Python\\Research\\7 (mod 14)\\texgraph')

#*(61)-5
G1 = merge(path([1,14,5,15,2]),path([16,5,17]), path([9,20]))
G2 = merge(path([6,14,4,16,3]),path([15,4,13]), path([0,9]))
G3 = merge(path([12,4,17,6,15]),path([8,17,7]), path([5,13]))
G4 = merge(path([3,8,1,4,2]),path([5,1,7]), path([9,10]))

F_61_5 = [G1,G2,G3,G4]
#visualize(14*t+7,F_61_5, '(61)-5', 'C:\\Users\\baneg\\OneDrive\\Desktop\\Git\\Python\\Research\\7 (mod 14)\\texgraph')

#*(61)-6
G1 = merge(star(1,[13,10,14]),star(5,[14,16,15]),path([3,11]))
G2 = merge(star(5,[17,18,13]),star(4,[14,15,13]),path([9,20]))
G3 = merge(star(9,[1,18,17]),star(7,[16,20,17]),path([3,13]))
G4 = merge(star(8,[7,4,1]),star(6,[1,0,3]),path([9,11]))

F_61_6 = [G1,G2,G3,G4]
#visualize(14*t+7,F_61_6, '(61)-6', 'C:\\Users\\baneg\\OneDrive\\Desktop\\Git\\Python\\Research\\7 (mod 14)\\texgraph')

#*(61)-7
G1 = merge(star(5,[16,14,17,15]),path([7,15,2]),path([1,10]))
G2 = merge(star(14,[4,2,3,6]),path([15,6,19]),path([9,17]))
G3 = merge(star(4,[16,12,17,13]),path([3,13,2]),path([1,11]))
G4 = merge(star(1,[8,5,6,7]),path([3,6,4]),path([9,10]))

F_61_7 = [G1,G2,G3,G4]
#visualize(14*t+7,F_61_7, '(61)-7', 'C:\\Users\\baneg\\OneDrive\\Desktop\\Git\\Python\\Research\\7 (mod 14)\\texgraph')

#*(61)-8
G1 = merge(star(15,[7,6,5,3,2]),path([2,13]),path([12,20]))
G2 = merge(star(14,[6,5,4,3,2]),path([2,10]),path([9,19]))
G3 = merge(star(4,[16,15,12,13,17]),path([17,6]),path([10,19]))
G4 = merge(star(1,[5,6,7,8,4]),path([3,5,1]),path([9,10]))

F_61_8 = [G1,G2,G3,G4]
#visualize(14*t+7,F_61_8, '(61)-8', 'C:\\Users\\baneg\\OneDrive\\Desktop\\Git\\Python\\Research\\7 (mod 14)\\texgraph')

#*(61)-9
G1 = merge(path([20,10,0,8,16]),path([0,9,18]),path([3,11]))
G2 = merge(path([6,14,4,12,2]),path([4,13,1]),path([5,15]))
G3 = merge(path([13,2,10,19,6]),path([10,1,11]),path([5,14]))
G4 = merge(path([5,11,9,12,7]),path([9,10,6]),path([1,8]))

F_61_9 = [G1,G2,G3,G4]
#visualize(14*t+7,F_61_9, '(61)-9', 'C:\\Users\\baneg\\OneDrive\\Desktop\\Git\\Python\\Research\\7 (mod 14)\\texgraph')

#*(61)-10
G1 = merge(star(5,[17,16,15]),path([7,15,2,14]),path([4,12]))
G2 = merge(star(14,[4,3,6]),path([15,6,19,7]),path([1,10]))
G3 = merge(star(13,[3,2,4]),path([16,4,17,9]),path([1,11]))
G4 = merge(star(8,[1,4,5]), path([3,1,6,0]),path([9,10]))

F_61_10 = [G1,G2,G3,G4]
#visualize(14*t+7,F_61_10, '(61)-10', 'C:\\Users\\baneg\\OneDrive\\Desktop\\Git\\Python\\Research\\7 (mod 14)\\texgraph')

#! (52)

#*(52)-1
G1 = merge(path([0,9,1,14,5,15]), path([17,7,20]))
G2 = merge(path([14,4,13,5,18,8]), path([12,3,15]))
G3 = merge(path([12,2,11,3,16,6]), path([10,20,8]))
G4 = merge(path([0,6,1,5,2,9]),path([12,10,11]))

F_52_1 = [G1,G2,G3,G4]
#visualize(14*t+7,F_52_1, '(52)-1', 'C:\\Users\\baneg\\OneDrive\\Desktop\\Git\\Python\\Research\\7 (mod 14)\\texgraph')

#*(52)-2
G1 = merge(path([9,1,14,5,16]),path([5,15]),path([7,20,8]))
G2 = merge(path([18,5,13,4,14]),path([4,16]),path([9,0,10]))
G3 = merge(path([3,16,6,17,4]),path([17,5]),path([10,1,11]))
G4 = merge(path([4,8,1,6,3]),path([0,6]),path([10,9,11]))

F_52_2 = [G1,G2,G3,G4]
#visualize(14*t+7,F_52_2, '(52)-2', 'C:\\Users\\baneg\\OneDrive\\Desktop\\Git\\Python\\Research\\7 (mod 14)\\texgraph')

#*(52)-3
G1 = merge(path([1,14,5,15,2]),path([5,17]),path([9,19,6]))
G2 = merge(path([6,14,4,16,3]),path([4,13]),path([0,9,20]))
G3 = merge(path([12,4,17,6,15]),path([7,17]),path([11,1,10]))
G4 = merge(path([5,11,9,12,7]),path([9,10]),path([1,8,4]))

F_52_3 = [G1,G2,G3,G4]
#visualize(14*t+7,F_52_3, '(52)-3', 'C:\\Users\\baneg\\OneDrive\\Desktop\\Git\\Python\\Research\\7 (mod 14)\\texgraph')

#*(52)-4
G1 = merge(path([16,5,15,7]),path([17,5,15,2]), path([12,0,9]))
G2 = merge(path([4,14,6,15]),path([3,14,6,19]), path([1,10,2]))
G3 = merge(path([3,13,4,16]),path([2,13,4,17]), path([8,18,5]))
G4 = merge(path([3,8,1,7]),path([4,8,1,6]), path([10,9,11]))

F_52_4 = [G1,G2,G3,G4]
#visualize(14*t+7,F_52_4, '(52)-4', 'C:\\Users\\baneg\\OneDrive\\Desktop\\Git\\Python\\Research\\7 (mod 14)\\texgraph')

#*(52)-5
G1 = merge(star(5,[17,16,15,14]),path([14,1]),path([7,20,8]))
G2 = merge(star(4,[16,14,13,12]),path([13,5]),path([9,1,11]))
G3 = merge(star(17,[9,8,6,4]),path([6,16]),path([2,14,3]))
G4 = merge(star(1,[8,5,4,7]),path([8,3]),path([10,9,11]))

F_52_5 = [G1,G2,G3,G4]
#visualize(14*t+7,F_52_5, '(52)-5', 'C:\\Users\\baneg\\OneDrive\\Desktop\\Git\\Python\\Research\\7 (mod 14)\\texgraph')

#*(52)-6
G1 = merge(star(0,[13,12,10,9,8]),path([17,6,19]))
G2 = merge(star(2,[15,13,12,10,11]),path([20,8,17]))
G3 = merge(star(4,[17,15,14,13,12]),path([8,19,10]))
G4 = merge(star(1,[4,5,6,7,8]),path([10,9,11]))

F_52_6 = [G1,G2,G3,G4]
#visualize(14*t+7,F_52_6, '(52)-6', 'C:\\Users\\baneg\\OneDrive\\Desktop\\Git\\Python\\Research\\7 (mod 14)\\texgraph')

#! (43)

#*(43)-1
G1 = merge(path([15,5,14,6,17]),path([10,0,9,1]))
G2 = merge(path([14,4,13,5,17]),path([11,1,10,2]))
G3 = merge(path([4,12,2,11,3]),path([16,6,15,7]))
G4 = merge(path([0,6,1,5,2]),path([3,10,8,9]))

F_43_1 = [G1,G2,G3,G4]
#visualize(14*t+7,F_43_1, '(43)-1', 'C:\\Users\\baneg\\OneDrive\\Desktop\\Git\\Python\\Research\\7 (mod 14)\\texgraph')

#*(43)-2
G1 = merge(path([6,14,5,15]),path([5,17]),path([10,0,9,1]))
G2 = merge(path([14,4,13,5]),path([3,13]),path([11,1,10,2]))
G3 = merge(path([12,2,11,3]),path([19,11]),path([16,6,15,7]))
G4 = merge(path([5,8,1,7]),path([1,6]), path([0,4,2,3]))

F_43_2 = [G1,G2,G3,G4]
#visualize(14*t+7,F_43_2, '(43)-2', 'C:\\Users\\baneg\\OneDrive\\Desktop\\Git\\Python\\Research\\7 (mod 14)\\texgraph')

#*(43)-3
G1 = merge(path([14,4,13,5]),path([1,13]),star(0,[10,9,8]))
G2 = merge(path([6,14,5,15]),path([5,18]),star(1,[11,10,9]))
G3 = merge(path([16,5,17,6]),path([4,17]),star(2,[13,11,10]))
G4 = merge(path([4,8,1,7]),path([1,6]),star(9,[10,12,11]))

F_43_3 = [G1,G2,G3,G4]
#visualize(14*t+7,F_43_3, '(43)-3', 'C:\\Users\\baneg\\OneDrive\\Desktop\\Git\\Python\\Research\\7 (mod 14)\\texgraph')

#*(43)-4
G1 = merge(star(0,[12,10,9,8]),path([3,13,5,17]))
G2 = merge(star(4,[17,14,13,12]),path([7,20,8,19]))
G3 = merge(star(2,[15,13,12,11]),path([9,17,8,18]))
G4 = merge(star(0,[6,5,4,3]),path([2,9,7,8]))

F_43_4 = [G1,G2,G3,G4]
#visualize(14*t+7,F_43_4, '(43)-4', 'C:\\Users\\baneg\\OneDrive\\Desktop\\Git\\Python\\Research\\7 (mod 14)\\texgraph')

#*(43)-5
G1 = merge(star(0,[12,9,8]),path([14,3,13,5,17]))
G2 = merge(star(4,[17,13,12]),path([18,7,20,8,19]))
G3 = merge(star(2,[15,13,11]),path([19,9,17,8,18]))
G4 = merge(star(9,[12,11,10]),path([4,8,1,7,2]))

F_43_5 = [G1,G2,G3,G4]
#visualize(14*t+7,F_43_5, '(43)-5', 'C:\\Users\\baneg\\OneDrive\\Desktop\\Git\\Python\\Research\\7 (mod 14)\\texgraph')

#*(43)-6
G1 = merge(star(5,[17,15,14,13]),star(0,[10,9,8]))
G2 = merge(star(4,[17,14,13,12]),star(1,[11,10,9]))
G3 = merge(star(6,[17,16,15,14]),star(2,[12,11,10]))
G4 = merge(star(0,[6,5,4,3]),star(9,[8,7,2]))

F_43_6 = [G1,G2,G3,G4]
#visualize(14*t+7,F_43_6, '(43)-6', 'C:\\Users\\baneg\\OneDrive\\Desktop\\Git\\Python\\Research\\7 (mod 14)\\texgraph')

#! (511)

#*(511)-1
G1 = merge(path([0,9,1,14,5,15]),path([3,13]),path([7,17]))
G2 = merge(path([14,4,13,5,18,8]),path([3,12]),path([1,10]))
G3 = merge(path([12,2,11,3,16,6]),path([8,20]),path([0,13]))
G4 = merge(path([0,6,1,5,2,9]),path([8,10]),path([3,4]))

F_511_1 = [G1,G2,G3,G4]
#visualize(14*t+7,F_511_1, '(511)-1', 'C:\\Users\\baneg\\OneDrive\\Desktop\\Git\\Python\\Research\\7 (mod 14)\\texgraph')

#*(511)-2
G1 = merge(path([16,5,14,1,9]),path([5,15]),path([8,20]),path([0,13]))
G2 = merge(path([14,4,13,5,18]),path([4,16]),path([7,17]),path([0,9]))
G3 = merge(path([4,17,6,16,3]),path([5,17]),path([1,10]),path([8,18]))
G4 = merge(path([3,6,1,8,4]),path([6,0]),path([5,7]),path([9,10]))

F_511_2 = [G1,G2,G3,G4]
#visualize(14*t+7,F_511_2, '(511)-2', 'C:\\Users\\baneg\\OneDrive\\Desktop\\Git\\Python\\Research\\7 (mod 14)\\texgraph')

#*(511)-3
G1 = merge(star(5,[17,16,15,14]),path([1,14]),path([8,20]),path([0,13]))
G2 = merge(star(4,[16,14,13,12]),path([5,13]),path([1,9]),path([8,18]))
G3 = merge(star(17,[9,8,6,4]),path([6,16]),path([2,14]),path([0,10]))
G4 = merge(star(1,[4,5,8,7]),path([8,3]),path([0,2]),path([9,10]))

F_511_3 = [G1,G2,G3,G4]
#visualize(14*t+7,F_511_3, '(511)-3', 'C:\\Users\\baneg\\OneDrive\\Desktop\\Git\\Python\\Research\\7 (mod 14)\\texgraph')

#*(511)-4
G1 = merge(path([16,5,15,7]),path([17,5,15,2]), path([0,9]),path([1,10])) #7-19
G2 = merge(path([4,14,6,15]),path([3,14,6,19]), path([2,10]),path([0,12])) #8-17
G3 = merge(path([3,13,4,16]),path([2,13,4,17]), path([5,18]),path([1,11]))
G4 = merge(path([5,8,1,7]),path([4,8,1,6]), path([0,2]),path([9,10]))

F_511_4 = [G1,G2,G3,G4]
#visualize(14*t+7,F_511_4, '(511)-4', 'C:\\Users\\baneg\\OneDrive\\Desktop\\Git\\Python\\Research\\7 (mod 14)\\texgraph')

#*(511)-5
G1 = merge(path([1,14,5,15,2]),path([5,17]),path([9,19]),path([12,20]))
G2 = merge(path([6,14,4,16,3]),path([4,13]),path([1,10]),path([8,18]))
G3 = merge(path([12,4,17,6,15]),path([7,17]),path([0,9]),path([2,13]))
G4 = merge(path([5,11,9,12,7]),path([9,10]),path([1,8]),path([0,4]))

F_511_5 = [G1,G2,G3,G4]
#visualize(14*t+7,F_511_5, '(511)-5', 'C:\\Users\\baneg\\OneDrive\\Desktop\\Git\\Python\\Research\\7 (mod 14)\\texgraph')

#*(511)-6
G1 = merge(star(0,[13,12,10,9,8]),path([6,17]),path([5,15]))
G2 = merge(star(2,[15,13,12,11,10]),path([6,19]),path([8,17]))
G3 = merge(star(4,[17,15,14,13,12]),path([10,19]),path([8,20]))
G4 = merge(star(1,[4,5,6,7,8]),path([2,3]),path([9,11]))

F_511_6 = [G1,G2,G3,G4]
#visualize(14*t+7,F_511_6, '(511)-6', 'C:\\Users\\baneg\\OneDrive\\Desktop\\Git\\Python\\Research\\7 (mod 14)\\texgraph')

#! (421)

#*(421)-1
G1 = merge(path([15,5,14,6,17]),path([10,0,9]),path([8,16]))
G2 = merge(path([14,4,13,5,17]),path([1,10,2]),path([8,18]))
G3 = merge(path([4,12,2,11,3]),path([16,6,15]),path([1,14]))
G4 = merge(path([0,6,1,5,2]),path([8,10,9]),path([4,11]))

F_421_1 = [G1,G2,G3,G4]
#visualize(14*t+7,F_421_1, '(421)-1', 'C:\\Users\\baneg\\OneDrive\\Desktop\\Git\\Python\\Research\\7 (mod 14)\\texgraph')

#*(421)-2
G1 = merge(path([6,14,5,15]),path([5,17]),path([10,0,9]),path([8,16]))
G2 = merge(path([14,4,13,5]),path([3,13]),path([1,10,2]),path([8,18]))
G3 = merge(path([12,2,11,3]),path([11,19]),path([16,6,15]),path([1,14]))
G4 = merge(path([5,8,1,7]),path([1,6]),path([10,9,11]),path([0,4]))

F_421_2 = [G1,G2,G3,G4]
#visualize(14*t+7,F_421_2, '(421)-2', 'C:\\Users\\baneg\\OneDrive\\Desktop\\Git\\Python\\Research\\7 (mod 14)\\texgraph')

#*(421)-3
G1 = merge(star(0,[12,10,9,8]),path([3,13,5]),path([7,20]))
G2 = merge(star(4,[17,14,13,12]),path([20,8,18]),path([19,10]))
G3 = merge(star(2,[15,13,12,11]),path([17,8,19]),path([3,16]))
G4 = merge(star(0,[6,5,4,3]),path([1,8,7]),path([9,11]))

F_421_3 = [G1,G2,G3,G4]
#visualize(14*t+7,F_421_3, '(421)-3', 'C:\\Users\\baneg\\OneDrive\\Desktop\\Git\\Python\\Research\\7 (mod 14)\\texgraph')

#! (331)

#*(331)-1
G1 = merge(path([15,5,14,6]),path([10,0,9,1]),path([4,12]))
G2 = merge(path([14,4,13,5]),path([11,1,10,2]),path([3,12]))
G3 = merge(path([16,6,15,7]),path([12,2,11,3]),path([10,20]))
G4 = merge(path([0,6,1,5]),path([2,9,7,10]),path([3,4]))

F_331_1 = [G1,G2,G3,G4]
#visualize(14*t+7,F_331_1, '(331)-1', 'C:\\Users\\baneg\\OneDrive\\Desktop\\Git\\Python\\Research\\7 (mod 14)\\texgraph')

#*(331)-2
G1 = merge(star(0,[10,9,8]),path([14,4,13,5]),path([11,19]))
G2 = merge(star(1,[11,10,9]),path([15,5,14,6]),path([3,13]))
G3 = merge(star(2,[13,11,10]),path([16,5,17,4]),path([6,15]))
G4 = merge(star(0,[4,5,6]),path([11,9,10,7]),path([1,8]))

F_331_2 = [G1,G2,G3,G4]
#visualize(14*t+7,F_331_2, '(331)-2', 'C:\\Users\\baneg\\OneDrive\\Desktop\\Git\\Python\\Research\\7 (mod 14)\\texgraph')

#*(331)-3
G1 = merge(star(0,[10,9,8]),star(5,[15,14,13]),path([3,11]))
G2 = merge(star(4,[14,13,12]),star(1,[11,10,9]),path([5,17]))
G3 = merge(star(2,[12,11,10]),star(6,[16,15,14]),path([3,13]))
G4 = merge(star(0,[4,5,6]),star(9,[10,11,12]),path([1,8]))

F_331_3 = [G1,G2,G3,G4]
#visualize(14*t+7,F_331_3, '(331)-3', 'C:\\Users\\baneg\\OneDrive\\Desktop\\Git\\Python\\Research\\7 (mod 14)\\texgraph')

#! (322)

#*(322)-1
G1 = merge(path([10,0,9,1]),path([8,19,7]),path([14,6,17]))
G2 = merge(path([11,1,10,2]),path([7,18,6]),path([13,5,17]))
G3 = merge(path([16,6,15,7]),path([9,18,10]),path([4,12,2]))
G4 = merge(path([0,6,1,5]),path([8,10,9]),path([11,4,7]))

F_322_1 = [G1,G2,G3,G4]
#visualize(14*t+7,F_322_1, '(322)-1', 'C:\\Users\\baneg\\OneDrive\\Desktop\\Git\\Python\\Research\\7 (mod 14)\\texgraph')

#*(322)-2
G1 = merge(star(0,[10,9,8]),path([6,18,7]),path([1,13,5]))
G2 = merge(star(1,[11,10,9]),path([12,0,13]),path([6,17,4]))
G3 = merge(star(2,[13,11,10]),path([17,5,16]),path([1,12,4]))
G4 = merge(star(0,[6,5,4]),path([1,8,7]),path([11,9,12]))

F_322_2 = [G1,G2,G3,G4]
#visualize(14*t+7,F_322_2, '(322)-2', 'C:\\Users\\baneg\\OneDrive\\Desktop\\Git\\Python\\Research\\7 (mod 14)\\texgraph')

#! (3211)

#*(3211)-1
G1 = merge(path([10,0,9,1]),path([8,19,7]),path([6,14]),path([3,13]))
G2 = merge(path([11,1,10,2]),path([7,18,6]),path([12,20]),path([5,17]))
G3 = merge(path([16,6,15,7]),path([9,18,10]),path([11,19]),path([2,12]))
G4 = merge(path([0,6,1,5]),path([8,10,7]),path([4,11]),path([2,3]))

F_3211_1 = [G1,G2,G3,G4]
#visualize(14*t+7,F_3211_1, '(3211)-1', 'C:\\Users\\baneg\\OneDrive\\Desktop\\Git\\Python\\Research\\7 (mod 14)\\texgraph')

#*(3211)-2
G1 = merge(star(0,[10,9,8]),path([6,18,7]),path([1,13]),path([12,20]))
G2 = merge(star(1,[11,10,9]),path([6,17,4]),path([7,19]),path([0,13]))
G3 = merge(star(2,[13,11,10]),path([17,5,16]),path([8,19]),path([4,12]))
G4 = merge(star(0,[4,5,6]),path([11,9,12]),path([2,3]),path([1,8]))

F_3211_2 = [G1,G2,G3,G4]
#visualize(14*t+7,F_3211_2, '(3211)-2', 'C:\\Users\\baneg\\OneDrive\\Desktop\\Git\\Python\\Research\\7 (mod 14)\\texgraph')

#! (4111)

#*(4111)-1
G1 = merge(path([15,5,14,6,17]),path([0,10]),path([7,16]),path([1,9]))
G2 = merge(path([14,4,13,5,17]),path([1,10]),path([3,16]),path([8,18]))
G3 = merge(path([4,12,2,11,3]),path([9,20]),path([6,15]),path([1,14]))
G4 = merge(path([0,6,1,5,2]),path([3,10]),path([7,9]),path([11,12]))

F_4111_1 = [G1,G2,G3,G4]
#visualize(14*t+7,F_4111_1, '(4111)-1', 'C:\\Users\\baneg\\OneDrive\\Desktop\\Git\\Python\\Research\\7 (mod 14)\\texgraph')

#*(4111)-2
G1 = merge(path([6,14,5,15]),path([5,17]),path([0,10]),path([7,16]),path([1,9]))
G2 = merge(path([14,4,13,5]),path([3,13]),path([1,10]),path([9,17]),path([8,18]))
G3 = merge(path([12,2,11,3]),path([11,19]),path([9,20]),path([6,15]),path([1,14]))
G4 = merge(path([4,8,1,7]),path([1,6]),path([3,5]),path([9,12]),path([10,11]))

F_4111_2 = [G1,G2,G3,G4]
#visualize(14*t+7,F_4111_2, '(4111)-2', 'C:\\Users\\baneg\\OneDrive\\Desktop\\Git\\Python\\Research\\7 (mod 14)\\texgraph')

#*(4111)-3
G1 = merge(star(0,[12,10,9,8]),path([6,17]),path([5,13]),path([7,20]))
G2 = merge(star(4,[17,14,13,12]),path([8,20]),path([1,11]),path([19,10]))
G3 = merge(star(2,[15,13,12,11]),path([1,10]),path([8,19]),path([3,16]))
G4 = merge(star(0,[6,5,4,3]),path([1,8]),path([10,11]),path([7,9]))

F_4111_3 = [G1,G2,G3,G4]
#visualize(14*t+7,F_4111_3, '(4111)-3', 'C:\\Users\\baneg\\OneDrive\\Desktop\\Git\\Python\\Research\\7 (mod 14)\\texgraph')

#! (2221)

#*(2221)-1
G1 = merge(path([10,0,9]),path([8,19,7]),path([14,6,17]),path([2,15]))
G2 = merge(path([1,10,2]),path([7,18,6]),path([13,5,17]),path([4,15]))
G3 = merge(path([16,6,15]),path([9,18,10]),path([4,12,2]),path([0,8]))
G4 = merge(path([0,6,1]),path([4,8,5]),path([2,9,7]),path([10,11]))

F_2221_1 = [G1,G2,G3,G4]
#visualize(14*t+7,F_2221_1, '(2221)-1', 'C:\\Users\\baneg\\OneDrive\\Desktop\\Git\\Python\\Research\\7 (mod 14)\\texgraph')

#! (31111)

#*(31111)-1
G1 = merge(path([15,5,14,6]),path([0,10]),path([1,9]),path([7,16]),path([3,13]))
G2 = merge(path([4,13,5,17]),path([1,10]),path([8,18]),path([3,16]),path([0,11]))
G3 = merge(path([4,12,2,11]),path([9,20]),path([1,14]),path([6,15]),path([10,18]))
G4 = merge(path([0,6,1,5]),path([2,9]),path([8,10]),path([4,7]),path([11,12]))

F_31111_1 = [G1,G2,G3,G4]
#visualize(14*t+7,F_31111_1, '(31111)-1', 'C:\\Users\\baneg\\OneDrive\\Desktop\\Git\\Python\\Research\\7 (mod 14)\\texgraph')

#*(31111)-2
G1 = merge(star(0,[10,9,8]),path([6,18]),path([1,13]),path([4,14]),path([12,20]))
G2 = merge(star(1,[11,10,9]),path([3,13]),path([5,14]),path([4,12]),path([7,20]))
G3 = merge(star(2,[13,11,10]),path([3,12]),path([8,19]),path([5,16]),path([4,17]))
G4 = merge(star(0,[6,5,4]),path([2,3]),path([9,11]),path([1,8]),path([7,10]))

F_31111_2 = [G1,G2,G3,G4]
#visualize(14*t+7,F_31111_2, '(31111)-2', 'C:\\Users\\baneg\\OneDrive\\Desktop\\Git\\Python\\Research\\7 (mod 14)\\texgraph')

#! (22111)

#*(22111)-1
G1 = merge(path([10,0,9]),path([8,19,7]),path([6,14]),path([3,13]),path([2,15]))
G2 = merge(path([11,1,10]),path([7,18,6]),path([12,20]),path([5,17]),path([3,16]))
G3 = merge(path([16,6,15]),path([9,18,10]),path([11,19]),path([2,12]),path([0,8]))
G4 = merge(path([0,6,1]),path([4,8,5]),path([3,10]),path([7,9]),path([11,12]))

F_22111_1 = [G1,G2,G3,G4]
#visualize(14*t+7,F_22111_1, '(22111)-1', 'C:\\Users\\baneg\\OneDrive\\Desktop\\Git\\Python\\Research\\7 (mod 14)\\texgraph')

#! (211111)

#*(211111)-1
G1 = merge(path([8,0,9]),path([6,18]),path([1,13]),path([4,14]),path([12,20]),path([7,17]))
G2 = merge(path([9,1,10]),path([3,13]),path([5,14]),path([4,12]),path([7,20]),path([8,18]))
G3 = merge(path([10,2,11]),path([3,12]),path([8,19]),path([5,16]),path([4,17]),path([9,20]))
G4 = merge(path([0,6,1]),path([4,8]),path([2,5]),path([3,10]),path([7,9]),path([11,12]))

F_211111_1 = [G1,G2,G3,G4]
#visualize(14*t+7,F_211111_1, '(211111)-1', 'C:\\Users\\baneg\\OneDrive\\Desktop\\Git\\Python\\Research\\7 (mod 14)\\texgraph')
#^ entered up to here