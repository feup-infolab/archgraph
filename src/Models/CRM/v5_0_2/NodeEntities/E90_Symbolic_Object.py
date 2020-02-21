from neomodel import (IntegerProperty, RelationshipTo, StringProperty,
                      StructuredNode, UniqueIdProperty, config)

from src.Models.CRM.v5_0_2.NodeEntities.E28_Conceptual_Object import \
    E28_Conceptual_Object
from src.Models.CRM.v5_0_2.NodeEntities.E72_Legal_Object import \
    E72_Legal_Object


class E90_Symbolic_Object(E72_Legal_Object, E28_Conceptual_Object):
    pass
