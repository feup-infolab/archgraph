from neomodel import (config, StructuredNode, StringProperty, IntegerProperty,
                      UniqueIdProperty, RelationshipTo)


class E1_CRM_Entity(StructuredNode):
    name = StringProperty(unique_index=True, required=True)

