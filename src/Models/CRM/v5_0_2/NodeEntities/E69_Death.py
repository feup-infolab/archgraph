from marshmallow import fields
from neomodel import RelationshipTo
from src.Models.CRM.v5_0_2.NodeEntities.E64_End_of_Existence import E64_End_of_Existence, E64_End_of_ExistenceSchema
from src.Models.CRM.v5_0_2.NodeProperties.P100_was_death_of import P100_was_death_of
from src.GCF.decorators.OntologyClass import decorator_schema


@decorator_schema
class E69_DeathSchema(E64_End_of_ExistenceSchema):
    was_death_of = fields.List(fields.Nested(
        "src.Models.CRM.v5_0_2.NodeEntities.E21_Person.E21_PersonSchema")
    )


class E69_Death(E64_End_of_Existence):
    was_death_of = RelationshipTo(
        ".E21_Person.E21_Person", "P100_was_death_of", model=P100_was_death_of
    )

    def __init__(self, schema=None, *args, **kwargs):
        if schema is None:
            schema = E69_DeathSchema()

        super().__init__(schema, *args, **kwargs)
