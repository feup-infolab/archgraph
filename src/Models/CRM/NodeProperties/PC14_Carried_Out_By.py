from neomodel import (config, StructuredNode, StringProperty, IntegerProperty,
                      UniqueIdProperty, RelationshipTo, One)
from src.Models.CRM.NodeProperties.PC0_CRM_Property import PC0_CRM_Property, P01_has_domain, P02_has_range
from NodeEntities.E7_Activity import E7_Activity
from NodeEntities.E39_Actor import E39_Actor
from NodeEntities.E55_Type import E55_Type
from src.Models.CRM.NodeProperties.StructuredRelCl import StructuredRelCl


class P14_1_in_the_role_of(StructuredRelCl):
    pass


class PC14_Carried_Out_By(PC0_CRM_Property):
    hasDomain = RelationshipTo(E7_Activity, 'P01_has_domain', cardinality=One, model=P01_has_domain)
    hasRange = RelationshipTo(E39_Actor, 'P02_has_range', cardinality=One, model=P02_has_range)
    inTheRoleOf = RelationshipTo(E55_Type, 'P14.1_in_the_role_of', cardinality=One, model=P14_1_in_the_role_of)
