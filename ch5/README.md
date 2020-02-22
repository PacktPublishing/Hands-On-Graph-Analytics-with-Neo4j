# Chapter 5: Spatial data

This repository contains the data files used within Chapter 5.


## Representing spatial attributes

The file [NYC_POI.csv](data/NYC_POI.csv) was extracted from a list of POIs provided by the city of New York at: [https://data.cityofnewyork.us/City-Government/Points-Of-Interest/rxuy-2muj](https://data.cityofnewyork.us/City-Government/Points-Of-Interest/rxuy-2muj)

It was restricted to the POIs within Manhattan and classified as "Cultural Facility".


## Creating a geometry layer in Neo4j with neo4j-spatial

The file [manhattan_districts.shp](data/manhattan_districts.shp) contains the geometries for the 11 districts of Manhattan we consider in the book.


## Finding shortest path based on distance

The dataset we are using in this section comes from [kaggle](https://www.kaggle.com/crailtap/street-network-of-new-york-in-graphml#manhatten.graphml). It is redistributed here under [ch5/data/manhattan_road_network.graphml.zip](ch5/data/manhattan_road_network.graphml.zip).


## Visualizing spatial data with Neo4j

For the last subsection, you will use the code in [shortest_path_visualization.html](shortest_path_visualization.html). You will also need to download `wellknown.js` file from [https://github.com/mapbox/wellknown](https://github.com/mapbox/wellknown) in order to tranlate WKT goemetry format to GeoJSON.
