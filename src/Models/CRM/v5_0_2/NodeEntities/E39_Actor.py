from neomodel import RelationshipFrom, StructuredRel
from src.Models.CRM.v5_0_2.NodeEntities.E77_Persistent_Item import \
    E77_Persistent_Item
from src.Models.CRM.v5_0_2.NodeProperties.P11_had_participat import P11_had_participant
from src.Models.CRM.v5_0_2.NodeProperties.P14_carried_out_by import P14_carried_out_by


class E39_Actor(E77_Persistent_Item):
    had_participant = RelationshipFrom(
        ".E5_Event.E5_Event", "P11_had_participant", model=P11_had_participant
    )
    carried_out_by = RelationshipFrom(
        ".E7_Activity.E7_Activity", "P14_carried_out_by", model=P14_carried_out_by
    )
