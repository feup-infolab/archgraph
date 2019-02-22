package cidoc


import cidoc.nodeEntities.E41_Appellation
import cidoc.nodeEntities.E52_Time_Span
import cidoc.nodeEntities.E53_Place
import cidoc.nodeEntities.E5_Event
import groovy.transform.TypeChecked
import org.neo4j.ogm.session.Session
import org.neo4j.ogm.config.Configuration
import org.neo4j.ogm.session.SessionFactory
import org.neo4j.ogm.transaction.Transaction

@TypeChecked
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

        load(session)

    }

    private void load (Session session) {
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
}
