from neomodel import RelationshipTo
from src.Models.CRM.v5_0_2.NodeEntities.E7_Activity import E7_Activity
from src.Models.CRM.v5_0_2.NodeProperties.P31_has_modified import P31_has_modified
from src.Models.CRM.v5_0_2.NodeProperties.P126_employed import P126_employed


class E11_Modification(E7_Activity):
    employed = RelationshipTo(
        ".E57_Material.E57_Material", "P126_employed", model=P126_employed
    )
    has_modified = RelationshipTo(
        ".E18_Physical_Thing.E18_Physical_Thing",
        "P31_has_modified",
        model=P31_has_modified,
    )
