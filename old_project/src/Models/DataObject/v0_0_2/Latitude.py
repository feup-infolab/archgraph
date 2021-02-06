from src.Models.DataObject.v0_0_2.GeospatialCoordinates import (
    GeospatialCoordinates,
    GeospatialCoordinatesSchema,
)
from src.GCF.decorators.OntologyClass import decorator_schema


@decorator_schema
class LatitudeSchema(GeospatialCoordinatesSchema):
    pass


class Latitude(GeospatialCoordinates):
    pass

    def __init__(self, schema=None, *args, **kwargs):
        if schema is None:
            schema = LatitudeSchema()

        super().__init__(schema, *args, **kwargs)
