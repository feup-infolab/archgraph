from neomodel import RelationshipFrom, RelationshipTo, StructuredRel
from src.Models.CRM.v5_0_2.NodeEntities.E6_Destruction import E6_Destruction
from src.Models.CRM.v5_0_2.NodeEntities.E72_Legal_Object import \
    E72_Legal_Object
from src.Models.CRM.v5_0_2.NodeProperties import P8_took_place_on_or_within
from src.Models.CRM.v5_0_2.NodeProperties.P13_destroyed import P13_destroyed
from src.Models.CRM.v5_0_2.NodeProperties.P24_transferred_title_of import P24_transferred_title_of
from src.Models.CRM.v5_0_2.NodeProperties.P30_transferred_custody_of import P30_transferred_custody_of
from src.Models.CRM.v5_0_2.NodeProperties.P31_has_modified import P31_has_modified
from src.Models.CRM.v5_0_2.NodeProperties.P34_concerned import P34_concerned
from src.Models.CRM.v5_0_2.NodeProperties.P7_took_place_at import \
    P7_took_place_at
from src.Models.CRM.v5_0_2.NodeProperties.P156_occupies import P156_occupies


class P46_is_composed_of(StructuredRel):
    pass



class E18_Physical_Thing(E72_Legal_Object):
    is_composed_of = RelationshipTo(
        ".E18_Physical_Thing.E18_Physical_Thing",
        "P46_is_composed_of",
        model=P46_is_composed_of)
    took_place_on_or_within = RelationshipFrom(
        ".E4_Period.E4_Period",
        "P8_took_place_on_or_within",
        model=P8_took_place_on_or_within)

    occupies = RelationshipTo(
        ".E53_Place.E53_Place", "P156_occupies", model=P156_occupies
    )
    took_place_at = RelationshipTo(
        ".E53_Place.E53_Place", "P7_took_place_at", model=P7_took_place_at
    )
    transferred_title_of = RelationshipFrom(
        ".E8_Acquisition.E8_Acquisition",
        "P24_transferred_title_of",
        model=P24_transferred_title_of)
    transferred_custody_of = RelationshipFrom(
        ".E10_Transfer_of_Custody.E10_Transfer_of_Custody",
        "P30_transferred_custody_of",
        model=P30_transferred_custody_of)
    has_modified = RelationshipFrom(
        ".E11_Modification.E11_Modification",
        "P31_has_modified",
        model=P31_has_modified)
    concerned = RelationshipFrom(
        ".E14_Condition_Assessment.E14_Condition_Assessment",
        "P34_concerned",
        model=P34_concerned
    )

    destroyed = RelationshipFrom(E6_Destruction, "P13_destroyed", model=P13_destroyed)
