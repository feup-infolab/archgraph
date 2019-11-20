from neomodel import (config, StructuredNode, StringProperty, IntegerProperty,
                      UniqueIdProperty, RelationshipTo, RelationshipFrom)
from NodeEntities.E28_Conceptual_Object import E28_Conceptual_Object
from NodeEntities.E1_CRM_Entity import E1_CRM_Entity


class E55_Type(E28_Conceptual_Object):
    hasType = RelationshipFrom(E1_CRM_Entity, 'P2_has_type')


