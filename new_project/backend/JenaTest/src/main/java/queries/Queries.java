package queries;

import org.apache.jena.query.Query;
import org.apache.jena.query.QueryFactory;

public class Queries {


    public Query getGeneral_query() {
        return QueryFactory.create("SELECT * WHERE {\n" +
                "  ?sub ?pred ?obj .\n" +
                "}");
    }

    public Query getTitle_query(String uuid) {
        return QueryFactory.create("SELECT  ?description\n" +
                "WHERE {\n" +
                    uuid + " <http://erlangen-crm.org/200717/P102_has_title> ?type .\n" +
                    "  ?type <http://www.episa.inesctec.pt/ligacao#hasValue> ?title_type .\n" +
                    "  ?title_type <http://www.episa.inesctec.pt/data_object#stringValue> ?description\n" +
                "}");
    }

    public Query getLevel_of_description_query(String uuid) {
        return QueryFactory.create("SELECT ?descriptionLevel\n" +
                "WHERE {\n" +
                uuid + " <http://www.semanticweb.org/dmelo/ontologies/2020/7/untitled-ontology-151#ARP12_has_level_of_description> ?descriptionLevel\n" +
                "}");
    }

    public Query getUuid(String uuid) {
        return QueryFactory.create("SELECT ?description\n" +
                "WHERE {\n" +
                uuid + " <http://erlangen-crm.org/200717/has_uuid> ?description\n" +
                "}");
    }

    public Query getIDd(String uuid) {
        return QueryFactory.create("SELECT ?description\n" +
                "WHERE {\n" +
                "?description <http://erlangen-crm.org/200717/has_uuid> \"" + uuid + "\" }");
    }


    public Query getReference_codes_query(String uuid) {
        return QueryFactory.create("SELECT  ?description \n" +
                "WHERE {\n" +
                uuid + " <http://erlangen-crm.org/200717/P1_is_identified_by> ?cidoc_identifier .\n" +
                "  ?cidoc_identifier <http://www.episa.inesctec.pt/ligacao#hasValue> ?identifier_value .\n" +
                "  ?cidoc_identifier <http://erlangen-crm.org/200717/P2_has_type> ?type.\n" +
                "  ?identifier_value <http://www.episa.inesctec.pt/data_object#stringValue> ?description\n" +
                "}");
    }

    public Query getIdFromReference_codes_query(String refCode) {
        return QueryFactory.create("SELECT  ?description \n" +
                "WHERE {\n" +
                "?description <http://erlangen-crm.org/200717/P1_is_identified_by> ?cidoc_identifier .\n" +
                "  ?cidoc_identifier <http://www.episa.inesctec.pt/ligacao#hasValue> ?identifier_value .\n" +
                "  ?cidoc_identifier <http://erlangen-crm.org/200717/P2_has_type> ?type.\n" +
                "  ?identifier_value <http://www.episa.inesctec.pt/data_object#stringValue> " + refCode + "\n" +
                "}");
    }

    public Query getPerson(String uuid) {
        return QueryFactory.create("SELECT ?name\n" +
                "WHERE {\n" +
                uuid + "<http://erlangen-crm.org/200717/P1_is_identified_by> ?object.\n" +
                "  ?object <http://www.episa.inesctec.pt/ligacao#hasValue> ?object2.\n" +
                "  ?object2 <http://www.episa.inesctec.pt/ligacao#stringValue> ?name \n" +
                "}");
    }

    public Query getPlace(String uuid) {
        return QueryFactory.create("SELECT ?name \n" +
                "WHERE {\n" +
                uuid + "<http://erlangen-crm.org/200717/P1_is_identified_by> ?object.\n" +
                "  ?object <http://www.episa.inesctec.pt/ligacao#hasValue> ?object2.\n" +
                "  ?object2 <http://www.episa.inesctec.pt/ligacao#stringValue> ?name\n" +
                "}");
    }

    public Query getAllDocs() {
        return QueryFactory.create("SELECT ?subject\n" +
                "WHERE {\n" +
                "  ?subject <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://erlangen-crm.org/200717/E31_Document>\n" +
                "}");
    }

    public Query insertUuid(String olduuid, String uuid) {
        return QueryFactory.create("INSERT {\n" +
                olduuid + "<has_uuid> \"" + uuid + "\" \n" +
                " }");
    }


    public Query getIdentifier(String uuid) {
        return QueryFactory.create("SELECT  ?identifier ?type \n" +
                "WHERE {\n" +
                uuid + " <http://erlangen-crm.org/200717/P1_is_identified_by> ?cidoc_identifier .\n" +
                "  ?cidoc_identifier <http://www.episa.inesctec.pt/ligacao#hasValue> ?identifier_value .\n" +
                "  ?cidoc_identifier <http://erlangen-crm.org/200717/P2_has_type> ?type.\n" +
                "  ?identifier_value <http://www.episa.inesctec.pt/data_object#stringValue> ?identifier\n" +
                "}");
    }

    public Query getTitle(String uuid){
        return QueryFactory.create("SELECT  ?title ?typen \n" +
                "WHERE {\n" +
                uuid + " <http://erlangen-crm.org/200717/P102_has_title> ?typen .\n" +
                "  ?typen <http://www.episa.inesctec.pt/ligacao#hasValue> ?type .\n" +
                "  ?type <http://www.episa.inesctec.pt/data_object#stringValue> ?title\n" +
                "}");
    }

    public Query getMaterial(String uuid){
        return QueryFactory.create("SELECT ?material ?component\n" +
                "WHERE {\n" +
                uuid + " <http://erlangen-crm.org/200717/has_material> ?material .\n" +
                uuid + " <http://erlangen-crm.org/200717/has_material> ?component\n" +
                "}");
    }

    public Query getDimension(String uuid) {
        return QueryFactory.create("SELECT ?dimension ?value ?measurementUnit ?component\n" +
                "WHERE {\n" +
                uuid + " <http://erlangen-crm.org/200717/has_dimension> ?dimension .\n" +
                uuid + " <http://erlangen-crm.org/200717/has_dimension_value> ?value .\n" +
                uuid + " <http://erlangen-crm.org/200717/has_dimension_measurement_unit> ?measurementUnit .\n" +
                uuid + " <http://erlangen-crm.org/200717/has_dimension_component> ?component\n" +
                "}");
    }

    public Query getQuantity(String uuid) {
        return QueryFactory.create("SELECT ?quantity ?value ?measurementUnit ?component\n" +
                "WHERE {\n" +
                uuid + " <http://erlangen-crm.org/200717/has_quantity> ?quantity .\n" +
                uuid + " <http://erlangen-crm.org/200717/has_quantity_value> ?value .\n" +
                uuid + " <http://erlangen-crm.org/200717/has_quantity_measurement_unit> ?measurementUnit .\n" +
                uuid + " <http://erlangen-crm.org/200717/has_quantity_component> ?component\n" +
                "}");
    }

    public Query getConservationStatus(String uuid) {
        return QueryFactory.create("SELECT ?conservationStatus ?initialDate ?finalDate \n" +
                "WHERE {\n" +
                uuid + " <http://erlangen-crm.org/200717/has_conservation_status> ?conservationStatus .\n" +
                uuid + " <http://erlangen-crm.org/200717/has_conservation_status_ID> ?initialDate .\n" +
                uuid + " <http://erlangen-crm.org/200717/has_conservation_status_FD> ?finalDate \n" +
                "}");
    }

    public Query getLanguage(String uuid) {
        return QueryFactory.create("SELECT ?language ?identifier\n" +
                "WHERE {\n" +
                uuid + " <http://erlangen-crm.org/200717/has_language> ?language .\n" +
                uuid + " <http://erlangen-crm.org/200717/has_language_identifier> ?identifier\n" +
                "}");
    }

    public Query getWriting(String uuid) {
        return QueryFactory.create("SELECT ?writing ?identifier\n" +
                "WHERE {\n" +
                uuid + " <http://erlangen-crm.org/200717/has_writing> ?writing .\n" +
                uuid + " <http://erlangen-crm.org/200717/has_writing_identifier> ?identifier\n" +
                "}");
    }

    public Query getDocTradition(String uuid) {
        return QueryFactory.create("SELECT ?documentaryTradition\n" +
                "WHERE {\n" +
                uuid + " <http://erlangen-crm.org/200717/has_doc_tradition> ?documentaryTradition \n" +
                "}");
    }

    public Query getDocTypology(String uuid) {
        return QueryFactory.create("SELECT ?documentaryTypology\n" +
                "WHERE {\n" +
                uuid + " <http://erlangen-crm.org/200717/has_typology> ?documentaryTypology \n" +
                "}");
    }

    public Query getSubject(String uuid) {
        return QueryFactory.create("SELECT ?subject\n" +
                "WHERE {\n" +
                uuid + " <http://erlangen-crm.org/200717/has_subject> ?subject \n" +
                "}");
    }

    public Query getAccessCondition(String uuid) {
        return QueryFactory.create("SELECT ?accessConditions ?justification\n" +
                "WHERE {\n" +
                uuid + " <http://erlangen-crm.org/200717/has_access_condition> ?accessConditions .\n" +
                uuid + " <http://erlangen-crm.org/200717/has_access_condition_justification> ?justification\n" +
                "}");
    }

    public Query getReproductionCondition(String uuid) {
        return QueryFactory.create("SELECT ?reproductionConditions ?justification\n" +
                "WHERE {\n" +
                uuid + " <http://erlangen-crm.org/200717/has_reproduction_condition> ?reproductionConditions .\n" +
                uuid + " <http://erlangen-crm.org/200717/has_reproduction_condition_justification> ?justification\n" +
                "}");
    }

    public Query getEvent(String uuid) {
        return QueryFactory.create("SELECT ?episaIdentifier ?eventType ?initialDate ?finalDate\n" +
                "WHERE {\n" +
                uuid + " <http://erlangen-crm.org/200717/has_related_event> ?episaIdentifier .\n" +
                uuid + " <http://erlangen-crm.org/200717/has_related_event_type> ?eventType .\n" +
                uuid + " <http://erlangen-crm.org/200717/has_related_event_id> ?initialDate .\n" +
                uuid + " <http://erlangen-crm.org/200717/has_related_event_fd> ?finalDate\n" +
                "}");
    }

    public Query getRelDoc(String uuid){
        return QueryFactory.create("SELECT ?episaIdentifier ?dglabIdentifier  ?title ?relationType\n" +
                "WHERE {\n" +
                uuid + " <http://erlangen-crm.org/200717/has_related_document> ?tdoc .\n" +
                "  ?tdoc <http://erlangen-crm.org/200717/has_uuid> ?episaIdentifier .\n" +
                "  ?tdoc <http://erlangen-crm.org/200717/P1_is_identified_by> ?cidoc_identifier .\n" +
                "  ?cidoc_identifier <http://www.episa.inesctec.pt/ligacao#hasValue> ?identifier_value .\n" +
                "  ?identifier_value <http://www.episa.inesctec.pt/data_object#stringValue> ?dglabIdentifier .\n" +
                "  ?tdoc <http://erlangen-crm.org/200717/P102_has_title> ?type .\n" +
                "  ?type <http://www.episa.inesctec.pt/ligacao#hasValue> ?title_type .\n" +
                "  ?title_type <http://www.episa.inesctec.pt/data_object#stringValue> ?title .\n" +
                uuid + " ?relationType ?tdoc \n" +
                "}");
    }


}
