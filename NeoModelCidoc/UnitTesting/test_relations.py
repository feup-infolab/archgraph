import unittest

from NodeEntities.E55_Type import E55_Type, E1_CRM_Entity
from neomodel import (config, StructuredNode, StringProperty, IntegerProperty,
                      UniqueIdProperty, RelationshipTo)

config.DATABASE_URL = 'bolt://neo4j:password@localhost:7687'


class TestRelatioships(unittest.TestCase):
    def test_basic_relationship(self):
        e1 = E1_CRM_Entity(name="test").save()
        e55 = E55_Type(name="test2").save()
        e55.hasType.connect(e1)
        all_types = e55.hasType.filter(name="test2")

        for p in all_types:
            self.assertAlmostEqual(p.id, e1.id)
