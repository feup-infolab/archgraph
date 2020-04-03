from neomodel import RelationshipTo
from src.Models.CRM.v5_0_2.NodeEntities.E11_Modification import \
    E11_Modification
from src.Models.CRM.v5_0_2.NodeProperties.P108_was_produced_by import \
    P108_was_produced_by
from src.Models.CRM.v5_0_2.NodeProperties.P112_diminished import \
    P112_diminished
from src.Models.CRM.v5_0_2.NodeProperties.P113_removed import P113_removed


class E80_Part_Removal(E11_Modification):
    diminished = RelationshipTo(
        ".E24_Physical_Human_Made_Thing.E24_Physical_Human_Made_Thing",
        "P112_diminished",
        model=P112_diminished,
    )

    removed = RelationshipTo(
        ".E18_Physical_Thing.E18_Physical_Thing", "P113_removed", model=P113_removed
    )
