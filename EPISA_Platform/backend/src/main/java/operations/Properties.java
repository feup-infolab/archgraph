package operations;

import org.apache.jena.rdf.model.Model;
import org.apache.jena.rdf.model.Property;

import java.util.HashMap;

public class Properties {
    public HashMap<String, Property> properties;
    public Model model;

    public Properties(Model model) {
        this.properties = new HashMap<>();
        this.model = model;
    }

    public HashMap<String, Property> createProperties() {

        Property material= model.createProperty("http://erlangen-crm.org/200717/", "has_material");
        properties.put("material", material);

        Property materialType = model.createProperty("http://erlangen-crm.org/200717/", "has_material_type");
        properties.put("materialType", materialType);

        Property dimension = model.createProperty("http://erlangen-crm.org/200717/", "has_dimension");
        properties.put("dimension", dimension);

        Property dimensionValue = model.createProperty("http://erlangen-crm.org/200717/", "has_dimension_value");
        properties.put("dimensionValue", dimensionValue);

        Property dimensionMU = model.createProperty("http://erlangen-crm.org/200717/", "has_dimension_measurement_unit");
        properties.put("dimensionMU", dimensionMU);

        Property dimensionComponent = model.createProperty("http://erlangen-crm.org/200717/", "has_dimension_component");
        properties.put("dimensionComponent", dimensionComponent);

        Property quantity = model.createProperty("http://erlangen-crm.org/200717/", "has_quantity");
        properties.put("quantity", quantity);

        Property quantityValue = model.createProperty("http://erlangen-crm.org/200717/", "has_quantity_value");
        properties.put("quantityValue", quantityValue);

        Property quantityMU = model.createProperty("http://erlangen-crm.org/200717/", "has_quantity_measurement_unit");
        properties.put("quantityMU", quantityMU);

        Property quantityComponent = model.createProperty("http://erlangen-crm.org/200717/", "has_quantity_component");
        properties.put("quantityComponent", quantityComponent);

        Property conservation = model.createProperty("http://erlangen-crm.org/200717/", "has_conservation_status");
        properties.put("conservation", conservation);

        Property conservationID = model.createProperty("http://erlangen-crm.org/200717/", "has_conservation_status_ID");
        properties.put("conservationID", conservationID);

        Property conservationFD = model.createProperty("http://erlangen-crm.org/200717/", "has_conservation_status_FD");
        properties.put("conservationFD", conservationFD);

        Property llanguage = model.createProperty("http://erlangen-crm.org/200717/", "has_language");
        properties.put("llanguage", llanguage);

        Property languageIdentifier = model.createProperty("http://erlangen-crm.org/200717/", "has_language_identifier");
        properties.put("languageIdentifier", languageIdentifier);

        Property writing = model.createProperty("http://erlangen-crm.org/200717/", "has_writing");
        properties.put("writing", writing);

        Property writingIdentifier = model.createProperty("http://erlangen-crm.org/200717/", "has_writing_identifier");
        properties.put("writingIdentifier", writingIdentifier);

        Property doc = model.createProperty("http://erlangen-crm.org/200717/", "has_doc_tradition");
        properties.put("doc", doc);

        Property typology = model.createProperty("http://erlangen-crm.org/200717/", "has_typology");
        properties.put("typology", typology);

        Property subject = model.createProperty("http://erlangen-crm.org/200717/", "has_subject");
        properties.put("subject", subject);

        Property accessCondition = model.createProperty("http://erlangen-crm.org/200717/", "has_access_condition");
        properties.put("accessCondition", accessCondition);

        Property accessConditionJustifification = model.createProperty("http://erlangen-crm.org/200717/", "has_access_condition_justification");
        properties.put("accessConditionJustifification", accessConditionJustifification);

        Property ref = model.createProperty("http://erlangen-crm.org/200717/", "P2_has_type");
        properties.put("ref", ref);

        Property identification = model.createProperty("http://erlangen-crm.org/200717/", "P1_is_identified_by");
        properties.put("identification", identification);


        Property title = model.createProperty("http://erlangen-crm.org/200717/", "P102_has_title");
        properties.put("title", title);

        Property string = model.createProperty("http://www.episa.inesctec.pt/", "ligacao#hasValue");
        properties.put("string", string);

        Property stringValue = model.createProperty("http://www.episa.inesctec.pt/", "data_object#stringValue");
        properties.put("stringValue", stringValue);

        Property relatedDocument = model.createProperty("http://erlangen-crm.org/200717/", "has_related_document");
        properties.put("relatedDocument", relatedDocument);


        Property reproductionCondition = model.createProperty("http://erlangen-crm.org/200717/", "has_reproduction_condition");
        properties.put("reproductionCondition", reproductionCondition);

        Property reproductionConditionJustifification = model.createProperty("http://erlangen-crm.org/200717/", "has_reproduction_condition_justification");
        properties.put("reproductionConditionJustifification", reproductionConditionJustifification);

        Property relatedEventsType = model.createProperty("http://erlangen-crm.org/200717/", "has_related_event_type");
        properties.put("relatedEventsType", relatedEventsType);

        Property relatedEventsID = model.createProperty("http://erlangen-crm.org/200717/", "has_related_event_id");
        properties.put("relatedEventsID", relatedEventsID);

        Property relatedEventsFD = model.createProperty("http://erlangen-crm.org/200717/", "has_related_event_fd");
        properties.put("relatedEventsFD", relatedEventsFD);

        Property relatedEvents = model.createProperty("http://erlangen-crm.org/200717/", "has_related_event");
        properties.put("relatedEvents", relatedEvents);

        return properties;
    }

    public Property getMaterialProperty() {
        return properties.get("material");
    }

    public Property getMaterialTypeProperty() {
        return properties.get("materialType");
    }

    public Property getDimensionProperty() {
        return properties.get("dimension");
    }

    public Property getTypologyProperty() {
        return properties.get("typology");
    }

    public Property getSubjectProperty() {
        return properties.get("subject");
    }

    public Property getDocProperty() {
        return properties.get("doc");
    }

    public Property getWritingProperty() {
        return properties.get("writing");
    }

    public Property getWritingIdentifierProperty() {
        return properties.get("writingIdentifier");
    }

    public Property getStringProperty() {
        return properties.get("string");

    }

    public Property getStringValueProperty() {
        return properties.get("stringValue");

    }

    public Property getTitleProperty() {
        return properties.get("title");
    }

    public Property getRefProperty() {
        return properties.get("ref");
    }

    public Property getIdentificationProperty() {
        return properties.get("identification");

    }

    public Property getRelatedDocumentProperty() {
        return properties.get("relatedDocument");

    }

    public Property getAccessConditionJustifificationProperty() {
        return properties.get("accessConditionJustifification");
    }

    public Property getAccessConditionProperty() {
        return properties.get("accessCondition");
    }

    public Property getLanguageIdentifierProperty() {
        return properties.get("languageIdentifier");
    }

    public Property getLanguageProperty() {
        return properties.get("llanguage");
    }

    public Property getConservationProperty() {
        return properties.get("conservation");
    }

    public Property getConservationIDProperty() {
        return properties.get("conservationID");
    }

    public Property getConservationFDProperty() {
        return properties.get("conservationFD");
    }

    public Property getMaterialPropertyType() {
        return properties.get("materialType");
    }

    public Property getDimensionPropertyValue() {
        return properties.get("dimensionValue");
    }

    public Property getDimensionPropertyMU() {
        return properties.get("dimensionMU");
    }

    public Property getDimensionPropertyComponent() {
        return properties.get("dimensionComponent");
    }

    public Property getQuantityProperty() {
        return properties.get("quantity");
    }

    public Property getQuantityPropertyComponent() {
        return properties.get("quantityComponent");
    }

    public Property getQuantityPropertyMU() {
        return properties.get("quantityMU");
    }

    public Property getQuantityPropertyValue() {
        return properties.get("quantityValue");
    }

    public Property getReproductionConditionProperty() {
        return properties.get("reproductionCondition");
    }

    public Property getReproductionConditionJustifificationProperty() {
        return properties.get("reproductionConditionJustifification");
    }

    public Property getRelatedEventsProperty() {
        return properties.get("relatedEvents");
    }

    public Property getRelatedEventsTypeProperty() {
        return properties.get("relatedEventsType");
    }

    public Property getRelatedEventsIDProperty() {
        return properties.get("relatedEventsID");
    }

    public Property getRelatedEventsFDProperty() {
        return properties.get("relatedEventsFD");
    }
}
