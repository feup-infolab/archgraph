from neomodel import (config, StructuredNode, StringProperty, IntegerProperty,
                      UniqueIdProperty, RelationshipTo, DateTimeProperty, RelationshipFrom)
from NodeEntities.E1_CRM_Entity import E1_CRM_Entity
from NodeEntities.E18_Physical_Thing import E18_Physical_Thing
from NodeProperties.StructuredRelCl import StructuredRelCl


class P156_occupies(StructuredRelCl):
    pass


class E53_Place(E1_CRM_Entity):
    occupies = RelationshipFrom(E18_Physical_Thing, 'P156_occupies', model=P156_occupies)
