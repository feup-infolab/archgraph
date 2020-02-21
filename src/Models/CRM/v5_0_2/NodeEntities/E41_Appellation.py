from neomodel import (One, RelationshipFrom, StructuredRel)

from src.Models.CRM.v5_0_2.NodeEntities.E90_Symbolic_Object import \
    E90_Symbolic_Object


class P1_is_identified_by(StructuredRel):
    pass


class E41_Appellation(E90_Symbolic_Object):
    is_identified_by = RelationshipFrom(
        "E1_CRM_Entity",
        "P1_is_identified_by",
        cardinality=One,
        model=P1_is_identified_by,
    )
