from neomodel import (config, StructuredNode, StringProperty, IntegerProperty,
                      UniqueIdProperty, RelationshipTo, One, RelationshipFrom)
from NodeEntities.E41_Appellation import E41_Appellation

from NodeEntities.StructuredRelCl import StructuredRelCl


class P48_has_preferred_identifier(StructuredRelCl):
    pass


class E42_Identifier(E41_Appellation):
    has_preferred_identifier = RelationshipFrom('E1_CRM_Entity', 'P48_has_preferred_identifier', cardinality=One,
                                     model=P48_has_preferred_identifier)


