from neomodel import RelationshipFrom

from src.Models.CRM.v5_0_2.NodeEntities.E71_Human_Made_Thing import \
    E71_Human_Made_Thing
from src.Models.CRM.v5_0_2.NodeProperties.P94_has_created import P94_has_created


class E28_Conceptual_Object(E71_Human_Made_Thing):
    has_created = RelationshipFrom(
        ".E65_Creation.E65_Creation",
        "P94_has_created",
        model=P94_has_created
    )
