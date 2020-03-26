from neomodel import RelationshipFrom, StringProperty, StructuredNode
from src.GCF.decorators.OntologyClass import ontology_class
from src.Models.CRM.v5_0_2.NodeProperties.P15_was_influenced_by import \
    P15_was_influenced_by
from src.Models.CRM.v5_0_2.NodeProperties.P17_was_motivated_by import \
    P17_was_motivated_by
from src.Models.CRM.v5_0_2.NodeProperties.P39_measured import P39_measured
from src.Models.CRM.v5_0_2.NodeProperties.P41_classified import P41_classified
from src.Models.CRM.v5_0_2.NodeProperties.P62_depicts import P62_depicts
from src.Models.CRM.v5_0_2.NodeProperties.P67_refers_to import P67_refers_to
from src.Models.CRM.v5_0_2.NodeProperties.P70_documents import P70_documents
from src.Models.CRM.v5_0_2.NodeProperties.P71_lists import P71_lists
from src.Models.CRM.v5_0_2.NodeProperties.P129_is_about import P129_is_about
from src.Models.CRM.v5_0_2.NodeProperties.P136_was_based_on import \
    P136_was_based_on
from src.Models.CRM.v5_0_2.NodeProperties.P140_assigned_attribute_to import \
    P140_assigned_attribute_to
from src.Models.CRM.v5_0_2.NodeProperties.P141_assigned import P141_assigned


@ontology_class
class E1_CRM_Entity(StructuredNode):
    name = StringProperty(unique_index=True, required=True)
    is_composed_of = RelationshipFrom(
        ".E7_Activity.E7_Activity", "P15_was_influenced_by", model=P15_was_influenced_by
    )
    was_motivated_by = RelationshipFrom(
        ".E7_Activity.E7_Activity", "P17_was_motivated_by", model=P17_was_motivated_by
    )
    measured = RelationshipFrom(
        ".E16_Measurement.E16_Measurement", "P39_measured", model=P39_measured
    )
    classified = RelationshipFrom(
        ".E17_Type_Assignment.E17_Type_Assignment",
        "P41_classified",
        model=P41_classified,
    )
    depicts = RelationshipFrom(
        ".E24_Physical_Human_Made_Thing.E24_Physical_Human_Made_Thing",
        "P62_depicts",
        model=P62_depicts,
    )
    refers_to = RelationshipFrom(
        ".E89_Propositional_Object.E89_Propositional_Object",
        "P67_refers_to",
        model=P67_refers_to,
    )
    documents = RelationshipFrom(
        ".E31_Document.E31_Document", "P70_documents", model=P70_documents
    )
    lists = RelationshipFrom(
        ".E32_Authority_Document.E32_Authority_Document", "P71_lists", model=P71_lists
    )
    is_about = RelationshipFrom(
        ".E89_Propositional_Object.E89_Propositional_Object",
        "P129_is_about",
        model=P129_is_about,
    )
    was_based_on = RelationshipFrom(
        ".E83_Type_Creation.E83_Type_Creation",
        "P136_was_based_on",
        model=P136_was_based_on,
    )
    assigned_attribute_to = RelationshipFrom(
        ".E13_Attribute_Assignment.E13_Attribute_Assignment",
        "P140_assigned_attribute_to",
        model=P140_assigned_attribute_to,
    )
    assigned = RelationshipFrom(
        ".E13_Attribute_Assignment.E13_Attribute_Assignment",
        "P141_assigned",
        model=P141_assigned,
    )
