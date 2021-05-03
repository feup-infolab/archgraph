package restservice;

import java.util.*;

import cclasses.RequestBodyClass;
import cclasses.ResponseClass;
import com.fasterxml.jackson.core.JsonProcessingException;
import com.fasterxml.jackson.databind.ObjectMapper;
import operations.Insert;
import org.apache.jena.query.Query;
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
    private Object Json;

    @CrossOrigin
    @RequestMapping("/")
    public String home() {
        return "my sparqlHost:" + myConfig.getMyHost();
    }

    @CrossOrigin
    @GetMapping("/doc")
    public String document(@RequestParam(value = "id", defaultValue = "") String uuid) throws JSONException {
        SPARQLOperations conn = new SPARQLOperations(myConfig.getMyHost());
        JSONObject myJsonResult = new JSONObject();


        JSONObject myLocalJson =conn.addContentToResponse(queries.getIDd(uuid), "DocId", null);
        String docId = "<" + myLocalJson.get("DocId") + ">";

        conn.addContentToResponse(queries.getUuid(docId), "episaIdentifier", myJsonResult);
        addDocIdentity(conn, docId, myJsonResult);
        addDocContext(conn, docId, myJsonResult);
        addDocAccessUseConditions(conn, docId, myJsonResult);
        addDocLinkedData(conn, docId, myJsonResult);

        //        switch (arrayName) {
//            case 'descriptionLevel':
//                middleArray = 'DOC_IDENTITY';
//                break;

//        rep = conn.obtainTotalResponse(queries.getReproductionCondition(docId), "reproductionConditions", rep);

        return myJsonResult.toString();
    }


    @CrossOrigin
    @GetMapping("/searchdoc")
    public String documentSummary(@RequestParam(value = "refcode", defaultValue = "") Object rcode) {
        String refcode = rcode.toString();
        refcode = "\"" + refcode + "\"";
        SPARQLOperations conn = new SPARQLOperations(myConfig.getMyHost());
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

    @CrossOrigin
    @PostMapping("/search")
    public ArrayList<Map> search(@RequestBody RequestBodyClass searchForm) {

        String refcode = searchForm.getRefCode();
        if (refcode != null) {
            refcode = "\"" + refcode + "\"";
        } else {
            refcode = "\"\"";
        }

        String descriptionLevel = searchForm.getDescriptionLevel();
        if (descriptionLevel != null) {
            descriptionLevel = "\"" + descriptionLevel + "\"";
        } else {
            descriptionLevel = "\"\"";
        }

        String relatedTo = searchForm.getRelatedTo();
        if (relatedTo != null) {
            relatedTo = "\"" + relatedTo + "\"";
        } else {
            relatedTo = "\"\"";
        }

        String title = searchForm.getTitle();
        if (title != null) {
            title = "\"" + title + "\"";
        } else {
            title = "\"\"";
        }

        ArrayList<String> uuidList = new ArrayList<>();

        SPARQLOperations conn = new SPARQLOperations(myConfig.getMyHost());
        HashMap<String, Object> list0 = new HashMap<>();
        ResponseClass uuidrep = new ResponseClass(list0);
        conn.obtainGeneralResponse(queries.getIdFromLevelOfDescription(descriptionLevel), "levelOfDescriptionId", uuidrep);

        conn.obtainGeneralResponse(queries.getIdFromReference_codes_query(refcode), "ReferenceCodeId", uuidrep);


        conn.obtainGeneralResponse(queries.getIdFromRelDoc(relatedTo), "RelDocId", uuidrep);

        conn.obtainGeneralResponse(queries.getIdFromTitle(title), "Title", uuidrep);

        ArrayList<HashMap<String, String>> LODidmap = (ArrayList<HashMap<String, String>>) uuidrep.getProperties().get("levelOfDescriptionId");
        if (LODidmap != null) {
            for (HashMap<String, String> s : LODidmap) {
                String LODuuid = "<" + s.get("description") + ">";
                uuidList.add(LODuuid);
            }
        }

        HashMap<String, String> Refidmap = (HashMap<String, String>) uuidrep.getProperties().get("ReferenceCodeId");
        String Refuuid = "";
        if (Refidmap != null) {
            Refuuid = "<" + Refidmap.get("description") + ">";
        }

        HashMap<String, String> RDidmap = (HashMap<String, String>) uuidrep.getProperties().get("RelDocId");
        String RDuuid = "";
        if (RDidmap != null) {
            RDuuid = "<" + RDidmap.get("description") + ">";
        }

        HashMap<String, String> TitleIdMap = (HashMap<String, String>) uuidrep.getProperties().get("Title");
        String TitleId = "";
        if (TitleIdMap != null) {
            TitleId = "<" + TitleIdMap.get("description") + ">";
        }


        uuidList.add(Refuuid);
        uuidList.add(RDuuid);
        uuidList.add(TitleId);


        ArrayList<Map> reparray = new ArrayList<>();

        for (String s : uuidList) {
            if (!s.equals("")) {
                HashMap<String, Object> list = new HashMap<>();
                ResponseClass rep = new ResponseClass(list);
                rep = conn.obtainSummaryResponse(queries.getTitle_query(s), "title", rep);
                rep = conn.obtainSummaryResponse(queries.getUuid(s), "episaIdentifier", rep);
                rep = conn.obtainSummaryResponse(queries.getReference_codes_query(s), "dglabIdentifier", rep);
                reparray.add(rep.getProperties());
            }
        }

        return reparray;
    }

    @CrossOrigin
    @PostMapping("/insert")
    public HashMap<String, String> insert(@RequestBody HashMap<String, HashMap<String, ArrayList<HashMap<String, String>>>> insertForm) {
        Insert insertClass = new Insert(myConfig.getMyHost());
        return insertClass.insert(insertForm, false, null);
    }

    @CrossOrigin
    @GetMapping("/levelsdesc")
    public ArrayList<String> levels() {
        SPARQLOperations conn = new SPARQLOperations(myConfig.getMyHost());
        return conn.getAllLevelsOfDesc();
    }

    @CrossOrigin
    @PutMapping("/updatedoc/{uuid}")
    public Boolean updateDoc(@PathVariable String uuid, @RequestBody HashMap<String, HashMap<String, ArrayList<HashMap<String, String>>>> insertForm) {
        SPARQLOperations conn = new SPARQLOperations(myConfig.getMyHost());

        HashMap<String, Object> list0 = new HashMap<>();
        ResponseClass uuidrep = new ResponseClass(list0);
        conn.obtainGeneralResponse(queries.getIDd(uuid), "id", uuidrep);
        HashMap<String, String> idmap = (HashMap<String, String>) uuidrep.getProperties().get("id");
        String docid = "<" + idmap.get("DocId") + ">";
//        Insert insertclass = new Insert(myConfig.getMyHost());
//        insertclass.insert(insertForm, true, docid);

        SPARQLOperations conn2 = new SPARQLOperations(myConfig.getMyHost());

        conn2.deleteDoc(docid);
        Insert insertclass = new Insert(myConfig.getMyHost());
        insertclass.insert(insertForm, false, null);
        return true;
    }

    public void addDocContext(SPARQLOperations conn, String docId, JSONObject myJsonResult) throws JSONException {
        JSONObject DOC_CONTEXT = new JSONObject();
        myJsonResult.put("DOC_CONTEXT", DOC_CONTEXT);

        conn.addJsonArray(DOC_CONTEXT, queries.getSubject(docId), "subjects");
        conn.addJsonArray(DOC_CONTEXT, queries.getWriting(docId), "writings");
        conn.addJsonArray(DOC_CONTEXT, queries.getDocTypology(docId), "typologies");
        conn.addJsonArray(DOC_CONTEXT, queries.getConservationStatus(docId), "conservationStates");
        conn.addJsonArray(DOC_CONTEXT, queries.getDocTradition(docId), "documentaryTraditions");
    }

    private void addDocIdentity(SPARQLOperations conn, String docId, JSONObject myJsonResult) throws JSONException {
        JSONObject DOC_IDENTITY = new JSONObject();
        myJsonResult.put("DOC_IDENTITY", DOC_IDENTITY);

        conn.addJsonArray(DOC_IDENTITY, queries.getIdentifier(docId), "identifiers");
        conn.addJsonArray(DOC_IDENTITY, queries.getTitle(docId), "titles");
        conn.addJsonArray(DOC_IDENTITY, queries.getMaterial(docId), "materials");
        conn.addJsonArray(DOC_IDENTITY, queries.getDimension(docId), "dimensions");
        conn.addJsonArray(DOC_IDENTITY, queries.getQuantity(docId), "quantities");
    }

    private void addDocAccessUseConditions(SPARQLOperations conn, String docid, JSONObject myJsonResult) throws JSONException {
        JSONObject DOC_ACCESS_USE_CONDITIONS = new JSONObject();
        myJsonResult.put("DOC_CONTEXT", DOC_ACCESS_USE_CONDITIONS);

        conn.addJsonArray(DOC_ACCESS_USE_CONDITIONS, queries.getAccessCondition(docid), "accessConditions");
        conn.addJsonArray(DOC_ACCESS_USE_CONDITIONS, queries.getLanguage(docid), "languages");
    }

    private void addDocLinkedData(SPARQLOperations conn, String docid, JSONObject myJsonResult) throws JSONException {
        JSONObject DOC_LINKED_DATA = new JSONObject();
        myJsonResult.put("DOC_LINKED_DATA", DOC_LINKED_DATA);

        conn.addJsonArray(DOC_LINKED_DATA, queries.getRelatedDoc(docid), "relatedDocs");
        conn.addJsonArray(DOC_LINKED_DATA, queries.getRelatedEvent(docid), "relatedEvents");
    }
}