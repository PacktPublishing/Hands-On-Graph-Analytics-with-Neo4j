# GRANDstack Application - UI with React

Requires:

- Node.js and NPM which can be installed via: https://nodejs.org/en/download/
- A Neo4j instance running (see 'Configure' section to set your parameters)
- The GraphQL API running on port 4001


## Quickstart

Install dependencies:

```
npm install
```

Start the development server:

```
npm start
```

This will serve the app on `http://localhost:3000`

## Configure

Configuration is done with environment variables specified in `.env`

Edit `.env` to specify the URI of the GraphQL API. The default is `http://localhost:3000`:

```
REACT_APP_GRAPHQL_URI=http://localhost:3000
```
