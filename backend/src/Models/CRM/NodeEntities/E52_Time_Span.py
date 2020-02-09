from neomodel import (config, StructuredNode, StringProperty, IntegerProperty,
                      UniqueIdProperty, RelationshipTo, DateTimeProperty)
from NodeEntities.E1_CRM_Entity import E1_CRM_Entity


class E52_Time_Span(E1_CRM_Entity):
    date = DateTimeProperty(unique_index=True, required=True)
