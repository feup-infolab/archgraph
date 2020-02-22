from neomodel import One, RelationshipFrom
from src.Models.CRM.v5_0_2.NodeEntities.E2_Temporal_Entity import \
    E2_Temporal_Entity
from src.Models.CRM.v5_0_2.NodeProperties.P5_consists_of import P5_consists_of


class E3_Condition_State(E2_Temporal_Entity):
    consists_of = RelationshipFrom(
        "E3_Condition_State", "P5_consists_of", cardinality=One, model=P5_consists_of
    )
