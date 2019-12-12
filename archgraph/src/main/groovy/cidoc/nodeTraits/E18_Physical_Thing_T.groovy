package cidoc.nodeTraits

import cidoc.nodeEntities.Xsd_String
import groovy.transform.CompileStatic
import org.neo4j.ogm.annotation.Relationship

@CompileStatic
trait E18_Physical_Thing_T implements E72_Legal_Object_T, E92_Spacetime_Volume_T{

    @Relationship(type="P45_consists_of")
    ArrayList<E57_Material_T> P45_consists_of = new ArrayList<>()

    ArrayList<E57_Material_T> getP45(){
        return P45_consists_of
    }

    @Relationship(type="P46_is_composed_of")
    ArrayList<E18_Physical_Thing_T> P46_is_composed_of = new ArrayList<>()

    ArrayList<E18_Physical_Thing_T> getP46(){
        return P46_is_composed_of
    }

    @Relationship(type="AP11_has_materials")
    Xsd_String AP11_has_materials

    Xsd_String getAP11(){
        return AP11_has_materials
    }

    void setAP11(Xsd_String ap11){
        AP11_has_materials = ap11
    }

}