from neomodel import (config, StructuredNode, StringProperty, IntegerProperty,
                      UniqueIdProperty, RelationshipTo)
from NodeEntities.E18_Physical_Thing import E18_Physical_Thing
from NodeEntities.E71_Man_Made_Thing import E71_Man_Made_Thing


class E24_Physical_Man_Made_Thing(StructuredNode, E18_Physical_Thing, E71_Man_Made_Thing):
    pass
