from py2neo import Graph

# Create graph

import src.Utils.EnvVarManager as EnvVarManager


def get_connection():
    return Graph(
        host=EnvVarManager.get_from_env_or_return_default("NEO4J_HOST", "127.0.0.1"),
        port=EnvVarManager.get_from_env_or_return_default("NEO4J_PORT", "7687"),
    )


def get_node_count(graph):
    count = graph.evaluate("MATCH (n) RETURN count(n) as count;".format(int))
    return count


def drop_10k_nodes(graph):
    return graph.evaluate("match (n) with n limit 10000 DETACH DELETE n;  ".format(int))


def clean_database():
    graph = get_connection()
    while get_node_count(graph) > 0:
        drop_10k_nodes(graph)
