from neomodel import RelationshipFrom

from src.Models.CRM.v5_0_2.NodeEntities.E18_Physical_Thing import \
    E18_Physical_Thing
from src.Models.CRM.v5_0_2.NodeProperties.P25_moved import P25_moved


class E19_Physical_Object(E18_Physical_Thing):
    moved = RelationshipFrom(
        ".E9_Move.E9_Move",
        "P25_moved",
        model=P25_moved)
