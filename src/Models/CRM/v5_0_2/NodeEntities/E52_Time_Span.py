from neomodel import DateTimeFormatProperty, RelationshipTo
from src.Models.CRM.v5_0_2.NodeEntities.E1_CRM_Entity import E1_CRM_Entity
from src.Models.CRM.v5_0_2.NodeProperties.P86_falls_within import \
    P86_falls_within
from src.Models.CRM.v5_0_2.NodeProperties.P191_had_duration import \
    P191_had_duration


class E52_Time_Span(E1_CRM_Entity):
    date = DateTimeFormatProperty(format="%Y-%m-%d", unique_index=True, required=True)
    falls_within = RelationshipTo(
        ".E52_Time_Span.E52_Time_Span", "P86_falls_within", model=P86_falls_within
    )
    had_duration = RelationshipTo(
        ".E54_Dimension.E54_Dimension", "P191_had_duration", model=P191_had_duration
    )
