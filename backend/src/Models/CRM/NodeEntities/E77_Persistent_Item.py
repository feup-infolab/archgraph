from neomodel import (config, StructuredNode, StringProperty, IntegerProperty,
                      UniqueIdProperty, RelationshipTo, RelationshipFrom)
from NodeEntities.E1_CRM_Entity import E1_CRM_Entity
from NodeEntities.StructuredRelCl import StructuredRelCl


class P12_occurred_in_the_presence_of(StructuredRelCl):
    pass


class E77_Persistent_Item(E1_CRM_Entity):
    occurred_in_the_presence_of = RelationshipFrom('E5_Event', 'P12_occurred_in_the_presence_of', model=P12_occurred_in_the_presence_of)

