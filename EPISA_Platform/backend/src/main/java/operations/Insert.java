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


    public String sparqlHost;
    public String dataHost;

    public Insert(String sparqlHost, String dataHost) {
        this.sparqlHost = sparqlHost;
        this.dataHost = dataHost;
        System.out.println("ola");
    }

    public void insert(HashMap<String, HashMap<String, ArrayList<HashMap<String, String>>>> mapper) {
        RDFConnectionRemoteBuilder builder = RDFConnectionFuseki.create()
                .destination(this.dataHost);


        try (RDFConnectionFuseki conn = (RDFConnectionFuseki) builder.build()) {
            Model model = conn.fetch();
            Properties properties = new Properties(model);
            properties.createProperties();

            // create the resource
            Resource Docres = model.getResource("http://erlangen-crm.org/200717/E31_Document");
            Resource Idres = model.getResource("http://erlangen-crm.org/200717/E42_Identifier");


            Resource res = model.createResource("http://erlangen-crm.org/200717/" + UUID.randomUUID().toString(), Docres);


            Property uuindProperty = model.createProperty("http://erlangen-crm.org/200717/", "has_uuid");
            UUID uuid = UUID.randomUUID();
            String uuidAsString = uuid.toString();
            res.addProperty(uuindProperty, uuidAsString);

            Resource Stringres = model.getResource("http://www.episa.inesctec.pt/data_object#String");

            Resource FormalTitlegres = model.getResource("http://www.semanticweb.org/dmelo/ontologies/2020/7/untitled-ontology-151#ARE2FormalTitle");
            Resource SuppliedTitlegres = model.getResource("http://www.semanticweb.org/dmelo/ontologies/2020/7/untitled-ontology-151#ARE3SuppliedTitle");

            Resource RefCoderes = model.getResource("http://www.semanticweb.org/dmelo/ontologies/2020/7/untitled-ontology-151#Reference_code");


//            DOC_IDENTITY
            HashMap<String, ArrayList<HashMap<String, String>>> DOC_IDENTITY = mapper.get("DOC_IDENTITY");
            ArrayList<HashMap<String, String>> titlemaparray,
                    identifiermaparray,
                    materialmaparray,
                    dimensionsmaparray,
                    quantitiesmaparray;

            titlemaparray = DOC_IDENTITY.get("titles");
            identifiermaparray = DOC_IDENTITY.get("identifiers");
            materialmaparray = DOC_IDENTITY.get("materials");
            dimensionsmaparray = DOC_IDENTITY.get("dimensions");
            quantitiesmaparray = DOC_IDENTITY.get("quantities");


            // DOC_CONTEXT
            HashMap<String, ArrayList<HashMap<String, String>>> DOC_CONTEXT = mapper.get("DOC_CONTEXT");
            ArrayList<HashMap<String, String>> subjectsmaparray,
                    writingsmaparray,
                    typologiesmaparray,
                    conservationStatesmaparray,
                    documentaryTraditionsmaparray;

            conservationStatesmaparray = DOC_CONTEXT.get("conservationStates");
            writingsmaparray = DOC_CONTEXT.get("writings");
            documentaryTraditionsmaparray = DOC_CONTEXT.get("documentaryTraditions");
            typologiesmaparray = DOC_CONTEXT.get("typologies");
            subjectsmaparray = DOC_CONTEXT.get("subjects");


            // DOC_ACCESS_USE_CONDITIONS
            HashMap<String, ArrayList<HashMap<String, String>>> DOC_ACCESS_USE_CONDITIONS = mapper.get("DOC_ACCESS_USE_CONDITIONS");
            ArrayList<HashMap<String, String>> accessConditionsmaparray,
                    languagesmaparray;

            languagesmaparray = DOC_ACCESS_USE_CONDITIONS.get("languages");
            accessConditionsmaparray = DOC_ACCESS_USE_CONDITIONS.get("accessConditions");


            // DOC_LINKED_DATA
            HashMap<String, ArrayList<HashMap<String, String>>> DOC_LINKED_DATA = mapper.get("DOC_LINKED_DATA");
            ArrayList<HashMap<String, String>> relatedDocsmaparray;

            relatedDocsmaparray = DOC_LINKED_DATA.get("relatedDocs");

            if (titlemaparray != null)
                for (HashMap<String, String> map : titlemaparray) {

                    Resource TitleRes = null;
                    if (map.get("type").equals("suppliedTitle")) {
                        TitleRes = model.createResource(SuppliedTitlegres);
                    } else if (map.get("type").equals("formalTitle")) {
                        TitleRes = model.createResource(FormalTitlegres);
                    }

                    if (TitleRes != null) {
                        Resource StringRes = model.createResource(Stringres);

                        TitleRes.addProperty(properties.getStringProperty(), StringRes);
                        StringRes.addProperty(properties.getStringValueProperty(), map.get("title"));
                        res.addProperty(properties.getTitleProperty(), TitleRes);
                    }
                }

            if (identifiermaparray != null)
                for (HashMap<String, String> map : identifiermaparray) {
                    Resource IdentifierRes = model.createResource(Idres);

                    if (map.get("type").equals("referenceCode")) {
                        Resource RefCode = model.createResource(RefCoderes);
                        IdentifierRes.addProperty(properties.getRefProperty(), RefCode);
                    }
                    Resource StringRes = model.createResource(Stringres);

                    IdentifierRes.addProperty(properties.getStringProperty(), StringRes);
                    StringRes.addProperty(properties.getStringValueProperty(), map.get("identifier"));
                    res.addProperty(properties.getIdentificationProperty(), IdentifierRes);

                }

            if (materialmaparray != null)
                for (HashMap<String, String> map : materialmaparray) {
                    res.addProperty(properties.getMaterialProperty(), map.get("material"));
                    res.addProperty(properties.getMaterialPropertyType(), map.get("component"));
                }

            if (dimensionsmaparray != null)
                for (HashMap<String, String> map : dimensionsmaparray) {
                    res.addProperty(properties.getDimensionProperty(), map.get("dimension"));
                    res.addProperty(properties.getDimensionPropertyValue(), map.get("value"));
                    res.addProperty(properties.getDimensionPropertyMU(), map.get("measurementUnit"));
                    res.addProperty(properties.getDimensionPropertyComponent(), map.get("component"));
                }

            if (quantitiesmaparray != null)
                for (HashMap<String, String> map : quantitiesmaparray) {
                    res.addProperty(properties.getQuantityProperty(), map.get("dimension"));
                    res.addProperty(properties.getQuantityPropertyValue(), map.get("value"));
                    res.addProperty(properties.getQuantityPropertyMU(), map.get("measurementUnit"));
                    res.addProperty(properties.getQuantityPropertyComponent(), map.get("component"));
                }

            if (conservationStatesmaparray != null)
                for (HashMap<String, String> map : conservationStatesmaparray) {
                    res.addProperty(properties.getConservationProperty(), map.get("conservationStatus"));
                    res.addProperty(properties.getConservationIDProperty(), map.get("initialDate"));
                    res.addProperty(properties.getConservationFDProperty(), map.get("finalDate"));
                }

            if (languagesmaparray != null)
                for (HashMap<String, String> map : languagesmaparray) {
                    res.addProperty(properties.getLanguageProperty(), map.get("language"));
                    res.addProperty(properties.getLanguageIdentifierProperty(), map.get("identifier"));
                }

            if (writingsmaparray != null)
                for (HashMap<String, String> map : writingsmaparray) {
                    res.addProperty(properties.getWritingProperty(), map.get("writing"));
                    res.addProperty(properties.getWritingIdentifierProperty(), map.get("identifier"));
                }

            if (documentaryTraditionsmaparray != null)
                for (HashMap<String, String> map : documentaryTraditionsmaparray) {

                    res.addProperty(properties.getDocProperty(), map.get("documentaryTradition"));
                }

            if (typologiesmaparray != null)
                for (HashMap<String, String> map : typologiesmaparray) {

                    res.addProperty(properties.getTypologyProperty(), map.get("documentaryTypology"));
                }

            if (subjectsmaparray != null)
                for (HashMap<String, String> map : subjectsmaparray) {

                    res.addProperty(properties.getSubjectProperty(), map.get("subject"));
                }

            if (accessConditionsmaparray != null)
                for (HashMap<String, String> map : accessConditionsmaparray) {
                    res.addProperty(properties.getAccessConditionProperty(), map.get("accessCondition"));
                    res.addProperty(properties.getAccessConditionJustifificationProperty(), map.get("justification"));
                }

            if (relatedDocsmaparray != null)
                for (HashMap<String, String> map : relatedDocsmaparray) {
                    res.addProperty(properties.getRelatedDocumentProperty(), map.get("recordIdentifier"));
                }

            conn.put(model);
            conn.commit();
        }

    }


}
