from neomodel import RelationshipFrom

from src.Models.CRM.v5_0_2.NodeEntities.E18_Physical_Thing import \
    E18_Physical_Thing
from src.Models.CRM.v5_0_2.NodeProperties.P56_bears_feature import P56_bears_feature


class E26_Physical_Feature(E18_Physical_Thing):
    bears_feature = RelationshipFrom(
        ".E19_Physical_Object.E19_Physical_Object",
        "P56_bears_feature",
        model=P56_bears_feature)
