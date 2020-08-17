from neo4j import GraphDatabase


# update your connection parameters if needed
URL = "bolt://localhost:7687"
USER = "neo4j"
PWD = "<YOUR_PASSWORD>"  # put your own password here



driver = GraphDatabase.driver(URL, auth=(USER, PWD))
query = "MATCH (a:Person {id: 203749})-[:IS_FRIEND_WITH]-(b:Person) RETURN count(b.id)"

with driver.session() as session:
    with session.begin_transaction() as tx:
        result = tx.run(query)
        summary = result.consume()
        avail = summary.result_available_after  # ms
        cons = summary.result_consumed_after  # ms
        total_time = avail + cons

print(total_time)

