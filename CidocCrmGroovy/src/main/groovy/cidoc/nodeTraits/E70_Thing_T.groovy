package cidoc.nodeTraits

import org.neo4j.ogm.annotation.Relationship

trait E70_Thing_T implements E77_Persistent_Item_T{

    @Relationship(type="P130_shows_features_of")
    ArrayList<E70_Thing_T> P130_shows_features_of = new ArrayList<>()

    ArrayList<E70_Thing_T> getP130(){
        return P130_shows_features_of
    }

}