package runner;

import restservice.RestServiceApplication;
import showcase.Connection;
import showcase.CreateUuids;
import showcase.FillExamples;

public class Runner {


    // private static final Connection cn = new Connection();
    //    private static final Queries queries = new Queries();
    public static final String Fuseki_host = "http://fuseki:3030/";
    public static String DEFAULT_host = "http://localhost:3030/";



    public static void main(String[] args) throws InterruptedException {
        if(args.length>0){
            if (args[0].equals("production")) {
                DEFAULT_host = Fuseki_host;
            }
        }

        org.apache.jena.query.ARQ.init();
        Connection cn = new Connection(DEFAULT_host);

        if (cn.getAllBaseUuids().size() == 0) {
            System.out.println("============================= Creating UUIDS ================================");
            CreateUuids create = new CreateUuids(DEFAULT_host);
            //create.create();
        }
        if (cn.getAllMats().size() == 0) {
            System.out.println("============================= Filling Data ================================");
            FillExamples fillExamples = new FillExamples(DEFAULT_host);
            //fillExamples.fill();
        }
        String[] a = {""};
        RestServiceApplication.main(a);
    }
}
