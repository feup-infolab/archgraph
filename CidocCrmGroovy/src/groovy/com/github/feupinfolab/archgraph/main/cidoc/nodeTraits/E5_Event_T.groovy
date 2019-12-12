package cidoc.nodeTraits

import groovy.transform.CompileStatic


@CompileStatic
trait E5_Event_T implements E4_Period_T{

    
    ArrayList<E39_Actor_T> P11_had_participant = new ArrayList<>()

    ArrayList<E39_Actor_T> getP11_had_participant(){
        return P11_had_participant
    }

    static Object P11_had_participant_t = E39_Actor_T.class

}