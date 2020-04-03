from neomodel import RelationshipTo
from src.Models.CRM.v5_0_2.NodeEntities.E4_Period import E4_Period
from src.Models.CRM.v5_0_2.NodeProperties.P11_had_participat import \
    P11_had_participant


class E5_Event(E4_Period):
    had_participant = RelationshipTo(
        ".E39_Actor.E39_Actor", "P11_had_participant", model=P11_had_participant
    )
