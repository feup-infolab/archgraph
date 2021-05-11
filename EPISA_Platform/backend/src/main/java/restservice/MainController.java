package restservice;

import java.util.*;

import cclasses.RequestBodyClass;
import cclasses.ResponseClass;
import operations.Insert;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.configurationprocessor.json.JSONException;
import org.springframework.boot.configurationprocessor.json.JSONObject;
import org.springframework.web.bind.annotation.*;
import queries.Queries;
import operations.SPARQLOperations;

import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;


@RestController
public class MainController {
    @Autowired
    private YAMLConfig myConfig;
    private final Queries queries = new Queries();

    @CrossOrigin
    @RequestMapping("/")
    public String home() {
        return "my sparqlHost:" + myConfig.getMyHost();
    }

    @CrossOrigin
    @GetMapping("/levelsdesc")
    public ArrayList<HashMap<String, String>> levels() {
        SPARQLOperations conn = new SPARQLOperations(myConfig.getMyHost());
        return conn.obtainSummaryResponse(queries.getAllLevelOfDescription());
    }

    @CrossOrigin
    @PostMapping("/search")
    public ArrayList<HashMap<String, String>> search(@RequestBody RequestBodyClass searchForm) {
        SPARQLOperations conn = new SPARQLOperations(myConfig.getMyHost());

        String refCode = searchForm.getRefCode();
        String descriptionLevel = searchForm.getDescriptionLevel();
        String relatedTo = searchForm.getRelatedTo();
        String title = searchForm.getTitle();

        return conn.obtainSummaryResponse(queries.getSummaryDoc(refCode, descriptionLevel, title));
    }

    @CrossOrigin
    @GetMapping("/doc")
    public HashMap<String, HashMap<String, ArrayList<HashMap<String, String>>>> document(@RequestParam(value = "id", defaultValue = "") String uuid) throws JSONException {
        SPARQLOperations conn = new SPARQLOperations(myConfig.getMyHost());
        HashMap<String, HashMap<String, ArrayList<HashMap<String, String>>>> myHashMap = new HashMap<>();

        addDocIdentity(conn, uuid, myHashMap);
        addDocContext(conn, uuid, myHashMap);
        addDocAccessUseConditions(conn, uuid, myHashMap);
        addDocLinkedData(conn, uuid, myHashMap);

        //        switch (arrayName) {
//            case 'descriptionLevel':
//                middleArray = 'DOC_IDENTITY';
//                break;

//        rep = conn.obtainTotalResponse(queries.getReproductionCondition(docId), "reproductionConditions", rep);

        return myHashMap;
    }

//
//    @CrossOrigin
//    @GetMapping("/searchdoc")
//    public String documentSummary(@RequestParam(value = "refcode", defaultValue = "") Object rcode) {
//        String refcode = rcode.toString();
//        refcode = "\"" + refcode + "\"";
//        SPARQLOperations conn = new SPARQLOperations(myConfig.getMyHost());
//        HashMap<String, Object> list0 = new HashMap<>();
//        ResponseClass uuidrep = new ResponseClass(list0);
//        conn.obtainGeneralResponse(queries.getIdFromReference_codes_query(refcode), "id", uuidrep);
//        HashMap<String, String> idmap = (HashMap<String, String>) uuidrep.getProperties().get("id");
//        String uuid = "<" + idmap.get("description") + ">";
//
//
//        HashMap<String, Object> list = new HashMap<>();
//        ResponseClass rep = new ResponseClass(list);
//
//        rep = conn.obtainSummaryResponse(queries.getTitle_query(uuid), "title", rep);
//        rep = conn.obtainSummaryResponse(queries.getUuid(uuid), "episaIdentifier", rep);
//        rep = conn.obtainSummaryResponse(queries.getReference_codes_query(uuid), "dglabIdentifier", rep);
//
//        ObjectMapper mapper = new ObjectMapper();
//        String json = "";
//        try {
//            json = mapper.writeValueAsString(rep.getProperties());
//            return json;
//        } catch (JsonProcessingException e) {
//            e.printStackTrace();
//        }
//        return json;
//    }

    @CrossOrigin
    @PostMapping("/insert")
    public HashMap<String, String> insert(@RequestBody HashMap<String, HashMap<String, ArrayList<HashMap<String, String>>>> insertForm) throws JSONException {
        Insert insertClass = new Insert(myConfig.getMyHost());
        return insertClass.insert(insertForm, false, null);
    }

//    @CrossOrigin
//    @PutMapping("/updatedoc/{uuid}")
//    public Boolean updateDoc(@PathVariable String uuid, @RequestBody HashMap<String, HashMap<String, ArrayList<HashMap<String, String>>>> insertForm) {
//        SPARQLOperations conn = new SPARQLOperations(myConfig.getMyHost());
//
//        HashMap<String, Object> list0 = new HashMap<>();
//        ResponseClass uuidrep = new ResponseClass(list0);
//
////        Insert insertclass = new Insert(myConfig.getMyHost());
////        insertclass.insert(insertForm, true, uuid);
//
//        SPARQLOperations conn2 = new SPARQLOperations(myConfig.getMyHost());
//
//        conn2.deleteDoc(uuid);
//        Insert insertclass = new Insert(myConfig.getMyHost());
//        insertclass.insert(insertForm, false, null);
//        return true;
//    }

    @CrossOrigin
    @GetMapping("/person")
    public ResponseClass person(@RequestParam(value = "id", defaultValue = "") String uuid) {
        SPARQLOperations conn = new SPARQLOperations(myConfig.getMyHost());
        HashMap<String, Object> list = new HashMap<>();
        ResponseClass rep = new ResponseClass(list);
        rep = conn.obtainGeneralResponse(queries.getPerson(uuid), "person", rep);
        return rep;
    }

    @CrossOrigin
    @GetMapping("/place")
    public ResponseClass place(@RequestParam(value = "id", defaultValue = "") String uuid) {
        SPARQLOperations conn = new SPARQLOperations(myConfig.getMyHost());
        HashMap<String, Object> list = new HashMap<>();
        ResponseClass rep = new ResponseClass(list);
        rep = conn.obtainGeneralResponse(queries.getPlace(uuid), "place", rep);
        return rep;
    }

    public void addDocContext(SPARQLOperations conn, String uuid, HashMap<String, HashMap<String, ArrayList<HashMap<String, String>>>> myHashMapResult) throws JSONException {
        HashMap<String, ArrayList<HashMap<String, String>>> DOC_CONTEXT = new HashMap<>();
        myHashMapResult.put("DOC_CONTEXT", DOC_CONTEXT);

        conn.addArrayToParameter(DOC_CONTEXT, queries.getSubject(uuid), "subjects");
        conn.addArrayToParameter(DOC_CONTEXT, queries.getWriting(uuid), "writings");
        conn.addArrayToParameter(DOC_CONTEXT, queries.getDocTypology(uuid), "typologies");
        conn.addArrayToParameter(DOC_CONTEXT, queries.getConservationStatus(uuid), "conservationStates");
        conn.addArrayToParameter(DOC_CONTEXT, queries.getDocTradition(uuid), "documentaryTraditions");
    }

    private void addDocIdentity(SPARQLOperations conn, String uuid, HashMap<String, HashMap<String, ArrayList<HashMap<String, String>>>> myHashMapResult) {
        HashMap<String, ArrayList<HashMap<String, String>>> DOC_IDENTITY = new HashMap<>();
        myHashMapResult.put("DOC_IDENTITY", DOC_IDENTITY);

        System.out.println(queries.getIdentifier(uuid));
        conn.addArrayToParameter(DOC_IDENTITY, queries.getIdentifier(uuid), "identifiers");
        conn.addArrayToParameter(DOC_IDENTITY, queries.getLevel_of_description_query(uuid), "descriptionLevel");

        conn.addArrayToParameter(DOC_IDENTITY, queries.getTitle(uuid), "titles");
        conn.addArrayToParameter(DOC_IDENTITY, queries.getMaterial(uuid), "materials");
        conn.addArrayToParameter(DOC_IDENTITY, queries.getDimension(uuid), "dimensions");
        conn.addArrayToParameter(DOC_IDENTITY, queries.getQuantity(uuid), "quantities");
    }

    private void addDocAccessUseConditions(SPARQLOperations conn, String uuid, HashMap<String, HashMap<String, ArrayList<HashMap<String, String>>>> myHashMapResult) {
        HashMap<String, ArrayList<HashMap<String, String>>> DOC_ACCESS_USE_CONDITIONS = new HashMap<>();
        myHashMapResult.put("DOC_ACCESS_USE_CONDITIONS", DOC_ACCESS_USE_CONDITIONS);

        conn.addArrayToParameter(DOC_ACCESS_USE_CONDITIONS, queries.getAccessCondition(uuid), "accessConditions");
        conn.addArrayToParameter(DOC_ACCESS_USE_CONDITIONS, queries.getLanguage(uuid), "languages");
    }

    private void addDocLinkedData(SPARQLOperations conn, String uuid, HashMap<String, HashMap<String, ArrayList<HashMap<String, String>>>> myHashMapResult) {
        HashMap<String, ArrayList<HashMap<String, String>>> DOC_LINKED_DATA = new HashMap<>();
        myHashMapResult.put("DOC_LINKED_DATA", DOC_LINKED_DATA);

        conn.addArrayToParameter(DOC_LINKED_DATA, queries.getRelatedDoc(uuid), "relatedDocs");
        conn.addArrayToParameter(DOC_LINKED_DATA, queries.getRelatedEvent(uuid), "relatedEvents");
    }
}