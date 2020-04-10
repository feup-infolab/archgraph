from src.Models.DataObject.v0_0_2.GeospatialCoordinates import (
    GeospatialCoordinates,
    GeospatialCoordinatesSchema,
)


class LongitudeSchema(GeospatialCoordinatesSchema):
    pass


class Longitude(GeospatialCoordinates):
    pass

    def __init__(self, schema=None, *args, **kwargs):
        if schema is None:
            schema = LongitudeSchema()

        super().__init__(schema, *args, **kwargs)
