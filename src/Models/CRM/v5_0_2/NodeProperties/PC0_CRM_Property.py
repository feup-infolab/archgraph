from neomodel import One, RelationshipTo, StringProperty, StructuredNode, UniqueIdProperty

from .P01_has_domain import P01_has_domain
from .P02_has_range import P02_has_range


class PC0_CRM_Property(StructuredNode):

    name = StringProperty(unique_index=True, required=True)
    uid = UniqueIdProperty()


    hasDomain = RelationshipTo(
        "..NodeEntities.E1_CRM_Entity.E1_CRM_Entity",
        "P01_has_domain",
        cardinality=One,
        model=P01_has_domain,
    )
    hasRange = RelationshipTo(
        "..NodeEntities.E1_CRM_Entity.E1_CRM_Entity",
        "P02_has_range",
        cardinality=One,
        model=P02_has_range,
    )
