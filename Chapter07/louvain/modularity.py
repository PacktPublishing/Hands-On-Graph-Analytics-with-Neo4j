"""A simple python implementation for the Louvain modularity

Requirements:
------------
None

Usage:
------------

    python3 modularity.py

References:
------------


NB: this code was developed and tested with python 3.7
"""


def modularity(G, communities):
    """Compute Louvain modularity of graph G, given the partition `communities`.

    :param dict G: the graph
    :param dict communities: the communities each node is assigned to
    """
    m = sum(
        [w for _, neighbors in G.items() for _, w in neighbors.items()]
    ) / 2.0
    print("m =", m)
    ks = {k: sum([v for _, v in G[k].items()]) for k in G}
    print("ks =", ks)
    Q = 0
    for i in G:
        for j in G:
            if communities[i] != communities[j]:
                # delta function, if c(i) != c(j), modularity does not change
                continue
            Aij = G[i].get(j, 0)
            Q += 1 / (2 * m) * (
                Aij - ks[i] * ks[j] / (2 * m)
            )
    return round(Q, 3)


if __name__ == '__main__':
    G = {
        'A': {'B': 1, 'C': 1},
        'B': {'A': 1, 'C': 1},
        'C': {'A': 1, 'B': 1, 'D': 1},
        'D': {'C': 1, 'E': 1, 'G': 1},
        'E': {'D': 1, 'F': 1, 'G': 1},
        'F': {'E': 1, 'G': 1},
        'G': {'D': 1, 'E': 1, 'F': 1},
    }

    # Projected graph without "aggregation=SINGLE" is equivalent to:
    # G = {
    #     'A': {'B': 1, 'C': 1},
    #     'B': {'A': 1, 'C': 1},
    #     'C': {'A': 1, 'B': 1, 'D': 1},
    #     'D': {'C': 1, 'E': 2, 'G': 1},
    #     'E': {'D': 2, 'F': 1, 'G': 1},
    #     'F': {'E': 1, 'G': 1},
    #     'G': {'D': 1, 'E': 1, 'F': 1},
    # }
        
    # each node in its own community:
    communities_1 = {
        node: k for k, node in enumerate(G)
    }

    # all nodes in the same community:
    communities_2 = {
        node: 1 for node in G
    }

    # optimal communities
    communities_3 = {
        "A": 1,
        "B": 1,
        "C": 1,
        "D": 2,
        "E": 2,
        "F": 2,
        "G": 2
    }

    print("="*20, "Start", "="*20)
    r = modularity(G, communities_3)
    print("="*15, "Result", "="*15)
    print(r)
    print("="*20, " End ", "="*20)
