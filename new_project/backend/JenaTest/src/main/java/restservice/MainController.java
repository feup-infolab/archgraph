package restservice;


import java.util.HashMap;
import java.util.concurrent.atomic.AtomicLong;

import cclasses.ResponseClass;
import com.fasterxml.jackson.core.JsonProcessingException;
import com.fasterxml.jackson.databind.ObjectMapper;
import org.springframework.web.bind.annotation.CrossOrigin;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;
import queries.Queries;
import showcase.Connection;

@RestController
public class MainController {

    private static final String template = "Hello, %s!";
    private final AtomicLong counter = new AtomicLong();
    private final Queries queries = new Queries();

    @CrossOrigin(origins = {"http://localhost:4200", "http://localhost:4201"})
    @GetMapping("/doc")
    public String document(@RequestParam(value = "id", defaultValue = "") String uuid) {
        Connection conn = new Connection();
        HashMap<String, Object> list = new HashMap<>();

        HashMap<String, Object> list0 = new HashMap<>();
        ResponseClass uuidrep = new ResponseClass(list0);
        conn.obtainGeneralResponse(queries.getIDd(uuid), "id", uuidrep);
        HashMap<String, String> idmap = (HashMap<String, String>) uuidrep.getProperties().get("id");
        String docid = "<" + idmap.get("description") + ">";

        ResponseClass rep = new ResponseClass(list);
        rep = conn.obtainSummaryResponse(queries.getUuid(docid), "episaIdentifier", rep);
        rep = conn.obtainTotalResponse(queries.getIdentifier(docid), "identifiers", rep);
        rep = conn.obtainTotalResponse(queries.getTitle(docid), "titles", rep);
        rep = conn.obtainTotalResponse(queries.getMaterial(docid), "materials", rep);
        rep = conn.obtainTotalResponse(queries.getDimension(docid), "dimensions", rep);
        rep = conn.obtainTotalResponse(queries.getQuantity(docid), "quantities", rep);
        rep = conn.obtainTotalResponse(queries.getConservationStatus(docid), "conservationStatus", rep);
        rep = conn.obtainTotalResponse(queries.getLanguage(docid), "languages", rep);
        rep = conn.obtainTotalResponse(queries.getWriting(docid), "writings", rep);
        rep = conn.obtainTotalResponse(queries.getDocTradition(docid), "documentaryTraditions", rep);
        rep = conn.obtainTotalResponse(queries.getDocTypology(docid), "typologies", rep);
        rep = conn.obtainTotalResponse(queries.getSubject(docid), "subjects", rep);
        rep = conn.obtainTotalResponse(queries.getAccessCondition(docid), "accessConditions", rep);
        rep = conn.obtainTotalResponse(queries.getReproductionCondition(docid), "reproductionConditions", rep);
        rep = conn.obtainTotalResponse(queries.getEvent(docid), "relatedEvents", rep);
        rep = conn.obtainTotalResponse(queries.getRelDoc(docid), "relatedDocuments", rep);


        ObjectMapper mapper = new ObjectMapper();
        String json = "";
        try {
            json = mapper.writeValueAsString(rep.getProperties());
        } catch (JsonProcessingException e) {
            e.printStackTrace();
        }
        return json;
    }

    @CrossOrigin(origins = {"http://localhost:4200", "http://localhost:4201"})
    @GetMapping("/searchdoc")
    public String documentSummary(@RequestParam(value = "refcode", defaultValue = "") Object rcode) {
        String refcode = rcode.toString();
        refcode = "\"" + refcode + "\"";
        Connection conn = new Connection();
        HashMap<String, Object> list0 = new HashMap<>();
        ResponseClass uuidrep = new ResponseClass(list0);
        conn.obtainGeneralResponse(queries.getIdFromReference_codes_query(refcode), "id", uuidrep);
        HashMap<String, String> idmap = (HashMap<String, String>) uuidrep.getProperties().get("id");
        String uuid = "<" + idmap.get("description") + ">";


        HashMap<String, Object> list = new HashMap<>();
        ResponseClass rep = new ResponseClass(list);
        rep = conn.obtainSummaryResponse(queries.getTitle_query(uuid), "title", rep);
        rep = conn.obtainSummaryResponse(queries.getUuid(uuid), "episaIdentifier", rep);
        rep = conn.obtainSummaryResponse(queries.getReference_codes_query(uuid), "dglabIdentifier", rep);

        ObjectMapper mapper = new ObjectMapper();
        String json = "";
        try {
            json = mapper.writeValueAsString(rep.getProperties());
            return json;
        } catch (JsonProcessingException e) {
            e.printStackTrace();
        }
        return json;
    }

    @CrossOrigin(origins = {"http://localhost:4200", "http://localhost:4201"})
    @GetMapping("/person")
    public ResponseClass person(@RequestParam(value = "id", defaultValue = "") String uuid) {
        Connection conn = new Connection();
        HashMap<String, Object> list = new HashMap<>();
        ResponseClass rep = new ResponseClass(list);
        rep = conn.obtainGeneralResponse(queries.getPerson(uuid), "person", rep);
        return rep;
    }

    @CrossOrigin(origins = {"http://localhost:4200", "http://localhost:4201"})
    @GetMapping("/place")
    public ResponseClass place(@RequestParam(value = "id", defaultValue = "") String uuid) {
        Connection conn = new Connection();
        HashMap<String, Object> list = new HashMap<>();
        ResponseClass rep = new ResponseClass(list);
        rep = conn.obtainGeneralResponse(queries.getPlace(uuid), "place", rep);
        return rep;
    }
}

