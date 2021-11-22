import os.path
import sys 

import networkx as nx

# defining nodes

G=nx.Graph()
G.add_node('A',role='manager')

# defining links between nodes


# visualizing system

nx.draw_networkx(G)