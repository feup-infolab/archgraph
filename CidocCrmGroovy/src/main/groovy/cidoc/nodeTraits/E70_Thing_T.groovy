package cidoc.nodeTraits

import cidoc.nodeEntities.Xsd_String
import groovy.transform.CompileStatic


@CompileStatic
trait E70_Thing_T implements E77_Persistent_Item_T{

    
    ArrayList<E70_Thing_T> P130_shows_features_of = new ArrayList<>()

    ArrayList<E70_Thing_T> getP130_shows_features_of(){
        return P130_shows_features_of
    }

    static Object P130_shows_features_of_t = E70_Thing_T.class

    
    ArrayList<E54_Dimension_T> P43_has_dimension = new ArrayList<>()

    ArrayList<E54_Dimension_T> getP43_has_dimension(){
        return P43_has_dimension
    }


    static Object P43_has_dimension_t = E54_Dimension_T.class


    
    Xsd_String AP10_has_dimensions

    Xsd_String getAP10_has_dimensions(){
        return AP10_has_dimensions
    }

    void setAP10_has_dimensions(Xsd_String ap10){
        AP10_has_dimensions = ap10
    }

}