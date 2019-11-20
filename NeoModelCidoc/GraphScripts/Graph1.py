from neomodel import (config, StructuredNode, StringProperty, IntegerProperty,
                      UniqueIdProperty, RelationshipTo)
from NodeEntities.E56_Language import E56_Language
from NodeEntities.E1_CRM_Entity import E1_CRM_Entity

config.DATABASE_URL = 'bolt://neo4j:password@localhost:7687'

e1 = E1_CRM_Entity(name="test")
e56 = E56_Language(name="language")
e1.hasType.connect(e56)



