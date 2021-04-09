package operations;

import org.apache.jena.rdf.model.Model;
import org.apache.jena.rdf.model.Property;
import org.apache.jena.rdf.model.Resource;
import org.apache.jena.rdfconnection.RDFConnectionFuseki;
import org.apache.jena.rdfconnection.RDFConnectionRemoteBuilder;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.UUID;

public class Insert {

    public String destination_port;


    public Insert(String destination_port) {
        this.destination_port = destination_port + "name/data";
    }

    public void insert(HashMap<String, ArrayList<HashMap<String, String>>> mapper) {
        RDFConnectionRemoteBuilder builder = RDFConnectionFuseki.create()
                .destination(this.destination_port);


        try (RDFConnectionFuseki conn = (RDFConnectionFuseki) builder.build()) {
            Model model = conn.fetch();

            // create the resource
            Resource Docres = model.getResource("http://erlangen-crm.org/200717/E31_Document");
            Resource Idres = model.getResource("http://erlangen-crm.org/200717/E42_Identifier");



            Resource res = model.createResource("http://erlangen-crm.org/200717/" + UUID.randomUUID().toString(),Docres);


            Property testprop = model.createProperty("http://erlangen-crm.org/200717/", "has_uuid");
            UUID uuid = UUID.randomUUID();
            String uuidAsString = uuid.toString();
            res.addProperty(testprop, uuidAsString);

            Resource Stringres = model.getResource("http://www.episa.inesctec.pt/data_object#String");

            Resource FormalTitlegres = model.getResource("http://www.semanticweb.org/dmelo/ontologies/2020/7/untitled-ontology-151#ARE2FormalTitle");
            Resource SuppliedTitlegres = model.getResource("http://www.semanticweb.org/dmelo/ontologies/2020/7/untitled-ontology-151#ARE3SuppliedTitle");

            Resource RefCoderes = model.getResource("http://www.semanticweb.org/dmelo/ontologies/2020/7/untitled-ontology-151#Reference_code");




            Property materialProperty = model.createProperty("http://erlangen-crm.org/200717/", "has_material");
            Property materialPropertyType = model.createProperty("http://erlangen-crm.org/200717/", "has_material_type");

            Property dimensionProperty = model.createProperty("http://erlangen-crm.org/200717/", "has_dimension");
            Property dimensionPropertyValue = model.createProperty("http://erlangen-crm.org/200717/", "has_dimension_value");
            Property dimensionPropertyMU = model.createProperty("http://erlangen-crm.org/200717/", "has_dimension_measurement_unit");
            Property dimensionPropertyComponent = model.createProperty("http://erlangen-crm.org/200717/", "has_dimension_component");


            Property quantityProperty = model.createProperty("http://erlangen-crm.org/200717/", "has_quantity");
            Property quantityPropertyValue = model.createProperty("http://erlangen-crm.org/200717/", "has_quantity_value");
            Property quantityPropertyMU = model.createProperty("http://erlangen-crm.org/200717/", "has_quantity_measurement_unit");
            Property quantityPropertyComponent = model.createProperty("http://erlangen-crm.org/200717/", "has_quantity_component");


            Property conservationProperty = model.createProperty("http://erlangen-crm.org/200717/", "has_conservation_status");
            Property conservationIDProperty = model.createProperty("http://erlangen-crm.org/200717/", "has_conservation_status_ID");
            Property conservationFDProperty = model.createProperty("http://erlangen-crm.org/200717/", "has_conservation_status_FD");


            Property languageProperty = model.createProperty("http://erlangen-crm.org/200717/", "has_language");
            Property languageIdentifierProperty = model.createProperty("http://erlangen-crm.org/200717/", "has_language_identifier");

            Property writingProperty = model.createProperty("http://erlangen-crm.org/200717/", "has_writing");
            Property writingPropertyIdentifier = model.createProperty("http://erlangen-crm.org/200717/", "has_writing_identifier");

            Property docProperty = model.createProperty("http://erlangen-crm.org/200717/", "has_doc_tradition");

            Property typologyProperty = model.createProperty("http://erlangen-crm.org/200717/", "has_typology");

            Property subjectProperty = model.createProperty("http://erlangen-crm.org/200717/", "has_subject");

            Property accessConditionProperty = model.createProperty("http://erlangen-crm.org/200717/", "has_access_condition");
            Property accessConditionJustifificationProperty = model.createProperty("http://erlangen-crm.org/200717/", "has_access_condition_justification");

            Property refProperty = model.createProperty("http://erlangen-crm.org/200717/", "P2_has_type");
            Property identificationProperty = model.createProperty("http://erlangen-crm.org/200717/", "P1_is_identified_by");
            Property titleProperty = model.createProperty("http://erlangen-crm.org/200717/", "P102_has_title");

            Property stringProperty = model.createProperty("http://www.episa.inesctec.pt/", "ligacao#hasValue");

            Property stringValueProperty = model.createProperty("http://www.episa.inesctec.pt/", "data_object#stringValue");


            Property relatedDocumentProperty = model.createProperty("http://erlangen-crm.org/200717/", "has_related_document");


            // add the property


            ArrayList<HashMap<String,String>> titlemaparray = mapper.get("titles");
            ArrayList<HashMap<String,String>> identifiermaparray = mapper.get("identifiers");
            ArrayList<HashMap<String,String>> materialmaparray = mapper.get("materials");
            ArrayList<HashMap<String,String>> dimensionsmaparray = mapper.get("dimensions");
            ArrayList<HashMap<String,String>> quantitiesmaparray = mapper.get("quantities");
            ArrayList<HashMap<String,String>> conservationStatesmaparray = mapper.get("conservationStates");
            ArrayList<HashMap<String,String>> languagesmaparray = mapper.get("languages");
            ArrayList<HashMap<String,String>> writingsmaparray = mapper.get("writings");
            ArrayList<HashMap<String,String>> documentaryTraditionsmaparray = mapper.get("documentaryTraditions");
            ArrayList<HashMap<String,String>> typologiesmaparray = mapper.get("typologies");
            ArrayList<HashMap<String,String>> subjectsmaparray = mapper.get("subjects");
            ArrayList<HashMap<String,String>> accessConditionsmaparray = mapper.get("accessConditions");
            ArrayList<HashMap<String,String>> relatedDocsmaparray = mapper.get("relatedDocs");

            if(titlemaparray != null)
            for (HashMap<String,String> map : titlemaparray)
            {

                Resource TitleRes = null;
                if(map.get("type").equals("Supplied Title")){
                    TitleRes = model.createResource(SuppliedTitlegres);
                }
                else if(map.get("type").equals("Formal Title")){
                    TitleRes = model.createResource(FormalTitlegres);
                }

                if(TitleRes != null){
                    Resource StringRes = model.createResource(Stringres);

                    TitleRes.addProperty(stringProperty, StringRes);
                    StringRes.addProperty(stringValueProperty,map.get("title"));
                    res.addProperty(titleProperty,TitleRes);
                }
            }

            if(identifiermaparray != null)
            for (HashMap<String,String> map : identifiermaparray)
            {
                Resource IdentifierRes = model.createResource(Idres);


                if(map.get("type").equals("Reference Code")){
                    Resource RefCode = model.createResource(RefCoderes);
                    IdentifierRes.addProperty(refProperty, RefCode);

                }
                Resource StringRes = model.createResource(Stringres);

                IdentifierRes.addProperty(stringProperty, StringRes);
                StringRes.addProperty(stringValueProperty,map.get("identifier"));
                res.addProperty(identificationProperty,IdentifierRes);

            }

            if(materialmaparray != null)
            for (HashMap<String,String> map : materialmaparray)
            {
                res.addProperty(materialProperty, map.get("material"));
                res.addProperty(materialPropertyType, map.get("component"));
            }

            if(dimensionsmaparray != null)
            for (HashMap<String,String> map : dimensionsmaparray)
            {
                res.addProperty(dimensionProperty, map.get("dimension"));
                res.addProperty(dimensionPropertyValue, map.get("value"));
                res.addProperty(dimensionPropertyMU, map.get("measurementUnit"));
                res.addProperty(dimensionPropertyComponent, map.get("component"));
            }

            if(quantitiesmaparray != null)
            for (HashMap<String,String> map : quantitiesmaparray)
            {
                res.addProperty(quantityProperty, map.get("dimension"));
                res.addProperty(quantityPropertyValue, map.get("value"));
                res.addProperty(quantityPropertyMU, map.get("measurementUnit"));
                res.addProperty(quantityPropertyComponent, map.get("component"));
            }

            if(conservationStatesmaparray != null)
            for (HashMap<String,String> map : conservationStatesmaparray)
            {
                res.addProperty(conservationProperty, map.get("conservationStatus"));
                res.addProperty(conservationIDProperty, map.get("initialDate"));
                res.addProperty(conservationFDProperty, map.get("finalDate"));
            }

            if(languagesmaparray != null)
            for (HashMap<String,String> map : languagesmaparray)
            {
                res.addProperty(languageProperty, map.get("language"));
                res.addProperty(languageIdentifierProperty, map.get("identifier"));
            }

            if(writingsmaparray != null)
            for (HashMap<String,String> map : writingsmaparray)
            {
                res.addProperty(writingProperty, map.get("writing"));
                res.addProperty(writingPropertyIdentifier, map.get("identifier"));
            }

            if(documentaryTraditionsmaparray != null)
            for (HashMap<String,String> map : documentaryTraditionsmaparray)
            {

                res.addProperty(docProperty, map.get("documentaryTradition"));
            }

            if(typologiesmaparray != null)
            for (HashMap<String,String> map : typologiesmaparray)
            {

                res.addProperty(typologyProperty, map.get("documentaryTypology"));
            }

            if(subjectsmaparray != null)
            for (HashMap<String,String> map : subjectsmaparray)
            {

                res.addProperty(subjectProperty, map.get("subject"));
            }

            if(accessConditionsmaparray != null)
            for (HashMap<String,String> map : accessConditionsmaparray)
            {
                res.addProperty(accessConditionProperty, map.get("accessCondition"));
                res.addProperty(accessConditionJustifificationProperty, map.get("justification"));
            }

            if(relatedDocsmaparray != null)
            for (HashMap<String,String> map : relatedDocsmaparray)
            {
                res.addProperty(relatedDocumentProperty, map.get("recordIdentifier"));
            }

            conn.put(model);
            conn.commit();
        }
    }

}
