package queries;

import org.apache.jena.query.Query;
import org.apache.jena.query.QueryFactory;

public class Queries {



    public Query getGeneral_query(){
        return QueryFactory.create("SELECT * WHERE {\n" +
                "  ?sub ?pred ?obj .\n" +
                "}");
    }

    public Query getTitle_query(String uuid){
        return QueryFactory.create("SELECT  ?description\n" +
                "WHERE {\n" +
                uuid + " <http://erlangen-crm.org/200717/P102_has_title> ?type .\n" +
                "  ?type <http://www.episa.inesctec.pt/ligacao#hasValue> ?title_type .\n" +
                "  ?title_type <http://www.episa.inesctec.pt/data_object#stringValue> ?description\n" +
                "}");
    }

    public Query getLevel_of_description_query(String uuid){
        return QueryFactory.create("SELECT ?descriptionLevel\n" +
                "WHERE {\n" +
                uuid + " <http://www.semanticweb.org/dmelo/ontologies/2020/7/untitled-ontology-151#ARP12_has_level_of_description> ?descriptionLevel\n" +
                "}");
    }

    public Query getUuid(String uuid){
        return QueryFactory.create("SELECT ?description\n" +
                "WHERE {\n" +
                uuid + " <http://erlangen-crm.org/200717/has_uuid> ?description\n" +
                "}");
    }

    public Query getIDd(String uuid){
        return QueryFactory.create("SELECT ?description\n" +
                "WHERE {\n" +
                "?description <http://erlangen-crm.org/200717/has_uuid> "+ uuid +"\n" +
                "}");
    }



    public Query getReference_codes_query(String uuid){
        return QueryFactory.create("SELECT  ?description \n" +
                "WHERE {\n" +
                uuid + " <http://erlangen-crm.org/200717/P1_is_identified_by> ?cidoc_identifier .\n" +
                "  ?cidoc_identifier <http://www.episa.inesctec.pt/ligacao#hasValue> ?identifier_value .\n" +
                "  ?cidoc_identifier <http://erlangen-crm.org/200717/P2_has_type> ?type.\n" +
                "  ?identifier_value <http://www.episa.inesctec.pt/data_object#stringValue> ?description\n" +
                "}");
    }

    public Query getIdFromReference_codes_query(String refCode){
        return QueryFactory.create("SELECT  ?description \n" +
                "WHERE {\n" +
                "?description <http://erlangen-crm.org/200717/P1_is_identified_by> ?cidoc_identifier .\n" +
                "  ?cidoc_identifier <http://www.episa.inesctec.pt/ligacao#hasValue> ?identifier_value .\n" +
                "  ?cidoc_identifier <http://erlangen-crm.org/200717/P2_has_type> ?type.\n" +
                "  ?identifier_value <http://www.episa.inesctec.pt/data_object#stringValue> "+ refCode + "\n" +
                "}");
    }

    public Query getPerson(String uuid){
        return QueryFactory.create("SELECT ?name\n" +
                "WHERE {\n" +
                uuid + "<http://erlangen-crm.org/200717/P1_is_identified_by> ?object.\n" +
                "  ?object <http://www.episa.inesctec.pt/ligacao#hasValue> ?object2.\n" +
                "  ?object2 <http://www.episa.inesctec.pt/ligacao#stringValue> ?name \n" +
                "}");
    }

    public Query getPlace(String uuid){
        return QueryFactory.create("SELECT ?name \n" +
                "WHERE {\n" +
                uuid + "<http://erlangen-crm.org/200717/P1_is_identified_by> ?object.\n" +
                "  ?object <http://www.episa.inesctec.pt/ligacao#hasValue> ?object2.\n" +
                "  ?object2 <http://www.episa.inesctec.pt/ligacao#stringValue> ?name\n" +
                "}");
    }

    public Query getAllDocs(){
        return QueryFactory.create("SELECT ?subject\n" +
                "WHERE {\n" +
                "  ?subject <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://erlangen-crm.org/200717/E31_Document>\n" +
                "}");
    }

    public Query insertUuid(String olduuid, String uuid){
        return QueryFactory.create("INSERT {\n" +
                  olduuid + "<has_uuid> \""+ uuid +"\" \n" +
                " }");
    }





}
