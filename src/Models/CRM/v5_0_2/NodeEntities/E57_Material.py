from neomodel import RelationshipFrom

from src.Models.CRM.v5_0_2.NodeEntities.E55_Type import E55_Type
from src.Models.CRM.v5_0_2.NodeProperties.P45_consists_of import P45_consists_of
from src.Models.CRM.v5_0_2.NodeProperties.P68_foresees_use_of import P68_foresees_use_of


class E57_Material(E55_Type):
    consists_of = RelationshipFrom(
        ".E18_Physical_Thing.E18_Physical_Thing",
        "P45_consists_of",
        model=P45_consists_of)
    foresees_use_of = RelationshipFrom(
        ".E29_Design_or_Procedure.E29_Design_or_Procedure",
        "P68_foresees_use_of",
        model=P68_foresees_use_of)
