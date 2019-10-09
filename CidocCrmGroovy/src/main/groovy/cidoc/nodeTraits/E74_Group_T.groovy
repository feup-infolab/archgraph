package cidoc.nodeTraits

import groovy.transform.CompileStatic


@CompileStatic
trait E74_Group_T implements E39_Actor_T{

    
    private ArrayList<E39_Actor_T> P107_has_current_or_former_member = new ArrayList<>()


    ArrayList<E39_Actor_T> getP107_has_current_or_former_member() {
        return P107_has_current_or_former_member
    }


    static Object P107_has_current_or_former_member_t = E39_Actor_T.class

}