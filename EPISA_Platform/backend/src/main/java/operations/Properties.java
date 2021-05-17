package operations;

import org.apache.jena.rdf.model.Model;
import org.apache.jena.rdf.model.Property;
import org.apache.jena.rdf.model.Resource;

import java.util.HashMap;

public class Properties {
    public HashMap<String, Property> properties;
    public Model model;
    public String string200717 = "http://erlangen-crm.org/200717/";
    public String untitledOntology = "http://www.semanticweb.org/dmelo/ontologies/2020/7/untitled-ontology-151#";


    public Properties(Model model) {
        this.model = model;
        this.properties = new HashMap<>();
    }


    public Property getHasMaterial() {
        return model.getProperty(string200717, "has_material");
    }

    public Property getHasMaterialType() {
        return model.getProperty(string200717, "has_material_type");
    }


    public Property getHasTypology() {
        return model.getProperty(string200717, "has_typology");
    }

    public Property getHasSubject() {
        return model.getProperty(string200717, "has_subject");
    }

    public Property getHasDocTradition() {
        return model.getProperty(string200717, "has_doc_tradition");
    }

    public Property getHasWritingIdentifier() {
        return model.getProperty(string200717, "has_writing_identifier");

    }

    public Property getHasWriting() {
        return model.getProperty(string200717, "has_writing");

    }


    public Property getP102HasTitle() {
        return model.getProperty(string200717, "P102_has_title");
    }

    public Property getP2HasType() {
        return model.getProperty(string200717, "P2_has_type");
    }

    public Property getP1IsIdentifiedBy() {
        return model.getProperty(string200717, "P1_is_identified_by");

    }

    public Property getHasRelatedDocument() {
        return model.getProperty(string200717, "has_related_document");
    }

    public Property getHasAccessConditionJustifification() {
        return model.getProperty(string200717, "has_access_condition_justification");
    }

    public Property getHasAccessCondition() {
        return model.getProperty(string200717, "has_access_condition");
    }

    public Property getHasLanguageIdentifier() {
        return model.getProperty(string200717, "has_language_identifier");
    }

    public Property getHasLanguage() {
        return model.getProperty(string200717, "has_language");
    }

    public Property getHasConservationStatus() {
        return model.getProperty(string200717, "has_conservation_status");
    }

    public Property getHasConservationStatusID() {
        return model.getProperty(string200717, "has_conservation_status_ID");
    }

    public Property getHasConservationStatusFD() {
        return model.getProperty(string200717, "has_conservation_status_FD");
    }

    public Property getDimension() {
        return model.getProperty(string200717, "has_dimension");
    }

    public Property getHasDimensionValue() {
        return model.getProperty(string200717, "has_dimension_value");
    }

    public Property getHasDimensionMU() {
        return model.getProperty(string200717, "has_dimension_measurement_unit");
    }

    public Property getHasDimensionComponent() {
        return model.getProperty(string200717, "has_dimension_component");
    }

    public Property getHasQuantity() {
        return model.getProperty(string200717, "has_quantity");
    }

    public Property getHasQuantityComponent() {
        return model.getProperty(string200717, "has_quantity_component");
    }

    public Property getHasQuantityMU() {
        return model.getProperty(string200717, "has_quantity_measurement_unit");
    }

    public Property getHasQuantityValue() {
        return model.getProperty(string200717, "has_quantity_value");
    }

    public Property getHasReproductionCondition() {
        return model.getProperty(string200717, "has_reproduction_condition");
    }

    public Property getReproductionConditionJustifificationProperty() {
        return model.getProperty(string200717, "has_reproduction_condition_justification");
    }

    public Property getHasRelatedEvents() {
        return model.getProperty(string200717, "has_related_event");
    }

    public Property getHasRelatedEventsType() {
        return model.getProperty(string200717, "has_related_event_type");
    }

    public Property getHasRelatedEventsID() {
        return model.getProperty(string200717, "has_related_event_id");
    }

    public Property getHasRelatedEventsFD() {
        return model.getProperty(string200717, "has_related_event_fd");
    }

    public Property getRdfType() {
        return model.getProperty("rdf:type");
    }

    public Property getRdfsLabel() {
        return model.getProperty("rdfs:label");
    }


    public Property getLabel() {
        return model.getProperty("http://www.w3.org/2000/01/rdf-schema#label");
    }

    public Property getHasUuid() {
        return model.getProperty(string200717, "has_uuid");
    }

    public Property getHasValue() {
        return model.getProperty("http://www.episa.inesctec.pt/ligacao#hasValue");
    }

    public Property getStringValue() {
        return model.getProperty("http://www.episa.inesctec.pt/data_object#stringValue");
    }

    public Property getARP12HasDescriptionLevel() {
        return model.getProperty(untitledOntology, "ARP12_has_level_of_description");
    }
}
