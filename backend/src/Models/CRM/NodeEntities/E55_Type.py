from neomodel import (config, StructuredNode, StringProperty, IntegerProperty,
                      UniqueIdProperty, RelationshipTo, RelationshipFrom)
from NodeEntities.E28_Conceptual_Object import E28_Conceptual_Object
from NodeEntities.E1_CRM_Entity import E1_CRM_Entity
from NodeEntities.StructuredRelCl import StructuredRelCl


class P2_has_type(StructuredRelCl):
    pass


class P137_exemplifies(StructuredRelCl):
    pass


class E55_Type(E28_Conceptual_Object):
    hasType = RelationshipFrom(E1_CRM_Entity, 'P2_has_type', model=P2_has_type)
    exemplifies = RelationshipFrom(E1_CRM_Entity, 'P137_exemplifies', model=P137_exemplifies)