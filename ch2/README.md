# Chapter 2: Cypher query language

This folder contains the data files used within Chapter 2 of _Hands-on Graph Analytics with Neo4j_ under the `data` directory.

`github_ch2.tar.gz` contains the `graph.db` directory after this chapter and the assessments, that you can use if you do not have GitHub API token or if you skipped Chapter 2 (created with Neo4j 3.5).


## Facebook graph

1. Download Facebook data from Kaggle: https://www.kaggle.com/c/FacebookRecruiting/data (training sample)
2. Here is an eample data:
```
source_node,destination_node
1,690569
1,315892
1,189226
2,834328
2,1615927
2,1194519
2,470294
2,961886
2,626040
```

3. Load it into Neo4j using your preferred way. Here are three Cypher queries to import the data with LOAD CSV:


```
LOAD CSV WITH HEADERS FROM "file:///train.csv" AS row
MERGE (:Person {id: row.source_node})
```

```
LOAD CSV WITH HEADERS FROM "file:///train.csv" AS row
MERGE (:Person {id: row.destination_node})
```


```
LOAD CSV WITH HEADERS FROM "file:///train.csv" AS row
MATCH (p1:Person {id: row.source_node})
MATCH (p2:Person {id: row.destination_node})
CREATE (p1)-[:IS_FRIEND_WITH]->(p2)
```
