from neomodel import RelationshipFrom, StringProperty, StructuredNode
from src.GCF.decorators.OntologyClass import ontology_class
from src.Models.CRM.v5_0_2.NodeProperties.P15_was_influenced_by import P15_was_influenced_by
from src.Models.CRM.v5_0_2.NodeProperties.P17_was_motivated_by import P17_was_motivated_by


@ontology_class
class E1_CRM_Entity(StructuredNode):
    name = StringProperty(unique_index=True, required=True)
    is_composed_of = RelationshipFrom(
        ".E7_Activity.E7_Activity",
        "P15_was_influenced_by",
        model=P15_was_influenced_by,
    )
    was_motivated_by = RelationshipFrom(
        ".E7_Activity.E7_Activity",
        "P17_was_motivated_by",
        model=P17_was_motivated_by,
    )
