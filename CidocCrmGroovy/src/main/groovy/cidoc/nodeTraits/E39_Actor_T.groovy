package cidoc.nodeTraits

import cidoc.nodeEntities.E55_Type
import org.neo4j.ogm.annotation.Relationship

trait E39_Actor_T implements E77_Persistent_Item_T{


    @Relationship(type = "P14_1_in_the_role_of")
    ArrayList<E55_Type> P14_1_in_the_role_of = new ArrayList<>()

    ArrayList<E55_Type> getP14_1(){
        return P14_1_in_the_role_of
    }
}