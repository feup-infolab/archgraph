package operations;

import org.apache.jena.query.Query;
import org.apache.jena.query.QueryFactory;
import utils.Properties;

public class Queries {
    private final Properties properties;


    public Queries() {
        this.properties = new Properties();
    }

    public Query getAllLevelOfDescription() {
        String query = "SELECT  DISTINCT ?descriptionLevel\n" +
                "WHERE {\n" +
                "?descriptionLevel ?object <" + properties.getARE1LevelOfDescription() + "> .\n" +
                "}";
        System.out.println(query);
        return QueryFactory.create(query);
    }

    public Query getHeaderSummaryDoc(String refCode, String descriptionLevel, String title) {
        String myQuery = "SELECT distinct ?episaIdentifier ?dglabIdentifier ?physicalLocation\n" +
                "WHERE {\n" +
                "?DocId <" + properties.getP102HasTitle() + "> ?type.\n" +
                "?type <" + properties.getHasValue() + "> ?title_type.\n" +
                "?title_type <" + properties.getStringValue() + "> ?title.\n" +

                "OPTIONAL \n" +
                " { ?DocId <" + properties.getP1IsIdentifiedBy() + "> ?physicalLocationIdentifier .\n" +
                "?physicalLocationIdentifier <" + properties.getP2HasType() + "> <" + properties.getPhysicalLocation() + ">.\n" +
                "?physicalLocationIdentifier <" + properties.getStringValue() + "> ?physicalLocation.\n }" +

                "?DocId <" + properties.getHasUuid() + "> ?episaIdentifier.\n" +
                "?DocId <" + properties.getP1IsIdentifiedBy() + "> ?dglabIdentifier.\n" +
                "?dglabIdentifier <" + properties.getP2HasType() + "> <" + properties.getReferenceCode() + ">.\n" +
                "?DocId <" + properties.getARP12HasDescriptionLevel() + "> ?descriptionLevel.\n";
        if (refCode != null) {
            myQuery += "?DocId <" + properties.getP1IsIdentifiedBy() + "> <" + properties.getTitleOntology() + refCode + ">.\n";
        }
        if (title != null) {
            myQuery += " FILTER regex(?title,\"" + title + "\", \"i\")\n";
        }
        if (descriptionLevel != null) {
            myQuery += "?DocId <" + properties.getARP12HasDescriptionLevel() + "> <" + properties.getPropertyWithNameSpace(descriptionLevel) + ">.\n";
        }
        myQuery += "}";
        System.out.println(myQuery);
        return QueryFactory.create(myQuery);
    }

    public Query getTitles(String episaIdentifier, String dglabIdentifier) {
        String myQuery = "SELECT distinct ?title \n" +
                "WHERE {\n" +
                "?DocId <" + properties.getP102HasTitle() + "> ?type.\n" +
                "?type <" + properties.getHasValue() + "> ?title_type.\n" +
                "?title_type <" + properties.getStringValue() + "> ?title.\n" +
                "?DocId <" + properties.getHasUuid() + "> \"" + episaIdentifier + "\".\n" +
                "?DocId <" + properties.getP1IsIdentifiedBy() + "> <" + dglabIdentifier + ">.\n" +
                "}";
        System.out.println(myQuery);
        return QueryFactory.create(myQuery);
    }

    public Query getLevel_of_description_query(String uuid) {
        String myQuery = "SELECT ?descriptionLevel ?" + properties.getMyEntityUuid() + "\n" +
                "WHERE {\n" +
                "?DocId <" + properties.getHasUuid() + "> \"" + uuid + "\".\n" +
                "?DocId <" + properties.getARP12HasDescriptionLevel() + "> ?descriptionLevel.\n" +
                "?DocId <" + properties.getARP12HasDescriptionLevel() + "> ?" + properties.getMyEntityUuid() + ".\n" +
                "}";
        System.out.println(myQuery);
        return QueryFactory.create(myQuery);
    }


    public Query getDocId(String uuid) {
        return QueryFactory.create("SELECT ?DocId\n" +
                "WHERE {\n" +
                "?DocId  <" + properties.getHasUuid() + "> \"" + uuid + "\".\n" +
                "}");
    }

    public Query getAllUuids() {
        return QueryFactory.create("SELECT ?description\n" +
                "WHERE {\n" +
                "?a <" + properties.getHasUuid() + "> ?description\n" +
                "}");
    }

    public Query getAllMater() {
        return QueryFactory.create("SELECT ?description\n" +
                "WHERE {\n" +
                "?a <" + properties.getNameSpace() + "has_material> ?description\n" +
                "}");
    }

    public Query getIdFromRelDoc(String uuid) {
        return QueryFactory.create("SELECT ?description \n" +
                "WHERE {\n" +
                "?description <" + properties.getNameSpace() + "has_related_document> ?tdoc .\n" +
                "?tdoc <" + properties.getHasUuid() + "> \"" + uuid + "\".\n" +
                "}");
    }

    public Query getPerson(String uuid) {
        return QueryFactory.create("SELECT ?name\n" +
                "WHERE {\n" +
                uuid + "<" + properties.getP1IsIdentifiedBy() + "> ?object.\n" +
                "  ?object <" + properties.getHasValue() + "> ?object2.\n" +
                "  ?object2 <" + properties.getStringValue() + "> ?name \n" +
                "}");
    }

    public Query getPlace(String uuid) {
        return QueryFactory.create("SELECT ?name \n" +
                "WHERE {\n" +
                uuid + "<" + properties.getP1IsIdentifiedBy() + "> ?object.\n" +
                "  ?object <" + properties.getHasValue() + "> ?object2.\n" +
                "  ?object2 <" + properties.getStringValue() + "> ?name\n" +
                "}");
    }

    public Query getAllResourcesDocs() {
        return QueryFactory.create("SELECT distinct ?subject\n" +
                "WHERE {\n" +
                "{  ?subject <" + properties.getRdfType() + "> <" + properties.getNameSpace() + "E31_Document>.}\n" +
                "}");
    }

    public Query getIdentifier(String uuid) {
        String myString = "SELECT ?identifier ?type ?" + properties.getMyEntityUuid() + "\n" +
                "WHERE {\n" +
                "?DocId <" + properties.getHasUuid() + "> \"" + uuid + "\".\n" +
                "?DocId <" + properties.getP1IsIdentifiedBy() + "> ?identifier .\n" +
                "?DocId <" + properties.getP1IsIdentifiedBy() + "> ?" + properties.getMyEntityUuid() + " .\n" +
                "?identifier <" + properties.getP2HasType() + "> <" + properties.getReferenceCode() + ">.\n" +
                "?identifier <" + properties.getP2HasType() + "> ?type.\n" +
                "FILTER ( ?identifier = ?" + properties.getMyEntityUuid() + "  )\n" +
                "}";
        System.out.println(myString);
        return QueryFactory.create(myString);
    }

    public Query getPhysicalLocation(String uuid) {
        String myString = "SELECT ?stringValue ?" + properties.getMyEntityUuid() + "\n" +
                "WHERE {\n" +
                "?DocId <" + properties.getHasUuid() + "> \"" + uuid + "\".\n" +
                "?DocId <" + properties.getP1IsIdentifiedBy() + "> ?physicalLocation .\n" +
                "?DocId <" + properties.getP1IsIdentifiedBy() + "> ?" + properties.getMyEntityUuid() + " .\n" +
                "?physicalLocation <" + properties.getP2HasType() + "> <" + properties.getPhysicalLocation() + ">.\n" +
                "?physicalLocation <" + properties.getStringValue() + "> ?stringValue.\n" +
                "FILTER ( ?" + properties.getMyEntityUuid() + " =  ?physicalLocation )\n" +
                "}";
        return QueryFactory.create(myString);
    }

    public Query getTitle(String uuid) {
        String query = "SELECT ?title ?type ?" + properties.getMyEntityUuid() + "\n" +
                "WHERE {\n" +
                "?DocId <" + properties.getHasUuid() + "> \"" + uuid + "\".\n" +
                "?DocId <" + properties.getP102HasTitle() + "> ?" + properties.getMyEntityUuid() + " .\n" +
                "?" + properties.getMyEntityUuid() + " <" + properties.getHasValue() + "> ?titleValue .\n" +
                "?" + properties.getMyEntityUuid() + " <" + properties.getRdfType() + ">  ?type.\n" +
                "?titleValue <" + properties.getStringValue() + "> ?title\n" +
                "FILTER ( ?type !=  <" + properties.getNamedIndividual() + ">  )\n" +
                "}";
        System.out.println(query);
        return QueryFactory.create(query);
    }

    public Query getMaterial(String uuid) {
        return QueryFactory.create("SELECT ?material ?component\n" +
                "WHERE {\n" +
                "?DocId <" + properties.getHasUuid() + "> \"" + uuid + "\".\n" +
                "?DocId  <" + properties.getNameSpace() + "has_material> ?material .\n" +
                "?DocId  <" + properties.getNameSpace() + "has_material> ?component\n" +
                "}");
    }
    public Query getPhysicalCharacteristicsTechnicalRequirements (String uuid) {
        return QueryFactory.create("SELECT ?physicalCharacteristics ?" + properties.getMyEntityUuid() + "\n" +
                "WHERE {\n" +
                "?DocId <" + properties.getHasUuid() + "> \"" + uuid + "\".\n" +
                "?DocId  <" + properties.getPhysicalCharacteristicsTechnicalRequirements() + "> ?physicalCharacteristics .\n" +
                "}");
    }

    public Query getDimension(String uuid) {
        String query = "SELECT ?material ?value ?measurementUnit ?" + properties.getMyEntityUuid() + "\n" +
                "WHERE {\n" +
                "?DocId <" + properties.getHasUuid() + "> \"" + uuid + "\".\n" +
                "?DocId <" + properties.getP128IsCarriedBy() + "> ?" + properties.getMyEntityUuid() + ".\n" +
                "?" + properties.getMyEntityUuid() + " <" + properties.getP45ConsistsOf() + "> ?material.\n" +
                "?" + properties.getMyEntityUuid() + " <" + properties.getP43HasDimension() + "> ?dimension.\n" +
                "?dimension <" + properties.getP90HasValue() + "> ?value .\n" +
                "?dimension <" + properties.getP91HasUnit() + "> ?measurementUnit.\n" +
                "}";
        System.out.println(query);
        return QueryFactory.create(query);
    }


    public Query getQuantity(String uuid) {
        return QueryFactory.create("SELECT ?quantity ?value ?measurementUnit ?component\n" +
                "WHERE {\n" +
                "?DocId <" + properties.getHasUuid() + "> \"" + uuid + "\".\n" +
                "?DocId <" + properties.getNameSpace() + "has_quantity> ?quantity .\n" +
                "?DocId <" + properties.getNameSpace() + "has_quantity_value> ?value .\n" +
                "?DocId <" + properties.getNameSpace() + "has_quantity_measurement_unit> ?measurementUnit .\n" +
                "?DocId <" + properties.getNameSpace() + "has_quantity_component> ?component\n" +
                "}");
    }

    public Query getConservationStatus(String uuid) {
        return QueryFactory.create("SELECT ?conservationStatus ?initialDate ?finalDate \n" +
                "WHERE {\n" +
                "?DocId <" + properties.getHasUuid() + "> \"" + uuid + "\".\n" +
                "?DocId <" + properties.getNameSpace() + "has_conservation_status> ?conservationStatus .\n" +
                "?DocId <" + properties.getNameSpace() + "has_conservation_status_ID> ?initialDate .\n" +
                "?DocId <" + properties.getNameSpace() + "has_conservation_status_FD> ?finalDate \n" +
                "}");
    }

    public Query getLanguage(String uuid) {
        return QueryFactory.create("SELECT ?language ?identifier\n" +
                "WHERE {\n" +
                "?DocId <" + properties.getHasUuid() + "> \"" + uuid + "\".\n" +
                "?DocId <" + properties.getNameSpace() + "has_language> ?language .\n" +
                "?DocId <" + properties.getNameSpace() + "has_language_identifier> ?identifier\n" +
                "}");
    }

    public Query getAccessCondition(String uuid) {
        return QueryFactory.create("SELECT ?accessConditions ?justification\n" +
                "WHERE {\n" +
                "?DocId <" + properties.getHasUuid() + "> \"" + uuid + "\".\n" +
                "?DocId <" + properties.getNameSpace() + "has_access_condition> ?accessConditions .\n" +
                "?DocId <" + properties.getNameSpace() + "has_access_condition_justification> ?justification\n" +
                "}");
    }

    public Query getWriting(String uuid) {
        return QueryFactory.create("SELECT ?writing ?identifier\n" +
                "WHERE {\n" +
                "?DocId <" + properties.getHasUuid() + "> \"" + uuid + "\".\n" +
                "?DocId <" + properties.getNameSpace() + "has_writing> ?writing .\n" +
                "?DocId  <" + properties.getNameSpace() + "has_writing_identifier> ?identifier\n" +
                "}");
    }

    public Query getDocTradition(String uuid) {
        return QueryFactory.create("SELECT ?documentaryTradition\n" +
                "WHERE {\n" +
                "?DocId <" + properties.getHasUuid() + "> \"" + uuid + "\".\n" +
                "?DocId <" + properties.getNameSpace() + "has_doc_tradition> ?documentaryTradition \n" +
                "}");
    }

    public Query getDocTypology(String uuid) {
        return QueryFactory.create("SELECT ?documentaryTypology\n" +
                "WHERE {\n" +
                "?DocId <" + properties.getHasUuid() + "> \"" + uuid + "\".\n" +
                "?DocId <" + properties.getNameSpace() + "has_typology> ?documentaryTypology \n" +
                "}");
    }

    public Query getSubject(String uuid) {
        return QueryFactory.create("SELECT ?subject\n" +
                "WHERE {\n" +
                "?DocId <" + properties.getHasUuid() + "> \"" + uuid + "\".\n" +
                "?DocId <" + properties.getNameSpace() + "has_subject> ?subject \n" +
                "}");
    }

    public Query getReproductionCondition(String uuid) {
        return QueryFactory.create("SELECT ?reproductionConditions ?justification\n" +
                "WHERE {\n" +
                "?DocId <" + properties.getHasUuid() + "> \"" + uuid + "\".\n" +
                "?DocId <" + properties.getNameSpace() + "has_reproduction_condition> ?reproductionConditions .\n" +
                "?DocId <" + properties.getNameSpace() + "has_reproduction_condition_justification> ?justification\n" +
                "}");
    }

    public Query getRelatedEvent(String uuid) {
        return QueryFactory.create("SELECT ?episaIdentifier ?eventType ?initialDate ?finalDate\n" +
                "WHERE {\n" +
                "?DocId <" + properties.getHasUuid() + "> \"" + uuid + "\".\n" +
                "?DocId <" + properties.getNameSpace() + "has_related_event> ?episaIdentifier .\n" +
                "?DocId <" + properties.getNameSpace() + "has_related_event_type> ?eventType .\n" +
                "?DocId <" + properties.getNameSpace() + "has_related_event_id> ?initialDate .\n" +
                "?DocId <" + properties.getNameSpace() + "has_related_event_fd> ?finalDate\n" +
                "}");
    }

    public Query getRelatedDoc(String uuid) {
        return QueryFactory.create("SELECT ?episaIdentifier ?dglabIdentifier  ?title ?relationType\n" +
                "WHERE {\n" +
                "?DocId <" + properties.getHasUuid() + "> \"" + uuid + "\".\n" +
                "?DocId <" + properties.getNameSpace() + "has_related_document> ?tdoc .\n" +
                "?tdoc <" + properties.getHasUuid() + "> ?episaIdentifier .\n" +
                "?tdoc <" + properties.getP1IsIdentifiedBy() + "> ?cidoc_identifier .\n" +
                "?cidoc_identifier <" + properties.getHasValue() + "> ?identifier_value .\n" +
                "?identifier_value <" + properties.getStringValue() + "> ?dglabIdentifier .\n" +
                "?tdoc <" + properties.getP102HasTitle() + "> ?type .\n" +
                "?type <" + properties.getHasValue() + "> ?title_type .\n" +
                "?title_type <" + properties.getStringValue() + "> ?title .\n" +
                "?DocId ?relationType ?tdoc \n" +
                "}");
    }

    /// =========================== DELETE ==========================
    public String deleteDoc(String uuid) {
        String myQuery = "DELETE " +
                "WHERE {\n" +
                "?DocId <" + properties.getHasUuid() + "> \"" + uuid + "\".\n" +
                "?DocId <" + properties.getP102HasTitle() + "> ?myTitle.\n" +
                "?myTitle <" + properties.getRdfType() + ">  ?titleType.\n" +
                "?myTitle <" + properties.getHasValue() + "> ?StringValueProperty .\n" +
                "?StringValueProperty <" + properties.getStringValue() + "> ?stringValue.\n" +
                "?StringValueProperty <" + properties.getRdfType() + "> ?type.\n" +
                "?DocId <" + properties.getP1IsIdentifiedBy() + "> ?myIdentifier.\n" +
                "?myIdentifier <" + properties.getP2HasType() + "> ?p2HasType.\n" +
                "?myIdentifier <" + properties.getRdfType() + "> ?identifierType.\n" +

                "?DocId  <" + properties.getARP12HasDescriptionLevel() + "> ?descriptionLevel .\n" +
                "}";
        System.out.println(myQuery);
        return myQuery;
    }

    public String deleteSomeInformationDoc(String docId) {
        String myQuery = "DELETE " +
                "WHERE {\n" +
                "<" + docId + "> <" + properties.getP102HasTitle() + "> ?type.\n" +
                "?type <" + properties.getHasValue() + "> ?title_type.\n" +
                "?title_type <" + properties.getStringValue() + "> ?title.\n" +
                "<" + docId + "> <" + properties.getP1IsIdentifiedBy() + "> ?cidoc_identifier.\n" +
                "?cidoc_identifier <" + properties.getHasValue() + "> ?identifier_value.\n" +
                "?identifier_value <" + properties.getStringValue() + "> ?dglabIdentifier.\n" +

                "<" + docId + "> <" + properties.getARP12HasDescriptionLevel() + "> ?descriptionLevel .\n" +
                "}";
        System.out.println(myQuery);
        return myQuery;
    }

    //updated
    public String deleteDocTitle(String titleUuid) {
        String myQuery = "DELETE " +
                "WHERE {\n" +
                "?docId <" + properties.getP102HasTitle() + "> <" + titleUuid + "> .\n" +
                "<" + titleUuid + "> <" + properties.getRdfType() + "> ?typeTitle.\n" +
                "<" + titleUuid + "> <" + properties.getHasValue() + "> ?StringValueProperty.\n" +
                "?StringValueProperty <" + properties.getStringValue() + "> ?stringValue.\n" +
                "?StringValueProperty <" + properties.getRdfType() + "> ?type.\n" +
                "}";
        System.out.println(myQuery);
        return myQuery;
    }

    //updated
    public String deleteDocIdentifier(String identifierUuid) {
        String myQuery = "DELETE " +
                "WHERE {\n" +
                "?docId <" + properties.getP1IsIdentifiedBy() + ">  <" + identifierUuid + "> .\n" +
                "<" + identifierUuid + "> <" + properties.getP2HasType() + "> ?p2HasType.\n" +
                "<" + identifierUuid + "> <" + properties.getRdfType() + "> ?type.\n" +
                "}";
        System.out.println(myQuery);
        return myQuery;
    }

    public String deleteDocDescriptionLevel(String docId) {
        String myQuery = "DELETE \n" +
                "WHERE {\n" +
                "<" + docId + "> <" + properties.getARP12HasDescriptionLevel() + ">  ?descriptionLevel .\n" +
                "}";
        System.out.println(myQuery);
        return myQuery;
    }

    //updated
    public String deleteDocDimension(String physicalObjectUuid) {
        String myQuery = "DELETE \n" +
                "WHERE {\n" +
                " ?docId <" + properties.getP128IsCarriedBy() + ">  <" + physicalObjectUuid + "> .\n" +
                "<" + physicalObjectUuid + "> <" + properties.getP45ConsistsOf() + ">  ?material .\n" +
                "<" + physicalObjectUuid + "> <" + properties.getP43HasDimension() + ">  ?dimension .\n" +
                " ?dimension <" + properties.getRdfType() + ">  ?dimensionType .\n" +
                " ?dimension <" + properties.getP90HasValue() + ">  ?value .\n" +
                " ?dimension <" + properties.getP91HasUnit() + ">  ?myMeasurementUnit .\n" +
                " ?myMeasurementUnit <" + properties.getRdfType() + ">  ?myMeasurementUnitType .\n" +
                "}";
        System.out.println(myQuery);
        return myQuery;
    }

    /*
    PREFIX ex: <http://example.org#>
DELETE {
   ?id a ex:Example ;
       ex:name ?name .
}
WHERE {
  ?id a ex:Example ;
      ex:name ?name .
  FILTER(str(?id) != "something")
}
     */


}
