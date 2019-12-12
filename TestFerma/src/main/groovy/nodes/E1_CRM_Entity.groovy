package nodes


import com.syncleus.ferma.ClassInitializer
import com.syncleus.ferma.annotations.GraphElement
import com.syncleus.ferma.ext.AbstractInterceptingVertexFrame
import edges.P2_has_type
import nodeTraits.E1_CRM_Entity_T
import nodeTraits.E55_Type_T

@GraphElement
public class E1_CRM_Entity extends AbstractInterceptingVertexFrame implements E1_CRM_Entity_T{
    @Override
    String getName() {
        return null
    }

    @Override
    void setName(String name) {

    }

    @Override
    List<E55_Type_T> getHasTypeE55() {
        return null
    }

    @Override
    List<P2_has_type> getHasType() {
        return null
    }

    @Override
    P2_has_type addHasType(E55_Type_T e55, ClassInitializer<? extends P2_has_type> type) {
        return null
    }
}
