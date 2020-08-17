"""A simple python implementation of the
Label Propagation algorithm.

Requirements:
------------
None

Usage:
------------

    python3 label_propagation.py

References:
------------

- https://docs.python.org/3.7/library/statistics.html


NB: this code was developed and tested with python 3.7

Disclaimer: this code is intended for teaching purposes only.
"""
from collections import Counter


def label_propagation(G, max_iterations=100):
    """Returns the community of the nodes in G
    based on the Label Propagation algorithm

    :param dict G: the graph
    :param int max_iter: max number of iterations
    """
    # initialize labels
    labels = {node:k  for k, node in enumerate(G)}
    print("======= Initialization")
    print(labels)
    
    # main loop
    for it in range(max_iterations):
        print("======= Iteration", it)
        old_labels = dict(labels)
        for node, neighbors in G.items():
            # counting the number of votes from each neighbors:
            votes = Counter([old_labels[n] for n in neighbors])
            print(node, votes)
            max_vote = -9999
            new_label = old_labels[node]
            for label, vote  in votes.items():
                if vote > max_vote:
                    max_vote = vote
                    new_label = label
                elif vote == max_vote:
                    if label > new_label:
                        new_label = label
            labels[node] = new_label            
        print(labels)
        # check convergence
        end = True
        for node in G:
            if old_labels[node] != labels[node]:
                end = False
                break
        if end:
            return labels
    raise Exception(
        f'Label propagation failed after max iteration = {max_iterations}'
    )


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
    print("="*20, "Start", "="*20)
    r = label_propagation(G)
    print("="*15, "Result", "="*15)
    print(r)
    print("="*20, " End ", "="*20)
