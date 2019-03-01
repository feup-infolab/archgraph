package cidoc

import cidoc.nodeEntities.E22_E33
import cidoc.nodeEntities.E22_E38
import cidoc.nodeEntities.E28_Conceptual_Object
import cidoc.nodeEntities.E33_Linguistic_Object
import cidoc.nodeEntities.E35_Title
import cidoc.nodeEntities.E41_Appellation
import cidoc.nodeEntities.E52_Time_Span
import cidoc.nodeEntities.E53_Place
import cidoc.nodeEntities.E55_Type
import cidoc.nodeEntities.E5_Event
import cidoc.nodeEntities.E7_Activity
import cidoc.nodeEntities.E84_E33
import groovy.transform.TypeChecked
import org.neo4j.ogm.session.Session
import org.neo4j.ogm.config.Configuration
import org.neo4j.ogm.session.SessionFactory
import org.neo4j.ogm.transaction.Transaction

//@TypeChecked
class Loader {

    private final SessionFactory sessionFactory

    static private final String SERVER_URI = "bolt://localhost:7687"
    static private final String SERVER_USERNAME = "neo4j"
    static private final String SERVER_PASSWORD = "password"


    Loader() {
        Configuration configuration = new Configuration.Builder().uri(SERVER_URI).credentials(SERVER_USERNAME, SERVER_PASSWORD).build()
        sessionFactory = new SessionFactory(configuration, "cidoc.nodeEntities")
    }

    void process () {
        Session session = sessionFactory.openSession()
        session.purgeDatabase()

        loadApocalipse(session)

    }

    private void loadFEUP(Session session){
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

    private void loadApocalipse (Session session) {
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
}
