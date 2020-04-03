from neomodel import RelationshipTo
from src.Models.CRM.v5_0_2.NodeEntities.E28_Conceptual_Object import \
    E28_Conceptual_Object

from ..NodeProperties.P127_has_broader_term import P127_has_broader_term
from ..NodeProperties.P150_defines_typical_parts_of import \
    P150_defines_typical_parts_of


class E55_Type(E28_Conceptual_Object):
    has_broader_term = RelationshipTo(
        ".E55_Type.E55_Type", "P127_has_broader_term", model=P127_has_broader_term
    )
    defines_typical_parts_of = RelationshipTo(
        ".E55_Type.E55_Type",
        "P150_defines_typical_parts_of",
        model=P150_defines_typical_parts_of,
    )
