package model;

import operations.Queries;
import operations.SPARQLOperations;
import org.apache.jena.rdf.model.*;
import org.apache.jena.rdfconnection.RDFConnectionFuseki;
import org.apache.jena.rdfconnection.RDFConnectionRemoteBuilder;
import org.apache.jena.update.UpdateFactory;
import org.apache.jena.update.UpdateRequest;
import utils.Properties;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.UUID;


public class Document {

    public HashMap<String, String> myHost = new HashMap<>();
    public Model model;
    public Queries queries;
    public String uuid;
    public String myDocId;
    public HashMap<String, HashMap<String, ArrayList<HashMap<String, String>>>> docContent;
    public HashMap<String, String> myStatus = new HashMap<>();

    public Properties properties;

    public Document(String defaultHost, HashMap<String, HashMap<String, ArrayList<HashMap<String, String>>>> mapper, String uuid) {
        this.myHost.put("sparql", defaultHost + "sparql");
        this.myHost.put("data", defaultHost + "data");
        this.myHost.put("update", defaultHost + "update");
        this.myHost.put("default", defaultHost);

        this.uuid = uuid;
        this.queries = new Queries();
        if (mapper != null) {
            this.docContent = mapper;
        } else {
            this.docContent = new HashMap<>();
        }

        myStatus.put("added", "added");
        myStatus.put("deleted", "deleted");
        myStatus.put("changed", "changed");
        myStatus.put("notChanged", "notChanged");
    }

    public void setMyDocId(String myDocId) {
        this.myDocId = myDocId;
    }

    public HashMap<String, HashMap<String, ArrayList<HashMap<String, String>>>> getDocContent() {
        return docContent;
    }

    public String getMiddleArrayString(String arrayName) throws Exception {
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
            case "physicalLocation":
            case "physicalCharacteristicsTechnicalRequirements":
                middleArray = "DOC_ACCESS_USE_CONDITIONS";
                break;

            case "relatedDocs":
                middleArray = "DOC_LINKED_DATA";
                break;
            default:
                throw new Exception("There is no such field in the document");
        }
        return middleArray;
    }

    public ArrayList<HashMap<String, String>> getArrayName(String arrayName) throws Exception {
        String middleArrayString = this.getMiddleArrayString(arrayName);
        if (this.docContent == null) {
            throw new Exception("Document doesn't have fields");
        }
        HashMap<String, ArrayList<HashMap<String, String>>> middleArray = this.docContent.get(middleArrayString);
        if (middleArray == null) {
            throw new Exception("There isn't such intermediate field in the document");
        }
        return middleArray.get(arrayName);
    }

    public HashMap<String, String> insert() throws Exception {
        RDFConnectionRemoteBuilder builder = RDFConnectionFuseki.create()
                .destination(myHost.get("data"));
        HashMap<String, String> response = new HashMap<>();

        RDFConnectionFuseki conn = (RDFConnectionFuseki) builder.build();
        this.model = conn.fetch();
        this.properties = new Properties();

        Resource E31_myDoc;
        String myUuidString;
        myUuidString = UUID.randomUUID().toString();
        E31_myDoc = model.getResource(properties.getE31Document() + myUuidString);
        model.add(E31_myDoc, properties.getRdfType(), properties.getE31Document());
        model.add(E31_myDoc, properties.getRdfType(), properties.getNamedIndividual());

        //episaIdentifier
        model.add(E31_myDoc, properties.getHasUuid(), myUuidString);

        this.insertTitles(E31_myDoc, this.getArrayName("titles"));
        this.insertIdentifiers(E31_myDoc, this.getArrayName("identifiers"));
        this.insertDescriptionLevel(E31_myDoc, this.getArrayName("descriptionLevel"));
        this.insertDimensions(E31_myDoc, this.getArrayName("dimensions"));


        conn.put(model);
        conn.commit();
        conn.close();

        response.put("uuid", myUuidString);
        response.put("message", "Document created successfully");
        return response;
    }

    public HashMap<String, String> update() throws Exception {
        RDFConnectionRemoteBuilder builder = RDFConnectionFuseki.create()
                .destination(myHost.get("data"));
        HashMap<String, String> response = new HashMap<>();

        RDFConnectionFuseki conn = (RDFConnectionFuseki) builder.build();
        this.model = conn.fetch();
        this.properties = new Properties();

        if (myDocId == null) {
            conn.close();
            throw new Exception("Document Id is null");
        } else {
            Resource E31_myDoc = model.getResource(myDocId);
            ArrayList<HashMap<String, String>> titlesToAdd = this.elementsToAdd(this.getArrayName("titles"));
            this.insertTitles(E31_myDoc, titlesToAdd);

            ArrayList<HashMap<String, String>> identifiersToAdd = this.elementsToAdd(this.getArrayName("identifiers"));
            this.insertIdentifiers(E31_myDoc, identifiersToAdd);

            ArrayList<HashMap<String, String>> descriptionAdd = this.elementsToAdd(this.getArrayName("descriptionLevel"));
            this.insertDescriptionLevel(E31_myDoc, descriptionAdd);

            ArrayList<HashMap<String, String>> dimensionAdd = this.elementsToAdd(this.getArrayName("dimensions"));
            this.insertDimensions(E31_myDoc, dimensionAdd);

            response.put("message", "Document updated successfully");
            conn.put(model);
            conn.commit();
            conn.close();
            return response;
        }
    }

    public void insertTitles(Resource E31_myDoc, ArrayList<HashMap<String, String>> myTitles) throws Exception {
        if (myTitles != null) {
//        if (myTitles.size() == 0) {
//            throw new Exception("There aren't titles");
//        }
            for (HashMap<String, String> map : myTitles) {
                String titleUuid = UUID.randomUUID().toString();
                String typeTitle;
                if (map.get("type").equals("suppliedTitle")) {
                    typeTitle = properties.getARE3SuppliedTitle().toString();
                } else {
                    typeTitle = properties.getARE2FormalTitle().toString();
                }

                Property myTypeTitle = model.getProperty(typeTitle + titleUuid);
                String stringValue = properties.getTitleString() + UUID.randomUUID().toString();
                Property StringValueProperty = model.getProperty(stringValue);
                model.add(E31_myDoc, properties.getP102HasTitle(), myTypeTitle);
                model.add(myTypeTitle, properties.getRdfType(), model.getProperty(typeTitle));
                model.add(myTypeTitle, properties.getRdfType(), properties.getNamedIndividual());

                model.add(myTypeTitle, properties.getHasValue(), StringValueProperty);
                model.add(StringValueProperty, properties.getStringValue(), map.get("title"));
                model.add(StringValueProperty, properties.getRdfType(), properties.getNamedIndividual());
                model.add(StringValueProperty, properties.getRdfType(), properties.getString());
            }
        }
    }

    public void insertIdentifiers(Resource E31_myDoc, ArrayList<HashMap<String, String>> myIdentifiers) throws Exception {
        if (myIdentifiers != null) {
//            if (myIdentifiers.size() == 0) {
//                throw new Exception("There aren't identifiers");
//            }
            int referenceCodeCount = 0;
            for (HashMap<String, String> map : myIdentifiers) {
                Property myIdentifier = model.getProperty(properties.getTitleOntology() + map.get("identifier"));
                model.add(E31_myDoc, properties.getP1IsIdentifiedBy(), myIdentifier);
                if (map.get("type").equals("referenceCode")) {
                    model.add(myIdentifier, properties.getP2HasType(), properties.getReferenceCode());
                    referenceCodeCount++;
                }
                String identifierUuid = UUID.randomUUID().toString();
                model.add(myIdentifier, properties.getRdfType(), properties.getNamedIndividual());
                model.add(myIdentifier, properties.getRdfType(), properties.getE42Identifier());

            }
            if (referenceCodeCount > 1) {
                throw new Exception("There are more than one Reference Code");
            }
        }
    }

//    private void insertString(Property property, String identifier, Property propertyType) {
//        String uuid = UUID.randomUUID().toString();
//        model.add(property, properties.getHasValue(), identifier);
//        model.add(property, properties.getRdfType(), propertyType);
//        model.add(property, properties.getRdfType(), properties.getNamedIndividual());
//
//
//    }

    public void insertDescriptionLevel(Resource E31_myDoc, ArrayList<HashMap<String, String>> myDescriptionLevel) throws Exception {
        if (myDescriptionLevel != null) {
//            if (myDescriptionLevel.size() == 0) {
//                throw new Exception("There isn't description level");
//            }
            for (HashMap<String, String> map : myDescriptionLevel) {
                String descriptionLevel = map.get("descriptionLevel");
                Property descriptionLevelResource = properties.getPropertyWithNameSpace(descriptionLevel);
                model.add(E31_myDoc, properties.getARP12HasDescriptionLevel(), descriptionLevelResource);
                String[] arrOfStr = descriptionLevel.toString().split("#", 1);
                model.add(descriptionLevelResource, properties.getLabel(), arrOfStr[0]);
            }
        }
    }


    public void insertDimensions(Resource E31_myDoc, ArrayList<HashMap<String, String>> myDimensions) throws Exception {
        if (myDimensions != null) {
//            if (myDescriptionLevel.size() == 0) {
//                throw new Exception("There isn't description level");
//            }
            for (HashMap<String, String> map : myDimensions) {
                String material = map.get("material");
                String value = map.get("value");
                String measurementUnit = map.get("measurementUnit");

                String physicalObjectUuid = UUID.randomUUID().toString();
                Property physicalObject = model.getProperty(properties.getNameSpace() + "physicalObject" + physicalObjectUuid);
                model.add(E31_myDoc, properties.getP128IsCarriedBy(), physicalObject);

                model.add(physicalObject, properties.getP45ConsistsOf(), properties.getPropertyWithNameSpace(material));
                String dimensionUuid = UUID.randomUUID().toString();
                Property dimension = properties.getPropertyWithNameSpace("dimension" + dimensionUuid);

                model.add(physicalObject, properties.getP43HasDimension(), dimension);

                model.add(dimension, properties.getRdfType(), properties.getNamedIndividual());
                model.add(dimension, properties.getRdfType(), properties.getE54Dimension());
                model.add(dimension, properties.getP90HasValue(), value);

                Property myMeasurementUnit = properties.getPropertyWithNameSpace(measurementUnit);
                model.add(dimension, properties.getP91HasUnit(), myMeasurementUnit);

                model.add(myMeasurementUnit, properties.getRdfType(), properties.getE58MeasurementUnit());
                model.add(myMeasurementUnit, properties.getRdfType(), properties.getNamedIndividual());

            }
        }
    }

    public HashMap<String, String> deleteDoc(String uuid) throws Exception {

        RDFConnectionRemoteBuilder builder = RDFConnectionFuseki.create().destination(myHost.get("update"));

        RDFConnectionFuseki conn = (RDFConnectionFuseki) builder.build();
        UpdateRequest request = UpdateFactory.create();

        request.add(queries.deleteDoc(uuid));
        conn.update(request);
        HashMap<String, String> response = new HashMap<>();
        response.put("message", "Document deleted successfully");

        return response;
    }

    public HashMap<String, String> deleteSomeInformationAndUpdate() throws Exception {

        RDFConnectionRemoteBuilder builder = RDFConnectionFuseki.create().destination(myHost.get("update"));
        HashMap<String, String> response;

        RDFConnectionFuseki conn = (RDFConnectionFuseki) builder.build();
        UpdateRequest request = UpdateFactory.create();

        ArrayList<String> uuidTitles = this.elementsToDelete(this.getArrayName("titles"));
        if (uuidTitles != null) {
            for (String titleUuid : uuidTitles) {
                request.add(queries.deleteDocTitle(titleUuid));
            }
        }

        ArrayList<String> uuidIdentifiers = this.elementsToDelete(this.getArrayName("identifiers"));
        if (uuidIdentifiers != null) {
            for (String identifierUuid : uuidIdentifiers) {
                request.add(queries.deleteDocIdentifier(identifierUuid));
            }
        }

        ArrayList<String> uuidDescriptionLevel = this.elementsToDelete(this.getArrayName("descriptionLevel"));
        if (uuidDescriptionLevel != null) {
            for (String descritor : uuidDescriptionLevel) {
                request.add(queries.deleteDocDescriptionLevel(this.myDocId));
            }
        }

        ArrayList<String> uuidDimensions = this.elementsToDelete(this.getArrayName("dimensions"));
        if (uuidDimensions != null) {
            for (String dimensionUuid : uuidDimensions) {
                request.add(queries.deleteDocDimension(dimensionUuid));
            }
        }

        conn.update(request);
        response = this.update();

        conn.commit();
        conn.close();
        return response;
    }

    private ArrayList<String> elementsToDelete(ArrayList<HashMap<String, String>> myArray) throws Exception {
        if (myArray == null)
            return null;

        ArrayList<String> result = new ArrayList<>();
        for (HashMap<String, String> elem : myArray) {
            if (elem.get("status").equals(this.myStatus.get("deleted")) || elem.get("status").equals(this.myStatus.get("changed"))) {
                result.add(elem.get("myEntityUuid"));
            }
        }
        return result;
    }

    private ArrayList<HashMap<String, String>> elementsToAdd(ArrayList<HashMap<String, String>> myArray) throws
            Exception {
        if (myArray == null)
            return null;

        ArrayList<HashMap<String, String>> result = new ArrayList<>();
        for (HashMap<String, String> elem : myArray) {
            if (elem.get("status").equals(this.myStatus.get("added")) || elem.get("status").equals(this.myStatus.get("changed"))) {
                result.add(elem);
            }
        }
        return result;
    }

    public HashMap<String, HashMap<String, ArrayList<HashMap<String, String>>>> getDocFromDatabase(SPARQLOperations
                                                                                                           conn) {
        this.addDocIdentity(conn);
        this.addDocContext(conn);
        this.addDocAccessUseConditions(conn);
        this.addDocLinkedData(conn);

        return this.getDocContent();
    }

    public void addDocIdentity(SPARQLOperations conn) {

        HashMap<String, ArrayList<HashMap<String, String>>> DOC_IDENTITY = new HashMap<>();
        docContent.put("DOC_IDENTITY", DOC_IDENTITY);

        conn.executeQueryAndAddContent(queries.getIdentifier(uuid), DOC_IDENTITY, "identifiers");
        conn.executeQueryAndAddContent(queries.getLevel_of_description_query(uuid), DOC_IDENTITY, "descriptionLevel");

        conn.executeQueryAndAddContent(queries.getTitle(uuid), DOC_IDENTITY, "titles");
        conn.executeQueryAndAddContent(queries.getMaterial(uuid), DOC_IDENTITY, "materials");
        conn.executeQueryAndAddContent(queries.getDimension(uuid), DOC_IDENTITY, "dimensions");
        conn.executeQueryAndAddContent(queries.getQuantity(uuid), DOC_IDENTITY, "quantities");
    }

    public void addDocContext(SPARQLOperations conn) {
        HashMap<String, ArrayList<HashMap<String, String>>> DOC_CONTEXT = new HashMap<>();
        docContent.put("DOC_CONTEXT", DOC_CONTEXT);

        conn.executeQueryAndAddContent(queries.getSubject(uuid), DOC_CONTEXT, "subjects");
        conn.executeQueryAndAddContent(queries.getWriting(uuid), DOC_CONTEXT, "writings");
        conn.executeQueryAndAddContent(queries.getDocTypology(uuid), DOC_CONTEXT, "typologies");
        conn.executeQueryAndAddContent(queries.getConservationStatus(uuid), DOC_CONTEXT, "conservationStates");
        conn.executeQueryAndAddContent(queries.getDocTradition(uuid), DOC_CONTEXT, "documentaryTraditions");
    }

    public void addDocAccessUseConditions(SPARQLOperations conn) {
        HashMap<String, ArrayList<HashMap<String, String>>> DOC_ACCESS_USE_CONDITIONS = new HashMap<>();
        docContent.put("DOC_ACCESS_USE_CONDITIONS", DOC_ACCESS_USE_CONDITIONS);

        conn.executeQueryAndAddContent(queries.getAccessCondition(uuid), DOC_ACCESS_USE_CONDITIONS, "accessConditions");
        conn.executeQueryAndAddContent(queries.getLanguage(uuid), DOC_ACCESS_USE_CONDITIONS, "languages");
        conn.executeQueryAndAddContent(queries.getPhysicalLocation(uuid), DOC_ACCESS_USE_CONDITIONS, "physicalLocation");
        conn.executeQueryAndAddContent(queries.getPhysicalCharacteristicsTechnicalRequirements(uuid), DOC_ACCESS_USE_CONDITIONS, "physicalCharacteristicsTechnicalRequirements");


    }

    public void addDocLinkedData(SPARQLOperations conn) {
        HashMap<String, ArrayList<HashMap<String, String>>> DOC_LINKED_DATA = new HashMap<>();
        docContent.put("DOC_LINKED_DATA", DOC_LINKED_DATA);

        conn.executeQueryAndAddContent(queries.getRelatedDoc(uuid), DOC_LINKED_DATA, "relatedDocs");
        conn.executeQueryAndAddContent(queries.getRelatedEvent(uuid), DOC_LINKED_DATA, "relatedEvents");
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


