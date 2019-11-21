from neomodel import (config, StructuredNode, StringProperty, IntegerProperty,
                      UniqueIdProperty, RelationshipTo, One)
from NodeProperties.PC0_CRM_Property import PC0_CRM_Property


class PC14_Carried_Out_By(PC0_CRM_Property):
    hasDomain = RelationshipTo('E7_Activity', 'P01_has_domain', cardinality=One)
    hasRange = RelationshipTo('E39_Actor', 'P02_has_range', cardinality=One)
    inTheRoleOf = RelationshipTo('E55_Type','P14.1_in_the_role_of', cardinality=One)
