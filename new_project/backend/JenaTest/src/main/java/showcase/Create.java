package showcase;

import org.apache.jena.query.Query;
import org.apache.jena.query.QueryFactory;
import org.apache.jena.rdf.model.Model;
import org.apache.jena.rdf.model.Property;
import org.apache.jena.rdf.model.Resource;
import org.apache.jena.rdfconnection.RDFConnectionFuseki;
import org.apache.jena.rdfconnection.RDFConnectionRemoteBuilder;
import org.apache.jena.vocabulary.VCARD;

public class Create {

    static String personURI    = "http://erlangen-crm.org/200717/E999_Test";
    static String fullName     = "Test Name";



    public static void main(String args[]) {
        RDFConnectionRemoteBuilder builder = RDFConnectionFuseki.create()
                .destination("http://localhost:3030/name/data");
        //.destination("http://localhost:3030/name/sparql");


        try ( RDFConnectionFuseki conn = (RDFConnectionFuseki)builder.build() ) {
            Model model =conn.fetch();

            // create the resource
            Resource johnSmith = model.createResource(personURI);
            Property testprop = model.createProperty("http://www.w3.org/2004/02/skos/core#notation_test", "testprop");

            // add the property
            johnSmith.addProperty(testprop, fullName);

            System.out.println("object:");
            System.out.println(johnSmith);

            String prop = johnSmith.getRequiredProperty(testprop)
                    .getString();
            System.out.println("property:");
            System.out.println(prop);


            conn.put(model);
            conn.commit();


        }
    }
}
