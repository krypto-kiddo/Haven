# A python script that builds a network graph and visualises it based on the Transactions dataset (src: ../files/transactions.csv)
# Brought to you by @Krypto-Kiddo and @Sassycular feat. ChatGPT
# The resultant graph output can be found at "../files/network_graph.png"

# CODE BEGINS BELOW
import networkx as nx
import matplotlib.pyplot as plt

# Create an empty directed graph
graph = nx.DiGraph()

# Read the dataset and add edges to the graph
with open('transactions.csv', 'r') as file:
    next(file)  # Skip the header line if it exists
    for line in file:
        sender, receiver, amount, block_id = line.strip().split(',')
        graph.add_edge(sender, receiver, amount=float(amount), block_id=int(block_id))

# Set the layout for the graph
layout = nx.spring_layout(graph, seed=42)

# Define colors for labeled and unlabeled nodes
labeled_color = 'red'
unlabeled_color = 'skyblue'

# Draw the nodes with smaller size and transparency
node_size = 20
node_alpha = 0.6
node_color = [unlabeled_color] * len(graph.nodes())
nx.draw_networkx_nodes(graph, layout, node_size=node_size, node_color=node_color, alpha=node_alpha, edgecolors='white')

# Draw the labeled nodes with bigger size
labeled_nodes = [node for node in graph.nodes() if node in labels]
labeled_node_size = 100
labeled_node_color = labeled_color
nx.draw_networkx_nodes(graph, layout, nodelist=labeled_nodes, node_size=labeled_node_size,
                       node_color=labeled_node_color, alpha=node_alpha, edgecolors='white')

# Draw the edges with transparency
edge_color = 'gray'
edge_alpha = 0.4
nx.draw_networkx_edges(graph, layout, edge_color=edge_color, alpha=edge_alpha, arrows=True)

# Draw the labels for a subset of nodes with smaller font size
labels = {node: node[-4:] for node in graph.nodes() if graph.degree(node) >= 5}
nx.draw_networkx_labels(graph, layout, labels, font_size=6, font_color='black')

# Set the plot size and remove the axis
plt.figure(figsize=(10, 6))
plt.axis('off')

# Add a title
plt.title('NEAR Network Graph')

# Show the plot
plt.tight_layout()
plt.show()


# END OF CODE
