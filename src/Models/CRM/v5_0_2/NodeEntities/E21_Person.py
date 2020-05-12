from marshmallow import fields
from neomodel import RelationshipTo
from src.Models.CRM.v5_0_2.NodeEntities.E20_Biological_Object import (
    E20_Biological_Object,
    E20_Biological_ObjectSchema)
from src.Models.CRM.v5_0_2.NodeProperties.P152_has_parent import P152_has_parent
from src.GCF.decorators.OntologyClass import decorator_schema


@decorator_schema
class E21_PersonSchema(E20_Biological_ObjectSchema):
    has_parent = fields.List(fields.Nested(
        "src.Models.CRM.v5_0_2.NodeEntities.E21_Person.E21_PersonSchema")
    )


class E21_Person(E20_Biological_Object):
    has_parent = RelationshipTo(
        ".E21_Person.E21_Person", "P152_has_parent", model=P152_has_parent
    )

    def __init__(self, schema=None, *args, **kwargs):
        if schema is None:
            schema = E21_PersonSchema()

        super().__init__(schema, *args, **kwargs)
