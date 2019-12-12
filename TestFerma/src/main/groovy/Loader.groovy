import com.syncleus.ferma.DefaultClassInitializer
import com.syncleus.ferma.DelegatingFramedGraph
import com.syncleus.ferma.FramedGraph
import com.syncleus.ferma.ext.orientdb.impl.OrientTransactionFactoryImpl
import com.syncleus.ferma.tx.Tx
import com.syncleus.ferma.tx.TxFactory
import db.DBConnection
import edges.P2_has_type
import groovy.transform.CompileStatic
import nodeTraits.E1_CRM_Entity_T
import nodeTraits.E55_Type_T
import nodes.E1_CRM_Entity
import nodes.E55_Type
import org.apache.tinkerpop.gremlin.orientdb.OrientGraphFactory

@CompileStatic
class Loader {

    static void testAnnotatedTyping() {

        Set<Class<?>> types = new HashSet<Class<?>>(Arrays.asList(
                E1_CRM_Entity.class,
                E55_Type_T.class,
                P2_has_type.class))

        OrientGraphFactory graphFactory = DBConnection.databaseFactory()
        // OrientGraphFactory graphFactory = DBConnection.memoryFactory()
        TxFactory graph = new OrientTransactionFactoryImpl(graphFactory, false, "nodes")
        try {
            FramedGraph fd = new DelegatingFramedGraph(graphFactory.getNoTx(),false,types)

            Tx tx = graph.tx()
            E1_CRM_Entity e1 = (E1_CRM_Entity) tx.getGraph().addFramedVertex(E1_CRM_Entity as Class<Object>)
            E55_Type e55 = (E55_Type) tx.getGraph().addFramedVertex(E55_Type)
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
//            tx.getGraph().getFramedVerticesExplicit(com.packageT.E1_CRM_Entity_T.class).collect {
//                (entity) -> {
//                    println("Found E1_CRM_Entity with name: " + entity)
//                }
//            }
//        }

        //println(e55Again)
        //List<com.packageT.E55_Type_T> e55Again = e1Again.getHasTypeE55()
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
