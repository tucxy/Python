import networkx as nx
import matplotlib.pyplot as plt

# Create an undirected graph
G = nx.Graph()

# Add nodes
G.add_node(1)
G.add_node(2)
G.add_node(3)

# Define custom positions
positions = {1: (0, 0), 2: (1, 1), 3: (0, 1)}
# Define custom vertex labels
custom_labels = {1: 2, 2: 2, 3: 3}

# Add edges
G.add_edge(1, 2)
G.add_edge(2, 3)
G.add_edge(1, 3)

# Define custom positions
positions = {1: (0, 0), 2: (1, 1), 3: (0, 1)}
# Define custom vertex labels
custom_labels = {1: 2, 2: 2, 3: 3}
# Define custom edge labels


edge_labels = {(u, v): d['weight'] for u, v, d in G.edges(data=True)}

# Draw the graph using custom positions
nx.draw(G, pos=positions, with_labels=False, node_color='skyblue', node_size=700, edge_color='k')
#Draw custom vertex labels
nx.draw_networkx_labels(G, positions, labels=custom_labels, font_size=12)
#Draw custom edge labels
nx.draw_networkx_edge_labels(G, positions, edge_labels=edge_labels)

# Show the plot
plt.show()