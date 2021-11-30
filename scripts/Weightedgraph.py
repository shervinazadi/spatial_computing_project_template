# import related libraries

import matplotlib.pyplot as plt
import networkx as nx
from random import randint, seed
from random import random
from networkx.algorithms.core import k_core

# Create graph G

G = nx.Graph()

# Define node names

a =	 "Student Housing"
b =	 "Assisted Living"
c =	 "Starter Housing"
d0 = "Co-cookingA"
d1 = "Co-cookingB"
d2 = "Co-cookingC"
e =	 "Co-working"
f =	 "Community Centre"
g =	 "Library"
h =	 "Cinematheque"
i =	 "Laundry"
j =  "Fab-Labs"
k =	 "Workspaces/ start ups"
l =	 "Workshop"
m =	 "Car Parking"
n =	 "Biking"
o =	 "Shops"
p =	 "Grocery"
q =	 "Gym"
r =	 "Restuarant"
s =	 "Medicine Shop"
t =	 "Vegetation"
u =	 "Street"
v =	 "Lobby/Entrance"
w =  "Communal garden"
x =  "Arcade"
y =  "BiergartenA"
z =  "Soccerfield"

# defining weights

c1  = 1.0                                                                                                                                   # connection between @ & ^
c2  = 1.0                                                                                                                                   # connection between @ & ^
c3  = 1.0                                                                                                                                   # connection between @ & ^
c4  = 1.0                                                                                                                                   # connection between @ & ^
c5  = 0.5                                                                                                                                   # connection between @ & ^
c6  = 1.0                                                                                                                                   # connection between @ & ^
c7  = 0.75                                                                                                                                  # connection between @ & ^
c8  = 0.75                                                                                                                                  # connection between @ & ^
c9  = 1.0                                                                                                                                   # connection between @ & ^
c10 = 1.0                                                                                                                                   # connection between @ & ^
c11 = 0.2                                                                                                                                   # connection between @ & ^
c12 = 0.15                                                                                                                                  # connection between @ & ^
c13 = 0.55                                                                                                                                  # connection between @ & ^
c14 = 0.55                                                                                                                                  # connection between @ & ^
c16 = 0.55                                                                                                                                  # connection between @ & ^
c17 = 0.55                                                                                                                                  # connection between @ & ^
c19 = 0.65                                                                                                                                  # connection between @ & ^
c20 = 0.65                                                                                                                                  # connection between @ & ^
c21 = 0.65                                                                                                                                  # connection between @ & ^
c22 = 0.6                                                                                                                                   # connection between @ & ^
c23 = 0.65                                                                                                                                  # connection between @ & ^
c24 = 0.65                                                                                                                                  # connection between @ & ^
c25 = 0.7                                                                                                                                   # connection between @ & ^
c26 = 0.2                                                                                                                                   # connection between @ & ^
c27 = 0.6                                                                                                                                   # connection between @ & ^
c28 = 0.65                                                                                                                                  # connection between @ & ^
c29 = 0.65                                                                                                                                  # connection between @ & ^
c30 = 0.65                                                                                                                                  # connection between @ & ^
c31 = 0.6                                                                                                                                   # connection between @ & ^
c32 = 1.0                                                                                                                                   # connection between @ & ^
c33 = 1.0                                                                                                                                   # connection between @ & ^
c34 = 1.0                                                                                                                                   # connection between @ & ^
c35 = 1.0                                                                                                                                   # connection between @ & ^
c36 = 0.5                                                                                                                                   # connection between @ & ^
c37 = 1.0                                                                                                                                   # connection between @ & ^
c38 = 1.0                                                                                                                                   # connection between @ & ^
c39 = 1.0                                                                                                                                   # connection between @ & ^
c40 = 2.0                                                                                                                                   # connection between Soccerfield and Street
c41 = 2.0                                                                                                                                   #
c42 = 2.0                                                                                                                                   # connection between @ & ^
c43 = 2.0                                                                                                                                   # connection between @ & ^
c44 = 2.0                                                                                                                                   # connection between @ & ^

# defining edges
    # defining student housing connections 

G.add_edge(a, d0, weight=c1)
G.add_edge(a, i, weight=c2)

    # defining assisted living connections

G.add_edge(b, w, weight=c3)
G.add_edge(b, d1, weight=c4)
G.add_edge(b, v, weight=c5)
G.add_edge(b, i, weight=c6)

    # Cinematheque to arcvade

G.add_edge(h, x,weight=c43)


    # Biergarten to co-cooking

G.add_edge(y, d0,weight=c7)
G.add_edge(y, d2,weight=c8)

    # defining starter connections

G.add_edge(c, d2, weight=c9)
G.add_edge(c, i, weight=c10)

    # defining start up connections

G.add_edge(k, w, weight=c11)

    # workshop to fablabs

G.add_edge(j, l,weight=c44)

    # Defining co-working connections
 
G.add_edge(e, w, weight=c12)
G.add_edge(e, f, weight=c13)
G.add_edge(e, g, weight=c42)

    # Defining community centre connections

G.add_edge(f, w, weight=c14)
G.add_edge(f, j, weight=c16)
G.add_edge(f, l, weight=c17)
G.add_edge(f, d0, weight=c19)
G.add_edge(f, d1, weight=c20)
G.add_edge(f, d2, weight=c21)
G.add_edge(f, g, weight=c22)
G.add_edge(f, x, weight=c23)
G.add_edge(f, h, weight=c24)
G.add_edge(f, v, weight=c25)

    # Defining lobby connections

G.add_edge(v, w, weight=c26)
G.add_edge(v, k, weight=c27)
G.add_edge(v, n, weight=c28)
G.add_edge(v, m, weight=c29)
G.add_edge(v, u, weight=c30)
G.add_edge(v, q, weight=c31)

    # Defining street connections

G.add_edge(u, q, weight=c32)
G.add_edge(u, o, weight=c33)
G.add_edge(u, t, weight=c34)
G.add_edge(u, m, weight=c35)
G.add_edge(u, n, weight=c36)
G.add_edge(u, p, weight=c37)
G.add_edge(u, s, weight=c38)
G.add_edge(u, r, weight=c39)

    # Defininf soccerfield connections

G.add_edge(z, u, weight=c40)
G.add_edge(z, f, weight=c41)

# create random seed

randomvalue = seed(1000)

for _ in range(1):
	value = randint(0, 100000)

# Preference's 

elarge = [(u, v) for (u, v, d) in G.edges(data=True) if d["weight"] > 0.5]
# elarge = [(u, v) for (u, v, d) in G.edges(data=True) if d["weight"] > 0.5]
# elarge = [(u, v) for (u, v, d) in G.edges(data=True) if d["weight"] > 0.5]
# elarge = [(u, v) for (u, v, d) in G.edges(data=True) if d["weight"] > 0.5]
esmall = [(u, v) for (u, v, d) in G.edges(data=True) if d["weight"] <= 0.5]

pos = nx.spring_layout(G, seed=randomvalue)  # positions for all nodes - seed for reproducibility

# Node properties

nx.draw_networkx_nodes(G, pos, node_size=700)

# Edge properties

nx.draw_networkx_edges(G, pos, edgelist=elarge, width=6, alpha=0.5, edge_color = "#00ff31")
# nx.draw_networkx_edges(G, pos, edgelist=elarge, width=6, alpha=0.5, edge_color = "#00ff31")
# nx.draw_networkx_edges(G, pos, edgelist=elarge, width=6, alpha=0.5, edge_color = "#00ff31")
# nx.draw_networkx_edges(G, pos, edgelist=elarge, width=6, alpha=0.5, edge_color = "#00ff31")
nx.draw_networkx_edges(G, pos, edgelist=esmall, width=6, alpha=0.5, edge_color="#aaaaaa", style="dashed")

# Label properties

nx.draw_networkx_labels(G, pos, font_size=20, font_family="sans-serif")

# Print properties

ax = plt.gca()
ax.margins(0.08)
plt.axis("off")
plt.tight_layout()
plt.show()