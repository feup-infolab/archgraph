from neo4j import GraphDatabase

# TODO nao apagar estes importes
from src.Models.CRM.v5_0_2.NodeEntities.E4_Period import E4_Period
from src.Models.CRM.v5_0_2.NodeEntities.E5_Event import E5_Event
from src.Models.DataObject.v0_0_2.DataObject import DataObject
from src.Models.DataObject.v0_0_2.Approximate import Approximate
from src.Models.DataObject.v0_0_2.AuthorityFile import AuthorityFile
from src.Models.DataObject.v0_0_2.AuthorityString import AuthorityString
from src.Models.DataObject.v0_0_2.Boolean import Boolean
from src.Models.DataObject.v0_0_2.Date import Date
from src.Models.DataObject.v0_0_2.Decimal import Decimal
from src.Models.DataObject.v0_0_2.GeospatialCoordinates import GeospatialCoordinates
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
from src.Models.CRM.v5_0_2.NodeEntities.E22_Human_Made_Object import (
    E22_Human_Made_Object,
)
from src.Models.CRM.v5_0_2.NodeEntities.E35_Title import E35_Title
from src.Models.CRM.v5_0_2.NodeEntities.E41_Appellation import E41_Appellation
from src.Models.CRM.v5_0_2.NodeEntities.E53_Place import E53_Place
from src.Models.CRM.v5_0_2.NodeEntities.E70_Thing import E70_Thing
from src.Models.CRM.v5_0_2.NodeEntities.E55_Type import E55_Type
from src.Models.CRM.v5_0_2.NodeEntities.E1_CRM_Entity import E1_CRM_Entity
from src.Models.CRM.v5_0_2.NodeEntities.E18_Physical_Thing import E18_Physical_Thing
from src.Models.CRM.v5_0_2.NodeEntities.E24_Physical_Human_Made_Thing import (
    E24_Physical_Human_Made_Thing,
)
from src.Models.CRM.v5_0_2.NodeEntities.E52_Time_Span import E52_Time_Span
from src.Models.CRM.v5_0_2.NodeEntities.E72_Legal_Object import E72_Legal_Object
from src.Models.CRM.v5_0_2.NodeEntities.E39_Actor import E39_Actor
from src.Models.CRM.v5_0_2.NodeEntities.E7_Activity import E7_Activity
from src.Models.CRM.v5_0_2.NodeEntities.E2_Temporal_Entity import E2_Temporal_Entity
from src.Models.CRM.v5_0_2.NodeEntities.E83_Type_Creation import E83_Type_Creation
from src.Models.CRM.v5_0_2.NodeEntities.E77_Persistent_Item import E77_Persistent_Item

# TODO nao apagar estes importes

import src.Utils.Utils as self

uri = "bolt://localhost:7687"
driver = None


def get_driver():
    if self.driver is None:
        self.driver = GraphDatabase.driver(uri, auth=("neo4j", "password"))
    return self.driver


def nested_json(node, template):
    if isinstance(template, str):
        return node.decodeJSON()

    node_name = list(template.keys())[0]
    relationships = template[node_name]
    new_object = {}
    for relationship_name in relationships:
        schema_relationship = node.get_property_from_entity(relationship_name)
        if schema_relationship['type'] == 'array':
            new_object[relationship_name] = []
        else:
            new_object[relationship_name] = {}

        json_nested = relationships[relationship_name]
        array_uid = read_relationships(node_name, relationship_name)

        for uid in array_uid:
            new_node = get_node_by_uid(uid)
            if new_node is None:
                return None

            if schema_relationship['type'] == 'array':
                result = nested_json(new_node, json_nested)
                if result is None:
                    return None
                else:
                    new_object[relationship_name].append(result)
            else:
                result = nested_json(new_node, json_nested)
                if result is None:
                    return None
                else:
                    new_object[relationship_name] = nested_json(new_node, json_nested)

    return dict(node.decodeJSON(), **new_object)


def read_relationships(search_node, relationship_name):
    def read(tx, search_node, relationship_name):
        array_uids = []
        records = tx.run(
            "MATCH (a: "
            + search_node
            + ")-[: "
            + relationship_name
            + "]->(nested_node) "
            "Return nested_node.uid"
        )
        for record in records:
            array_uids.append(record[0])
        return array_uids

    with get_driver().session() as session:
        return session.read_transaction(
            read, search_node, relationship_name
        )


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
