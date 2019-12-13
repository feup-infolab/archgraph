package cidoc.nodeTraits

import groovy.transform.CompileStatic
import org.neo4j.ogm.annotation.Relationship


@CompileStatic
trait E4_Period_T implements E2_Temporal_Entity_T{

    @Relationship(type = "P9_consists_of")
    private ArrayList<E4_Period_T> P9_consists_of = new ArrayList<>()

    @Relationship(type = "P7_took_place_at")
    private ArrayList<E53_Place_T> P7_took_place_at = new ArrayList<>()

    ArrayList<E53_Place_T> getP7_took_place_at(){
        return P7_took_place_at
    }

    ArrayList<E4_Period_T> getP9_consists_of(){
        return P9_consists_of
    }

    static Object P7_took_place_at_t = E53_Place_T.class
    static Object P9_consists_of_t = E4_Period_T.class




}