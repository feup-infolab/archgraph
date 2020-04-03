from neomodel import RelationshipTo

from src.Models.CRM.v5_0_2.NodeEntities.E5_Event import E5_Event
from src.Models.CRM.v5_0_2.NodeProperties.P93_took_out_of_existence import P93_took_out_of_existence


class E64_End_of_Existence(E5_Event):
    took_out_of_existence = RelationshipTo(
        ".E77_Persistent_Item.E77_Persistent_Item",
        "P93_took_out_of_existence",
        model=P93_took_out_of_existence,
    )
