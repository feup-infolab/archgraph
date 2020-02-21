from neomodel import One, RelationshipTo

import src.Models.CRM.v5_0_2.NodeProperties.P14_1_in_the_role_of as P14_1_in_the_role_of
import src.Models.CRM.v5_0_2.NodeProperties.PC0_CRM_Property as PC0_CRM_Property


class PC14_Carried_Out_By(PC0_CRM_Property):
    inTheRoleOf = RelationshipTo(
        "..NodeEntities.E55_Type.E55_Type",
        "P14.1_in_the_role_of",
        cardinality=One,
        model=P14_1_in_the_role_of,
    )
