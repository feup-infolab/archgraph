from neomodel import RelationshipTo
from src.Models.CRM.v5_0_2.NodeEntities.E63_Beggining_of_Existence import (
    E63_Beggining_of_Existence,
)
from src.Models.CRM.v5_0_2.NodeEntities.E64_End_of_Existence import E64_End_of_Existence
from src.Models.CRM.v5_0_2.NodeProperties.P123_resulted_in import P123_resulted_in
from src.Models.CRM.v5_0_2.NodeProperties.P124_transformed import P124_transformed


class E81_Transformation(E63_Beggining_of_Existence, E64_End_of_Existence):
    resulted_in = RelationshipTo(
        ".E18_Physical_Thing.E18_Physical_Thing",
        "P123_resulted_in",
        model=P123_resulted_in,
    )
    transformed = RelationshipTo(
        ".E18_Physical_Thing.E18_Physical_Thing",
        "P124_transformed",
        model=P124_transformed,
    )
