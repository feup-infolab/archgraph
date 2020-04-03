from neomodel import RelationshipTo

from src.Models.CRM.v5_0_2.NodeEntities.E5_Event import E5_Event
from src.Models.CRM.v5_0_2.NodeProperties.P92_brought_into_existence import P92_brought_into_existence


class E63_Beggining_of_Existence(E5_Event):
    brought_into_existence = RelationshipTo(
        ".E77_Persistent_Item.E77_Persistent_Item",
        "P92_brought_into_existence",
        model=P92_brought_into_existence,
    )
