from neomodel import (IntegerProperty, One, RelationshipFrom, RelationshipTo,
                      StringProperty, StructuredNode, UniqueIdProperty, config)

from src.GCF.decorators.OntologyClass import ontology_class

from ..NodeProperties.P2_has_type import P2_has_type


@ontology_class
class E1_CRM_Entity(StructuredNode):

    hasType = RelationshipFrom(
        ".E1_CRM_Entity.E1_CRM_Entity", "P2_has_type", model=P2_has_type
    )

    name = StringProperty(unique_index=True, required=True)
