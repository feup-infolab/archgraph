package showcase;

import org.apache.jena.rdf.model.*;
import org.apache.jena.rdfconnection.RDFConnectionFuseki;
import org.apache.jena.rdfconnection.RDFConnectionRemoteBuilder;

public class Read {

    static String personURI = "http://erlangen-crm.org/200717/E999_Test";
    static String fullName = "John Smith";
    public String destination_port;


    public Read(String destination_port) {
        this.destination_port = destination_port + "name/get";
    }
    void read() {
        RDFConnectionRemoteBuilder builder = RDFConnectionFuseki.create()
                .destination(destination_port);


        try (RDFConnectionFuseki conn = (RDFConnectionFuseki) builder.build()) {
            Model model = conn.fetch();


            Resource resource = model.getResource(personURI);
            Property testprop = model.createProperty("http://www.w3.org/2004/02/skos/core#notation_test", "testprop");


            System.out.println("object:");
            System.out.println(resource);

            String prop = resource.getRequiredProperty(testprop)
                    .getString();
            System.out.println("property:");
            System.out.println(prop);

            System.out.println("------------------------------------------");


            StmtIterator iter = model.listStatements(resource, testprop, "Test Name");
            while (iter.hasNext()) {
                Statement stmt = iter.nextStatement();         // get next statement
                Resource subject = stmt.getSubject();   // get the subject
                Property predicate = stmt.getPredicate(); // get the predicate
                RDFNode object = stmt.getObject();    // get the object


                System.out.print(subject.toString());
                System.out.print(" " + predicate.toString() + " ");
                if (object instanceof Resource) {
                    System.out.print(object.toString());
                } else {
                    // object is a literal
                    System.out.print(" \"" + object.toString() + "\"");
                }
                System.out.println(" .");
            }


        }
    }
}
