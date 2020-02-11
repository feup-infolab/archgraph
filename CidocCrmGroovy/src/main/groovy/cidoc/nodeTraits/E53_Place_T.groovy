package cidoc.nodeTraits

import groovy.transform.CompileStatic
import org.neo4j.ogm.annotation.Relationship

@CompileStatic
trait E53_Place_T implements E1_CRM_Entity_T{

    @Relationship(type="P87_is_identified_by")
    private ArrayList<E41_Appellation_T> P87_is_identified_by = new ArrayList<>()

    ArrayList<E41_Appellation_T> getP87_is_identified_by(){
        return P87_is_identified_by
    }

    static Object P87_is_identified_by_t = E41_Appellation_T.class


}