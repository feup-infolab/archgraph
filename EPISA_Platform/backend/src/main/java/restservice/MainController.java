package restservice;


import java.util.*;

import cclasses.RequestBodyClass;
import cclasses.ResponseClass;
import com.fasterxml.jackson.core.JsonProcessingException;
import com.fasterxml.jackson.databind.ObjectMapper;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;
import queries.Queries;
import operations.SPARQLOperations;

import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;
import operations.Insert;


@RestController
public class MainController {
    @Autowired
    private YAMLConfig myConfig;

    private final Queries queries = new Queries();

    @CrossOrigin 
    @RequestMapping("/")
    public String home() {

        return "my sparqlHost:" + myConfig.getSparqlHost();
    }

    @CrossOrigin 
    @GetMapping("/doc")
    public String document(@RequestParam(value = "id", defaultValue = "") String uuid) {
        SPARQLOperations conn = new SPARQLOperations(myConfig.getSparqlHost(), myConfig.getDataHost());
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
        rep = conn.obtainTotalResponse(queries.getConservationStatus(docid), "conservationStates", rep);
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

    @CrossOrigin 
    @GetMapping("/searchdoc")
    public String documentSummary(@RequestParam(value = "refcode", defaultValue = "") Object rcode) {
        String refcode = rcode.toString();
        refcode = "\"" + refcode + "\"";
        SPARQLOperations conn = new SPARQLOperations(myConfig.getSparqlHost(), myConfig.getDataHost());
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
        SPARQLOperations conn = new SPARQLOperations(myConfig.getSparqlHost(), myConfig.getDataHost());
        HashMap<String, Object> list = new HashMap<>();
        ResponseClass rep = new ResponseClass(list);
        rep = conn.obtainGeneralResponse(queries.getPerson(uuid), "person", rep);
        return rep;
    }

    @CrossOrigin 
    @GetMapping("/place")
    public ResponseClass place(@RequestParam(value = "id", defaultValue = "") String uuid) {
        SPARQLOperations conn = new SPARQLOperations(myConfig.getSparqlHost(), myConfig.getDataHost());
        HashMap<String, Object> list = new HashMap<>();
        ResponseClass rep = new ResponseClass(list);
        rep = conn.obtainGeneralResponse(queries.getPlace(uuid), "place", rep);
        return rep;
    }

    @CrossOrigin 
    @PostMapping("search")
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

        SPARQLOperations conn = new SPARQLOperations(myConfig.getSparqlHost(), myConfig.getDataHost());
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
    @PostMapping("insert")
    public ArrayList<Map> insert(@RequestBody HashMap<String, ArrayList<HashMap<String, String>>> insertForm) {

        Insert insertclass = new Insert(myConfig.getSparqlHost(), myConfig.getDataHost());

        insertclass.insert(insertForm);

        return null;


    }


    @CrossOrigin
    @GetMapping("/levelsdesc")
    public ArrayList<String> levels() {
        SPARQLOperations conn = new SPARQLOperations(myConfig.getSparqlHost(), myConfig.getDataHost());
        HashMap<String, ArrayList<String>> list = new HashMap<>();
        ArrayList<String> alist = new ArrayList<>();
        alist = conn.getAllLevelsOfDesc();
        return alist;
    }


}

