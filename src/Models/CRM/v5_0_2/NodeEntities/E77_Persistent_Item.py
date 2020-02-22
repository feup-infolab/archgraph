from neomodel import RelationshipFrom, StructuredRel
from src.Models.CRM.v5_0_2.NodeEntities.E1_CRM_Entity import E1_CRM_Entity

from ..NodeEntities.E5_Event import E5_Event
from ..NodeProperties.P12_occurred_in_the_presence_of import P12_occurred_in_the_presence_of


class E77_Persistent_Item(E1_CRM_Entity):
    occurred_in_the_presence_of = RelationshipFrom(
        E5_Event,
        "P12_occurred_in_the_presence_of",
        model=P12_occurred_in_the_presence_of,
    )
