package cidoc.nodeTraits

import org.neo4j.ogm.annotation.Relationship


trait E4_Period_T implements E2_Temporal_Entity_T{

    @Relationship(type = "P9_consists_of")
    private ArrayList<E4_Period_T> P9_consists_of = new ArrayList<>()

    @Relationship(type = "P7_took_place_at")
    private ArrayList<E53_Place_T> P7_took_place_at = new ArrayList<>()

    ArrayList<E53_Place_T> getP7(){
        return P7_took_place_at
    }

    ArrayList<E4_Period_T> getP9(){
        return P9_consists_of
    }

}