package restservice;

import java.util.*;

import model.Document;
import model.RequestBody;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.configurationprocessor.json.JSONArray;
import org.springframework.boot.configurationprocessor.json.JSONObject;
import org.springframework.http.HttpStatus;
import org.springframework.web.bind.annotation.*;
import org.springframework.web.server.ResponseStatusException;
import operations.Queries;
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
        return conn.executeQueryAndAddContent(queries.getAllLevelOfDescription(), null, null);
    }

    @CrossOrigin
    @PostMapping("/search")
    public String search(@org.springframework.web.bind.annotation.RequestBody RequestBody searchForm) throws Exception {
        SPARQLOperations conn = new SPARQLOperations(myConfig.getMyHost());
        ArrayList<JSONObject> myResult = new ArrayList<>();

        String refCode = searchForm.getRefCode();
        String descriptionLevel = searchForm.getDescriptionLevel();
        String relatedTo = searchForm.getRelatedTo();
        String title = searchForm.getTitle();

        ArrayList<HashMap<String, String>> myHashMap;
        myHashMap = conn.executeQueryAndAddContent(queries.getHeaderSummaryDoc(refCode, descriptionLevel, title), null, null);

        for (HashMap<String, String> myValue : myHashMap) {
            JSONObject doc = new JSONObject();
            String episaIdentifier = myValue.get("episaIdentifier");
            String dglabIdentifier = myValue.get("dglabIdentifier");

            doc.put("episaIdentifier", episaIdentifier);
            doc.put("dglabIdentifier", dglabIdentifier);

            ArrayList<String> titles = conn.obtainAColumn(queries.getTitles(episaIdentifier, dglabIdentifier));
            doc.put("titles", new JSONArray(titles));
            myResult.add(doc);
        }
        return myResult.toString();
    }

    @CrossOrigin
    @GetMapping("/doc")
    public HashMap<String, HashMap<String, ArrayList<HashMap<String, String>>>> document(@RequestParam(value = "id", defaultValue = "") String uuid) {
        SPARQLOperations conn = new SPARQLOperations(myConfig.getMyHost());
        Document doc = new Document(myConfig.getMyHost(), null, uuid);



        //        switch (arrayName) {
//            case 'descriptionLevel':
//                middleArray = 'DOC_IDENTITY';
//                break;

//        rep = conn.obtainTotalResponse(queries.getReproductionCondition(docId), "reproductionConditions", rep);

        return doc.getDocFromDatabase(conn);
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
    @DeleteMapping("/deletedoc/{uuid}")
    public HashMap<String, String> deleteDoc(@PathVariable String uuid) {
        Document doc = new Document(myConfig.getMyHost(), null, uuid);
        try {
            return doc.deleteDoc(uuid);
        } catch (Exception e) {
            System.out.println(e.getMessage());

            if (e.getMessage() != null) {
                throw new ResponseStatusException(HttpStatus.BAD_REQUEST, e.getMessage());
            } else {
                throw new ResponseStatusException(HttpStatus.BAD_REQUEST, "Some error occurred");
            }
        }
    }

    @CrossOrigin
    @PostMapping("/insert")
    @ResponseBody
    public HashMap<String, String> insert(@org.springframework.web.bind.annotation.RequestBody HashMap<String, HashMap<String, ArrayList<HashMap<String, String>>>> insertForm) {
        Document doc = new Document(myConfig.getMyHost(), insertForm, null);
        try {
            return doc.insert();
        } catch (Exception e) {
            System.out.println(e.getMessage());
            if (e.getMessage() != null) {
                throw new ResponseStatusException(HttpStatus.BAD_REQUEST, e.getMessage());
            } else {
                throw new ResponseStatusException(HttpStatus.BAD_REQUEST, "Some error occurred");
            }
        }
    }

    @CrossOrigin
    @PutMapping("/updatedoc/{uuid}")
    public String updateDoc(@PathVariable String uuid, @org.springframework.web.bind.annotation.RequestBody HashMap<String, HashMap<String, ArrayList<HashMap<String, String>>>> updateForm) {

        Document doc = new Document(myConfig.getMyHost(), updateForm, uuid);

        try {
            SPARQLOperations conn = new SPARQLOperations(myConfig.getMyHost());
            String myDocId = conn.obtainARecordOfAColumn(queries.getDocId(uuid));
            doc.setMyDocId(myDocId);
            JSONObject result = new JSONObject(doc.getDocContent());
            String message = doc.deleteSomeInformationAndUpdate().get("message");
            result.put("message", message);

            return result.toString();

        } catch (Exception e) {
            System.out.println(e.getMessage());

            if (e.getMessage() != null) {
                throw new ResponseStatusException(HttpStatus.BAD_REQUEST, e.getMessage());
            } else {
                throw new ResponseStatusException(HttpStatus.BAD_REQUEST, "Some error occurred");
            }
        }
    }

//    @CrossOrigin
//    @GetMapping("/person")
//    public HashMap<String, String>  person(@RequestParam(value = "id", defaultValue = "") String uuid) {
//        SPARQLOperations conn = new SPARQLOperations(myConfig.getMyHost());
//        HashMap<String, Object> list = new HashMap<>();
//        ResponseClass rep = new ResponseClass(list);
//        rep = conn.obtainGeneralResponse(queries.getPerson(uuid), "person", rep);
//        return rep;
//    }

//    @CrossOrigin
//    @GetMapping("/place")
//    public HashMap<String, String>  place(@RequestParam(value = "id", defaultValue = "") String uuid) {
//        SPARQLOperations conn = new SPARQLOperations(myConfig.getMyHost());
//        HashMap<String, Object> list = new HashMap<>();
//        ResponseClass rep = new ResponseClass(list);
//        rep = conn.obtainGeneralResponse(queries.getPlace(uuid), "place", rep);
//        return rep;
//    }

}