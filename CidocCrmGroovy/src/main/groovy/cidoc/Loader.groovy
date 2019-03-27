package cidoc

import cidoc.nodeEntities.E10_Transfer_of_Custody
import cidoc.nodeEntities.E12_Production
import cidoc.nodeEntities.E21_Person
import cidoc.nodeEntities.E22_E33
import cidoc.nodeEntities.E22_E38
import cidoc.nodeEntities.E28_Conceptual_Object
import cidoc.nodeEntities.E33_Linguistic_Object
import cidoc.nodeEntities.E35_Title
import cidoc.nodeEntities.E40_Legal_Body
import cidoc.nodeEntities.E41_Appellation
import cidoc.nodeEntities.E42_Identifier
import cidoc.nodeEntities.E52_Time_Span
import cidoc.nodeEntities.E53_Place
import cidoc.nodeEntities.E55_Type
import cidoc.nodeEntities.E5_Event
import cidoc.nodeEntities.E74_Group
import cidoc.nodeEntities.E7_Activity
import cidoc.nodeEntities.E84_E33
import cidoc.nodeEntities.Entity
import cidoc.nodeEntities.PC14_Carried_Out_By
import cidoc.relationshipEntities.P14_was_carried_out_by
import org.neo4j.ogm.cypher.Filter
import org.neo4j.ogm.cypher.Filters
import org.neo4j.ogm.session.Session
import org.neo4j.ogm.config.Configuration
import org.neo4j.ogm.session.SessionFactory
import org.neo4j.ogm.transaction.Transaction

//@TypeChecked
class Loader {

    private final SessionFactory sessionFactory

    static private final String SERVER_URI = "bolt://localhost:11001"
    static private final String SERVER_USERNAME = "neo4j"
    static private final String SERVER_PASSWORD = "password"


    Loader() {
        Configuration configuration = new Configuration.Builder().uri(SERVER_URI).credentials(SERVER_USERNAME, SERVER_PASSWORD).build()
        sessionFactory = new SessionFactory(configuration, "cidoc.nodeEntities","cidoc.relationshipEntities")
    }

    void process () {
        Session session = sessionFactory.openSession()
        session.purgeDatabase()

        //loadApocalipse(session)
        loadApArchive(session)

        //Iterable<Entity> en = queryTest(session)
        //Iterable<Entity> en2 = queryForTernary(session)
        //Iterable<Entity> en3 = queryAll(session)
        //int t = en.size()
        //int t2 = en2.size()
        //int t3 = en3.size()

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
        pc14.p14_1 = e55_3

        pc14_2.p01 = e12
        pc14_2.p02 = e21_2
        pc14_2.p14_1 = e55_4




        //e12.p14_1(e40,e55_3)
        //e12.p14_1(e21_2,e55_4)

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

    static private Iterable<Entity> queryForTernary(Session session){

        String cypher = "MATCH (h)-[:P14_1_in_the_role_of]->(w:E55_Type), (t)-[:P14_1_in_the_role_of]->(w:E55_Type), (h)-[:P14_carried_out_by]->(t) return h,w,t"
        return session.query(Entity.class,cypher,new HashMap<>(1))


    }

    static private Iterable<Entity> queryTest(Session session){

        String cypher = "MATCH (h)-[:P4_has_time_span]->(w) return h,w,t"
        return session.query(Entity.class,cypher,new HashMap<>(1))


    }

    static private Iterable<Entity> queryAll(Session session){

        String cypher = "MATCH (n) return n"
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


}
