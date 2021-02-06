from marshmallow import fields
from neomodel import RelationshipTo
from src.Models.CRM.v5_0_2.NodeEntities.E63_Beggining_of_Existence import (
    E63_Beggining_of_Existence,
    E63_Beggining_of_ExistenceSchema,
)
from src.Models.CRM.v5_0_2.NodeProperties.P96_by_mother import P96_by_mother
from src.Models.CRM.v5_0_2.NodeProperties.P97_from_father import P97_from_father
from src.Models.CRM.v5_0_2.NodeProperties.P98_brought_into_life import (
    P98_brought_into_life,
)
from src.GCF.decorators.OntologyClass import decorator_schema


@decorator_schema
class E67_BirthSchema(E63_Beggining_of_ExistenceSchema):
    by_mother = fields.List(
        fields.Nested("src.Models.CRM.v5_0_2.NodeEntities.E21_Person.E21_PersonSchema")
    )
    from_father = fields.List(
        fields.Nested("src.Models.CRM.v5_0_2.NodeEntities.E21_Person.E21_PersonSchema")
    )
    brought_into_life = fields.List(
        fields.Nested("src.Models.CRM.v5_0_2.NodeEntities.E21_Person.E21_PersonSchema")
    )


class E67_Birth(E63_Beggining_of_Existence):
    by_mother = RelationshipTo(
        ".E21_Person.E21_Person", "P96_by_mother", model=P96_by_mother
    )
    from_father = RelationshipTo(
        ".E21_Person.E21_Person", "P97_from_father", model=P97_from_father
    )
    brought_into_life = RelationshipTo(
        ".E21_Person.E21_Person", "P98_brought_into_life", model=P98_brought_into_life
    )

    def __init__(self, schema=None, *args, **kwargs):
        if schema is None:
            schema = E67_BirthSchema()

        super().__init__(schema, *args, **kwargs)
