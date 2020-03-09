from src.Models.DataObject.v0_0_2.DataObject import (DataObject,
                                                     DataObjectSchema)


class AuthorityFileSchema(DataObjectSchema):
    pass


class AuthorityFile(DataObject):
    pass

    def __init__(self, schema=None, *args, **kwargs):
        if schema is None:
            schema = AuthorityFileSchema()

        super().__init__(schema, *args, **kwargs)
