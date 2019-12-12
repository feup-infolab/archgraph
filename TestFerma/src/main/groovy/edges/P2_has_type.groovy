package edges

import com.syncleus.ferma.AbstractEdgeFrame
import com.syncleus.ferma.annotations.GraphElement
import com.syncleus.ferma.annotations.InVertex
import com.syncleus.ferma.annotations.OutVertex
import com.syncleus.ferma.annotations.Property
import com.syncleus.ferma.ext.AbstractInterceptingEdgeFrame
import nodeTraits.E1_CRM_Entity_T
import nodeTraits.E55_Type_T

@GraphElement
 abstract class P2_has_type extends AbstractEdgeFrame{
    @Property("name")
     abstract void setName(String name);

    @Property("name")
    abstract String getName();

    @InVertex
    abstract E55_Type_T getIn();

    @OutVertex
    abstract E1_CRM_Entity_T getOut();


}
