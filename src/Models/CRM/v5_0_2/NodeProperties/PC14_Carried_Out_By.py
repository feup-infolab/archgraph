from neomodel import StructuredRel, RelationshipFrom, One

import src.Models.CRM.v5_0_2.NodeProperties.PC0_CRM_Property as PC0_CRM_Property
import src.Models.CRM.v5_0_2.NodeProperties.P01_has_domain as P01_has_domain
import src.Models.CRM.v5_0_2.NodeProperties.P02_has_range as P02_has_range

import src.Models.CRM.v5_0_2.NodeProperties.P14_1_in_the_role_of as P14_1_in_the_role_of


class PC14_Carried_Out_By(PC0_CRM_Property):
    hasDomain = RelationshipFrom(
        "E7_Activity", "P01_has_domain", cardinality=One, model=P01_has_domain
    )
    hasRange = RelationshipFrom(
        "E39_Actor", "P02_has_range", cardinality=One, model=P02_has_range
    )
    inTheRoleOf = RelationshipFrom(
        "E55_Type", "P14.1_in_the_role_of", cardinality=One, model=P14_1_in_the_role_of
    )
