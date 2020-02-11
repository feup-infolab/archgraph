package cidoc.nodeTraits

import groovy.transform.CompileStatic


@CompileStatic
trait E24_Physical_ManMade_Thing_T implements E18_Physical_Thing_T,E71_Man_Made_Thing_T{


    ArrayList<E1_CRM_Entity_T> P62_depicts = new ArrayList<>()

    ArrayList<E1_CRM_Entity_T> getP62_depicts(){
        return P62_depicts
    }

    static Object P62_depicts_t = E1_CRM_Entity_T.class




}