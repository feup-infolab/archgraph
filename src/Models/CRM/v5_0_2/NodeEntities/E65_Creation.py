from marshmallow import fields
from neomodel import RelationshipTo
from src.Models.CRM.v5_0_2.NodeEntities.E7_Activity import E7_Activity, E7_ActivitySchema
from src.Models.CRM.v5_0_2.NodeEntities.E63_Beggining_of_Existence import (
    E63_Beggining_of_Existence,
    E63_Beggining_of_ExistenceSchema)
from src.Models.CRM.v5_0_2.NodeProperties.P94_has_created import P94_has_created


class E65_CreationSchema(E7_ActivitySchema, E63_Beggining_of_ExistenceSchema):
    has_created = fields.List(fields.Nested(
        "src.Models.CRM.v5_0_2.NodeEntities.E28_Conceptual_Object.E28_Conceptual_ObjectSchema")
    )


class E65_Creation(E7_Activity, E63_Beggining_of_Existence):
    has_created = RelationshipTo(
        ".E28_Conceptual_Object.E28_Conceptual_Object",
        "P94_has_created",
        model=P94_has_created,
    )

    def __init__(self, schema=None, *args, **kwargs):
        if schema is None:
            schema = E65_CreationSchema()

        super().__init__(schema, *args, **kwargs)
