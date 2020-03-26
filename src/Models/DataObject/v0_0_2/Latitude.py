from src.Models.DataObject.v0_0_2.GeospatialCoordinates import (
    GeospatialCoordinates, Schema)


class Schema(Schema):
    pass


class Latitude(GeospatialCoordinates):
    pass

    def __init__(self, schema=None, *args, **kwargs):
        if schema is None:
            schema = Schema()

        super().__init__(schema, *args, **kwargs)
