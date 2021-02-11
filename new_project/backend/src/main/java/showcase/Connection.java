package showcase;
import cclasses.ResponseClass;
import org.apache.jena.query.*;
import org.apache.jena.rdf.model.*;
import org.apache.jena.rdfconnection.RDFConnectionFuseki;
import org.apache.jena.rdfconnection.RDFConnectionRemoteBuilder;
import queries.Queries;

import java.util.*;


public class Connection {
    Queries querier = new Queries();


    public ResponseClass obtainSummaryResponse(Query query,String key,ResponseClass r){
        RDFConnectionRemoteBuilder builder = RDFConnectionFuseki.create()
                .destination("http://localhost:3030/name/sparql");


        try ( RDFConnectionFuseki conn = (RDFConnectionFuseki)builder.build() ) {
            QueryExecution qExec = conn.query(query) ;
            ResultSet rs = qExec.execSelect();
            QuerySolution stmt;
            if(rs.hasNext()){
                stmt = rs.next();
                Iterator<String> b = stmt.varNames();

                while(b.hasNext()){
                    String current = b.next();
                    RDFNode res = stmt.get(current);
                    r.putProperties(key,res.toString());

                }
                qExec.close();
                conn.close();
            }else{
                qExec.close();
                conn.close();
                return r;
            }
        }

            return r;
    }


    public ResponseClass obtainTotalResponse(Query query,String key,ResponseClass r){
        RDFConnectionRemoteBuilder builder = RDFConnectionFuseki.create()
                .destination("http://localhost:3030/name/sparql");


        try ( RDFConnectionFuseki conn = (RDFConnectionFuseki)builder.build() ) {

            QueryExecution qExec = conn.query(query) ;
            ResultSet rs = qExec.execSelect();
            ArrayList<Map<String,String>> complexList = new ArrayList<>();
            QuerySolution stmt;

            while (rs.hasNext()) {

                stmt = rs.next();
                Iterator<String> b = stmt.varNames();
                HashMap<String, String> map = new HashMap<>();

                while (b.hasNext()) {
                    String current = b.next();
                    RDFNode res = stmt.get(current);

                    //TODO - MUDAR ISTO - DEMASIADO ESPECIFICO
                    if(res.toString().contains("http://www.semanticweb.org/dmelo/ontologies/2020/7/untitled-ontology-151#ARE3SuppliedTitle")){
                        map.put(current, "Atribuído");
                    } else if(res.toString().contains("http://www.semanticweb.org/dmelo/ontologies/2020/7/untitled-ontology-151#ARE2FormalTitle")){
                        map.put(current, "Formal");
                    }else{
                        map.put(current, res.toString());
                    }
                }
                complexList.add(map);
            }

            qExec.close();
            conn.close();
            r.addList(key,complexList);
        }
        return r;
    }

    public ResponseClass obtainGeneralResponse(Query query,String key,ResponseClass r){
        RDFConnectionRemoteBuilder builder = RDFConnectionFuseki.create()
                .destination("http://localhost:3030/name/sparql");


        try ( RDFConnectionFuseki conn = (RDFConnectionFuseki)builder.build() ) {

            QueryExecution qExec = conn.query(query) ;
            ResultSet rs = qExec.execSelect();
            ArrayList<Map<String,String>> complexList = new ArrayList<>();
            QuerySolution stmt;
            if(rs.hasNext()){
                stmt = rs.next();
            }else{
                qExec.close();
                conn.close();
                return r;
            }

            //TODO CLEAN INTO 2 FUNCTIONS
            if(!rs.hasNext()){
                Iterator<String> b = stmt.varNames();
                HashMap<String,String> map = new HashMap<>();

                while(b.hasNext()){
                    String current = b.next();
                    RDFNode res = stmt.get(current);
                    map.put(current,res.toString());

                }
                r.addContent(key,map);

                qExec.close();
                conn.close();
                return r;
            }

            int i;
            i = 0;
            while (rs.hasNext()) {
                if (i != 0){
                stmt = rs.next();}
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
            r.addList(key,complexList);
            }
            return r;
    }

    public ArrayList<String> getAllUuids(){
        RDFConnectionRemoteBuilder builder = RDFConnectionFuseki.create()
                .destination("http://localhost:3030/name/sparql");
        ArrayList<String> list = new ArrayList<>();

        try ( RDFConnectionFuseki conn = (RDFConnectionFuseki)builder.build() ) {
            Query query = querier.getAllDocs();
            ResultSet rs = conn.query(query).execSelect();
            while (rs.hasNext()) {

                QuerySolution qs = rs.next();

                list.add(qs.get("subject").toString());

            }
        }
        return list;
    }


}



