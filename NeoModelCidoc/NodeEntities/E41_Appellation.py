from neomodel import (config, StructuredNode, StringProperty, IntegerProperty,
                      UniqueIdProperty, RelationshipTo, RelationshipFrom)

from NodeEntities.E1_CRM_Entity import E1_CRM_Entity
from NodeEntities.E90_Symbolic_Object import E90_Symbolic_Object

from NodeProperties.StructuredRelCl import StructuredRelCl


class P1_is_identified_by(StructuredRelCl):
    pass


class E41_Appellation(E90_Symbolic_Object):
    isIdentifiedBy = RelationshipFrom(E1_CRM_Entity, 'P1_is_identified_by', model=P1_is_identified_by)
