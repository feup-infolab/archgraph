from neomodel import RelationshipFrom, StructuredRel
from src.Models.CRM.v5_0_2.NodeEntities.E77_Persistent_Item import E77_Persistent_Item
from src.Models.CRM.v5_0_2.NodeProperties.P105_right_held_by import P105_right_held_by
from src.Models.CRM.v5_0_2.NodeProperties.P107_has_current_or_former_member import P107_has_current_or_former_member
from src.Models.CRM.v5_0_2.NodeProperties.P109_has_current_or_former_curator import P109_has_current_or_former_curator
from src.Models.CRM.v5_0_2.NodeProperties.P143_joined import P143_joined
from src.Models.CRM.v5_0_2.NodeProperties.P145_separated import P145_separated
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
    right_held_by = RelationshipFrom(
        ".E72_Legal_Object.E72_Legal_Object",
        "P105_right_held_by",
        model=P105_right_held_by)
    has_current_or_former_member = RelationshipFrom(
        ".E74_Group.E74_Group",
        "P107_has_current_or_former_member",
        model=P107_has_current_or_former_member)
    has_current_or_former_curator = RelationshipFrom(
        ".E78_Collection.E78_Collection",
        "P109_has_current_or_former_curator",
        model=P109_has_current_or_former_curator)
    joined = RelationshipFrom(
        ".E85_Joining.E85_Joining",
        "P143_joined",
        model=P143_joined
    )
    separated = RelationshipFrom(
        ".E86_Leaving.E86_Leaving",
        "P145_separated_from",
        model=P145_separated
    )


