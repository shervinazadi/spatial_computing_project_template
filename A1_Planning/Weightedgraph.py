import matplotlib.pyplot as plt
import networkx as nx
from networkx.algorithms.core import k_core

G = nx.Graph()

a =	"Student Housing"
b =	"Assisted Living"
c =	"Starter Housing"
d =	"Co-cooking"
e =	"Co-working"
f =	"Community Centre"
g =	"Library"
h =	"Cinematheque"
i =	"Laundry"
j = "Fab-Labs"
k =	"Workspaces/ start ups"
l =	"Workshop"
m =	"Car Parking"
n =	"Biking"
o =	"Shops"
p =	"Grocery"
q =	"Gym"
r =	"Restuarant"
s =	"Medicine Shop"
t =	"Vegetation"
u =	"Street"
v =	"Lobby/Entrance"
w = "Communal garden"
x = "Arcade"

# defining student housing connections 

G.add_edge(a, d, weight=1.0)
G.add_edge(a, i, weight=1.0)

# defining assisted living connections

G.add_edge(b, w, weight=1.0)
G.add_edge(b, v, weight=1.0)
G.add_edge(b, i, weight=1.0)

# defining starter connections

G.add_edge(c, d, weight=1.0)
G.add_edge(c, i, weight=1.0)

# Defining co-working connections
 
G.add_edge(e, w, weight=1.0)
G.add_edge(e, g, weight=1.0)

# Defining community centre connections

G.add_edge(f, w, weight=1.0)
G.add_edge(f, e, weight=1.0)
G.add_edge(f, j, weight=1.0)
G.add_edge(f, l, weight=1.0)
G.add_edge(f, b, weight=1.0)
G.add_edge(f, d, weight=1.0)
G.add_edge(f, g, weight=1.0)
G.add_edge(f, x, weight=1.0)
G.add_edge(f, h, weight=1.0)
G.add_edge(f, v, weight=1.0)

# Defining lobby connections

G.add_edge(v, w, weight=1.0)
G.add_edge(v, k, weight=1.0)
G.add_edge(v, n, weight=1.0)
G.add_edge(v, m, weight=1.0)
G.add_edge(v, u, weight=1.0)
G.add_edge(v, q, weight=1.0)

# Defining street connections

G.add_edge(u, q, weight=1.0)
G.add_edge(u, o, weight=1.0)
G.add_edge(u, t, weight=1.0)
G.add_edge(u, m, weight=1.0)
G.add_edge(u, n, weight=1.0)

# 

elarge = [(u, v) for (u, v, d) in G.edges(data=True) if d["weight"] > 0.5]
esmall = [(u, v) for (u, v, d) in G.edges(data=True) if d["weight"] <= 0.5]

pos = nx.spring_layout(G, seed=3204932094)  # positions for all nodes - seed for reproducibility

# nodes
nx.draw_networkx_nodes(G, pos, node_size=700)

# edges
nx.draw_networkx_edges(G, pos, edgelist=elarge, width=6)
nx.draw_networkx_edges(
    G, pos, edgelist=esmall, width=6, alpha=0.5, edge_color="b", style="dashed"
)

# labels
nx.draw_networkx_labels(G, pos, font_size=20, font_family="sans-serif")

ax = plt.gca()
ax.margins(0.08)
plt.axis("off")
plt.tight_layout()
plt.show()