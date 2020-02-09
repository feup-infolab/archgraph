from neomodel import (config, StructuredNode, StringProperty, IntegerProperty,
                      UniqueIdProperty, RelationshipTo)

from NodeEntities.E89_Propositional_Object import E89_Propositional_Object
from NodeEntities.E90_Symbolic_Object import E90_Symbolic_Object


class E73_Information_Object(E89_Propositional_Object, E90_Symbolic_Object):
    pass
