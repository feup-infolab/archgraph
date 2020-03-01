import datetime
import unittest

from src.Models.DataObject.v0_0_2.String import String

from neomodel import (config, OUTGOING, Traversal, DeflateError,
                      AttemptedCardinalityViolation)
import json

config.DATABASE_URL = 'bolt://neo4j:password@localhost:7687'
date = datetime.datetime.now().strftime("%H:%M:%S")

string = String(name=date, stringValue="String_Value").save()


class TestString(unittest.TestCase):
    def test_create_update_string_Node(self):
        returned_string = String.nodes.get(name=date)
        new_name = "new_Name"
        returned_string.stringValue = new_name
        returned_string.save()
        change_returned_string = String.nodes.get(name=date)
        self.assertAlmostEqual(string.id, returned_string.id)
        self.assertEqual(change_returned_string.stringValue, new_name)
        self.assertAlmostEqual(string.id, change_returned_string.id)
