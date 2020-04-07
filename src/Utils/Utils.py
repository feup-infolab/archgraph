from neo4j import GraphDatabase
# TODO nao apagar estes importes
from src.Models.CRM.v5_0_2.NodeEntities.E4_Period import E4_Period
from src.Models.CRM.v5_0_2.NodeEntities.E5_Event import E5_Event
from src.Models.DataObject.v0_0_2 import DataObject
from src.Models.DataObject.v0_0_2.Approximate import Approximate
from src.Models.DataObject.v0_0_2.AuthorityFile import AuthorityFile
from src.Models.DataObject.v0_0_2.AuthorityString import AuthorityString
from src.Models.DataObject.v0_0_2.Boolean import Boolean
from src.Models.DataObject.v0_0_2.Date import Date
from src.Models.DataObject.v0_0_2.Decimal import Decimal
from src.Models.DataObject.v0_0_2.GeospatialCoordinates import \
    GeospatialCoordinates
from src.Models.DataObject.v0_0_2.Instant import Instant
from src.Models.DataObject.v0_0_2.Integer import Integer
from src.Models.DataObject.v0_0_2.Interval import Interval
from src.Models.DataObject.v0_0_2.Latitude import Latitude
from src.Models.DataObject.v0_0_2.Longitude import Longitude
from src.Models.DataObject.v0_0_2.PersonName import PersonName
from src.Models.DataObject.v0_0_2.Polygon import Polygon
from src.Models.DataObject.v0_0_2.RegexString import RegexString
from src.Models.DataObject.v0_0_2.String import String

from src.Models.ArchOnto.v0_1.NodeEntities.ARE2_Formal_Title import ARE2_Formal_Title
from src.Models.CRM.v5_0_2.NodeEntities.E12_Production import E12_Production
from src.Models.CRM.v5_0_2.NodeEntities.E22_Human_Made_Object import E22_Human_Made_Object
from src.Models.CRM.v5_0_2.NodeEntities.E35_Title import E35_Title
from src.Models.CRM.v5_0_2.NodeEntities.E41_Appellation import E41_Appellation
from src.Models.CRM.v5_0_2.NodeEntities.E53_Place import E53_Place
from src.Models.CRM.v5_0_2.NodeEntities.E70_Thing import E70_Thing
from src.Models.CRM.v5_0_2.NodeEntities.E55_Type import E55_Type
from src.Models.CRM.v5_0_2.NodeEntities.E1_CRM_Entity import E1_CRM_Entity
from src.Models.CRM.v5_0_2.NodeEntities.E18_Physical_Thing import E18_Physical_Thing
from src.Models.CRM.v5_0_2.NodeEntities.E24_Physical_Human_Made_Thing import E24_Physical_Human_Made_Thing
from src.Models.CRM.v5_0_2.NodeEntities.E52_Time_Span import E52_Time_Span
from src.Models.CRM.v5_0_2.NodeEntities.E72_Legal_Object import E72_Legal_Object
from src.Models.CRM.v5_0_2.NodeEntities.E39_Actor import E39_Actor
from src.Models.CRM.v5_0_2.NodeEntities.E7_Activity import E7_Activity
from src.Models.CRM.v5_0_2.NodeEntities.E2_Temporal_Entity import E2_Temporal_Entity
from src.Models.CRM.v5_0_2.NodeEntities.E83_Type_Creation import E83_Type_Creation
from src.Models.CRM.v5_0_2.NodeEntities.E77_Persistent_Item import E77_Persistent_Item


# TODO nao apagar estes importes

uri = "bolt://localhost:7687"
driver = GraphDatabase.driver(uri, auth=("neo4j", "password"))


def nested_json(node, json_schema):
    if isinstance(json_schema, str):
        return node.decodeJSON()

    def read_relationships(tx, search_node, node_relationship):
        array_uid = []
        records = tx.run("MATCH (a: " + search_node + ")-[: " + node_relationship + "]->(nested_node) "
                                                                                    "Return nested_node.uid")
        for record in records:
            array_uid.append(record[0])
        return array_uid

    node_name = list(json_schema.keys())[0]
    relationships = json_schema[node_name]
    array = []

    for relationship in relationships:
        relationship_name = list(relationship.keys())[0]
        uid = ""
        new_node = ""

        with driver.session() as session:
            array_uid = session.read_transaction(read_relationships, node_name, relationship_name)

        json_nested = relationship[relationship_name]

        for uid in array_uid:
            if relationship_name == "has_value":
                new_node = DataObject.nodes.get(uid=uid)
            else:
                new_node = E1_CRM_Entity.nodes.get(uid=uid)

            array.append(nested_json(new_node, json_nested))

    return dict(node.decodeJSON(), **{"relationships": array})


def get_node_by_uid(uid):
    try:
        return DataObject.nodes.get(uid=uid)
    except:
        try:
            return E1_CRM_Entity.nodes.get(uid=uid)
        except:
            return None


def delete_node_by_uid(uid):
    try:
        node = DataObject.nodes.get(uid=uid)
        node.delete()
        return True
    except:
        try:
            node = E1_CRM_Entity.nodes.get(uid=uid)
            node.delete()
            return True
        except:
            return None

