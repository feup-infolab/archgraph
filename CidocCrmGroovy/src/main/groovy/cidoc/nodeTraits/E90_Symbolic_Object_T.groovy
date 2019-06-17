package cidoc.nodeTraits

import groovy.transform.CompileStatic
import org.neo4j.ogm.annotation.Relationship

@CompileStatic
trait E90_Symbolic_Object_T implements E72_Legal_Object_T, E28_Conceptual_Object_T {

    @Relationship(type="P106_is_composed_of")
    ArrayList<E90_Symbolic_Object_T> P106_is_composed_of = new ArrayList<>()

    ArrayList<E90_Symbolic_Object_T> getP106_is_composed_of(){
        return P106_is_composed_of
    }

    static Object P106_is_composed_of_t = E90_Symbolic_Object_T.class


}
