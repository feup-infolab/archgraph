from neomodel import RelationshipFrom, StructuredRel
from src.Models.CRM.v5_0_2.NodeEntities.E77_Persistent_Item import \
    E77_Persistent_Item
from src.Models.CRM.v5_0_2.NodeProperties.P11_had_participat import P11_had_participant
from src.Models.CRM.v5_0_2.NodeProperties.P14_carried_out_by import P14_carried_out_by
from src.Models.CRM.v5_0_2.NodeProperties.P22_transferred_title_to import P22_transferred_title_to
from src.Models.CRM.v5_0_2.NodeProperties.P23_transferred_title_from import P23_transferred_title_from
from src.Models.CRM.v5_0_2.NodeProperties.P29_custody_received_by import P29_custody_received_by


class E39_Actor(E77_Persistent_Item):
    had_participant = RelationshipFrom(
        ".E5_Event.E5_Event", "P11_had_participant", model=P11_had_participant
    )
    carried_out_by = RelationshipFrom(
        ".E7_Activity.E7_Activity", "P14_carried_out_by", model=P14_carried_out_by
    )
    transferred_title_to = RelationshipFrom(
        ".E8_Acquisition.E8_Acquisition",
        "P22_transferred_title_to",
        model=P22_transferred_title_to)
    transferred_title_from = RelationshipFrom(
        ".E8_Acquisition.E8_Acquisition",
        "P23_transferred_title_from",
        model=P23_transferred_title_from)
    custody_received_by = RelationshipFrom(
        ".E10_Transfer_of_Custody.E10_Transfer_of_Custody",
        "P29_custody_received_by",
        model=P29_custody_received_by)
