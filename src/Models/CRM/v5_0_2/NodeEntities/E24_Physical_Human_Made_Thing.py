from neomodel import RelationshipTo
from src.Models.CRM.v5_0_2.NodeEntities.E18_Physical_Thing import \
    E18_Physical_Thing
from src.Models.CRM.v5_0_2.NodeEntities.E71_Human_Made_Thing import \
    E71_Human_Made_Thing
from src.Models.CRM.v5_0_2.NodeProperties.P62_depicts import P62_depicts
from src.Models.CRM.v5_0_2.NodeProperties.P65_shows_visual_item import \
    P65_shows_visual_item
from src.Models.CRM.v5_0_2.NodeProperties.P108_was_produced_by import \
    P108_was_produced_by


class E24_Physical_Human_Made_Thing(E18_Physical_Thing, E71_Human_Made_Thing):
    depicts = RelationshipTo(
        ".E1_CRM_Entity.E1_CRM_Entity", "P62_depicts", model=P62_depicts,
    )
    was_produced_by = RelationshipTo(
        ".E12_Production.E12_Production",
        "P108_has_produced_by",
        model=P108_was_produced_by,
    )
