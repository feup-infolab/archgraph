package showcase;

import org.apache.jena.query.Query;
import org.apache.jena.query.QueryFactory;
import org.apache.jena.rdf.model.Model;
import org.apache.jena.rdf.model.Property;
import org.apache.jena.rdf.model.Resource;
import org.apache.jena.rdfconnection.RDFConnectionFuseki;
import org.apache.jena.rdfconnection.RDFConnectionRemoteBuilder;
import org.apache.jena.vocabulary.VCARD;

import java.util.ArrayList;
import java.util.UUID;

public class CreateUuids {

    static String personURI = "http://erlangen-crm.org/200717/E999_Test";
    static String fullName = "Test Name";
    public String destination_port;

    private final Connection con;

    public CreateUuids(String host) {
        this.destination_port = host;
        //+ "name/data";
        this.con = new Connection(this.destination_port);
    }

    public void create() {
        ArrayList<String> namelist = con.getAllUuids();

        RDFConnectionRemoteBuilder builder = RDFConnectionFuseki.create()
                .destination(destination_port + "/name/data");


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
