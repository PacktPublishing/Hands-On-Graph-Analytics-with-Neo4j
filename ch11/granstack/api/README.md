# GRANDstack Starter - GraphQL API

Requires:

- Node.js and NPM which can be installed via: https://nodejs.org/en/download/
- A Neo4j instance running with the APOC plugin installed (see 'Configure' section to set your parameters)


## Quick Start

Install dependencies:

```
npm install
```

Start the GraphQL service:

```
npm start
```

This will start the GraphQL service (by default on localhost:4000) where you can issue GraphQL requests or access GraphQL Playground in the browser.


## Configure

Set your Neo4j connection string and credentials in `.env`. For example:

```
NEO4J_URI=bolt://localhost:7687
NEO4J_USER=neo4j
NEO4J_PASSWORD=1234
```
