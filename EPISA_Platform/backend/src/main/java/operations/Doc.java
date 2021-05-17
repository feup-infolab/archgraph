package operations;

import org.apache.jena.rdf.model.*;
import org.apache.jena.rdfconnection.RDFConnectionFuseki;
import org.apache.jena.rdfconnection.RDFConnectionRemoteBuilder;
import queries.Queries;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.UUID;

public class Doc {

    public String updateHost;
    public String sparqlHost;
    public String dataHost;
    public String defaultHost;
    public Model model;
    public Queries queries = new Queries();
    public HashMap<String, HashMap<String, ArrayList<HashMap<String, String>>>> docContent;

    public Properties properties;
    public Resources resources;

    public Doc(String defaultHost, HashMap<String, HashMap<String, ArrayList<HashMap<String, String>>>> mapper) {
        this.sparqlHost = defaultHost + "sparql";
        this.dataHost = defaultHost + "data";
        this.updateHost = defaultHost + "update";
        this.defaultHost = defaultHost;
        this.queries = new Queries();
        this.docContent = mapper;
    }

    public String getMiddleArrayString(String arrayName) {
        String middleArray;

        switch (arrayName) {
            case "titles":
            case "descriptionLevel":
            case "identifiers":
            case "materials":
            case "dimensions":
            case "quantities":
                middleArray = "DOC_IDENTITY";
                break;

            case "subjects":
            case "writings":
            case "typologies":
            case "conservationStates":
            case "documentaryTraditions":
                middleArray = "DOC_CONTEXT";
                break;

            case "accessConditions":
            case "languages":
                middleArray = "DOC_ACCESS_USE_CONDITIONS";
                break;

            case "relatedDocs":
                middleArray = "DOC_LINKED_DATA";
                break;
            default:
                middleArray = null;
        }
        return middleArray;
    }

    public ArrayList<HashMap<String, String>> getArrayName(String arrayName) {
        String middleArrayString = this.getMiddleArrayString(arrayName);
        HashMap<String, ArrayList<HashMap<String, String>>> middleArray = this.docContent.get(middleArrayString);
        if (middleArray != null) {
            return middleArray.get(arrayName);
        }
        return null;
    }

    public HashMap<String, String> insert() throws Exception {
        RDFConnectionRemoteBuilder builder = RDFConnectionFuseki.create()
                .destination(this.dataHost);
        HashMap<String, String> response = new HashMap<>();

        RDFConnectionFuseki conn = (RDFConnectionFuseki) builder.build();
        this.model = conn.fetch();
        this.properties = new Properties(model);
        this.resources = new Resources(model);

        Resource E31_myDoc;
        String myUuidString;
        myUuidString = UUID.randomUUID().toString();
        E31_myDoc = model.getResource(resources.getE31Document() + myUuidString);
        model.add(E31_myDoc, properties.getRdfType(), resources.getE31Document());
        model.add(E31_myDoc, properties.getRdfType(), resources.getNamedIndividual());

        //episaIdentifier
        model.add(E31_myDoc, properties.getHasUuid(), myUuidString);


        this.insertTitles(E31_myDoc, this.getArrayName("titles"));
        this.insertIdentifiers(E31_myDoc, this.getArrayName("identifiers"));
        this.insertDescriptionLevel(E31_myDoc, this.getArrayName("descriptionLevel"));

        conn.put(model);
        conn.commit();
        conn.close();

        response.put("uuid", myUuidString);
        response.put("message", "Document created successfully");
        return response;
    }

    public HashMap<String, String> update(String myDocId, String uuid) throws Exception {
        RDFConnectionRemoteBuilder builder = RDFConnectionFuseki.create()
                .destination(this.dataHost);
        HashMap<String, String> response = new HashMap<>();

        try (RDFConnectionFuseki conn = (RDFConnectionFuseki) builder.build()) {
            this.model = conn.fetch();
            this.properties = new Properties(model);
            this.resources = new Resources(model);

            if (myDocId == null) {
                String message = "Doesn't exists any document with the uui = " + uuid;
                conn.close();
                throw new Exception(message);
            } else {
                Resource E31_myDoc = model.getResource(myDocId);
                this.insertTitles(E31_myDoc, this.getArrayName("titles"));
                this.insertIdentifiers(E31_myDoc, this.getArrayName("identifiers"));
                this.insertDescriptionLevel(E31_myDoc, this.getArrayName("descriptionLevel"));

                response.put("message", "Document updated successfully");
                conn.put(model);
                conn.commit();
                conn.close();
            }
            return response;
        }
    }

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


    public void insertTitles(Resource E31_myDoc, ArrayList<HashMap<String, String>> titleMapArray) throws Exception {
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
        } else
            throw new Exception("Don't exists titles");
    }

    public void insertIdentifiers(Resource E31_myDoc, ArrayList<HashMap<String, String>> identifierMapArray) throws Exception {
        if (identifierMapArray != null) {
            for (HashMap<String, String> map : identifierMapArray) {
                Property myIdentifier = model.getProperty(resources.getE42Identifier().toString(), UUID.randomUUID().toString());
                model.add(E31_myDoc, properties.getP1IsIdentifiedBy(), myIdentifier);
                model.add(myIdentifier, properties.getRdfType(), resources.getE42Identifier());
                model.add(myIdentifier, properties.getRdfType(), resources.getNamedIndividual());
                model.add(myIdentifier, properties.getP2HasType(), resources.getReferenceCode());
                this.insertString(myIdentifier, map.get("identifier"));
            }
        } else {
            throw new Exception("Don't exists identifiers");
        }
    }

    private void insertString(Property myIdentifier, String identifier) {
        String myString = resources.getString() + UUID.randomUUID().toString();
        model.add(myIdentifier, properties.getHasValue(), model.getProperty(myString));
        model.add(model.getResource(myString), properties.getStringValue(), identifier);
    }

    private void insertDescriptionLevel(Resource E31_myDoc, ArrayList<HashMap<String, String>> descriptionLevelMapArray) throws Exception {
        if (descriptionLevelMapArray != null) {
            for (HashMap<String, String> map : descriptionLevelMapArray) {
                String descriptionLevel = map.get("descriptionLevel");
                Resource descriptionLevelResource = resources.getDescriptionLevel(descriptionLevel);
                model.add(E31_myDoc, properties.getARP12HasDescriptionLevel(), descriptionLevelResource);
                String[] arrOfStr = descriptionLevel.toString().split("#", 1);
                model.add(descriptionLevelResource, properties.getLabel(), arrOfStr[0]);
            }
        } else
            throw new Exception("Don't exists description level");
    }

    public void saveDocFromRequest() {

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

    }
}


