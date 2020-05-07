from marshmallow import fields, Schema
from neomodel import RelationshipTo
from src.Models.CRM.v5_0_2.NodeEntities.E89_Propositional_Object import (
    E89_Propositional_Object,
    E89_Propositional_ObjectSchema)
from src.Models.CRM.v5_0_2.NodeEntities.E90_Symbolic_Object import E90_Symbolic_Object, E90_Symbolic_ObjectSchema
from src.Models.CRM.v5_0_2.NodeProperties.P165_incorporates import P165_incorporates
from src.GCF.decorators.OntologyClass import decorator_schema


#todo
@decorator_schema
class E73_Information_ObjectSchema(E90_Symbolic_ObjectSchema):
    incorporates = fields.List(fields.Nested(
        "src.Models.CRM.v5_0_2.NodeEntities.E73_Information_Object.E73_Information_ObjectSchema")
    )


class E73_Information_Object(E89_Propositional_Object, E90_Symbolic_Object):
    incorporates = RelationshipTo(
        ".E73_Information_Object.E73_Information_Object",
        "P165_incorporates",
        model=P165_incorporates,
    )

    def __init__(self, schema=None, *args, **kwargs):
        if schema is None:
            schema = E73_Information_ObjectSchema()

        super().__init__(schema, *args, **kwargs)
