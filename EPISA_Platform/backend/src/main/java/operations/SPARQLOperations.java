package operations;

import cclasses.ResponseClass;
import org.apache.jena.query.*;
import org.apache.jena.rdf.model.*;
import org.apache.jena.rdfconnection.RDFConnectionFuseki;
import org.apache.jena.rdfconnection.RDFConnectionRemoteBuilder;
import org.apache.jena.update.UpdateFactory;
import org.apache.jena.update.UpdateRequest;
import org.springframework.boot.configurationprocessor.json.JSONException;
import org.springframework.boot.configurationprocessor.json.JSONObject;
import queries.Queries;

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
            conn.load("owls/Exemplo-25registos.owl");
        }
    }

    public ArrayList<HashMap<String, String>> obtainSummaryResponse(Query query) {
        RDFConnectionRemoteBuilder builder = RDFConnectionFuseki.create()
                .destination(sparqlHost);

        System.out.println(query.toString());
        ArrayList<HashMap<String, String>> myArray = new ArrayList<>();

        try (RDFConnectionFuseki conn = (RDFConnectionFuseki) builder.build()) {

            QueryExecution qExec = conn.query(query);
            ResultSet rs = qExec.execSelect();
            QuerySolution stmt;
            while (rs.hasNext()) {
                stmt = rs.next();
                Iterator<String> b = stmt.varNames();
                HashMap<String, String> myarrayLocal = new HashMap<>();

                while (b.hasNext()) {
                    String current = b.next();
                    RDFNode res = stmt.get(current);
                    myarrayLocal.put(current, res.toString());
                }
                myArray.add(myarrayLocal);
            }
            qExec.close();
        }
        return myArray;
    }

    public ResponseClass obtainGeneralResponse(Query query, String key, ResponseClass r) {
        System.out.println(query.toString());
        RDFConnectionRemoteBuilder builder = RDFConnectionFuseki.create()
                .destination(sparqlHost);

        try (RDFConnectionFuseki conn = (RDFConnectionFuseki) builder.build()) {

            QueryExecution qExec = conn.query(query);
            ResultSet rs = qExec.execSelect();
            ArrayList<Map<String, String>> complexList = new ArrayList<>();
            QuerySolution stmt;
            if (rs.hasNext()) {
                stmt = rs.next();
            } else {
                qExec.close();
                conn.close();
                return r;
            }

            if (!rs.hasNext()) {
                Iterator<String> b = stmt.varNames();
                HashMap<String, String> map = new HashMap<>();

                while (b.hasNext()) {
                    String current = b.next();
                    RDFNode res = stmt.get(current);
                    map.put(current, res.toString());

                }
                r.addContent(key, map);

                qExec.close();
                conn.close();
                return r;
            }

            int i = 0;
            while (rs.hasNext()) {
                if (i != 0) {
                    stmt = rs.next();
                }
                Iterator<String> b = stmt.varNames();
                HashMap<String, String> map = new HashMap<>();

                while (b.hasNext()) {
                    String current = b.next();
                    RDFNode res = stmt.get(current);
                    map.put(current, res.toString());

                }
                complexList.add(map);
                i++;
            }

            qExec.close();
            conn.close();
            r.addList(key, complexList);
        }
        return r;
    }

    public ArrayList<String> getAllUuids() {
        RDFConnectionRemoteBuilder builder = RDFConnectionFuseki.create()
                .destination(sparqlHost);
        ArrayList<String> list = new ArrayList<>();

        try (RDFConnectionFuseki conn = (RDFConnectionFuseki) builder.build()) {
            Query query = queries.getAllDocs();
            ResultSet rs = conn.query(query).execSelect();
            while (rs.hasNext()) {

                QuerySolution qs = rs.next();
                list.add(qs.get("subject").toString());
            }
        }
        return list;
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


    public Boolean deleteDoc(String docId) {

        String query = queries.deleteDoc(docId, true, true);
        System.out.println(query);

        RDFConnectionRemoteBuilder builder = RDFConnectionFuseki.create()
                .destination(updateHost);
        try (RDFConnectionFuseki conn = (RDFConnectionFuseki) builder.build()) {
            UpdateRequest request = UpdateFactory.create();

            request.add(query);
            conn.update(request);
            return true;
        } catch (Exception e) {
            System.out.println("error:");
            System.out.println(e.getMessage());
            System.out.println("sparqlHost: " + this.sparqlHost);
            return false;
        }
    }

    public ArrayList<HashMap<String, String>> addArrayToParameter(HashMap<String, ArrayList<HashMap<String, String>>>  myObject, Query query, String key)  {
        RDFConnectionRemoteBuilder builder = RDFConnectionFuseki.create()
                .destination(sparqlHost);
        ArrayList<HashMap<String, String>> myArrayList = new ArrayList<>();

        try (RDFConnectionFuseki conn = (RDFConnectionFuseki) builder.build()) {
            QueryExecution qExec = conn.query(query);
            ResultSet rs = qExec.execSelect();
            QuerySolution stmt;
            HashMap<String, String> result = new HashMap<>();

            while (rs.hasNext()) {

                stmt = rs.next();
                Iterator<String> b = stmt.varNames();

                while (b.hasNext()) {
                    String current = b.next();
                    RDFNode res = stmt.get(current);

                    if (res.toString().contains("http://www.semanticweb.org/dmelo/ontologies/2020/7/untitled-ontology-151#ARE3SuppliedTitle")) {
                        result.put(current, "suppliedTitle");
                    } else if (res.toString().contains("http://www.semanticweb.org/dmelo/ontologies/2020/7/untitled-ontology-151#ARE2FormalTitle")) {
                        result.put(current, "formalTitle");

                    } else if (res.toString().contains("http://www.semanticweb.org/dmelo/ontologies/2020/7/untitled-ontology-151#Reference_code")) {
                        result.put(current, "referenceCode");
                    } else {
                        result.put(current, res.toString());
                    }
                }
                myArrayList.add(result);
            }

            conn.close();
            qExec.close();
        }
        myObject.put(key, myArrayList);
        return myArrayList;
    }
}



