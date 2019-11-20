from neomodel import (config, StructuredNode, StringProperty, IntegerProperty,
                      UniqueIdProperty, RelationshipTo)

from NodeEntities.E55_Type import E55_Type


class E1_CRM_Entity(StructuredNode):
    name = StringProperty(unique_index=True, required=True)
    hasType = RelationshipTo(E55_Type, 'P2_has_type')
