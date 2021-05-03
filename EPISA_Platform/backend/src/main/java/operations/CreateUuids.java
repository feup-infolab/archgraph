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
    public String updateHost;

    private final SPARQLOperations con;

    public CreateUuids(String defaultHost) {
        this.sparqlHost = defaultHost + "sparql";
        this.dataHost = defaultHost + "data";
        this.updateHost = defaultHost + "update";
        this.con = new SPARQLOperations(defaultHost);
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
                Properties properties = new Properties(model);
                Property testProp = properties.getHasUuid();
                UUID uuid = UUID.randomUUID();
                String uuidAsString = uuid.toString();
                res.addProperty(testProp, uuidAsString);
                conn.put(model);
            }
            conn.commit();
        }
    }
}


