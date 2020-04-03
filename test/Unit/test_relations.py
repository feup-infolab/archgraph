import datetime
import unittest

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
from src.Models.CRM.v5_0_2.NodeEntities.E21_Person import E21_Person
from src.Models.CRM.v5_0_2.NodeEntities.E2_Temporal_Entity import E2_Temporal_Entity
from src.Models.CRM.v5_0_2.NodeEntities.E83_Type_Creation import E83_Type_Creation
from src.Models.CRM.v5_0_2.NodeProperties.PC14_Carried_Out_By import PC14_Carried_Out_By

from neomodel import (config, OUTGOING, Traversal, DeflateError,
                      AttemptedCardinalityViolation, db)

from src.GCF.utils.db import clean_database

import json

from src.Models.DataObject.v0_0_2.Interval import Interval
from src.Models.DataObject.v0_0_2.String import String
from src.Utils.JsonEncoder import json_merge, index_creation, search_cidoc, specific_index_creation, \
    search_specific_cidoc, index_drop, specific_index_drop, list_indexes

clean_database()

config.DATABASE_URL = 'bolt://neo4j:password@localhost:7687'
ref = list_indexes()
if ref[0].__len__() != 0:
    index_drop()
    specific_index_drop()
index_creation()
specific_index_creation()
e1 = E1_CRM_Entity(name="test").save()
e1_2 = E1_CRM_Entity(name="test").save()
e55 = E55_Type(name="test2").save()
e1_2.hasType.connect(e55)

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

        e1.hasType.connect(e55)
        e55_2.hasType.connect(e55)
        # Obtains origin of relationship
        all_types = e55.hasType.filter(name="test2")
        # Check if Node is the correct one
        for p in all_types:
            self.assertAlmostEqual(p.id, e1.id)

    def test_traversal(self):
        # Tests Creation of Traversals
        # Creates definition of traversal, the destination node must be a E55, and can be through any relationship
        definition = dict(node_class=E55_Type, direction=OUTGOING, relation_type=None, model=None)
        # Define traversal and perform it
        relations_traversal = Traversal(e1, E55_Type.__label__, definition)
        all_relations = relations_traversal.all()
        # Check if traversal returned correct nodes
        e55rels = e55_2.hasType
        for p in all_relations:
            self.assertAlmostEqual(p.id, e55.id)
        for p in e55rels:
            self.assertAlmostEqual(p.id, e55.id)

    def test_illegal_relationship(self):
        # Tests creation of illegal relationships, by raising of exception
        # e7.is_composed_of.connect(e1)
        # e1.was_based_on.connect(e83)
        # e83.was_based_on.connect(e1)
        self.assertRaises(ValueError, e18.is_composed_of.connect, e1)

    def test_diamond_problem(self):
        # Tests if E24 that inherits showsFeaturesOf from both it's superclasses (P130, that E70 has from which E71
        # and and E18 inherit)
        e18.showsFeaturesOf.connect(e24)
        all_features = e18.showsFeaturesOf.filter(name="e24")
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
        self.assertRaises(DeflateError, E52_Time_Span(name="e52", date="shouldn't work").save)

    def test_expand_graph_3_levels(self):
        # Test if traversals can be done for 3 levels
        # Creation of traversal that can go into any node (since E1 is the basis for all cidoc nodes)
        definition = dict(node_class=E1_CRM_Entity, direction=OUTGOING, relation_type=None, model=None)
        relations_traversal = Traversal(e1, E1_CRM_Entity.__label__, definition)
        # Creation of traversal to 2nd level
        all_relations = relations_traversal.all()
        relations_traversal2 = Traversal(relations_traversal, E1_CRM_Entity.__label__, definition)
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
        e2_1.is_equal_in_time_to.connect(e2_2)
        # Creation of second relationship, should raise exception
        self.assertRaises(AttemptedCardinalityViolation, e2_1.is_equal_in_time_to.connect, e2_3)

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
        self.assertTrue('PC0_CRM_Property' in returned_pc14.labels())
        # When serialization is complete test how to remove it through verification

    def test_serialization(self):
        # Test to check if serialization works
        # Creation of nodes
        e21 = E21_Person(name="Roberto").save()
        e55_3 = E55_Type(name="Bibliotecario").save()
        # Creation of relationship
        e21.hasType.connect(e55_3)
        # Obtaining Json
        json_a = e21.encodeJSON()
        json_b = e55_3.encodeJSON()
        json_c = json.dumps(e21.hasType.relationship(e55_3).encodeJSON())
        # Merge of json documents
        json_d = json_merge(json_merge(json_a, json_b), json_c)
        # Printing the json for easy verification
        print(json_a)
        print(json_b)
        print(json_c)
        print(json_d)
        # Verification
        self.assertEqual(json_a, "{\"E21_Person\": {\"name\": \"Roberto\", \"uid\": \"" + e21.uid + "\"}}")
        self.assertEqual(json_b, "{\"E55_Type\": {\"name\": \"Bibliotecario\", \"uid\": \"" + e55_3.uid + "\"}}")
        # self.assertEqual(json_c, "{\"P2_has_type\": {""\"start_node\": {\"E21_Person\": {\"name\": \"Roberto\", "
        #                          "\"uid\": \"" + e21.uid + "\"}}, \"end_node\": {\"E55_Type\": {\"name\": "
        #                                                    "\"Bibliotecario\", \"uid\": \"" + e55_3.uid + "\"" +
        #                  "}}}}")
        # self.assertEqual(json_d, "{\"E21_Person\": {\"name\": \"Roberto\", \"id\": " + str(e21.id) +
        #                 "},\"E55_Type\": {\"name\": \"Bibliotecario\", \"id\": " + str(e55_3.id) + "},\"P2_has_type\": "
        #                                                                                        "{\"id\": " + str(
        #    e55_3.hasType.relationship(e21).id) + ", \"start_node\": {\"name\": \"Roberto\", \"id\": " + str(
        #    e21.id) + "}, \"end_node\": {\"name\": \"Bibliotecario\", \"id\": " + str(e55_3.id) + "}}}")

    def test_case(self):
        # Define nodes to use
        monumento = E70_Thing(name="Monumentooo").save()
        titulo_torre_eiffel = E35_Title(name="Torre Eiffel").save()
        paris = E53_Place(name="Paris").save()
        torre_eiffel = E24_Physical_Human_Made_Thing(name="Torre Eiffel").save()
        uma_entidade_qualquer = E1_CRM_Entity(name="E1 de Teste").save()

        # Definition of Relations
        torre_eiffel.occupies.connect(paris)
        torre_eiffel.has_title.connect(titulo_torre_eiffel)
        monumento.showsFeaturesOf.connect(torre_eiffel)

        # Exception Raised on Illegal Relation
        self.assertRaises(ValueError, torre_eiffel.showsFeaturesOf.connect, uma_entidade_qualquer)

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
        self.assertEqual(test_results[0].labels, {'E70_Thing', 'E77_Persistent_Item', 'E1_CRM_Entity'})
        self.assertEqual(test_results[0].properties, {'name': 'Monument', 'uid': monument.uid})
        self.assertEqual(test_results[1].labels, {'E70_Thing', 'E77_Persistent_Item', 'E1_CRM_Entity'})
        self.assertEqual(test_results[1].properties, {'name': 'Monument2', 'uid': monument2.uid})
        # Results of Fuzzy Search
        self.assertEqual(test_results2[0].labels, {'E70_Thing', 'E77_Persistent_Item', 'E1_CRM_Entity'})
        self.assertEqual(test_results2[0].properties, {'name': 'Monument2', 'uid': monument2.uid})
        # Results of Specific Search
        self.assertEqual(test_results3[0].labels, {'E70_Thing', 'E77_Persistent_Item', 'E1_CRM_Entity'})
        self.assertEqual(test_results3[0].properties, {'name': 'Monument', 'uid': monument.uid})

        # Test of JSON Serialization of search result / Due to the nature of Set inside of labels is always different so labels must be found to be tested
        json_results = test_results[0].encodeJSON()
        start = json_results.find("[") + len("[")
        end = json_results.find("]")
        substring = json_results[start:end]

        self.assertEqual(test_results[0].encodeJSON(),
                         "{\"labels\": [" + substring + "], \"name\": \"Monument\", \"uid\": \"" + monument.uid + "\"}")

    def test_create_graph(self):
        e22 = E22_Human_Made_Object(name="humam_made_object").save()
        are2 = ARE2_Formal_Title(name="Document Title").save()
        string = String(name="string name", stringValue="Registo_de_Baptismo").save()

        e22.has_title.connect(are2)
        are2.has_value.connect(string)

        startDatetime = datetime.datetime(1812, 2, 12)
        endDatetime = datetime.datetime(1812, 2, 13)
        e12 = E12_Production(name="Document Production").save()
        e52 = E52_Time_Span(name="Production time", date=startDatetime).save()
        e41 = E41_Appellation(name="1812-02-12").save()

        node = Interval(name="1812-02-12", startDateValue=startDatetime, endDateValue=endDatetime).save()

        e41.has_value.connect(node)
        e52.is_identified_by.connect(e41)
        e12.has_time_span.connect(e52)
        e22.was_produced_by.connect(e12)


