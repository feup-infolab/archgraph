from neomodel import (config, StructuredNode, StringProperty, IntegerProperty,
                      UniqueIdProperty, RelationshipTo, RelationshipFrom)

from NodeEntities.E1_CRM_Entity import E1_CRM_Entity
from NodeEntities.E41_Appellation import E41_Appellation

from NodeProperties.StructuredRelCl import StructuredRelCl


class P48_has_preferred_identifier(StructuredRelCl):
    pass


class E42_Identifier(E41_Appellation):
    hasPreferredIdentifier = RelationshipFrom(E1_CRM_Entity, 'P48_has_preferred_identifier', model=P48_has_preferred_identifier)
