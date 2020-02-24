from neomodel import RelationshipFrom

from src.Models.CRM.v5_0_2.NodeEntities.E18_Physical_Thing import \
    E18_Physical_Thing
from src.Models.CRM.v5_0_2.NodeEntities.E71_Human_Made_Thing import \
    E71_Human_Made_Thing
from src.Models.CRM.v5_0_2.NodeProperties.P108_has_produced import P108_has_produced
from src.Models.CRM.v5_0_2.NodeProperties.P110_augmented import P110_augmented


class E24_Physical_Human_Made_Thing(E18_Physical_Thing, E71_Human_Made_Thing):
    has_produced = RelationshipFrom(
        ".E12_Production.E12_Production",
        "P108_has_produced",
        model=P108_has_produced
    )
    augmented = RelationshipFrom(
        ".E79_Part_Addition.E79_Part_Addition",
        "P110_augmented",
        model=P110_augmented
    )
