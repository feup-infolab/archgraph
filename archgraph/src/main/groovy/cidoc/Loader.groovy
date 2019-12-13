package cidoc

import cidoc.nodeEntities.*
import groovy.json.JsonSlurper
import org.neo4j.ogm.config.Configuration
import org.neo4j.ogm.session.Session
import org.neo4j.ogm.session.SessionFactory
import org.neo4j.ogm.transaction.Transaction
import org.neo4j.ogm.config.Configuration

class Loader {



    static private final String SERVER_URI = "bolt://localhost:11001"
    static private final String SERVER_USERNAME = "neo4j"
    static private final String SERVER_PASSWORD = "password"

    static private Configuration configuration =  new Configuration.Builder().uri(SERVER_URI).credentials(SERVER_USERNAME, SERVER_PASSWORD).build()
    private final SessionFactory sessionFactory = new SessionFactory(configuration, "cidoc.nodeEntities")
    private static Loader factory = new Loader()


    void process () {
        Session session = getNeo4jSession()
        session.purgeDatabase()

        loadApocalipse(session)
        //loadApArchive(session)
        //String json = jsonQuery(session)
        //println(json)
        //json = json.substring(1,json.size())
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

    public static Loader getInstance() {
        return factory
    }


    private Loader() {
    }

    Session getNeo4jSession() {
        return sessionFactory.openSession()
    }

     private Entity findById(ArrayList<Entity> entities, String name){
         for(int i = 0; i<entities.size(); i++){
             if(name == entities.get(i).name){
                 return entities.get(i)
             }
         }
     }

    int countEntities(){
        Collection<Entity> results = sessionFactory.openSession().loadAll(Entity)
        return results.size()

    }

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
            String typeMin = type.substring(0, type.indexOf("_"))
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

    static private void addEntity(Entity e, Session session){
        Transaction txn = session.beginTransaction()
        session.save(e)
        txn.commit()

    }

    static private void loadFEUP(Session session){
        Transaction txn = session.beginTransaction()

        E52_Time_Span e52= new E52_Time_Span()
        E52_Time_Span e52_2= new E52_Time_Span()
        E52_Time_Span e52_3= new E52_Time_Span()
        E5_Event e5 = new E5_Event()
        E5_Event e5_2 = new E5_Event()
        E53_Place e53 = new E53_Place()
        E41_Appellation e41 = new E41_Appellation()
        E41_Appellation e41_3 = new E41_Appellation()
        E41_Appellation e41_2 = new E41_Appellation()


        e5.setName("Construction of Feup")
        e5_2.setName("Laying of the First Stone in FEUP")
        e53.setName("The extent of the Campus of FEUP")
        e41.setName("FEUP")
        e41_2.setName("41.1779° N, 8.5977° W")
        e41_3.setName("s/n, R. Dr. Roberto Frias, 4200-465 Porto")
        e52.setName("27-09-1996")
        e52_2.setName("22-03-2001")
        e52_3.setName("From 27-09-1996 to 22-03-2001")


        e5.p4.add(e52_3)
        e5.p9.add(e5_2)
        e5.p7.add(e53)
        e5_2.p4.add(e52)
        e52.p86.add(e52_3)
        e52_2.p86.add(e52_3)
        e53.p87.add(e41)
        e41.p139.add(e41_2)
        e41.p139.add(e41_3)

        session.save(e52)
        session.save(e52_2)
        session.save(e52_3)
        session.save(e5)
        session.save(e5_2)
        session.save(e53)
        session.save(e41)
        session.save(e41_2)
        session.save(e41_3)

        txn.commit()
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

        e22E33.p2.add(e55)
        e22E33.p102.add(e35)

        e22E33_2.p46.add(e22E33)
        e22E33_2.p106.add(e22E33)
        e22E33_2.p2.add(e55_2)
        e22E33_2.p102.add(e35_2)

        e84E33.p46.add(e22E33_2)
        e84E33.p106.add(e22E33_2)
        e84E33.p46.add(e22E38)
        e84E33.p106.add(e22E38)
        e84E33.p130.add(e33)
        e84E33.p2.add(e55_4)
        e84E33.p2.add(e55_3)
        e84E33.p102.add(e35_3)

        e22E38.p102.add(e35_4)
        e22E38.p62.add(e28)
        e22E38.p62.add(e7)

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


        e12.p21.add(e55)
        e12.p21.add(e55_2)
        e12.p108.add(e84E33)
        e12.p4.add(e52)



        e10.p21.add(e55_2)
        e10.p30.add(e84E33)
        e10.p4.add(e52_2)
        e10.p11.add(e21)
        e10.p29.add(e40_2)
        e10.p28.add(e74)

        e84E33.p102.add(e35)

        e40.p1.add(e42)

        e21_2.p1.add(e41_3)

        e21.p1.add(e41)
        e40_2.p1.add(e41_2)

        e74.p107.add(e40)


        pc14.p01 = e12
        pc14.p02 = e40

        pc14_2.p01 = e12
        pc14_2.p02 = e21_2

        pc14.p14d1 = e55_3

        pc14_2.p14d1 = e55_4


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
        Xsd_String xsd = new Xsd_String()
        Xsd_String xsd_2 = new Xsd_String()
        Xsd_String xsd_3 = new Xsd_String()
        Xsd_String xsd_4 = new Xsd_String()
        Xsd_String xsd_5 = new Xsd_String()
        Xsd_String xsd_6 = new Xsd_String()
        Xsd_String xsd_7 = new Xsd_String()
        Xsd_String xsd_8 = new Xsd_String()
        Xsd_String xsd_9 = new Xsd_String()
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


        e52.setAP16(xsd)
        e52_2.setAP17(xsd_8)
        e52_3.setAP15(xsd_9)


        e12.p108.add(e22)
        e12.p4.add(e52)
        e52.setAP16(xsd)

        e22.getP102_has_title()
        e22.p2.add(ae1)
        e22.p1.add(e42)
        e22.getAP12().add(ae1)
        e22.p1.add(e42_2)
        e22.p1.add(e42_3)
        e22.p1.add(e42_4)
        e22.p102.add(e35)

        e22.p3 = xsd_2
        e22.setAP3(xsd_3)
        e22.setAP6(xsd_4)
        e22.setAP10(xsd_5)
        e22.setAP7(xsd_6)
        e22.setAP11(xsd_7)

        e42.p2.add(e55)
        e42_2.p2.add(e55_2)
        e42_3.p2.add(e55_3)
        e42_4.p2.add(e55_4)

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

    static private String jsonQuery(Session session){
        String cypher = "MATCH (n) \n" +
                "WHERE n.name = \"Production of Apocalipse do Lorvão\"\n" +
                "CALL apoc.path.subgraphAll(n, {}) YIELD nodes, relationships\n" +
                "WITH [node in nodes | node {.*, id:id(node), label:labels(node)}] as nodes, \n" +
                "     [rel in relationships | rel {.*, type:apoc.rel.type(rel), fromNode:{label:labels(startNode(rel))[1], name:startNode(rel).name, id:id(startNode(rel))}, toNode:{label:labels(endNode(rel))[1], name:endNode(rel).name, id:id(endNode(rel))}}] as rels\n" +
                "WITH {nodes:nodes, relationships:rels} as json\n" +
                "RETURN apoc.convert.toJson(json)"
        return session.query(String.class,cypher,new HashMap<String, Object>(1))
    }


}
