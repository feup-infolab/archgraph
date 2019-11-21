from neomodel import (config, StructuredNode, StringProperty, IntegerProperty,
                      UniqueIdProperty, RelationshipTo, One)


class E1_CRM_Entity(StructuredNode):
    name = StringProperty(unique_index=True, required=True)
    testCardinality = RelationshipTo('E1_CRM_Entity', 'Cardinality_Relationship', cardinality=One)

