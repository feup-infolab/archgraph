from neomodel import RelationshipTo
from src.Models.CRM.v5_0_2.NodeEntities.E28_Conceptual_Object import \
    E28_Conceptual_Object
from src.Models.CRM.v5_0_2.NodeProperties.P67_refers_to import P67_refers_to
from src.Models.CRM.v5_0_2.NodeProperties.P129_is_about import P129_is_about
from src.Models.CRM.v5_0_2.NodeProperties.P148_has_component import \
    P148_has_component


class E89_Propositional_Object(E28_Conceptual_Object):
    curated = RelationshipTo(
        ".E89_Propositional_Object.E89_Propositional_Object",
        "P148_has_component",
        model=P148_has_component,
    )
    refers_to = RelationshipTo(
        ".E1_CRM_Entity.E1_CRM_Entity", "P67_refers_to", model=P67_refers_to,
    )
    is_about = RelationshipTo(
        ".E1_CRM_Entity.E1_CRM_Entity", "P129_is_about", model=P129_is_about,
    )
