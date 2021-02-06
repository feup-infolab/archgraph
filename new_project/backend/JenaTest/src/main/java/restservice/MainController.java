package restservice;


    import java.util.HashMap;
    import java.util.concurrent.atomic.AtomicLong;

    import cclasses.ResponseClass;
    import com.fasterxml.jackson.core.JsonProcessingException;
    import com.fasterxml.jackson.databind.ObjectMapper;
    import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;
    import queries.Queries;
    import showcase.Connection;

@RestController
    public class MainController  {

        private static final String template = "Hello, %s!";
        private final AtomicLong counter = new AtomicLong();
        private final Queries queries =new Queries();

    @GetMapping("/doc")
    public String document(@RequestParam(value = "id", defaultValue = "") String uuid) {
        Connection conn = new Connection();
        HashMap<String,Object> list = new HashMap<>();

        HashMap<String,Object> list0 = new HashMap<>() ;
        ResponseClass uuidrep = new ResponseClass(list0);
        conn.obtainGeneralResponse(queries.getIDd(uuid),"id",uuidrep);
        HashMap<String,String > idmap = (HashMap<String, String>) uuidrep.getProperties().get("id");
        String docid = "<" + idmap.get("description")  + ">";

        ResponseClass rep = new ResponseClass( list);
        rep = conn.obtainGeneralResponse(queries.getTitle_query(docid),"title",rep);
        rep = conn.obtainGeneralResponse(queries.getUuid(docid),"episaIdentifier",rep);
        rep = conn.obtainGeneralResponse(queries.getReference_codes_query(docid),"dglabIdentifier",rep);

        ObjectMapper mapper = new ObjectMapper();
        String json = "";
        try {
            json = mapper.writeValueAsString(rep.getProperties());
        } catch (JsonProcessingException e) {
            e.printStackTrace();
        }
        return json;
    }

    @GetMapping("/searchdoc")
    public String documentSummary(@RequestParam(value = "refcode", defaultValue = "") String refcode) {
        Connection conn = new Connection();
        HashMap<String,Object> list0 = new HashMap<>() ;
        ResponseClass uuidrep = new ResponseClass(list0);
        conn.obtainGeneralResponse(queries.getIdFromReference_codes_query(refcode),"id",uuidrep);
        HashMap<String,String > idmap = (HashMap<String, String>) uuidrep.getProperties().get("id");
        String uuid = "<" + idmap.get("description")  + ">";


        HashMap<String,Object> list = new HashMap<>() ;
        ResponseClass rep = new ResponseClass( list);
        rep = conn.obtainSummaryResponse(queries.getTitle_query(uuid),"title",rep);
        rep = conn.obtainSummaryResponse(queries.getUuid(uuid),"episaIdentifier",rep);
        rep = conn.obtainSummaryResponse(queries.getReference_codes_query(uuid),"dglabIdentifier",rep);

        ObjectMapper mapper = new ObjectMapper();
        String json = "";
        try {
            json = mapper.writeValueAsString(rep.getProperties());
        } catch (JsonProcessingException e) {
            e.printStackTrace();
        }
        return json;
    }

    @GetMapping("/person")
    public ResponseClass person(@RequestParam(value = "id", defaultValue = "") String uuid) {
        Connection conn = new Connection();
        HashMap<String,Object> list = new HashMap<>() ;
        ResponseClass rep = new ResponseClass( list);
        rep = conn.obtainGeneralResponse(queries.getPerson(uuid),"person",rep);
        return rep;
    }

    @GetMapping("/place")
    public ResponseClass place(@RequestParam(value = "id", defaultValue = "") String uuid) {
        Connection conn = new Connection();
        HashMap<String,Object> list = new HashMap<>() ;
        ResponseClass rep = new ResponseClass( list);
        rep = conn.obtainGeneralResponse(queries.getPlace(uuid),"place",rep);
        return rep;
    }
}

