from neomodel import RelationshipTo
from src.Models.CRM.v5_0_2.NodeEntities.E73_Information_Object import (
    E73_Information_Object,
)

from src.Models.CRM.v5_0_2.NodeProperties.P68_foresees_use_of import P68_foresees_use_of
from src.Models.CRM.v5_0_2.NodeProperties.P69_has_association_with import (
    P69_has_association_with,
)


class E29_Design_or_Procedure(E73_Information_Object):
    has_association_with = RelationshipTo(
        ".E29_Design_or_Procedure.E29_Design_or_Procedure",
        "P69_has_association_with",
        model=P69_has_association_with,
    )
    foresees_use_of = RelationshipTo(
        ".E57_Material.E57_Material", "P68_foresees_use_of", model=P68_foresees_use_of,
    )
