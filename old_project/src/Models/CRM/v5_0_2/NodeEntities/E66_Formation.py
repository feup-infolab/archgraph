from marshmallow import fields
from neomodel import RelationshipTo
from src.Models.CRM.v5_0_2.NodeEntities.E7_Activity import (
    E7_Activity,
    E7_ActivitySchema,
)
from src.Models.CRM.v5_0_2.NodeEntities.E63_Beggining_of_Existence import (
    E63_Beggining_of_Existence,
    E63_Beggining_of_ExistenceSchema,
)
from src.Models.CRM.v5_0_2.NodeProperties.P95_has_formed import P95_has_formed
from src.Models.CRM.v5_0_2.NodeProperties.P151_was_formed_from import (
    P151_was_formed_from,
)
from src.GCF.decorators.OntologyClass import decorator_schema


@decorator_schema
class E66_FormationSchema(E7_ActivitySchema, E63_Beggining_of_ExistenceSchema):
    has_formed = fields.List(
        fields.Nested("src.Models.CRM.v5_0_2.NodeEntities.E74_Group.E74_GroupSchema")
    )
    was_formed_from = fields.List(
        fields.Nested("src.Models.CRM.v5_0_2.NodeEntities.E74_Group.E74_GroupSchema")
    )


class E66_Formation(E7_Activity, E63_Beggining_of_Existence):
    has_formed = RelationshipTo(
        ".E74_Group.E74_Group", "P95_has_formed", model=P95_has_formed
    )
    was_formed_from = RelationshipTo(
        ".E74_Group.E74_Group", "P151_was_formed_from", model=P151_was_formed_from,
    )

    def __init__(self, schema=None, *args, **kwargs):
        if schema is None:
            schema = E66_FormationSchema()

        super().__init__(schema, *args, **kwargs)
