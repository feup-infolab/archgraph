package cidoc.nodeTraits

import org.neo4j.ogm.annotation.Relationship

trait E18_Physical_Thing_T implements E72_Legal_Object_T{

    @Relationship(type="P46_is_composed_of")
    ArrayList<E18_Physical_Thing_T> P46_is_composed_of = new ArrayList<>()

    ArrayList<E18_Physical_Thing_T> getP46(){
        return P46_is_composed_of
    }

}