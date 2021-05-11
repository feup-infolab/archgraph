package operations;

import org.apache.jena.rdf.model.*;
import org.apache.jena.rdfconnection.RDFConnectionFuseki;
import org.apache.jena.rdfconnection.RDFConnectionRemoteBuilder;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.UUID;

public class Insert {

    public String updateHost;
    public String sparqlHost;
    public String dataHost;
    public String defaultHost;
    public Model model;
    public Properties properties;
    public Resources resources;

    public Insert(String defaultHost) {
        this.sparqlHost = defaultHost + "sparql";
        this.dataHost = defaultHost + "data";
        this.updateHost = defaultHost + "update";
        this.defaultHost = defaultHost;
    }

    public HashMap<String, String> insert(HashMap<String, HashMap<String, ArrayList<HashMap<String, String>>>> mapper, Boolean deletebefore, String docid) {
        RDFConnectionRemoteBuilder builder = RDFConnectionFuseki.create()
                .destination(this.dataHost);

        HashMap<String, String> response = new HashMap<>();

        try (RDFConnectionFuseki conn = (RDFConnectionFuseki) builder.build()) {
            this.model = conn.fetch();
            this.properties = new Properties(model);
            this.resources = new Resources(model);

            // create the resource
            String myUuidString = UUID.randomUUID().toString();
            Resource E31_myDoc = model.getResource(resources.getE31Document() + myUuidString);

            model.add(E31_myDoc, properties.getRdfType(), resources.getE31Document());
            model.add(E31_myDoc, properties.getRdfType(), resources.getNamedIndividual());


//            DOC_IDENTITY
            HashMap<String, ArrayList<HashMap<String, String>>> DOC_IDENTITY = mapper.get("DOC_IDENTITY");
            ArrayList<HashMap<String, String>> titleMapArray,
                    identifiermaparray,
                    materialmaparray,
                    dimensionsmaparray,
                    quantitiesmaparray,
                    descriptionLevelArray;

            titleMapArray = DOC_IDENTITY.get("titles");
            identifiermaparray = DOC_IDENTITY.get("identifiers");
            materialmaparray = DOC_IDENTITY.get("materials");
            dimensionsmaparray = DOC_IDENTITY.get("dimensions");
            quantitiesmaparray = DOC_IDENTITY.get("quantities");
            descriptionLevelArray = DOC_IDENTITY.get("descriptionLevel");

//
//            // DOC_CONTEXT
//            HashMap<String, ArrayList<HashMap<String, String>>> DOC_CONTEXT = mapper.get("DOC_CONTEXT");
//            ArrayList<HashMap<String, String>> subjectsmaparray,
//                    writingsmaparray,
//                    typologiesmaparray,
//                    conservationStatesmaparray,
//                    documentaryTraditionsmaparray;
//
//            conservationStatesmaparray = DOC_CONTEXT.get("conservationStates");
//            writingsmaparray = DOC_CONTEXT.get("writings");
//            documentaryTraditionsmaparray = DOC_CONTEXT.get("documentaryTraditions");
//            typologiesmaparray = DOC_CONTEXT.get("typologies");
//            subjectsmaparray = DOC_CONTEXT.get("subjects");
//
//
//            // DOC_ACCESS_USE_CONDITIONS
//            HashMap<String, ArrayList<HashMap<String, String>>> DOC_ACCESS_USE_CONDITIONS = mapper.get("DOC_ACCESS_USE_CONDITIONS");
//            ArrayList<HashMap<String, String>> accessConditionsmaparray,
//                    languagesmaparray;
//
//            languagesmaparray = DOC_ACCESS_USE_CONDITIONS.get("languages");
//            accessConditionsmaparray = DOC_ACCESS_USE_CONDITIONS.get("accessConditions");
//
//
//            // DOC_LINKED_DATA
//            HashMap<String, ArrayList<HashMap<String, String>>> DOC_LINKED_DATA = mapper.get("DOC_LINKED_DATA");
//            ArrayList<HashMap<String, String>> relatedDocsmaparray;
//
//            relatedDocsmaparray = DOC_LINKED_DATA.get("relatedDocs");

            this.insertTitles(E31_myDoc, titleMapArray);
            this.insertIdentifiers(E31_myDoc, myUuidString, identifiermaparray);
            this.insertDescriptionLevel(E31_myDoc, descriptionLevelArray);


//            if (materialmaparray != null) {
//                for (HashMap<String, String> map : materialmaparray) {
//                    res.addProperty(properties.getMaterialProperty(), map.get("material"));
//                    res.addProperty(properties.getMaterialPropertyType(), map.get("component"));
//                }
//            }
//
//            if (dimensionsmaparray != null) {
//                for (HashMap<String, String> map : dimensionsmaparray) {
//                    res.addProperty(properties.getDimensionProperty(), map.get("dimension"));
//                    res.addProperty(properties.getDimensionPropertyValue(), map.get("value"));
//                    res.addProperty(properties.getDimensionPropertyMU(), map.get("measurementUnit"));
//                    res.addProperty(properties.getDimensionPropertyComponent(), map.get("component"));
//                }
//            }
//
//            if (quantitiesmaparray != null)
//                for (HashMap<String, String> map : quantitiesmaparray) {
//                    res.addProperty(properties.getQuantityProperty(), map.get("dimension"));
//                    res.addProperty(properties.getQuantityPropertyValue(), map.get("value"));
//                    res.addProperty(properties.getQuantityPropertyMU(), map.get("measurementUnit"));
//                    res.addProperty(properties.getQuantityPropertyComponent(), map.get("component"));
//                }
//
//            if (conservationStatesmaparray != null)
//                for (HashMap<String, String> map : conservationStatesmaparray) {
//                    res.addProperty(properties.getConservationProperty(), map.get("conservationStatus"));
//                    res.addProperty(properties.getConservationIDProperty(), map.get("initialDate"));
//                    res.addProperty(properties.getConservationFDProperty(), map.get("finalDate"));
//                }
//
//            if (languagesmaparray != null) {
//                for (HashMap<String, String> map : languagesmaparray) {
//                    res.addProperty(properties.getLanguageProperty(), map.get("language"));
//                    res.addProperty(properties.getLanguageIdentifierProperty(), map.get("identifier"));
//                }
//            }
//
//            if (writingsmaparray != null) {
//                for (HashMap<String, String> map : writingsmaparray) {
//                    res.addProperty(properties.getWritingProperty(), map.get("writing"));
//                    res.addProperty(properties.getWritingIdentifierProperty(), map.get("identifier"));
//                }
//            }
//
//            if (documentaryTraditionsmaparray != null) {
//                for (HashMap<String, String> map : documentaryTraditionsmaparray) {
//
//                    res.addProperty(properties.getDocProperty(), map.get("documentaryTradition"));
//                }
//            }
//
//            if (typologiesmaparray != null) {
//                for (HashMap<String, String> map : typologiesmaparray) {
//
//                    res.addProperty(properties.getTypologyProperty(), map.get("documentaryTypology"));
//                }
//            }
//
//            if (subjectsmaparray != null) {
//                for (HashMap<String, String> map : subjectsmaparray) {
//
//                    res.addProperty(properties.getSubjectProperty(), map.get("subject"));
//                }
//            }
//
//            if (accessConditionsmaparray != null)
//                for (HashMap<String, String> map : accessConditionsmaparray) {
//                    res.addProperty(properties.getAccessConditionProperty(), map.get("accessCondition"));
//                    res.addProperty(properties.getAccessConditionJustifificationProperty(), map.get("justification"));
//                }
//
//            if (relatedDocsmaparray != null)
//                for (HashMap<String, String> map : relatedDocsmaparray) {
//                    res.addProperty(properties.getRelatedDocumentProperty(), map.get("recordIdentifier"));
//                }

            //TODO update

            //         Resource alice = model.createResource("http://example.org/people/alice");
            //           Property name = model.createProperty("http://example.org/ontology/name");
//
            //Literal alicesName = model.createLiteral("Alice");
//            System.out.println("Triple count before inserts: " + model.size());
//            // Alice's name is "Alice"
            //model.add(alice, name, alicesName);
//
//            System.out.println("Triple count after inserts: " + (model.size()));
//            model.remove(alice, name, alicesName);
//
//            System.out.println("Triple count after deletion: " + (model.size()));

            conn.put(model);
            conn.commit();
            conn.close();

            response.put("uuid", myUuidString);
            response.put("message", "Document created successfully");
            return response;
        } catch (Exception e) {
            System.out.println(e.getMessage());
            HashMap<String, String> errorResponse = new HashMap<>();
            if (e.getMessage() != null) {
                errorResponse.put("error", e.getMessage());
            } else {
                errorResponse.put("error", "Some error occurred");
            }
            return errorResponse;
        }
    }

    public void insertTitles(Resource E31_myDoc, ArrayList<HashMap<String, String>> titleMapArray) {
        if (titleMapArray != null) {
            for (HashMap<String, String> map : titleMapArray) {
                if (map.get("type").equals("suppliedTitle")) {
                    String myTitle = resources.getARE3SuppliedTitle().toString() + UUID.randomUUID().toString();
                    Property myTypeTitle = model.getProperty(myTitle);
                    model.add(E31_myDoc, properties.getP102HasTitle(), myTypeTitle);
                    model.add(myTypeTitle, properties.getRdfType(), resources.getARE3SuppliedTitle());
                    this.insertString(myTypeTitle, map.get("title"));

                } else if (map.get("type").equals("formalTitle")) {
                    String myTitle = resources.getARE2FormalTitle().toString() + UUID.randomUUID().toString();
                    Property myTypeTitle = model.getProperty(myTitle);
                    model.add(E31_myDoc, properties.getP102HasTitle(), myTypeTitle);
                    model.add(myTypeTitle, properties.getRdfType(), resources.getARE2FormalTitle());
                    this.insertString(myTypeTitle, map.get("title"));
                }
            }
        }
    }

    public void insertIdentifiers(Resource E31_myDoc, String myUuidString, ArrayList<HashMap<String, String>> identifierMapArray) {
        if (identifierMapArray != null) {
            for (HashMap<String, String> map : identifierMapArray) {

                Property myIdentifier = model.getProperty(resources.getE42Identifier().toString(), UUID.randomUUID().toString());
                model.add(E31_myDoc, properties.getP1IsIdentifiedBy(), myIdentifier);
                model.add(myIdentifier, properties.getRdfType(), resources.getE42Identifier());
                model.add(myIdentifier, properties.getRdfType(), resources.getNamedIndividual());
                model.add(myIdentifier, properties.getP2HasType(), resources.getReferenceCode());

                this.insertString(myIdentifier, map.get("identifier"));
            }
        }
        model.add(E31_myDoc, properties.getHasUuid(), myUuidString);
    }

    private void insertString(Property myIdentifier, String identifier) {
        String myString = resources.getString() + UUID.randomUUID().toString();
        model.add(myIdentifier, properties.getHasValue(), model.getProperty(myString));
        model.add(model.getResource(myString), properties.getStringValue(), identifier);
    }

    private void insertDescriptionLevel(Resource E31_myDoc, ArrayList<HashMap<String, String>> identifierMapArray) {
        for (HashMap<String, String> map : identifierMapArray) {
            String descriptionLevel = map.get("descriptionLevel");
            Resource descriptionLevelResource = resources.getDescriptionLevel(descriptionLevel);
            model.add(E31_myDoc, properties.getARP12HasDescriptionLevel(), descriptionLevelResource);
            String[] arrOfStr = descriptionLevel.toString().split("#", 1);
            model.add(descriptionLevelResource, properties.getLabel(), arrOfStr[0]);
        }
    }
}
