from neomodel import RelationshipFrom, StructuredRel
from src.Models.CRM.v5_0_2.NodeEntities.E77_Persistent_Item import E77_Persistent_Item
from src.Models.CRM.v5_0_2.NodeProperties.P51_has_former_or_current_owner import P51_has_former_or_current_owner
from src.Models.CRM.v5_0_2.NodeProperties.P50_has_current_keeper import P50_has_current_keeper
from src.Models.CRM.v5_0_2.NodeProperties.P11_had_participat import P11_had_participant
from src.Models.CRM.v5_0_2.NodeProperties.P14_carried_out_by import P14_carried_out_by
from src.Models.CRM.v5_0_2.NodeProperties.P22_transferred_title_to import P22_transferred_title_to
from src.Models.CRM.v5_0_2.NodeProperties.P23_transferred_title_from import P23_transferred_title_from
from src.Models.CRM.v5_0_2.NodeProperties.P29_custody_received_by import P29_custody_received_by
from src.Models.CRM.v5_0_2.NodeProperties.P49_has_former_or_current_keeper import P49_has_former_or_current_keeper
from src.Models.CRM.v5_0_2.NodeProperties.P52_has_current_owner import P52_has_current_owner


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
    has_former_or_current_keeper = RelationshipFrom(
        ".E18_Physical_Thing.E18_Physical_Thing",
        "P49_has_former_or_current_keeper",
        model=P49_has_former_or_current_keeper)
    has_current_keeper = RelationshipFrom(
        ".E18_Physical_Thing.E18_Physical_Thing",
        "P50_has_current_keeper",
        model=P50_has_current_keeper)
    has_former_or_current_owner = RelationshipFrom(
        ".E18_Physical_Thing.E18_Physical_Thing",
        "P51_has_former_or_current_owner",
        model=P51_has_former_or_current_owner)
    has_current_owner = RelationshipFrom(
        ".E18_Physical_Thing.E18_Physical_Thing",
        "P52_has_current_owner",
        model=P52_has_current_owner)

