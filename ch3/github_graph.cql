/*
CONFIGURATION:
===============

neo4j.conf
------------

dbms.security.procedures.unrestricted=apoc.*,ga.nlp.*
dbms.unmanaged_extension_classes=com.graphaware.server=/graphaware

com.graphaware.runtime.enabled=true
com.graphaware.module.NLP.1=com.graphaware.nlp.module.NLPBootstrapper

apoc.import.file.enabled=true 


ls -1 plugins
------------

apoc-3.5.0.12.jar
graphaware-server-all-3.5.14.55.jar
nlp-3.5.4.53.18.jar
nlp-stanfordnlp-3.5.4.53.18.jar
stanford-english-corenlp-2018-10-05-models.jar


Data files from chapter 2:
ls -1 import
------------
neo4j_repos_github.json
neo4j_neo4j_contributors_github.json

*/

/*********************/
// DATA IMPORT FROM GITHUB
/*********************/

CREATE INDEX ON :User(login)

CALL apoc.load.json("neo4j_repos_github.json") YIELD value AS item
CREATE (r:Repository {name: item.name,created_at: item.created_at,
contributors_url: item.contributors_url} )
MERGE (u:User {login: item.owner.login})
CREATE (u)-[:OWNS]->(r)

CALL apoc.load.json("neo4j_neo4j_contributors_github.json") YIELD value AS
item
MATCH (r:Repository {name: "neo4j"})
MERGE (u:User {login: item.login})
CREATE (u)-[:CONTRIBUTED_TO]->(r)


// Set token:     :params {"token": "SECRET"}

CALL apoc.load.json("neo4j_neo4j_contributors_github.json") 
YIELD value AS item
MATCH (u:User {login: item.login})
// get user's followers
CALL apoc.load.jsonParams(item.followers_url, {Authorization: 'Token ' + $token}, null) YIELD value AS contrib
// create new user f
MERGE (f:User {login: contrib.login})
// create FOLLOWS relationship between f and u
CREATE (f)-[:FOLLOWS]->(u)


// WARNING: LONG QUERY
MATCH (u:User)-[:OWNS]->(r:Repository)
// Find repository contributors
CALL apoc.load.jsonParams("https://api.github.com/repos/" + u.login + "/" + r.name + "/contributors", {Authorization: 'Token ' + $token}, null)
YIELD value AS item
// create user if not exists
MERGE (u2:User {login: item.login})
// Create CONTRIBUTED_TO relationship between new user u2 and r
MERGE (u2)-[:CONTRIBUTED_TO]->(r)
WITH item, u2
// get u2 owned repositories
CALL apoc.load.jsonParams(item.repos_url, {Authorization: 'Token ' + $token}, null) YIELD value AS contrib
MERGE (r2:Repository {name: contrib.name})
MERGE (u2)-[:OWNS]->(r2)



// WARNING: LONG QUERY
MATCH (u:User)-[:OWNS]->(r:Repository)
WHERE u.login = "neo4j"
CALL apoc.load.jsonParams("https://api.github.com/repos/" + u.login + "/" + r.name + "/readme", {Authorization: "Token " + $token }, null, null, {failOnError: false}) 
YIELD value 
CREATE (d:Document {name: value.name, content:value.content, encoding: value.encoding}) 
CREATE (d)-[:DESCRIBES]->(r)

// END LOADING DATA FROM GITHUB


/*********************/
// START NLP ANALYSIS
/*********************/

// Update text to a valid string
MATCH (d:Document)
SET d.text = apoc.text.base64Decode(apoc.text.join(split(d.content, "\n"), ""))
RETURN d

// Create NLP pipeline
CALL ga.nlp.processor.addPipeline({
	name:"named_entity_extraction",
	textProcessor: 'com.graphaware.nlp.processor.stanford.StanfordTextProcessor',
	processingSteps: {tokenize:true, ner:true}
})

// Analyze text content
MATCH (n:Document)-[:DESCRIBES]->(r:Repository)<-[:OWNS]-(:User {login: "neo4j"})
WHERE size(n.text) > 10
CALL ga.nlp.annotate({text: n.text, id: id(n), checkLanguage: false, pipeline : "named_entity_extraction"})
YIELD result
MERGE (n)-[:HAS_ANNOTATED_TEXT]->(result)


// Analyze text NLP result
MATCH (n:NER_Person) RETURN n.value

MATCH (r:Repository)<-[:DESCRIBES]-(:Document)-[:HAS_ANNOTATED_TEXT]->(:AnnotatedText)-[:CONTAINS_SENTENCE]->(:Sentence)-[:HAS_TAG]->(:NER_Person {value: 'Keanu Reeves'})
RETURN r.name




// If needed, you can clear the NLP results with:
CALL db.labels() YIELD label
WITH label WHERE label starts with "NER" OR label starts with "NE" OR label = "AnnotatedText" OR label = "TagOccurrence" OR label = "Tag" OR label = "Sentence"
CALL apoc.cypher.doIt('MATCH (n:'+label+') DETACH DELETE n', {}) YIELD value RETURN value

