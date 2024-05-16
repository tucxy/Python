import math
import networkx as nx
import matplotlib.pyplot as plt
import plotly.graph_objects as go

class Graph:
    def __init__(self):
        self.N = {}  # dictionary to store graph connections
        self.L = {}  # dictionary to store edge lengths for each vertex
        self.L_7 = {}  # dictionary to store mod 7 edge lengths for each vertex

    def add_vertex(self, vertex):
        if vertex not in self.N:
            self.N[vertex] = []  # Initialize empty list for connections
            self.L[vertex] = []  # Initialize empty list for edge lengths
            self.L_7[vertex] = []  # Initialize empty list for mod 7 edge lengths

    def add_edge(self, vertex1, vertex2):
        if vertex1 in self.N and vertex2 in self.N:
            d = abs(vertex1 - vertex2)
            l = min(d, 21 - d)
            lmod7 = (vertex1 + vertex2) % 7  # Calculate edge length mod 7
            
            self.N[vertex1].append(vertex2)
            self.N[vertex2].append(vertex1)
            self.L[vertex1].append(l)
            self.L[vertex2].append(l)
            self.L_7[vertex1].append(lmod7)
            self.L_7[vertex2].append(lmod7)

    def __str__(self):
        return "\n".join(f"{vertex}: neighbors = {self.N[vertex]}, lengths = {self.L[vertex]}, lengths_7 = {self.L_7[vertex]}" for vertex in self.N)

'''Functions:'''
#builds 
def build(vertices, edges):  # G=(vertices = [u,v,w,...],edges = [(u, v), (w, v), ...])
    G = Graph()
    for node in vertices:
        G.add_vertex(node)
    for u, v in edges:
        G.add_edge(u, v)
    return G

def merge(*graphs):
    G = Graph()
    added_edges = set()  # To keep track of added edges and prevent duplicates

    # Merge nodes from all provided graphs
    for graph in graphs:
        for node in graph.N:
            G.add_vertex(node)

    # Merge edges from all provided graphs
    for graph in graphs:
        for node in graph.N:
            for connected_node in graph.N[node]:
                edge = frozenset({node, connected_node})
                if edge not in added_edges:
                    G.add_edge(node, connected_node)
                    added_edges.add(edge)

    return G

def visualize_graph(G, title):
    # Create a networkx graph
    G_nx = nx.Graph()
    
    # Add nodes and edges
    for vertex in G.N:
        G_nx.add_node(vertex)
        for neighbor in G.N[vertex]:
            if not G_nx.has_edge(vertex, neighbor):
                G_nx.add_edge(vertex, neighbor)
    
    # Choose a layout
    pos = nx.spring_layout(G_nx, seed=40, k=1)  # positions for all nodes
    
    # Draw the graph
    nx.draw(G_nx, pos, with_labels=False, node_color='skyblue', node_size=1500, edge_color='gray')
    
    # Create labels with subscripts
    labels = {vertex: f"{vertex}$_{{{vertex % 7}}}$" for vertex in G.N}
    nx.draw_networkx_labels(G_nx, pos, labels, font_size=16, font_weight='bold')

    # Draw edge labels
    edge_labels = {(vertex, neighbor): G.L[vertex][G.N[vertex].index(neighbor)] for vertex in G.N for neighbor in G.N[vertex]}
    nx.draw_networkx_edge_labels(G_nx, pos, edge_labels=edge_labels, font_color='red')

    # Set the title
    plt.title(title)
    plt.show()

def visualize_graph_plotly(G, title):
    # Create a networkx graph
    G_nx = nx.Graph()
    
    # Add nodes and edges
    for vertex in G.N:
        G_nx.add_node(vertex)
        for neighbor in G.N[vertex]:
            G_nx.add_edge(vertex, neighbor)
    
    pos = nx.spring_layout(G_nx)  # positions for all nodes
    
    edge_x = []
    edge_y = []
    for edge in G_nx.edges():
        x0, y0 = pos[edge[0]]
        x1, y1 = pos[edge[1]]
        edge_x.append(x0)
        edge_x.append(x1)
        edge_x.append(None)
        edge_y.append(y0)
        edge_y.append(y1)
        edge_y.append(None)

    edge_trace = go.Scatter(
        x=edge_x, y=edge_y,
        line=dict(width=0.5, color='#888'),
        hoverinfo='none',
        mode='lines')

    node_x = []
    node_y = []
    for node in G_nx.nodes():
        x, y = pos[node]
        node_x.append(x)
        node_y.append(y)

    node_trace = go.Scatter(
        x=node_x, y=node_y,
        mode='markers+text',
        hoverinfo='text',
        marker=dict(
            showscale=True,
            colorscale='YlGnBu',
            size=10,
            colorbar=dict(
                thickness=15,
                title='Node Connections',
                xanchor='left',
                titleside='right'
            ),
            line_width=2))

    node_text = []
    for node in G_nx.nodes():
        node_text.append(f'{node}')
    
    node_trace.text = node_text

    fig = go.Figure(data=[edge_trace, node_trace],
             layout=go.Layout(
                title=title,
                titlefont_size=16,
                showlegend=False,
                hovermode='closest',
                margin=dict(b=20,l=5,r=5,t=40),
                annotations=[dict(
                    text="Interactive Graph Visualization",
                    showarrow=False,
                    xref="paper", yref="paper")],
                xaxis=dict(showgrid=False, zeroline=False),
                yaxis=dict(showgrid=False, zeroline=False))
                )
    
    fig.show()

def path(cycle):#path([a,b,c])=a-b-c
    C = list(cycle)
    G = Graph()
    for node in C:
        G.add_vertex(node)
    i=0
    while i < len(C)-1:
        G.add_edge(C[i], C[(i+1)])
        i+= 1
    return G

def cycle(cycle):#cycle([a,b,c])=(a,b,c)
    C = list(cycle)
    G = Graph()
    for node in C:
        G.add_vertex(node)
    i=0
    while i <= len(C)-1:
        G.add_edge(C[i], C[(i+1)% len(C)])
        i+= 1
    return G

def star(hub,neighbors):#star(h,(a,b,c))=h--a U h--b U h--c
    leaves = list(neighbors)
    G = Graph()
    G.add_vertex(hub)
    for node in leaves:
        G.add_vertex(node)
        G.add_edge(hub,node)
    return G

def lengths(G):#returns [l, ['lengths mod 7 for each length']]
    lengths_map = {}
    for vertex in G.L:
        for i, length in enumerate(G.L[vertex]):
            length_mod_7 = G.L_7[vertex][i]
            if length not in lengths_map:
                lengths_map[length] = set()
            lengths_map[length].add(length_mod_7)
    
    result = [[length, list(sorted(mod_lengths))] for length, mod_lengths in sorted(lengths_map.items())]
    return result 

def merge_lengths(*graphs):#merge()[l, ['lengths mod 7 for each length']]
    merged_lengths_map = {}
    for graph in graphs:
        for vertex in graph.L:
            for i, length in enumerate(graph.L[vertex]):
                length_mod_7 = graph.L_7[vertex][i]
                if length not in merged_lengths_map:
                    merged_lengths_map[length] = set()
                merged_lengths_map[length].add(length_mod_7)

    result = [[length, list(sorted(mod_lengths))] for length, mod_lengths in sorted(merged_lengths_map.items())]
    return result
#notebook
'''5/15 (61) cases'''
#G1
s1 = star(5,[16,15,17,14])
p1 = path([9,1,14])
l1 =path([0,13])
G1 = merge(s1,p1,l1)
print(lengths(G1),"\n")
#G2
s2 = star(4,[14,15,13,16])
p2 = path([18,5,13])
l2 =path([7,17])
G2 = merge(s2,p2,l2)
print(lengths(G2),"\n")
#G3
s3 = star(17,[4,9,6,8])
p3 = path([7,16,6])
l3 =path([1,13])
G3 = merge(s3,p3,l3)
print(lengths(G3),"\n")

print(merge_lengths(G1,G2,G3))
visualize_graph(G3,"G3")