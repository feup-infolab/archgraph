from neomodel import (
    config,
    StructuredNode,
    StringProperty,
    IntegerProperty,
    UniqueIdProperty,
    RelationshipTo,
    One,
    RelationshipFrom,
)

from src.GCF.decorators.OntologyClass import ontology_class
from ..NodeProperties.PC14_Carried_Out_By import PC14_Carried_Out_By

# @ontology_class
class E1_CRM_Entity(StructuredNode):

    name = StringProperty(unique_index=True, required=True)

    def to_json(self):
        return {self.__class__.__name__: self.__properties__}
