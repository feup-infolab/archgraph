import json
import datetime
import marshmallow.fields as fields

from neo4j import GraphDatabase
from neomodel import db
import importlib

# TODO nao apagar estes importes
from src.Models.CRM.v5_0_2.NodeEntities.E4_Period import E4_Period, E4_PeriodSchema
from src.Models.CRM.v5_0_2.NodeEntities.E5_Event import E5_Event, E5_EventSchema
from src.Models.DataObject.v0_0_2.DataObject import DataObject, DataObjectSchema
from src.Models.DataObject.v0_0_2.Approximate import Approximate, ApproximateSchema
from src.Models.DataObject.v0_0_2.AuthorityFile import (
    AuthorityFile,
    AuthorityFileSchema,
)
from src.Models.DataObject.v0_0_2.AuthorityString import (
    AuthorityString,
    AuthorityStringSchema,
)
from src.Models.DataObject.v0_0_2.Boolean import Boolean, BooleanSchema
from src.Models.DataObject.v0_0_2.Date import Date, DateSchema
from src.Models.DataObject.v0_0_2.Decimal import Decimal, DecimalSchema
from src.Models.DataObject.v0_0_2.GeospatialCoordinates import (
    GeospatialCoordinates,
    GeospatialCoordinatesSchema,
)
from src.Models.DataObject.v0_0_2.Instant import Instant, InstantSchema
from src.Models.DataObject.v0_0_2.Integer import Integer, IntegerSchema
from src.Models.DataObject.v0_0_2.Interval import Interval, IntervalSchema
from src.Models.DataObject.v0_0_2.Latitude import Latitude, LatitudeSchema
from src.Models.DataObject.v0_0_2.Longitude import Longitude, LongitudeSchema
from src.Models.DataObject.v0_0_2.PersonName import PersonName, PersonNameSchema
from src.Models.DataObject.v0_0_2.Polygon import Polygon, PolygonSchema
from src.Models.DataObject.v0_0_2.RegexString import RegexString, RegexStringSchema
from src.Models.DataObject.v0_0_2.String import String, StringSchema

from src.Models.ArchOnto.v0_1.NodeEntities.ARE2_Formal_Title import ARE2_Formal_Title
from src.Models.CRM.v5_0_2.NodeEntities.E1_CRM_Entity import (
    E1_CRM_Entity,
    E1_CRM_EntitySchema,
)
from src.Models.CRM.v5_0_2.NodeEntities.E2_Temporal_Entity import (
    E2_Temporal_Entity,
    E2_Temporal_EntitySchema,
)
from src.Models.CRM.v5_0_2.NodeEntities.E3_Condition_State import (
    E3_Condition_State,
    E3_Condition_StateSchema,
)
from src.Models.CRM.v5_0_2.NodeEntities.E4_Period import E4_Period, E4_PeriodSchema
from src.Models.CRM.v5_0_2.NodeEntities.E5_Event import E5_Event, E5_EventSchema
from src.Models.CRM.v5_0_2.NodeEntities.E6_Destruction import (
    E6_Destruction,
    E6_DestructionSchema,
)
from src.Models.CRM.v5_0_2.NodeEntities.E7_Activity import (
    E7_Activity,
    E7_ActivitySchema,
)
from src.Models.CRM.v5_0_2.NodeEntities.E8_Acquisition import (
    E8_Acquisition,
    E8_AcquisitionSchema,
)
from src.Models.CRM.v5_0_2.NodeEntities.E9_Move import E9_Move, E9_MoveSchema
from src.Models.CRM.v5_0_2.NodeEntities.E10_Transfer_of_Custody import (
    E10_Transfer_of_Custody,
    E10_Transfer_of_CustodySchema,
)
from src.Models.CRM.v5_0_2.NodeEntities.E11_Modification import (
    E11_Modification,
    E11_ModificationSchema,
)
from src.Models.CRM.v5_0_2.NodeEntities.E12_Production import (
    E12_Production,
    E12_ProductionSchema,
)
from src.Models.CRM.v5_0_2.NodeEntities.E13_Attribute_Assignment import (
    E13_Attribute_Assignment,
    E13_Attribute_AssignmentSchema,
)
from src.Models.CRM.v5_0_2.NodeEntities.E14_Condition_Assessment import (
    E14_Condition_Assessment,
    E14_Condition_AssessmentSchema,
)
from src.Models.CRM.v5_0_2.NodeEntities.E15_Identifier_Assignment import (
    E15_Identifier_Assignment,
    E15_Identifier_AssignmentSchema,
)
from src.Models.CRM.v5_0_2.NodeEntities.E16_Measurement import (
    E16_Measurement,
    E16_MeasurementSchema,
)
from src.Models.CRM.v5_0_2.NodeEntities.E17_Type_Assignment import (
    E17_Type_Assignment,
    E17_Type_AssignmentSchema,
)
from src.Models.CRM.v5_0_2.NodeEntities.E18_Physical_Thing import (
    E18_Physical_Thing,
    E18_Physical_ThingSchema,
)
from src.Models.CRM.v5_0_2.NodeEntities.E19_Physical_Object import (
    E19_Physical_Object,
    E19_Physical_ObjectSchema,
)
from src.Models.CRM.v5_0_2.NodeEntities.E20_Biological_Object import (
    E20_Biological_Object,
    E20_Biological_ObjectSchema,
)
from src.Models.CRM.v5_0_2.NodeEntities.E21_Person import E21_Person, E21_PersonSchema
from src.Models.CRM.v5_0_2.NodeEntities.E22_Human_Made_Object import (
    E22_Human_Made_Object,
    E22_Human_Made_ObjectSchema,
)
from src.Models.CRM.v5_0_2.NodeEntities.E24_Physical_Human_Made_Thing import (
    E24_Physical_Human_Made_Thing,
    E24_Physical_Human_Made_ThingSchema,
)
from src.Models.CRM.v5_0_2.NodeEntities.E25_Human_Made_Feature import (
    E25_Human_Made_Feature,
    E25_Human_Made_FeatureSchema,
)
from src.Models.CRM.v5_0_2.NodeEntities.E26_Physical_Feature import (
    E26_Physical_Feature,
    E26_Physical_FeatureSchema,
)
from src.Models.CRM.v5_0_2.NodeEntities.E27_Site import E27_Site, E27_SiteSchema
from src.Models.CRM.v5_0_2.NodeEntities.E28_Conceptual_Object import (
    E28_Conceptual_Object,
    E28_Conceptual_ObjectSchema,
)
from src.Models.CRM.v5_0_2.NodeEntities.E29_Design_or_Procedure import (
    E29_Design_or_Procedure,
    E29_Design_or_ProcedureSchema,
)
from src.Models.CRM.v5_0_2.NodeEntities.E30_Right import E30_Right, E30_RightSchema
from src.Models.CRM.v5_0_2.NodeEntities.E31_Document import (
    E31_Document,
    E31_DocumentSchema,
)
from src.Models.CRM.v5_0_2.NodeEntities.E32_Authority_Document import (
    E32_Authority_Document,
    E32_Authority_DocumentSchema,
)
from src.Models.CRM.v5_0_2.NodeEntities.E33_Linguistic_Object import (
    E33_Linguistic_Object,
    E33_Linguistic_ObjectSchema,
)
from src.Models.CRM.v5_0_2.NodeEntities.E34_Inscription import (
    E34_Inscription,
    E34_InscriptionSchema,
)
from src.Models.CRM.v5_0_2.NodeEntities.E35_Title import E35_Title, E35_TitleSchema
from src.Models.CRM.v5_0_2.NodeEntities.E36_Visual_Item import (
    E36_Visual_Item,
    E36_Visual_ItemSchema,
)
from src.Models.CRM.v5_0_2.NodeEntities.E37_Mark import E37_Mark, E37_MarkSchema
from src.Models.CRM.v5_0_2.NodeEntities.E39_Actor import E39_Actor, E39_ActorSchema
from src.Models.CRM.v5_0_2.NodeEntities.E41_Appellation import (
    E41_Appellation,
    E41_AppellationSchema,
)
from src.Models.CRM.v5_0_2.NodeEntities.E42_Identifier import (
    E42_Identifier,
    E42_IdentifierSchema,
)
from src.Models.CRM.v5_0_2.NodeEntities.E52_Time_Span import (
    E52_Time_Span,
    E52_Time_SpanSchema,
)
from src.Models.CRM.v5_0_2.NodeEntities.E53_Place import E53_Place, E53_PlaceSchema
from src.Models.CRM.v5_0_2.NodeEntities.E54_Dimension import (
    E54_Dimension,
    E54_DimensionSchema,
)
from src.Models.CRM.v5_0_2.NodeEntities.E55_Type import E55_Type, E55_TypeSchema
from src.Models.CRM.v5_0_2.NodeEntities.E56_Language import (
    E56_Language,
    E56_LanguageSchema,
)
from src.Models.CRM.v5_0_2.NodeEntities.E57_Material import (
    E57_Material,
    E57_MaterialSchema,
)
from src.Models.CRM.v5_0_2.NodeEntities.E58_Measurement_Unit import (
    E58_Measurement_Unit,
    E58_Measurement_UnitSchema,
)
from src.Models.CRM.v5_0_2.NodeEntities.E63_Beggining_of_Existence import (
    E63_Beggining_of_Existence,
    E63_Beggining_of_ExistenceSchema,
)
from src.Models.CRM.v5_0_2.NodeEntities.E64_End_of_Existence import (
    E64_End_of_Existence,
    E64_End_of_ExistenceSchema,
)
from src.Models.CRM.v5_0_2.NodeEntities.E65_Creation import (
    E65_Creation,
    E65_CreationSchema,
)
from src.Models.CRM.v5_0_2.NodeEntities.E66_Formation import (
    E66_Formation,
    E66_FormationSchema,
)
from src.Models.CRM.v5_0_2.NodeEntities.E67_Birth import E67_Birth, E67_BirthSchema
from src.Models.CRM.v5_0_2.NodeEntities.E68_Dissolution import (
    E68_Dissolution,
    E68_DissolutionSchema,
)
from src.Models.CRM.v5_0_2.NodeEntities.E69_Death import E69_Death, E69_DeathSchema
from src.Models.CRM.v5_0_2.NodeEntities.E70_Thing import E70_Thing, E70_ThingSchema
from src.Models.CRM.v5_0_2.NodeEntities.E71_Human_Made_Thing import (
    E71_Human_Made_Thing,
    E71_Human_Made_ThingSchema,
)
from src.Models.CRM.v5_0_2.NodeEntities.E72_Legal_Object import (
    E72_Legal_Object,
    E72_Legal_ObjectSchema,
)
from src.Models.CRM.v5_0_2.NodeEntities.E73_Information_Object import (
    E73_Information_Object,
    E73_Information_ObjectSchema,
)
from src.Models.CRM.v5_0_2.NodeEntities.E74_Group import E74_Group, E74_GroupSchema
from src.Models.CRM.v5_0_2.NodeEntities.E77_Persistent_Item import (
    E77_Persistent_Item,
    E77_Persistent_ItemSchema,
)
from src.Models.CRM.v5_0_2.NodeEntities.E78_Curated_Holding import (
    E78_Curated_Holding,
    E78_Curated_HoldingSchema,
)
from src.Models.CRM.v5_0_2.NodeEntities.E79_Part_Addition import (
    E79_Part_Addition,
    E79_Part_AdditionSchema,
)
from src.Models.CRM.v5_0_2.NodeEntities.E80_Part_Removal import (
    E80_Part_Removal,
    E80_Part_RemovalSchema,
)
from src.Models.CRM.v5_0_2.NodeEntities.E81_Transformation import (
    E81_Transformation,
    E81_TransformationSchema,
)
from src.Models.CRM.v5_0_2.NodeEntities.E83_Type_Creation import (
    E83_Type_Creation,
    E83_Type_CreationSchema,
)
from src.Models.CRM.v5_0_2.NodeEntities.E85_Joining import (
    E85_Joining,
    E85_JoiningSchema,
)
from src.Models.CRM.v5_0_2.NodeEntities.E86_Leaving import (
    E86_Leaving,
    E86_LeavingSchema,
)
from src.Models.CRM.v5_0_2.NodeEntities.E87_Curation_Activity import (
    E87_Curation_Activity,
    E87_Curation_ActivitySchema,
)
from src.Models.CRM.v5_0_2.NodeEntities.E89_Propositional_Object import (
    E89_Propositional_Object,
    E89_Propositional_ObjectSchema,
)
from src.Models.CRM.v5_0_2.NodeEntities.E90_Symbolic_Object import (
    E90_Symbolic_Object,
    E90_Symbolic_ObjectSchema,
)
from src.Models.CRM.v5_0_2.NodeEntities.E92_Spacetime_Volume import (
    E92_Spacetime_Volume,
    E92_Spacetime_VolumeSchema,
)
from src.Models.CRM.v5_0_2.NodeEntities.E93_Presence import (
    E93_Presence,
    E93_PresenceSchema,
)
from src.Models.CRM.v5_0_2.NodeEntities.E95_Purchase import (
    E95_Purchase,
    E95_PurchaseSchema,
)
from src.Models.CRM.v5_0_2.NodeEntities.E97_Monetary_Amount import (
    E97_Monetary_Amount,
    E97_Monetary_AmountSchema,
)
from src.Models.CRM.v5_0_2.NodeEntities.E99_Product_Type import (
    E99_Product_Type,
    E99_Product_TypeSchema,
)

# TODO nao apagar estes importes

import src.Utils.Utils as self

import src.Utils.EnvVarManager as EnvVarManager

uri = (
    "bolt://neo4j:password@"
    + EnvVarManager.get_from_env_or_return_default("NEO4J_HOST", "127.0.0.1")
    + ":"
    + EnvVarManager.get_from_env_or_return_default("NEO4J_PORT", "27017")
)

driver = None


def get_driver():
    if self.driver is None:
        self.driver = GraphDatabase.driver(uri, auth=("neo4j", "password"))
    return self.driver


def read_relationships(search_node, search_node_uid, relationship_name):
    """The function reads all relation of a node with a given name"""

    def read(tx, search_node, search_node_uid, relationship_name):
        array_uids = []
        records = tx.run(
            "MATCH (a: "
            + search_node
            + "{ uid:'"
            + search_node_uid
            + "'}"
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
            read, search_node, search_node_uid, relationship_name
        )


def build_next_json(node, template):
    """The function builds information block for a node with a given template"""
    if isinstance(template, str):
        return node.decodeJSON()

    node_name = list(template.keys())[0]
    relationships = template[node_name]
    new_object = {}
    for relationship_name in relationships:
        schema_relationship = node.get_property_from_entity(relationship_name)
        if schema_relationship["type"] == "array":
            new_object[relationship_name] = []
        else:
            new_object[relationship_name] = {}

        json_nested = relationships[relationship_name]
        array_uid = read_relationships(node_name, node.uid, relationship_name)

        for uid in array_uid:
            new_node = get_node_by_uid(uid)
            if new_node is None:
                return None

            if schema_relationship["type"] == "array":
                result = build_next_json(new_node, json_nested)
                if result is None:
                    return None
                else:
                    new_object[relationship_name].append(result)
            else:
                result = build_next_json(new_node, json_nested)
                if result is None:
                    return None
                else:
                    new_object[relationship_name] = build_next_json(
                        new_node, json_nested
                    )

    return dict(node.decodeJSON(), **new_object)


def get_node_by_uid(uid):
    """The function get node from database with a given uid"""
    try:
        return DataObject.nodes.get(uid=uid)
    except:
        try:
            return E1_CRM_Entity.nodes.get(uid=uid)
        except:
            return None


def delete_node_by_uid(uid):
    """The function delete node from database with a given uid"""
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


def updated_node(node, data, template):
    """The function given a template and a node, the node and next nodes information is updated"""
    db.begin()
    result = updated_node_aux(node, data, template[list(template.keys())[0]])
    if result is None:
        db.rollback()
        return None
    else:
        db.commit()
        return True


def updated_node_aux(current_node, data, template):
    """Auxiliary function - The function given a template and a node, the node and next nodes information is updated"""
    new_node = current_node.build_node(data)
    if current_node.merge_node(new_node["self_node"]):
        for relationship_name in template:
            relationship_of_node = getattr(current_node, relationship_name)
            existing_relationships = relationship_of_node.all()
            for existing_relationship in existing_relationships:
                relationship_of_node.disconnect(existing_relationship)
            if relationship_name in new_node["relationships"]:
                new_relationships = new_node["relationships"][relationship_name]
                if (
                    add_all_relationships(
                        new_relationships,
                        relationship_of_node,
                        template[relationship_name],
                    )
                    is None
                ):
                    return None
        return True
    else:
        return None


def add_all_relationships(relationships, node, template):
    """The function given a template and the current node, the function add all relations to the current node"""

    def update_node_and_call_next(new_instance, next_node, template):
        for attr in next_node:
            if new_instance.schema.fields[attr].__class__ == fields.Date:
                setattr(
                    new_instance,
                    attr,
                    datetime.datetime.strptime(next_node[attr], "%Y-%m-%d"),
                )
            elif new_instance.schema.fields[attr].__class__ == fields.Str:
                setattr(new_instance, attr, next_node[attr])

        new_instance.save()
        node.connect(new_instance)
        if isinstance(template, str):
            return True
        else:
            return updated_node_aux(
                new_instance, next_node, template[new_instance.__class__.__name__]
            )

    for next_node in relationships:
        if "uid" not in next_node:
            range_class = node.definition["node_class"]
            new_instance = range_class()
            if update_node_and_call_next(new_instance, next_node, template) is None:
                return None
        else:
            uid = next_node["uid"]
            try:
                new_instance = DataObject.nodes.get(uid=uid)
                if update_node_and_call_next(new_instance, next_node, template) is None:
                    return None
            except:
                try:
                    new_instance = E1_CRM_Entity.nodes.get(uid=uid)
                    if (
                        update_node_and_call_next(new_instance, next_node, template)
                        is None
                    ):
                        return None
                except:
                    return None
    return True


def make_result(result):

    response_array = "["

    for i in range(len(result)):
        response_array += result[i].encodeJSON()
        if i < (len(result) - 1):
            response_array += ","

    response_array += "]"
    return response_array


def find_name_of_classes_in_project(classes_name):
    """The function given a classes name array, the function return the class instance"""
    classes = []
    error = False
    for class_name in classes_name:
        try:
            class__ = getattr(
                importlib.import_module(
                    "src.Models.DataObject.v0_0_2.NodeEntities." + class_name
                ),
                class_name,
            )
            classes.append(class__)
        except:
            try:
                class__ = getattr(
                    importlib.import_module(
                        "src.Models.CRM.v5_0_2.NodeEntities." + class_name
                    ),
                    class_name,
                )
                classes.append(class__)
            except:
                try:
                    class__ = getattr(
                        importlib.import_module(
                            "src.Models.ArchOnto.v0_1." + class_name
                        ),
                        class_name,
                    )
                    classes.append(class__)
                except:
                    error = True
                    break

    if error:
        return None
    else:
        return classes


def find_name_of_schema_classes_in_project(classes_name):
    """The function given a model class names array, the function return the schema class instance"""
    schemas_classes = []
    error = False

    for class_name in classes_name:
        try:
            schema_class = getattr(
                importlib.import_module(
                    "src.Models.DataObject.v0_0_2.NodeEntities." + class_name
                ),
                class_name + "Schema",
            )
            schemas_classes.append(schema_class)
        except:
            try:
                schema_class = getattr(
                    importlib.import_module(
                        "src.Models.CRM.v5_0_2.NodeEntities." + class_name
                    ),
                    class_name + "Schema",
                )
                schemas_classes.append(schema_class)
            except:
                try:
                    schema_class = getattr(
                        importlib.import_module(
                            "src.Models.ArchOnto.v0_1." + class_name
                        ),
                        class_name + "Schema",
                    )
                    schemas_classes.append(schema_class)
                except:
                    error = True
                    break
    if error:
        return None
    else:
        return schemas_classes
