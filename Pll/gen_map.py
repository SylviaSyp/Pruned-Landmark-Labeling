import osmnx as ox
import matplotlib.cm as cm
import networkx as nx
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

G = ox.graph_from_bbox(31.265904285611525,30.051649815003344,104.5372282472983,102.5439798312058, network_type='drive')
# 形成路网图
G = ox.projection.project_graph(G)
plt.rcParams['figure.dpi'] = 200
fig=plt.figure(figsize=(10,6)) #设置画布大小
ax = plt.gca()
ox.plot.plot_graph(G,ax=ax,figsize=(8*4),bgcolor='white',node_color='blue',edge_color='grey',show=True,edge_linewidth=0.3,node_size=5,node_alpha=0.5)

edges = ox.graph_to_gdfs(G, nodes=False, edges=True)

# print("d\n%d %d\n" % (len(G.nodes), len(G.edges)))
f= open("chengdu.map","w")

f.write("d\n%d %d\n" % (len(G.nodes), len(G.edges)))

D = {}
ID = {}

for index, row in edges.iterrows():
    if list(index)[0] not in D:
        ID[len(D)] = list(index)[0]
        D[list(index)[0]] = len(D)

    if list(index)[1] not in D:
        ID[len(D)] = list(index)[1]
        D[list(index)[1]] = len(D)

    if row["oneway"]:
        f.write("%d %d %d %d\n" % (D[list(index)[0]], D[list(index)[1]], int(row.length * 1000), 1))
    else:
        f.write("%d %d %d %d\n" % (D[list(index)[0]], D[list(index)[1]], int(row.length * 1000), 0))

f.close()
