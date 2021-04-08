package restservice;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import operations.SPARQLOperations;
import operations.CreateUuids;
import operations.FillExamples;

@SpringBootApplication
public class RestServiceApplication {

    public static final String Fuseki_host = "http://fuseki:3030/";
    public static String DEFAULT_host = "http://localhost:3030/";

    public static void main(String[] args) {

        if (args.length > 0) {
            if (args[0].equals("production")) {
                DEFAULT_host = Fuseki_host;
            }
        }
        SPARQLOperations cn = new SPARQLOperations(DEFAULT_host);
        System.err.println("============================= UUIDS ================================");

        System.err.println("IS THIS CHANGING?!");
        cn.importOWL();


        if (cn.getAllBaseUuids().size() == 0) {
            System.out.println("============================= Creating UUIDS ================================");
            CreateUuids create = new CreateUuids(DEFAULT_host);
            create.create();
        }
        if (cn.getAllMats().size() == 0) {
            System.out.println("============================= Filling Data ================================");
            FillExamples fillExamples = new FillExamples(DEFAULT_host);
            fillExamples.fill();
        }
        System.err.println("===========================IS THIS CHANGING?!==========================================");
        SpringApplication.run(RestServiceApplication.class, args);


    }
}
