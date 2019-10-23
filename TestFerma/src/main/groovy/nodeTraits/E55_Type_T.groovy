package nodeTraits


import com.syncleus.ferma.VertexFrame
import com.syncleus.ferma.annotations.Property

trait E55_Type_T extends E1_CRM_Entity_T  implements VertexFrame{

    @Property("name")
    public abstract String getName()

    @Property("name")
    public abstract void setName(String name)

}