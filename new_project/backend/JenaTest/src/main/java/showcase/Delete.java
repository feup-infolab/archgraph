package showcase;

import org.apache.jena.rdf.model.*;
import org.apache.jena.rdfconnection.RDFConnectionFuseki;
import org.apache.jena.rdfconnection.RDFConnectionRemoteBuilder;

import java.util.List;

public class Delete {

    static String personURI    = "http://erlangen-crm.org/200717/E999_Test";
    public static void main(String args[]) {
        RDFConnectionRemoteBuilder builder = RDFConnectionFuseki.create()
                .destination("http://localhost:3030/name/data");
        //.destination("http://localhost:3030/name/sparql");


        try ( RDFConnectionFuseki conn = (RDFConnectionFuseki)builder.build() ) {
            Model model =conn.fetch();


            Resource resource = model.getResource(personURI);
            Property testprop = model.createProperty("http://www.w3.org/2004/02/skos/core#notation_test", "testprop");
            //StmtIterator iter2 = model.listStatements(resource,testprop,"Different Test");
            StmtIterator iter2 = model.listStatements(resource,testprop,"Test Name");



            model.remove(iter2.nextStatement());

            StmtIterator iter = model.listStatements(resource,testprop,"Test Name");

            System.out.println("First Iter ---------------------");
            while (iter.hasNext()) {
                Statement stmt      = iter.nextStatement();         // get next statement
                Resource  subject   = stmt.getSubject();   // get the subject
                Property  predicate = stmt.getPredicate(); // get the predicate
                RDFNode   object    = stmt.getObject();    // get the object

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
            conn.put(model);
            conn.commit();
        }
    }
}