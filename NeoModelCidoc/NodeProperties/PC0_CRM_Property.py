from neomodel import (config, StructuredNode, StringProperty, IntegerProperty,
                      UniqueIdProperty, RelationshipTo, One)
from NodeEntities.E1_CRM_Entity import E1_CRM_Entity


class PC0_CRM_Property(E1_CRM_Entity):
    hasDomain = RelationshipTo(E1_CRM_Entity, 'P01_has_domain', cardinality=One)
    hasRange = RelationshipTo(E1_CRM_Entity, 'P02_has_range', cardinality=One)

