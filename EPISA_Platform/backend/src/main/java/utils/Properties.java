package utils;

import org.apache.jena.rdf.model.Model;
import org.apache.jena.rdf.model.ModelFactory;
import org.apache.jena.rdf.model.Property;
import org.apache.jena.rdf.model.Resource;

import java.util.HashMap;

public class Properties {
    public HashMap<String, Property> properties;
    public Model model;
    public String string200717 = "http://erlangen-crm.org/200717/";
    public String untitledOntology = "http://www.episa.inesctec.pt/archonto/registo1-15#";


    public Properties() {
        this.model = ModelFactory.createDefaultModel();
        this.properties = new HashMap<>();
    }

    public Property getTitleOntology() {
        return model.getProperty(untitledOntology);
    }

    public Property getNameSpace() {
        return model.getProperty(string200717);
    }

//    public Property getHasTypology() {
//        return model.getProperty(string200717, "has_typology");
//    }
//
//    public Property getHasSubject() {
//        return model.getProperty(string200717, "has_subject");
//    }
//
//    public Property getHasDocTradition() {
//        return model.getProperty(string200717, "has_doc_tradition");
//    }
//
//    public Property getHasWritingIdentifier() {
//        return model.getProperty(string200717, "has_writing_identifier");
//    }
//
//    public Property getHasWriting() {
//        return model.getProperty(string200717, "has_writing");
//    }
//
//    public Property getHasRelatedDocument() {
//        return model.getProperty(string200717, "has_related_document");
//    }
//
//    public Property getHasAccessConditionJustifification() {
//        return model.getProperty(string200717, "has_access_condition_justification");
//    }
//
//    public Property getHasAccessCondition() {
//        return model.getProperty(string200717, "has_access_condition");
//    }
//
//    public Property getHasLanguageIdentifier() {
//        return model.getProperty(string200717, "has_language_identifier");
//    }
//
//    public Property getHasLanguage() {
//        return model.getProperty(string200717, "has_language");
//    }
//
//    public Property getHasConservationStatus() {
//        return model.getProperty(string200717, "has_conservation_status");
//    }
//
//    public Property getHasConservationStatusID() {
//        return model.getProperty(string200717, "has_conservation_status_ID");
//    }
//
//    public Property getHasConservationStatusFD() {
//        return model.getProperty(string200717, "has_conservation_status_FD");
//    }
//
//    public Property getHasReproductionCondition() {
//        return model.getProperty(string200717, "has_reproduction_condition");
//    }
//
//    public Property getReproductionConditionJustifificationProperty() {
//        return model.getProperty(string200717, "has_reproduction_condition_justification");
//    }
//
//    public Property getHasRelatedEvents() {
//        return model.getProperty(string200717, "has_related_event");
//    }
//
//    public Property getHasRelatedEventsType() {
//        return model.getProperty(string200717, "has_related_event_type");
//    }
//
//    public Property getHasRelatedEventsID() {
//        return model.getProperty(string200717, "has_related_event_id");
//    }
//
//    public Property getHasRelatedEventsFD() {
//        return model.getProperty(string200717, "has_related_event_fd");
//    }

    public Property getRdfType() {
        return model.getProperty("http://www.w3.org/1999/02/22-rdf-syntax-ns#type");
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

    public Property getString() {
        return model.getProperty("http://www.episa.inesctec.pt/data_object#String");
    }

    public Property getARP12HasDescriptionLevel() {
        return model.getProperty(untitledOntology, "ARP12_has_level_of_description");
    }

    public Property getNamedIndividual() {
        return model.getProperty("http://www.w3.org/2002/07/owl#NamedIndividual");
    }

    public Property getE42Identifier() {
        return model.getProperty(string200717 + "E42_Identifier");
    }

    public Property getARE3SuppliedTitle() {
        return model.getProperty(untitledOntology + "ARE3SuppliedTitle");
    }

    public Property getARE2FormalTitle() {
        return model.getProperty(untitledOntology + "ARE2FormalTitle");

    }

    public Property getTitleString() {
        return model.getProperty(untitledOntology + "titleString");
    }

    public Property getE22HumanMadeObject() {
        return model.getProperty(string200717 + "E22_Human-Made_Object");

    }

    public Property getE54Dimension() {
        return model.getProperty(string200717 + "E54_Dimension");
    }

    public Property getE58MeasurementUnit() {
        return model.getProperty(string200717 + "E58_Measurement_Unit");
    }

    public Property getPropertyWithNameSpace(String property) {
        return model.getProperty(untitledOntology + property);
    }

    //================ Properties    =================

    public Property getP1IsIdentifiedBy() {
        return model.getProperty(string200717, "P1_is_identified_by");
    }

    public Property getP2HasType() {
        return model.getProperty(string200717, "P2_has_type");
    }

    public Property getP43HasDimension() {
        return model.getProperty(string200717 + "P43_has_dimension");
    }

    public Property getP45ConsistsOf() {
        return model.getProperty(string200717 + "P45_consists_of");
    }

    public Property getP90HasValue() {
        return model.getProperty(string200717 + "P90_has_value");
    }

    public Property getP91HasUnit() {
        return model.getProperty(string200717 + "P91_has_unit");
    }

    public Property getP102HasTitle() {
        return model.getProperty(string200717, "P102_has_title");
    }

    public Property getP128IsCarriedBy() {
        return model.getProperty(string200717, "P128i_is_carried_by");
    }
}
