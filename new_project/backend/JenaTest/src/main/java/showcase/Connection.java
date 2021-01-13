package showcase;
import org.apache.jena.query.Query;
import org.apache.jena.query.QueryFactory;
import org.apache.jena.query.ReadWrite;
import org.apache.jena.query.ResultSetFormatter;
import org.apache.jena.rdf.model.*;
import org.apache.jena.rdfconnection.RDFConnection;
import org.apache.jena.rdfconnection.RDFConnectionFuseki;
import org.apache.jena.rdfconnection.RDFConnectionRemoteBuilder;



public class Connection {

    public static void main (String args[]) {
        RDFConnectionRemoteBuilder builder = RDFConnectionFuseki.create()
                .destination("http://localhost:3030/name/get");
        Query query = QueryFactory.create("SELECT * WHERE {\n" +
                "  ?sub ?pred ?obj .\n" +
                "} \n" +
                "LIMIT 100");

        try ( RDFConnectionFuseki conn = (RDFConnectionFuseki)builder.build() ) {
            //conn.queryResultSet(query, ResultSetFormatter::out);

            Model model = conn.fetch();
            //conn.query("SELECT * WHERE {\n" +
            //        "  ?sub ?pred ?obj .\n" +
            //        "} \n" +
             //       "LIMIT 10").execSelect();
            // list the statements in the graph
            StmtIterator iter = model.listStatements();

            int i = 0;
            // print out the predicate, subject and object of each statement
            while (iter.hasNext() && i<10) {
                Statement stmt      = iter.nextStatement();         // get next statement
                Resource subject   = stmt.getSubject();   // get the subject
                Property predicate = stmt.getPredicate(); // get the predicate
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
                i++;
            }

            //model.write(System.out);*/
        }
    }



}
