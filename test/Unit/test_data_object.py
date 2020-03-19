import datetime
import unittest
from src.Models.DataObject.v0_0_2.Approximate import Approximate
from src.Models.DataObject.v0_0_2.PersonName import PersonName
from src.Models.DataObject.v0_0_2.RegexString import RegexString
from src.Models.DataObject.v0_0_2.String import String
from neomodel import (config)
from src.GCF.utils.db import clean_database
config.DATABASE_URL = 'bolt://neo4j:password@localhost:7687'
clean_database()


class TestString(unittest.TestCase):
    def test_create_update_string_Node(self):
        name = "stringName"
        node = String(name=name, stringValue="String_Value").save()
        print(node.getSchema())
        print(node.toJSON())
        returned_node = String.nodes.get(name=name)
        new_string_value = "new_Name"
        returned_node.stringValue = new_string_value
        returned_node.save()
        change_returned_string = String.nodes.get(name=name)
        self.assertAlmostEqual(node.id, returned_node.id)
        self.assertEqual(change_returned_string.stringValue, new_string_value)
        self.assertAlmostEqual(node.id, change_returned_string.id)

    def test_create_update_regexString_Node(self):
        name = "RegexStringName"
        string_value= "stringValue"
        node = RegexString(expression="r'dw'", name=name, stringValue=string_value).save()
        print(node.getSchema())
        print(node.toJSON())
        returned_node = RegexString.nodes.get(name=name)
        new_string_value = "new_Name"
        returned_node.stringValue = new_string_value
        returned_node.save()
        change_returned_regex = RegexString.nodes.get(name=name)
        self.assertAlmostEqual(node.id, returned_node.id)
        self.assertEqual(change_returned_regex.stringValue, new_string_value)
        self.assertAlmostEqual(node.id, change_returned_regex.id)

    def test_create_update_approximate_Node(self):
        name = "approximateName"
        datetime_object = datetime.datetime(2018, 12, 12)
        node = Approximate(name=name, approximateDateValue=datetime_object).save()
        print(node.getSchema())
        print(node.toJSON())
        returned_node = Approximate.nodes.get(name=name)
        new_approximate_date_value = datetime.datetime.now()
        returned_node.approximateDateValue = new_approximate_date_value
        returned_node.save()
        change_returned_approximate = Approximate.nodes.get(name=name)
        self.assertAlmostEqual(node.id, returned_node.id)
        returned_date = change_returned_approximate.approximateDateValue
        new_date = new_approximate_date_value
        self.assertEqual(returned_date.strftime("%Y-%m-%d"), new_date.strftime("%Y-%m-%d"))
        self.assertAlmostEqual(node.id, change_returned_approximate.id)

    def test_create_update_person_Node(self):
        name = "personName"
        person_name = "person_node_name"
        string_value = "stringValue"
        node = PersonName(person_name=person_name, name=name, stringValue=string_value).save()
        print(node.getSchema())
        print(node.toJSON())
        returned_node = PersonName.nodes.get(name=name)
        person_new_name = "person_node__new_name"
        returned_node.person_name = person_new_name
        returned_node.save()
        change_returned_person = PersonName.nodes.get(name=name)
        self.assertAlmostEqual(node.id, returned_node.id)
        self.assertEqual(change_returned_person.person_name, person_new_name)
        self.assertAlmostEqual(node.id, change_returned_person.id)
