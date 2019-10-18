import com.syncleus.ferma.DefaultClassInitializer
import com.syncleus.ferma.DelegatingFramedGraph
import com.syncleus.ferma.FramedGraph
import com.syncleus.ferma.ext.orientdb.impl.OrientTransactionFactoryImpl
import com.syncleus.ferma.tx.TxFactory
import edges.P2_has_type
import groovy.transform.CompileStatic
import nodeTraits.E1_CRM_Entity_T
import nodeTraits.E55_Type_T
import org.apache.tinkerpop.gremlin.orientdb.OrientGraph
import org.apache.tinkerpop.gremlin.orientdb.OrientGraphFactory
import org.apache.tinkerpop.gremlin.process.traversal.Traverser
import org.apache.tinkerpop.gremlin.process.traversal.dsl.graph.GraphTraversalSource
import org.apache.tinkerpop.gremlin.process.traversal.step.filter.HasStep
import org.apache.tinkerpop.gremlin.structure.Graph
import org.apache.tinkerpop.gremlin.tinkergraph.structure.TinkerGraph

@CompileStatic
class Loader {

    public static void testAnnotatedTyping() {


        Set<Class<?>> types = new HashSet<Class<?>>(Arrays.asList(
                E1_CRM_Entity_T.class,
                E55_Type_T.class,
                P2_has_type.class));

        Graph graph = TinkerGraph.open()
        FramedGraph fd = new DelegatingFramedGraph(graph,true,types)
        E1_CRM_Entity_T e1 = (E1_CRM_Entity_T) fd.addFramedVertex(E1_CRM_Entity_T.class as Class<Object>)
        E55_Type_T e55 = (E55_Type_T) fd.addFramedVertex(E55_Type_T.class as Class<Object>)
        e1.setName("E1")
        e55.setName("E55")
        e1.addHasType(e55, new DefaultClassInitializer(P2_has_type.class))

        GraphTraversalSource g = graph.traversal()
        E1_CRM_Entity_T e1Again = fd.traverse({g.V().has("name", "E1") }).next(E1_CRM_Entity_T.class)
        //List<E55_Type_T> e55Again = e1Again.getHasTypeE55()

        println(e1Again)
        //println(e55Again)


    }

    public static void testOrientdbFerma() {


        Set<Class<?>> types = new HashSet<Class<?>>(Arrays.asList(
                E1_CRM_Entity_T.class,
                E55_Type_T.class,
                P2_has_type.class));

        OrientGraphFactory graphFactory = new OrientGraphFactory("memory:tinkerpop")
        TxFactory graph = new OrientTransactionFactoryImpl(graphFactory,false,"com.syncleus.ferma.ext.orientdb.model")


        //println(e55Again)


    }

    public static void main(String[] args) {
        testAnnotatedTyping()
    }
}
