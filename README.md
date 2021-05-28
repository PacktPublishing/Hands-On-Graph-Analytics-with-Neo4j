# Hands-On Graph Analytics with Neo4j
<a href="https://www.packtpub.com/product/hands-on-graph-analytics-with-neo4j/9781839212611"><img src="https://static.packt-cdn.com/products/9781839212611/cover/smaller" alt="Hands-On Graph Analytics with Neo4j" height="256px" align="right"></a>

This is the code repository for [Hands-On Graph Analytics with Neo4j](https://www.packtpub.com/product/hands-on-graph-analytics-with-neo4j/9781839212611), published by Packt.

**Perform graph processing and visualization techniques using connected data across your enterprise**

## What is this book about?
Neo4j is a graph database that includes plugins to run complex graph algorithms.
The book starts with an introduction to the basics of graph analytics, the Cypher query language, and graph architecture components, and helps you to understand why enterprises have started to adopt graph analytics within their organizations. You’ll find out how to implement Neo4j algorithms and techniques and explore various graph analytics methods to reveal complex relationships in your data. You’ll be able to implement graph analytics catering to different domains such as fraud detection, graph-based search, recommendation systems, social networking, and data management. You’ll also learn how to store data in graph databases and extract valuable insights from it. As you become well-versed with the techniques, you’ll discover graph machine learning in order to address simple to complex challenges using Neo4j. You will also understand how to use graph data in a machine learning model in order to make predictions based on your data. Finally, you’ll get to grips with structuring a web application for production using Neo4j.

This book covers the following exciting features: 
* Become well-versed with Neo4j graph database building blocks, nodes, and relationships
* Discover how to create, update, and delete nodes and relationships using Cypher querying
* Use graphs to improve web search and recommendations
* Understand graph algorithms such as pathfinding, spatial search, centrality, and community detection
* Find out different steps to integrate graphs in a normal machine learning pipeline

If you feel this book is for you, get your [copy](https://www.amazon.com/dp/1839212616) today!

<a href="https://www.packtpub.com/?utm_source=github&utm_medium=banner&utm_campaign=GitHubBanner"><img src="https://raw.githubusercontent.com/PacktPublishing/GitHub/master/GitHub.png" 
alt="https://www.packtpub.com/" border="5" /></a>

## Errata
Chapter 2
Page no:56 

It looks like:

LOAD CSV FROM 'path/to/file.csv' AS row
CREATE (:Node {name: row[1]

It should look like: 

LOAD CSV FROM 'path/to/file.csv' AS row
CREATE (:Node {name: row[1] })

Page no: 348

It looks like:

its relationship to u and v is more important and the edge between u and v is more probable:

It should look like: 

its relationship to u and v is more important and the edge between u and v is more probable.

It looks like:

Therefore, nodes u and v on the left-hand side are more likely to accept new connections:

It should look like: 

Therefore, nodes u and v on the left-hand side are more likely to accept new connections.


## Instructions and Navigations
All of the code is organized into folders. For example, Chapter02.

The code will look like the following:
```
MERGE (n:Label {id: 1})
ON CREATE SET n.timestamp_created = timestamp()
ON MATCH SET n.timestamp_last_update = timestamp()
```

**Following is what you need for this book:**
This book is for data analysts, business analysts, graph analysts, and database developers looking to store and process graph data to reveal key data insights. This book will also appeal to data scientists who want to build intelligent graph applications catering to different domains. Some experience with Neo4j is required.

With the following software and hardware list you can run all code files present in the book (Chapter 1-15).

### Software and Hardware List

| Chapter  | Software required                   | OS required                        |
| -------- | ------------------------------------| -----------------------------------|
| 2        | Neo4j ≥ 3.5, APOC ≥ 3.5.0.11        | Windows, Mac OS X, and Linux (Any) |
| 3        |Neo4j ≥ 3.5, APOC ≥ 3.5.0.11, GraphAware NLP plugin | Windows, Mac OS X, and Linux (Any) |
| 4        | Neo4j ≥ 3.5, Graph Data Science plugin ≥ 1.0           | Windows, Mac OS X, and Linux (Any) |
| 5        | Neo4j ≥ 3.5; < 4, Graph Data Science plugin ≥ 1.0, neo4-spatial            | Windows, Mac OS X, and Linux (Any) |
| 6 -7     | Neo4j ≥ 3.5, Graph Data Science plugin ≥ 1.0          | Windows, Mac OS X, and Linux (Any) |
| 8-9-10   | Neo4j ≥ 3.5, Graph Data Science plugin ≥ 1.0, Anaconda            | Windows, Mac OS X, and Linux (Any) |
| 11        | Python, Node.js            | Windows, Mac OS X, and Linux (Any) |
| 12       | Neo4j ≥ 4.0           | Windows, Mac OS X, and Linux (Any) |

Detailed installation steps (software-wise)

**The steps should be listed in a way that it prepares the system environment to be able to test the codes of the book.**

* **Neo4j**:
   Download Neo4j Desktop from https://neo4j.com/download/
   Create a new graph with the proper version of Neo4j (Neo4j Desktop will take care of downloading it if not yes installed or your system)
* **APOC**
   Go to a given graph Management panel in Neo4j Desktop
   Click Plugins
   Install APOC
* **GraphAware NLP pluigns:**
   Download required jar files from:
   Copy them to the plugins/ directory of your Neo4j graph
* **Graph Data Science plugin:** 
   installation process similar to APOC, through Neo4j Desktop
   neo4-spatial: download last jar file from https://github.com/neo4j-contrib/spatial/releases and copy it into the plugins directory of your graph.
* **Anaconda:**
   Download from https://www.anaconda.com/products/individual
   Start anaconda-navigator
* **Install Jupyter Notebook (or JupyterLab) application**
   Click Launch
* **Node.js and npm:**
   https://nodejs.org/en/download/


We also provide a PDF file that has color images of the screenshots/diagrams used in this book. [Click here to download it](https://static.packt-cdn.com/downloads/9781839212611_ColorImages.pdf).

### Related products <Other books you may enjoy>
* Learning Neo4j 3.x - Second Edition [[Packt]](https://www.packtpub.com/product/learning-neo4j-3-x-second-edition/9781786466143) [[Amazon](https://www.amazon.com/dp/1786466147)

## Get to Know the Author
**Estelle Scifo**
possesses over 7 years' experience as a data scientist, having received her PhD from the Laboratoire de l'Accélérateur Linéaire, Orsay (affiliated to CERN in Geneva). As a Neo4j-certified professional, she uses graph databases on a daily basis and takes full advantage of its features to build efficient machine learning models from this data. In addition, she is also a data science mentor to newcomers to the field. Her domain expertise and deep insights into the perspective of the needs of beginners make her an excellent teacher.

## Other books by the authors
* [Exploring Graph Algorithms with Neo4j [Video]](https://www.packtpub.com/product/exploring-graph-algorithms-with-neo4j-video/9781838555580)

### Suggestions and Feedback
[Click here](https://docs.google.com/forms/d/e/1FAIpQLSdy7dATC6QmEL81FIUuymZ0Wy9vH1jHkvpY57OiMeKGqib_Ow/viewform) if you have any feedback or suggestions.
