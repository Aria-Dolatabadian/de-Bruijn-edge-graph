import networkx as nx
import matplotlib.pyplot as plt
#Define the de_bruijn_edge function
def de_bruijn_edge(a, b):
    a = a[:0] + 'A' + a[1:]  # reset first base: [T]GAG -> [A]GAG
    b = 'A' + b[:-1]  # shift right to A: [GAG]C -> A[GAG]
    return a == b  # suffix of a == prefix of b

# Example usage
print(de_bruijn_edge('TGAG', 'GAGC'))
print(de_bruijn_edge('TCAG', 'GAGC'))

# Construct the de Bruijn graph
sequence = "CGACATGCACGAATCAGCATA"
k = 3
kmers = [sequence[i:i+k] for i in range(len(sequence)-k+1)]
edges = [(kmer[:-1], kmer[1:]) for kmer in kmers]

graph = nx.DiGraph()
graph.add_edges_from(edges)

# Plot the de Bruijn graph
plt.figure(figsize=(6, 4))
pos = nx.circular_layout(graph)
nx.draw_networkx_nodes(graph, pos, node_size=200, node_color='lightblue')
nx.draw_networkx_edges(graph, pos, edge_color='gray')
nx.draw_networkx_labels(graph, pos, font_size=10, font_color='black')
plt.axis('off')
plt.title("De Bruijn Graph")
plt.show()
