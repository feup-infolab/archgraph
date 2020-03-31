from neomodel import RelationshipFrom
from src.Models.CRM.v5_0_2.NodeEntities.E1_CRM_Entity import E1_CRM_Entity

from ..NodeEntities.E5_Event import E5_Event
from ..NodeProperties.P12_occurred_in_the_presence_of import \
    P12_occurred_in_the_presence_of
from ..NodeProperties.P92_brought_into_existence import \
    P92_brought_into_existence
from ..NodeProperties.P93_took_out_of_existence import \
    P93_took_out_of_existence


class E77_Persistent_Item(E1_CRM_Entity):
    occurred_in_the_presence_of = RelationshipFrom(
        E5_Event,
        "P12_occurred_in_the_presence_of",
        model=P12_occurred_in_the_presence_of,
    )
    brought_into_existence = RelationshipFrom(
        ".E63_Beggining_of_Existence.E63_Beggining_of_Existence",
        "P92_brought_into_existence",
        model=P92_brought_into_existence,
    )
    took_out_of_existence = RelationshipFrom(
        ".E64_End_of_Existence.E64_End_of_Existence",
        "P93_took_out_of_existence",
        model=P93_took_out_of_existence,
    )
