"""
Helper functions to create/drop projected graphs
and run some algorithms in write mode
"""

def create_projected_graph(driver, graph_name, node_projection, relationship_projection, is_cypher=False):
    if is_cypher:
        procedure_name = "gds.graph.create.cypher"
    else:
        procedure_name = "gds.graph.create"
    with driver.session() as session:
        result = session.run(
            f"CALL {procedure_name}($graphName, $nodeProj, $relProj)",
            graphName=graph_name,
            nodeProj=node_projection,
            relProj=relationship_projection
         )

    
def drop_projected_graph(driver, graph_name):
    with driver.session() as session:
        result = session.run(
            "CALL gds.graph.drop($graphName)",
            graphName=graph_name,
        )

        
def run_wcc_algorithm(driver, graph_name, configuration):
    with driver.session() as session:
        result = session.run(
            "CALL gds.wcc.write($graphName, $algoConfig)",
            graphName=graph_name,
            algoConfig=configuration,
        )


def run_louvain_algorithm(driver, graph_name, configuration):
    with driver.session() as session:
        result = session.run(
            "CALL gds.louvain.write($graphName, $algoConfig)",
            graphName=graph_name,
            algoConfig=configuration,
        )


def run_pageRank_algorithm(driver, graph_name, configuration):
    with driver.session() as session:
        result = session.run(
            "CALL gds.pageRank.write($graphName, $algoConfig)",
            graphName=graph_name,
            algoConfig=configuration,
        )