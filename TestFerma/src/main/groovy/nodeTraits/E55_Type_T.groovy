package nodeTraits

import com.syncleus.ferma.AbstractVertexFrame
import com.syncleus.ferma.VertexFrame
import com.syncleus.ferma.annotations.Adjacency
import com.syncleus.ferma.annotations.Incidence
import com.syncleus.ferma.annotations.Property
import edges.P2_has_type

trait E55_Type_T  extends E1_CRM_Entity_T  implements VertexFrame{

    @Property("name")
    public abstract String getName()

    @Property("name")
    public abstract void setName(String name)

}