from marshmallow import Schema, fields
from neomodel import RelationshipTo

from src.Models.CRM.v5_0_2.NodeEntities.E1_CRM_Entity import E1_CRM_Entity
from src.Models.CRM.v5_0_2.NodeEntities.E28_Conceptual_Object import (
    E28_Conceptual_Object,
)
from src.Models.CRM.v5_0_2.NodeProperties.P67_refers_to import P67_refers_to
from src.Models.CRM.v5_0_2.NodeProperties.P129_is_about import P129_is_about
from src.Models.CRM.v5_0_2.NodeProperties.P148_has_component import P148_has_component


class E89_Propositional_ObjectSchema(Schema):
    P106_is_composed_of = fields.List(
        fields.Nested(
            "src.Models.CRM.v5_0_2.NodeEntities.E89_Propositional_Object.E89_Propositional_ObjectSchema"
        )
    )
    P67_refers_to = fields.List(
        fields.Nested(
            "src.Models.CRM.v5_0_2.NodeEntities.E1_CRM_Entity.E1_CRM_EntitySchema"
        )
    )
    P129_is_about = fields.List(
        fields.Nested(
            "src.Models.CRM.v5_0_2.NodeEntities.E1_CRM_Entity.E1_CRM_EntitySchema"
        )
    )


class E89_Propositional_Object(E28_Conceptual_Object):
    P148_has_component = RelationshipTo(
        ".E89_Propositional_Object.E89_Propositional_Object",
        "P148_has_component",
        model=P148_has_component,
    )
    P67_refers_to = RelationshipTo(
        ".E1_CRM_Entity.E1_CRM_Entity", "P67_refers_to", model=P67_refers_to,
    )
    P129_is_about = RelationshipTo(
        ".E1_CRM_Entity.E1_CRM_Entity", "P129_is_about", model=P129_is_about,
    )

    def __init__(self, schema=None, *args, **kwargs):
        if schema is None:
            schema = E89_Propositional_ObjectSchema()

        super().__init__(schema, *args, **kwargs)
