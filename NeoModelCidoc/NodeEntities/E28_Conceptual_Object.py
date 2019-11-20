from abc import ABC

from neomodel import (config, StructuredNode, StringProperty, IntegerProperty,
                      UniqueIdProperty, RelationshipTo)
from NodeEntities.E71_Man_Made_Thing import E71_Man_Made_Thing


class E28_Conceptual_Object(StructuredNode, E71_Man_Made_Thing):
    pass


