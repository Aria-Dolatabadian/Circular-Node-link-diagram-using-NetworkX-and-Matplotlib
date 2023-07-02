import networkx as nx
import matplotlib.pyplot as plt

# Create an empty directed graph
graph = nx.DiGraph()

# Add nodes (genes) to the graph
graph.add_nodes_from(['GeneA', 'GeneB', 'GeneC', 'GeneD'])

# Add directed edges (regulatory relationships) between genes
graph.add_edges_from([('GeneA', 'GeneC'), ('GeneB', 'GeneC'), ('GeneC', 'GeneD'), ('GeneB', 'GeneC')])

# Visualize the network
pos = nx.spring_layout(graph)
nx.draw_networkx(graph, pos=pos, with_labels=True, node_color='lightblue', edge_color='gray', arrowsize=10)

# Show the plot
plt.title('Gene Regulatory Network')
plt.axis('off')
plt.show()
