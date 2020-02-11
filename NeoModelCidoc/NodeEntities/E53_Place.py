from neomodel import (config, StructuredNode, StringProperty, IntegerProperty,
                      UniqueIdProperty, RelationshipTo, DateTimeProperty, RelationshipFrom)
from NodeEntities.E1_CRM_Entity import E1_CRM_Entity
from NodeEntities.E18_Physical_Thing import E18_Physical_Thing
from NodeEntities.StructuredRelCl import StructuredRelCl


class P156_occupies(StructuredRelCl):
    pass

class P7_took_place_at(StructuredRelCl):
    pass


class E53_Place(E1_CRM_Entity):
    occupies = RelationshipFrom(E18_Physical_Thing, 'P156_occupies', model=P156_occupies)
    took_place_at = RelationshipFrom(E18_Physical_Thing, 'P7_took_place_at', model=P7_took_place_at)
