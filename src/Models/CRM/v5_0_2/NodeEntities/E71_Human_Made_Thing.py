from neomodel import RelationshipTo
from src.Models.CRM.v5_0_2.NodeEntities.E70_Thing import E70_Thing, E70_ThingSchema
from src.Models.CRM.v5_0_2.NodeProperties.P102_has_title import P102_has_title
from src.Models.CRM.v5_0_2.NodeProperties.P103_was_intended_for import (
    P103_was_intended_for,
)


#todo
class E71_Human_Made_ThingSchema(E70_ThingSchema):
    pass
    # P103_was_intended_for = fields.List(fields.Nested("src.Models.CRM.v5_0_2.NodeEntities.E55_Type.E55_TypeSchema"))
    # P102_has_title = fields.List(fields.Nested("src.Models.CRM.v5_0_2.NodeEntities.E35_Title.E35_TitleSchema"))


class E71_Human_Made_Thing(E70_Thing):
    P103_was_intended_for = RelationshipTo(
        ".E55_Type.E55_Type", "P103_was_intended_for", model=P103_was_intended_for,
    )
    P102_has_title = RelationshipTo(
        ".E35_Title.E35_Title", "P102_has_title", model=P102_has_title,
    )

    def __init__(self, schema=None, *args, **kwargs):
        if schema is None:
            schema = E71_Human_Made_ThingSchema()

        super().__init__(schema, *args, **kwargs)
