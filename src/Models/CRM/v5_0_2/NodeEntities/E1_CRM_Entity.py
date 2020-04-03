from neomodel import (One, RelationshipFrom, RelationshipTo, StringProperty,
                      StructuredNode, UniqueIdProperty, db)
from src.GCF.decorators.OntologyClass import ontology_class
from src.Models.CRM.v5_0_2.NodeProperties.has_value import has_value
from src.Models.CRM.v5_0_2.NodeProperties.P1_is_identified_by import \
    P1_is_identified_by
from src.Models.CRM.v5_0_2.NodeProperties.P2_has_type import P2_has_type
from src.Models.CRM.v5_0_2.NodeProperties.P48_has_preferred_identifier import \
    P48_has_preferred_identifier
from src.Models.CRM.v5_0_2.NodeProperties.P137_exemplifies import \
    P137_exemplifies
from src.Models.CRM.v5_0_2.NodeProperties.P138_represents import \
    P138_represents
from src.Models.CRM.v5_0_2.NodeProperties.P139_has_alternative_form import \
    P139_has_alternative_form
from src.Models.DataObject.v0_0_2.SuperClass import SuperClass


@ontology_class
class E1_CRM_Entity(StructuredNode, SuperClass):
    name = StringProperty(unique_index=True, required=True)
    uid = UniqueIdProperty()
    # def full_text_ind(self):
    #    result_index = self.cypher(
    #        "CALL db.index.fulltext.createNodeIndex('node_entity',['" + self.__class__.__name__ + "'],['name'])")
    represents = RelationshipTo(
        ".E36_Visual_Item.E36_Visual_Item", "P138_represents", model=P138_represents
    )
    hasType = RelationshipTo(".E55_Type.E55_Type", "P2_has_type", model=P2_has_type)
    exemplifies = RelationshipTo(
        ".E55_Type.E55_Type", "P137_exemplifies", model=P137_exemplifies
    )
    has_preferred_identifier = RelationshipTo(
        ".E42_Identifier.E42_Identifier",
        "P48_has_preferred_identifier",
        cardinality=One,
        model=P48_has_preferred_identifier,
    )
    has_alternative_form = RelationshipTo(
        ".E41_Appellation.E41_Appellation",
        "P139_has_alternative_form",
        model=P139_has_alternative_form,
    )
    is_identified_by = RelationshipTo(
        ".E41_Appellation.E41_Appellation",
        "P1_is_identified_by",
        cardinality=One,
        model=P1_is_identified_by,
    )
    has_value = RelationshipTo(
        "src.Models.DataObject.v0_0_2.DataObject.DataObject",
        "has_value",
        model=has_value,
    )
