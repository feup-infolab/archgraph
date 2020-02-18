from neomodel import StructuredRel, RelationshipTo, One

from .P01_has_domain import P01_has_domain
from .P02_has_range import P02_has_range


class PC0_CRM_Property(StructuredRel):

    hasDomain = RelationshipTo(
        "E1_CRM_Entity", "P01_has_domain", cardinality=One, model=P01_has_domain
    )
    hasRange = RelationshipTo(
        "E1_CRM_Entity", "P02_has_range", cardinality=One, model=P02_has_range
    )
