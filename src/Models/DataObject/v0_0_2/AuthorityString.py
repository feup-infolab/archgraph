from src.Models.DataObject.v0_0_2.String import Schema, String


class Schema(Schema):
    pass


class AuthorityString(String):
    pass

    def __init__(self, schema=None, *args, **kwargs):
        if schema is None:
            schema = Schema()

        super().__init__(schema, *args, **kwargs)
