# Chapter 10: Graph embedding: from graphs to matrices

## Importing the Zachary's karate club data

1. Download [data/zkc.graph](data/zkc.graph) and copy it into the `import` folder of your graph
2. Run the following Cypher query:

```
LOAD CSV FROM "file:///zkc.graph" AS row
FIELDTERMINATOR " "
MERGE (u:Node {id: toInteger(row[0])} )
MERGE (v:Node {id: toInteger(row[1])} )
CREATE (u)-[:LINK]->(v)
```

