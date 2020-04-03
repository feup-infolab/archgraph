from neomodel import RelationshipTo
from src.Models.CRM.v5_0_2.NodeEntities.E7_Activity import E7_Activity
from src.Models.CRM.v5_0_2.NodeEntities.E63_Beggining_of_Existence import \
    E63_Beggining_of_Existence
from src.Models.CRM.v5_0_2.NodeProperties.P95_has_formed import P95_has_formed
from src.Models.CRM.v5_0_2.NodeProperties.P151_was_formed_from import \
    P151_was_formed_from


class E66_Formation(E7_Activity, E63_Beggining_of_Existence):
    has_formed = RelationshipTo(
        ".E74_Group.E74_Group", "P95_has_formed", model=P95_has_formed
    )
    was_formed_from = RelationshipTo(
        ".E74_Group.E74_Group", "P151_was_formed_from", model=P151_was_formed_from,
    )
