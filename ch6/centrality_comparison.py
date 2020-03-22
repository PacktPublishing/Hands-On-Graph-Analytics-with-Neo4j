"""A comparison of different centrality algorithms
on a given graph using python networkx.

Requirements:
------------
- networkx
- scipy
- matplotlib


Results are saved in the `figures` directory:

    mkdir figures

Usage:
------------

    python3 centrality_comparison.py

"""
import networkx as nx
import matplotlib.pyplot as plt


G = nx.read_edgelist("test_graph.edgelist")
pos = nx.kamada_kawai_layout(G)


algos = {
    "Degree": nx.degree_centrality,
    "PageRank": nx.pagerank,
    "Closeness": nx.closeness_centrality,
    "Betweenness": nx.betweenness_centrality,
}

f, axs = plt.subplots(2, 2, figsize=(12, 12))

for k, (name, func) in enumerate(algos.items()):

    res = func(G)
    # print(name, res)
    res_nodes = list(res.keys())
    res_values = list(res.values())

    ax = axs.flatten()[k]

    plt_nodes = nx.draw_networkx_nodes(
        G, pos,
        ax=ax,
        nodelist=res_nodes,
        node_color=res_values,
        alpha=1,
        node_size=1200,
        cmap=plt.cm.Blues,
        vmax=max(res_values)*1.1
    )
    ax.set_title(name)
    ax.axis("off")
    nx.draw_networkx_edges(G, pos, ax=ax)
    nx.draw_networkx_labels(G, pos, font_size=14, ax=ax)
    # cbar = plt.colorbar(plt_nodes, ticks=[min(res_values),
    #                     max(res_values)*1.1])
    # cbar.ax.set_yticklabels(['Low', 'High'])

f.savefig("figures/graph_centralities.png")
