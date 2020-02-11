package cidoc.nodeTraits

import groovy.transform.CompileStatic
import org.neo4j.ogm.annotation.Relationship

@CompileStatic
trait E33_Linguistic_Object_T implements E73_Information_Object_T{

    @Relationship(type="P72_has_language")
    ArrayList<E56_Language_T> P72_has_language = new ArrayList<>()

    ArrayList<E56_Language_T> getP72_has_language(){
        return P72_has_language
    }

    static Object P72_has_language_t = E56_Language_T.class


}