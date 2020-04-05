"""A python implementation of the PageRank algorithm.

Requirements:
------------
None

Usage:
------------

    python3 page_rank.py


NB: this code was developed and tested with python 3.7

Disclaimer: this code is intended for teaching purposes only.
"""


def page_rank(G, d=0.85, tolerance=0.01, max_iterations=50):
    """Returns the PageRank of the nodes in the graph.

    :param dict G: the graph
    :param float d: the damping factor
    :param flat tol: tolerance to determine algorithm convergence
    :param int max_iter: max number of iterations
    """
    N = len(G)
    pr = dict.fromkeys(G, 1.0)
    print("======= Initialization")
    print(pr)
    outgoing_degree = {k: len(v) for k, v in G.items()}

    # main loop
    for it in range(max_iterations):
        print("======= Iteration", it)
        old_pr = dict(pr)
        pr = dict.fromkeys(old_pr.keys(), 0)
        for node in G:
            for neighbor in G[node]:
                pr[neighbor] += d * old_pr[node] / outgoing_degree[node]
            pr[node] += (1 - d)
        print(pr)
        # check convergence
        mean_diff_to_prev_pr = sum([abs(pr[n] - old_pr[n]) for n in G])/N
        if mean_diff_to_prev_pr < tolerance:
            return pr
    raise Exception(
        f'PageRank failed after max iteration = {max_iterations}'
        f' (err={mean_diff_to_prev_pr} > tol = {tolerance})'
    )


if __name__ == '__main__':
    G = {
        'A': {'B': 1, 'D': 1},
        'B': {'A': 1},
        'C': {'B': 1},
        'D': {'B': 1},
    }
    print("="*20, "Start", "="*20)
    pr = page_rank(G)
    print("="*15, "Result", "="*15)
    print(pr)
    print("="*20, " End ", "="*20)
