from marshmallow import fields
from neomodel import RelationshipTo
from src.Models.CRM.v5_0_2.NodeEntities.E63_Beggining_of_Existence import (
    E63_Beggining_of_Existence,
    E63_Beggining_of_ExistenceSchema)
from src.Models.CRM.v5_0_2.NodeEntities.E64_End_of_Existence import E64_End_of_Existence, E64_End_of_ExistenceSchema
from src.Models.CRM.v5_0_2.NodeProperties.P123_resulted_in import P123_resulted_in
from src.Models.CRM.v5_0_2.NodeProperties.P124_transformed import P124_transformed


class E81_TransformationSchema(E63_Beggining_of_ExistenceSchema, E64_End_of_ExistenceSchema):
    resulted_in = fields.List(fields.Nested(
        "src.Models.CRM.v5_0_2.NodeEntities.E18_Physical_Thing.E18_Physical_ThingSchema")
    )
    transformed = fields.List(fields.Nested(
        "src.Models.CRM.v5_0_2.NodeEntities.E18_Physical_Thing.E18_Physical_ThingSchema")
    )


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

    def __init__(self, schema=None, *args, **kwargs):
        if schema is None:
            schema = E81_TransformationSchema()

        super().__init__(schema, *args, **kwargs)
