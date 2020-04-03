from neomodel import RelationshipTo
from src.Models.CRM.v5_0_2.NodeEntities.E7_Activity import E7_Activity
from src.Models.CRM.v5_0_2.NodeProperties.P143_joined import P143_joined
from src.Models.CRM.v5_0_2.NodeProperties.P144_joined_with import \
    P144_joined_with


class E85_Joining(E7_Activity):
    joined = RelationshipTo(".E39_Actor.E39_Actor", "P143_joined", model=P143_joined)
    joined_with = RelationshipTo(
        ".E74_Group.E74_Group", "P144_joined_with", model=P144_joined_with
    )
