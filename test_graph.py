#!/usr/bin/env python3

import matplotlib.pyplot as plt
import networkx as nx
import random
import time

WEIGHT = 0.7

G = nx.Graph()

G.add_node('a',pos=(2,5))
G.add_node('b',pos=(4,5))
G.add_node('c',pos=(3,3))
G.add_node('d',pos=(1,3))
G.add_node('e',pos=(4,2))
G.add_node('f',pos=(2,1))
G.add_node('g',pos=(1,6))

G.add_edge('a', 'b', weight=0.6)
G.add_edge('g', 'a', weight=0.7)
G.add_edge('c', 'd', weight=0.5)
G.add_edge('c', 'e', weight=0.7)
G.add_edge('c', 'f', weight=0.9)
G.add_edge('a', 'd', weight=0.8)

elarge = [(u, v) for (u, v, d) in G.edges(data=True) if d['weight'] >= 0.7]
esmall = [(u, v) for (u, v, d) in G.edges(data=True) if d['weight'] < 0.7]

###### new random node ######
G.add_node('N',pos=(0,3))

pos=nx.get_node_attributes(G,'pos')
labels = nx.get_edge_attributes(G,'weight')

nodes = list(G.nodes())
nodes.remove('N')
random_node = random.choice(nodes)

# G.add_edge('N',random_node, weight=WEIGHT)
# path_edges = [('N',random_node)]
current_node_edges = G.edges(random_node)
# print (type(current_node_edges))
next_node = random_node
old_node = random_node
new_node = random_node

print("picked random node: ", random_node)
path = [('N',random_node)]
while len(current_node_edges) > 0:
    max_weight = 0
    for (a,b) in current_node_edges:
        w = G.get_edge_data(a,b)['weight']
        if w > max_weight:
            max_weight = w
            new_node = b
        # print("w", w)
    old_node = next_node
    next_node = new_node
    path.append((old_node,next_node))
    # current_node_edges = []
    current_node_edges = list(G.edges(next_node))
    # print("current_node_edges: ", current_node_edges)
    # print("next_node, old_node : ", next_node, old_node)
    current_node_edges.remove((next_node,old_node))
    # print("current_node_edges updated: ", current_node_edges)


# print ("max_weight: ", max_weight)
# print ("next_node: ", next_node)
print("found path: ", path)
# nodes
nx.draw_networkx_nodes(G, pos, node_size=700)

# edges
nx.draw_networkx_edges(G, pos, edgelist=elarge,
                       width=3)
nx.draw_networkx_edges(G, pos, edgelist=esmall,
                       width=3, alpha=0.5, edge_color='b', style='dashed')

# labels
nx.draw_networkx_labels(G, pos, font_size=20, font_family='sans-serif')
nx.draw_networkx_edge_labels(G,pos,edge_labels=labels)
nx.draw_networkx_edges(G,pos,edgelist=path,edge_color='r',width=10, alpha=0.3, arrows=True)

plt.axis('off')
plt.show()