package runner;

import queries.Queries;
import restservice.RestServiceApplication;
import showcase.Connection;
import showcase.CreateUuids;
import showcase.FillExamples;

public class Runner {


    private static final Connection cn = new Connection();
     private static final Queries queries = new Queries();
    public static final String DEFAULT_host = "http://fuseki:3030/";


    public static void main(String[] args) {
            org.apache.jena.query.ARQ.init();

        if (cn.getAllBaseUuids().size() == 0) {
            System.out.println("============================= Creating UUIDS ================================");
            CreateUuids.main(null);
        }
        if (cn.getAllMats().size() == 0) {
            System.out.println("============================= Filling Data ================================");
            FillExamples.main(null);
        }
        String[] a = {""};
        RestServiceApplication.main(a);
    }
}
