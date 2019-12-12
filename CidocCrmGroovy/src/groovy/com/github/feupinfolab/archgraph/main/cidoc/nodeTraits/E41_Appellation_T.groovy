package cidoc.nodeTraits

import groovy.transform.CompileStatic


@CompileStatic
trait E41_Appellation_T implements E90_Symbolic_Object_T{

    
    private ArrayList<E41_Appellation_T> P139_has_alternative_form = new ArrayList<>()


    ArrayList<E41_Appellation_T> getP139_has_alternative_form() {
        return P139_has_alternative_form
    }

    static Object P139_has_alternative_form_t = E41_Appellation_T.class


}