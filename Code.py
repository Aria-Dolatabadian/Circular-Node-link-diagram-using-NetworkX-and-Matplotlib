import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt

# Read the CSV file into a pandas DataFrame
df = pd.read_csv('node_connection_data.csv', header=None)

# Create a graph object
G = nx.Graph()

# Add edges to the graph from the DataFrame
for i, row in df.iterrows():
    G.add_edge(row[0], row[1])

# Plot the graph as a circular layout
pos = nx.circular_layout(G)
pos_labels = {}
for node, coords in pos.items():
    x, y = coords
    # multiply the coordinates by a factor slightly greater than 1 to move the labels outside the circle
    pos_labels[node] = (1.1 * x, 1.1 * y)
nx.draw_networkx_nodes(G, pos, node_color='lightblue', node_size=160)
nx.draw_networkx_edges(G, pos, edge_color='gray')
labels = {i: str(i) for i in G.nodes()}  # Create a dictionary of labels
nx.draw_networkx_labels(G, pos_labels, labels, font_size=8, font_family='sans-serif')
plt.axis('off')
plt.title('Circular Node-link diagram using NetworkX and Matplotlib')
plt.show()





