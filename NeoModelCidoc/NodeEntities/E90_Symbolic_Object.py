from neomodel import (config, StructuredNode, StringProperty, IntegerProperty,
                      UniqueIdProperty, RelationshipTo)
from NodeEntities.E72_Legal_Object import E72_Legal_Object
from NodeEntities.E28_Conceptual_Object import E28_Conceptual_Object


class E90_Symbolic_Object(StructuredNode, E72_Legal_Object, E28_Conceptual_Object):
    pass
