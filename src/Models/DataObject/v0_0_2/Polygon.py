from src.Models.DataObject.v0_0_2.GeospatialCoordinates import (
    GeospatialCoordinates, GeospatialCoordinatesSchema)


class PolygonSchema(GeospatialCoordinatesSchema):
    pass


class Polygon(GeospatialCoordinates):
    pass

    def __init__(self, schema=None, *args, **kwargs):
        if schema is None:
            schema = PolygonSchema()

        super().__init__(schema, *args, **kwargs)
