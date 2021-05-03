package operations;

import cclasses.ResponseClass;
import org.apache.jena.query.*;
import org.apache.jena.rdf.model.*;
import org.apache.jena.rdfconnection.RDFConnectionFuseki;
import org.apache.jena.rdfconnection.RDFConnectionRemoteBuilder;
import org.apache.jena.update.UpdateFactory;
import org.apache.jena.update.UpdateRequest;
import org.springframework.boot.configurationprocessor.json.JSONArray;
import org.springframework.boot.configurationprocessor.json.JSONException;
import org.springframework.boot.configurationprocessor.json.JSONObject;
import queries.Queries;

import java.util.*;

public class SPARQLOperations {
    public Queries querier = new Queries();
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

    public ResponseClass obtainSummaryResponse(Query query, String key, ResponseClass r) {
        RDFConnectionRemoteBuilder builder = RDFConnectionFuseki.create()
                .destination(sparqlHost);

        try (RDFConnectionFuseki conn = (RDFConnectionFuseki) builder.build()) {

            QueryExecution qExec = conn.query(query);
            ResultSet rs = qExec.execSelect();
            QuerySolution stmt;
            if (rs.hasNext()) {
                stmt = rs.next();
                Iterator<String> b = stmt.varNames();

                while (b.hasNext()) {
                    String current = b.next();
                    RDFNode res = stmt.get(current);
                    r.putProperties(key, res.toString());
                }
                qExec.close();
                conn.close();
            } else {
                qExec.close();
                conn.close();
                return r;
            }
        }
        return r;
    }

    public ResponseClass obtainGeneralResponse(Query query, String key, ResponseClass r) {
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

    public JSONObject addContentToResponse(Query query, String key, JSONObject myJson) {
        RDFConnectionRemoteBuilder builder = RDFConnectionFuseki.create()
                .destination(sparqlHost);
        JSONObject myNewJson = new JSONObject();

        try (RDFConnectionFuseki conn = (RDFConnectionFuseki) builder.build()) {

            QueryExecution qExec = conn.query(query);
            ResultSet rs = qExec.execSelect();
            QuerySolution stmt;
            if (rs.hasNext()) {
                stmt = rs.next();
            } else {
                qExec.close();
                conn.close();
                if (myJson != null) {
                    return myJson;
                } else return myNewJson;
            }

            if (!rs.hasNext()) {
                Iterator<String> b = stmt.varNames();

                while (b.hasNext()) {
                    String current = b.next();
                    RDFNode res = stmt.get(current);
                    if (myJson != null) {
                        myJson.put(key, res.toString());
                    } else {
                        myNewJson.put(key, res.toString());
                    }

                }
                qExec.close();
                conn.close();
                if (myJson != null) {
                    return myJson;
                } else return myNewJson;
            }
//
//            int i = 0;
//            while (rs.hasNext()) {
//                if (i != 0) {
//                    stmt = rs.next();
//                }
//                Iterator<String> b = stmt.varNames();
//                JSONObject result2 = new JSONObject();
//
//
//                while (b.hasNext()) {
//                    String current = b.next();
//                    RDFNode res = stmt.get(current);
//                    result2.put(current, res.toString());
//
//
//                }
//                jsonArray.put(result2);
//                i++;
//            }
//
//            qExec.close();
//            conn.close();
//            result.put(key, jsonArray);

            if (myJson != null) {
                return myJson;
            } else return myNewJson;
        } catch (JSONException jsonException) {
            jsonException.printStackTrace();
        }

        if (myJson != null) {
            return myJson;
        } else return myNewJson;

    }


    public ArrayList<String> getAllUuids() {
        RDFConnectionRemoteBuilder builder = RDFConnectionFuseki.create()
                .destination(sparqlHost);
        ArrayList<String> list = new ArrayList<>();

        try (RDFConnectionFuseki conn = (RDFConnectionFuseki) builder.build()) {
            Query query = querier.getAllDocs();
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
            Query query = querier.getAllUuids();
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
            Query query = querier.getAllMater();
            ResultSet rs = conn.query(query).execSelect();
            while (rs.hasNext()) {

                QuerySolution qs = rs.next();
                list.add(qs.get("description").toString());
            }
        }
        return list;
    }

    public ArrayList<String> getAllLevelsOfDesc() {

        RDFConnectionRemoteBuilder builder = RDFConnectionFuseki.create()
                .destination(sparqlHost);
        ArrayList<String> list = new ArrayList<>();
        Query query = null;

        try (RDFConnectionFuseki conn = (RDFConnectionFuseki) builder.build()) {
            query = querier.getAllLevelofDescription();
            QueryExecution qExec = conn.query(query);
            ResultSet rs = qExec.execSelect();
            while (rs.hasNext()) {

                QuerySolution qs = rs.next();

                if (!list.contains(qs.get("label").toString())) {
                    list.add(qs.get("label").toString());
                }
            }
            conn.close();
            qExec.close();

        } catch (Exception e) {
            System.out.println("error:");
            System.out.println(e.getMessage());
            System.out.println("Query: " + query.toString());
            System.out.println("sparqlHost: " + this.sparqlHost);
        }
        return list;
    }

    public Boolean deleteDoc(String docId) {

        String query = querier.deleteDoc(docId, true, true);
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

    public JSONArray addJsonArray(JSONObject myObject, Query query, String key) throws JSONException {
        RDFConnectionRemoteBuilder builder = RDFConnectionFuseki.create()
                .destination(sparqlHost);
        JSONArray jsonArray = new JSONArray();

        try (RDFConnectionFuseki conn = (RDFConnectionFuseki) builder.build()) {
            QueryExecution qExec = conn.query(query);
            ResultSet rs = qExec.execSelect();
            QuerySolution stmt;
            JSONObject result = new JSONObject();

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
                jsonArray.put(result);
            }

            conn.close();
            qExec.close();
        } catch (JSONException e) {
            e.printStackTrace();
        }
        myObject.put(key, jsonArray);
        return jsonArray;
    }
}



