import datetime
import unittest

from src.Models.CRM.v5_0_2.NodeEntities.E10_Transfer_of_Custody import E10_Transfer_of_Custody
from src.Models.CRM.v5_0_2.NodeEntities.E11_Modification import E11_Modification
from src.Models.CRM.v5_0_2.NodeEntities.E13_Attribute_Assignment import E13_Attribute_Assignment
from src.Models.CRM.v5_0_2.NodeEntities.E14_Condition_Assessment import E14_Condition_Assessment
from src.Models.CRM.v5_0_2.NodeEntities.E15_Identifier_Assignment import E15_Identifier_Assignment
from src.Models.CRM.v5_0_2.NodeEntities.E16_Measurement import E16_Measurement
from src.Models.CRM.v5_0_2.NodeEntities.E17_Type_Assignment import E17_Type_Assignment
from src.Models.CRM.v5_0_2.NodeEntities.E19_Physical_Object import E19_Physical_Object
from src.Models.CRM.v5_0_2.NodeEntities.E20_Biological_Object import E20_Biological_Object
from src.Models.CRM.v5_0_2.NodeEntities.E21_Person import E21_Person
from src.Models.CRM.v5_0_2.NodeEntities.E3_Condition_State import E3_Condition_StateSchema, E3_Condition_State
from src.Models.CRM.v5_0_2.NodeEntities.E4_Period import E4_Period
from src.Models.CRM.v5_0_2.NodeEntities.E5_Event import E5_Event
from src.Models.CRM.v5_0_2.NodeEntities.E6_Destruction import E6_Destruction
from src.Models.CRM.v5_0_2.NodeEntities.E8_Acquisition import E8_Acquisition
from src.Models.CRM.v5_0_2.NodeEntities.E9_Move import E9_Move
from src.Utils.Utils import nested_json

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
from src.Models.CRM.v5_0_2.NodeProperties.PC14_Carried_Out_By import PC14_Carried_Out_By

from neomodel import (
    config,
    OUTGOING,
    Traversal,
    DeflateError,
    AttemptedCardinalityViolation,
    db,
)

from src.GCF.utils.db import clean_database

import json

from src.Models.DataObject.v0_0_2.Interval import Interval
from src.Models.DataObject.v0_0_2.String import String
from src.Utils.JsonEncoder import (
    json_merge,
    index_creation,
    search_cidoc,
    specific_index_creation,
    search_specific_cidoc,
    index_drop,
    specific_index_drop,
    list_indexes,
)

clean_database()

config.DATABASE_URL = "bolt://neo4j:password@localhost:7687"
#ref = list_indexes()
#if ref[0].__len__() != 0:
try:
    index_creation()
except:
    index_drop()
    index_creation()

try:
    specific_index_creation()
except:
    specific_index_drop()
    specific_index_creation()


e1 = E1_CRM_Entity(name="test").save()
e1_2 = E1_CRM_Entity(name="test").save()
e55 = E55_Type(name="test2").save()
e1_2.P2_has_type.connect(e55)

e55_2 = E55_Type(name="test3").save()
e7 = E7_Activity(name="e7").save()
e18 = E18_Physical_Thing(name="e18").save()
e18_2 = E18_Physical_Thing(name="e18_2").save()
e24 = E24_Physical_Human_Made_Thing(name="e24").save()
e83 = E83_Type_Creation(name="e83").save()


class TestNeoModel(unittest.TestCase):
    def test_basic_relationship(self):
        # Tests creation of basic relationships
        # Creates 2 P2_Has_Type Relationships that connect A E1 instance to a E55 and that E55 to another

        e1.P2_has_type.connect(e55)
        e55_2.P2_has_type.connect(e55)
        # Obtains origin of relationship
        all_types = e55.P2_has_type.filter(name="test2")
        # Check if Node is the correct one
        for p in all_types:
            self.assertAlmostEqual(p.id, e1.id)

    def test_traversal(self):
        # Tests Creation of Traversals
        # Creates definition of traversal, the destination node must be a E55, and can be through any relationship
        definition = dict(
            node_class=E55_Type, direction=OUTGOING, relation_type=None, model=None
        )
        # Define traversal and perform it
        relations_traversal = Traversal(e1, E55_Type.__label__, definition)
        all_relations = relations_traversal.all()
        # Check if traversal returned correct nodes
        e55rels = e55_2.P2_has_type
        for p in all_relations:
            self.assertAlmostEqual(p.id, e55.id)
        for p in e55rels:
            self.assertAlmostEqual(p.id, e55.id)

    def test_illegal_relationship(self):
        # Tests creation of illegal relationships, by raising of exception
        # e7.is_composed_of.connect(e1)
        # e1.was_based_on.connect(e83)
        # e83.was_based_on.connect(e1)
        self.assertRaises(ValueError, e18.P46_is_composed_of.connect, e1)

    def test_diamond_problem(self):
        # Tests if E24 that inherits showsFeaturesOf from both it's superclasses (P130, that E70 has from which E71
        # and and E18 inherit)
        e18.P130_shows_features_of.connect(e24)
        all_features = e18.P130_shows_features_of.filter(name="e24")
        for p in all_features:
            self.assertAlmostEqual(p.id, e24.id)

    def test_multiple_inheritance_queries(self):
        # Test if multiple levels of inheritance is detected
        found_e24 = E72_Legal_Object.nodes.get(name="e24")
        self.assertAlmostEqual(found_e24.id, e24.id)

    def test_data_property_types(self):
        # Test if data properties are stored using correct data properties
        future_date = datetime.datetime(2020, 5, 17)
        e52 = E52_Time_Span(name="e52", date=future_date).save()
        # Querying the database by data property
        returned_e52 = E52_Time_Span.nodes.get(date=future_date)
        self.assertAlmostEqual(e52.id, returned_e52.id)
        # Check if exception is raised if wrong type of data property is created
        self.assertRaises(
            DeflateError, E52_Time_Span(name="e52", date="shouldn't work").save
        )

    def test_expand_graph_3_levels(self):
        # Test if traversals can be done for 3 levels
        # Creation of traversal that can go into any node (since E1 is the basis for all cidoc nodes)
        definition = dict(
            node_class=E1_CRM_Entity, direction=OUTGOING, relation_type=None, model=None
        )
        relations_traversal = Traversal(e1, E1_CRM_Entity.__label__, definition)
        # Creation of traversal to 2nd level
        all_relations = relations_traversal.all()
        relations_traversal2 = Traversal(
            relations_traversal, E1_CRM_Entity.__label__, definition
        )
        # Creation of traversal to 3rd level
        all_relations2 = relations_traversal2.all()
        # Confirmation of the traversal destinations
        for p in all_relations:
            self.assertAlmostEqual(p.id, e55.id)
        for p in all_relations2:
            self.assertAlmostEqual(p.id, e55_2.id)

    def test_cardinality(self):
        # Test if cardinality holds
        # A placeholder relationship was created with cardinality One
        # Three nodes created, in order to check if it's possible to break the cardinality constraint
        e2_1 = E2_Temporal_Entity(name="instante_1").save()
        e2_2 = E2_Temporal_Entity(name="instante_2").save()
        e2_3 = E2_Temporal_Entity(name="instante_3").save()
        # Creation of first relationship, shouldn't break
        e2_1.P114_is_equal_in_time_to.connect(e2_2)
        # Creation of second relationship, should raise exception
        self.assertRaises(
            AttemptedCardinalityViolation, e2_1.P114_is_equal_in_time_to.connect, e2_3
        )

    def test_ternary_relationship(self):
        # Test to check ternary functioning
        # Creation of both domain and range class instances
        e39 = E39_Actor(name="e39").save()
        e7 = E7_Activity(name="e7").save()
        e55_4 = E55_Type(name="e55").save()
        # Creation of property entity instance
        pc14 = PC14_Carried_Out_By(name="PC14").save()
        # Creation of relations for property
        pc14.hasDomain.connect(e7)
        pc14.hasRange.connect(e39)
        pc14.inTheRoleOf.connect(e55_4)
        # Retrieval of node
        returned_pc14 = PC14_Carried_Out_By.nodes.get(name="PC14")
        self.assertTrue("PC0_CRM_Property" in returned_pc14.labels())
        # When serialization is complete test how to remove it through verification

    def test_case(self):
        # Define nodes to use
        monumento = E70_Thing(name="Monumentooo").save()
        titulo_torre_eiffel = E35_Title(name="Torre Eiffel").save()
        paris = E53_Place(name="Paris").save()
        torre_eiffel = E24_Physical_Human_Made_Thing(name="Torre Eiffel").save()
        uma_entidade_qualquer = E1_CRM_Entity(name="E1 de Teste").save()

        # Definition of Relations
        torre_eiffel.P156_occupies.connect(paris)
        torre_eiffel.P102_has_title.connect(titulo_torre_eiffel)
        monumento.P130_shows_features_of.connect(torre_eiffel)

        # Exception Raised on Illegal Relation
        self.assertRaises(
            ValueError,
            torre_eiffel.P130_shows_features_of.connect,
            uma_entidade_qualquer,
        )

    def test_full_test(self):
        # Testing full test searching and indexing
        monument = E70_Thing(name="Monument").save()
        monument2 = E70_Thing(name="Monument2").save()

        # General Search Test
        test_results = search_cidoc("Monument")
        # Fuzzy Search Test
        test_results3 = search_specific_cidoc("E70_Thing", "Monument")
        # Specific Search Test
        test_results2 = search_cidoc('"Monument2"')

        # Results of General Search
        self.assertEqual(
            test_results[0].labels,
            {"E70_Thing", "E77_Persistent_Item", "E1_CRM_Entity"},
        )
        self.assertEqual(
            test_results[0].properties, {"name": "Monument", "uid": monument.uid}
        )
        self.assertEqual(
            test_results[1].labels,
            {"E70_Thing", "E77_Persistent_Item", "E1_CRM_Entity"},
        )
        self.assertEqual(
            test_results[1].properties, {"name": "Monument2", "uid": monument2.uid}
        )
        # Results of Fuzzy Search
        self.assertEqual(
            test_results2[0].labels,
            {"E70_Thing", "E77_Persistent_Item", "E1_CRM_Entity"},
        )
        self.assertEqual(
            test_results2[0].properties, {"name": "Monument2", "uid": monument2.uid}
        )
        # Results of Specific Search
        self.assertEqual(
            test_results3[0].labels,
            {"E70_Thing", "E77_Persistent_Item", "E1_CRM_Entity"},
        )
        self.assertEqual(
            test_results3[0].properties, {"name": "Monument", "uid": monument.uid}
        )

        # Test of JSON Serialization of search result / Due to the nature of Set inside of labels is always different
        # so labels must be found to be tested
        json_results = test_results[0].encodeJSON()
        start = json_results.find("[") + len("[")
        end = json_results.find("]")
        substring = json_results[start:end]

        self.assertEqual(
            test_results[0].encodeJSON(),
            '{"labels": ['
            + substring
            + '], "name": "Monument", "uid": "'
            + monument.uid
            + '"}',
        )

    def test_create_graph(self):
        e22 = E22_Human_Made_Object(name="humam_made_object").save()
        are2 = ARE2_Formal_Title(name="Document Title").save()
        string = String(name="string name", stringValue="Registo_de_Baptismo").save()

        e22.P102_has_title.connect(are2)
        are2.has_value.connect(string)

        startDatetime = datetime.datetime(1812, 2, 12)
        endDatetime = datetime.datetime(1812, 2, 13)
        e12 = E12_Production(name="Document Production").save()
        e52 = E52_Time_Span(name="Production time", date=startDatetime).save()
        e41 = E41_Appellation(name="1812-02-12").save()

        node = Interval(
            name="1812-02-12", startDateValue=startDatetime, endDateValue=endDatetime
        ).save()

        e41.has_value.connect(node)
        e52.P1_is_identified_by.connect(e41)
        e12.P4_has_time_span.connect(e52)
        e22.P108_has_produced_by.connect(e12)

    def test_schema(self):
        e2 = E2_Temporal_Entity(name="E2").save()
        e3 = E3_Condition_State(name="E3").save()
        e4 = E4_Period(name="E4").save()
        e5 = E5_Event(name="E5").save()
        e6 = E6_Destruction(name="E6").save()
        e8 = E8_Acquisition(name="E8").save()
        e9 = E9_Move(name="E9").save()
        e10 = E10_Transfer_of_Custody(name="E10").save()
        e11 = E11_Modification(name="E11").save()
        e12 = E12_Production(name="E12").save()
        e13 = E13_Attribute_Assignment(name="E13").save()
        e14 = E14_Condition_Assessment(name="E14").save()
        e15 = E15_Identifier_Assignment(name="E15").save()
        e16 = E16_Measurement(name="E16").save()
        e17 = E17_Type_Assignment(name="E17").save()
        e19 = E19_Physical_Object(name="E19").save()
        e20 = E20_Biological_Object(name="E20").save()
        e21 = E21_Person(name="E21").save()
        e22 = E22_Human_Made_Object(name="E22").save()

        e41 = E41_Appellation(name="1812-02-12").save()
        e52 = E52_Time_Span(
            name="Production time", date=datetime.datetime(1812, 2, 12)
        ).save()

        e70 = E70_Thing(name="E70").save()
        print(e1.getSchema())
        print(e2.getSchema())
        print(e3.getSchema())
        print(e4.getSchema())
        print(e5.getSchema())
        print(e6.getSchema())
        print(e7.getSchema())
        print(e8.getSchema())
        print(e9.getSchema())
        print(e10.getSchema())
        print(e11.getSchema())
        print(e12.getSchema())
        print(e13.getSchema())
        print(e14.getSchema())
        print(e15.getSchema())
        print(e16.getSchema())
        print(e17.getSchema())
        print(e18.getSchema())
        print(e19.getSchema())
        print(e20.getSchema())
        print(e21.getSchema())
        print(e22.getSchema())
        print(e24.getSchema())

        print(e41.getSchema())
        print(e52.getSchema())
        print(e55.getSchema())

        print(e70.getSchema())
        print(e83.getSchema())

    def test_serialization(self):
        startDatetime = datetime.datetime(1812, 2, 12)
        endDatetime = datetime.datetime(1812, 2, 13)

        e52 = E52_Time_Span(
            name="Production time", date=datetime.datetime(1812, 2, 12)
        ).save()
        e41 = E41_Appellation(name="1812-02-12").save()

        node = Interval(
            name="1812-02-12", startDateValue=startDatetime, endDateValue=endDatetime
        ).save()
        node2 = Interval(
            name="1812-02-12", startDateValue=startDatetime, endDateValue=endDatetime
        ).save()

        e41.has_value.connect(node)
        e41.has_value.connect(node2)
        e52.P1_is_identified_by.connect(e41)

        json1 = {"E41_Appellation": {"has_value": "DataObject"}}
        # result1 = json.dumps(nested_json(e41, json1))
        # #e41.get_schema_with_template(json1)
        # print(result1)
        #
        # # example 2
        # json2 = {
        #     "E52_Time_Span":
        #         {
        #             "P1_is_identified_by": {
        #                 "E41_Appellation": {"has_value": "DataObject"}
        #             }
        #         }
        #
        # }
        # result2 = json.dumps(nested_json(e52, json2))
        # print(result2)

        # example 3
        thing = E70_Thing(name="thing").save()
        title = E35_Title(name="title").save()
        place = E53_Place(name="place").save()
        humanThing = E24_Physical_Human_Made_Thing(name="humam Eiffel").save()

        humanThing.P156_occupies.connect(place)
        humanThing.P102_has_title.connect(title)
        thing.P130_shows_features_of.connect(humanThing)
        #
        # json3 = {
        #     "E70_Thing":
        #         {
        #             "P130_shows_features_of": {
        #                 "E24_Physical_Human_Made_Thing":
        #                     {"P102_has_title": "E35_Title",
        #                      "P156_occupies": "E53_Place"},
        #
        #             }
        #         }
        #
        # }
        # result3 = json.dumps(nested_json(thing, json3))
        # print(result3)

    def test_schema_with_template(self):
        e18.P46_is_composed_of.connect(e18)

        json1 = {
            "E18_Physical_Thing":
                {"P46_is_composed_of": "E18_Physical_Thing"}
        }

        e18.get_schema_with_template(json1)

        e2 = E2_Temporal_Entity(name="E2_222").save()
        date = datetime.datetime(2020, 5, 17)
        e52 = E52_Time_Span(name="E52_22", date=date).save()
        dataobject = String(name="name", stringValue="String_Value").save()

        e2.P4_has_time_span.connect(e52)
        e52.has_value.connect(dataobject)

        json2 = {
            "E2_Temporal_Entity":
                {"P4_has_time_span": {
                    "E52_Time_Span":
                            {"has_value": "DataObject"}

                    }
                }
        }
        json2_1 = {
        "E52_Time_Span":
                {"has_value": "DataObject"}

        }
        e2.get_schema_with_template(json2)
        e52.get_schema_with_template(json2_1)

        result3 = json.dumps(nested_json(e2, json2))
        print(result3)


var = {'$schema': 'http://json-schema.org/draft-07/schema#', 'definitions': {
    'E2_Temporal_EntitySchema': {'type': 'object', 'properties': {'name': {'title': 'name', 'type': 'string'},
                                                                  'uid': {'title': 'uid', 'type': 'string'},
                                                                  'P4_has_time_span': {'type': 'object',
                                                                                       '$ref': '#/definitions/E52_Time_SpanSchema'}},
                                 'additionalProperties': False, 'required': ['name']},
    'E52_Time_SpanSchema': {'type': 'object',
                            'properties': {'date': {'title': 'date', 'type': 'string', 'format': 'date'},
                                           'name': {'title': 'name', 'type': 'string'},
                                           'uid': {'title': 'uid', 'type': 'string'},
                                           'has_value': {'title': 'has_value', 'type': 'array',
                                                         'items': {'type': 'object',
                                                                   '$ref': '#/definitions/DataObjectSchema'}}},
                            'additionalProperties': False, 'required': ['date', 'name']},
    'DataObjectSchema': {'type': 'object', 'properties': {'name': {'title': 'name', 'type': 'string'},
                                                          'uid': {'title': 'uid', 'type': 'string'}},
                         'additionalProperties': False, 'required': ['name']}},
       '$ref': '#/definitions/E2_Temporal_EntitySchema'}



var2 = {'$schema': 'http://json-schema.org/draft-07/schema#', 'definitions': {'E52_Time_SpanSchema': {'properties': {
    'P137_exemplifies': {'title': 'P137_exemplifies', 'type': 'array',
                         'items': {'type': 'object', '$ref': '#/definitions/E55_TypeSchema'}},
    'date': {'title': 'date', 'type': 'string', 'format': 'date'}, 'has_value': {'title': 'has_value', 'type': 'array',
                                                                                 'items': {'type': 'object',
                                                                                           '$ref': '#/definitions/DataObjectSchema'}},
    'name': {'title': 'name', 'type': 'string'}, 'uid': {'title': 'uid', 'type': 'string'}}, 'type': 'object',
                                                                                                     'required': [
                                                                                                         'date',
                                                                                                         'name'],
                                                                                                     'additionalProperties': False},
                                                                             'DataObjectSchema': {'properties': {
                                                                                 'name': {'title': 'name',
                                                                                          'type': 'string'},
                                                                                 'uid': {'title': 'uid',
                                                                                         'type': 'string'}},
                                                                                                  'type': 'object',
                                                                                                  'required': ['name'],
                                                                                                  'additionalProperties': False},
                                                                             'E2_Temporal_EntitySchema': {
                                                                                 'properties': {
                                                                                     'P114_is_equal_in_time_to': {
                                                                                         'type': 'object',
                                                                                         '$ref': '#/definitions/E52_Time_SpanSchema'},
                                                                                     'P4_has_time_span': {
                                                                                         'type': 'object',
                                                                                         '$ref': '#/definitions/E52_Time_SpanSchema'},
                                                                                     'has_value': {'title': 'has_value',
                                                                                                   'type': 'array',
                                                                                                   'items': {
                                                                                                       'type': 'object',
                                                                                                       '$ref': '#/definitions/DataObjectSchema'}},
                                                                                     'name': {'title': 'name',
                                                                                              'type': 'string'},
                                                                                     'uid': {'title': 'uid',
                                                                                             'type': 'string'}},
                                                                                 'type': 'object', 'required': ['name'],
                                                                                 'additionalProperties': False}},
       '$ref': '#/definitions/E2_Temporal_EntitySchema'}

