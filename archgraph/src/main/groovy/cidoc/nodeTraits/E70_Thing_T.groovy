package cidoc.nodeTraits

import cidoc.nodeEntities.Xsd_String
import groovy.transform.CompileStatic
import org.neo4j.ogm.annotation.Relationship

@CompileStatic
trait E70_Thing_T implements E77_Persistent_Item_T{

    @Relationship(type="P130_shows_features_of")
    ArrayList<E70_Thing_T> P130_shows_features_of = new ArrayList<>()

    ArrayList<E70_Thing_T> getP130(){
        return P130_shows_features_of
    }

    @Relationship(type="P43_has_dimension")
    ArrayList<E54_Dimension_T> P43_has_dimension = new ArrayList<>()

    ArrayList<E54_Dimension_T> getP43(){
        return P43_has_dimension
    }

    @Relationship(type="AP10_has_dimensions")
    Xsd_String AP10_has_dimensions

    Xsd_String getAP10(){
        return AP10_has_dimensions
    }

    void setAP10(Xsd_String ap10){
        AP10_has_dimensions = ap10
    }

}