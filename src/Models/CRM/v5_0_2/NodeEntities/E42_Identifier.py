from neomodel import One, RelationshipFrom, StructuredRel

from src.Models.CRM.v5_0_2.NodeEntities.E41_Appellation import E41_Appellation


class P48_has_preferred_identifier(StructuredRel):
    pass


class E42_Identifier(E41_Appellation):
    has_preferred_identifier = RelationshipFrom(
        "E1_CRM_Entity",
        "P48_has_preferred_identifier",
        cardinality=One,
        model=P48_has_preferred_identifier,
    )
