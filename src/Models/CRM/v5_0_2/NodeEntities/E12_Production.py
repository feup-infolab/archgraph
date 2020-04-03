from neomodel import RelationshipFrom

from src.Models.CRM.v5_0_2.NodeEntities.E11_Modification import \
    E11_Modification
from src.Models.CRM.v5_0_2.NodeProperties.P108_was_produced_by import P108_was_produced_by


class E12_Production(E11_Modification):
    was_produced_by = RelationshipFrom(
        ".E24_Physical_Human_Made_Thing.E24_Physical_Human_Made_Thing", "P108_has_produced_by",
        model=P108_was_produced_by
    )
    pass
