# Chapter 7: Community detection and node similarity

Code for Chapter 7 of the book "Hands on Graph Analytics with Neo4j".



## Connected components


### Algorithms

- [test_graph.cql](test_graph.cql) contains the Cypher queries to create the test graph used in this section and the following ones.


### Graph visualization

- [connected_components/graph_viz.html](connected_components/graph_viz.html) contains an example usage of the `neoviz.js` JavaScript module for graph visualization.

- NEuler: installation:
    - Mac/Windows: click on the following link [neo4j://graphapps/install?url=https://bit.ly/install-neuler](https://community.neo4j.com/t/introducing-neuler-the-graph-algorithms-playground/6555)
	- Linux: copy the link [https://neo.jfrog.io/neo/api/npm/npm/neuler](https://neo.jfrog.io/neo/api/npm/npm/neuler) into the ‘Graph Applications’ > 'Install' input in Neo4j Desktop.


## Label propagation algorithm

- [label_propagation/label_propagation.py](label_propagation/label_propagation.py): contains a simple implementation of label propagation algorithm in Python.


## Louvain algorithm


- [louvain/modularity.py](louvain/modularity.py): a python function to compute modularity from a given graph and its partition.
