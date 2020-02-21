from neomodel import One, RelationshipTo

from .P14_1_in_the_role_of import P14_1_in_the_role_of
from .PC0_CRM_Property import PC0_CRM_Property


class PC14_Carried_Out_By(PC0_CRM_Property):
    inTheRoleOf = RelationshipTo(
        "..NodeEntities.E55_Type.E55_Type",
        ".P14_1_in_the_role_of",
        cardinality=One,
        model=P14_1_in_the_role_of,
    )
