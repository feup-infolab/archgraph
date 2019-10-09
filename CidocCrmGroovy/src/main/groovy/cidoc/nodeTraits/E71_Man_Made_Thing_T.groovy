package cidoc.nodeTraits

import groovy.transform.CompileStatic


@CompileStatic
trait E71_Man_Made_Thing_T implements E70_Thing_T{

    
    ArrayList<E35_Title_T> P102_has_title= new ArrayList<>()

    ArrayList<E35_Title_T> getP102_has_title(){
        return P102_has_title
    }


    static Object P102_has_title_t = E35_Title_T.class

}