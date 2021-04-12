package operations;

import org.apache.jena.rdf.model.Model;
import org.apache.jena.rdf.model.Property;
import org.apache.jena.rdf.model.Resource;
import org.apache.jena.rdfconnection.RDFConnectionFuseki;
import org.apache.jena.rdfconnection.RDFConnectionRemoteBuilder;

import java.util.ArrayList;
import java.util.UUID;

public class CreateUuids {

    public String sparqlHost;
    public String dataHost;

    private final SPARQLOperations con;

    public CreateUuids(String sparqlHost, String dataHost) {
        this.sparqlHost = sparqlHost;
        this.dataHost = dataHost;
        this.con = new SPARQLOperations( sparqlHost, dataHost);
    }

    public void create() {
        ArrayList<String> namelist = con.getAllUuids();

        RDFConnectionRemoteBuilder builder = RDFConnectionFuseki.create()
                .destination(dataHost);


        try (RDFConnectionFuseki conn = (RDFConnectionFuseki) builder.build()) {
            Model model = conn.fetch();

            // create the resource
            for (String s : namelist) {
                Resource res = model.getResource(s);
                Property testprop = model.createProperty("http://erlangen-crm.org/200717/", "has_uuid");
                UUID uuid = UUID.randomUUID();
                String uuidAsString = uuid.toString();
                res.addProperty(testprop, uuidAsString);
                conn.put(model);
            }
            conn.commit();
        }

    }
}


