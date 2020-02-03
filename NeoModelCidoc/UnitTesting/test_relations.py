import datetime
import unittest

from NodeEntities.E35_Title import E35_Title
from NodeEntities.E53_Place import E53_Place
from NodeEntities.E70_Thing import E70_Thing
from NodeEntities.E55_Type import E55_Type, E1_CRM_Entity
from NodeEntities.E18_Physical_Thing import E18_Physical_Thing
from NodeEntities.E24_Physical_Man_Made_Thing import E24_Physical_Man_Made_Thing
from NodeEntities.E52_Time_Span import E52_Time_Span
from NodeEntities.E72_Legal_Object import E72_Legal_Object
from NodeEntities.E39_Actor import E39_Actor
from NodeProperties.PC14_Carried_Out_By import PC14_Carried_Out_By
from NodeEntities.E7_Activity import E7_Activity
from NodeEntities.E21_Person import E21_Person
from neomodel import (config, StructuredNode, StringProperty, IntegerProperty,
                      UniqueIdProperty, RelationshipTo, OUTGOING, Traversal, DeflateError,
                      AttemptedCardinalityViolation)
import json

from utils.JsonEncoder import MyEncoder, json_merge

config.DATABASE_URL = 'bolt://neo4j:password@localhost:7687'
e1 = E1_CRM_Entity(name="test").save()
e1_2 = E1_CRM_Entity(name="test").save()
e55 = E55_Type(name="test2").save()
e55.hasType.connect(e1_2)
e55_2 = E55_Type(name="test3").save()
e18 = E18_Physical_Thing(name="e18").save()
e18_2 = E18_Physical_Thing(name="e18_2").save()
e24 = E24_Physical_Man_Made_Thing(name="e24").save()


class TestNeoModel(unittest.TestCase):
    def test_basic_relationship(self):
        # Tests creation of basic relationships
        # Creates 2 P2_Has_Type Relationships that connect A E1 instance to a E55 and that E55 to another
        e55.hasType.connect(e1)
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
        self.assertRaises(ValueError, e18.isComposedOf.connect, e1)

    def test_diamond_problem(self):
        # Tests if E24 that inherits showsFeaturesOf from both it's superclasses (P130, that E70 has from which E71
        # and and E18 inherit)
        e24.showsFeaturesOf.connect(e18)
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
        e1_2 = E1_CRM_Entity(name="cardTest").save()
        e24_2 = E24_Physical_Man_Made_Thing(name="test4").save()
        e24_3 = E24_Physical_Man_Made_Thing(name="test5").save()
        # Creation of first relationship, shouldn't break
        e1_2.testCardinality.connect(e24_2)
        # Creation of second relationship, should raise exception
        self.assertRaises(AttemptedCardinalityViolation, e1_2.testCardinality.connect, e24_3)

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
        pc14.inTheRoleOf.connect(e55)
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
        e55_3.hasType.connect(e21)
        # Obtaining Json
        json_a = json.dumps(e21.to_json())
        json_b = json.dumps(e55_3.to_json())
        json_c = json.dumps(e55_3.hasType.relationship(e21).to_json())
        # Merge of json documents
        json_d = json_merge(json_merge(json_a, json_b), json_c)
        # Printing the json for easy verification
        print(json_a)
        print(json_b)
        print(json_c)
        print(json_d)
        # Verification
        self.assertEqual(json_a, "{\"E21_Person\": {\"name\": \"Roberto\", \"id\": " + str(e21.id) + "}}")
        self.assertEqual(json_b, "{\"E55_Type\": {\"name\": \"Bibliotecario\", \"id\": " + str(e55_3.id) + "}}")
        self.assertEqual(json_c, "{\"P2_has_type\": {\"id\": " + str(e55_3.hasType.relationship(e21).id) + ", "
                                                                                                           "\"start_node\": {\"name\": \"Roberto\", \"id\": "
                         + str(e21.id) + "}, \"end_node\": {\"name\": \"Bibliotecario\", \"id\": " + str(e55_3.id)
                         + "}}}")
        self.assertEqual(json_d, "{\"E21_Person\": {\"name\": \"Roberto\", \"id\": " + str(e21.id) +
                         "},\"E55_Type\": {\"name\": \"Bibliotecario\", \"id\": " + str(e55_3.id) + "},\"P2_has_type\": "
                                                                                                 "{\"id\": " + str(
            e55_3.hasType.relationship(e21).id) + ", \"start_node\": {\"name\": \"Roberto\", \"id\": " + str(
            e21.id) + "}, \"end_node\": {\"name\": \"Bibliotecario\", \"id\": " + str(e55_3.id) + "}}}")

    def test_case(self):
        # Define nodes to use
        e24_2 = E24_Physical_Man_Made_Thing(name="Monumento").save()
        e35 = E35_Title(name="Torre Eiffel").save()
        e53 = E53_Place(name="Paris").save()
        e70 = E70_Thing(name="Torre").save()
        e1_7 = E1_CRM_Entity(name="E1 de Teste").save()

        # Definition of Relations
        e24_2.occupies.connect(e53)
        e24_2.has_title.connect(e35)
        e24_2.showsFeaturesOf.connect(e70)

        # Exception Raised on Illegal Relation
        self.assertRaises(ValueError, e24_2.showsFeaturesOf.connect, e1_7)

