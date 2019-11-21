from neomodel import (config, StructuredNode, StringProperty, IntegerProperty,
                      UniqueIdProperty, RelationshipTo, RelationshipFrom)
from NodeEntities.E72_Legal_Object import E72_Legal_Object


class E18_Physical_Thing(E72_Legal_Object):
    isComposedOf = RelationshipFrom('E18_Physical_Thing', 'P46_is_composed_of')
