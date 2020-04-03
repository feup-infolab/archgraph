from neomodel import RelationshipTo
from src.Models.CRM.v5_0_2.NodeEntities.E11_Modification import \
    E11_Modification
from src.Models.CRM.v5_0_2.NodeProperties.P110_augmented import P110_augmented
from src.Models.CRM.v5_0_2.NodeProperties.P111_added import P111_added


class E79_Part_Addition(E11_Modification):
    augmented = RelationshipTo(
        ".E24_Physical_Human_Made_Thing.E24_Physical_Human_Made_Thing",
        "P110_augmented",
        model=P110_augmented,
    )
    added = RelationshipTo(
        ".E18_Physical_Thing.E18_Physical_Thing", "P111_added", model=P111_added
    )
