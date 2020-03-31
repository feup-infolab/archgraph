from neomodel import One, RelationshipFrom
from src.Models.CRM.v5_0_2.NodeEntities.E90_Symbolic_Object import \
    E90_Symbolic_Object
from src.Models.CRM.v5_0_2.NodeProperties.P1_is_identified_by import \
    P1_is_identified_by
from src.Models.CRM.v5_0_2.NodeProperties.P139_has_alternative_form import \
    P139_has_alternative_form


class E41_Appellation(E90_Symbolic_Object):
    is_identified_by = RelationshipFrom(
        ".E1_CRM_Entity.E1_CRM_Entity",
        "P1_is_identified_by",
        cardinality=One,
        model=P1_is_identified_by,
    )
    has_alternative_form = RelationshipFrom(
        ".E1_CRM_Entity.E1_CRM_Entity",
        "P139_has_alternative_form",
        model=P139_has_alternative_form,
    )
