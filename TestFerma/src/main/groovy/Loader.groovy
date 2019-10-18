import com.syncleus.ferma.DefaultClassInitializer
import com.syncleus.ferma.ext.orientdb.impl.OrientTransactionFactoryImpl
import com.syncleus.ferma.tx.Tx
import com.syncleus.ferma.tx.TxAction0
import com.syncleus.ferma.tx.TxFactory
import db.DBConnection
import edges.P2_has_type
import groovy.transform.CompileStatic
import nodeTraits.E1_CRM_Entity_T
import nodeTraits.E55_Type_T
import org.apache.tinkerpop.gremlin.orientdb.OrientGraphFactory

@CompileStatic
class Loader {

    static void testAnnotatedTyping() {

        Set<Class<?>> types = new HashSet<Class<?>>(Arrays.asList(
                E1_CRM_Entity_T.class,
                E55_Type_T.class,
                P2_has_type.class))

        OrientGraphFactory graphFactory = DBConnection.databaseFactory()
        // OrientGraphFactory graphFactory = DBConnection.memoryFactory()

        TxFactory graph = new OrientTransactionFactoryImpl(graphFactory, false, "com.syncleus.ferma.ext.orientdb.model")

        try {
            Tx tx = graph.tx()
            E1_CRM_Entity_T e1 = (E1_CRM_Entity_T) tx.getGraph().addFramedVertex(E1_CRM_Entity_T.class as Class<Object>)
            E55_Type_T e55 = (E55_Type_T) tx.getGraph().addFramedVertex(E55_Type_T.class as Class<Object>)
            e1.setName("E1")
            e55.setName("E55")
            e1.addHasType(e55, new DefaultClassInitializer(P2_has_type.class))
            tx.success()
        }
        catch (Exception e)
        {
            println ("Deu asneira: " + e.getMessage())
        }

//        try (Tx tx = graph.tx()) {
//            tx.getGraph().getFramedVerticesExplicit(E1_CRM_Entity_T.class).collect {
//                (entity) -> {
//                    println("Found E1_CRM_Entity with name: " + entity)
//                }
//            }
//        }

        //println(e55Again)
        //List<E55_Type_T> e55Again = e1Again.getHasTypeE55()
    }

    static void testOrientdbFerma() {


        Set<Class<?>> types = new HashSet<Class<?>>(Arrays.asList(
                E1_CRM_Entity_T.class,
                E55_Type_T.class,
                P2_has_type.class))

        OrientGraphFactory graphFactory = DBConnection.databaseFactory()
        TxFactory graph = new OrientTransactionFactoryImpl(graphFactory,false,"com.syncleus.ferma.ext.orientdb.model")


        //println(e55Again)


    }

    static void main(String[] args) {
        testAnnotatedTyping()
    }
}
