package restservice;

import utils.GlobalConstants;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import operations.SPARQLOperations;
import operations.CreateUuids;
import operations.FillExamples;

@SpringBootApplication
public class RestServiceApplication implements GlobalConstants {
    public static String myHost;


    public static void main(String[] args) {

        myHost = DEFAULTHost;
        if (args.length > 0) {
            if (args[0].equals("production")) {
                myHost = FusekiHost;
            }
        }
        SPARQLOperations cn = new SPARQLOperations(myHost);
        System.err.println("============================= UUIDS ================================");


        if (cn.getAllBaseUuids().size() == 0) {
            cn.importOWL();
            System.out.println("============================= Creating UUIDS ================================");
            CreateUuids create = new CreateUuids(myHost);
            create.create();
        }
        if (cn.getAllMats().size() == 0) {
            System.out.println("============================= Filling Data ================================");
            FillExamples fillExamples = new FillExamples(myHost);
            fillExamples.fill();
        }
        System.err.println("===========================IS THIS CHANGING?!==========================================");
        SpringApplication.run(RestServiceApplication.class, args);
    }
}
