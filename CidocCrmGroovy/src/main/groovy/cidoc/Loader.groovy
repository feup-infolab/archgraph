package cidoc

import cidoc.nodeEntities.AE1_Level_of_Description
import cidoc.nodeEntities.E10_Transfer_of_Custody
import cidoc.nodeEntities.E12_Production
import cidoc.nodeEntities.E21_Person
import cidoc.nodeEntities.E22_E33
import cidoc.nodeEntities.E22_E38
import cidoc.nodeEntities.E22_ManMade_Object
import cidoc.nodeEntities.E28_Conceptual_Object
import cidoc.nodeEntities.E33_Linguistic_Object
import cidoc.nodeEntities.E35_Title
import cidoc.nodeEntities.E40_Legal_Body
import cidoc.nodeEntities.E41_Appellation
import cidoc.nodeEntities.E42_Identifier
import cidoc.nodeEntities.E52_Time_Span
import cidoc.nodeEntities.E53_Place
import cidoc.nodeEntities.E54_Dimension
import cidoc.nodeEntities.E55_Type
import cidoc.nodeEntities.E56_Language
import cidoc.nodeEntities.E5_Event
import cidoc.nodeEntities.E74_Group
import cidoc.nodeEntities.E7_Activity
import cidoc.nodeEntities.E84_E33
import cidoc.nodeEntities.Entity
import cidoc.nodeEntities.PC14_Carried_Out_By
import cidoc.nodeEntities.Xsd_Date
import cidoc.nodeEntities.Xsd_Integer
import cidoc.nodeEntities.Xsd_String
import cidoc.nodeTraits.E12_Production_T
import cidoc.nodeTraits.E1_CRM_Entity_T
import groovy.json.JsonOutput
import groovy.json.JsonSlurper
import groovy.transform.CompileDynamic
import groovy.transform.CompileStatic
import org.neo4j.ogm.session.Session
import org.neo4j.ogm.config.Configuration
import org.neo4j.ogm.session.SessionFactory
import org.neo4j.ogm.transaction.Transaction

import java.lang.reflect.Array

@CompileStatic
class Loader {

    private final SessionFactory sessionFactory

    static private final String SERVER_URI = "bolt://localhost:11001"
    static private final String SERVER_USERNAME = "neo4j"
    static private final String SERVER_PASSWORD = "password"


    Loader() {

        Configuration configuration = new Configuration.Builder().uri(SERVER_URI).credentials(SERVER_USERNAME, SERVER_PASSWORD).build()
        sessionFactory = new SessionFactory(configuration, "cidoc.nodeEntities","cidoc.relationshipEntities")
    }

    Session getNeo4jSession() {
        return sessionFactory.openSession()
    }


    void process () {
        Session session = getNeo4jSession()
        session.purgeDatabase()

        //loadApocalipse(session)

        loadApArchive(session)
        //Iterable<Entity> t = query6(session,"E12_Production")
        String json = jsonQuery(session)
        println(json)
        json = json.substring(1,json.size())
        String jsonLd = jsonToJsonLd(session,json)
        session.purgeDatabase()
        loadJsonLd(session,jsonLd)

        Collection<Entity> entities = session.loadAll(Entity)

        println(entities[0])
        //session.delete(entities[0])



        /*Collection<Entity> test = session.loadAll(Entity)

        for(item in test){
        if(item  instanceof  E1_CRM_Entity_T){
            println(item)
        }}*/




        //loadJson(session,"{\"relationships\":[{\"fromNode\":{\"name\":\"Production of Apocalipse do Lorvão\",\"label\":\"E12_Production\",\"id\":194},\"type\":\"P21_had_general_purpose\",\"toNode\":{\"name\":\"Information dessimination\",\"label\":\"E55_Type\",\"id\":151}},{\"fromNode\":{\"name\":\"Production of Apocalipse do Lorvão\",\"label\":\"E12_Production\",\"id\":194},\"type\":\"P21_had_general_purpose\",\"toNode\":{\"name\":\"Preserving information\",\"label\":\"E55_Type\",\"id\":189}},{\"fromNode\":{\"name\":\"Production of Apocalipse do Lorvão\",\"label\":\"E12_Production\",\"id\":194},\"type\":\"P108_has_produced\",\"toNode\":{\"name\":\"Record\",\"label\":\"E84_E33\",\"id\":195}},{\"fromNode\":{\"name\":\"Production of Apocalipse do Lorvão\",\"label\":\"E12_Production\",\"id\":194},\"type\":\"P4_has_time_span\",\"toNode\":{\"name\":\"31-12-1189\",\"label\":\"Entity\",\"id\":192}},{\"fromNode\":{\"name\":\"P14 Carried Out By\",\"label\":\"PC14_Carried_Out_By\",\"id\":169},\"type\":\"P01_has_domain\",\"toNode\":{\"name\":\"Production of Apocalipse do Lorvão\",\"label\":\"E12_Production\",\"id\":194}},{\"fromNode\":{\"name\":\"P14 Carried Out By\",\"label\":\"PC14_Carried_Out_By\",\"id\":169},\"type\":\"P14.1_in_the_role_of\",\"toNode\":{\"name\":\"Material author\",\"label\":\"E55_Type\",\"id\":191}},{\"fromNode\":{\"name\":\"P14 Carried Out By\",\"label\":\"PC14_Carried_Out_By\",\"id\":169},\"type\":\"P02_has_range\",\"toNode\":{\"name\":\"Person\",\"label\":\"E21_Person\",\"id\":167}},{\"fromNode\":{\"name\":\"P14 Carried Out By\",\"label\":\"PC14_Carried_Out_By\",\"id\":168},\"type\":\"P01_has_domain\",\"toNode\":{\"name\":\"Production of Apocalipse do Lorvão\",\"label\":\"E12_Production\",\"id\":194}},{\"fromNode\":{\"name\":\"P14 Carried Out By\",\"label\":\"PC14_Carried_Out_By\",\"id\":168},\"type\":\"P02_has_range\",\"toNode\":{\"name\":\"Corporate body\",\"label\":\"E40_Legal_Body\",\"id\":161}},{\"fromNode\":{\"name\":\"P14 Carried Out By\",\"label\":\"PC14_Carried_Out_By\",\"id\":168},\"type\":\"P14.1_in_the_role_of\",\"toNode\":{\"name\":\"Creator\",\"label\":\"E55_Type\",\"id\":190}},{\"fromNode\":{\"name\":\"Record\",\"label\":\"E84_E33\",\"id\":195},\"type\":\"P102_has_title\",\"toNode\":{\"name\":\"Apocalipse do Lorvão\",\"label\":\"E35_Title\",\"id\":193}},{\"fromNode\":{\"name\":\"Person\",\"label\":\"E21_Person\",\"id\":167},\"type\":\"P1_is_identified_by\",\"toNode\":{\"name\":\"Egeas\",\"label\":\"E41_Appellation\",\"id\":166}},{\"fromNode\":{\"name\":\"Corporate body\",\"label\":\"E40_Legal_Body\",\"id\":161},\"type\":\"P1_is_identified_by\",\"toNode\":{\"name\":\"Ordem de Cister. Mosteiro de Lorvão. 878-1834\",\"label\":\"E42_Identifier\",\"id\":164}},{\"fromNode\":{\"name\":\"Transfer of Apocalipse do Lorvão\",\"label\":\"E10_Transfer_of_Custody\",\"id\":162},\"type\":\"P21_had_general_purpose\",\"toNode\":{\"name\":\"Preserving information\",\"label\":\"E55_Type\",\"id\":189}},{\"fromNode\":{\"name\":\"Transfer of Apocalipse do Lorvão\",\"label\":\"E10_Transfer_of_Custody\",\"id\":162},\"type\":\"P4_has_time_span\",\"toNode\":{\"name\":\"31-12-1853\",\"label\":\"Entity\",\"id\":102}},{\"fromNode\":{\"name\":\"Transfer of Apocalipse do Lorvão\",\"label\":\"E10_Transfer_of_Custody\",\"id\":162},\"type\":\"P28_custody_surrendered_by\",\"toNode\":{\"name\":\"Group\",\"label\":\"E74_Group\",\"id\":163}},{\"fromNode\":{\"name\":\"Transfer of Apocalipse do Lorvão\",\"label\":\"E10_Transfer_of_Custody\",\"id\":162},\"type\":\"P30_transferred_custody_of\",\"toNode\":{\"name\":\"Record\",\"label\":\"E84_E33\",\"id\":195}},{\"fromNode\":{\"name\":\"Transfer of Apocalipse do Lorvão\",\"label\":\"E10_Transfer_of_Custody\",\"id\":162},\"type\":\"P11_had_participant\",\"toNode\":{\"name\":\"Person\",\"label\":\"E21_Person\",\"id\":165}},{\"fromNode\":{\"name\":\"Transfer of Apocalipse do Lorvão\",\"label\":\"E10_Transfer_of_Custody\",\"id\":162},\"type\":\"P29_custody_received_by\",\"toNode\":{\"name\":\"Corporate body\",\"label\":\"E40_Legal_Body\",\"id\":160}},{\"fromNode\":{\"name\":\"Group\",\"label\":\"E74_Group\",\"id\":163},\"type\":\"P107_has_current_or_former_member\",\"toNode\":{\"name\":\"Corporate body\",\"label\":\"E40_Legal_Body\",\"id\":161}},{\"fromNode\":{\"name\":\"Person\",\"label\":\"E21_Person\",\"id\":165},\"type\":\"P1_is_identified_by\",\"toNode\":{\"name\":\"Alexandre Herculano\",\"label\":\"E41_Appellation\",\"id\":158}},{\"fromNode\":{\"name\":\"Corporate body\",\"label\":\"E40_Legal_Body\",\"id\":160},\"type\":\"P1_is_identified_by\",\"toNode\":{\"name\":\"Real Arquivo da Torre do Tombo\",\"label\":\"E41_Appellation\",\"id\":159}}],\"nodes\":[{\"name\":\"Production of Apocalipse do Lorvão\",\"id\":194,\"label\":[\"Entity\",\"E12_Production\"]},{\"name\":\"P14 Carried Out By\",\"id\":169,\"label\":[\"Entity\",\"PC14_Carried_Out_By\"]},{\"name\":\"P14 Carried Out By\",\"id\":168,\"label\":[\"Entity\",\"PC14_Carried_Out_By\"]},{\"name\":\"Information dessimination\",\"id\":151,\"label\":[\"Entity\",\"E55_Type\"]},{\"name\":\"Preserving information\",\"id\":189,\"label\":[\"Entity\",\"E55_Type\"]},{\"name\":\"Record\",\"id\":195,\"label\":[\"Entity\",\"E84_E33\"]},{\"name\":\"31-12-1189\",\"id\":192,\"label\":[\"E52_Time_Span\",\"Entity\"]},{\"name\":\"Material author\",\"id\":191,\"label\":[\"Entity\",\"E55_Type\"]},{\"name\":\"Person\",\"id\":167,\"label\":[\"Entity\",\"E21_Person\"]},{\"name\":\"Corporate body\",\"id\":161,\"label\":[\"Entity\",\"E40_Legal_Body\"]},{\"name\":\"Creator\",\"id\":190,\"label\":[\"Entity\",\"E55_Type\"]},{\"name\":\"Transfer of Apocalipse do Lorvão\",\"id\":162,\"label\":[\"Entity\",\"E10_Transfer_of_Custody\"]},{\"name\":\"Apocalipse do Lorvão\",\"id\":193,\"label\":[\"Entity\",\"E35_Title\"]},{\"name\":\"Egeas\",\"id\":166,\"label\":[\"Entity\",\"E41_Appellation\"]},{\"name\":\"Ordem de Cister. Mosteiro de Lorvão. 878-1834\",\"id\":164,\"label\":[\"Entity\",\"E42_Identifier\"]},{\"name\":\"Group\",\"id\":163,\"label\":[\"Entity\",\"E74_Group\"]},{\"name\":\"31-12-1853\",\"id\":102,\"label\":[\"E52_Time_Span\",\"Entity\"]},{\"name\":\"Person\",\"id\":165,\"label\":[\"Entity\",\"E21_Person\"]},{\"name\":\"Corporate body\",\"id\":160,\"label\":[\"Entity\",\"E40_Legal_Body\"]},{\"name\":\"Alexandre Herculano\",\"id\":158,\"label\":[\"Entity\",\"E41_Appellation\"]},{\"name\":\"Real Arquivo da Torre do Tombo\",\"id\":159,\"label\":[\"Entity\",\"E41_Appellation\"]}]}")
        //loadCalendario(session)

        //Iterable<Entity> en = queryTest(session)
        //Iterable<Entity> en2 = queryForTernary(session)

        //Iterable<Entity> en3 = queryAll(session)

        //println(json)
        //int t = en.size()
        //int t2 = en2.size()
        //int t3 = en3.size()

    }

     private Entity findById(ArrayList<Entity> entities, String name){
         for(int i = 0; i<entities.size(); i++){
             if(name == entities.get(i).name){
                 return entities.get(i)
             }
         }
     }


    @CompileDynamic
    private void addNode(Session session, String json){
        Transaction txn = session.beginTransaction()

        JsonSlurper slurper = new JsonSlurper()
        Map result = (Map) slurper.parseText(json)

        Entity instance = (Entity) Class.forName("cidoc.nodeEntities." + (String) result."@type").getDeclaredConstructor().newInstance()
        instance.setName((String) result._label)

        Set<String> keys = result.keySet()

        for(int i = 4; i< result.size(); i++){

            String property = keys[i]
            ArrayList relationsList = (ArrayList) result.get(property)

            for(int j = 0; j<relationsList.size();j++){
                Map relations = (Map) relationsList.get(j)
                String id = relations."@id"
                Entity targetNode = (Entity) session.load(Entity,id)


                String typeMin = property
                if(typeMin.indexOf(".")!= -1){
                    typeMin = typeMin.substring(0, typeMin.indexOf(".")) + "d" +  typeMin.substring(typeMin.indexOf(".")+1)
                }
                String typeMinimum = typeMin
                //TODO CHANGE THIS
                if(typeMin[0] != "A" || typeMin[1] !="P"){
                    typeMinimum = typeMin[0].toLowerCase() + typeMin.substring(1)}

                //understand if relation is one to on or many to many. This is done by understanding it it's possible to obtain ArrayList or by doing e1.p3 for example
                Object cidocProperty = instance."$typeMinimum"

                if(cidocProperty == null){
                    String method = "set" + typeMin
                    instance."$method"(targetNode)
                }else if(cidocProperty.class.toString() == "class java.util.ArrayList"){
                    ArrayList arrayProperty = (ArrayList) cidocProperty
                    arrayProperty.add(targetNode)
                }
            }
        }
        session.save(instance)

        txn.commit()

    }

    private void deleteNode(Session session, String json){
        Transaction txn = session.beginTransaction()

        JsonSlurper slurper = new JsonSlurper()
        Map result = (Map) slurper.parseText(json)
        String id = result."@id"
        Entity ent = session.load(Entity,id)
        session.delete(ent)

        txn.commit()

    }

    private void modifyNode(Session session, String json){
        //continue later
    }

    @CompileDynamic
     private void loadJson(Session session, String json){
         //Begin Neo4J Transaction
         Transaction txn = session.beginTransaction()

         //Obtain a Map with the Json contents, modify as necessary
         JsonSlurper slurper = new JsonSlurper()
         Map result = (Map) slurper.parseText(json)
         ArrayList nodes = (ArrayList) result.nodes
         ArrayList relationships = (ArrayList) result.relationships

         //Create a Map with the previous Ids as keys and the entities to be added as they are created (this is because the creation of the entities forces
         // new ids, and the OGM seems to take it as an update if the IDs are set to their old IDs)
         Map<Long,Entity> entities = new HashMap<>()


         //For cycle to create all Nodes
         for(int i = 0; i < nodes.size(); i++){
             Map entityMap =  (Map) nodes.get(i)
             ArrayList entityArray = (ArrayList) entityMap.label
             String entity = (String) entityArray.get(1)
             //Neo4j Java creation isnt always consistent, this makes sure the right entity gets created
             if(entity == "Entity"){
                 entity = (String) entityArray.get(0)
             }

             Entity instance = (Entity) Class.forName("cidoc.nodeEntities." + entity).getDeclaredConstructor().newInstance()
             instance.setName((String) entityMap.name)

             //put entitities on map alongside id
             entities.put((Long) entityMap.id,instance)


         }


        //For cycle to create relationships
         for(int i = 0; i< relationships.size(); i++){
             Map relationshipMap =(Map) relationships.get(i)
             Map fromNode = (Map) relationshipMap.fromNode
             Map toNode = (Map) relationshipMap.toNode
             String type = (String) relationshipMap.type
             //Obtain entities from map
            Entity e1 = entities.get((Long) fromNode.id)
            Entity e2 = entities.get((Long) toNode.id)

             //turn properties into method names for groovy. Example: P3_has_note into p3
            String typeMin = type
            if(typeMin.indexOf(".")!= -1){
                typeMin = typeMin.substring(0, typeMin.indexOf(".")) + "d" +  typeMin.substring(typeMin.indexOf(".")+1)
            }
            String typeMinimum = typeMin[0].toLowerCase() + typeMin.substring(1)

             //understand if relation is one to on or many to many. This is done by understanding it it's possible to obtain ArrayList or by doing e1.p3 for example
            Object cidocProperty = e1."$typeMinimum"

            if(cidocProperty == null){
                String method = "set" + typeMin
                e1."$method"(e2)
            }else if(cidocProperty.class.toString() == "class java.util.ArrayList"){
                ArrayList arrayProperty = (ArrayList) cidocProperty
                arrayProperty.add(e2)
            }

         }

         //saving of each of the entities
         entities.each {k, v ->session.save(v)}


         txn.commit()

    }

    @CompileDynamic
    void  loadJsonLd(Session session, String jsonld){

        Transaction txn = session.beginTransaction()

        session.purgeDatabase()
       // String json = jsonld.substring(1,jsonld.size())
        String json = "{ \"Jsonld\":" + jsonld + "}"
        JsonSlurper slurper = new JsonSlurper()
        Map result = (Map) slurper.parseText(json)
        ArrayList nodes = (ArrayList) result.Jsonld
        Map<Long,Entity> entities = new HashMap<>()

        for(int i =0; i< nodes.size(); i++){
            Map entityMap =  (Map) nodes.get(i)
            String entity =  entityMap."@type"

            if(entity == "Entity"){
                entity = "E52_Time_Span"
            }
            Entity instance

            if(!entities.containsKey((Long) entityMap."@id")){


            instance = (Entity) Class.forName("cidoc.nodeEntities." + entity).getDeclaredConstructor().newInstance()
            instance.setName((String) entityMap._label)

            }else{
                instance = entities.get((Long) entityMap."@id")
                instance.setName((String) entityMap._label)
            }


            Set<String> keys = entityMap.keySet()
            for(int j = 4; j< keys.size(); j++){
                String property = keys[j]
                ArrayList relationsList = (ArrayList) entityMap.get(property)

                for(int k = 0 ;k< relationsList.size(); k++){
                Map relations = (Map) relationsList.get(k)

                String entity2 =  relations."@type"

                if(entity2 == "Entity"){
                    entity2 = "E52_Time_Span"
                }

                Entity instance2

                if(!entities.containsKey((Long) relations."@id")){

                    instance2 = (Entity) Class.forName("cidoc.nodeEntities." + entity2).getDeclaredConstructor().newInstance()
                    //instance2.setName((String) relations._label)
                    entities.put((Long) relations."@id",instance2)

                }else{
                    instance2 = entities.get((Long) relations."@id")
                }



                //put entitities on map alongside id


                String typeMin = property
                if(typeMin.indexOf(".")!= -1){
                    typeMin = typeMin.substring(0, typeMin.indexOf(".")) + "d" +  typeMin.substring(typeMin.indexOf(".")+1)
                }
                String typeMinimum = typeMin
                    //TODO CHANGE THIS
                if(typeMin[0] != "A" || typeMin[1] !="P"){
                typeMinimum = typeMin[0].toLowerCase() + typeMin.substring(1)}

                //understand if relation is one to on or many to many. This is done by understanding it it's possible to obtain ArrayList or by doing e1.p3 for example
                Object cidocProperty = instance."$typeMinimum"

                if(cidocProperty == null){
                    String method = "set" + typeMin
                    instance."$method"(instance2)
                }else if(cidocProperty.class.toString() == "class java.util.ArrayList"){
                    ArrayList arrayProperty = (ArrayList) cidocProperty
                    arrayProperty.add(instance2)
                }
                }
            }

            entities.put((Long) entityMap."@id",instance)
            session.save(instance)
        }

        println(entities)
        //entities.each {k, v ->session.save(v)}


        txn.commit()
    }

    @CompileDynamic
    String getAllRelations(String entityType){

        ArrayList<String> propertyList = new ArrayList<>()
        Entity instance
        instance = (Entity) Class.forName("cidoc.nodeEntities." + entityType).getDeclaredConstructor().newInstance()

        //println(instance.getProperties().toString())
        Set propertySet = instance.getProperties().keySet()

        for(int i = 0; i < propertySet.size(); i++){
            String property = propertySet[i]
            def match = (property =~ /^a?p\d+_.*(?<!t)$/)
            def matchCapital = (property =~ /^A?P\d+_.*(?<!t)$/)
            if(match.size() > 0 ){
                int j = property.indexOf("p")
                String first = property.substring(0,j+1)
                first = first.toUpperCase()
                property = first + property.substring(j+1)


                propertyList.add(property)
            }else if(matchCapital.size() > 0){
                propertyList.add(property)
            }

        }

        String json = JsonOutput.toJson(propertyList)

        return json


    }

    @CompileDynamic
    String packCounterDomain(String json){
        JsonSlurper slurper = new JsonSlurper()
        Map result = (Map) slurper.parseText(json)
        Map ntargets
        ntargets = getCounterDomain((String) result.type,(String)result.rel,result)

        String response = JsonOutput.toJson(ntargets)
        return response
    }


    @CompileDynamic
    Map getCounterDomain(String entityType, String relation, Map targets){

        Map propertyList = new HashMap()
        Entity instance
        instance = (Entity) Class.forName("cidoc.nodeEntities." + entityType).getDeclaredConstructor().newInstance()


        String typeMinimum = relation[0].toLowerCase() + relation.substring(1)

        String typeMin = typeMinimum + "_t"
        if (typeMin.indexOf(".") != -1) {
            typeMin = typeMin.substring(0, typeMin.indexOf(".")) + "d" + typeMin.substring(typeMin.indexOf(".") + 1)
        }
        Object cidocProperty = instance."$typeMin"

        for(int i =0; i< targets.size()-2; i++){
            Map specificTarget = (Map) targets.get(i.toString())
            String targetType = specificTarget."@type"
            if(targetType == "Entity"){
                targetType = "E52_Time_Span"
            }
            Entity instance2 = (Entity) Class.forName("cidoc.nodeEntities." + targetType).getDeclaredConstructor().newInstance()
            if( instance2 in cidocProperty){
                propertyList.put(propertyList.size(),specificTarget)
            }

        }

        return propertyList

    }






    private String jsonToJsonLd(Session session, String json){

        ArrayList<Entity> e = (ArrayList)session.loadAll(Entity)

        println(e)

        JsonSlurper slurper = new JsonSlurper()
        Map result = (Map) slurper.parseText(json)
        ArrayList relationships = (ArrayList) result.relationships

        ArrayList<Map> ld = new ArrayList<>()
        ArrayList<Long> ids = new ArrayList<>()

        for(int i = 0; i< relationships.size(); i++){
            Map relationshipMap =(Map) relationships.get(i)
            Map fromNode = (Map) relationshipMap.fromNode
            Map toNode = (Map) relationshipMap.toNode
            String type = (String) relationshipMap.type

            def relation = [:]

            ArrayList types = (ArrayList) toNode.label
            String actualType
            if(types.get(0) == "Entity"){
                actualType = types.get(1)
            }else{
                actualType = types.get(0)
            }

            relation.put("@id",toNode.id)
            relation.put("@type",actualType)
            relation.put("_label",toNode.name)

            def fNode = [:]
            def tNode = [:]



            if(!ids.contains((Long)fromNode.id)){
                ids.add((Long) fromNode.id)
                fNode.put("@context","http://www.cidoc-crm.org/cidoc-crm/")

                ArrayList types2 = (ArrayList) fromNode.label
                String actualType2
                if(types2.get(0) == "Entity"){
                    actualType2 = types2.get(1)
                }else{
                    actualType2 = types2.get(0)
                }

                fNode.put("@id",fromNode.id)
                fNode.put("@type",actualType2)
                fNode.put("_label",fromNode.name)
                ArrayList<Map> properties = new ArrayList<>()
                properties.add(relation)
                fNode.put(type,properties)
                ld.add(fNode)
            }
            else{
                int j = ids.indexOf((Long) fromNode.id)
                if(ld[j].containsKey(type)){
                    ArrayList<Map> properties = (ArrayList<Map>) ld[j].get(type)
                    properties.add(relation)
                    ld[j].put(type,properties)
                }else{
                    ArrayList<Map> properties = new ArrayList<>()
                    properties.add(relation)
                    ld[j].put(type,properties)

                }
            }

            if(!ids.contains((Long)toNode.id)){
                ids.add((Long) toNode.id)
                tNode.put("@context","http://www.cidoc-crm.org/cidoc-crm/")

                ArrayList types2 = (ArrayList) toNode.label
                String actualType2
                if(types2.get(0) == "Entity"){
                    actualType2 = types2.get(1)
                }else{
                    actualType2 = types2.get(0)
                }


                tNode.put("@id",toNode.id)
                tNode.put("@type",actualType2)
                tNode.put("_label",toNode.name)
                ld.add(tNode)
            }
        }

        def jsonLd = JsonOutput.toJson(ld)

        return jsonLd


    }

     String getJsonLd(){
        Session session = getNeo4jSession()
        String json = jsonQuery(session)
        json = json.substring(1,json.size())
        String jsonLd = jsonToJsonLd(session,json)
        return jsonLd
    }



    static private void loadApocalipse (Session session) {
        Transaction txn = session.beginTransaction()
        E22_E33 e22E33 = new E22_E33()
        E22_E33 e22E33_2 = new E22_E33()

        E84_E33 e84E33 = new E84_E33()

        E22_E38 e22E38 = new E22_E38()

        E55_Type e55 = new E55_Type()
        E55_Type e55_2 = new E55_Type()
        E55_Type e55_3 = new E55_Type()
        E55_Type e55_4 = new E55_Type()


        E35_Title e35 = new E35_Title()
        E35_Title e35_2 = new E35_Title()
        E35_Title e35_3 = new E35_Title()
        E35_Title e35_4 = new E35_Title()

        E33_Linguistic_Object e33 = new E33_Linguistic_Object()

        E28_Conceptual_Object e28 = new E28_Conceptual_Object()

        E7_Activity e7  = new E7_Activity()

        e22E33.setName("Record Set")
        e22E33_2.setName("Record Set")

        e84E33.setName("Record")

        e22E38.setName("Miniature")

        e55.setName("Fonds")
        e55_2.setName("Sub-group")
        e55_3.setName("Item")
        e55_4.setName("Copy")

        e35.setName("Monastery of Lorvao")
        e35_2.setName("Scriptorium")
        e35_3.setName("Apocalypse of Lorvao")
        e35_4.setName("The Harvest and the vintage")

        e33.setName("Commentarium in Apocalypsin")

        e28.setName("Revelation 14:14-20")

        e7.setName("Harvesting")

        e22E33.p2_has_type.add(e55)
        e22E33.p102_has_title.add(e35)

        e22E33_2.p46_is_composed_of.add(e22E33)
        e22E33_2.p106_is_composed_of.add(e22E33)
        e22E33_2.p2_has_type.add(e55_2)
        e22E33_2.p102_has_title.add(e35_2)

        e84E33.p46_is_composed_of.add(e22E33_2)
        e84E33.p106_is_composed_of.add(e22E33_2)
        e84E33.p46_is_composed_of.add(e22E38)
        e84E33.p106_is_composed_of.add(e22E38)
        e84E33.p130_shows_features_of.add(e33)
        e84E33.p2_has_type.add(e55_4)
        e84E33.p2_has_type.add(e55_3)
        e84E33.p102_has_title.add(e35_3)

        e22E38.p102_has_title.add(e35_4)
        e22E38.p62_depicts.add(e28)
        e22E38.p62_depicts.add(e7)

        session.save(e22E33)
        session.save(e22E33_2)
        session.save(e84E33)
        session.save(e22E38)
        session.save(e55)
        session.save(e55_2)
        session.save(e55_3)
        session.save(e55_4)
        session.save(e35)
        session.save(e35_2)
        session.save(e35_3)
        session.save(e35_4)
        session.save(e28)
        session.save(e7)


        txn.commit()




    }

    static private void loadApArchive(Session session){
        Transaction txn = session.beginTransaction()

        E55_Type e55 = new E55_Type()
        E55_Type e55_2 = new E55_Type()
        E55_Type e55_3 = new E55_Type()
        E55_Type e55_4 = new E55_Type()

        E12_Production e12 = new E12_Production()

        E10_Transfer_of_Custody e10 = new E10_Transfer_of_Custody()

        E84_E33 e84E33 = new E84_E33()

        E35_Title e35 = new E35_Title()

        E52_Time_Span e52 = new E52_Time_Span()
        E52_Time_Span e52_2 = new E52_Time_Span()

        E40_Legal_Body e40 = new E40_Legal_Body()
        E40_Legal_Body e40_2 = new E40_Legal_Body()

        E21_Person e21 = new E21_Person()
        E21_Person e21_2 = new E21_Person()

        E41_Appellation e41 = new E41_Appellation()
        E41_Appellation e41_2 = new E41_Appellation()
        E41_Appellation e41_3 = new E41_Appellation()

        E42_Identifier e42 = new E42_Identifier()

        E74_Group e74 = new E74_Group()

        PC14_Carried_Out_By pc14 = new PC14_Carried_Out_By()
        PC14_Carried_Out_By pc14_2 = new PC14_Carried_Out_By()

        E54_Dimension e54 = new E54_Dimension()
        Xsd_String xsd_string = new Xsd_String()
        Xsd_Integer xsd_integer = new Xsd_Integer()

        Xsd_Date xsd_date = new Xsd_Date()

        Date date = new Date(1996,03,31)
        e54.setName("Dimension Test")
        xsd_integer.setName(1.toString())
        xsd_string.setName("Test")
        xsd_date.setName(date.toString())

        e55.setName("Information dessimination")
        e55_2.setName("Preserving information")
        e55_3.setName("Creator")
        e55_4.setName("Material author")

        e12.setName("Production of Apocalipse do Lorvão")
        e10.setName("Transfer of Apocalipse do Lorvão")

        e84E33.setName("Record")

        e35.setName("Apocalipse do Lorvão")

        e52.setName("31-12-1189")
        e52_2.setName("31-12-1853")

        e21.setName("Person")
        e21_2.setName("Person")

        e40.setName("Corporate body")
        e40_2.setName("Corporate body")

        e41.setName("Alexandre Herculano")
        e41_2.setName("Real Arquivo da Torre do Tombo")
        e41_3.setName("Egeas")

        e42.setName("Ordem de Cister. Mosteiro de Lorvão. 878-1834")

        e74.setName("Group")

        pc14.setName("P14 Carried Out By")
        pc14_2.setName("P14 Carried Out By")


        e52.setAP14_has_date(xsd_date)
        e52_2.setAP14_has_date(xsd_date)

        e12.p21_had_general_purpose.add(e55)
        e12.p21_had_general_purpose.add(e55_2)
        e12.p108_has_produced.add(e84E33)
        e12.p4_has_time_span.add(e52)
        e12.setP3_has_note(xsd_string)

        e54.setP90_has_value(xsd_integer)

        e10.p21_had_general_purpose.add(e55_2)
        e10.p30_transferred_custody_of.add(e84E33)
        e10.p4_has_time_span.add(e52_2)
        e10.p11_had_participant.add(e21)
        e10.p29_custody_received_by.add(e40_2)
        e10.p28_custody_surrendered_by.add(e74)
        e10.p15_was_influenced_by.add(e54)

        e84E33.p102_has_title.add(e35)

        e40.p1_is_identified_by.add(e42)

        e21_2.p1_is_identified_by.add(e41_3)

        e21.p1_is_identified_by.add(e41)
        e40_2.p1_is_identified_by.add(e41_2)

        e74.p107_has_current_or_former_member.add(e40)


        pc14.p01_has_domain = e12
        pc14.p02_has_range = e40

        pc14_2.p01_has_domain = e12
        pc14_2.p02_has_range = e21_2

        pc14.p14d1_in_the_role_of = e55_3

        pc14_2.p14d1_in_the_role_of = e55_4


        //e12.p14d1(e40,e55_3)
        //e12.p14d1(e21_2,e55_4)

        session.save(e55)
        session.save(e55_2)
        session.save(e55_3)
        session.save(e55_4)
        session.save(e12)
        session.save(e10)
        session.save(e84E33)
        session.save(e35)
        session.save(e52)
        session.save(e52_2)
        session.save(e40)
        session.save(e40_2)
        session.save(e41)
        session.save(e41_2)
        session.save(e41_3)
        session.save(e42)
        session.save(e21)
        session.save(e21_2)
        session.save(e74)
        session.save(pc14)
        session.save(pc14_2)
        session.save(e54)
        session.save(xsd_string)
        session.save(xsd_integer)

        session.save(xsd_date)
        txn.commit()





    }

    static private void loadCalendario(Session session) {
        Transaction txn = session.beginTransaction()

        E22_ManMade_Object e22 = new E22_ManMade_Object()
        AE1_Level_of_Description ae1 = new AE1_Level_of_Description()
        E42_Identifier e42 = new E42_Identifier()
        E42_Identifier e42_2 = new E42_Identifier()
        E42_Identifier e42_3 = new E42_Identifier()
        E42_Identifier e42_4 = new E42_Identifier()
        E56_Language e56 = new E56_Language()
        E55_Type e55 = new E55_Type()
        E55_Type e55_2 = new E55_Type()
        E55_Type e55_3 = new E55_Type()
        E55_Type e55_4 = new E55_Type()
        E35_Title e35 = new E35_Title()
        Xsd_Date xsd = new Xsd_Date()
        Xsd_String xsd_2 = new Xsd_String()
        Xsd_String xsd_3 = new Xsd_String()
        Xsd_String xsd_4 = new Xsd_String()
        Xsd_String xsd_5 = new Xsd_String()
        Xsd_String xsd_6 = new Xsd_String()
        Xsd_String xsd_7 = new Xsd_String()
        Xsd_Date xsd_8 = new Xsd_Date()
        Xsd_Date xsd_9 = new Xsd_Date()
        Xsd_String xsd_10 = new Xsd_String()
        E52_Time_Span e52 = new E52_Time_Span()
        E52_Time_Span e52_2 = new E52_Time_Span()
        E52_Time_Span e52_3 = new E52_Time_Span()
        E12_Production e12 = new E12_Production()

        e22.setName("Calendario Gregoriano")
        ae1.setName("Documento Simples")
        e42.setName("PT/TT/LO/003/3/036")
        e55.setName("Codigo de Referencia")
        e56.setName("Portugues")
        e42_2.setName("Armario 11 da Casa da Coroa")
        e55_2.setName("Cota Original")
        e42_3.setName('Leis e ordenações, Leis, mç. 3, n.º 36')
        e42_4.setName('Gavetas, Gav. 2, mç. 9, n.º 28')
        e55_3.setName("Cota Atual")
        e55_4.setName("Cota Antiga")
        e35.setName("Lei de Adopcao do calendario Gregoriano")

        e52.setName("E52_Time_Span")
        e52_2.setName("E52_Time_Span")
        e52_3.setName("E52_Time_Span")

        xsd.setName("1582-09-20")
        xsd_2.setName("Titulo atribuído.ttonline_tesouros_leis")
        xsd_3.setName("O calendário de Júlio César atribuía ao ano a duração de 365 dias e 6 horas, as quais, ao fim de 4 anos, formavam um dia que se intercalava a seguir a 24 de Fevereiro que era o 6º das calendas de Março, repetindo-se esse dia, ou seja, repetia-se o 6º das calendas: ficava um bissexto mas este não era exactamente o tempo do curso do sol. O calendário medieval estava baseado na Bíblia e nos concílios e dificilmente se consideraria que precisasse de ser melhorado. Por isso durante 4 séculos se pensou fazer a necessária reforma, que foi sucessivamente adiada, até que ela se tornou uma realidade. A correcção foi feita pelo matemático Lílio, e consistiu em avançar 10 dias a seguir ao dia 4 de Outubro de 1582, contando-se o dia seguinte como dia 15, e contando como anos bissextos os seculares apenas de 400 em 400 anos: depois da reforma o primeiro ano secular bissexto foi 1600 e o segundo o de 2000. A reforma de Gregório XIII foi publicada pela bula \"Inter gravissimas\" de 24 de Fevereiro de 1582, e dirige-se à Igreja e sua estrutura, ao Imperador Rodolfo, do Império Germânico, e a todos os chefes de Estado cristãos, ou seja, o papa no plano espiritual é a autoridade suprema, e no plano temporal é o rei, mas o papa pode pedir ao rei a aceitação de uma decisão sua, e o rei intervir na organização da Igreja, por exemplo, na nomeação dos bispos. A demora na execução da reforma não se deveu a atraso científico, mas à ponderação das suas consequências na unidade dos cristãos. Como resultado directo que era do Concílio de Trento, o calendário gregoriano provocou uma fractura imediata: os países católicos aceitaram o novo calendário no mesmo ano, o que não aconteceu nos países das diferentes confissões cristãs. Os cantões protestantes da Suiça foram dos mais irredutíveis, e só a ponderação de que a não aceitação do novo calendário os afastava das grandes correntes económicas da Europa e dificultava o comércio e as comunicações fez com que pouco a pouco esses cantões, comunas e outros estados reformados o aceitassem, já em pleno séc. XIX. A Rússia em 1918 e finalmente a Turquia em 1927 aderiram ao calendário vigente. A lei foi publicada em Lisboa a 20 de Setembro de 1582. Tipologia e suporte: Documento impresso.")
        xsd_4.setName("CAPPELLI, Adrien, Cronologia, cronografia e calendario perpetuo dal principio dell'éra cristiana ai nostri giorni: tavole cronologico-sincrone e quadri sinottici per verificare le date storiche / A. Cappelli. 6ª ed. aggiornata . - Milano : Ulrico Hoepli, 1988." +
                "De temps en temps. Histoires de Calendriers. Centre Historique Des Archives Nationales. Ed. Tallandier. Paris:2001 Documento publicado em “As gavetas da Torre do Tombo: edição digital”. Vol. 1: (GAV. 1-2), entrada 545, p. 887 a 889.")
        xsd_5.setName("1 doc. impresso (315 x 222 mm.)")
        xsd_6.setName("Relação sucessora: Portugal, Torre do Tombo, Reforma das Gavetas, liv. 6, f. 63 v.")
        xsd_7.setName("papel")
        xsd_8.setName("24/3/2015")
        xsd_9.setName("31/1/2008")
        e12.setName("Production")


        e52.setAP16_has_production_date(xsd)
        e52_2.setAP17_has_last_modification(xsd_8)
        e52_3.setAP15_has_date_of_description(xsd_9)


        e12.p108_has_produced.add(e22)
        e12.p4_has_time_span.add(e52)
        e52.setAP16_has_production_date(xsd)

        e22.getP102_has_title()
        e22.p2_has_type.add(ae1)
        e22.p1_is_identified_by.add(e42)
        e22.getAP12_has_level_of_description().add(ae1)
        e22.p1_is_identified_by.add(e42_2)
        e22.p1_is_identified_by.add(e42_3)
        e22.p1_is_identified_by.add(e42_4)
        e22.p102_has_title.add(e35)

        e22.p3_has_note = xsd_2
        e22.setAP3_has_scope(xsd_3)
        e22.setAP6_has_publication_note(xsd_4)
        e22.setAP10_has_dimensions(xsd_5)
        e22.setAP7_has_publication_note(xsd_6)
        e22.setAP11_has_materials(xsd_7)

        e42.p2_has_type.add(e55)
        e42_2.p2_has_type.add(e55_2)
        e42_3.p2_has_type.add(e55_3)
        e42_4.p2_has_type.add(e55_4)

        session.save(e22)
        session.save(ae1)
        session.save(e42)
        session.save(e42_2)
        session.save(e42_3)
        session.save(e42_4)
        session.save(e56)
        session.save(e55)
        session.save(e55_2)
        session.save(e55_3)
        session.save(e55_4)
        session.save(e35)
        session.save(xsd)
        session.save(xsd_2)
        session.save(xsd_3)
        session.save(xsd_4)
        session.save(xsd_5)
        session.save(xsd_6)
        session.save(xsd_7)
        session.save(xsd_8)
        session.save(xsd_9)
        session.save(e52)
        session.save(e52_2)
        session.save(e52_3)
        session.save(e12)

        txn.commit()



    }

    static private Iterable<Entity> queryForTernary(Session session){

        String cypher = "MATCH (h)-[:P14_1_in_the_role_of]->(w:E55_Type), (t)-[:P14_1_in_the_role_of]->(w:E55_Type), (h)-[:P14_carried_out_by]->(t) return h,w,t"
        return session.query(Entity.class,cypher,new HashMap<>(1))


    }

    static private Iterable<Entity> queryTest(Session session){

        String cypher = "MATCH (h)-[:P4_has_time_span]->(w) return h,w,t"
        return session.query(Entity.class,cypher,new HashMap<>(1))


    }

    static private Iterable<Entity> queryAll(Session session){

        String cypher = "match(n:PC14_Carried_Out_By)-[]->(s),(n:PC14_Carried_Out_By)-[]->(t),(t)-[:P1_is_identified_by]->(m) return n,s,t,m"
        return session.query(Entity.class,cypher,new HashMap<>(1))


    }

    static private Iterable<Entity> query1(Session session){

        String cypher = "MATCH (n:E12_Production)-[:P4_has_time_span]->(o)  , (n)-[:P21_had_general_purpose]->(p) return n,o,p"
        return session.query(Entity.class,cypher,new HashMap<>(1))


    }
    static private Iterable<Entity> query2(Session session){

        String cypher = "MATCH (n:E10_Transfer_of_Custody)-[:P28_custody_surrendered_by]->(o)  , (o)-[:P107_has_current_or_former_member]->(p), (p)-[:P1_is_identified_by]->(q),  (n)-[:P29_custody_received_by]->(r), (r)-[s]->(t), (n)-[:P4_has_time_span]->(v) return n,o,p,q,r,t,v"
        return session.query(Entity.class,cypher,new HashMap<>(1))


    }

    static private Iterable<Entity> query3(Session session){

        String cypher = "MATCH (n)-[m]->(o)  , (n)-[:P2_has_type]->(p) where o.name = 'Apocalypse of Lorvao' return n,o,p"
        return session.query(Entity.class,cypher,new HashMap<>(1))


    }

    static private Iterable<Entity> query4(Session session){

        String cypher = "MATCH (n)-[m]->(o)  , (n)-[p]->(q), (q)-[r]->(s) where o.name = 'Apocalypse of Lorvao' AND q.name = 'Miniature' return n,o,q,s"
        return session.query(Entity.class,cypher,new HashMap<>(1))


    }

    static private Iterable<Entity> query5(Session session){

        String cypher = "MATCH (n)-[m]->(o)  , (n)-[p]->(q), (q)-[r]->(s), (s)-[:P2_has_type]->(u), (s)-[t]->(v) where o.name = 'Apocalypse of Lorvao' AND u.name = 'Fonds' return n,o,q,s,u,v"
        return session.query(Entity.class,cypher,new HashMap<>(1))


    }

    public Iterable<Entity> query6(Session session,String resourceName ){

        String cypher = "MATCH (n:" + resourceName + ")-[m]->(o)  , (n)-[p]->(q) RETURN n,p,q"
        return session.query(Entity.class,cypher,new HashMap<>(1))


    }

    static private String jsonQuery(Session session){
        Collection<Entity> entities = session.loadAll(Entity)

        String entityName = entities[0].name

        String cypher = "MATCH (n) \n" +
                "WHERE n.name = \"" + entityName + "\"\n" +
                "CALL apoc.path.subgraphAll(n, {}) YIELD nodes, relationships\n" +
                "WITH [node in nodes | node {.*, id:id(node), label:labels(node)}] as nodes, \n" +
                "     [rel in relationships | rel {.*, type:apoc.rel.type(rel), fromNode:{label:labels(startNode(rel)), name:startNode(rel).name, id:id(startNode(rel))}, toNode:{label:labels(endNode(rel)), name:endNode(rel).name, id:id(endNode(rel))}}] as rels\n" +
                "WITH {nodes:nodes, relationships:rels} as json\n" +
                "RETURN apoc.convert.toJson(json)"
        return session.query(String.class,cypher,new HashMap<String, Object>(1))
    }


}
