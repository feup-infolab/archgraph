from marshmallow import Schema, fields
from neomodel import (One, RelationshipTo, StringProperty,
                      StructuredNode, UniqueIdProperty, db)
from src.GCF.decorators.OntologyClass import ontology_class
from src.Models.CRM.v5_0_2.NodeProperties.has_value import has_value
from src.Models.CRM.v5_0_2.NodeProperties.P1_is_identified_by import \
    P1_is_identified_by
from src.Models.CRM.v5_0_2.NodeProperties.P2_has_type import P2_has_type
from src.Models.CRM.v5_0_2.NodeProperties.P48_has_preferred_identifier import \
    P48_has_preferred_identifier
from src.Models.CRM.v5_0_2.NodeProperties.P137_exemplifies import \
    P137_exemplifies
from src.Models.CRM.v5_0_2.NodeProperties.P138_represents import \
    P138_represents
from src.Models.CRM.v5_0_2.NodeProperties.P139_has_alternative_form import \
    P139_has_alternative_form
from src.Models.DataObject.v0_0_2.SuperClass import SuperClass


class E1_CRM_EntitySchema(Schema):
    uid = fields.String()
    name = fields.String(required=True)
    P138_represents = fields.List(fields.Nested("src.Models.CRM.v5_0_2.NodeEntities.E36_Visual_Item.E36_Visual_ItemSchema"))
    #P2_has_type = fields.List(fields.Nested("src.Models.CRM.v5_0_2.NodeEntities.E55_Type.E55_TypeSchema"))
    #P137_exemplifies = fields.List(fields.Nested("src.Models.CRM.v5_0_2.NodeEntities.E55_Type.E55_TypeSchema"))
    # P48_has_preferred_identifier = fields.Nested("src.Models.CRM.v5_0_2.NodeEntities.E42_Identifier.E42_IdentifierSchema")
    # P139_has_alternative_form = fields.List(fields.Nested("src.Models.CRM.v5_0_2.NodeEntities.E41_Appellation.E41_AppellationSchema"))
    # P1_is_identified_by = fields.Nested("src.Models.CRM.v5_0_2.NodeEntities.E55_Type.E55_TypeSchema")
    has_value = fields.List(fields.Nested("src.Models.DataObject.v0_0_2.DataObject.DataObjectSchema"))


@ontology_class
class E1_CRM_Entity(StructuredNode, SuperClass):
    name = StringProperty(unique_index=True, required=True)
    uid = UniqueIdProperty()

    P138_represents = RelationshipTo(
        ".E36_Visual_Item.E36_Visual_Item", "P138_represents", model=P138_represents
    )
    P2_has_type = RelationshipTo(".E55_Type.E55_Type", "P2_has_type", model=P2_has_type)
    P137_exemplifies = RelationshipTo(
        ".E55_Type.E55_Type", "P137_exemplifies", model=P137_exemplifies
    )
    P48_has_preferred_identifier = RelationshipTo(
        ".E42_Identifier.E42_Identifier",
        "P48_has_preferred_identifier",
        cardinality=One,
        model=P48_has_preferred_identifier,
    )
    P139_has_alternative_form = RelationshipTo(
        ".E41_Appellation.E41_Appellation",
        "P139_has_alternative_form",
        model=P139_has_alternative_form,
    )
    P1_is_identified_by = RelationshipTo(
        ".E41_Appellation.E41_Appellation",
        "P1_is_identified_by",
        cardinality=One,
        model=P1_is_identified_by,
    )
    has_value = RelationshipTo(
        "src.Models.DataObject.v0_0_2.DataObject.DataObject",
        "has_value",
        model=has_value,
    )

    def __init__(self, schema=None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if schema is None:
            schema = E1_CRM_EntitySchema()

        SuperClass.__init__(self, schema)
