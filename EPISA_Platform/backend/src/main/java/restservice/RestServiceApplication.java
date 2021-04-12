package restservice;

import operations.GlobalConstants;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import operations.SPARQLOperations;
import operations.CreateUuids;
import operations.FillExamples;

@SpringBootApplication
public class RestServiceApplication implements GlobalConstants {

    public static String sparqlHost;
    public static String dataHost;


    public static void main(String[] args) {

        sparqlHost = DEFAULTSparqlHost;
        dataHost = DEFAULTDataHost;
        if (args.length > 0) {
            if (args[0].equals("production")) {
                sparqlHost = FusekiSparqlHost;
                dataHost = FusekiDataHost;
            }
        }
        SPARQLOperations cn = new SPARQLOperations(sparqlHost, dataHost);
        System.err.println("============================= UUIDS ================================");

        cn.importOWL();


        if (cn.getAllBaseUuids().size() == 0) {
            System.out.println("============================= Creating UUIDS ================================");
            CreateUuids create = new CreateUuids(sparqlHost, dataHost);
            create.create();
        }
        if (cn.getAllMats().size() == 0) {
            System.out.println("============================= Filling Data ================================");
            FillExamples fillExamples = new FillExamples(sparqlHost, dataHost);
            fillExamples.fill();
        }
        System.err.println("===========================IS THIS CHANGING?!==========================================");
        SpringApplication.run(RestServiceApplication.class, args);


    }
}
