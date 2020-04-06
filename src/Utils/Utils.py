from neo4j import GraphDatabase
from src.Models.DataObject.v0_0_2.DataObject import DataObject
from src.Models.CRM.v5_0_2.NodeEntities.E1_CRM_Entity import E1_CRM_Entity

uri = "bolt://localhost:7687"
driver = GraphDatabase.driver(uri, auth=("neo4j", "password"))


def nested_json(node, json_schema):
    if isinstance(json_schema, str):
        return node.decodeJSON()

    def read_relationships(tx, search_node, node_relationship):
        for record in tx.run("MATCH (a: " + search_node + ")-[: " + node_relationship + "]->(nested_node) "
                                                                                       "Return nested_node.uid"):
            return record[0]

    node_name = list(json_schema.keys())[0]
    relationships = json_schema[node_name]

    array = []
    for relationship in relationships:
        relationship_name = list(relationship.keys())[0]
        uid = ""
        new_node = ""

        with driver.session() as session:
            uid = session.read_transaction(read_relationships, node_name, relationship_name)

        if relationship_name == "has_value":
            new_node = DataObject.nodes.get(uid=uid)
        else:
            new_node = E1_CRM_Entity.nodes.get(uid=uid)

        json_nested = relationship[relationship_name]

        array.append(nested_json(new_node, json_nested))

    return dict(node.decodeJSON(), **{"relationships": array})