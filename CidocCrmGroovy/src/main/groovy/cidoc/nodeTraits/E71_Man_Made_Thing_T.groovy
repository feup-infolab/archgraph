package cidoc.nodeTraits

import org.neo4j.ogm.annotation.Relationship

trait E71_Man_Made_Thing_T implements E70_Thing_T{

    @Relationship(type="P102_has_title")
    ArrayList<E35_Title_T> P102_has_title= new ArrayList<>()

    ArrayList<E35_Title_T> getP102(){
        return P102_has_title
    }

}