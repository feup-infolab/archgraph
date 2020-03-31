from src.Models.DataObject.v0_0_2.String import String, StringSchema


class AuthorityStringSchema(StringSchema):
    pass


class AuthorityString(String):
    pass

    def __init__(self, schema=None, *args, **kwargs):
        if schema is None:
            schema = AuthorityStringSchema()

        super().__init__(schema, *args, **kwargs)
