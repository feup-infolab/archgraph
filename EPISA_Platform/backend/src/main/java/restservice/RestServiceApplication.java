package restservice;

import utils.GlobalConstants;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import operations.SPARQLOperations;
import operations.CreateUuids;

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

        System.err.println("===========================IS THIS CHANGING?!==========================================");
        SpringApplication.run(RestServiceApplication.class, args);
    }
}
