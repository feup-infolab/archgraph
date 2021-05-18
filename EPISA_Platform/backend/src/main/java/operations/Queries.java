package operations;

import org.apache.jena.query.Query;
import org.apache.jena.query.QueryFactory;

public class Queries {
//    private Resources resources;
//    private Properties properties;
//    private Model model;


    public Queries() {

    }

    public Query getSummaryDoc(String refCode, String descriptionLevel, String title) {
        String myQuery = "SELECT distinct ?title ?episaIdentifier ?dglabIdentifier\n" +
                "WHERE {\n" +
                "?docIdentifier <http://erlangen-crm.org/200717/P102_has_title> ?type.\n" +
                "?type <http://www.episa.inesctec.pt/ligacao#hasValue> ?title_type.\n" +
                "?title_type <http://www.episa.inesctec.pt/data_object#stringValue> ?title.\n" +
                "?docIdentifier <http://erlangen-crm.org/200717/has_uuid> ?episaIdentifier .\n" +
                "?docIdentifier <http://erlangen-crm.org/200717/P1_is_identified_by> ?cidoc_identifier.\n" +
                "?cidoc_identifier <http://www.episa.inesctec.pt/ligacao#hasValue> ?identifier_value.\n" +
                "?identifier_value <http://www.episa.inesctec.pt/data_object#stringValue> ?dglabIdentifier.\n" +
                "?cidoc_identifier <http://erlangen-crm.org/200717/P2_has_type> ?p2hastype.\n" +
                "?docIdentifier <http://www.semanticweb.org/dmelo/ontologies/2020/7/untitled-ontology-151#ARP12_has_level_of_description> ?descriptionLevel .\n" +
                "?descriptionLevel <http://www.w3.org/2000/01/rdf-schema#label> ?descriptionLevelString .\n";

        if (refCode != null) {
            myQuery += "?identifier_value <http://www.episa.inesctec.pt/data_object#stringValue>" + refCode + ".\n";
        }
        if (title != null) {
            myQuery += " FILTER regex(?title," + title + ", \"i\")\n";
        }
        if (descriptionLevel != null) {
            myQuery += "?descriptionLevel <http://www.w3.org/2000/01/rdf-schema#label> " + descriptionLevel + " .\n";
        }

        myQuery += "}";
        System.out.println(myQuery);
        return QueryFactory.create(myQuery);
    }

    public String deleteDoc(String uuid) {
        String myQuery = "DELETE " +
                "WHERE {\n" +
                "?docIdentifier <http://erlangen-crm.org/200717/P102_has_title> ?type.\n" +
                "?type <http://www.episa.inesctec.pt/ligacao#hasValue> ?title_type.\n" +
                "?title_type <http://www.episa.inesctec.pt/data_object#stringValue> ?title.\n" +
                "?docIdentifier <http://erlangen-crm.org/200717/has_uuid> \"" + uuid + "\".\n" +
                "?docIdentifier <http://erlangen-crm.org/200717/P1_is_identified_by> ?cidoc_identifier.\n" +
                "?cidoc_identifier <http://www.episa.inesctec.pt/ligacao#hasValue> ?identifier_value.\n" +
                "?identifier_value <http://www.episa.inesctec.pt/data_object#stringValue> ?dglabIdentifier.\n" +
                "?docIdentifier  <http://www.semanticweb.org/dmelo/ontologies/2020/7/untitled-ontology-151#ARP12_has_level_of_description> ?descriptionLevel .\n" +
                "}";
        System.out.println(myQuery);
        return myQuery;
    }

    public String deleteSomeInformationDoc(String docId) {
        String myQuery = "DELETE " +
                "WHERE {\n" +
                "<" + docId + "> <http://erlangen-crm.org/200717/P102_has_title> ?type.\n" +
                "?type <http://www.episa.inesctec.pt/ligacao#hasValue> ?title_type.\n" +
                "?title_type <http://www.episa.inesctec.pt/data_object#stringValue> ?title.\n" +


                "<" + docId + "> <http://erlangen-crm.org/200717/P1_is_identified_by> ?cidoc_identifier.\n" +
                "?cidoc_identifier <http://www.episa.inesctec.pt/ligacao#hasValue> ?identifier_value.\n" +
                "?identifier_value <http://www.episa.inesctec.pt/data_object#stringValue> ?dglabIdentifier.\n" +

                "<" + docId + "> <http://www.semanticweb.org/dmelo/ontologies/2020/7/untitled-ontology-151#ARP12_has_level_of_description> ?descriptionLevel .\n" +
                "}";
        System.out.println(myQuery);
        return myQuery;
    }


    public Query insertTitle_query(String uuid) {
        return QueryFactory.create("Insert ?description\n" +
                "WHERE {\n" +
                uuid + " <http://erlangen-crm.org/200717/P102_has_title> ?type .\n" +
                "  ?type <http://www.episa.inesctec.pt/ligacao#hasValue> ?title_type .\n" +
                "  ?title_type <http://www.episa.inesctec.pt/data_object#stringValue> ?description\n" +
                "}");
    }

    public Query getLevel_of_description_query(String uuid) {
        return QueryFactory.create("SELECT ?descriptionLevel\n" +
                "WHERE {\n" +
                "?DocId <http://erlangen-crm.org/200717/has_uuid> \"" + uuid + "\".\n" +

                "?DocId <http://www.semanticweb.org/dmelo/ontologies/2020/7/untitled-ontology-151#ARP12_has_level_of_description> ?hasDescriptionLevel .\n" +
                "?hasDescriptionLevel <http://www.w3.org/2000/01/rdf-schema#label> ?descriptionLevel \n" +
                "}");
    }

    public Query getUuid(String docUuid) {
        return QueryFactory.create("SELECT ?Uuid\n" +
                "WHERE {\n" +
                docUuid + " <http://erlangen-crm.org/200717/has_uuid> ?Uuid\n" +
                "}");
    }

    public Query getDocId(String uuid) {
        return QueryFactory.create("SELECT ?docUuid\n" +
                "WHERE {\n" +
                "?docUuid  <http://erlangen-crm.org/200717/has_uuid> \"" + uuid + "\".\n" +
                "}");
    }

    public Query getAllUuids() {
        return QueryFactory.create("SELECT ?description\n" +
                "WHERE {\n" +
                "?a <http://erlangen-crm.org/200717/has_uuid> ?description\n" +
                "}");
    }

    public Query getAllMater() {
        return QueryFactory.create("SELECT ?description\n" +
                "WHERE {\n" +
                "?a <http://erlangen-crm.org/200717/has_material> ?description\n" +
                "}");
    }


    public Query getIdFromRelDoc(String uuid) {
        return QueryFactory.create("SELECT ?description \n" +
                "WHERE {\n" +
                "?description <http://erlangen-crm.org/200717/has_related_document> ?tdoc .\n" +
                "?tdoc <http://erlangen-crm.org/200717/has_uuid> \"" + uuid + "\".\n" +
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
        String myString = "SELECT  ?identifier ?type \n" +
                "WHERE {\n" +
                "?DocId <http://erlangen-crm.org/200717/has_uuid> \"" + uuid + "\".\n" +
                "?DocId <http://erlangen-crm.org/200717/P1_is_identified_by> ?cidoc_identifier .\n" +
                "?cidoc_identifier <http://www.episa.inesctec.pt/ligacao#hasValue> ?identifier_value .\n" +
                "?cidoc_identifier <http://erlangen-crm.org/200717/P2_has_type> ?type.\n" +
                "?identifier_value <http://www.episa.inesctec.pt/data_object#stringValue> ?identifier\n" +
                "}";
        return QueryFactory.create(myString);
    }

    public Query getTitle(String uuid) {
        String query = "SELECT ?title ?type \n" +
                "WHERE {\n" +
                "?DocId <http://erlangen-crm.org/200717/has_uuid> \"" + uuid + "\".\n" +
                "?DocId <http://erlangen-crm.org/200717/P102_has_title> ?type .\n" +
                "?type <http://www.episa.inesctec.pt/ligacao#hasValue> ?typen .\n" +
                "?typen <http://www.episa.inesctec.pt/data_object#stringValue> ?title\n" +
                "}";
        System.out.println(query);
        return QueryFactory.create(query);
    }


    public Query getMaterial(String uuid) {
        return QueryFactory.create("SELECT ?material ?component\n" +
                "WHERE {\n" +
                "?DocId <http://erlangen-crm.org/200717/has_uuid> \"" + uuid + "\".\n" +
                "?DocId  <http://erlangen-crm.org/200717/has_material> ?material .\n" +
                "?DocId  <http://erlangen-crm.org/200717/has_material> ?component\n" +
                "}");
    }

    public Query getDimension(String uuid) {
        return QueryFactory.create("SELECT ?dimension ?value ?measurementUnit ?component\n" +
                "WHERE {\n" +
                "?DocId <http://erlangen-crm.org/200717/has_uuid> \"" + uuid + "\".\n" +
                "?DocId <http://erlangen-crm.org/200717/has_dimension> ?dimension .\n" +
                "?DocId <http://erlangen-crm.org/200717/has_dimension_value> ?value .\n" +
                "?DocId <http://erlangen-crm.org/200717/has_dimension_measurement_unit> ?measurementUnit .\n" +
                "?DocId <http://erlangen-crm.org/200717/has_dimension_component> ?component\n" +
                "}");
    }

    public Query getQuantity(String uuid) {
        return QueryFactory.create("SELECT ?quantity ?value ?measurementUnit ?component\n" +
                "WHERE {\n" +
                "?DocId <http://erlangen-crm.org/200717/has_uuid> \"" + uuid + "\".\n" +
                "?DocId <http://erlangen-crm.org/200717/has_quantity> ?quantity .\n" +
                "?DocId <http://erlangen-crm.org/200717/has_quantity_value> ?value .\n" +
                "?DocId <http://erlangen-crm.org/200717/has_quantity_measurement_unit> ?measurementUnit .\n" +
                "?DocId <http://erlangen-crm.org/200717/has_quantity_component> ?component\n" +
                "}");
    }

    public Query getConservationStatus(String uuid) {
        return QueryFactory.create("SELECT ?conservationStatus ?initialDate ?finalDate \n" +
                "WHERE {\n" +
                "?DocId <http://erlangen-crm.org/200717/has_uuid> \"" + uuid + "\".\n" +
                "?DocId <http://erlangen-crm.org/200717/has_conservation_status> ?conservationStatus .\n" +
                "?DocId <http://erlangen-crm.org/200717/has_conservation_status_ID> ?initialDate .\n" +
                "?DocId <http://erlangen-crm.org/200717/has_conservation_status_FD> ?finalDate \n" +
                "}");
    }

    public Query getLanguage(String uuid) {
        return QueryFactory.create("SELECT ?language ?identifier\n" +
                "WHERE {\n" +
                "?DocId <http://erlangen-crm.org/200717/has_uuid> \"" + uuid + "\".\n" +
                "?DocId <http://erlangen-crm.org/200717/has_language> ?language .\n" +
                "?DocId <http://erlangen-crm.org/200717/has_language_identifier> ?identifier\n" +
                "}");
    }

    public Query getAccessCondition(String uuid) {
        return QueryFactory.create("SELECT ?accessConditions ?justification\n" +
                "WHERE {\n" +
                "?DocId <http://erlangen-crm.org/200717/has_uuid> \"" + uuid + "\".\n" +
                "?DocId <http://erlangen-crm.org/200717/has_access_condition> ?accessConditions .\n" +
                "?DocId <http://erlangen-crm.org/200717/has_access_condition_justification> ?justification\n" +
                "}");
    }


    public Query getWriting(String uuid) {
        return QueryFactory.create("SELECT ?writing ?identifier\n" +
                "WHERE {\n" +
                "?DocId <http://erlangen-crm.org/200717/has_uuid> \"" + uuid + "\".\n" +
                "?DocId <http://erlangen-crm.org/200717/has_writing> ?writing .\n" +
                "?DocId  <http://erlangen-crm.org/200717/has_writing_identifier> ?identifier\n" +
                "}");
    }

    public Query getDocTradition(String uuid) {
        return QueryFactory.create("SELECT ?documentaryTradition\n" +
                "WHERE {\n" +
                "?DocId <http://erlangen-crm.org/200717/has_uuid> \"" + uuid + "\".\n" +
                "?DocId <http://erlangen-crm.org/200717/has_doc_tradition> ?documentaryTradition \n" +
                "}");
    }

    public Query getDocTypology(String uuid) {
        return QueryFactory.create("SELECT ?documentaryTypology\n" +
                "WHERE {\n" +
                "?DocId <http://erlangen-crm.org/200717/has_uuid> \"" + uuid + "\".\n" +
                "?DocId <http://erlangen-crm.org/200717/has_typology> ?documentaryTypology \n" +
                "}");
    }

    public Query getSubject(String uuid) {
        return QueryFactory.create("SELECT ?subject\n" +
                "WHERE {\n" +
                "?DocId <http://erlangen-crm.org/200717/has_uuid> \"" + uuid + "\".\n" +
                "?DocId <http://erlangen-crm.org/200717/has_subject> ?subject \n" +
                "}");
    }


    public Query getReproductionCondition(String uuid) {
        return QueryFactory.create("SELECT ?reproductionConditions ?justification\n" +
                "WHERE {\n" +
                "?DocId <http://erlangen-crm.org/200717/has_uuid> \"" + uuid + "\".\n" +
                "?DocId <http://erlangen-crm.org/200717/has_reproduction_condition> ?reproductionConditions .\n" +
                "?DocId <http://erlangen-crm.org/200717/has_reproduction_condition_justification> ?justification\n" +
                "}");
    }

    public Query getRelatedEvent(String uuid) {
        return QueryFactory.create("SELECT ?episaIdentifier ?eventType ?initialDate ?finalDate\n" +
                "WHERE {\n" +
                "?DocId <http://erlangen-crm.org/200717/has_uuid> \"" + uuid + "\".\n" +
                "?DocId <http://erlangen-crm.org/200717/has_related_event> ?episaIdentifier .\n" +
                "?DocId <http://erlangen-crm.org/200717/has_related_event_type> ?eventType .\n" +
                "?DocId <http://erlangen-crm.org/200717/has_related_event_id> ?initialDate .\n" +
                "?DocId <http://erlangen-crm.org/200717/has_related_event_fd> ?finalDate\n" +
                "}");
    }

    public Query getRelatedDoc(String uuid) {
        return QueryFactory.create("SELECT ?episaIdentifier ?dglabIdentifier  ?title ?relationType\n" +
                "WHERE {\n" +
                "?DocId <http://erlangen-crm.org/200717/has_uuid> \"" + uuid + "\".\n" +
                "?DocId <http://erlangen-crm.org/200717/has_related_document> ?tdoc .\n" +
                "?tdoc <http://erlangen-crm.org/200717/has_uuid> ?episaIdentifier .\n" +
                "?tdoc <http://erlangen-crm.org/200717/P1_is_identified_by> ?cidoc_identifier .\n" +
                "?cidoc_identifier <http://www.episa.inesctec.pt/ligacao#hasValue> ?identifier_value .\n" +
                "?identifier_value <http://www.episa.inesctec.pt/data_object#stringValue> ?dglabIdentifier .\n" +
                "?tdoc <http://erlangen-crm.org/200717/P102_has_title> ?type .\n" +
                "?type <http://www.episa.inesctec.pt/ligacao#hasValue> ?title_type .\n" +
                "?title_type <http://www.episa.inesctec.pt/data_object#stringValue> ?title .\n" +
                "?DocId ?relationType ?tdoc \n" +
                "}");
    }

    public Query getAllLevelOfDescription() {
        return QueryFactory.create("SELECT  DISTINCT ?descriptionLevel\n" +
                "WHERE {\n" +
                "?subject <http://www.semanticweb.org/dmelo/ontologies/2020/7/untitled-ontology-151#ARP12_has_level_of_description> ?object .\n" +
                "?object <http://www.w3.org/2000/01/rdf-schema#label> ?descriptionLevel\n" +
                "}");
    }
}
