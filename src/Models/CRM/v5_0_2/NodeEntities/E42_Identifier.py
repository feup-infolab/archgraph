from neomodel import One, RelationshipFrom, StructuredRel
from src.Models.CRM.v5_0_2.NodeEntities.E41_Appellation import E41_Appellation
from src.Models.CRM.v5_0_2.NodeProperties.P37_assigned import P37_assigned
from src.Models.CRM.v5_0_2.NodeProperties.P38_deassigned import P38_deassigned


class P48_has_preferred_identifier(StructuredRel):
    pass


class E42_Identifier(E41_Appellation):
    has_preferred_identifier = RelationshipFrom(
        "E1_CRM_Entity",
        "P48_has_preferred_identifier",
        cardinality=One,
        model=P48_has_preferred_identifier)
    assigned = RelationshipFrom(
        ".E15_Identifier_Assignment.E15_Identifier_Assignment",
        "P37_assigned",
        model=P37_assigned
    )
    deassigned = RelationshipFrom(
        ".E15_Identifier_Assignment.E15_Identifier_Assignment",
        "P38_deassigned",
        model=P38_deassigned
    )
