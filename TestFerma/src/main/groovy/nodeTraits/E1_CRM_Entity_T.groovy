package nodeTraits

import com.syncleus.ferma.ClassInitializer
import com.syncleus.ferma.VertexFrame
import com.syncleus.ferma.annotations.Adjacency
import com.syncleus.ferma.annotations.Incidence
import com.syncleus.ferma.annotations.Property
import org.apache.tinkerpop.gremlin.structure.Direction;
import edges.P2_has_type

trait E1_CRM_Entity_T implements VertexFrame{

    @Property("name")
    public abstract String getName()

    @Property("name")
    public abstract void setName(String name)

    @Adjacency(label="P2_has_type")
    abstract List<E55_Type_T> getHasTypeE55()

    @Incidence(label="P2_has_type")
    abstract List<P2_has_type> getHasType()

    @Incidence(label="knows", direction= Direction.OUT)
    public abstract  P2_has_type addHasType(E55_Type_T e55, ClassInitializer<? extends P2_has_type> type)

}