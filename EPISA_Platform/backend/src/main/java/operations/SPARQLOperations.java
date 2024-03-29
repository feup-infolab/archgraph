package operations;

import org.apache.jena.query.*;
import org.apache.jena.rdf.model.*;
import org.apache.jena.rdfconnection.RDFConnectionFuseki;
import org.apache.jena.rdfconnection.RDFConnectionRemoteBuilder;
import utils.Properties;

import java.util.*;

public class SPARQLOperations {
    public Queries queries = new Queries();
    public String sparqlHost;
    public String dataHost;
    public String updateHost;

    public SPARQLOperations(String defaultHost) {
        this.sparqlHost = defaultHost + "sparql";
        this.dataHost = defaultHost + "data";
        this.updateHost = defaultHost + "update";
    }

    public void importOWL() {
        RDFConnectionRemoteBuilder builder = RDFConnectionFuseki.create()
                .destination(dataHost);

        try (RDFConnectionFuseki conn = (RDFConnectionFuseki) builder.build()) {
            conn.load("owls/Exemplo-15registos.owl");
        }
    }

    public String obtainARecordOfAColumn(Query query) throws Exception {
        RDFConnectionRemoteBuilder builder = RDFConnectionFuseki.create()
                .destination(sparqlHost);
        String result = null;
        int numberOfRows = 0;
        int numberOfColumns = 0;

        try (RDFConnectionFuseki conn = (RDFConnectionFuseki) builder.build()) {

            QueryExecution qExec = conn.query(query);
            ResultSet rs = qExec.execSelect();
            QuerySolution stmt;
            while (rs.hasNext()) {
                numberOfColumns++;
                stmt = rs.next();
                Iterator<String> b = stmt.varNames();

                while (b.hasNext()) {
                    numberOfRows++;
                    String current = b.next();
                    RDFNode res = stmt.get(current);
                    result = res.toString();
                }
            }

            qExec.close();
            conn.close();
            //There are more than 1 record or there aren't records
        }
        if (numberOfRows != 1 & numberOfColumns != 1) {
            throw new Exception("There are more than 1 record or there isn't a record");
        }
        return result;
    }

    public ArrayList<String> obtainAColumn(Query query) throws Exception {
        RDFConnectionRemoteBuilder builder = RDFConnectionFuseki.create()
                .destination(sparqlHost);
        ArrayList<String> result = new ArrayList<>();

        try (RDFConnectionFuseki conn = (RDFConnectionFuseki) builder.build()) {

            QueryExecution qExec = conn.query(query);
            ResultSet rs = qExec.execSelect();
            QuerySolution stmt;
            while (rs.hasNext()) {
                stmt = rs.next();
                Iterator<String> b = stmt.varNames();

                int numberOfColumns = 0;
                while (b.hasNext()) {
                    numberOfColumns++;
                    String current = b.next();
                    RDFNode res = stmt.get(current);
                    result.add(res.toString());
                }
                if (numberOfColumns != 1) {
                    throw new Exception("There are more than 1 Column or there aren't records");
                }
            }

            qExec.close();
        }
        return result;
    }

    public ArrayList<HashMap<String, String>> executeQueryAndAddContent(Query query, HashMap<String, ArrayList<HashMap<String, String>>> myObject, String key) {
        RDFConnectionRemoteBuilder builder = RDFConnectionFuseki.create()
                .destination(sparqlHost);
        Properties myProperties = new Properties();

        ArrayList<HashMap<String, String>> myArrayList = new ArrayList<>();
        if (myObject != null && key != null) {
            myObject.put(key, myArrayList);
        }

        try (RDFConnectionFuseki conn = (RDFConnectionFuseki) builder.build()) {
            QueryExecution qExec = conn.query(query);
            ResultSet rs = qExec.execSelect();
            QuerySolution stmt;

            while (rs.hasNext()) {

                stmt = rs.next();
                Iterator<String> b = stmt.varNames();
                HashMap<String, String> result = new HashMap<>();

                while (b.hasNext()) {
                    String current = b.next();
                    RDFNode res = stmt.get(current);

                    if (current.equals(myProperties.getMyEntityUuid())) {
                        result.put(current, res.toString());
                    } else if (res.toString().contains(myProperties.getARE3SuppliedTitle().toString())) {
                        result.put(current, "suppliedTitle");
                    } else if (res.toString().contains(myProperties.getARE2FormalTitle().toString())) {
                        result.put(current, "formalTitle");
                    } else if (current.equals("descriptionLevel")) {
                        String[] arrayString = res.toString().split("#");
                        if (arrayString.length == 2) {
                            result.put(current, arrayString[1]);
                        }
                    } else if (myObject != null && key != null) {
                        String[] arrayString = res.toString().split("#");
                        if (arrayString.length == 2) {
                            result.put(current, arrayString[1]);
                        } else {
                            result.put(current, res.toString());
                        }
                    } else {
                        result.put(current, res.toString());

                    }
                }
                if (result.size() != 0) {
                    myArrayList.add(result);
                }
            }
            conn.close();
            qExec.close();
        }
        return myArrayList;
    }

    public ArrayList<String> getAllUuids() {
        RDFConnectionRemoteBuilder builder = RDFConnectionFuseki.create()
                .destination(sparqlHost);
        ArrayList<String> list = new ArrayList<>();

        try (RDFConnectionFuseki conn = (RDFConnectionFuseki) builder.build()) {
            Query query = queries.getAllResourcesDocs();

            ResultSet rs = conn.query(query).execSelect();
            while (rs.hasNext()) {

                QuerySolution qs = rs.next();
                list.add(qs.get("subject").toString());
            }
            return list;

        }
    }


    public ArrayList<String> getAllBaseUuids() {
        RDFConnectionRemoteBuilder builder = RDFConnectionFuseki.create()
                .destination(sparqlHost);
        ArrayList<String> list = new ArrayList<>();

        try (RDFConnectionFuseki conn = (RDFConnectionFuseki) builder.build()) {
            Query query = queries.getAllUuids();
            System.err.println("Query: " + query.toString());
            ResultSet rs = conn.query(query).execSelect();
            while (rs.hasNext()) {

                QuerySolution qs = rs.next();
                list.add(qs.get("description").toString());
            }
        }
        return list;
    }

    public ArrayList<String> getAllMats() {
        RDFConnectionRemoteBuilder builder = RDFConnectionFuseki.create()
                .destination(sparqlHost);
        ArrayList<String> list = new ArrayList<>();

        try (RDFConnectionFuseki conn = (RDFConnectionFuseki) builder.build()) {
            Query query = queries.getAllMater();
            ResultSet rs = conn.query(query).execSelect();
            while (rs.hasNext()) {

                QuerySolution qs = rs.next();
                list.add(qs.get("description").toString());
            }
        }
        return list;
    }


}